#!/usr/bin/env python3

import copy
import importlib.util
import math
import os
import random
import unittest


HERE = os.path.dirname(os.path.abspath(__file__))
SPEC = importlib.util.spec_from_file_location("v4_1_scoring_tests", os.path.join(HERE, "v4_1_scoring.py"))
scoring = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(scoring)


def selection(value, low=None, high=None, state="DIRECT", quality="MED", method="OBSERVED"):
    return {
        "value": value,
        "range": {"low": value if low is None else low, "high": value if high is None else high},
        "evidence_state": state,
        "evidence_quality": quality,
        "method": method,
    }


def missing():
    return selection(None, None, None, state="MISSING", quality="NONE")


def record():
    return {
        "dataset_inputs": {"n_band": selection(500, 400, 600)},
        "inputs": {
            "target_archetype": {"selection_uncertainty": False},
            "target_labor_cost_share": selection(0.5, 0.4, 0.6),
            "target_role_mix": {
                "spec_mode": "frozen",
                "roles": [
                    {"role": "delivery", "cost_weight": 0.6,
                     "removable_fraction": selection(0.7, 0.6, 0.8)},
                    {"role": "operations", "cost_weight": 0.4,
                     "removable_fraction": selection(0.5, 0.4, 0.6)},
                ],
            },
            "implementation_ramp": {
                "r1": selection(0.6, 0.5, 0.7),
                "r2": selection(0.7, 0.6, 0.8),
                "r3": selection(0.8, 0.7, 0.9),
                "r4": selection(0.9, 0.8, 1.0),
                "r5": selection(1.0, 0.9, 1.0),
            },
            "commercial_retention": selection(0.8, 0.7, 0.9),
            "target_archetype_coverage": selection(1.0, 0.8, 1.0),
            "five_year_sale_availability": selection(1.0, 0.8, 1.0),
            "buy_mult": selection(5.0, 4.0, 6.0),
            "downside_exit_mult": selection(5.0, 4.0, 6.0),
            "y5_survival": selection(0.9, 0.8, 1.0),
        },
    }


def support_forward_inputs(item):
    for name in ("commercial_retention", "five_year_sale_availability", "downside_exit_mult", "y5_survival"):
        item["inputs"][name].update(evidence_state="PROXY", bridge_supported=True)
    for ramp in item["inputs"]["implementation_ramp"].values():
        ramp.update(evidence_state="PROXY", bridge_supported=True)
    return item


