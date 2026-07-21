#!/usr/bin/env python3

import importlib.util
import copy
import json
import math
import os
import shutil
import subprocess
import tempfile
import unittest
from unittest import mock
from datetime import date


HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))


def load_module(name, filename):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, filename))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


campaign = load_module("v4_2_campaign_tests", "campaign_v4_2.py")
gate_issuer = load_module("v4_2_gate_issuer_tests", "issue_gate_certificate_v4_2.py")
scoring_fixtures = load_module("v4_2_campaign_scoring_fixtures", "test_v4_2_scoring.py")
finalizer_fixtures = load_module("v4_2_campaign_finalizer_fixtures", "test_v4_2_finalizer.py")


def write(path, value):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        json.dump(value, handle, sort_keys=True, separators=(",", ":"))


def selection(value, low, high):
    return {"value": value, "range": {"low": low, "high": high},
            "source_ids": [], "caveats": []}


def h_record():
    realization = {"r%d" % year: selection(0.5, 0.4, 0.6) for year in range(1, 6)}
    retention = {"c%d" % year: selection(0.5, 0.3, 0.7) for year in range(1, 6)}
    investment = {"k%d" % year: selection(0.1, 0.05, 0.2) for year in range(0, 6)}
    record = {"inputs": {"implementation_realization": realization,
                         "implementation_investment": investment,
                         "commercial_retention": retention}, "scenarios": {}}
    weights = [1 / (1.1 ** year) for year in range(1, 6)]
    for bound in ("low", "base", "high"):
        if bound == "base":
            r, c, k = [0.5] * 5, [0.5] * 5, [0.1] * 6
        elif bound == "low":
            r, c, k = [0.4] * 5, [0.3] * 5, [0.2] * 6
        else:
            r, c, k = [0.6] * 5, [0.7] * 5, [0.05] * 6
        retained = sum(r[index] * c[index] * weights[index] for index in range(5))
        discounted_investment = k[0] + sum(k[index + 1] * weights[index]
                                           for index in range(5))
        h_value = retained - discounted_investment
        record["scenarios"][bound] = {"scores": {"V": 5.0, "I": 5.0},
                                     "subfactors": {"V": {"G": 1.0}, "h": {
            "discounted_retained_realization": retained,
            "discounted_investment": discounted_investment,
            "h": h_value, "gate_triggered": h_value <= 0,
        }}}
    return record


def membership_snapshot(root, scope):
    for relative in (campaign.TARGET_UNIVERSE_PATH,
                     campaign.REGRESSION_MEMBERSHIP_PATH,
                     campaign.HOLDOUT_MEMBERSHIP_PATH):
        destination = os.path.join(root, relative)
        os.makedirs(os.path.dirname(destination), exist_ok=True)
        shutil.copyfile(os.path.join(REPO, relative), destination)
    universe = sorted(item["naics"] for item in campaign.load_json(
        os.path.join(root, campaign.TARGET_UNIVERSE_PATH))["codes"])
    selected = (set(campaign.REGRESSION_CODES) if scope == "regression"
                else set(campaign.HOLDOUT_CODES) if scope == "holdout"
                else set(universe) - set(campaign.REGRESSION_CODES) - set(campaign.HOLDOUT_CODES))
    result = {
        "target_universe": campaign.artifact_ref(campaign.TARGET_UNIVERSE_PATH, root),
        "target_expected": sorted(selected),
        "target_omitted": sorted(set(universe) - selected),
    }
    if scope in ("regression", "full"):
        result["regression_membership"] = campaign.artifact_ref(
            campaign.REGRESSION_MEMBERSHIP_PATH, root)
    if scope in ("holdout", "full"):
        result["holdout_membership"] = campaign.artifact_ref(
            campaign.HOLDOUT_MEMBERSHIP_PATH, root)
    result["snapshot_sha256"] = campaign.membership_sha256(result)
    return result


def closed_entry(attempt=1):
    entry = {
        "entry_id": "entry_v42_aaaaaaaaaaaaaaaaaaaaaaaa_a%d" % attempt,
        "kind": "target", "naics": "238220", "title": "Neutral target",
        "run_id": "v42_aaaaaaaaaaaaaaaaaaaaaaaa_a%d" % attempt,
        "run_date": date.today().isoformat(), "attempt": attempt,
        "remediates_run_id": None if attempt == 1 else "v42_first_a1",
        "issuance_entry_sha256": "e" * 64, "artifacts": {},
        "review_path": "reviews/neutral.json", "input_registry": [],
        "source_registry": [], "authored_caveats": [],
    }
    if attempt == 2:
        entry.update({"remediates_entry_id": "entry_v42_first_a1",
                      "predecessor_review_sha256": "a" * 64,
                      "predecessor_run_sha256": "b" * 64,
                      "remediable_paths": ["inputs.recognized_revenue"],
                      "remediation_bundle": {"path": "remediation.json",
                                             "sha256": "c" * 64}})
    return entry


