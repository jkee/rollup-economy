#!/usr/bin/env python3

import copy
import importlib.util
import json
import os
import shutil
import tempfile
import unittest
from datetime import date
from unittest import mock


HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))


def load_module(name, filename):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, filename))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


campaign = load_module("v4_1_campaign_tests", "campaign_v4_1.py")
finalizer_fixtures = load_module("v4_1_finalizer_campaign_interop", "test_v4_1_finalizer.py")
gate_issuer = load_module("v4_1_gate_certificate_tests", "issue_gate_certificate_v4_1.py")


def write(path, value, raw=False):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if raw:
        with open(path, "w", encoding="utf-8") as handle:
            handle.write(value)
    else:
        with open(path, "w", encoding="utf-8") as handle:
            json.dump(value, handle, indent=2, ensure_ascii=False)
            handle.write("\n")


def write_bytes(path, value):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "wb") as handle:
        handle.write(value)


def selection(source_ids=None, caveats=None):
    result = {
        "value": 0.5,
        "source_ids": list(source_ids or ["S1"]),
        "caveats": list(caveats or []),
        "range": {"low": 0.3, "high": 0.7},
    }
    return result


def record(code, run_id, attempt=1, caveats=None):
    return {
        "naics": code,
        "title": "Synthetic Services",
        "run_meta": {"run_id": run_id, "attempt": attempt},
        "sources": [{"id": "S1", "url": "https://example.com/source"}],
        "dataset_inputs": {"n_band": selection()},
        "inputs": {
            "target_archetype": {"name": "Synthetic archetype"},
            "target_archetype_coverage": selection(),
            "target_labor_cost_share": selection(),
            "target_role_mix": {
                "roles": [{"role_id": "ROLE1", "cost_weight": 1.0,
                           "removable_fraction": selection()}],
                "caveats": [],
            },
            "implementation_ramp": {"r%d" % year: selection() for year in range(1, 6)},
            "commercial_retention": selection(caveats=caveats),
            "five_year_sale_availability": selection(),
            "buy_mult": selection(),
            "downside_exit_mult": selection(),
            "y5_survival": selection(),
        },
    }


