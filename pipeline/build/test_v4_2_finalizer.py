#!/usr/bin/env python3

import copy
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest


HERE = Path(__file__).resolve().parent


def load_module(name, filename):
    spec = importlib.util.spec_from_file_location(name, HERE / filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


finalizer = load_module("v4_2_finalizer_tests", "finalize_run_v4_2.py")
scoring_fixture = load_module("v4_2_scoring_fixture_for_finalizer", "test_v4_2_scoring.py")


def assumption(value, low, high, **extra):
    result = {
        "value": value, "range": {"low": low, "high": high}, "method": "ESTIMATE",
        "evidence_state": "ASSUMPTION", "evidence_quality": "NONE", "confidence": "LOW",
        "source_ids": [], "rationale": "Bounded source-free pre-frozen assumption for contract testing.",
        "caveats": ["Not empirical evidence."],
    }
    result.update(extra)
    return result


def bridge():
    return {"population": "Target operators", "geography": "United States", "period": "2025",
            "unit": "fraction", "business_model": "Recurring accountable service"}


def endpoint_support():
    return {"low_source_ids": ["S1"], "base_source_ids": ["S1"], "high_source_ids": ["S1"]}


def proxy_with_validation(validation_source, kind="independent_corroboration"):
    return {
        "value": .5, "range": {"low": .4, "high": .6}, "method": "ESTIMATE",
        "evidence_state": "PROXY", "evidence_quality": "MED", "confidence": "MED",
        "source_ids": ["S1", "S2"], "rationale": "Mapped proxy with separately declared validation.",
        "caveats": [], "bridge": bridge(), "endpoint_support": endpoint_support(),
        "validation_support": {"kind": kind, "source_ids": [validation_source],
            "independence_basis": "validation_source_ids_disjoint_from_primary_support",
            "rationale": "Validation provenance is tested deterministically for source-ID independence."},
    }


def proxy_state(validation_source):
    state = {
        "state_id": "proxy-y5", "state_digest": None,
        "accounting": "HOLD_ENTRY_REFERENCE", "size": "HOLD_ENTRY_REFERENCE",
        "service_mix": "HOLD_ENTRY_REFERENCE", "customer_concentration": "HOLD_ENTRY_REFERENCE",
        "management_depth": "HOLD_ENTRY_REFERENCE", "platform_quality": "HOLD_ENTRY_REFERENCE",
        "entry_equivalence": {"reference": "ENTRY_TARGET_ARCHETYPE",
            "scenario_policy": "ONE_STATE_LOW_BASE_HIGH",
            "transformation_policy": "NO_SPONSOR_TRANSFORMATION"},
        "method": "ESTIMATE", "evidence_state": "PROXY", "evidence_quality": "MED",
        "confidence": "MED", "source_ids": ["S1", "S2"],
        "rationale": "Forward normalized state with explicit endpoint and validation provenance.",
        "caveats": [], "bridge": bridge(), "endpoint_support": endpoint_support(),
        "validation_support": {"kind": "independent_corroboration", "source_ids": [validation_source],
            "independence_basis": "validation_source_ids_disjoint_from_primary_support",
            "rationale": "Validation provenance is separately identified and checked by the finalizer."},
    }
    state["state_digest"] = finalizer.normalized_state_digest(state)
    return state


def capacity_scope():
    return {"reference_buyer": "CREDIBLE_US_LMM_NATIONAL_SOURCING_NO_PRIVILEGED_ACCESS",
            "horizon_years": 5, "geography": "UNITED_STATES",
            "target_archetype": "FROZEN_SELECTED_TARGET_ARCHETYPE",
            "counts_only_completed_and_onboarded_targets": True}


def capacity_horizon():
    return {"start": "ENTRY_DATE", "end": "END_OF_YEAR_5", "years": 5}


def capacity_calculation():
    return {"measure": "MAXIMUM_TARGET_COUNT",
            "completion_requirement": "CLOSED_WITHIN_FIVE_YEARS",
            "onboarding_requirement": "FULLY_ONBOARDED_WITHIN_FIVE_YEARS",
            "aggregation": "NON_DUPLICATIVE_TARGET_COUNT"}


def capacity_fields(capacity_type):
    return {"capacity_type": capacity_type, "capacity_horizon": capacity_horizon(),
            "capacity_calculation": capacity_calculation(), "capacity_scope": capacity_scope()}


def recognized_accounting_basis(presentation="GROSS_OF_ALL"):
    return {"recognition_standard": "ACCRUAL_RECOGNIZED_REVENUE",
            "measurement_period": "TRAILING_TWELVE_MONTHS",
            "pass_through_presentation": presentation}


def anchor_basis(state_digest):
    return {"channel": "ENTRY_EQUIVALENT_COMPARABLE_MULTIPLE_LEVEL",
            "normalized_y5_state_digest": state_digest,
            "state_reference": "ENTRY_TARGET_ARCHETYPE",
            "scenario_policy": "ONE_STATE_LOW_BASE_HIGH"}


def excluded_channel_map():
    return {key: "EXCLUDED" for key in (
        "commercial_retention", "constant_price_survival", "implementation_realization",
        "implementation_investment", "operating_value_viability_h", "controllable_value_added_v",
        "buyability_b", "sponsor_transformation", "sponsor_synergy", "margin_change", "size_change",
        "service_mix_change", "customer_concentration_change", "management_depth_change",
        "platform_quality_change", "accounting_change")}


def fixed_base_assertions():
    return {"index_method": "FIXED_BASE_LASPEYRES_CVA",
            "price_basis": "BASELINE_CVA_PER_UNIT_HELD_CONSTANT",
            "quality_basis": "CONSTANT_QUALITY", "basket_scope": "EXHAUSTIVE_BASELINE_SERVICES_ONLY",
            "operator_control_scope": "PURCHASED_FROM_NAMED_OPERATOR",
            "new_demand_treatment": "EXCLUDED_AND_CAPPED_AT_ONE",
            "pass_through_boundary": "MATCHES_R_CVA_RECONCILIATION"}


def dataset():
    return {
        "dataset_version": "4.2", "snapshot_id": "synthetic-999999-v42", "naics": "999999",
        "title": "Synthetic Services",
        "labor_share": {"value": 0.5, "quality": "HIGH", "basis": "Normalized synthetic share."},
        "n_total": {"value": 1250, "quality": "HIGH", "basis": "Normalized synthetic count."},
        "n_band": {"value": 1000, "quality": "HIGH", "basis": "Normalized target-band count."},
        "role_mix": {"basis": "Dataset descriptor only; never used as the assumption value basis.",
                     "quality": "LOW", "occupations": [
                         {"soc": "11-0001", "title": "Synthetic operators", "employment_share": 0.8,
                          "wage_share": 0.9}]},
        "provenance": {"derivation_version": "synthetic-v42", "source_manifest_sha256": "a" * 64,
                       "vintage": "2026 synthetic"},
    }


def target_archetype():
    return {
        "selected_id": "core", "alternatives": [{
            "id": "core", "name": "Core accountable operator",
            "inclusion_criteria": ["Directly accountable recurring service"],
            "exclusion_criteria": ["Pure product resale"],
            "band_count": {"base": 800, "low": 750, "high": 850}, "source_ids": ["A1"],
            "rationale": "Largest objective target-band population."}],
        "residual": {"name": "Residual", "band_count": {"base": 200, "low": 150, "high": 250},
                     "rationale": "Non-selected remainder."},
        "enumeration_coverage": {"base": 0.8, "low": 0.75, "high": 0.85},
        "sources": [{"id": "A1", "url": "https://example.com/archetype", "title": "Registry",
                     "vintage": "2026"}],
        "selection_basis": "Largest base count with the frozen lexicographic tie-break.",
        "selection_uncertainty": False,
    }


def industry_spec(dataset_sha, methodology_sha):
    questions = ("controllable_value_added", "operational_realization", "commercial_retention",
                 "sale_availability", "buyer_access_win", "valuation_robustness", "operator_survival")
    return {
        "spec_version": "4.2", "naics": "999999", "title": "Synthetic Services",
        "methodology_snapshot": {"path": "V4_2_RUNTIME_METHODOLOGY.md", "sha256": methodology_sha},
        "dataset_snapshot": {"path": "pipeline/datasets/v4_2/999999.json", "sha256": dataset_sha},
        "target_archetype": target_archetype(),
        "value_basis": {
            "mode": "assumption", "scope": "Pre-frozen target-specific cash-cost taxonomy.",
            "controllable_value_added_boundary": "Recognized revenue less documented third-party pass-through.",
            "approved_pass_through_categories": ["materials"],
            "employee_cash_cost_id": "employee_cash", "controllable_contractor_cash_cost_id": "contractor_cash",
            "roles": [
                {"role_id": "OPS", "title": "Operations", "role_cash_cost_weight": 0.7,
                 "method": "ESTIMATE", "evidence_quality": "NONE", "source_ids": [],
                 "rationale": "Pre-frozen source-free bounded taxonomy."},
                {"role_id": "ADMIN", "title": "Administration", "role_cash_cost_weight": 0.3,
                 "method": "ESTIMATE", "evidence_quality": "NONE", "source_ids": [],
                 "rationale": "Pre-frozen source-free bounded taxonomy."}],
            "sources": [], "rationale": "Explicit feasibility assumption, not a dataset proxy.",
            "caveats": ["Forces evidence readiness UNPROVEN."]},
        "source_hints": [{"area": "synthetic", "source": "Registry", "why": "Future validation",
                          "uncertain_exists": True}],
        "research_questions": {key: ["What defensible bounded primitive can be established?"] for key in questions},
        "special_notes": ["Do not promote the assumption basis with sources."],
    }


def packet():
    text = "Synthetic narrative that is deliberately long enough for the closed v4.2 packet contract and deterministic memo rendering."
    r = [(.2, .1, .3), (.4, .2, .5), (.6, .4, .7), (.75, .55, .85), (.85, .65, .95)]
    state = {
        "state_id": "normalized-y5", "state_digest": None,
        "accounting": "HOLD_ENTRY_REFERENCE", "size": "HOLD_ENTRY_REFERENCE",
        "service_mix": "HOLD_ENTRY_REFERENCE", "customer_concentration": "HOLD_ENTRY_REFERENCE",
        "management_depth": "HOLD_ENTRY_REFERENCE", "platform_quality": "HOLD_ENTRY_REFERENCE",
        "entry_equivalence": {"reference": "ENTRY_TARGET_ARCHETYPE",
            "scenario_policy": "ONE_STATE_LOW_BASE_HIGH",
            "transformation_policy": "NO_SPONSOR_TRANSFORMATION"},
        "method": "ESTIMATE", "evidence_state": "ASSUMPTION", "evidence_quality": "NONE",
        "confidence": "LOW", "source_ids": [], "rationale": text, "caveats": ["Assumption."]}
    state["state_digest"] = finalizer.normalized_state_digest(state)
    return {
        "naics": "999999", "title": "Synthetic Services",
        "sources": [{"id": "S1", "url": "https://example.com/research", "title": "Unused future source",
                     "access_date": "2026-07-21", "what_it_supports": "No assumption-basis claim."}],
        "narrative": {key: text for key in ("executive_view", "revenue_and_pass_through", "technical_value",
                      "implementation", "commercial_capture", "buyability", "entry_and_exit",
                      "operator_survival", "risks_and_uncertainty")},
        "scenario_narratives": {key: text for key in ("low", "base", "high")},
        "inputs": {
            "recognized_revenue": assumption(100.0, 90.0, 110.0,
                accounting_basis=recognized_accounting_basis(),
                pass_through_reconciliation={"revenue_basis": "GROSS_OF_ALL",
                    "included_cost_ids": ["materials_cash"], "already_netted_cost_ids": [],
                    "evidence": {"method": "OBSERVED", "evidence_state": "DIRECT",
                        "evidence_quality": "MED", "source_ids": ["S1"],
                        "rationale": "Source directly documents that recognized revenue is gross of materials.",
                        "caveats": []}}),
            "third_party_pass_through": [{"category": "materials", "cost_id": "materials_cash",
                "accounting_basis": "Accrual third-party materials passed through without operator value add.",
                "amount": assumption(20.0, 15.0, 25.0)}],
            "employee_cash_cost": {"cost_id": "employee_cash", "accounting_basis": "Cash wages and benefits.",
                                   "amount": assumption(30.0, 25.0, 35.0)},
            "controllable_contractor_cash_cost": {"cost_id": "contractor_cash",
                "accounting_basis": "Cash contractor spend controlled by the operator.",
                "amount": assumption(10.0, 5.0, 15.0)},
            "target_role_judgments": {"roles": [
                {"role_id": "OPS", "removable_fraction": assumption(.5, .3, .7)},
                {"role_id": "ADMIN", "removable_fraction": assumption(.4, .2, .6)}]},
            "implementation_realization": {"r%d" % i: assumption(*values) for i, values in enumerate(r, 1)},
            "implementation_investment": {"k%d" % i: assumption(.05 if i else .2,
                .02 if i else .1, .08 if i else .3) for i in range(6)},
            "commercial_retention": {"c%d" % i: assumption(.65, .45, .8) for i in range(1, 6)},
            "target_archetype_coverage": assumption(.8, .75, .85),
            "five_year_sale_availability": assumption(.25, .15, .35),
            "buyer_access_win_share": assumption(.5, .3, .7),
            "deal_execution_capacity_5y": assumption(100.0, 50.0, 150.0,
                **capacity_fields("DEAL_EXECUTION")),
            "integration_onboarding_capacity_5y": assumption(80.0, 40.0, 120.0,
                **capacity_fields("INTEGRATION_ONBOARDING")),
            "buy_multiple": assumption(6.0, 5.0, 7.0),
            "normalized_y5_operating_state": state,
            "downside_exit_multiple": {"normalized_y5_state_digest": state["state_digest"],
                "anchor": assumption(5.0, 4.0, 6.0, anchor_basis=anchor_basis(state["state_digest"])),
                "adjustments": [],
                "excluded_channel_map": excluded_channel_map()},
            "operator_controlled_value_added_demand_share_y5": {
                "status": "SUPPORTED", "basket_id": "synthetic-fixed-base-basket",
                "fixed_base_assertions": fixed_base_assertions(),
                "services": [{"service_id": "core_service", "unit": "completed service unit",
                    "constant_quality_spec": "Frozen entry-quality accountable service unit.",
                    "baseline_quantity": assumption(100.0, 100.0, 100.0),
                    "baseline_revenue": assumption(100.0, 100.0, 100.0),
                    "baseline_pass_through": assumption(20.0, 20.0, 20.0),
                    "baseline_cva": 80.0, "baseline_cva_unit_price": .8, "base_weight": 1.0,
                    "y5_operator_controlled_quantity": assumption(70.0, 50.0, 85.0)}],
                "rationale": "One-service exhaustive fixed-base basket for deterministic contract testing."},
        },
        "cross_checks": {key: text for key in ("target_identity_preserved", "pass_through_removed_once",
            "removability_only_in_v", "investment_only_in_i", "commercial_only_in_c",
            "buyer_access_separate_from_price", "p_uses_frozen_y5_state", "p_excludes_c_and_survival",
            "survival_is_constant_price_value_added")},
        "confidence_overall": "LOW",
        "top_uncertain_inputs": [{"input": "assumption basis", "range": "bounded synthetic support",
                                  "score_impact": "Forces evidence-first action regardless of economics."}],
        "reviewer_note": "Synthetic contract fixture only.",
    }


def write_json(path, value):
    path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")


class Fixture:
    def __init__(self, root):
        root = Path(root)
        self.dataset_path, self.spec_path = root / "dataset.json", root / "spec.json"
        self.packet_path, self.envelope_path = root / "packet.json", root / "envelope.json"
        self.prompt_path = root / "prompt.md"
        self.methodology_path = HERE.parent.parent / "V4_2_RUNTIME_METHODOLOGY.md"
        self.prompt_path.write_text("# Frozen synthetic prompt\n", encoding="utf-8")
        write_json(self.dataset_path, dataset())
        write_json(self.spec_path, industry_spec(finalizer.sha256_file(self.dataset_path),
                                                  finalizer.sha256_file(self.methodology_path)))
        write_json(self.packet_path, packet())
        hashes = {
            "prompt_sha256": finalizer.sha256_file(self.prompt_path),
            "dataset_sha256": finalizer.sha256_file(self.dataset_path),
            "spec_sha256": finalizer.sha256_file(self.spec_path),
            "methodology_sha256": finalizer.sha256_file(self.methodology_path),
            "thresholds_sha256": finalizer.sha256_file(HERE / "thresholds_v4_2.json"),
            "research_packet_schema_sha256": finalizer.sha256_file(HERE / "schemas/research_packet_v4_2.schema.json"),
            "dataset_schema_sha256": finalizer.sha256_file(HERE / "schemas/dataset_v4_2.schema.json"),
            "industry_spec_schema_sha256": finalizer.sha256_file(HERE / "schemas/industry_spec_v4_2.schema.json"),
            "run_record_schema_sha256": finalizer.sha256_file(HERE / "schemas/run_record_v4_2.schema.json"),
            "scoring_sha256": finalizer.sha256_file(HERE / "v4_2_scoring.py"),
            "finalizer_sha256": finalizer.sha256_file(HERE / "finalize_run_v4_2.py"),
        }
        write_json(self.envelope_path, {"envelope_version": "4.2", "kind": "target", "naics": "999999",
            "title": "Synthetic Services", "run_id": "synthetic-v42", "run_date": "2026-07-21",
            "attempt": 1, "remediates_run_id": None, "issued_by_task_path": "/root",
            "codex_task_path": "/root/research_999999", "fork_policy": "none", "role": "research",
            "model_id": "gpt-5.6-terra", **hashes})
        self.reload()

    def reload(self):
        self.data = finalizer.load_json(self.dataset_path); self.spec = finalizer.load_json(self.spec_path)
        self.packet = finalizer.load_json(self.packet_path); self.envelope = finalizer.load_json(self.envelope_path)
        self.paths = {"dataset": str(self.dataset_path), "spec": str(self.spec_path),
                      "packet": str(self.packet_path), "envelope": str(self.envelope_path),
                      "prompt": str(self.prompt_path), "methodology": str(self.methodology_path)}


class FinalizerV42Tests(unittest.TestCase):
    def test_assumption_basis_scores_but_forces_unproven(self):
        with tempfile.TemporaryDirectory() as root:
            fixture = Fixture(root)
            record, errors = finalizer.finalize(fixture.packet, fixture.data, fixture.spec,
                                                fixture.envelope, fixture.paths)
            self.assertEqual(errors, [])
            self.assertIsNotNone(record["scenarios"]["base"]["scores"]["V"])
            self.assertEqual(record["inputs"]["target_role_mix"]["spec_mode"], "assumption")
            self.assertEqual(record["decision"]["evidence_readiness"]["status"], "UNPROVEN")
            self.assertEqual(record["decision"]["action"], "EVIDENCE_FIRST")
            self.assertEqual(record["dataset_inputs"]["n_band"]["source_ids"], ["DATASET"])

    def test_finalizer_preserves_zero_g_annihilator_with_missing_revenue(self):
        with tempfile.TemporaryDirectory() as root:
            fixture = Fixture(root)
            revenue = fixture.packet["inputs"]["recognized_revenue"]
            revenue.update(value=None, range={"low": None, "high": None},
                           method="ESTIMATE", evidence_state="MISSING",
                           evidence_quality="NONE", confidence="LOW", source_ids=[])
            fixture.packet["inputs"]["employee_cash_cost"]["amount"] = assumption(0, 0, 0)
            fixture.packet["inputs"]["controllable_contractor_cash_cost"]["amount"] = assumption(0, 0, 0)
            write_json(fixture.packet_path, fixture.packet)
            record, errors = finalizer.finalize(fixture.packet, fixture.data, fixture.spec,
                                                fixture.envelope, fixture.paths)
            self.assertEqual(errors, [])
            self.assertEqual([record["scenarios"][bound]["scores"]["V"]
                              for bound in scoring_fixture.scoring.BOUNDS], [0, 0, 0])
            self.assertEqual([record["scenarios"][bound]["scores"]["I"]
                              for bound in scoring_fixture.scoring.BOUNDS], [0, 0, 0])
            self.assertEqual(record["decision"]["economic_verdict"], "kill")
            self.assertEqual(record["decision"]["action"], "AVOID")

    def test_assumption_basis_cannot_be_promoted_by_packet_sources(self):
        with tempfile.TemporaryDirectory() as root:
            fixture = Fixture(root)
            promoted = copy.deepcopy(fixture.packet)
            promoted["inputs"]["employee_cash_cost"]["amount"].update(
                method="OBSERVED", evidence_state="DIRECT", evidence_quality="HIGH", source_ids=["S1"],
                endpoint_support=endpoint_support())
            errors = finalizer.packet_errors(promoted, fixture.data, fixture.spec)
            self.assertTrue(any("remain ASSUMPTION" in error for error in errors), errors)

    def test_finalizer_accepts_operational_ramp_then_decay(self):
        with tempfile.TemporaryDirectory() as root:
            fixture = Fixture(root)
            path = [.2, .8, .9, .4, .1]
            for year, value in enumerate(path, 1):
                fixture.packet["inputs"]["implementation_realization"]["r%d" % year] = assumption(
                    value, value, value)
            write_json(fixture.packet_path, fixture.packet)
            record, errors = finalizer.finalize(fixture.packet, fixture.data, fixture.spec,
                                                fixture.envelope, fixture.paths)
            self.assertEqual(errors, [])
            self.assertEqual(record["scenarios"]["base"]["subfactors"]["implementation_realization"],
                             path)

    def test_assumption_spec_rejects_sources_and_non_estimate_roles(self):
        with tempfile.TemporaryDirectory() as root:
            fixture = Fixture(root)
            bad = copy.deepcopy(fixture.spec)
            bad["value_basis"]["sources"] = [{"id": "B1", "url": "https://example.com/basis",
                                                   "title": "Basis", "vintage": "2026"}]
            bad["value_basis"]["roles"][0].update(method="OBSERVED", evidence_quality="HIGH",
                                                    source_ids=["B1"])
            errors = finalizer.spec_errors(bad, fixture.data,
                                            finalizer.sha256_file(fixture.methodology_path))
            self.assertTrue(any("maxItems 0" in error or "const 'ESTIMATE'" in error for error in errors), errors)

    def test_proxy_may_use_observed_method_when_bridge_and_endpoints_exist(self):
        item = {"value": .5, "range": {"low": .4, "high": .6}, "method": "OBSERVED",
                "evidence_state": "PROXY", "evidence_quality": "MED", "confidence": "MED",
                "source_ids": ["S1"], "rationale": "Mapped observation.", "caveats": [],
                "bridge": bridge(), "endpoint_support": endpoint_support()}
        self.assertEqual(finalizer._numeric_errors("proxy", item, {"S1"}, 0, 1), [])

    def test_reused_endpoint_source_does_not_qualify_as_independent_validation(self):
        item = proxy_with_validation("S1")
        self.assertEqual(finalizer._numeric_errors("proxy", item, {"S1", "S2"}, 0, 1), [])
        resolved = finalizer._finalize_selection(item, {"S1", "S2"})
        self.assertFalse(resolved["independent_validation"])
        self.assertFalse(resolved["longitudinal_validation"])

    def test_distinct_validation_source_qualifies(self):
        item = proxy_with_validation("S2")
        self.assertEqual(finalizer._numeric_errors("proxy", item, {"S1", "S2"}, 0, 1), [])
        resolved = finalizer._finalize_selection(item, {"S1", "S2"})
        self.assertTrue(resolved["independent_validation"])
        self.assertFalse(resolved["longitudinal_validation"])

    def test_derived_independence_controls_scorer_readiness(self):
        reused_item = proxy_with_validation("S1")
        distinct_item = proxy_with_validation("S2")
        for item in (reused_item, distinct_item):
            item["range"] = {"low": .5, "high": .5}
        reused = scoring_fixture.record()
        reused["inputs"]["buyer_access_win_share"] = finalizer._finalize_selection(
            reused_item, {"S1", "S2"})
        distinct = scoring_fixture.record()
        distinct["inputs"]["buyer_access_win_share"] = finalizer._finalize_selection(
            distinct_item, {"S1", "S2"})
        self.assertEqual(finalizer.scoring.calculate(reused)["decision"]["evidence_readiness"]["status"],
                         "PROVISIONAL")
        self.assertEqual(finalizer.scoring.calculate(distinct)["decision"]["evidence_readiness"]["status"],
                         "SUBSTANTIATED")

    def test_longitudinal_validation_also_requires_distinct_provenance(self):
        reused = finalizer._finalize_selection(
            proxy_with_validation("S1", "longitudinal_validation"), {"S1", "S2"})
        distinct = finalizer._finalize_selection(
            proxy_with_validation("S2", "longitudinal_validation"), {"S1", "S2"})
        self.assertFalse(reused["longitudinal_validation"])
        self.assertTrue(distinct["longitudinal_validation"])

    def test_composite_accepts_mixed_complete_validation_kinds(self):
        independent = proxy_with_validation("S2", "independent_corroboration")
        longitudinal = proxy_with_validation("S2", "longitudinal_validation")
        resolved = finalizer._composite_selection(
            .8, .8, .8, [independent, longitudinal], {"S1", "S2"},
            "Mixed component validation kinds are each complete.")
        self.assertTrue(resolved["independent_validation"])
        self.assertTrue(resolved["endpoints_supported"])
        item = scoring_fixture.record()
        item["inputs"]["operator_controlled_value_added_demand_share_y5"] = resolved
        self.assertEqual(finalizer.scoring.calculate(item)["decision"]["evidence_readiness"]["status"],
                         "SUBSTANTIATED")

    def test_validation_schema_requires_closed_independence_basis(self):
        with tempfile.TemporaryDirectory() as root:
            fixture = Fixture(root)
            item = proxy_with_validation("S1")
            item["source_ids"] = ["S1"]
            item["validation_support"].pop("independence_basis")
            fixture.packet["inputs"]["implementation_realization"]["r1"] = item
            errors = finalizer.packet_errors(fixture.packet, fixture.data, fixture.spec)
            self.assertTrue(any("independence_basis" in error and "required" in error for error in errors), errors)

    def test_downside_excluded_channels_require_exact_semantic_set(self):
        with tempfile.TemporaryDirectory() as root:
            fixture = Fixture(root)
            fixture.packet["inputs"]["downside_exit_multiple"]["excluded_channel_map"].pop(
                "constant_price_survival")
            errors = finalizer.packet_errors(fixture.packet, fixture.data, fixture.spec)
            self.assertTrue(any("constant_price_survival" in error and "required" in error
                                for error in errors), errors)

    def test_proxy_normalized_state_requires_endpoint_and_validation_objects(self):
        with tempfile.TemporaryDirectory() as root:
            fixture = Fixture(root)
            state = proxy_state("S2")
            state.pop("endpoint_support")
            state.pop("validation_support")
            fixture.packet["inputs"]["normalized_y5_operating_state"] = state
            errors = finalizer.packet_errors(fixture.packet, fixture.data, fixture.spec)
            self.assertTrue(any("endpoint_support" in error and "required" in error for error in errors), errors)
            self.assertTrue(any("validation_support" in error and "required" in error for error in errors), errors)

    def test_normalized_state_support_flags_are_derived_not_hardcoded(self):
        reused = finalizer._finalize_state(proxy_state("S1"), {"S1", "S2"})
        distinct = finalizer._finalize_state(proxy_state("S2"), {"S1", "S2"})
        no_endpoints = proxy_state("S2")
        no_endpoints.pop("endpoint_support")
        unsupported = finalizer._finalize_state(no_endpoints, {"S1", "S2"})
        self.assertTrue(reused["endpoints_supported"])
        self.assertFalse(reused["independent_validation"])
        self.assertTrue(distinct["endpoints_supported"])
        self.assertTrue(distinct["independent_validation"])
        self.assertFalse(unsupported["endpoints_supported"])

    def test_low_quality_dataset_count_is_not_promoted_to_direct(self):
        resolved = finalizer._dataset_selection(
            {"value": 12, "quality": "LOW", "basis": "Weak normalized estimate."}, "target-band count")
        self.assertEqual(resolved["evidence_state"], "ASSUMPTION")
        self.assertEqual(resolved["source_ids"], [])
        self.assertFalse(resolved["endpoints_supported"])

    def test_construct_provenance_preserves_attribution_and_h_basis(self):
        with tempfile.TemporaryDirectory() as root:
            fixture = Fixture(root)
            record, errors = finalizer.finalize(fixture.packet, fixture.data, fixture.spec,
                                                fixture.envelope, fixture.paths)
            self.assertEqual(errors, [])
            provenance = record["construct_provenance"]
            self.assertEqual(provenance["cva_reconciliation"]["pass_through"][0]["cost_id"], "materials_cash")
            self.assertEqual(provenance["p_attribution"]["normalized_y5_state_digest"],
                             record["inputs"]["normalized_y5_operating_state"]["state_digest"])
            self.assertEqual(provenance["p_attribution"]["excluded_channel_map"]["commercial_retention"],
                             "EXCLUDED")
            self.assertEqual(provenance["constant_price_survival"]["fixed_base_assertions"]["index_method"],
                             "FIXED_BASE_LASPEYRES_CVA")
            self.assertEqual(provenance["h"]["discount_rate"], .10)

    def test_reconciliation_basis_controls_single_pass_through_subtraction(self):
        with tempfile.TemporaryDirectory() as root:
            fixture = Fixture(root)
            gross, errors = finalizer.finalize(fixture.packet, fixture.data, fixture.spec,
                                               fixture.envelope, fixture.paths)
            self.assertEqual(errors, [])
            self.assertEqual(gross["scenarios"]["base"]["subfactors"]["V"]["R_cva"], 80.0)

            fixture.packet["inputs"]["recognized_revenue"]["pass_through_reconciliation"].update(
                revenue_basis="NET_OF_ALL", included_cost_ids=[],
                already_netted_cost_ids=["materials_cash"])
            fixture.packet["inputs"]["recognized_revenue"]["accounting_basis"][
                "pass_through_presentation"] = "NET_OF_ALL"
            write_json(fixture.packet_path, fixture.packet)
            net, errors = finalizer.finalize(fixture.packet, fixture.data, fixture.spec,
                                             fixture.envelope, fixture.paths)
            self.assertEqual(errors, [])
            self.assertEqual(net["scenarios"]["base"]["subfactors"]["V"]["R_cva"], 100.0)
            self.assertEqual(net["scenarios"]["base"]["subfactors"]["V"]["included_pass_through"], 0.0)
            self.assertEqual(net["scenarios"]["base"]["subfactors"]["V"]["already_netted_pass_through"], 20.0)

    def test_mixed_reconciliation_requires_exact_disjoint_partition(self):
        with tempfile.TemporaryDirectory() as root:
            fixture = Fixture(root)
            fixture.spec["value_basis"]["approved_pass_through_categories"].append("fees")
            fixture.packet["inputs"]["third_party_pass_through"].append({
                "category": "fees", "cost_id": "fees_cash", "accounting_basis": "Netted third-party fee.",
                "amount": assumption(10.0, 8.0, 12.0)})
            reconciliation = fixture.packet["inputs"]["recognized_revenue"]["pass_through_reconciliation"]
            reconciliation.update(revenue_basis="MIXED", included_cost_ids=["materials_cash"],
                                  already_netted_cost_ids=["fees_cash"])
            fixture.packet["inputs"]["recognized_revenue"]["accounting_basis"][
                "pass_through_presentation"] = "MIXED"
            self.assertEqual(finalizer.packet_errors(fixture.packet, fixture.data, fixture.spec), [])
            reconciliation["already_netted_cost_ids"] = ["materials_cash"]
            errors = finalizer.packet_errors(fixture.packet, fixture.data, fixture.spec)
            self.assertTrue(any("partitions must be disjoint" in error for error in errors), errors)
            self.assertTrue(any("exactly partition" in error for error in errors), errors)

    def test_structured_accounting_capacity_and_anchor_semantics_are_closed(self):
        with tempfile.TemporaryDirectory() as root:
            fixture = Fixture(root)
            bad = copy.deepcopy(fixture.packet)
            bad["inputs"]["recognized_revenue"]["accounting_basis"][
                "pass_through_presentation"] = "NET_OF_ALL"
            errors = finalizer.packet_errors(bad, fixture.data, fixture.spec)
            self.assertIn("recognized_revenue accounting basis must equal the pass-through revenue basis",
                          errors)

            bad = copy.deepcopy(fixture.packet)
            bad["inputs"]["deal_execution_capacity_5y"]["capacity_type"] = "INTEGRATION_ONBOARDING"
            errors = finalizer.packet_errors(bad, fixture.data, fixture.spec)
            self.assertTrue(any("DEAL_EXECUTION" in error for error in errors), errors)

            bad = copy.deepcopy(fixture.packet)
            bad["inputs"]["downside_exit_multiple"]["anchor"]["anchor_basis"]["channel"] = (
                "PRIVATE_TRANSACTION_LIQUIDITY")
            errors = finalizer.packet_errors(bad, fixture.data, fixture.spec)
            self.assertTrue(any("ENTRY_EQUIVALENT_COMPARABLE_MULTIPLE_LEVEL" in error
                                for error in errors), errors)

            bad = copy.deepcopy(fixture.packet)
            bad["inputs"]["downside_exit_multiple"]["anchor"]["anchor_basis"][
                "normalized_y5_state_digest"] = "0" * 64
            errors = finalizer.packet_errors(bad, fixture.data, fixture.spec)
            self.assertIn("downside anchor must bind the exact normalized y5 state digest", errors)

    def test_capacity_capping_and_fixed_base_survival_are_recomputed(self):
        with tempfile.TemporaryDirectory() as root:
            fixture = Fixture(root)
            record, errors = finalizer.finalize(fixture.packet, fixture.data, fixture.spec,
                                                fixture.envelope, fixture.paths)
            self.assertEqual(errors, [])
            buyability = record["scenarios"]["base"]["subfactors"]["B"]
            self.assertEqual((buyability["O5"], buyability["K5"], buyability["N5"]),
                             (100.0, 80.0, 80.0))
            self.assertEqual(record["inputs"]["operator_controlled_value_added_demand_share_y5"]["value"], .7)
            survival = record["construct_provenance"]["constant_price_survival"]
            self.assertEqual(survival["calculation_status"], "RECOMPUTED")
            self.assertEqual(survival["R_cva_base"], 80.0)

    def test_survival_rejects_ranged_fixed_baseline_instead_of_discarding_it(self):
        with tempfile.TemporaryDirectory() as root:
            fixture = Fixture(root)
            service = fixture.packet["inputs"]["operator_controlled_value_added_demand_share_y5"]["services"][0]
            service["baseline_quantity"] = assumption(100.0, 50.0, 400.0)
            service["y5_operator_controlled_quantity"] = assumption(80.0, 80.0, 80.0)
            errors = finalizer.packet_errors(fixture.packet, fixture.data, fixture.spec)
            self.assertTrue(any("baseline_quantity must be point-identified" in error
                                for error in errors), errors)
            reconciliation = finalizer._finalize_reconciliation(
                fixture.packet["inputs"]["recognized_revenue"]["pass_through_reconciliation"],
                fixture.packet["inputs"]["third_party_pass_through"], {"S1"})
            resolved, provenance = finalizer._finalize_survival(
                fixture.packet["inputs"]["operator_controlled_value_added_demand_share_y5"],
                fixture.packet["inputs"]["recognized_revenue"],
                fixture.packet["inputs"]["third_party_pass_through"], reconciliation, {"S1"})
            self.assertEqual(resolved["evidence_state"], "MISSING")
            self.assertTrue(any(reason.startswith("baseline_not_point_identified")
                                for reason in provenance["failure_reasons"]))

    def test_downside_digest_and_closed_adjustments_control_p(self):
        with tempfile.TemporaryDirectory() as root:
            fixture = Fixture(root)
            downside = fixture.packet["inputs"]["downside_exit_multiple"]
            downside["adjustments"] = [{"channel": "PRIVATE_TRANSACTION_LIQUIDITY",
                                        "amount": assumption(-1.0, -1.5, -.5)}]
            write_json(fixture.packet_path, fixture.packet)
            record, errors = finalizer.finalize(fixture.packet, fixture.data, fixture.spec,
                                                fixture.envelope, fixture.paths)
            self.assertEqual(errors, [])
            self.assertEqual(record["inputs"]["downside_exit_mult"]["value"], 4.0)
            self.assertEqual(record["construct_provenance"]["p_attribution"]["calculation_status"],
                             "RECOMPUTED")

            bad = copy.deepcopy(fixture.packet)
            bad["inputs"]["downside_exit_multiple"]["normalized_y5_state_digest"] = "0" * 64
            errors = finalizer.packet_errors(bad, fixture.data, fixture.spec)
            self.assertIn("downside multiple must bind the exact normalized y5 state digest", errors)
            bad = copy.deepcopy(fixture.packet)
            bad["inputs"]["downside_exit_multiple"]["adjustments"][0]["amount"] = assumption(.1, 0, .2)
            errors = finalizer.packet_errors(bad, fixture.data, fixture.spec)
            self.assertTrue(any("range.high violates its domain" in error or
                                "may not encode favorable" in error for error in errors), errors)

    def test_envelope_is_closed(self):
        with tempfile.TemporaryDirectory() as root:
            fixture = Fixture(root)
            fixture.envelope["unauthorized"] = True
            errors = finalizer.envelope_errors(fixture.envelope, fixture.packet, fixture.data,
                                                fixture.spec, fixture.paths)
            self.assertTrue(any("unknown keys" in error for error in errors), errors)


if __name__ == "__main__":
    unittest.main()