class V42CampaignTests(unittest.TestCase):
    def test_mechanics_keys_exactly_equal_review_schema(self):
        schema = campaign.load_json(os.path.join(
            HERE, "schemas", "review_record_v4_2.schema.json"))
        mechanics = schema["properties"]["mechanics"]
        self.assertEqual(tuple(mechanics["required"]), campaign.MECHANICS_KEYS)
        self.assertEqual(set(mechanics["properties"]), set(campaign.MECHANICS_KEYS))
        self.assertEqual(28, len(campaign.MECHANICS_KEYS))
        self.assertNotIn("roles_equal", campaign.MECHANICS_KEYS)

    def test_schema_valid_publishable_review_reaches_regression_gate(self):
        with tempfile.TemporaryDirectory() as root:
            entry = {
                "entry_id": "entry_v42_aaaaaaaaaaaaaaaaaaaaaaaa_a1",
                "kind": "target", "naics": "238220",
                "run_id": "reachable", "attempt": 1,
                "source_registry": [{"source_id": "S1", "url": "https://example.com/source",
                                     "score_driving": True, "input_paths": ["inputs.recognized_revenue"],
                                     "driving_classes": ["score"]}],
                "input_registry": [{"input_path": "inputs.recognized_revenue",
                                    "required_bounds": ["low", "base", "high"],
                                    "source_ids": ["S1"], "driving_class": "score"}],
                "authored_caveats": [],
            }
            review = {
                "entry_id": entry["entry_id"], "manifest_sha256": "a" * 64,
                "artifact_digests": {key + "_sha256": "b" * 64 for key in
                                     campaign.ARTIFACT_KEYS},
                "toolchain_digests": {"campaign_validator": "c" * 64},
                "review_meta": {"model_id": "gpt-5.6-sol",
                                "review_date": date.today().isoformat(),
                                "prompt_version": "validator-4.2"},
                "execution": {"issued_by_task_path": "/root",
                              "codex_task_path": "/root/review_reachable_238220",
                              "model_id": "gpt-5.6-sol", "fork_policy": "isolated",
                              "role": "reviewer"},
                "outcome": "publishable",
                "mechanics": {key: True for key in campaign.MECHANICS_KEYS},
                "source_reviews": [{"source_id": "S1", "url": "https://example.com/source",
                                    "score_driving": True, "accessible": True,
                                    "support": "supported",
                                    "input_paths": ["inputs.recognized_revenue"],
                                    "notes": "Exact source support reviewed."}],
                "input_reviews": [{"input_path": "inputs.recognized_revenue",
                                   "reviewed_bounds": ["low", "base", "high"],
                                   "evidence_state_honest": True, "base_supported": True,
                                   "range_supported": True, "scope_supported": True,
                                   "attribution_separated": True,
                                   "notes": "Exact input bounds reviewed."}],
                "findings": [], "publication_caveats": [],
                "summary": "All v4.2 publication checks pass.",
            }
            schema = campaign.load_json(os.path.join(
                HERE, "schemas", "review_record_v4_2.schema.json"))
            self.assertEqual([], campaign.legacy_build.schema_errors(review, schema, schema))
            self.assertEqual("publishable", campaign.computed_outcome(entry, review))

            entries, reviews, review_hashes = [], {}, {}
            for index, code in enumerate(campaign.REGRESSION_CODES, 1):
                item = dict(entry)
                item["entry_id"] = "entry_v42_%024x_a1" % index
                item["naics"] = code
                item["run_id"] = "reachable-%s" % code
                item["artifacts"] = {
                    key: {"path": "unused/%s/%s" % (item["entry_id"], key),
                          "sha256": ("%x" % index) * 64}
                    for key in campaign.ARTIFACT_KEYS}
                entries.append(item)
                item_review = copy.deepcopy(review)
                item_review["entry_id"] = item["entry_id"]
                item_review["execution"]["codex_task_path"] = "/root/review_reachable_%s" % code
                reviews[item["entry_id"]] = item_review
                review_hashes[item["entry_id"]] = campaign.value_sha256(item_review)
            manifest = {"manifest_version": campaign.MANIFEST_VERSION,
                        "campaign_id": "reachable-regression", "scope": "regression",
                        "issuance_plan": {"sha256": "e" * 64}, "entries": entries}
            report_path = "gate/reachable-sentinel-report.json"
            signoff_path = "gate/reachable-operator-signoff.json"
            report = {"scope": "regression", "records": [
                {"path": item["artifacts"]["record"]["path"]} for item in entries]}
            write(os.path.join(root, report_path), report)
            key = os.path.join(root, "operator-key")
            subprocess.run(["ssh-keygen", "-q", "-t", "ed25519", "-N", "", "-f", key],
                           check=True)
            os.makedirs(os.path.join(root, "pipeline/v4_2"), exist_ok=True)
            with open(key + ".pub", encoding="utf-8") as handle:
                public_key = handle.read().strip()
            with open(os.path.join(root, campaign.OPERATOR_SIGNOFF_ALLOWED_SIGNERS),
                      "w", encoding="utf-8") as handle:
                handle.write("jkee %s\n" % public_key)
            subprocess.run(["git", "-C", root, "init", "-q"], check=True)
            subprocess.run(["git", "-C", root, "config", "user.email", "operator@test"], check=True)
            subprocess.run(["git", "-C", root, "config", "user.name", "Operator Test"], check=True)
            subprocess.run(["git", "-C", root, "config", "gpg.format", "ssh"], check=True)
            subprocess.run(["git", "-C", root, "config", "user.signingkey", key], check=True)
            subprocess.run(["git", "-C", root, "config", "gpg.ssh.allowedSignersFile",
                            campaign.OPERATOR_SIGNOFF_ALLOWED_SIGNERS], check=True)
            subprocess.run(["git", "-C", root, "add", "."], check=True)
            subprocess.run(["git", "-C", root, "commit", "-qm", "operator context"], check=True)
            commit_sha = subprocess.run(
                ["git", "-C", root, "rev-parse", "HEAD"], check=True,
                stdout=subprocess.PIPE, text=True).stdout.strip()
            tag_name = "v4.2-operator-test"
            subprocess.run(["git", "-C", root, "tag", "-s", tag_name,
                            "-m", "operator gate context"], check=True)
            tag_object_sha = subprocess.run(
                ["git", "-C", root, "rev-parse", "refs/tags/%s^{tag}" % tag_name],
                check=True, stdout=subprocess.PIPE, text=True).stdout.strip()
            def full_ref(relative):
                ref = campaign.artifact_ref(relative, root)
                ref["byte_length"] = os.path.getsize(os.path.join(root, relative))
                return ref
            report_ref = full_ref(report_path)
            payload = {
                "signoff_version": campaign.OPERATOR_SIGNOFF_VERSION,
                "scope": "regression", "campaign_id": "reachable-regression",
                "issuance_plan_sha256": "e" * 64,
                "entries_artifacts_reviews_root_sha256": campaign.gate_entries_root(
                    manifest, entries, review_hashes),
                "sentinel_gate_report_sha256": report_ref["sha256"],
                "decision": "approve", "signer_principal": "jkee",
                "signature_namespace": campaign.OPERATOR_SIGNOFF_NAMESPACE,
                "timestamp": date.today().isoformat() + "T00:00:00+00:00",
                "git_context": {"commit_sha": commit_sha, "tag_name": tag_name,
                                "tag_object_sha": tag_object_sha},
            }
            with open(os.path.join(root, signoff_path), "wb") as handle:
                handle.write(campaign.canonical_bytes(payload))
            subprocess.run(["ssh-keygen", "-Y", "sign", "-f", key, "-n",
                            campaign.OPERATOR_SIGNOFF_NAMESPACE,
                            os.path.join(root, signoff_path)], check=True,
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            signature_path = signoff_path + ".sig"
            with open(os.path.join(root, signature_path), "rb") as handle:
                valid_signature = handle.read()
            manifest["regression_gate"] = {
                "sentinel_gate_report": report_ref,
                "operator_signoff": {
                    "payload": full_ref(signoff_path),
                    "signature": full_ref(signature_path),
                },
            }
            with unittest.mock.patch.object(
                    campaign.gate_report_v4_2, "validate_report", return_value=report):
                self.assertEqual([], campaign._canary_errors(
                    manifest, entries, reviews, review_hashes, root))

            # A dummy hexadecimal assertion is not a signature.
            with open(os.path.join(root, signature_path), "w", encoding="utf-8") as handle:
                handle.write("d" * 64)
            manifest["regression_gate"]["operator_signoff"]["signature"] = \
                full_ref(signature_path)
            with unittest.mock.patch.object(
                    campaign.gate_report_v4_2, "validate_report", return_value=report):
                errors = campaign._operator_signoff_errors(
                    manifest, entries, review_hashes, root, manifest["regression_gate"], "regression")
            self.assertTrue(any("SSH signature" in item for item in errors), errors)

            # A signed payload cannot be edited or replayed onto another campaign.
            with open(os.path.join(root, signature_path), "wb") as handle:
                handle.write(valid_signature)
            manifest["regression_gate"]["operator_signoff"]["signature"] = \
                full_ref(signature_path)
            mismatched = dict(payload)
            mismatched["decision"] = "reject"
            with open(os.path.join(root, signoff_path), "wb") as handle:
                handle.write(campaign.canonical_bytes(mismatched))
            manifest["regression_gate"]["operator_signoff"]["payload"] = \
                full_ref(signoff_path)
            with unittest.mock.patch.object(
                    campaign.gate_report_v4_2, "validate_report", return_value=report):
                errors = campaign._operator_signoff_errors(
                    manifest, entries, review_hashes, root, manifest["regression_gate"], "regression")
            self.assertTrue(any("SSH signature" in item for item in errors), errors)
            with open(os.path.join(root, signoff_path), "wb") as handle:
                handle.write(campaign.canonical_bytes(payload))
            manifest["regression_gate"]["operator_signoff"]["payload"] = \
                full_ref(signoff_path)
            replay = dict(manifest)
            replay["campaign_id"] = "different-campaign"
            with unittest.mock.patch.object(
                    campaign.gate_report_v4_2, "validate_report", return_value=report):
                errors = campaign._operator_signoff_errors(
                    replay, entries, review_hashes, root, manifest["regression_gate"], "regression")
            self.assertTrue(any("campaign_id" in item for item in errors), errors)

    def test_attribution_separation_false_requires_material_reject(self):
        with tempfile.TemporaryDirectory() as root:
            entry = {
                "entry_id": "entry_v42_bbbbbbbbbbbbbbbbbbbbbbbb_a1",
                "kind": "target", "naics": "238220",
                "run_id": "attribution", "attempt": 1,
                "source_registry": [{"source_id": "S1", "url": "https://example.com/source",
                                     "score_driving": True,
                                     "input_paths": ["inputs.recognized_revenue"],
                                     "driving_classes": ["score"]}],
                "input_registry": [{"input_path": "inputs.recognized_revenue",
                                    "required_bounds": ["low", "base", "high"],
                                    "source_ids": ["S1"], "driving_class": "score"}],
                "authored_caveats": [],
            }
            envelope_path = "artifacts/attribution/execution.json"
            write(os.path.join(root, envelope_path), {
                "run_date": date.today().isoformat(), "issued_by_task_path": "/root",
                "codex_task_path": "/root/research_attribution", "model_id": "gpt-5.6-terra",
                "fork_policy": "none", "role": "research",
            })
            entry["artifacts"] = {
                key: {"path": envelope_path if key == "execution_envelope" else
                      "artifacts/attribution/%s" % key, "sha256": "b" * 64}
                for key in campaign.ARTIFACT_KEYS
            }
            review_execution = {
                "issued_by_task_path": "/root", "codex_task_path": "/root/review_attribution",
                "model_id": "gpt-5.6-sol", "fork_policy": "isolated", "role": "reviewer",
            }
            toolchain = {
                key: {"path": path, "sha256": "c" * 64}
                for key, path in campaign.TOOLCHAIN_PATHS.items()
            }
            plan_path = "campaign/attribution-plan.json"
            write(os.path.join(root, plan_path), {
                "entries": [{"entry_id": entry["entry_id"],
                             "review_execution": review_execution}],
            })
            manifest = {
                "manifest_version": campaign.MANIFEST_VERSION,
                "campaign_id": "attribution-review", "scope": "regression",
                "toolchain": toolchain, "entries": [entry],
                "issuance_plan": {"path": plan_path, "sha256": "d" * 64},
            }
            review = {
                "entry_id": entry["entry_id"],
                "manifest_sha256": campaign.review_binding_sha256(manifest, entry),
                "artifact_digests": campaign.artifact_digests(entry),
                "toolchain_digests": campaign.toolchain_digests(manifest),
                "review_meta": {"model_id": "gpt-5.6-sol",
                                "review_date": date.today().isoformat(),
                                "prompt_version": "validator-4.2"},
                "execution": review_execution, "outcome": "publishable",
                "mechanics": {key: True for key in campaign.MECHANICS_KEYS},
                "source_reviews": [{"source_id": "S1", "url": "https://example.com/source",
                                    "score_driving": True, "accessible": True,
                                    "support": "supported",
                                    "input_paths": ["inputs.recognized_revenue"],
                                    "notes": "Exact source support reviewed."}],
                "input_reviews": [{"input_path": "inputs.recognized_revenue",
                                   "reviewed_bounds": ["low", "base", "high"],
                                   "evidence_state_honest": True, "base_supported": True,
                                   "range_supported": True, "scope_supported": True,
                                   "attribution_separated": True,
                                   "notes": "P/C/survival attribution is separated."}],
                "findings": [], "publication_caveats": [],
                "summary": "Attribution review fixture.",
            }

            self.assertEqual([], campaign.review_errors(review, entry, manifest, root))
            self.assertEqual("publishable", campaign.computed_outcome(entry, review))

            review["input_reviews"][0]["attribution_separated"] = False
            errors = campaign.review_errors(review, entry, manifest, root)
            self.assertEqual("reject", campaign.computed_outcome(entry, review))
            self.assertTrue(any(
                "unsupported input inputs.recognized_revenue requires a material finding" in item
                for item in errors))
            self.assertTrue(any("outcome must be computed as reject" in item for item in errors))

    def test_versioned_paths_and_h_contract_never_reuse_v41(self):
        self.assertEqual("review-campaign-4.2", campaign.MANIFEST_VERSION)
        self.assertEqual("regression", campaign.core.DEVELOPMENT_SCOPE)
        self.assertEqual("regression_gate", campaign.core.DEVELOPMENT_GATE_KEY)
        self.assertIn("h_gate_valid", campaign.MECHANICS_KEYS)
        self.assertIn("operating_value_viability_h_gate", campaign.INVARIANT_CHECKS)
        for key, path in campaign.TOOLCHAIN_PATHS.items():
            if key not in ("rejection_record", "methodology", "campaign_authority_core",
                           "gate_certificate_core"):
                self.assertNotIn("v4_1", path)
        self.assertEqual("V4_2_RUNTIME_METHODOLOGY.md", campaign.TOOLCHAIN_PATHS["methodology"])
        self.assertEqual("pipeline/build/issue_campaign_v4_2.py",
                         campaign.TOOLCHAIN_PATHS["issuer"])
        self.assertEqual(campaign.FROZEN_HOLDOUT_SHA256, campaign.HOLDOUT_MEMBERSHIP_SHA256)
        self.assertEqual({"541890", "541340", "541370", "541199", "541420"},
                         set(campaign.HOLDOUT_CODES))
        self.assertIn("campaign_authority_core", campaign.TOOLCHAIN_KEYS)
        self.assertIn("gate_certificate_core", campaign.TOOLCHAIN_KEYS)
        self.assertEqual("gate-certificate-4.2", gate_issuer.campaign.GATE_CERTIFICATE_VERSION)

    def test_h_gate_is_recomputed_from_primitive_schedules(self):
        record = h_record()
        self.assertEqual([], campaign._h_record_errors(record))
        record["scenarios"]["low"]["subfactors"]["h"]["h"] += 0.01
        record["scenarios"]["base"]["subfactors"]["h"]["gate_triggered"] = not (
            record["scenarios"]["base"]["subfactors"]["h"]["h"] <= 0)
        errors = campaign._h_record_errors(record)
        self.assertTrue(any("differs from primitive inputs" in item for item in errors))
        self.assertTrue(any("trigger iff h <= 0" in item for item in errors))

    def test_unresolved_base_h_cannot_claim_a_gate_result(self):
        record = h_record()
        record["inputs"]["implementation_realization"]["r1"] = selection(None, None, None)
        diagnostic = record["scenarios"]["base"]["subfactors"]["h"]
        diagnostic.update(discounted_retained_realization=None, discounted_investment=None,
                          h=None, gate_triggered=False)
        errors = campaign._h_record_errors(record)
        self.assertTrue(any("unresolved h must remain null" in item for item in errors))

    def test_zero_g_structural_h_matches_scorer_and_rejects_fabrication(self):
        source = scoring_fixtures.record()
        source["inputs"]["employee_cash_cost"] = scoring_fixtures.selection(0.0)
        source["inputs"]["controllable_contractor_cash_cost"] = scoring_fixtures.selection(0.0)
        computed = scoring_fixtures.scoring.calculate(source)
        finalized = copy.deepcopy(source)
        finalized["scenarios"] = {bound: computed[bound] for bound in ("low", "base", "high")}
        finalized["decision"] = computed["decision"]
        self.assertEqual([], campaign._h_record_errors(finalized))
        self.assertEqual("kill", finalized["decision"]["economic_verdict"])
        finalized["scenarios"]["base"]["subfactors"]["h"][
            "discounted_retained_realization"] = 1.0
        errors = campaign._h_record_errors(finalized)
        self.assertTrue(any("G=0 requires structural zero h" in item for item in errors))

    def test_missing_and_unbounded_g_stay_indeterminate_across_layers(self):
        source = scoring_fixtures.record()
        source["inputs"]["employee_cash_cost"] = scoring_fixtures.missing()
        computed = scoring_fixtures.scoring.calculate(source)
        finalized = copy.deepcopy(source)
        finalized["scenarios"] = {bound: computed[bound] for bound in ("low", "base", "high")}
        finalized["decision"] = computed["decision"]
        self.assertEqual("indeterminate", finalized["decision"]["economic_verdict"])
        self.assertEqual([], campaign._h_record_errors(finalized))
        for bound in ("low", "base", "high"):
            finalized["scenarios"][bound]["subfactors"]["V"]["G"] = "UNBOUNDED"
        self.assertEqual([], campaign._h_record_errors(finalized))
        finalized["scenarios"]["base"]["subfactors"]["h"].update(
            discounted_retained_realization=1.0, discounted_investment=0.0,
            h=1.0, gate_triggered=False)
        errors = campaign._h_record_errors(finalized)
        self.assertTrue(any("missing/unbounded G requires unresolved h" in item for item in errors))

    def test_membership_snapshots_are_closed_exact_63_code_partitions(self):
        with tempfile.TemporaryDirectory() as root:
            for scope, expected_size, omitted_size in (
                    ("regression", 5, 58), ("holdout", 5, 58), ("full", 53, 10)):
                membership = membership_snapshot(root, scope)
                self.assertEqual(expected_size, len(membership["target_expected"]))
                self.assertEqual(omitted_size, len(membership["target_omitted"]))
                self.assertEqual([], campaign._v4_2_membership_errors(
                    {"scope": scope, "membership": membership}, root))

    def test_membership_mutations_fail_with_plan_codes_unchanged(self):
        with tempfile.TemporaryDirectory() as root:
            original = membership_snapshot(root, "regression")
            fixed_entries, fixed_plan_entries = [], []
            for index, code in enumerate(original["target_expected"], 1):
                entry = closed_entry()
                entry["entry_id"] = "entry_v42_%024x_a1" % index
                entry["run_id"] = "v42_%024x_a1" % index
                entry["naics"] = code
                fixed_entries.append(entry)
                fixed_plan_entries.append({key: entry.get(key) for key in
                                           campaign.V4_2_PLAN_IDENTITY_KEYS})
            plan = {"membership": {
                "codes": list(original["target_expected"]),
                "target_universe": {**original["target_universe"], "byte_length": 1},
                "regression_manifest": {**original["regression_membership"],
                                        "byte_length": 1},
                "holdout_manifest": None, "full_gate_certificates": None,
            }, "entries": fixed_plan_entries}
            manifest = {"scope": "regression", "membership": original,
                        "entries": fixed_entries}
            self.assertEqual([], campaign._v4_2_plan_binding_errors(manifest, plan))

            mutations = []
            value = copy.deepcopy(original); value["unexpected"] = True; mutations.append(value)
            value = copy.deepcopy(original); value["target_universe"]["sha256"] = "0" * 64; mutations.append(value)
            value = copy.deepcopy(original); value["target_universe"]["path"] = "other.json"; mutations.append(value)
            value = copy.deepcopy(original); value["regression_membership"]["sha256"] = "0" * 64; mutations.append(value)
            value = copy.deepcopy(original); value["target_omitted"].append(value["target_omitted"][-1]); mutations.append(value)
            value = copy.deepcopy(original); value["target_omitted"][0] = value["target_expected"][0]; mutations.append(value)
            value = copy.deepcopy(original); value["target_expected"] = value["target_expected"][:-1]; mutations.append(value)
            value = copy.deepcopy(original); value["snapshot_sha256"] = "0" * 64; mutations.append(value)
            for membership in mutations:
                if membership["snapshot_sha256"] != "0" * 64:
                    membership["snapshot_sha256"] = campaign.membership_sha256(membership)
                mutated = {"scope": "regression", "membership": membership, "entries": []}
                self.assertTrue(campaign._v4_2_membership_errors(mutated, root))
                if membership.get("target_expected") != original["target_expected"]:
                    self.assertTrue(campaign._v4_2_plan_binding_errors(mutated, plan))

    def test_manifest_entry_closure_leakage_and_plan_projection(self):
        entry = closed_entry()
        self.assertEqual([], campaign._v4_2_entry_shape_errors(entry))
        self.assertEqual([], campaign._v4_2_entry_leakage_errors(entry))
        for key, value in (("expected_outcome", "publishable"),
                           ("scope", "regression"),
                           ("class_label", "holdout"),
                           ("reviewer_note", "Prior result was a reject.")):
            mutated = copy.deepcopy(entry)
            mutated[key] = value
            self.assertTrue(campaign._v4_2_entry_shape_errors(mutated))
            self.assertTrue(campaign._v4_2_entry_leakage_errors(mutated))

        plan_entry = {key: entry.get(key) for key in campaign.V4_2_PLAN_IDENTITY_KEYS}
        plan = {"membership": {"codes": [], "target_universe": None,
                                "regression_manifest": None, "holdout_manifest": None,
                                "full_gate_certificates": None},
                "entries": [plan_entry]}
        manifest = {"scope": "regression", "membership": {"target_expected": []},
                    "entries": [entry]}
        self.assertEqual([], campaign._v4_2_plan_binding_errors(manifest, plan))
        for field in ("title", "run_date", "remediates_run_id"):
            mutated = copy.deepcopy(entry)
            mutated[field] = "changed"
            mutated["issuance_entry_sha256"] = entry["issuance_entry_sha256"]
            bound = copy.deepcopy(manifest); bound["entries"] = [mutated]
            self.assertTrue(any(field in error for error in
                                campaign._v4_2_plan_binding_errors(bound, plan)))

        second = closed_entry(2)
        self.assertEqual([], campaign._v4_2_entry_shape_errors(second))
        planned_second = {key: second.get(key) for key in
                          campaign.V4_2_PLAN_IDENTITY_KEYS + campaign.V4_2_PLAN_LINEAGE_KEYS}
        planned_second["remediation_bundle"] = {**second["remediation_bundle"],
                                                "byte_length": 1}
        plan["entries"] = [planned_second]
        manifest["entries"] = [second]
        second["predecessor_run_sha256"] = "f" * 64
        self.assertTrue(any("predecessor_run_sha256" in error for error in
                            campaign._v4_2_plan_binding_errors(manifest, plan)))

    def test_full_gate_certificates_are_exactly_plan_bound(self):
        certificates = {
            "regression_canary": {"path": "regression-certificate.json",
                                  "sha256": "a" * 64},
            "holdout": {"path": "holdout-certificate.json", "sha256": "b" * 64},
        }
        manifest = {"scope": "full", "membership": {"target_expected": []},
                    "full_gate_certificates": certificates, "entries": []}
        plan = {"membership": {
            "codes": [], "target_universe": None, "regression_manifest": None,
            "holdout_manifest": None,
            "full_gate_certificates": {
                key: {**ref, "byte_length": 1} for key, ref in certificates.items()},
        }, "entries": []}
        self.assertEqual([], campaign._v4_2_plan_binding_errors(manifest, plan))
        manifest["full_gate_certificates"]["holdout"]["sha256"] = "c" * 64
        self.assertTrue(any("gate certificates" in error for error in
                            campaign._v4_2_plan_binding_errors(manifest, plan)))

    def test_issuance_plan_authorization_chain_is_mandatory(self):
        errors = campaign._issuance_errors({"scope": "regression"}, "/tmp")
        self.assertTrue(any("issuance plan" in item for item in errors))
        self.assertEqual("v4.2-pre-run-issuance-1", campaign.issuer_v4_2.PLAN_VERSION)

    def test_pass_through_costs_are_exact_review_inputs(self):
        record = {
            "inputs": {
                "recognized_revenue": selection(100, 90, 110),
                "employee_cash_cost": selection(30, 25, 35),
                "controllable_contractor_cash_cost": selection(10, 8, 12),
                "target_archetype_coverage": selection(0.6, 0.5, 0.7),
                "implementation_realization": {"r%d" % year: selection(0.5, 0.4, 0.6)
                                               for year in range(1, 6)},
                "implementation_investment": {"k%d" % year: selection(0.1, 0.05, 0.2)
                                              for year in range(0, 6)},
                "commercial_retention": {"c%d" % year: selection(0.5, 0.4, 0.6)
                                         for year in range(1, 6)},
                "five_year_sale_availability": selection(0.2, 0.1, 0.3),
                "buyer_access_win_share": selection(0.4, 0.2, 0.6),
                "deal_execution_capacity_5y": selection(12, 8, 20),
                "integration_onboarding_capacity_5y": selection(10, 6, 16),
                "buy_mult": selection(5, 4, 6),
                "normalized_y5_operating_state": selection(1, 0.8, 1.1),
                "downside_exit_mult": selection(4, 3, 5),
                "operator_controlled_value_added_demand_share_y5": selection(0.8, 0.6, 0.9),
                "target_role_mix": {"roles": []},
                "third_party_pass_through": [
                    {"cost_id": "MEDIA", "amount": selection(15, 10, 20)},
                ],
            }
        }
        rows = campaign.build_input_registry(record)
        self.assertIn("inputs.third_party_pass_through[cost_id=MEDIA].amount",
                      {item["input_path"] for item in rows})

    def test_finalized_structured_target_run_builds_exact_campaign_registries(self):
        with tempfile.TemporaryDirectory() as root:
            fixture = finalizer_fixtures.Fixture(root)
            record, errors = finalizer_fixtures.finalizer.finalize(
                fixture.packet, fixture.data, fixture.spec, fixture.envelope, fixture.paths)
            self.assertEqual([], errors)
            self.assertEqual("target", record["run_meta"]["kind"])
            self.assertEqual(
                os.path.join(os.path.dirname(os.path.dirname(HERE)),
                             "V4_2_RUNTIME_METHODOLOGY.md"),
                str(fixture.methodology_path))
            self.assertEqual(
                campaign.sha256(str(fixture.methodology_path)),
                fixture.spec["methodology_snapshot"]["sha256"])

            buyability = record["scenarios"]["base"]["subfactors"]["B"]
            self.assertEqual((100.0, 80.0, 80.0),
                             (buyability["O5"], buyability["K5"], buyability["N5"]))
            self.assertEqual(
                "RECOMPUTED", record["construct_provenance"]["p_attribution"][
                    "calculation_status"])
            survival = record["construct_provenance"]["constant_price_survival"]
            self.assertEqual("RECOMPUTED", survival["calculation_status"])
            self.assertEqual("FIXED_BASE_LASPEYRES_CVA",
                             survival["fixed_base_assertions"]["index_method"])

            record_path = "record.json"
            memo_path = "memo.md"
            write(os.path.join(root, record_path), record)
            with open(os.path.join(root, memo_path), "w", encoding="utf-8") as handle:
                handle.write(finalizer_fixtures.finalizer.render_memo(record))
            artifact_paths = {
                "assembled_prompt": "prompt.md", "packet": "packet.json",
                "dataset": "dataset.json", "industry_spec": "spec.json",
                "execution_envelope": "envelope.json", "record": record_path,
                "memo": memo_path,
            }
            artifacts = {
                key: campaign.artifact_ref(path, root) for key, path in artifact_paths.items()
            }
            input_registry = campaign.build_input_registry(record, fixture.spec)
            input_paths = {item["input_path"] for item in input_registry}
            self.assertIn("inputs.deal_execution_capacity_5y", input_paths)
            self.assertIn("inputs.integration_onboarding_capacity_5y", input_paths)
            self.assertIn("inputs.third_party_pass_through[cost_id=materials_cash].amount",
                          input_paths)

            envelope_hashes = {
                "methodology": "methodology_sha256", "thresholds": "thresholds_sha256",
                "packet_schema": "research_packet_schema_sha256",
                "dataset_schema": "dataset_schema_sha256",
                "industry_spec_schema": "industry_spec_schema_sha256",
                "run_schema": "run_record_schema_sha256", "scoring": "scoring_sha256",
                "finalizer": "finalizer_sha256",
            }
            toolchain = {
                key: {"path": path,
                      "sha256": fixture.envelope[envelope_hashes[key]]
                      if key in envelope_hashes else "c" * 64}
                for key, path in campaign.TOOLCHAIN_PATHS.items()
            }
            entry = {
                "entry_id": "entry_v42_0123456789abcdef01234567_a1",
                "kind": "target", "naics": record["naics"], "title": record["title"],
                "run_id": record["run_meta"]["run_id"],
                "run_date": record["run_meta"]["run_date"], "attempt": 1,
                "remediates_run_id": None,
                "issuance_entry_sha256": "e" * 64, "artifacts": artifacts,
                "review_path": "review.json",
                "input_registry": input_registry,
                "source_registry": campaign.build_source_registry(
                    record, input_registry, fixture.spec),
                "authored_caveats": campaign.declared_caveats(record, fixture.spec),
            }
            manifest = {"toolchain": toolchain}
            self.assertEqual([], campaign._entry_errors(entry, manifest, root))


if __name__ == "__main__":
    unittest.main()
