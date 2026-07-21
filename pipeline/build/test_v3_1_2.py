#!/usr/bin/env python3
"""Synthetic v3.1.2 boundary, publication and frozen-artifact tests."""

import copy
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import shutil
import tempfile
import unittest


HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
SCHEMAS = HERE / "schemas"


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


build = load_module("build_v312_tests", HERE / "build.py")
finalizer = load_module("finalizer_v312_tests", HERE / "finalize_run_v3_1_2.py")
campaign = load_module("campaign_v312_tests", HERE / "review_campaign_v3_1_2.py")
assemble = load_module("assemble_v312_tests", HERE / "assemble_prompts.py")


def selection(value, method="ESTIMATE", source_ids=None, evidence_quality="MED"):
    return {
        "value": value,
        "method": method,
        "evidence_quality": evidence_quality,
        "confidence": "MED",
        "source_ids": ["S1"] if source_ids is None else source_ids,
        "rationale": "A bounded synthetic judgment tied to the declared source context.",
        "plausible_range": "Synthetic low-to-high range.",
        "caveats": [],
    }


def dataset():
    return {
        "naics": "999999",
        "title": "Synthetic Industry",
        "labor_share": {"value": 0.5, "method": "synthetic", "quality": "HIGH"},
        "role_mix": {
            "oews_level": "synthetic",
            "occupations": [
                {"soc": "11-1111", "title": "Synthetic Managers", "emp_share": 0.6, "wage_share": 0.6},
                {"soc": "22-2222", "title": "Synthetic Specialists", "emp_share": 0.3, "wage_share": 0.3},
            ],
            "quality": "HIGH",
        },
        "n_total": {"value": 1000, "source": "synthetic", "quality": "HIGH"},
        "n_band": {"value": 100, "derivation": "synthetic", "quality": "ESTIMATE"},
    }


def packet(model="gpt-5.6-terra", attempt=1):
    role = {
        "method": "ESTIMATE", "evidence_quality": "MED", "confidence": "MED",
        "source_ids": ["S1"], "rationale": "Task-level synthetic judgment for supplied roles.",
        "plausible_range": "0.2-0.6", "caveats": [],
        "role_judgments": [
            {"soc": "11-1111", "within_role_automatable_fraction": 0.2, "rationale": "Some managerial analysis automates.", "plausible_range": "0.1-0.3"},
            {"soc": "22-2222", "within_role_automatable_fraction": 0.6, "rationale": "More specialist workflow automates.", "plausible_range": "0.4-0.8"},
            {"soc": "RESIDUAL", "within_role_automatable_fraction": 0.4, "rationale": "Residual work is mixed.", "plausible_range": "0.2-0.6"},
        ],
    }
    meta = {"model_id": model, "run_date": "2026-07-21", "run_id": "synthetic-v312-a%d-999999" % attempt, "template_version": "3.1.2", "prompt_version": "v3.1.2-text-first-1", "attempt": attempt}
    if attempt == 2:
        meta["remediates_run_id"] = "synthetic-v312-a1-999999"
    paragraph = "This synthetic paragraph is deliberately long enough to represent a useful research memo section with explicit reasoning."
    return {
        "naics": "999999", "title": "Synthetic Industry", "run_meta": meta,
        "narrative": {
            "executive_view": paragraph, "how_ai_changes_work": paragraph,
            "value_capture": paragraph, "adoption_timing": paragraph,
            "consolidation_economics": paragraph, "terminal_demand": paragraph,
            "risks_and_uncertainty": paragraph,
        },
        "sources": [{"id": "S1", "url": "https://example.com/synthetic", "title": "Synthetic source", "access_date": "2026-07-21", "what_it_supports": "Synthetic background for all bounded inputs."}],
        "dataset_fallbacks": {},
        "scorecard": {
            "ai_replaceable_share": role,
            "pi_dist": selection(0.5), "pi_moat": selection(0.5),
            "t50_years": selection(4.0), "current_adoption_pct": selection(0.3),
            "historical_analogs": selection("Synthetic gradual adoption analogue"),
            "owners_60plus_pct": {"selection": selection(0.3), "succession_shortage_documented": selection(False)},
            "active_consolidators": selection(2), "buy_mult": selection(4.0),
            "exit_mult": selection(8.0), "pricing_structure": selection("Synthetic fixed-fee pricing"),
        },
        "cross_checks": {
            "uplift_vs_A_consistent": "Synthetic productivity and timing are directionally consistent.",
            "terminal_value": {"class": "DURABLE", "justification": "Paid demand survives in this synthetic fixture."},
            "no_proxy_confirmed": "Deal evidence is confined to buyability and multiples.",
            "pricing_model_deflation": "Potential repricing is reflected only in capture.",
        },
        "disclosures": {
            "dataset_mismatch": {"applies": False, "description": "", "sensitivity": []},
            "market_boundary": {"applies": False, "subsegments": [], "dominant_subsegment": "", "selection_basis": ""},
        },
        "confidence_overall": "MED", "heterogeneous": False,
        "top_uncertain_inputs": [{"input": "t50_years", "plausible_range": "2-6 years", "score_impact": "A varies across the stated range."}],
        "reviewer_note": "Synthetic fixture only.",
    }