class V41ScoringTests(unittest.TestCase):
    def setUp(self):
        self.thresholds = scoring.load_thresholds()

    def calculate(self, item=None):
        return scoring.calculate(item or record(), self.thresholds)

    def test_thresholds_validate_and_are_exact(self):
        thresholds = self.thresholds
        self.assertEqual(thresholds["verdict_cuts"], {
            "hell_yes": 7.5, "strong": 6.0, "conditional": 4.5, "pass": 3.0})
        self.assertEqual(thresholds["verdict_min_each_factor"], {
            "hell_yes": 6.0, "strong": 4.0, "conditional": 2.0, "pass": 1.0})
        self.assertIs(scoring.validate_thresholds(thresholds), thresholds)

    def test_threshold_validation_rejects_each_structural_family(self):
        mutations = []
        item = copy.deepcopy(self.thresholds); item["score"]["factors"] = ["V"]; mutations.append(item)
        item = copy.deepcopy(self.thresholds); item["implementation"]["years"] = 4; mutations.append(item)
        item = copy.deepcopy(self.thresholds); item["implementation"]["discount_rate"] = -0.1; mutations.append(item)
        item = copy.deepcopy(self.thresholds); item["verdict_cuts"]["strong"] = 8; mutations.append(item)
        item = copy.deepcopy(self.thresholds); item["verdict_min_each_factor"]["pass"] = 3; mutations.append(item)
        item = copy.deepcopy(self.thresholds); item["survival_gate"]["pass_cap_at_or_above"] = 0.6; mutations.append(item)
        item = copy.deepcopy(self.thresholds); item["buyability"]["n5_full_score"] = 0; mutations.append(item)
        item = copy.deepcopy(self.thresholds); item["unexpected"] = True; mutations.append(item)
        item = copy.deepcopy(self.thresholds); item["freeze_date"] = "2026-07-22"; mutations.append(item)
        item = copy.deepcopy(self.thresholds); item["archetype_selection"]["near_tie_fraction"] = 0.11; mutations.append(item)
        item = copy.deepcopy(self.thresholds); item["domains"]["commercial_retention"] = [0, 2]; mutations.append(item)
        item = copy.deepcopy(self.thresholds); item["partial_identification"]["unbounded_token"] = "INF"; mutations.append(item)
        item = copy.deepcopy(self.thresholds); item["evidence_contract"]["qualities"] = ["HIGH"]; mutations.append(item)
        item = copy.deepcopy(self.thresholds); item["readiness"]["cross_tier_status"] = "SUBSTANTIATED"; mutations.append(item)
        item = copy.deepcopy(self.thresholds); item["sentinels"]["numeric_tolerance"] = 1e-8; mutations.append(item)
        item = copy.deepcopy(self.thresholds); item["sentinels"]["implementation_schedules"][1]["expected"] += 2e-9; mutations.append(item)
        item = copy.deepcopy(self.thresholds); item["display"]["decimal_places"] = 3; mutations.append(item)
        for family in ("archetype_selection", "domains", "partial_identification", "evidence_contract",
                       "readiness", "sentinels", "display"):
            item = copy.deepcopy(self.thresholds); item[family]["unused"] = True; mutations.append(item)
        for malformed in mutations:
            with self.assertRaises(ValueError):
                scoring.validate_thresholds(malformed)
        with self.assertRaises(ValueError):
            scoring.calculate(record(), {})

    def test_v_formula_and_role_weights(self):
        item = record()
        item["inputs"]["target_labor_cost_share"] = selection(0.25)
        for role in item["inputs"]["target_role_mix"]["roles"]:
            role["removable_fraction"] = selection(0.5)
        result = self.calculate(item)
        self.assertAlmostEqual(result["base"]["scores"]["V"], 5.0)
        item["inputs"]["target_role_mix"]["roles"][0]["cost_weight"] = 0.7
        with self.assertRaisesRegex(ValueError, "sum to 1"):
            self.calculate(item)

    def test_missing_role_spec_has_full_v_support(self):
        item = record()
        item["inputs"]["target_role_mix"] = {"spec_mode": "missing", "roles": []}
        result = self.calculate(item)
        self.assertEqual([result[b]["scores"]["V"] for b in scoring.BOUNDS], [0.0, None, 10.0])
        self.assertEqual(result["decision"]["evidence_readiness"]["status"], "UNPROVEN")

    def test_missing_v_primitive_preserves_known_support(self):
        item = record()
        item["inputs"]["target_role_mix"]["roles"][0]["removable_fraction"] = missing()
        result = self.calculate(item)
        self.assertIsNone(result["base"]["scores"]["V"])
        # Known operations role gives a positive lower bound; known labor high tightens upper support.
        self.assertGreater(result["low"]["scores"]["V"], 0)
        self.assertLessEqual(result["high"]["scores"]["V"], 10)

    def test_i_is_discounted_five_year_realization(self):
        item = record()
        values = [0.1, 0.2, 0.3, 0.4, 0.5]
        for year, value in enumerate(values, 1):
            item["inputs"]["implementation_ramp"]["r%d" % year] = selection(value)
        expected = 10 * sum(value / (1.1 ** year) for year, value in enumerate(values, 1)) / sum(
            1 / (1.1 ** year) for year in range(1, 6))
        self.assertAlmostEqual(self.calculate(item)["base"]["scores"]["I"], expected)

    def test_i_reproduces_every_frozen_schedule_anchor(self):
        tolerance = self.thresholds["sentinels"]["numeric_tolerance"]
        for sentinel in self.thresholds["sentinels"]["implementation_schedules"]:
            actual = scoring._implementation_score(sentinel["ramp"], self.thresholds)
            self.assertLessEqual(abs(actual - sentinel["expected"]), tolerance)

    def test_archetype_enumeration_minimum_is_machine_enforced(self):
        item = record()
        item["inputs"]["target_archetype"]["enumeration_coverage"] = {
            "base": 0.80, "low": 0.70, "high": 0.90}
        self.calculate(item)
        item["inputs"]["target_archetype"]["enumeration_coverage"]["base"] = 0.799999
        with self.assertRaisesRegex(ValueError, "frozen minimum coverage"):
            self.calculate(item)

    def test_missing_ramp_uses_tightest_coherent_monotone_support(self):
        item = record()
        item["inputs"]["implementation_ramp"] = {
            "r1": selection(0.4), "r2": missing(), "r3": missing(),
            "r4": selection(0.7), "r5": selection(0.9),
        }
        result = self.calculate(item)
        self.assertEqual(result["low"]["subfactors"]["implementation_ramp"], [0.4, 0.4, 0.4, 0.7, 0.9])
        self.assertEqual(result["high"]["subfactors"]["implementation_ramp"], [0.4, 0.7, 0.7, 0.7, 0.9])
        self.assertIsNone(result["base"]["scores"]["I"])

    def test_incoherent_ramp_is_rejected(self):
        item = record()
        item["inputs"]["implementation_ramp"]["r2"] = selection(0.8, 0.8, 0.9)
        item["inputs"]["implementation_ramp"]["r3"] = selection(0.6, 0.5, 0.7)
        with self.assertRaisesRegex(ValueError, "nondecreasing"):
            self.calculate(item)

    def test_missing_year_cannot_hide_incoherent_known_ramp_endpoints(self):
        item = record()
        item["inputs"]["implementation_ramp"] = {
            "r1": selection(0.8, 0.8, 0.9), "r2": missing(),
            "r3": selection(0.5, 0.5, 0.6), "r4": selection(0.7), "r5": selection(0.9),
        }
        with self.assertRaisesRegex(ValueError, "nondecreasing"):
            self.calculate(item)

    def test_c_formula(self):
        item = record(); item["inputs"]["commercial_retention"] = selection(0.37)
        self.assertAlmostEqual(self.calculate(item)["base"]["scores"]["C"], 3.7)

    def test_b_n5_anchor(self):
        item = record()
        item["dataset_inputs"]["n_band"] = selection(1000)
        item["inputs"]["target_archetype_coverage"] = selection(0.5)
        item["inputs"]["five_year_sale_availability"] = selection(1.0)
        result = self.calculate(item)
        self.assertEqual(result["base"]["subfactors"]["B"]["N5"], 500)
        self.assertAlmostEqual(result["base"]["scores"]["B"], 10.0)

    def test_b_semantic_anchors_and_epsilon_monotonicity(self):
        denominator = math.log10(501)
        previous = -1
        for n5 in (0, math.nextafter(10.0, 0.0), 10, math.nextafter(10.0, math.inf),
                   21, 100, math.nextafter(500.0, 0.0), 500, math.nextafter(500.0, math.inf)):
            score = min(10.0, 10 * math.log10(1 + n5) / denominator)
            self.assertGreaterEqual(score, previous)
            previous = score
        self.assertAlmostEqual(10 * math.log10(11) / denominator, 3.86, places=2)
        self.assertAlmostEqual(10 * math.log10(101) / denominator, 7.42, places=2)

    def test_missing_n_band_retains_zero_proof_and_unbounded_upside(self):
        item = record(); item["dataset_inputs"]["n_band"] = missing()
        result = self.calculate(item)
        self.assertEqual(result["low"]["scores"]["B"], 0.0)
        self.assertEqual(result["high"]["scores"]["B"], 10.0)
        self.assertEqual(result["high"]["subfactors"]["B"]["N5"], "UNBOUNDED")
        item["inputs"]["target_archetype_coverage"] = selection(0.0)
        self.assertEqual(self.calculate(item)["high"]["scores"]["B"], 0.0)

    def test_p_uses_absolute_entry_and_downside_minimum(self):
        cases = ((4.0, 4.0, 10.0), (5.0, 5.0, 9.0), (10.0, 10.0, 4.0), (5.0, 2.5, 0.0))
        for buy, exit_, expected in cases:
            item = record()
            item["inputs"]["buy_mult"] = selection(buy)
            item["inputs"]["downside_exit_mult"] = selection(exit_)
            self.assertAlmostEqual(self.calculate(item)["base"]["scores"]["P"], expected)

    def test_p_entry_and_resilience_anchors_with_epsilon(self):
        for buy, entry in ((4, 10), (6, 8), (8, 6), (10, 4), (12, 2), (14, 0)):
            _score, actual, _resilience = scoring._price_scores(buy, buy, self.thresholds)
            self.assertAlmostEqual(actual, entry)
        for ratio, resilience in ((0.5, 0), (0.75, 5), (1.0, 10), (1.25, 10)):
            _score, _entry, actual = scoring._price_scores(4, 4 * ratio, self.thresholds)
            self.assertAlmostEqual(actual, resilience)
        for anchor in (4.0, 6.0, 8.0, 10.0, 12.0, 14.0):
            below = scoring._price_scores(math.nextafter(anchor, 0.0), anchor, self.thresholds)[1]
            at = scoring._price_scores(anchor, anchor, self.thresholds)[1]
            above = scoring._price_scores(math.nextafter(anchor, math.inf), anchor, self.thresholds)[1]
            self.assertGreaterEqual(below, at)
            self.assertGreaterEqual(at, above)

    def test_missing_p_primitives_use_tight_monotonic_bounds(self):
        item = record(); item["inputs"]["downside_exit_mult"] = missing()
        result = self.calculate(item)
        self.assertEqual(result["low"]["scores"]["P"], 0.0)
        self.assertEqual(result["high"]["scores"]["P"], 10.0)  # buy.low=4 => E=10
        item = record(); item["inputs"]["buy_mult"] = missing(); item["inputs"]["downside_exit_mult"] = selection(0)
        self.assertEqual(self.calculate(item)["high"]["scores"]["P"], 0.0)

    def test_tier_cuts_and_weak_link_floors(self):
        cases = (
            (7.5, 6.0, "hell_yes"), (7.5, math.nextafter(6.0, 0.0), "strong"),
            (6.0, 4.0, "strong"), (6.0, math.nextafter(4.0, 0.0), "conditional"),
            (4.5, 2.0, "conditional"), (4.5, math.nextafter(2.0, 0.0), "pass"),
            (3.0, 1.0, "pass"), (3.0, math.nextafter(1.0, 0.0), "kill"),
        )
        for aggregate, minimum, expected in cases:
            scores = {name: 10.0 for name in scoring.FACTOR_NAMES}; scores["V"] = minimum
            self.assertEqual(scoring._raw_verdict(aggregate, scores, self.thresholds), expected)

    def test_frozen_factor_sentinels(self):
        cases = (
            ([8, 8, 8, 8, 8], "hell_yes"),
            ([7, 7, 7, 7, 7], "strong"),
            ([5, 5, 5, 5, 5], "conditional"),
            ([10, 1.5, 10, 10, 10], "pass"),
            ([10, 0.9, 10, 10, 10], "kill"),
            ([10, 10, 10, 0, 10], "kill"),
        )
        for values, expected in cases:
            scores = dict(zip(scoring.FACTOR_NAMES, values))
            self.assertEqual(scoring._raw_verdict(scoring.geometric_mean(values), scores, self.thresholds), expected)

    def test_numeric_survival_gate_boundaries(self):
        for value, expected in ((0.249999, "kill"), (0.25, "pass"), (0.499999, "pass"),
                                (0.5, "conditional"), (0.749999, "conditional"), (0.75, "hell_yes")):
            verdict, _ = scoring._gate_verdict("hell_yes", value, self.thresholds)
            self.assertEqual(verdict, expected)

    def test_missing_factor_makes_base_and_decision_indeterminate(self):
        item = record(); item["inputs"]["commercial_retention"] = missing()
        result = self.calculate(item)
        self.assertIsNone(result["base"]["scores"]["C"])
        self.assertIsNone(result["base"]["S"])
        self.assertEqual(result["decision"]["raw_verdict"], "indeterminate")
        self.assertEqual(result["decision"]["economic_verdict"], "indeterminate")
        self.assertEqual(result["decision"]["action"], "EVIDENCE_FIRST")

    def test_missing_survival_spans_kill_to_uncapped(self):
        item = record(); item["inputs"]["y5_survival"] = missing()
        result = self.calculate(item)
        self.assertEqual(result["decision"]["sensitivity"]["low_verdict"], "kill")
        self.assertGreater(scoring.VERDICT_ORDER[result["decision"]["sensitivity"]["high_verdict"]], 0)
        self.assertEqual(result["decision"]["economic_verdict"], "indeterminate")
        self.assertEqual(result["decision"]["action"], "EVIDENCE_FIRST")

    def test_stable_structural_kill_overrides_unproven_action(self):
        item = record()
        item["inputs"]["commercial_retention"] = missing()
        item["inputs"]["target_archetype_coverage"] = selection(0.0)
        result = self.calculate(item)
        self.assertEqual(result["decision"]["economic_verdict"], "kill")
        self.assertTrue(result["decision"]["sensitivity"]["stable_structural_kill"])
        self.assertEqual(result["decision"]["action"], "AVOID")

    def test_action_instability_is_provisional_and_forces_evidence_first(self):
        item = support_forward_inputs(record())
        item["inputs"]["commercial_retention"] = selection(0.8, 0.05, 0.9)
        item["inputs"]["commercial_retention"].update(evidence_state="PROXY", bridge_supported=True)
        result = self.calculate(item)
        self.assertEqual(result["decision"]["evidence_readiness"]["status"], "PROVISIONAL")
        self.assertTrue(result["decision"]["sensitivity"]["action_instability"])
        self.assertEqual(result["decision"]["action"], "EVIDENCE_FIRST")

    def test_evidence_state_does_not_change_values_or_gates(self):
        direct = record()
        proxy = copy.deepcopy(direct)
        for item in proxy["inputs"].values():
            if isinstance(item, dict) and "evidence_state" in item:
                item["evidence_state"] = "PROXY"
        proxy["dataset_inputs"]["n_band"]["evidence_state"] = "PROXY"
        for role in proxy["inputs"]["target_role_mix"]["roles"]:
            role["removable_fraction"]["evidence_state"] = "PROXY"
        for item in proxy["inputs"]["implementation_ramp"].values():
            item["evidence_state"] = "PROXY"
        first, second = self.calculate(direct), self.calculate(proxy)
        self.assertEqual({b: first[b] for b in scoring.BOUNDS}, {b: second[b] for b in scoring.BOUNDS})
        self.assertEqual(first["decision"]["economic_verdict"], second["decision"]["economic_verdict"])

    def test_any_low_quality_critical_input_is_unproven(self):
        item = record()
        item["inputs"]["commercial_retention"]["evidence_quality"] = "LOW"
        result = self.calculate(item)
        self.assertEqual(result["decision"]["evidence_readiness"]["status"], "UNPROVEN")
        self.assertEqual(result["decision"]["action"], "EVIDENCE_FIRST")

    def test_archetype_selection_uncertainty_is_unproven_without_changing_economics(self):
        stable = self.calculate(record())
        item = record(); item["inputs"]["target_archetype"]["selection_uncertainty"] = True
        uncertain = self.calculate(item)
        self.assertEqual({bound: stable[bound] for bound in scoring.BOUNDS},
                         {bound: uncertain[bound] for bound in scoring.BOUNDS})
        self.assertEqual(uncertain["decision"]["evidence_readiness"]["status"], "UNPROVEN")
        self.assertTrue(uncertain["decision"]["evidence_readiness"]["selection_uncertainty"])
        self.assertEqual(uncertain["decision"]["action"], "EVIDENCE_FIRST")

    def test_generic_forward_proxy_cannot_claim_substantiated(self):
        item = support_forward_inputs(record())
        item["inputs"]["commercial_retention"]["bridge_supported"] = False
        result = self.calculate(item)
        self.assertEqual(result["decision"]["evidence_readiness"]["status"], "PROVISIONAL")

    def test_unbridged_core_proxy_is_unproven(self):
        item = record()
        item["dataset_inputs"]["n_band"].update(evidence_state="PROXY", bridge_supported=False)
        result = self.calculate(item)
        self.assertEqual(result["decision"]["evidence_readiness"]["status"], "UNPROVEN")

    def test_target_role_mix_basis_provenance_controls_readiness(self):
        # Backward-compatible scorer fixtures default the absent basis fields
        # to DIRECT/MED/bridge-supported.
        self.assertNotEqual(self.calculate(support_forward_inputs(record()))["decision"]["evidence_readiness"]["status"],
                            "UNPROVEN")
        item = support_forward_inputs(record())
        item["inputs"]["target_role_mix"].update(
            basis_evidence_state="PROXY", basis_evidence_quality="MED",
            basis_bridge_supported=False)
        self.assertEqual(self.calculate(item)["decision"]["evidence_readiness"]["status"], "UNPROVEN")
        item = support_forward_inputs(record())
        item["inputs"]["target_role_mix"].update(
            basis_evidence_state="ASSUMPTION", basis_evidence_quality="NONE",
            basis_bridge_supported=False)
        self.assertEqual(self.calculate(item)["decision"]["evidence_readiness"]["status"], "UNPROVEN")

    def test_forward_direct_without_temporal_population_bridge_is_unproven(self):
        item = support_forward_inputs(record())
        item["inputs"]["commercial_retention"].update(evidence_state="DIRECT", bridge_supported=False)
        result = self.calculate(item)
        self.assertEqual(result["decision"]["evidence_readiness"]["status"], "UNPROVEN")
        self.assertEqual(result["decision"]["action"], "EVIDENCE_FIRST")

    def test_machine_supported_forward_proxy_can_be_substantiated_when_stable(self):
        item = record()
        for name in ("commercial_retention", "five_year_sale_availability", "downside_exit_mult", "y5_survival"):
            item["inputs"][name].update(evidence_state="PROXY", bridge_supported=True)
        for ramp in item["inputs"]["implementation_ramp"].values():
            ramp.update(evidence_state="PROXY", bridge_supported=True)
        for role in item["inputs"]["target_role_mix"]["roles"]:
            role["removable_fraction"].update(evidence_state="PROXY", bridge_supported=True)
        # Collapse ranges so scenario stability is not the limiting condition.
        for selection_ in [item["dataset_inputs"]["n_band"], item["inputs"]["target_labor_cost_share"],
                           item["inputs"]["target_archetype_coverage"], item["inputs"]["buy_mult"],
                           *(item["inputs"]["implementation_ramp"].values()),
                           item["inputs"]["commercial_retention"], item["inputs"]["five_year_sale_availability"],
                           item["inputs"]["downside_exit_mult"], item["inputs"]["y5_survival"],
                           *(role["removable_fraction"] for role in item["inputs"]["target_role_mix"]["roles"])]:
            selection_["range"] = {"low": selection_["value"], "high": selection_["value"]}
        result = self.calculate(item)
        self.assertEqual(result["decision"]["evidence_readiness"]["status"], "SUBSTANTIATED")

    def test_all_known_strong_to_hell_yes_interval_is_indeterminate(self):
        item = support_forward_inputs(record())
        item["inputs"]["target_labor_cost_share"] = selection(0.5)
        for role in item["inputs"]["target_role_mix"]["roles"]:
            role["removable_fraction"] = selection(0.8)
        for ramp in item["inputs"]["implementation_ramp"].values():
            ramp.update(value=0.7, range={"low": 0.4, "high": 0.9})
        item["inputs"]["commercial_retention"].update(value=0.7, range={"low": 0.4, "high": 0.9})
        item["dataset_inputs"]["n_band"] = selection(500)
        item["inputs"]["target_archetype_coverage"] = selection(1.0)
        item["inputs"]["five_year_sale_availability"].update(value=1.0, range={"low": 1.0, "high": 1.0})
        item["inputs"]["buy_mult"] = selection(5.0)
        item["inputs"]["downside_exit_mult"].update(value=5.0, range={"low": 5.0, "high": 5.0})
        item["inputs"]["y5_survival"].update(value=0.8, range={"low": 0.8, "high": 0.8})
        result = self.calculate(item)
        self.assertEqual(result["decision"]["sensitivity"]["low_verdict"], "strong")
        self.assertEqual(result["decision"]["sensitivity"]["high_verdict"], "hell_yes")
        self.assertEqual(result["decision"]["economic_verdict"], "indeterminate")
        self.assertEqual(result["decision"]["action"], "EVIDENCE_FIRST")

    def test_all_known_kill_to_conditional_interval_is_indeterminate(self):
        item = support_forward_inputs(record())
        item["inputs"]["commercial_retention"].update(value=0.25, range={"low": 0.05, "high": 0.5})
        item["inputs"]["y5_survival"].update(value=0.7, range={"low": 0.7, "high": 0.7})
        result = self.calculate(item)
        self.assertEqual(result["decision"]["sensitivity"]["low_verdict"], "kill")
        self.assertEqual(result["decision"]["sensitivity"]["high_verdict"], "conditional")
        self.assertEqual(result["decision"]["economic_verdict"], "indeterminate")
        self.assertEqual(result["decision"]["action"], "EVIDENCE_FIRST")

    def test_invalid_numeric_selections_are_rejected(self):
        mutations = []
        item = record(); item["inputs"]["commercial_retention"] = selection(float("nan")); mutations.append(item)
        item = record(); item["inputs"]["buy_mult"] = selection(0); mutations.append(item)
        item = record(); item["dataset_inputs"]["n_band"] = selection(1.5); mutations.append(item)
        item = record(); item["inputs"]["commercial_retention"] = selection(0.5, 0.6, 0.7); mutations.append(item)
        item = record(); item["inputs"]["commercial_retention"] = selection(0.5, state="MISSING"); mutations.append(item)
        for malformed in mutations:
            with self.assertRaises(ValueError):
                self.calculate(malformed)

    def test_unknown_evidence_enums_are_rejected(self):
        for field, value in (("method", "MODELED"), ("evidence_state", "HEARSAY"),
                             ("evidence_quality", "GOOD")):
            item = record(); item["inputs"]["commercial_retention"][field] = value
            with self.assertRaises(ValueError):
                self.calculate(item)

    def test_randomized_valid_records_preserve_score_and_verdict_order(self):
        rng = random.Random(41001)
        for _ in range(3000):
            item = record()
            def ordered(low_domain, high_domain):
                return sorted(rng.uniform(low_domain, high_domain) for _unused in range(3))
            low, base, high = ordered(0, 1); item["inputs"]["target_labor_cost_share"] = selection(base, low, high)
            for role in item["inputs"]["target_role_mix"]["roles"]:
                low, base, high = ordered(0, 1); role["removable_fraction"] = selection(base, low, high)
            ramp_base = sorted(rng.random() for _unused in range(5))
            ramp_low = sorted(rng.uniform(0, value) for value in ramp_base)
            ramp_high = sorted(rng.uniform(value, 1) for value in ramp_base)
            # Sorting highs can move an element below its base; cumulative maxima repairs that coherently.
            ramp_high = [max(ramp_high[index], ramp_base[index]) for index in range(5)]
            for year in range(5):
                item["inputs"]["implementation_ramp"]["r%d" % (year + 1)] = selection(
                    ramp_base[year], ramp_low[year], ramp_high[year])
            for name in ("commercial_retention", "target_archetype_coverage",
                         "five_year_sale_availability", "y5_survival"):
                low, base, high = ordered(0, 1); item["inputs"][name] = selection(base, low, high)
            low, base, high = sorted(rng.randint(0, 2000) for _unused in range(3)); item["dataset_inputs"]["n_band"] = selection(base, low, high)
            low, base, high = ordered(0.1, 20); item["inputs"]["buy_mult"] = selection(base, low, high)
            low, base, high = ordered(0, 20); item["inputs"]["downside_exit_mult"] = selection(base, low, high)
            result = self.calculate(item)
            for factor in scoring.FACTOR_NAMES:
                values = [result[bound]["scores"][factor] for bound in scoring.BOUNDS]
                self.assertLessEqual(values[0], values[1] + scoring.EPS)
                self.assertLessEqual(values[1], values[2] + scoring.EPS)
            aggregates = [result[bound]["S"] for bound in scoring.BOUNDS]
            self.assertLessEqual(aggregates[0], aggregates[1] + scoring.EPS)
            self.assertLessEqual(aggregates[1], aggregates[2] + scoring.EPS)
            decision = result["decision"]
            if decision["economic_verdict"] == "indeterminate":
                self.assertNotEqual(decision["sensitivity"]["low_verdict"],
                                    decision["sensitivity"]["high_verdict"])
                self.assertEqual(decision["action"], "EVIDENCE_FIRST")
            else:
                self.assertEqual(decision["sensitivity"]["low_verdict"], decision["economic_verdict"])
                self.assertEqual(decision["economic_verdict"], decision["sensitivity"]["high_verdict"])


if __name__ == "__main__":
    unittest.main()