class Fixture:
    def __init__(self, root, fleet_codes=("999999",), golden_codes=(), scope="full",
                 real_toolchain=False):
        self.root = root
        self.entries = []
        write(os.path.join(root, campaign.MEMBERSHIP_PATHS["fleet_universe"]), {"codes": [{"naics": item} for item in fleet_codes]})
        write(os.path.join(root, campaign.MEMBERSHIP_PATHS["golden_universe"]), {"codes": [{"naics": item} for item in golden_codes]})
        self.toolchain = {}
        for key in campaign.TOOLCHAIN_KEYS:
            path = campaign.TOOLCHAIN_PATHS[key]
            destination = os.path.join(root, path)
            if real_toolchain:
                os.makedirs(os.path.dirname(destination), exist_ok=True)
                shutil.copyfile(os.path.join(REPO, path), destination)
            else:
                write(destination, "frozen %s\n" % key, raw=True)
            self.toolchain[key] = campaign.artifact_ref(path, root)
        membership = {
            "fleet_universe": campaign.artifact_ref(campaign.MEMBERSHIP_PATHS["fleet_universe"], root),
            "golden_universe": campaign.artifact_ref(campaign.MEMBERSHIP_PATHS["golden_universe"], root),
            "fleet_expected": sorted(fleet_codes),
            "golden_expected": sorted(golden_codes),
            "fleet_omitted": [],
            "golden_omitted": [],
        }
        if scope == "holdout":
            destination = os.path.join(root, campaign.HOLDOUT_MEMBERSHIP_PATH)
            os.makedirs(os.path.dirname(destination), exist_ok=True)
            shutil.copyfile(os.path.join(REPO, campaign.HOLDOUT_MEMBERSHIP_PATH), destination)
            membership["holdout_membership"] = campaign.artifact_ref(
                campaign.HOLDOUT_MEMBERSHIP_PATH, root)
        membership["snapshot_sha256"] = campaign.membership_sha256(membership)
        self.manifest = {
            "manifest_version": campaign.MANIFEST_VERSION,
            "campaign_id": "synthetic-v4.1",
            "scope": scope,
            "toolchain": self.toolchain,
            "membership": membership,
            "entries": self.entries,
        }
        if scope == "full":
            certificates = {}
            for name, certificate_scope, codes, marker in (
                    ("regression_canary", "canary", campaign.CANARY_CODES, "a"),
                    ("holdout", "holdout", campaign.HOLDOUT_CODES, "b")):
                paths = campaign.FULL_GATE_PATHS[name]
                proof_entries = []
                source_entries = []
                for code in sorted(codes):
                    entry_id = "fleet:%s:proof-%s" % (code, certificate_scope)
                    research_execution = {"issued_by_task_path": "/root",
                                          "codex_task_path": "/root/proof_research_%s_%s" %
                                                             (certificate_scope, code),
                                          "fork_policy": "none", "role": "research"}
                    review_execution = {"issued_by_task_path": "/root",
                                        "codex_task_path": "/root/proof_review_%s_%s" %
                                                           (certificate_scope, code),
                                        "fork_policy": "isolated", "role": "reviewer"}
                    envelope_path = "gate-source/%s/%s-envelope.json" % (certificate_scope, code)
                    review_path = "gate-source/%s/%s-review.json" % (certificate_scope, code)
                    write(os.path.join(root, envelope_path), research_execution)
                    write(os.path.join(root, review_path), {
                        "execution": review_execution, "outcome": "publishable"})
                    review_sha = campaign.sha256(os.path.join(root, review_path))
                    proof_entries.append({
                        "entry_id": entry_id,
                        "naics": code,
                        "research_execution": research_execution,
                        "review_execution": review_execution,
                        "review_sha256": review_sha,
                        "outcome": "publishable",
                    })
                    source_entries.append({"entry_id": entry_id, "naics": code,
                                           "artifacts": {"execution_envelope": {
                                               "path": envelope_path,
                                               "sha256": campaign.sha256(os.path.join(root, envelope_path))}},
                                           "review_path": review_path})
                source_manifest = {"proof_fixture": True, "scope": certificate_scope,
                                   "entries": source_entries}
                write(os.path.join(root, paths["source"]), source_manifest)
                campaign_proof = {"proof_version": "gate-campaign-proof-4.1",
                                  "scope": certificate_scope,
                                  "source_manifest": campaign.artifact_ref(paths["source"], root),
                                  "entries": proof_entries}
                write(os.path.join(root, paths["campaign"]), campaign_proof)
                campaign_root = campaign.value_sha256(campaign_proof)
                entry_ids = sorted(item["entry_id"] for item in proof_entries)
                review_digests = dict(sorted((item["entry_id"], item["review_sha256"])
                                             for item in proof_entries))
                gate_proof = {
                    "proof_version": "gate-proof-4.1", "scope": certificate_scope,
                    "campaign_root_sha256": campaign_root, "accepted": True,
                    "selected_entry_ids": entry_ids, "review_digests": review_digests,
                    "invariant_checks": {key: True for key in campaign.INVARIANT_CHECKS},
                    "signoff": {
                        "decision": "approve", "reviewer_identity": "reviewer@rollup.local",
                        "signed_at": date.today().isoformat(), "notes": "Exact proof signoff.",
                        "selected_entry_ids": entry_ids, "review_digests": review_digests,
                        "signoff_execution": {"issued_by_task_path": "/root",
                                              "codex_task_path": "/root/proof_signoff_%s" % certificate_scope,
                                              "role": "human_signoff"},
                        "commit_sha256": campaign.value_sha256(
                            {"scope": certificate_scope, "commit": marker}),
                    },
                }
                write(os.path.join(root, paths["gate"]), gate_proof)
                certificate = {
                    "certificate_version": "gate-certificate-4.1", "scope": certificate_scope,
                    "campaign_root_sha256": campaign_root,
                    "gate_root_sha256": campaign.value_sha256(gate_proof),
                    "accepted": True, "selected_codes": sorted(codes),
                    "issued_by_task_path": "/root",
                    "codex_task_path": "/root/certify_%s" % name,
                    "issued_at": date.today().isoformat(),
                    "campaign_artifact": campaign.artifact_ref(paths["campaign"], root),
                    "gate_artifact": campaign.artifact_ref(paths["gate"], root),
                }
                certificate["certificate_binding_sha256"] = campaign.value_sha256(certificate)
                write(os.path.join(root, paths["certificate"]), certificate)
                certificates[name] = campaign.artifact_ref(paths["certificate"], root)
            self.manifest["full_gate_certificates"] = certificates

    def add(self, kind, code, run_id, attempt=1, remediates=None, caveats=None,
            predecessor_review_sha256=None):
        base = "artifacts/%s/%s" % (code, run_id)
        research_model = "gpt-5.6-terra" if kind == "fleet" else "gpt-5.6-sol"
        remediation_ref = None
        if attempt == 2:
            bundle_path = "%s/remediation.json" % base
            write(os.path.join(self.root, bundle_path), {
                "predecessor_entry_id": remediates,
                "predecessor_review_sha256": predecessor_review_sha256,
                "findings": [],
            })
            remediation_ref = campaign.artifact_ref(bundle_path, self.root)
        execution_envelope = {
            "envelope_version": "4.1", "kind": kind, "naics": code,
            "title": "Synthetic Services", "run_id": run_id, "attempt": attempt,
            "run_date": date.today().isoformat(),
            "remediates_run_id": remediates.rsplit(":", 1)[-1] if attempt == 2 and remediates else None,
            "issued_by_task_path": "/root", "codex_task_path": "/root/research_%s" % run_id,
            "model_id": research_model, "fork_policy": "none", "role": "research",
        }
        rec = record(code, run_id, attempt=attempt, caveats=caveats)
        packet = {"naics": code, "run_meta": {"run_id": run_id, "attempt": attempt}}
        dataset = {"naics": code, "title": "Synthetic Services", "aux": {"vintage": "frozen"}}
        early_values = {
            "assembled_prompt": ("prompt.md", "frozen prompt\n", True),
            "packet": ("packet.json", packet, False),
            "dataset": ("dataset.json", dataset, False),
            "industry_spec": ("industry_spec.json", {"naics": code, "title": "Synthetic Services"}, False),
        }
        artifacts = {}
        for key, (filename, value, raw) in early_values.items():
            path = "%s/%s" % (base, filename)
            write(os.path.join(self.root, path), value, raw=raw)
            artifacts[key] = campaign.artifact_ref(path, self.root)
        execution_envelope.update({
            "prompt_sha256": artifacts["assembled_prompt"]["sha256"],
            "dataset_sha256": artifacts["dataset"]["sha256"],
            "spec_sha256": artifacts["industry_spec"]["sha256"],
            "methodology_sha256": self.toolchain["methodology"]["sha256"],
            "thresholds_sha256": self.toolchain["thresholds"]["sha256"],
            "research_packet_schema_sha256": self.toolchain["packet_schema"]["sha256"],
            "dataset_schema_sha256": self.toolchain["dataset_schema"]["sha256"],
            "industry_spec_schema_sha256": self.toolchain["industry_spec_schema"]["sha256"],
            "run_record_schema_sha256": self.toolchain["run_schema"]["sha256"],
            "scoring_sha256": self.toolchain["scoring"]["sha256"],
            "finalizer_sha256": self.toolchain["finalizer"]["sha256"],
        })
        envelope_path = "%s/execution.json" % base
        write(os.path.join(self.root, envelope_path), execution_envelope)
        artifacts["execution_envelope"] = campaign.artifact_ref(envelope_path, self.root)
        rec["artifact_provenance"] = {
            "execution_envelope": execution_envelope,
            "execution_envelope_sha256": artifacts["execution_envelope"]["sha256"],
            "packet_sha256": artifacts["packet"]["sha256"],
        }
        rec["run_meta"].update({key: execution_envelope[key] for key in
                                ("model_id", "issued_by_task_path", "codex_task_path", "fork_policy")})
        for key, filename, value, raw in (
                ("record", "record.json", rec, False), ("memo", "memo.md", "frozen memo\n", True)):
            path = "%s/%s" % (base, filename)
            write(os.path.join(self.root, path), value, raw=raw)
            artifacts[key] = campaign.artifact_ref(path, self.root)
        inputs = campaign.build_input_registry(rec)
        entry = {
            "entry_id": "%s:%s:%s" % (kind, code, run_id),
            "kind": kind, "naics": code, "run_id": run_id, "attempt": attempt,
            "remediates_entry_id": remediates,
            "predecessor_review_sha256": predecessor_review_sha256,
            "remediation_bundle": remediation_ref,
            "artifacts": artifacts,
            "review_path": "reviews/%s.json" % run_id,
            "input_registry": inputs,
            "source_registry": campaign.build_source_registry(rec, inputs),
            "authored_caveats": campaign.declared_caveats(rec),
        }
        self.entries.append(entry)
        return entry

    def freeze(self):
        freeze_path = "pipeline/v4_1/freeze_manifest.synthetic.json"
        write(os.path.join(self.root, freeze_path), {"synthetic": "frozen"})
        freeze_ref = campaign.artifact_ref(freeze_path, self.root)
        freeze = {
            **freeze_ref, "root_sha256": campaign.value_sha256({"root": "synthetic"}),
            "manifest_version": "v4.1-freeze-1", "git_commit": "a" * 64,
        }
        authorization = {"root_sha256": freeze["root_sha256"],
                         "manifest_sha256": freeze["sha256"], "commit_sha": freeze["git_commit"]}
        for key in ("contract", "commit_receipt", "tag_receipt", "ci_receipt"):
            path = "authorization/%s.json" % key
            write(os.path.join(self.root, path), {"kind": key, "valid": True})
            ref = campaign.artifact_ref(path, self.root)
            ref["byte_length"] = os.path.getsize(os.path.join(self.root, path))
            authorization[key] = ref
        plan_entries = []
        for entry in self.entries:
            envelope = campaign.load_json(os.path.join(
                self.root, entry["artifacts"]["execution_envelope"]["path"]))
            def with_length(ref):
                result = dict(ref)
                result["byte_length"] = os.path.getsize(os.path.join(self.root, ref["path"]))
                return result
            planned = {
                "entry_id": entry["entry_id"], "kind": entry["kind"], "naics": entry["naics"],
                "title": "Synthetic Services", "run_id": entry["run_id"],
                "run_date": envelope["run_date"], "attempt": entry["attempt"],
                "remediates_run_id": envelope["remediates_run_id"],
                "research_execution": {key: envelope[key] for key in
                                       ("issued_by_task_path", "codex_task_path", "fork_policy",
                                        "role", "model_id")},
                "review_execution": {"issued_by_task_path": "/root",
                                     "codex_task_path": "/root/review_%s" % entry["run_id"],
                                     "fork_policy": "isolated", "role": "reviewer",
                                     "model_id": "gpt-5.6-sol",
                                     "prompt_version": campaign.REVIEW_PROMPT_VERSION},
                "frozen_inputs": {
                    "assembled_prompt": with_length(entry["artifacts"]["assembled_prompt"]),
                    "industry_spec": with_length(entry["artifacts"]["industry_spec"]),
                    "dataset": with_length(entry["artifacts"]["dataset"]),
                },
                "execution_envelope": with_length(entry["artifacts"]["execution_envelope"]),
                "planned_outputs": {
                    "packet": entry["artifacts"]["packet"]["path"],
                    "execution_envelope": entry["artifacts"]["execution_envelope"]["path"],
                    "record": entry["artifacts"]["record"]["path"],
                    "memo": entry["artifacts"]["memo"]["path"],
                    "review": entry["review_path"],
                },
            }
            entry["issuance_entry_sha256"] = campaign.value_sha256(planned)
            plan_entries.append(planned)
        plan = {
            "plan_version": "v4.1-pre-run-issuance-1", "campaign_id": self.manifest["campaign_id"],
            "scope": self.manifest["scope"], "issued_by_task_path": "/root",
            "run_date": date.today().isoformat(), "prompt_version": "v4.1-target-archetype-1",
            "research_model_id": "gpt-5.6-terra", "review_model_id": "gpt-5.6-sol",
            "review_prompt_version": campaign.REVIEW_PROMPT_VERSION,
            "model_routes": {"path": "pipeline/v4_1/model_routes.json", "sha256": "b" * 64},
            "freeze": freeze, "authorization": authorization,
            "membership": {"codes": sorted(self.manifest["membership"]["fleet_expected"]
                                                  + self.manifest["membership"]["golden_expected"]),
                           "regression_manifest": None, "holdout_manifest": None,
                           "target_universe": self.manifest["membership"]["fleet_universe"]},
            "toolchain": {key: with_length(ref) for key, ref in self.toolchain.items()},
            "entries": plan_entries,
        }
        plan["plan_sha256"] = campaign.value_sha256(plan)
        plan_path = "pipeline/v4_1/issuance/synthetic-v4.1.json"
        write_bytes(os.path.join(self.root, plan_path), campaign.canonical_bytes(plan))
        self.manifest["issuance_plan"] = campaign.artifact_ref(plan_path, self.root)
        self.manifest["freeze"] = freeze
        self.manifest["authorization"] = authorization
        self.manifest["manifest_sha256"] = campaign.manifest_sha256(self.manifest)
        return self.manifest

    def review(self, entry, outcome=None):
        review = {
            "entry_id": entry["entry_id"],
            "manifest_sha256": campaign.review_binding_sha256(self.manifest, entry),
            "artifact_digests": campaign.artifact_digests(entry),
            "toolchain_digests": campaign.toolchain_digests(self.manifest),
            "review_meta": {"model_id": "gpt-5.6-sol", "review_date": date.today().isoformat(), "prompt_version": campaign.REVIEW_PROMPT_VERSION},
            "execution": {"issued_by_task_path": "/root", "codex_task_path": "/root/review_%s" % entry["run_id"], "model_id": "gpt-5.6-sol", "fork_policy": "isolated", "role": "reviewer"},
            "mechanics": {key: True for key in campaign.MECHANICS_KEYS},
            "source_reviews": [{
                "source_id": item["source_id"], "url": item["url"], "score_driving": item["score_driving"],
                "accessible": True, "support": "supported", "input_paths": item["input_paths"], "notes": "Exact synthetic source review.",
            } for item in entry["source_registry"]],
            "input_reviews": [{
                "input_path": item["input_path"], "reviewed_bounds": item["required_bounds"],
                "evidence_state_honest": True, "base_supported": True, "range_supported": True,
                "scope_supported": True, "notes": "Exact synthetic input review.",
            } for item in entry["input_registry"]],
            "findings": [],
            "publication_caveats": list(entry["authored_caveats"]),
            "summary": "Synthetic review passes all checks.",
        }
        review["outcome"] = outcome or campaign.computed_outcome(entry, review)
        write(os.path.join(self.root, entry["review_path"]), review)
        return review