def review(run_id, outcome="publishable"):
    findings, caveats = [], []
    if outcome == "publishable_with_caveats":
        findings = [{"severity": "caveat", "category": "scope", "input_paths": ["inputs.pi_dist"], "explanation": "The proxy is broad.", "materiality": "The disclosed breadth is unlikely to change the factor direction.", "remediation": "Keep visible as a caveat.", "publication_caveat": "Capture uses a broad disclosed proxy."}]
        caveats = ["Capture uses a broad disclosed proxy."]
    elif outcome == "reject":
        findings = [{"severity": "material", "category": "factor_semantics", "input_paths": ["inputs.pi_dist"], "explanation": "Capture semantics are reversed.", "materiality": "Correcting direction could materially lower C and change the thesis.", "remediation": "Re-estimate pi_dist with the frozen direction."}]
    elif outcome == "invalid":
        findings = [{"severity": "fatal_mechanics", "category": "mechanics", "input_paths": ["scores.S"], "explanation": "Arithmetic does not reproduce.", "materiality": "The score is mechanically unusable.", "remediation": "Re-finalize from a valid packet."}]
    mechanics = {name: True for name in ("schema_valid", "identity_valid", "model_route_valid", "dataset_equal", "finalization_equal", "memo_equal", "arithmetic_valid")}
    if outcome == "invalid":
        mechanics["arithmetic_valid"] = False
    return {
        "naics": "999999", "run_id": run_id,
        "artifact_digests": {"packet_sha256": "0" * 64, "run_sha256": "1" * 64, "memo_sha256": "2" * 64},
        "review_meta": {"model_id": "gpt-5.6-sol", "review_date": "2026-07-21", "prompt_version": "validator-3.1.2"},
        "outcome": outcome, "mechanics": mechanics,
        "source_reviews": [{"source_id": "S1", "url": "https://example.com/synthetic", "accessible": True, "score_driving": True, "support": "supported", "notes": "Synthetic source supports the fixture."}],
        "findings": findings, "publication_caveats": caveats,
        "summary": "Synthetic review summary.",
    }


