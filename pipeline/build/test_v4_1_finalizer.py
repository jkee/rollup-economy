#!/usr/bin/env python3

import copy
import importlib.util
import json
import os
from pathlib import Path
import tempfile
import unittest


HERE = Path(__file__).resolve().parent


def load_module(name, filename):
    spec = importlib.util.spec_from_file_location(name, HERE / filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


finalizer = load_module("v4_1_finalizer_tests", "finalize_run_v4_1.py")


def proxy_bridge():
    return {
        "population": "Target-band service operators",
        "geography": "United States",
        "period": "2024-2026",
        "unit": "Share of target cash cost or supported outcome",
        "business_model": "Recurring accountable business service",
    }


def selection(value, low, high, state="PROXY", method="ESTIMATE", quality="MED"):
    result = {
        "value": value, "range": {"low": low, "high": high}, "method": method,
        "evidence_state": state, "evidence_quality": quality, "confidence": "MED",
        "source_ids": ["S1"] if state in ("DIRECT", "PROXY") else [],
        "rationale": "Synthetic evidence rationale sufficient for deterministic contract tests.",
        "caveats": [],
    }
    if state == "PROXY":
        result["bridge"] = proxy_bridge()
    return result


def missing_selection():
    return selection(None, None, None, state="MISSING", quality="NONE")


def dataset():
    return {
        "dataset_version": "4.1", "snapshot_id": "synthetic-999999-v1",
        "naics": "999999", "title": "Synthetic Services",
        "labor_share": {"value": 0.5, "quality": "HIGH", "basis": "Synthetic labor basis."},
        "n_total": {"value": 2000, "quality": "HIGH", "basis": "Synthetic total count."},
        "n_band": {"value": 1000, "quality": "HIGH", "basis": "Synthetic target-band count."},
        "role_mix": {
            "basis": "Exact synthetic target-compatible occupational basis.", "quality": "HIGH",
            "occupations": [
                {"soc": "11-0001", "title": "Synthetic operations", "employment_share": 0.55, "wage_share": 0.6},
                {"soc": "13-0001", "title": "Synthetic analysts", "employment_share": 0.35, "wage_share": 0.4},
            ],
        },
        "provenance": {"derivation_version": "synthetic-1", "source_manifest_sha256": "a" * 64,
                       "vintage": "2026 synthetic"},
    }


def _archetype():
    return {
        "selected_id": "core-operator",
        "alternatives": [{
            "id": "core-operator", "name": "Frozen core operator",
            "inclusion_criteria": ["Recurring accountable service"],
            "exclusion_criteria": ["Pure product resale"],
            "band_count": {"base": 900, "low": 800, "high": 1000},
            "source_ids": ["A1"], "rationale": "Highest frozen lower-bound eligible count."
        }],
        "residual": {"name": "Residual operators", "band_count": {"base": 100, "low": 0, "high": 200},
                     "rationale": "Remainder outside the selected archetype."},
        "enumeration_coverage": {"base": 0.9, "low": 0.8, "high": 1.0},
        "sources": [{"id": "A1", "url": "https://example.com/archetype", "title": "Archetype source", "vintage": "2026"}],
        "selection_basis": "Frozen before economics using the greatest lower-bound target count.",
        "selection_uncertainty": False,
    }


def industry_spec(dataset_sha, mode="dataset"):
    value_basis = {
        "mode": mode, "scope": "Frozen target cash-cost basis.",
        "labor_contractor_cash_cost_share": None, "roles": [], "sources": [],
        "bridge": None,
        "rationale": "Frozen independently of economic scoring.", "caveats": [],
    }
    if mode == "target_specific":
        value_basis.update({
            "labor_contractor_cash_cost_share": {
                "value": 0.45, "range": {"low": 0.35, "high": 0.55}, "evidence_quality": "MED",
                "source_ids": ["B1"], "rationale": "Target-specific cash-cost study.", "caveats": []},
            "roles": [
                {"role_id": "OPS", "title": "Target operations", "role_cash_cost_weight": 0.7,
                 "source_ids": ["B1"], "rationale": "Target staffing study."},
                {"role_id": "ADMIN", "title": "Target administration", "role_cash_cost_weight": 0.3,
                 "source_ids": ["B1"], "rationale": "Target staffing study."},
            ],
            "sources": [{"id": "B1", "url": "https://example.com/basis", "title": "Basis source", "vintage": "2026"}],
        })
    elif mode == "assumption":
        value_basis.update({
            "labor_contractor_cash_cost_share": {
                "base": 0.45, "range": {"low": 0.35, "high": 0.55},
                "evidence_state": "ASSUMPTION", "evidence_quality": "NONE", "source_ids": [],
                "rationale": "Explicit bounded assumption made before economic scoring.", "caveats": []},
            "roles": [
                {"role_id": "OPS", "title": "Assumed operations", "role_cash_cost_weight": 0.7,
                 "source_ids": [], "rationale": "Explicit frozen role-weight assumption."},
                {"role_id": "ADMIN", "title": "Assumed administration", "role_cash_cost_weight": 0.3,
                 "source_ids": [], "rationale": "Explicit frozen role-weight assumption."},
            ],
        })
    return {
        "spec_version": "4.1", "naics": "999999", "title": "Synthetic Services",
        "dataset_snapshot": {"path": "pipeline/datasets/v4_1/999999.json", "sha256": dataset_sha},
        "target_archetype": _archetype(), "value_basis": value_basis,
        "source_hints": [{"area": "synthetic", "source": "Synthetic registry", "why": "Testing",
                          "uncertain_exists": False}],
        "research_questions": {name: ["Synthetic question?"] for name in
                               ("implementation", "commercial_retention", "sale_availability",
                                "valuation_robustness", "operator_survival")},
        "special_notes": [],
    }


def packet(role_ids=("11-0001", "13-0001")):
    long_text = "Synthetic narrative text long enough to satisfy the closed v4.1 research contract and renderer tests."
    role_set = {
        "method": "ESTIMATE", "evidence_state": "PROXY", "evidence_quality": "MED", "confidence": "MED",
        "source_ids": ["S1"], "rationale": long_text, "caveats": [],
        "bridge": proxy_bridge(),
        "roles": [{"role_id": role_id, "removable_fraction": 0.5,
                   "range": {"low": 0.25, "high": 0.75}, "rationale": long_text} for role_id in role_ids],
    }
    return {
        "naics": "999999", "title": "Synthetic Services",
        "sources": [{"id": "S1", "url": "https://example.com/research", "title": "Synthetic research",
                     "access_date": "2026-07-21", "what_it_supports": "Every synthetic authored input."}],
        "narrative": {key: long_text for key in
                      ("executive_view", "technical_value", "implementation", "commercial_capture",
                       "buyability", "entry_and_exit", "operator_survival", "risks_and_uncertainty")},
        "dataset_fallbacks": {},
        "inputs": {
            "target_archetype_coverage": selection(0.9, 0.8, 1.0),
            "target_role_judgments": role_set,
            "implementation_realization": {
                "value": [0.2, 0.4, 0.6, 0.7, 0.8], "low": [0.1, 0.2, 0.3, 0.4, 0.5],
                "high": [0.3, 0.5, 0.7, 0.85, 0.95], "method": "ESTIMATE", "evidence_state": "PROXY",
                "evidence_quality": "MED", "confidence": "MED", "source_ids": ["S1"],
                "rationale": long_text, "caveats": [], "bridge": proxy_bridge()},
            "commercial_capture_share": selection(0.55, 0.35, 0.7),
            "five_year_sale_availability": selection(0.2, 0.1, 0.3),
            "buy_multiple": selection(5.0, 4.0, 6.0),
            "downside_exit_multiple": selection(4.0, 3.0, 5.0),
            "operator_controlled_demand_share_y5": selection(0.75, 0.55, 0.9),
        },
        "cross_checks": {key: long_text for key in
                         ("target_identity_preserved", "implementation_costs_only_in_I",
                          "commercial_leakage_only_in_C", "competition_not_double_counted",
                          "survival_is_operator_controlled_demand")},
        "confidence_overall": "MED",
        "top_uncertain_inputs": [{"input": "commercial_capture_share", "range": "0.35-0.70",
                                  "score_impact": long_text}], "reviewer_note": "",
    }


def write_json(path, value):
    path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")


class Fixture:
    def __init__(self, root, *, mode="dataset", null_n_band=False):
        self.root = Path(root)
        self.dataset_path = self.root / "dataset.json"
        self.spec_path = self.root / "spec.json"
        self.packet_path = self.root / "packet.json"
        self.envelope_path = self.root / "envelope.json"
        self.prompt_path = self.root / "prompt.md"
        self.methodology_path = self.root / "methodology.md"
        self.prompt_path.write_text("# Frozen synthetic assembled prompt\n", encoding="utf-8")
        self.methodology_path.write_text("# Frozen synthetic methodology\n", encoding="utf-8")
        data = dataset()
        if null_n_band:
            data["n_band"].update(value=None, quality="NONE")
        write_json(self.dataset_path, data)
        spec_value = industry_spec(finalizer.sha256_file(self.dataset_path), mode=mode)
        write_json(self.spec_path, spec_value)
        role_ids = (("OPS", "ADMIN") if mode in ("target_specific", "assumption")
                    else (("11-0001", "13-0001") if mode == "dataset" else ()))
        packet_value = packet(role_ids)
        if mode == "missing":
            packet_value["inputs"]["target_role_judgments"].update(
                method="ESTIMATE", evidence_state="MISSING", evidence_quality="NONE", source_ids=[], roles=[])
            packet_value["inputs"]["target_role_judgments"].pop("bridge")
        write_json(self.packet_path, packet_value)
        hashes = {
            "prompt_sha256": finalizer.sha256_file(self.prompt_path),
            "dataset_sha256": finalizer.sha256_file(self.dataset_path),
            "spec_sha256": finalizer.sha256_file(self.spec_path),
            "methodology_sha256": finalizer.sha256_file(self.methodology_path),
            "thresholds_sha256": finalizer.sha256_file(HERE / "thresholds_v4_1.json"),
            "research_packet_schema_sha256": finalizer.sha256_file(HERE / "schemas/research_packet_v4_1.schema.json"),
            "dataset_schema_sha256": finalizer.sha256_file(HERE / "schemas/dataset_v4_1.schema.json"),
            "industry_spec_schema_sha256": finalizer.sha256_file(HERE / "schemas/industry_spec_v4_1.schema.json"),
            "run_record_schema_sha256": finalizer.sha256_file(HERE / "schemas/run_record_v4_1.schema.json"),
            "scoring_sha256": finalizer.sha256_file(HERE / "v4_1_scoring.py"),
            "finalizer_sha256": finalizer.sha256_file(HERE / "finalize_run_v4_1.py"),
        }
        envelope = {
            "envelope_version": "4.1", "kind": "fleet", "naics": "999999", "title": "Synthetic Services",
            "run_id": "2026-07-21_synthetic_v41_999999", "run_date": "2026-07-21", "attempt": 1,
            "remediates_run_id": None, "issued_by_task_path": "/root", "codex_task_path": "/root/research_999999",
            "fork_policy": "none", "role": "research", "model_id": "gpt-5.6-terra",
            **hashes,
        }
        write_json(self.envelope_path, envelope)
        self.reload()

    def reload(self):
        self.packet = finalizer.load_json(self.packet_path)
        self.dataset = finalizer.load_json(self.dataset_path)
        self.spec = finalizer.load_json(self.spec_path)
        self.envelope = finalizer.load_json(self.envelope_path)
        self.paths = {"packet": str(self.packet_path), "dataset": str(self.dataset_path),
                      "spec": str(self.spec_path), "envelope": str(self.envelope_path),
                      "prompt": str(self.prompt_path), "methodology": str(self.methodology_path)}

    def rewrite_packet(self):
        write_json(self.packet_path, self.packet)
        self.reload()

    def finalize(self):
        return finalizer.finalize(self.packet, self.dataset, self.spec, self.envelope, self.paths)


class V41FinalizerTests(unittest.TestCase):
    def test_closed_packet_finalizes_deterministically(self):
        with tempfile.TemporaryDirectory() as root:
            fixture = Fixture(root)
            record, errors = fixture.finalize()
            self.assertEqual([], errors)
            second, errors = fixture.finalize()
            self.assertEqual([], errors)
            self.assertEqual(finalizer.serialize_record(record), finalizer.serialize_record(second))
            self.assertEqual(finalizer.render_memo(record), finalizer.render_memo(second))
            self.assertEqual(["11-0001", "13-0001"],
                             [item["role_id"] for item in record["inputs"]["target_role_mix"]["roles"]])

    def test_unknown_selection_property_rejected(self):
        with tempfile.TemporaryDirectory() as root:
            fixture = Fixture(root)
            fixture.packet["inputs"]["commercial_capture_share"]["attacker"] = True
            fixture.rewrite_packet()
            record, errors = fixture.finalize()
            self.assertIsNone(record)
            self.assertTrue(any("additional property" in item for item in errors))

    def test_proxy_bridge_is_exact_closed_and_preserved(self):
        with tempfile.TemporaryDirectory() as root:
            fixture = Fixture(root)
            record, errors = fixture.finalize()
            self.assertEqual([], errors)
            retained = record["inputs"]["commercial_retention"]
            self.assertEqual(proxy_bridge(), retained["bridge"])
            self.assertTrue(retained["bridge_supported"])
            self.assertTrue(record["inputs"]["implementation_ramp"]["r1"]["bridge_supported"])
            self.assertTrue(record["inputs"]["target_role_mix"]["roles"][0]
                            ["removable_fraction"]["bridge_supported"])

            del fixture.packet["inputs"]["commercial_capture_share"]["bridge"]["period"]
            fixture.rewrite_packet()
            record, errors = fixture.finalize()
            self.assertIsNone(record)
            self.assertTrue(any("bridge" in item and "period" in item for item in errors))

    def test_bridge_is_required_only_for_proxy(self):
        with tempfile.TemporaryDirectory() as root:
            fixture = Fixture(root)
            del fixture.packet["inputs"]["commercial_capture_share"]["bridge"]
            fixture.rewrite_packet()
            record, errors = fixture.finalize()
            self.assertIsNone(record)
            self.assertTrue(any("PROXY requires" in item or "missing required key 'bridge'" in item
                                for item in errors))

        with tempfile.TemporaryDirectory() as root:
            fixture = Fixture(root)
            item = fixture.packet["inputs"]["commercial_capture_share"]
            item.update(evidence_state="DIRECT", method="OBSERVED")
            fixture.rewrite_packet()
            record, errors = fixture.finalize()
            self.assertIsNone(record)
            self.assertTrue(any("bridge is forbidden" in item for item in errors))

    def test_missing_numeric_remains_partially_identified(self):
        with tempfile.TemporaryDirectory() as root:
            fixture = Fixture(root)
            fixture.packet["inputs"]["commercial_capture_share"] = missing_selection()
            fixture.rewrite_packet()
            record, errors = fixture.finalize()
            self.assertEqual([], errors)
            self.assertIsNone(record["scenarios"]["base"]["scores"]["C"])
            self.assertEqual((0.0, 10.0), (record["scenarios"]["low"]["scores"]["C"],
                                          record["scenarios"]["high"]["scores"]["C"]))
            self.assertEqual("EVIDENCE_FIRST", record["decision"]["action"])

    def test_null_dataset_n_band_never_crashes(self):
        with tempfile.TemporaryDirectory() as root:
            fixture = Fixture(root, null_n_band=True)
            record, errors = fixture.finalize()
            self.assertEqual([], errors)
            self.assertIsNone(record["dataset_inputs"]["n_band"]["value"])
            self.assertIsNone(record["scenarios"]["base"]["scores"]["B"])
            self.assertEqual(10.0, record["scenarios"]["high"]["scores"]["B"])

    def test_unbridged_dataset_role_basis_propagates_none_quality_and_is_unproven(self):
        with tempfile.TemporaryDirectory() as root:
            fixture = Fixture(root)
            fixture.dataset["role_mix"]["quality"] = "NONE"
            write_json(fixture.dataset_path, fixture.dataset)
            fixture.spec["dataset_snapshot"]["sha256"] = finalizer.sha256_file(fixture.dataset_path)
            write_json(fixture.spec_path, fixture.spec)
            fixture.envelope["dataset_sha256"] = finalizer.sha256_file(fixture.dataset_path)
            fixture.envelope["spec_sha256"] = finalizer.sha256_file(fixture.spec_path)
            write_json(fixture.envelope_path, fixture.envelope)
            fixture.reload()
            record, errors = fixture.finalize()
            self.assertEqual([], errors)
            basis = record["inputs"]["target_role_mix"]
            self.assertEqual(("PROXY", "NONE", False),
                             (basis["basis_evidence_state"], basis["basis_evidence_quality"],
                              basis["basis_bridge_supported"]))
            labor = record["inputs"]["target_labor_cost_share"]
            self.assertEqual(("PROXY", False), (labor["evidence_state"], labor["bridge_supported"]))
            self.assertEqual("UNPROVEN", record["decision"]["evidence_readiness"]["status"])

    def test_dataset_basis_bridge_is_machine_readable_and_preserved(self):
        with tempfile.TemporaryDirectory() as root:
            fixture = Fixture(root)
            fixture.spec["value_basis"]["bridge"] = proxy_bridge()
            write_json(fixture.spec_path, fixture.spec)
            fixture.envelope["spec_sha256"] = finalizer.sha256_file(fixture.spec_path)
            write_json(fixture.envelope_path, fixture.envelope)
            fixture.reload()
            record, errors = fixture.finalize()
            self.assertEqual([], errors)
            basis = record["inputs"]["target_role_mix"]
            self.assertEqual(proxy_bridge(), basis["basis_bridge"])
            self.assertTrue(basis["basis_bridge_supported"])
            labor = record["inputs"]["target_labor_cost_share"]
            self.assertEqual(proxy_bridge(), labor["bridge"])
            self.assertTrue(labor["bridge_supported"])

    def test_dataset_duplicate_soc_and_invalid_sums_rejected(self):
        data = dataset()
        duplicate = copy.deepcopy(data["role_mix"]["occupations"][0])
        duplicate["wage_share"] = 0.1
        data["role_mix"]["occupations"].append(duplicate)
        errors = finalizer.dataset_errors(data)
        self.assertTrue(any("unique" in item for item in errors))
        data = dataset()
        data["role_mix"]["occupations"][0]["wage_share"] = 0.8
        data["role_mix"]["occupations"][1]["wage_share"] = 0.4
        self.assertTrue(any("sum exceeds" in item for item in finalizer.dataset_errors(data)))

    def test_invalid_dataset_fallback_rejected(self):
        with tempfile.TemporaryDirectory() as root:
            fixture = Fixture(root, null_n_band=True)
            fixture.packet["dataset_fallbacks"]["n_band"] = selection(
                3.5, 2.5, 4.5, state="ASSUMPTION", quality="NONE")
            fixture.rewrite_packet()
            record, errors = fixture.finalize()
            self.assertIsNone(record)
            self.assertTrue(any("integers" in item for item in errors))

    def test_source_free_assumption_fallback_is_forbidden_without_frozen_spec_rule(self):
        with tempfile.TemporaryDirectory() as root:
            fixture = Fixture(root, null_n_band=True)
            fixture.packet["dataset_fallbacks"]["n_band"] = selection(
                500, 300, 700, state="ASSUMPTION", quality="NONE")
            fixture.rewrite_packet()
            record, errors = fixture.finalize()
            self.assertIsNone(record)
            self.assertIsNone(fixture.dataset["n_band"]["value"])
            self.assertTrue(any("frozen deterministic spec fallback" in item for item in errors))

    def test_n_band_fallback_must_be_explicit_assumption(self):
        with tempfile.TemporaryDirectory() as root:
            fixture = Fixture(root, null_n_band=True)
            fixture.packet["dataset_fallbacks"]["n_band"] = selection(500, 300, 700)
            fixture.rewrite_packet()
            record, errors = fixture.finalize()
            self.assertIsNone(record)
            self.assertTrue(any("frozen deterministic spec fallback" in item for item in errors))

    def test_role_identity_cannot_be_relabelled(self):
        with tempfile.TemporaryDirectory() as root:
            fixture = Fixture(root)
            fixture.packet["inputs"]["target_role_judgments"]["roles"][0]["role_id"] = "99-9999"
            fixture.rewrite_packet()
            record, errors = fixture.finalize()
            self.assertIsNone(record)
            self.assertTrue(any("exactly equal frozen spec roles" in item for item in errors))

    def test_target_specific_roles_and_weights_are_injected_from_spec(self):
        with tempfile.TemporaryDirectory() as root:
            fixture = Fixture(root, mode="target_specific")
            record, errors = fixture.finalize()
            self.assertEqual([], errors)
            roles = record["inputs"]["target_role_mix"]["roles"]
            self.assertEqual([("OPS", "Target operations", 0.7), ("ADMIN", "Target administration", 0.3)],
                             [(item["role_id"], item["role"], item["cost_weight"]) for item in roles])
            labor = record["inputs"]["target_labor_cost_share"]
            self.assertEqual(0.45, labor["value"])
            self.assertEqual(("DIRECT", "OBSERVED", False),
                             (labor["evidence_state"], labor["method"], labor["bridge_supported"]))
            self.assertNotIn("bridge", labor)

    def test_assumption_basis_is_frozen_source_free_and_unproven(self):
        with tempfile.TemporaryDirectory() as root:
            fixture = Fixture(root, mode="assumption")
            record, errors = fixture.finalize()
            self.assertEqual([], errors)
            roles = record["inputs"]["target_role_mix"]["roles"]
            self.assertEqual([("OPS", "Assumed operations", 0.7),
                              ("ADMIN", "Assumed administration", 0.3)],
                             [(item["role_id"], item["role"], item["cost_weight"]) for item in roles])
            labor = record["inputs"]["target_labor_cost_share"]
            self.assertEqual((0.45, {"low": 0.35, "high": 0.55}),
                             (labor["value"], labor["range"]))
            self.assertEqual(("ASSUMPTION", "NONE", []),
                             (labor["evidence_state"], labor["evidence_quality"], labor["source_ids"]))
            self.assertEqual("UNPROVEN", record["decision"]["evidence_readiness"]["status"])

    def test_missing_value_basis_yields_unresolved_v(self):
        with tempfile.TemporaryDirectory() as root:
            fixture = Fixture(root, mode="missing")
            record, errors = fixture.finalize()
            self.assertEqual([], errors)
            self.assertEqual("missing", record["inputs"]["target_role_mix"]["spec_mode"])
            self.assertIsNone(record["scenarios"]["base"]["scores"]["V"])
            self.assertEqual((0.0, 10.0), (record["scenarios"]["low"]["scores"]["V"],
                                          record["scenarios"]["high"]["scores"]["V"]))

    def test_calculation_requires_every_operand_and_fails_closed(self):
        with tempfile.TemporaryDirectory() as root:
            fixture = Fixture(root)
            item = fixture.packet["inputs"]["commercial_capture_share"]
            item.update(value=0.5, range={"low": 0.4, "high": 0.6}, method="CALCULATED",
                        evidence_state="DIRECT", evidence_quality="HIGH",
                        calculation={"expression": "0.5", "operands": [
                            {"name": "unused", "value": 999, "source_id": "S1"}]})
            item.pop("bridge")
            fixture.rewrite_packet()
            record, errors = fixture.finalize()
            self.assertIsNone(record)
            self.assertTrue(any("unused" in item for item in errors))
            with self.assertRaises(finalizer.ContractError):
                finalizer.safe_calculation({"expression": "1" + "0" * 400,
                                            "operands": [{"name": "unused", "value": 1, "source_id": "S1"}]})

    def test_valid_decimal_calculation_is_preserved_and_resolved(self):
        with tempfile.TemporaryDirectory() as root:
            fixture = Fixture(root)
            item = fixture.packet["inputs"]["commercial_capture_share"]
            item.update(value=0.5, range={"low": 0.4, "high": 0.6}, method="CALCULATED",
                        evidence_state="DIRECT", evidence_quality="HIGH",
                        calculation={"expression": "gross / total", "operands": [
                            {"name": "gross", "value": 1, "source_id": "S1"},
                            {"name": "total", "value": 2, "source_id": "S1"}]})
            item.pop("bridge")
            fixture.rewrite_packet()
            record, errors = fixture.finalize()
            self.assertEqual([], errors)
            retained = record["inputs"]["commercial_retention"]
            self.assertEqual("SAFE_CALCULATION", retained["resolution_type"])
            self.assertEqual(retained["authored_value"], retained["value"])

    def test_digest_and_attempt_rules_fail_closed(self):
        with tempfile.TemporaryDirectory() as root:
            fixture = Fixture(root)
            fixture.envelope["dataset_sha256"] = "0" * 64
            errors = finalizer.envelope_errors(fixture.envelope, fixture.packet, fixture.dataset, fixture.spec, fixture.paths)
            self.assertTrue(any("dataset_sha256" in item for item in errors))
            fixture.envelope["dataset_sha256"] = finalizer.sha256_file(fixture.dataset_path)
            fixture.envelope["prompt_sha256"] = "0" * 64
            errors = finalizer.envelope_errors(fixture.envelope, fixture.packet, fixture.dataset, fixture.spec, fixture.paths)
            self.assertTrue(any("prompt_sha256 does not match exact artifact" in item for item in errors))
            fixture.envelope["prompt_sha256"] = finalizer.sha256_file(fixture.prompt_path)
            fixture.envelope["methodology_sha256"] = "0" * 64
            errors = finalizer.envelope_errors(fixture.envelope, fixture.packet, fixture.dataset, fixture.spec, fixture.paths)
            self.assertTrue(any("methodology_sha256 does not match exact artifact" in item for item in errors))
            fixture.envelope["methodology_sha256"] = finalizer.sha256_file(fixture.methodology_path)
            fixture.envelope.update(attempt=2, remediates_run_id="")
            errors = finalizer.envelope_errors(fixture.envelope, fixture.packet, fixture.dataset, fixture.spec, fixture.paths)
            self.assertTrue(any("non-empty remediates" in item for item in errors))

            fixture.envelope.update(attempt=1, remediates_run_id=None, provider_response_id="unavailable")
            errors = finalizer.envelope_errors(fixture.envelope, fixture.packet, fixture.dataset, fixture.spec, fixture.paths)
            self.assertTrue(any("unknown keys" in item and "provider_response_id" in item for item in errors))
            self.assertEqual(("/root", "/root/research_999999"),
                             (fixture.envelope["issued_by_task_path"], fixture.envelope["codex_task_path"]))

    def test_archetype_selection_uncertainty_forces_unproven(self):
        with tempfile.TemporaryDirectory() as root:
            fixture = Fixture(root)
            fixture.spec["target_archetype"]["alternatives"][0]["band_count"] = {
                "base": 500, "low": 400, "high": 600}
            fixture.spec["target_archetype"]["alternatives"].append({
                "id": "secondary-operator", "name": "Frozen secondary operator",
                "inclusion_criteria": ["Adjacent accountable service"],
                "exclusion_criteria": ["Core operator"],
                "band_count": {"base": 400, "low": 350, "high": 500},
                "source_ids": ["A1"], "rationale": "Second-largest frozen alternative."})
            fixture.spec["target_archetype"]["selection_uncertainty"] = True
            fixture.packet["inputs"]["target_archetype_coverage"].update(
                value=0.5, range={"low": 0.4, "high": 0.6})
            write_json(fixture.spec_path, fixture.spec)
            write_json(fixture.packet_path, fixture.packet)
            fixture.envelope["spec_sha256"] = finalizer.sha256_file(fixture.spec_path)
            write_json(fixture.envelope_path, fixture.envelope)
            fixture.reload()
            record, errors = fixture.finalize()
            self.assertEqual([], errors)
            self.assertTrue(record["inputs"]["target_archetype"]["selection_uncertainty"])
            self.assertEqual("UNPROVEN", record["decision"]["evidence_readiness"]["status"])

    def test_archetype_objective_reconciliation_and_packet_coverage_fail_closed(self):
        with tempfile.TemporaryDirectory() as root:
            fixture = Fixture(root)
            fixture.spec["target_archetype"]["residual"]["band_count"]["base"] = 99
            errors = finalizer.spec_errors(fixture.spec, fixture.dataset)
            self.assertTrue(any("plus residual must equal" in item for item in errors))

            fixture.spec = industry_spec(finalizer.sha256_file(fixture.dataset_path))
            fixture.spec["target_archetype"]["alternatives"].append({
                "id": "aaa-operator", "name": "Tied alternative",
                "inclusion_criteria": ["Tied population"], "exclusion_criteria": ["Core population"],
                "band_count": {"base": 900, "low": 800, "high": 1000},
                "source_ids": ["A1"], "rationale": "Synthetic exact tie."})
            errors = finalizer.spec_errors(fixture.spec, fixture.dataset)
            self.assertTrue(any("lexicographically smallest" in item for item in errors))

        with tempfile.TemporaryDirectory() as root:
            fixture = Fixture(root)
            fixture.packet["inputs"]["target_archetype_coverage"].update(
                value=1.0, range={"low": 0.8, "high": 1.0})
            fixture.rewrite_packet()
            record, errors = fixture.finalize()
            self.assertIsNone(record)
            self.assertTrue(any("selected base band_count / n_band" in item for item in errors))

    def test_dataset_schema_is_closed(self):
        data = dataset()
        data["attacker"] = True
        self.assertTrue(any("additional property" in item for item in finalizer.dataset_errors(data)))

    def test_duplicate_json_keys_rejected(self):
        with tempfile.TemporaryDirectory() as root:
            path = Path(root) / "duplicate.json"
            path.write_text('{"a": 1, "a": 2}', encoding="utf-8")
            with self.assertRaises(finalizer.ContractError):
                finalizer.load_json(path)


if __name__ == "__main__":
    unittest.main()