class V41CampaignTests(unittest.TestCase):
    def setUp(self):
        def validate_test_plan(root, plan_path, expected_scope=None, **_kwargs):
            plan = campaign.load_json(os.path.join(root, plan_path))
            value = dict(plan); claimed = value.pop("plan_sha256", None)
            errors = []
            if claimed != campaign.value_sha256(value):
                errors.append("issued plan self-digest is stale")
            if expected_scope is not None and plan.get("scope") != expected_scope:
                errors.append("issued plan scope does not match the campaign scope")
            return plan, errors
        self.issuer_patch = mock.patch.object(
            campaign.issuer, "validate_issued_plan", side_effect=validate_test_plan)
        self.gate_issuer_patch = mock.patch.object(
            gate_issuer.campaign.issuer, "validate_issued_plan", side_effect=validate_test_plan)
        original_source_status = campaign._certificate_source_status
        def source_status(manifest, root):
            if manifest.get("proof_fixture") is not True:
                return original_source_status(manifest, root)
            selected = sorted(item["entry_id"] for item in manifest["entries"])
            digests = {item["entry_id"]: campaign.sha256(
                os.path.join(root, item["review_path"])) for item in manifest["entries"]}
            return {"campaign_accepted": True, "selected_entry_ids": selected,
                    "review_digests": dict(sorted(digests.items()))}, []
        self.source_status_patch = mock.patch.object(
            campaign, "_certificate_source_status", side_effect=source_status)
        self.issuer_patch.start()
        self.gate_issuer_patch.start()
        self.source_status_patch.start()

    def tearDown(self):
        self.source_status_patch.stop()
        self.gate_issuer_patch.stop()
        self.issuer_patch.stop()

    def test_real_finalizer_entry_is_campaign_interoperable(self):
        with tempfile.TemporaryDirectory() as root:
            fixture = Fixture(root, real_toolchain=True)
            actual_root = os.path.join(root, "actual")
            os.makedirs(actual_root, exist_ok=True)
            finalizer_fixture = finalizer_fixtures.Fixture(actual_root)
            prompt_path = os.path.join(root, "actual", "prompt.md")
            write(prompt_path, "frozen assembled prompt\n", raw=True)
            shutil.copyfile(os.path.join(REPO, campaign.TOOLCHAIN_PATHS["methodology"]),
                            finalizer_fixture.methodology_path)
            finalizer_fixture.packet["inputs"]["target_archetype_coverage"].update(
                value=0.8, range={"low": 0.6, "high": 0.9})
            finalizer_fixtures.write_json(finalizer_fixture.packet_path, finalizer_fixture.packet)
            finalizer_fixture.spec["value_basis"]["bridge"] = None
            finalizer_fixture.spec["target_archetype"]["enumeration_coverage"] = {
                "base": 0.8, "low": 0.6, "high": 0.9,
            }
            alternative = finalizer_fixture.spec["target_archetype"]["alternatives"][0]
            alternative["band_count"] = {"base": 800, "low": 600, "high": 900}
            finalizer_fixture.spec["target_archetype"]["residual"]["band_count"] = {
                "base": 200, "low": 100, "high": 400,
            }
            finalizer_fixtures.write_json(finalizer_fixture.spec_path, finalizer_fixture.spec)
            finalizer_fixture.envelope["prompt_sha256"] = campaign.sha256(prompt_path)
            finalizer_fixture.envelope["methodology_sha256"] = fixture.toolchain["methodology"]["sha256"]
            finalizer_fixture.envelope["spec_sha256"] = campaign.sha256(str(finalizer_fixture.spec_path))
            finalizer_fixtures.write_json(finalizer_fixture.envelope_path, finalizer_fixture.envelope)
            finalizer_fixture.reload()
            finalized, errors = finalizer_fixture.finalize()
            self.assertEqual([], errors)

            record_path = os.path.join(root, "actual", "record.json")
            memo_path = os.path.join(root, "actual", "memo.md")
            write_bytes(record_path, finalizer_fixtures.finalizer.serialize_record(finalized))
            write(memo_path, finalizer_fixtures.finalizer.render_memo(finalized), raw=True)
            paths = {
                "assembled_prompt": "actual/prompt.md", "packet": "actual/packet.json",
                "dataset": "actual/dataset.json", "industry_spec": "actual/spec.json",
                "execution_envelope": "actual/envelope.json", "record": "actual/record.json",
                "memo": "actual/memo.md",
            }
            artifacts = {key: campaign.artifact_ref(path, root) for key, path in paths.items()}
            inputs = campaign.build_input_registry(finalized, finalizer_fixture.spec)
            self.assertIn("industry_spec.target_archetype.selected_id",
                          {item["input_path"] for item in inputs})
            entry = {
                "entry_id": "fleet:999999:%s" % finalizer_fixture.envelope["run_id"],
                "kind": "fleet", "naics": "999999",
                "run_id": finalizer_fixture.envelope["run_id"], "attempt": 1,
                "remediates_entry_id": None, "predecessor_review_sha256": None,
                "remediation_bundle": None, "artifacts": artifacts,
                "review_path": "reviews/actual-finalized.json",
                "input_registry": inputs,
                "source_registry": campaign.build_source_registry(
                    finalized, inputs, finalizer_fixture.spec),
                "authored_caveats": campaign.declared_caveats(finalized, finalizer_fixture.spec),
            }
            self.assertIn("A1", {item["source_id"] for item in entry["source_registry"]})
            fixture.entries.append(entry)
            fixture.freeze()
            fixture.review(entry)
            status, errors = campaign.evaluate_campaign(fixture.manifest, root)
            self.assertEqual([], errors)
            self.assertTrue(status["campaign_accepted"])

    def test_exact_manifest_and_review_validate(self):
        with tempfile.TemporaryDirectory() as root:
            fixture = Fixture(root)
            entry = fixture.add("fleet", "999999", "r1")
            fixture.freeze(); fixture.review(entry)
            status, errors = campaign.evaluate_campaign(fixture.manifest, root)
            self.assertEqual([], errors)
            self.assertTrue(status["membership_complete"])
            self.assertTrue(status["reviews_complete"])
            self.assertTrue(status["publication_complete"])

    def test_review_binding_is_derived_and_cannot_be_overridden(self):
        with tempfile.TemporaryDirectory() as root:
            fixture = Fixture(root)
            entry = fixture.add("fleet", "999999", "r1")
            fixture.freeze()
            review = fixture.review(entry)
            review["manifest_sha256"] = "0" * 64
            self.assertTrue(any("frozen manifest revision" in item for item in
                                campaign.review_errors(review, entry, fixture.manifest, root)))
            entry["review_manifest_sha256"] = "0" * 64
            fixture.freeze()
            self.assertTrue(any("derived" in item for item in
                                campaign.validate_manifest(fixture.manifest, root)))

    def test_campaign_requires_exact_issued_plan_and_rejects_fake_paths(self):
        with tempfile.TemporaryDirectory() as root:
            fixture = Fixture(root); fixture.add("fleet", "999999", "r1"); fixture.freeze()
            fixture.manifest.pop("issuance_plan")
            fixture.manifest["manifest_sha256"] = campaign.manifest_sha256(fixture.manifest)
            errors = campaign.validate_manifest(fixture.manifest, root)
            self.assertTrue(any("requires issuance_plan" in item or "issuance plan" in item
                                for item in errors))
        with tempfile.TemporaryDirectory() as root:
            fixture = Fixture(root); entry = fixture.add("fleet", "999999", "r1"); fixture.freeze()
            plan_ref = fixture.manifest["issuance_plan"]
            plan = campaign.load_json(os.path.join(root, plan_ref["path"]))
            plan["entries"][0]["planned_outputs"]["record"] = "attacker/record.json"
            value = dict(plan); value.pop("plan_sha256")
            plan["plan_sha256"] = campaign.value_sha256(value)
            write_bytes(os.path.join(root, plan_ref["path"]), campaign.canonical_bytes(plan))
            fixture.manifest["issuance_plan"] = campaign.artifact_ref(plan_ref["path"], root)
            fixture.manifest["manifest_sha256"] = campaign.manifest_sha256(fixture.manifest)
            errors = campaign.validate_manifest(fixture.manifest, root)
            self.assertTrue(any("artifact paths differ from the issued plan" in item for item in errors))
            self.assertTrue(any("issuance entry binding is stale" in item for item in errors))

    def test_reviewer_tasks_are_globally_unique_and_never_research_tasks(self):
        with tempfile.TemporaryDirectory() as root:
            fixture = Fixture(root, fleet_codes=("111111", "222222"))
            first = fixture.add("fleet", "111111", "r1")
            second = fixture.add("fleet", "222222", "r2")
            fixture.freeze(); first_review = fixture.review(first); second_review = fixture.review(second)
            second_review["execution"]["codex_task_path"] = first_review["execution"]["codex_task_path"]
            write(os.path.join(root, second["review_path"]), second_review)
            _status, errors = campaign.evaluate_campaign(fixture.manifest, root)
            self.assertTrue(any("globally unique" in item for item in errors))
            second_review["execution"]["codex_task_path"] = "/root/research_%s" % first["run_id"]
            write(os.path.join(root, second["review_path"]), second_review)
            _status, errors = campaign.evaluate_campaign(fixture.manifest, root)
            self.assertTrue(any("distinct from all research" in item for item in errors))

    def test_dataset_and_toolchain_tampering_fail(self):
        with tempfile.TemporaryDirectory() as root:
            fixture = Fixture(root); entry = fixture.add("fleet", "999999", "r1"); fixture.freeze(); fixture.review(entry)
            dataset_path = os.path.join(root, entry["artifacts"]["dataset"]["path"])
            value = campaign.load_json(dataset_path); value["aux"]["vintage"] = "changed"; write(dataset_path, value)
            errors = campaign.validate_manifest(fixture.manifest, root)
            self.assertTrue(any("dataset digest is stale" in item for item in errors))
            write(dataset_path, {"naics": "999999", "title": "Synthetic Services", "aux": {"vintage": "frozen"}})
            write(os.path.join(root, fixture.toolchain["validator_prompt"]["path"]), "changed\n", raw=True)
            errors = campaign.validate_manifest(fixture.manifest, root)
            self.assertTrue(any("validator_prompt digest is stale" in item for item in errors))

    def test_exact_unique_source_and_input_coverage(self):
        with tempfile.TemporaryDirectory() as root:
            fixture = Fixture(root); entry = fixture.add("fleet", "999999", "r1"); fixture.freeze(); review = fixture.review(entry)
            review["source_reviews"].append(copy.deepcopy(review["source_reviews"][0]))
            review["input_reviews"] = [copy.deepcopy(review["input_reviews"][0]) for _ in entry["input_registry"]]
            errors = campaign.review_errors(review, entry, fixture.manifest, root)
            self.assertTrue(any("unique source" in item for item in errors))
            self.assertTrue(any("unique input" in item for item in errors))
            self.assertTrue(any("exactly equal input registry" in item for item in errors))

    def test_unsupported_driving_evidence_forces_material_reject(self):
        with tempfile.TemporaryDirectory() as root:
            fixture = Fixture(root); entry = fixture.add("fleet", "999999", "r1"); fixture.freeze(); review = fixture.review(entry)
            review["source_reviews"][0].update({"accessible": False, "support": "unsupported"})
            review["outcome"] = "publishable"
            errors = campaign.review_errors(review, entry, fixture.manifest, root)
            self.assertTrue(any("requires a material finding" in item for item in errors))
            self.assertTrue(any("computed as reject" in item for item in errors))

    def test_mechanics_precedence_and_caveat_union(self):
        with tempfile.TemporaryDirectory() as root:
            fixture = Fixture(root); entry = fixture.add("fleet", "999999", "r1", caveats=["Authored limitation."]); fixture.freeze(); review = fixture.review(entry)
            self.assertEqual("publishable_with_caveats", review["outcome"])
            review["publication_caveats"] = []
            errors = campaign.review_errors(review, entry, fixture.manifest, root)
            self.assertTrue(any("exact authored/reviewer caveat union" in item for item in errors))
            review = fixture.review(entry); review["mechanics"]["schema_valid"] = False; review["outcome"] = "reject"
            errors = campaign.review_errors(review, entry, fixture.manifest, root)
            self.assertTrue(any("computed as invalid" in item for item in errors))

    def test_root_issued_independent_reviewer_required(self):
        with tempfile.TemporaryDirectory() as root:
            fixture = Fixture(root); entry = fixture.add("fleet", "999999", "r1"); fixture.freeze(); review = fixture.review(entry)
            review["execution"]["issued_by_task_path"] = "/other"
            review["execution"]["codex_task_path"] = "/root/research_%s" % entry["run_id"]
            errors = campaign.review_errors(review, entry, fixture.manifest, root)
            self.assertTrue(any("root-issued" in item for item in errors))
            self.assertTrue(any("executions must differ" in item for item in errors))

    def test_lineage_rejects_orphan_and_duplicate_attempt(self):
        with tempfile.TemporaryDirectory() as root:
            fixture = Fixture(root)
            fixture.add("fleet", "999999", "r1")
            second = fixture.add("fleet", "999999", "r2", attempt=2,
                                 remediates="fleet:999999:missing", predecessor_review_sha256="0" * 64)
            fixture.freeze()
            errors = campaign.validate_manifest(fixture.manifest, root)
            self.assertTrue(any("exact attempt 1" in item for item in errors))
            duplicate = copy.deepcopy(second); duplicate["run_id"] = "r3"; duplicate["entry_id"] = "fleet:999999:r3"
            fixture.entries.append(duplicate); fixture.freeze()
            errors = campaign.validate_manifest(fixture.manifest, root)
            self.assertTrue(any("at most one attempt 2" in item for item in errors))

    def test_valid_attempt_two_binds_exact_rejected_review_and_findings(self):
        with tempfile.TemporaryDirectory() as root:
            fixture = Fixture(root); first = fixture.add("fleet", "999999", "r1"); fixture.freeze()
            prior = fixture.review(first)
            finding = {
                "finding_id": "F1", "defect_rule_id": "unsupported-driving-source",
                "severity": "material", "category": "range_support",
                "input_paths": [first["input_registry"][0]["input_path"]], "source_ids": ["S1"],
                "explanation": "The score-driving source is inaccessible.",
                "causal_effect": "The supported range and score can change.",
                "remediation": "Replace it with accessible target evidence.",
            }
            finding["fingerprint"] = campaign.finding_fingerprint(finding)
            prior["source_reviews"][0].update({"accessible": False, "support": "unsupported"})
            prior["findings"] = [finding]; prior["outcome"] = "reject"
            write(os.path.join(root, first["review_path"]), prior)
            prior_sha = campaign.sha256(os.path.join(root, first["review_path"]))
            second = fixture.add("fleet", "999999", "r2", attempt=2,
                                 remediates=first["entry_id"], predecessor_review_sha256=prior_sha)
            bundle = {
                "predecessor_entry_id": first["entry_id"],
                "predecessor_review_sha256": prior_sha,
                "findings": [finding],
            }
            write(os.path.join(root, second["remediation_bundle"]["path"]), bundle)
            second["remediation_bundle"] = campaign.artifact_ref(second["remediation_bundle"]["path"], root)
            fixture.freeze(); fixture.review(second)
            status, errors = campaign.evaluate_campaign(fixture.manifest, root)
            self.assertEqual([], errors)
            self.assertTrue(status["publication_complete"])

    def test_attempt_two_rejects_unlinked_packet_change(self):
        with tempfile.TemporaryDirectory() as root:
            fixture = Fixture(root); first = fixture.add("fleet", "999999", "r1"); fixture.freeze()
            prior = fixture.review(first)
            finding = {
                "finding_id": "F1", "defect_rule_id": "unsupported-driving-source",
                "severity": "material", "category": "range_support",
                "input_paths": [first["input_registry"][0]["input_path"]], "source_ids": ["S1"],
                "explanation": "The score-driving source is inaccessible.",
                "causal_effect": "The supported range and score can change.",
                "remediation": "Replace it with accessible target evidence.",
            }
            finding["fingerprint"] = campaign.finding_fingerprint(finding)
            prior["source_reviews"][0].update({"accessible": False, "support": "unsupported"})
            prior["findings"] = [finding]; prior["outcome"] = "reject"
            write(os.path.join(root, first["review_path"]), prior)
            prior_sha = campaign.sha256(os.path.join(root, first["review_path"]))
            second = fixture.add("fleet", "999999", "r2", attempt=2,
                                 remediates=first["entry_id"], predecessor_review_sha256=prior_sha)
            bundle = {"predecessor_entry_id": first["entry_id"],
                      "predecessor_review_sha256": prior_sha, "findings": [finding]}
            write(os.path.join(root, second["remediation_bundle"]["path"]), bundle)
            second["remediation_bundle"] = campaign.artifact_ref(second["remediation_bundle"]["path"], root)
            packet_path = os.path.join(root, second["artifacts"]["packet"]["path"])
            packet = campaign.load_json(packet_path); packet["unlinked_narrative"] = "changed"; write(packet_path, packet)
            second["artifacts"]["packet"] = campaign.artifact_ref(second["artifacts"]["packet"]["path"], root)
            record_path = os.path.join(root, second["artifacts"]["record"]["path"])
            second_record = campaign.load_json(record_path)
            second_record["artifact_provenance"]["packet_sha256"] = second["artifacts"]["packet"]["sha256"]
            write(record_path, second_record)
            second["artifacts"]["record"] = campaign.artifact_ref(second["artifacts"]["record"]["path"], root)
            fixture.freeze(); fixture.review(second)
            _status, errors = campaign.evaluate_campaign(fixture.manifest, root)
            self.assertTrue(any("outside predecessor-linked inputs" in item for item in errors))

    def test_attempt_two_rejects_archetype_and_value_basis_sibling_changes(self):
        with tempfile.TemporaryDirectory() as root:
            base_spec = {
                "target_archetype": {
                    "selected_id": "a", "selection_uncertainty": False,
                    "alternatives": [
                        {"id": "a", "band_count": {"low": 20, "base": 30, "high": 40}},
                        {"id": "b", "band_count": {"low": 10, "base": 20, "high": 30},
                         "rationale": "frozen sibling"},
                    ],
                    "enumeration_coverage": {"low": 0.4, "base": 0.5, "high": 0.7},
                    "residual": {"band_count": {"low": 30, "base": 50, "high": 60}},
                },
                "value_basis": {
                    "scope": "frozen scope",
                    "labor_contractor_cash_cost_share": {"value": 0.5}, "roles": [],
                },
            }
            record_value = record("999999", "old")
            packet_value, dataset_value = {"inputs": {}, "dataset_fallbacks": {}}, {"naics": "999999"}

            def remediation_entry(prefix, spec_value, rows):
                artifacts = {}
                for key, value in (("packet", packet_value), ("dataset", dataset_value),
                                   ("industry_spec", spec_value), ("record", record_value)):
                    path = "%s/%s.json" % (prefix, key)
                    write(os.path.join(root, path), value)
                    artifacts[key] = {"path": path}
                return {"input_registry": rows, "source_registry": [], "artifacts": artifacts}

            alternative_path = "industry_spec.target_archetype.alternatives[id=a].band_count"
            rows = [{"input_path": alternative_path, "source_ids": [],
                     "driving_class": "gate", "required_bounds": ["low", "base", "high"]}]
            changed_spec = copy.deepcopy(base_spec)
            changed_spec["target_archetype"]["alternatives"][0]["band_count"]["base"] = 35
            changed_spec["target_archetype"]["enumeration_coverage"]["base"] = 0.55
            changed_spec["target_archetype"]["residual"]["band_count"]["base"] = 45
            changed_spec["target_archetype"]["alternatives"][1]["rationale"] = "unlinked edit"
            changed_spec["target_archetype"]["enumeration_coverage"]["low"] = 0.1
            first = remediation_entry("old-a", base_spec, rows)
            second = remediation_entry("new-a", changed_spec, rows)
            errors = campaign._remediation_semantic_errors(
                first, second, [{"input_paths": [alternative_path], "source_ids": []}], root)
            self.assertTrue(any("industry spec outside" in item for item in errors))

            labor_path = "inputs.target_labor_cost_share"
            labor_rows = [{"input_path": labor_path, "source_ids": [],
                           "driving_class": "score", "required_bounds": ["low", "base", "high"]}]
            changed_value_spec = copy.deepcopy(base_spec)
            changed_value_spec["value_basis"]["labor_contractor_cash_cost_share"] = {"value": 0.6}
            changed_value_spec["value_basis"]["scope"] = "unlinked sibling scope"
            first = remediation_entry("old-v", base_spec, labor_rows)
            second = remediation_entry("new-v", changed_value_spec, labor_rows)
            errors = campaign._remediation_semantic_errors(
                first, second, [{"input_paths": [labor_path], "source_ids": []}], root)
            self.assertTrue(any("industry spec outside" in item for item in errors))

    def test_full_and_partial_membership_are_distinct(self):
        with tempfile.TemporaryDirectory() as root:
            fixture = Fixture(root, fleet_codes=("111111", "222222"))
            fixture.manifest["membership"]["fleet_expected"] = ["111111"]
            fixture.manifest["membership"]["fleet_omitted"] = ["222222"]
            fixture.manifest["membership"]["snapshot_sha256"] = campaign.membership_sha256(fixture.manifest["membership"])
            fixture.add("fleet", "111111", "r1"); fixture.freeze()
            errors = campaign.validate_manifest(fixture.manifest, root)
            self.assertTrue(any("full membership" in item for item in errors))
            fixture.manifest["scope"] = "partial"; fixture.manifest["partial_authorization"] = {
                "approved_by": "human", "approved_at": date.today().isoformat(), "reason": "bounded test",
            }; fixture.freeze()
            self.assertEqual([], campaign.validate_manifest(fixture.manifest, root))

    def test_canary_gate_requires_5_of_5_invariants_and_human_signoff(self):
        with tempfile.TemporaryDirectory() as root:
            fixture = Fixture(root, fleet_codes=campaign.CANARY_CODES, scope="canary")
            entries = [fixture.add("fleet", code, "r-%s" % code) for code in campaign.CANARY_CODES]
            fixture.freeze()
            for entry in entries:
                fixture.review(entry)
            review_digests = {entry["entry_id"]: campaign.sha256(os.path.join(root, entry["review_path"])) for entry in entries}
            binding = campaign.campaign_binding_sha256(fixture.manifest)
            write(os.path.join(root, "gate", "invariants.json"), {
                "campaign_binding_sha256": binding, "passed": True,
                "checks": {name: True for name in campaign.INVARIANT_CHECKS},
            })
            write(os.path.join(root, "gate", "signoff.json"), {
                "campaign_binding_sha256": binding, "decision": "approve", "reviewer_identity": "human@example.com",
                "signed_at": date.today().isoformat(), "notes": "Economic sense review completed.",
                "selected_entry_ids": sorted(entry["entry_id"] for entry in entries),
                "review_digests": dict(sorted(review_digests.items())),
                "signoff_execution": {"issued_by_task_path": "/root",
                                      "codex_task_path": "/root/human_signoff_canary",
                                      "role": "human_signoff"},
                "commit_sha256": "c" * 64,
            })
            fixture.manifest["canary_gate"] = {
                "invariant_report": campaign.artifact_ref("gate/invariants.json", root),
                "human_sense_signoff": campaign.artifact_ref("gate/signoff.json", root),
            }
            status, errors = campaign.evaluate_campaign(fixture.manifest, root)
            self.assertEqual([], errors)
            self.assertTrue(status["canary_gate_passed"])
            manifest_path = os.path.join(root, "accepted-canary.json")
            write(manifest_path, fixture.manifest)
            certificate = gate_issuer.issue(
                root, manifest_path, "/root/certify_accepted_canary", date.today().isoformat())
            self.assertEqual(campaign.value_sha256({
                key: value for key, value in certificate.items()
                if key != "certificate_binding_sha256"
            }), certificate["certificate_binding_sha256"])
            signoff = campaign.load_json(os.path.join(root, "gate", "signoff.json")); signoff["decision"] = "reject"; write(os.path.join(root, "gate", "signoff.json"), signoff)
            _status, errors = campaign.evaluate_campaign(fixture.manifest, root)
            self.assertTrue(any("signoff digest is stale" in item for item in errors))
            signoff["decision"] = "approve"
            signoff["reviewer_identity"] = "x"
            signoff["signed_at"] = "2999-01-01"
            signoff["signoff_execution"]["issued_by_task_path"] = "/other"
            signoff["commit_sha256"] = "0" * 64
            write(os.path.join(root, "gate", "signoff.json"), signoff)
            fixture.manifest["canary_gate"]["human_sense_signoff"] = campaign.artifact_ref(
                "gate/signoff.json", root)
            _status, errors = campaign.evaluate_campaign(fixture.manifest, root)
            self.assertTrue(any("root-issued execution receipt" in item for item in errors))
            self.assertTrue(any("cannot be in the future" in item for item in errors))
            self.assertTrue(any("economic-sense signoff must approve" in item for item in errors))
            self.assertTrue(any("verifiable commit digest" in item for item in errors))

    def test_canary_gate_detects_repeated_material_defect_fingerprint(self):
        with tempfile.TemporaryDirectory() as root:
            first = {"entry_id": "fleet:541512:r1", "kind": "fleet", "naics": "541512", "attempt": 1}
            second = {"entry_id": "fleet:541512:r2", "kind": "fleet", "naics": "541512", "attempt": 2}
            finding = {"fingerprint": "a" * 64, "severity": "material", "category": "target_archetype"}
            manifest = {"entries": [first, second], "canary_gate": {}}
            reviews = {first["entry_id"]: {"outcome": "reject", "findings": [finding]},
                       second["entry_id"]: {"outcome": "reject", "findings": [finding]}}
            errors = campaign._canary_errors(manifest, [second], reviews, {}, root)
            self.assertTrue(any("repeats a material/fatal defect" in item for item in errors))

    def test_holdout_is_exact_five_and_has_its_own_gate(self):
        with tempfile.TemporaryDirectory() as root:
            fixture = Fixture(root, fleet_codes=campaign.HOLDOUT_CODES, scope="holdout")
            self.assertEqual(campaign.HOLDOUT_MEMBERSHIP_SHA256,
                             fixture.manifest["membership"]["holdout_membership"]["sha256"])
            entries = [fixture.add("fleet", code, "h-%s" % code)
                       for code in campaign.HOLDOUT_CODES]
            fixture.freeze()
            for entry in entries:
                fixture.review(entry)
            review_digests = {
                entry["entry_id"]: campaign.sha256(os.path.join(root, entry["review_path"]))
                for entry in entries
            }
            binding = campaign.campaign_binding_sha256(fixture.manifest)
            write(os.path.join(root, "holdout-gate", "invariants.json"), {
                "campaign_binding_sha256": binding, "passed": True,
                "checks": {name: True for name in campaign.INVARIANT_CHECKS},
            })
            write(os.path.join(root, "holdout-gate", "signoff.json"), {
                "campaign_binding_sha256": binding, "decision": "approve",
                "reviewer_identity": "human@example.com", "signed_at": date.today().isoformat(),
                "notes": "Holdout economic-sense review completed.",
                "selected_entry_ids": sorted(entry["entry_id"] for entry in entries),
                "review_digests": dict(sorted(review_digests.items())),
                "signoff_execution": {"issued_by_task_path": "/root",
                                      "codex_task_path": "/root/human_signoff_holdout",
                                      "role": "human_signoff"},
                "commit_sha256": "d" * 64,
            })
            fixture.manifest["holdout_gate"] = {
                "invariant_report": campaign.artifact_ref("holdout-gate/invariants.json", root),
                "human_sense_signoff": campaign.artifact_ref("holdout-gate/signoff.json", root),
            }
            status, errors = campaign.evaluate_campaign(fixture.manifest, root)
            self.assertEqual([], errors)
            self.assertTrue(status["holdout_gate_passed"])
            self.assertNotIn("canary_gate_passed", status)
            self.assertTrue(status["campaign_accepted"])

    def test_full_scope_cannot_carry_holdout_membership(self):
        with tempfile.TemporaryDirectory() as root:
            fixture = Fixture(root)
            destination = os.path.join(root, campaign.HOLDOUT_MEMBERSHIP_PATH)
            os.makedirs(os.path.dirname(destination), exist_ok=True)
            shutil.copyfile(os.path.join(REPO, campaign.HOLDOUT_MEMBERSHIP_PATH), destination)
            fixture.manifest["membership"]["holdout_membership"] = campaign.artifact_ref(
                campaign.HOLDOUT_MEMBERSHIP_PATH, root)
            fixture.manifest["membership"]["snapshot_sha256"] = campaign.membership_sha256(
                fixture.manifest["membership"])
            fixture.add("fleet", "999999", "r1")
            fixture.freeze()
            errors = campaign.validate_manifest(fixture.manifest, root)
            self.assertTrue(any("full membership may not be conflated" in item for item in errors))

    def test_full_scope_requires_both_nonzero_accepted_gate_certificates(self):
        with tempfile.TemporaryDirectory() as root:
            fixture = Fixture(root); fixture.add("fleet", "999999", "r1")
            fixture.manifest.pop("full_gate_certificates")
            fixture.freeze()
            self.assertTrue(any("requires exact" in item for item in
                                campaign.validate_manifest(fixture.manifest, root)))
        with tempfile.TemporaryDirectory() as root:
            fixture = Fixture(root); fixture.add("fleet", "999999", "r1")
            ref = fixture.manifest["full_gate_certificates"]["holdout"]
            certificate = campaign.load_json(os.path.join(root, ref["path"]))
            certificate["gate_root_sha256"] = "0" * 64
            write(os.path.join(root, ref["path"]), certificate)
            fixture.manifest["full_gate_certificates"]["holdout"] = campaign.artifact_ref(ref["path"], root)
            fixture.freeze()
            self.assertTrue(any("gate root digest is invalid" in item for item in
                                campaign.validate_manifest(fixture.manifest, root)))

    def test_full_certificate_roots_must_recompute_from_canonical_proofs(self):
        with tempfile.TemporaryDirectory() as root:
            fixture = Fixture(root); fixture.add("fleet", "999999", "r1")
            ref = fixture.manifest["full_gate_certificates"]["regression_canary"]
            certificate = campaign.load_json(os.path.join(root, ref["path"]))
            certificate["campaign_root_sha256"] = "e" * 64
            certificate["gate_root_sha256"] = "f" * 64
            certificate["certificate_binding_sha256"] = campaign.value_sha256({
                key: value for key, value in certificate.items()
                if key != "certificate_binding_sha256"
            })
            write(os.path.join(root, ref["path"]), certificate)
            fixture.manifest["full_gate_certificates"]["regression_canary"] = campaign.artifact_ref(
                ref["path"], root)
            fixture.freeze()
            errors = campaign.validate_manifest(fixture.manifest, root)
            self.assertTrue(any("does not match the exact campaign artifact" in item for item in errors))
            self.assertTrue(any("does not match the exact gate artifact" in item for item in errors))

    def test_full_certificate_reopens_source_reviews(self):
        with tempfile.TemporaryDirectory() as root:
            fixture = Fixture(root); fixture.add("fleet", "999999", "r1"); fixture.freeze()
            source_review = os.path.join(root, "gate-source", "canary", "238220-review.json")
            review = campaign.load_json(source_review)
            review["outcome"] = "reject"
            write(source_review, review)
            errors = campaign.validate_manifest(fixture.manifest, root)
            self.assertTrue(any("differs from exact source artifacts" in item
                                or "does not exactly accept" in item for item in errors))


if __name__ == "__main__":
    unittest.main()