class V312Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.packet_schema = json.loads((SCHEMAS / "research_packet_v3_1_2.schema.json").read_text())
        cls.run_schema = json.loads((SCHEMAS / "run_record_v3_1_2.schema.json").read_text())
        cls.review_schema = json.loads((SCHEMAS / "review_record_v3_1_2.schema.json").read_text())

    def test_packet_finalizes_and_memo_is_byte_deterministic(self):
        value = packet()
        self.assertEqual([], build.schema_errors(value, self.packet_schema, self.packet_schema))
        record, errors = finalizer.finalize(value, dataset(), "fleet")
        self.assertEqual([], errors)
        self.assertEqual([], build.schema_errors(record, self.run_schema, self.run_schema))
        fresh, errors = finalizer.finalize(copy.deepcopy(value), copy.deepcopy(dataset()), "fleet")
        self.assertEqual([], errors)
        self.assertEqual(record, fresh)
        self.assertEqual(finalizer.render_memo(record), finalizer.render_memo(fresh))
        self.assertEqual("finalizer-3.1.2", record["run_meta"]["finalizer_version"])
        self.assertEqual(record["decision"], build.decide(record["S"], {name: record["scores"][name]["score"] for name in ("V", "C", "A", "B", "M")}, "DURABLE", "MED", json.loads((HERE / "thresholds.json").read_text())))

    def test_python_injects_roles_and_scores(self):
        record, errors = finalizer.finalize(packet(), dataset(), "fleet")
        self.assertFalse(errors)
        roles = record["inputs"]["ai_replaceable_share"]["breakdown_by_role"]
        self.assertEqual(["11-1111", "22-2222", "RESIDUAL"], [item["soc"] for item in roles])
        self.assertAlmostEqual(0.34, record["inputs"]["ai_replaceable_share"]["value"])
        self.assertAlmostEqual(0.17, record["cross_checks"]["uplift_pp"] / 100)
        self.assertEqual("ESTIMATE", record["inputs"]["pi_dist"]["provenance_type"])

    def test_model_route_and_t50_fail_closed(self):
        _record, errors = finalizer.finalize(packet(model="gpt-5.6-sol"), dataset(), "fleet")
        self.assertTrue(any("model_id" in item for item in errors))
        value = packet()
        value["scorecard"]["current_adoption_pct"]["value"] = 0.6
        _record, errors = finalizer.finalize(value, dataset(), "fleet")
        self.assertTrue(any("t50" in item for item in errors))

    def test_exact_prompt_version_is_fail_closed(self):
        value = packet()
        value["run_meta"]["prompt_version"] = "arbitrary-wrong-version"
        self.assertTrue(build.schema_errors(value, self.packet_schema, self.packet_schema))
        _record, errors = finalizer.finalize(value, dataset(), "fleet")
        self.assertTrue(any("prompt_version" in item for item in errors))

    def test_source_reference_and_quality_rules_fail_closed(self):
        value = packet()
        value["scorecard"]["pi_dist"]["source_ids"] = ["S9"]
        _record, errors = finalizer.finalize(value, dataset(), "fleet")
        self.assertTrue(any("unknown source" in item for item in errors))
        value = packet()
        value["scorecard"]["pi_dist"]["evidence_quality"] = "NONE"
        _record, errors = finalizer.finalize(value, dataset(), "fleet")
        self.assertTrue(any("NONE" in item for item in errors))

    def test_safe_calculation_is_recomputed_and_unsafe_syntax_rejected(self):
        value = packet()
        calc = selection(4.0, method="CALCULATED")
        calc["calculation"] = {"expression": "years / two", "operands": [{"name": "years", "value": 8, "source_id": "S1"}, {"name": "two", "value": 2, "source_id": "S1"}]}
        value["scorecard"]["t50_years"] = calc
        record, errors = finalizer.finalize(value, dataset(), "fleet")
        self.assertFalse(errors)
        self.assertEqual(4.0, record["inputs"]["t50_years"]["value"])
        value["scorecard"]["t50_years"]["calculation"]["expression"] = "__import__('os')"
        _record, errors = finalizer.finalize(value, dataset(), "fleet")
        self.assertTrue(any("unsafe calculation" in item for item in errors))

    def test_attempt_two_is_bounded_and_bound_to_prior_id(self):
        value = packet(attempt=2)
        record, errors = finalizer.finalize(value, dataset(), "fleet")
        self.assertFalse(errors)
        self.assertEqual(2, record["run_meta"]["attempt"])
        del value["run_meta"]["remediates_run_id"]
        _record, errors = finalizer.finalize(value, dataset(), "fleet")
        self.assertTrue(any("remediates" in item for item in errors))

    def test_all_four_review_outcomes_validate(self):
        entry = {"naics": "999999", "run_id": "synthetic-v312-a1-999999", "required_validator_model_id": "gpt-5.6-sol", "required_validator_prompt_version": "validator-3.1.2", "source_registry": [{"source_id": "S1", "url": "https://example.com/synthetic", "score_driving": True}], "declared_caveats": [], "artifact_digests": {"packet_sha256": "0" * 64, "run_sha256": "1" * 64, "memo_sha256": "2" * 64}}
        for outcome in ("publishable", "publishable_with_caveats", "reject", "invalid"):
            value = review(entry["run_id"], outcome)
            self.assertEqual([], campaign.review_errors(value, entry, self.review_schema), outcome)

    def test_reject_requires_score_changing_material_finding(self):
        entry = {"naics": "999999", "run_id": "synthetic-v312-a1-999999", "required_validator_model_id": "gpt-5.6-sol", "required_validator_prompt_version": "validator-3.1.2", "source_registry": [{"source_id": "S1", "url": "https://example.com/synthetic", "score_driving": True}], "declared_caveats": [], "artifact_digests": {"packet_sha256": "0" * 64, "run_sha256": "1" * 64, "memo_sha256": "2" * 64}}
        value = review(entry["run_id"], "publishable_with_caveats")
        value["outcome"] = "reject"
        self.assertTrue(any("material" in item for item in campaign.review_errors(value, entry, self.review_schema)))

    def test_fatal_mechanics_precedes_research_rejection(self):
        entry = {"naics": "999999", "run_id": "synthetic-v312-a1-999999", "required_validator_model_id": "gpt-5.6-sol", "required_validator_prompt_version": "validator-3.1.2", "source_registry": [{"source_id": "S1", "url": "https://example.com/synthetic", "score_driving": True}], "declared_caveats": [], "artifact_digests": {"packet_sha256": "0" * 64, "run_sha256": "1" * 64, "memo_sha256": "2" * 64}}
        value = review(entry["run_id"], "invalid")
        value["source_reviews"][0].update({"accessible": False, "support": "unsupported"})
        self.assertEqual([], campaign.review_errors(value, entry, self.review_schema))
        value["outcome"] = "reject"
        self.assertTrue(campaign.review_errors(value, entry, self.review_schema))

    def test_validator_caveat_must_reach_publication_list(self):
        entry = {"naics": "999999", "run_id": "synthetic-v312-a1-999999", "required_validator_model_id": "gpt-5.6-sol", "required_validator_prompt_version": "validator-3.1.2", "source_registry": [{"source_id": "S1", "url": "https://example.com/synthetic", "score_driving": True}], "declared_caveats": [], "artifact_digests": {"packet_sha256": "0" * 64, "run_sha256": "1" * 64, "memo_sha256": "2" * 64}}
        value = review(entry["run_id"], "publishable_with_caveats")
        value["publication_caveats"] = ["Different text."]
        self.assertTrue(any("caveat finding" in item for item in campaign.review_errors(value, entry, self.review_schema)))

    def test_dataset_fallback_sources_are_score_driving(self):
        value, data = packet(), dataset()
        value["sources"].append({"id": "S2", "url": "https://example.com/fallback", "title": "Fallback source", "access_date": "2026-07-21", "what_it_supports": "A synthetic missing labor-share fallback."})
        fallback = selection(0.4, source_ids=["S2"])
        value["dataset_fallbacks"]["labor_share"] = fallback
        data["labor_share"]["value"] = None
        record, errors = finalizer.finalize(value, data, "fleet")
        self.assertFalse(errors)
        self.assertIn("S2", build.v312_score_driving_source_ids(record))
        validator = (REPO / "pipeline" / "template" / "validator_brief_v3_1_2.md").read_text()
        self.assertIn("dataset_inputs.labor_share", validator)
        self.assertIn("dataset_inputs.n_band", validator)
        self.assertIn("dataset_inputs.<name>: <caveat>", validator)

    def test_artifact_digest_mutation_is_detected(self):
        root = Path(tempfile.mkdtemp(prefix="v312_digest_")); self.addCleanup(shutil.rmtree, root)
        value, data = packet(), dataset(); record, errors = finalizer.finalize(value, data, "fleet"); self.assertFalse(errors)
        run_id = record["run_meta"]["run_id"]
        packet_path = root / "pipeline" / "packets" / "999999" / (run_id + ".json")
        run_path = root / "pipeline" / "runs" / "999999" / (run_id + ".json")
        memo_path = root / "pipeline" / "memos" / "999999" / (run_id + ".md")
        dataset_path = root / "pipeline" / "datasets" / "derived" / "999999.json"
        for path in (packet_path, run_path, memo_path, dataset_path): path.parent.mkdir(parents=True, exist_ok=True)
        packet_path.write_text(json.dumps(value, indent=2) + "\n"); run_path.write_bytes(finalizer.serialize_record(record)); memo_path.write_text(finalizer.render_memo(record)); dataset_path.write_text(json.dumps(data))
        entry = campaign.artifact_entry("fleet", "999999", str(run_path), record, str(root))
        self.assertEqual([], campaign.validate_artifact(entry, str(root)))
        value["narrative"]["executive_view"] += " Mutated after review."
        packet_path.write_text(json.dumps(value, indent=2) + "\n")
        self.assertTrue(any("bytes differ" in item for item in campaign.validate_artifact(entry, str(root))))

    def test_prior_remediation_review_is_fully_validated(self):
        root = Path(tempfile.mkdtemp(prefix="v312_history_")); self.addCleanup(shutil.rmtree, root)
        history = []
        for attempt in (1, 2):
            value = packet(attempt=attempt); record, errors = finalizer.finalize(value, dataset(), "fleet"); self.assertFalse(errors)
            run_id = record["run_meta"]["run_id"]
            packet_path = root / "pipeline" / "packets" / "999999" / (run_id + ".json")
            run_path = root / "pipeline" / "runs" / "999999" / (run_id + ".json")
            memo_path = root / "pipeline" / "memos" / "999999" / (run_id + ".md")
            for path in (packet_path, run_path, memo_path): path.parent.mkdir(parents=True, exist_ok=True)
            packet_path.write_text(json.dumps(value, indent=2) + "\n"); run_path.write_bytes(finalizer.serialize_record(record)); memo_path.write_text(finalizer.render_memo(record))
            history.append(("2026-07-21", run_id, str(run_path), record))
        first_entry = campaign.artifact_entry("fleet", "999999", history[0][2], history[0][3], str(root))
        prior = review(history[0][1], "reject"); prior["artifact_digests"] = first_entry["artifact_digests"]
        review_path = root / first_entry["review_path"]; review_path.parent.mkdir(parents=True, exist_ok=True); review_path.write_text(json.dumps(prior))
        self.assertEqual([], campaign.validate_history("fleet", "999999", history, str(root)))
        prior["run_id"] = "wrong-run"; review_path.write_text(json.dumps(prior))
        self.assertTrue(any("prior review invalid" in item for item in campaign.validate_history("fleet", "999999", history, str(root))))

    def test_build_includes_both_publishable_tiers_and_excludes_reject(self):
        for outcome, expected_published in (("publishable", 1), ("publishable_with_caveats", 1), ("reject", 0)):
            root = tempfile.mkdtemp(prefix="v312_build_")
            self.addCleanup(shutil.rmtree, root)
            runs = Path(root) / "runs" / "999999"
            reviews = Path(root) / "reviews" / "999999"
            packets = Path(root) / "pipeline" / "packets" / "999999"
            memos = Path(root) / "pipeline" / "memos" / "999999"
            runs.mkdir(parents=True); reviews.mkdir(parents=True); packets.mkdir(parents=True); memos.mkdir(parents=True)
            packet_value = packet()
            record, errors = finalizer.finalize(packet_value, dataset(), "fleet")
            self.assertFalse(errors)
            run_path = runs / "run.json"
            packet_path = packets / (record["run_meta"]["run_id"] + ".json")
            memo_path = memos / (record["run_meta"]["run_id"] + ".md")
            run_path.write_bytes(finalizer.serialize_record(record))
            packet_path.write_text(json.dumps(packet_value, indent=2) + "\n")
            memo_path.write_text(finalizer.render_memo(record))
            review_value = review(record["run_meta"]["run_id"], outcome)
            review_value["artifact_digests"] = {
                "packet_sha256": build.sha256_file(packet_path),
                "run_sha256": build.sha256_file(run_path),
                "memo_sha256": build.sha256_file(memo_path),
            }
            (reviews / (record["run_meta"]["run_id"] + ".json")).write_text(json.dumps(review_value))
            result = build.run_build(
                repo_root=root, runs_dir=str(Path(root) / "runs"), review_dir=str(Path(root) / "reviews"),
                thresholds_path=str(HERE / "thresholds.json"), schemas_dir=str(SCHEMAS),
                expectations_path=str(HERE / "deep_dive_expectations.json"),
                site_out=str(Path(root) / "six.json"), stats_out=str(Path(root) / "stats.json"),
                flags_out=str(Path(root) / "flags.json"), reconciliation_out=str(Path(root) / "reconciliation.md"),
            )
            self.assertTrue(result["ok"], result.get("errors"))
            self.assertEqual(expected_published, result["stats"]["published"])
            self.assertEqual([] if expected_published else ["999999"], result["stats"]["rejected"])
            if outcome == "publishable_with_caveats":
                self.assertEqual(["Capture uses a broad disclosed proxy."], result["site"]["records"][0]["publication_caveats"])

    def test_prompt_routing_and_all_63_render_deterministically(self):
        route = assemble.VERSION_PATHS["3.1.2"]
        self.assertEqual(REPO / "pipeline" / "template" / "prompt_template_v3_1_2.md", route["template"])
        template = route["template"].read_text()
        targets = json.loads(assemble.TARGETS_PATH.read_text())["codes"]
        first = {item["naics"]: assemble.assemble_one(item["naics"], item["title"], template, "3.1.2") for item in targets}
        second = {item["naics"]: assemble.assemble_one(item["naics"], item["title"], template, "3.1.2") for item in targets}
        self.assertEqual(63, len(first)); self.assertEqual(first, second)
        for code, text in first.items():
            assemble.validate_prompt_text(code, text)

    def test_frozen_earlier_artifacts_are_unchanged(self):
        expected_files = {
            "pipeline/template/prompt_template_v3.md": "57d1ff51afd7a74d02b9334e17b7cbf79f3151d372521df91b00618c2e9e82dd",
            "pipeline/template/prompt_template_v3_1.md": "b639675d4defe72b7741b1f7fc08805b94f1445eeb762108fb294920f3d6176e",
            "pipeline/template/prompt_template_v3_1_1.md": "d867f7a4fbace473a5d310a2fd3b8d23e2d1843048b348b74e5e7eb264a72d25",
            "pipeline/build/schemas/run_record.schema.json": "42a6285a43a032cb2ad8038743e60448e8e3acd19c3634a1beca8ace0c6e3d48",
            "pipeline/build/schemas/run_record_v3_1.schema.json": "9f4b27da46ff3fa8e2fa1e7d1de67b71582820018a7ca1c6f590e9cbae9ecbfa",
            "pipeline/build/schemas/run_record_v3_1_1.schema.json": "5b2aa5879aff58937a9a77db83bf3fe556dab95551a9e0ae8e896907405c5cdb",
            "pipeline/build/thresholds.json": "3ea5a6240182726cc0451564665062955e6d178e5155d638a851f544c183e8af",
            "pipeline/golden/golden_set.json": "5c97a8b725da363d38888c91bffbdd4ef03eb4c90a0e602915f4440be1bab988",
        }
        for relative, digest in expected_files.items():
            self.assertEqual(digest, hashlib.sha256((REPO / relative).read_bytes()).hexdigest(), relative)
        expected_trees = {"pipeline/prompts": (75, "6a1290314a24c65555c98fbe2f9467fc29c8f9733f03c047cee5bb3ba72e9481"), "pipeline/prompts_v3_1": (63, "a3e1cb011ffca09b4b9adf047ca3590b7b842af742addb45fbb274228c25f6d0"), "pipeline/prompts_v3_1_1": (63, "bda3176d8b36c6136d09010d4cb9a8c0eb53250be912d30a72e5de968f81d420")}
        for relative, (count, digest) in expected_trees.items():
            directory = REPO / relative; files = sorted(item for item in directory.rglob("*") if item.is_file()); tree = hashlib.sha256()
            for item in files:
                tree.update(str(item.relative_to(directory)).encode()); tree.update(b"\0"); tree.update(item.read_bytes()); tree.update(b"\0")
            self.assertEqual(count, len(files), relative); self.assertEqual(digest, tree.hexdigest(), relative)


if __name__ == "__main__":
    unittest.main(verbosity=2)
