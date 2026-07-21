#!/usr/bin/env python3

import copy
import importlib.util
import itertools
import math
import os
import random
import unittest


HERE = os.path.dirname(os.path.abspath(__file__))
SPEC = importlib.util.spec_from_file_location("v4_2_scoring_tests", os.path.join(HERE, "v4_2_scoring.py"))
scoring = importlib.util.module_from_spec(SPEC); SPEC.loader.exec_module(scoring)


def selection(value, low=None, high=None, *, state="DIRECT", quality="MED", method=None,
              validated=True, state_id=None):
    method = method or ("ESTIMATE" if state in ("PROXY", "ASSUMPTION", "MISSING") else "OBSERVED")
    missing = state == "MISSING"
    item = {
        "value": None if missing else value,
        "range": {"low": None if missing else (value if low is None else low),
                  "high": None if missing else (value if high is None else high)},
        "method": method, "evidence_state": state,
        "evidence_quality": "NONE" if state in ("ASSUMPTION", "MISSING") else quality,
        "source_ids": [] if state in ("ASSUMPTION", "MISSING") else ["S1"],
        "bridge_supported": state == "PROXY",
        "endpoints_supported": not missing,
        "independent_validation": validated if state == "PROXY" else False,
        "longitudinal_validation": False,
    }
    if state_id is not None: item["normalized_y5_state_digest"] = state_id
    return item


def proxy(value, low=None, high=None, validated=True, state_id=None):
    return selection(value, low, high, state="PROXY", validated=validated, state_id=state_id)


def missing():
    return selection(None, state="MISSING")


def state(validated=True):
    return {"state_id": "normalized-state-1", "state_digest": "d" * 64,
            "method": "ESTIMATE", "evidence_state": "PROXY",
            "evidence_quality": "MED", "source_ids": ["S1"], "bridge_supported": True,
            "endpoints_supported": True, "independent_validation": validated,
            "longitudinal_validation": False, "rationale_separation_passed": True}


def record():
    return {
        "dataset_inputs": {"n_band": selection(1000)},
        "inputs": {
            "target_archetype": {"selection_uncertainty": False,
                                 "enumeration_coverage": {"base": .9, "low": .8, "high": 1.0}},
            "recognized_revenue": selection(100),
            "pass_through_reconciliation": {
                "revenue_basis": "GROSS_OF_ALL", "included_cost_ids": ["pass-media"],
                "already_netted_cost_ids": [], "supported": True, "method": "OBSERVED",
                "evidence_state": "DIRECT", "evidence_quality": "MED", "source_ids": ["S1"],
                "bridge_supported": False, "independent_validation": False,
                "longitudinal_validation": False, "rationale": "Direct accounting reconciliation.",
                "caveats": []},
            "third_party_pass_through": [
                {"category": "documented media", "cost_id": "pass-media", "amount": selection(20)}],
            "numerator_cost_ids": ["employee", "controlled-contractors"],
            "employee_cash_cost": selection(30),
            "controllable_contractor_cash_cost": selection(10),
            "target_role_mix": {
                "spec_mode": "frozen", "basis_method": "OBSERVED", "basis_evidence_state": "DIRECT",
                "basis_evidence_quality": "MED", "basis_source_ids": ["S1"],
                "basis_bridge_supported": False, "basis_endpoints_supported": True,
                "basis_independent_validation": False, "basis_longitudinal_validation": False,
                "roles": [
                    {"role": "delivery", "cost_weight": .6, "removable_fraction": selection(.5)},
                    {"role": "operations", "cost_weight": .4, "removable_fraction": selection(.5)},
                ]},
            "implementation_realization": {"r%d" % y: proxy(.8) for y in range(1, 6)},
            "implementation_investment": {"k%d" % y: proxy(.05 if y == 0 else 0.0)
                                            for y in range(6)},
            "commercial_retention": {"c%d" % y: proxy(.8) for y in range(1, 6)},
            "target_archetype_coverage": selection(1.0),
            "five_year_sale_availability": proxy(1.0),
            "buyer_access_win_share": proxy(.5),
            "deal_execution_capacity_5y": proxy(1000),
            "integration_onboarding_capacity_5y": proxy(1000),
            "buy_mult": selection(4.0),
            "normalized_y5_operating_state": state(),
            "downside_exit_mult": proxy(4.0, state_id="d" * 64),
            "operator_controlled_value_added_demand_share_y5": proxy(.8),
        }}


class V42ScoringTests(unittest.TestCase):
    def setUp(self): self.t = scoring.load_thresholds()
    def calculate(self, item=None): return scoring.calculate(item or record(), self.t)

    def test_threshold_contract_is_closed_and_exact(self):
        self.assertIs(scoring.validate_thresholds(self.t), self.t)
        mutations = []
        for family in ("score", "archetype_selection", "domains", "value_available", "implementation",
                       "commercial_capture", "buyability", "price_discipline", "viability_gate",
                       "survival_gate", "actions", "partial_identification", "evidence_contract",
                       "readiness", "validation_tolerances", "sentinels", "display"):
            item = copy.deepcopy(self.t); item[family]["unused"] = True; mutations.append(item)
        item = copy.deepcopy(self.t); item["unexpected"] = True; mutations.append(item)
        item = copy.deepcopy(self.t); item["verdict_cuts"]["strong"] = 6.1; mutations.append(item)
        item = copy.deepcopy(self.t); item["verdict_min_each_factor"]["pass"] = .9; mutations.append(item)
        item = copy.deepcopy(self.t); item["sentinels"]["implementation_schedules_zero_investment"][1]["expected"] += 2e-9; mutations.append(item)
        for item in mutations:
            with self.assertRaises(ValueError): scoring.validate_thresholds(item)

    def test_value_added_v_formula_and_symmetric_pass_through(self):
        result = self.calculate()
        self.assertEqual(result["base"]["subfactors"]["V"]["R_cva"], 80)
        self.assertEqual(result["base"]["subfactors"]["V"]["G"], 20)
        self.assertEqual(result["base"]["scores"]["V"], 10)
        item = record()
        item["inputs"]["recognized_revenue"] = selection(120)
        item["inputs"]["third_party_pass_through"][0]["amount"] = selection(40)
        self.assertEqual(self.calculate(item)["base"]["scores"]["V"], 10)

    def test_v_semantic_anchors(self):
        # R_cva=80 and weighted removability=.5, so total cash cost 160g realizes each g anchor.
        for g, expected in ((0, 0), (.05, 2), (.125, 5), (.20, 8), (.25, 10), (.30, 10)):
            item = record(); total_cost = 160 * g
            item["inputs"]["employee_cash_cost"] = selection(total_cost)
            item["inputs"]["controllable_contractor_cash_cost"] = selection(0)
            self.assertAlmostEqual(self.calculate(item)["base"]["scores"]["V"], expected)

    def test_pass_through_double_count_is_rejected(self):
        item = record(); item["inputs"]["numerator_cost_ids"].append("pass-media")
        with self.assertRaisesRegex(ValueError, "cannot also appear"):
            self.calculate(item)

    def test_denominator_must_be_positive_and_bounded(self):
        item = record(); item["inputs"]["third_party_pass_through"][0]["amount"] = selection(100)
        with self.assertRaisesRegex(ValueError, "positive, bounded"):
            self.calculate(item)

    def test_v_bounds_use_inverse_denominator_corners(self):
        item = record()
        item["inputs"]["recognized_revenue"] = selection(100, 90, 120)
        item["inputs"]["third_party_pass_through"][0]["amount"] = selection(20, 10, 30)
        result = self.calculate(item)
        self.assertEqual(result["low"]["subfactors"]["V"]["R_cva"], 110)
        self.assertEqual(result["high"]["subfactors"]["V"]["R_cva"], 60)
        self.assertLessEqual(result["low"]["scores"]["V"], result["high"]["scores"]["V"])

    def test_i_exact_zero_investment_anchors(self):
        tol = self.t["validation_tolerances"]["sentinel"]
        for item in self.t["sentinels"]["implementation_schedules_zero_investment"]:
            self.assertLessEqual(abs(scoring._implementation_score(item["r"], [0] * 6, self.t)
                                     - item["expected"]), tol)
        D = sum(scoring._weights(self.t))
        for item in self.t["sentinels"]["implementation_investment_cases"]:
            actual = scoring._implementation_score(
                item["r"], [item["k0_annuity_fraction"] * D] + [0] * 5, self.t)
            self.assertLessEqual(abs(actual - item["expected"]), tol)

    def test_c_exact_constant_schedule_anchors(self):
        tol = self.t["validation_tolerances"]["sentinel"]
        for sentinel in self.t["sentinels"]["commercial_constant_schedules"]:
            actual = scoring._commercial_score([1] * 5, [sentinel["value"]] * 5, self.t)
            self.assertLessEqual(abs(actual - sentinel["expected"]), tol)

    def test_equal_c_schedules_canonicalize_to_exactly_equal_support(self):
        item = record()
        for year in range(1, 6):
            item["inputs"]["implementation_realization"]["r%d" % year] = proxy(.5, .1, 1)
            item["inputs"]["commercial_retention"]["c%d" % year] = proxy(.8)
        result = self.calculate(item)
        values = [result[bound]["scores"]["C"] for bound in scoring.BOUNDS]
        self.assertEqual(values, [8, 8, 8])

    def test_c_timing_regression_weights_only_realized_savings(self):
        sentinel = self.t["sentinels"]["commercial_timing_case"]
        self.assertAlmostEqual(scoring._commercial_score(sentinel["r"], sentinel["c"], self.t), .01)
        item = record()
        for year, value in enumerate(sentinel["r"], 1):
            item["inputs"]["implementation_realization"]["r%d" % year] = proxy(value)
        for year, value in enumerate(sentinel["c"], 1):
            item["inputs"]["commercial_retention"]["c%d" % year] = proxy(value)
        for year in range(6): item["inputs"]["implementation_investment"]["k%d" % year] = proxy(0)
        result = self.calculate(item)
        self.assertAlmostEqual(result["base"]["scores"]["C"], .01)
        self.assertGreater(result["base"]["subfactors"]["h"]["h"], 0)
        self.assertEqual(result["decision"]["economic_verdict"], "kill")

    def test_seed_42003_realization_weight_counterexample_has_sound_support(self):
        item = record()
        lows = [0, 0, 0, 0, .1]
        for year in range(1, 6):
            item["inputs"]["implementation_realization"]["r%d" % year] = proxy(
                .5, lows[year - 1], 1)
            retention = 1 if year == 5 else 0
            item["inputs"]["commercial_retention"]["c%d" % year] = proxy(retention)
        result = self.calculate(item)
        values = [result[bound]["scores"]["C"] for bound in scoring.BOUNDS]
        # Naive coherent endpoint ratios put low C above base C. Joint vertex
        # optimization retains the full feasible support and contains base.
        self.assertLessEqual(values[0], values[1])
        self.assertLessEqual(values[1], values[2])
        self.assertGreater(values[2], values[1])

    def test_joint_decision_support_rejects_impossible_marginal_bundle(self):
        x = .043293960941
        item = record()
        item["inputs"]["employee_cash_cost"] = selection(26)
        item["inputs"]["controllable_contractor_cash_cost"] = selection(0)
        n5 = 501 ** .65 - 1
        item["inputs"]["buyer_access_win_share"] = proxy(n5 / 1000)
        item["inputs"]["buy_mult"] = selection(7.5)
        item["inputs"]["downside_exit_mult"] = proxy(7.5, state_id="d" * 64)
        for year in range(1, 5):
            item["inputs"]["implementation_realization"]["r%d" % year] = proxy(x, x, 1)
        item["inputs"]["implementation_realization"]["r5"] = proxy(1)
        for year in range(1, 6):
            item["inputs"]["commercial_retention"]["c%d" % year] = proxy(
                .05 if year < 5 else 1)
        for year in range(6):
            item["inputs"]["implementation_investment"]["k%d" % year] = proxy(0)
        item["inputs"]["operator_controlled_value_added_demand_share_y5"] = proxy(.8)
        result = self.calculate(item)
        self.assertEqual(result["low"]["scores"]["I"], 1.9999999999998344)
        self.assertGreater(result["high"]["scores"]["C"], 8)
        self.assertEqual(result["decision"]["sensitivity"]["low_verdict"], "conditional")
        self.assertEqual(result["decision"]["sensitivity"]["high_verdict"], "conditional")
        self.assertEqual(result["decision"]["economic_verdict"], "conditional")
        self.assertEqual(result["decision"]["action"], "SELECTIVE")

    def test_random_brute_interior_verdicts_are_contained_by_joint_bounds(self):
        rng = random.Random(42004)
        rank = {name: index for index, name in enumerate(self.t["verdict_order"])}
        for _ in range(20):
            low, high = sorted((rng.uniform(0, .4), rng.uniform(.6, 1)))
            base = (low + high) / 2
            capture = [rng.random() for _year in range(5)]
            investment = [rng.uniform(0, .05)] + [rng.uniform(0, .03) for _year in range(5)]
            item = record()
            for year in range(1, 6):
                item["inputs"]["implementation_realization"]["r%d" % year] = proxy(base, low, high)
                item["inputs"]["commercial_retention"]["c%d" % year] = proxy(capture[year - 1])
            for year in range(6):
                item["inputs"]["implementation_investment"]["k%d" % year] = proxy(investment[year])
            item["inputs"]["operator_controlled_value_added_demand_share_y5"] = proxy(.8)
            result = self.calculate(item)
            lower = rank[result["decision"]["sensitivity"]["low_verdict"]]
            upper = rank[result["decision"]["sensitivity"]["high_verdict"]]
            fixed = {name: result["base"]["scores"][name] for name in ("V", "B", "P")}
            for _sample in range(50):
                realization = [rng.uniform(low, high) for _year in range(5)]
                scores = {"I": scoring._implementation_score(realization, investment, self.t),
                          "C": scoring._commercial_score(realization, capture, self.t), **fixed}
                verdict = scoring._raw_verdict(scoring.geometric_mean(scores.values()), scores, self.t)
                if scoring._h_value(realization, investment, capture, self.t) <= 0:
                    verdict = "kill"
                verdict, _reasons = scoring._survival_gate(verdict, .8, self.t)
                self.assertLessEqual(lower, rank[verdict])
                self.assertLessEqual(rank[verdict], upper)

    def test_random_feasible_c_samples_are_contained_by_brute_box_vertex_extrema(self):
        rng = random.Random(42003)
        tolerance = self.t["validation_tolerances"]["sentinel"]
        for _ in range(12):
            item = record()
            center = sorted(rng.uniform(.05, .95) for _x in range(5))
            lows = sorted(rng.uniform(0, value) for value in center)
            highs = []
            previous = 0
            for value in center:
                previous = max(value, rng.uniform(previous, 1))
                highs.append(previous)
            c_lows, c_bases, c_highs = [], [], []
            for year in range(5):
                item["inputs"]["implementation_realization"]["r%d" % (year + 1)] = proxy(
                    center[year], lows[year], highs[year])
                c_low, c_base, c_high = sorted(rng.random() for _x in range(3))
                c_lows.append(c_low); c_bases.append(c_base); c_highs.append(c_high)
                item["inputs"]["commercial_retention"]["c%d" % (year + 1)] = proxy(
                    c_base, c_low, c_high)
            result = self.calculate(item)
            support_low = result["low"]["scores"]["C"]
            support_high = result["high"]["scores"]["C"]

            brute_vertices = list(itertools.product(
                *((lows[index], highs[index]) for index in range(5))))
            self.assertTrue(brute_vertices)
            brute_low = min(scoring._commercial_score(values, c_lows, self.t)
                            for values in brute_vertices)
            brute_high = max(scoring._commercial_score(values, c_highs, self.t)
                             for values in brute_vertices)
            self.assertAlmostEqual(support_low, brute_low, delta=tolerance)
            self.assertAlmostEqual(support_high, brute_high, delta=tolerance)

            accepted = 0
            for _attempt in range(5000):
                realization = [rng.uniform(lows[i], highs[i]) for i in range(5)]
                retention = [rng.uniform(c_lows[i], c_highs[i]) for i in range(5)]
                score = scoring._commercial_score(realization, retention, self.t)
                self.assertLessEqual(support_low, score + tolerance)
                self.assertLessEqual(score, support_high + tolerance)
                accepted += 1
                if accepted == 20:
                    break
            self.assertGreater(accepted, 0)

    def test_zero_realization_makes_c_exactly_zero(self):
        item = record()
        for year in range(1, 6):
            item["inputs"]["implementation_realization"]["r%d" % year] = proxy(0)
            item["inputs"]["commercial_retention"]["c%d" % year] = missing()
        result = self.calculate(item)
        self.assertEqual(result["base"]["scores"]["C"], 0)

    def test_investment_changes_i_and_h_not_c(self):
        first = self.calculate(record())
        item = record(); item["inputs"]["implementation_investment"]["k0"] = proxy(.5)
        second = self.calculate(item)
        self.assertLess(second["base"]["scores"]["I"], first["base"]["scores"]["I"])
        self.assertLess(second["base"]["subfactors"]["h"]["h"], first["base"]["subfactors"]["h"]["h"])
        self.assertEqual(second["base"]["scores"]["C"], first["base"]["scores"]["C"])

    def test_c_changes_c_and_h_not_i(self):
        first = self.calculate(record())
        item = record()
        for y in range(1, 6): item["inputs"]["commercial_retention"]["c%d" % y] = proxy(.2)
        second = self.calculate(item)
        self.assertLess(second["base"]["scores"]["C"], first["base"]["scores"]["C"])
        self.assertLess(second["base"]["subfactors"]["h"]["h"], first["base"]["subfactors"]["h"]["h"])
        self.assertEqual(second["base"]["scores"]["I"], first["base"]["scores"]["I"])

    def test_realization_ramp_then_decay_is_valid_and_affects_i_c_h(self):
        decayed = record()
        sustained = record()
        decayed_path = [.2, .8, .9, .4, .1]
        sustained_path = [.2, .8, .9, .9, .9]
        retention = [0, 0, 0, 1, 1]
        for year in range(1, 6):
            decayed["inputs"]["implementation_realization"]["r%d" % year] = proxy(
                decayed_path[year - 1])
            sustained["inputs"]["implementation_realization"]["r%d" % year] = proxy(
                sustained_path[year - 1])
            decayed["inputs"]["commercial_retention"]["c%d" % year] = proxy(retention[year - 1])
            sustained["inputs"]["commercial_retention"]["c%d" % year] = proxy(retention[year - 1])
        for year in range(6):
            decayed["inputs"]["implementation_investment"]["k%d" % year] = proxy(0)
            sustained["inputs"]["implementation_investment"]["k%d" % year] = proxy(0)
        down, held = self.calculate(decayed), self.calculate(sustained)
        self.assertLess(down["base"]["scores"]["I"], held["base"]["scores"]["I"])
        self.assertLess(down["base"]["scores"]["C"], held["base"]["scores"]["C"])
        self.assertLess(down["base"]["subfactors"]["h"]["h"],
                        held["base"]["subfactors"]["h"]["h"])

    def test_h_nonpositive_kills_before_survival(self):
        item = record(); D = sum(scoring._weights(self.t))
        for y in range(1, 6):
            item["inputs"]["implementation_realization"]["r%d" % y] = proxy(1)
            item["inputs"]["commercial_retention"]["c%d" % y] = proxy(.2)
        item["inputs"]["implementation_investment"]["k0"] = proxy(.25 * D)
        result = self.calculate(item)
        self.assertGreater(result["base"]["scores"]["I"], 0)
        self.assertGreater(result["base"]["scores"]["C"], 0)
        self.assertLess(result["base"]["subfactors"]["h"]["h"], 0)
        self.assertEqual(result["decision"]["economic_verdict"], "kill")
        self.assertIn("operating_value_viability_h_le_0", result["decision"]["gate_reasons"])

    def test_h_zero_boundary_and_epsilon(self):
        D = sum(scoring._weights(self.t))
        retained = .8 * .8 * D
        for k0, killed in ((math.nextafter(retained, 0), False), (retained, True),
                           (math.nextafter(retained, math.inf), True)):
            item = record(); item["inputs"]["implementation_investment"]["k0"] = proxy(k0)
            result = self.calculate(item)
            self.assertEqual(result["base"]["subfactors"]["h"]["gate_triggered"], killed)

    def test_zero_g_forces_v_i_zero_and_kill(self):
        item = record(); item["inputs"]["employee_cash_cost"] = selection(0)
        item["inputs"]["controllable_contractor_cash_cost"] = selection(0)
        result = self.calculate(item)
        self.assertEqual(result["base"]["scores"]["V"], 0)
        self.assertEqual(result["base"]["scores"]["I"], 0)
        self.assertEqual(result["decision"]["economic_verdict"], "kill")

    def test_zero_g_annihilates_missing_denominator_support(self):
        item = record()
        item["inputs"]["recognized_revenue"] = missing()
        item["inputs"]["employee_cash_cost"] = selection(0)
        item["inputs"]["controllable_contractor_cash_cost"] = selection(0)
        result = self.calculate(item)
        for bound in scoring.BOUNDS:
            self.assertEqual(result[bound]["scores"]["V"], 0)
            self.assertEqual(result[bound]["scores"]["I"], 0)
            self.assertEqual(result[bound]["subfactors"]["V"]["G"], 0)
            self.assertEqual(result[bound]["subfactors"]["h"]["h"], 0)
        self.assertEqual(result["decision"]["economic_verdict"], "kill")
        self.assertTrue(result["decision"]["sensitivity"]["stable_structural_kill"])
        self.assertEqual(result["decision"]["action"], "AVOID")

        item = record()
        item["inputs"]["recognized_revenue"] = missing()
        for role in item["inputs"]["target_role_mix"]["roles"]:
            role["removable_fraction"] = selection(0)
        result = self.calculate(item)
        self.assertEqual([result[bound]["scores"]["V"] for bound in scoring.BOUNDS], [0, 0, 0])
        self.assertEqual(result["decision"]["economic_verdict"], "kill")

        item = record()
        item["inputs"]["recognized_revenue"] = missing()
        result = self.calculate(item)
        self.assertEqual(result["low"]["scores"]["V"], 0)
        self.assertIsNone(result["base"]["scores"]["V"])
        self.assertEqual(result["high"]["scores"]["V"], 10)

    def test_missing_g_makes_v_i_and_h_base_missing(self):
        item = record(); item["inputs"]["employee_cash_cost"] = missing()
        result = self.calculate(item)
        self.assertIsNone(result["base"]["scores"]["V"])
        self.assertIsNone(result["base"]["scores"]["I"])
        self.assertIsNone(result["base"]["subfactors"]["h"]["h"])
        self.assertEqual(result["decision"]["economic_verdict"], "indeterminate")

    def test_missing_investment_has_unbounded_downside(self):
        item = record(); item["inputs"]["implementation_investment"]["k0"] = missing()
        result = self.calculate(item)
        self.assertEqual(result["low"]["scores"]["I"], 0)
        self.assertIsNone(result["base"]["scores"]["I"])
        self.assertTrue(result["low"]["subfactors"]["h"]["gate_triggered"])
        self.assertIsNone(result["low"]["subfactors"]["h"]["h"])

    def test_b_includes_access_win_and_is_monotone(self):
        item = record(); item["inputs"]["buyer_access_win_share"] = proxy(0)
        self.assertEqual(self.calculate(item)["base"]["scores"]["B"], 0)
        previous = -1
        for access in (0, .01, .1, .5, 1):
            item = record(); item["inputs"]["buyer_access_win_share"] = proxy(access)
            score = self.calculate(item)["base"]["scores"]["B"]
            self.assertGreaterEqual(score, previous); previous = score

    def test_b_exact_anchors(self):
        denominator = math.log10(501)
        for n5, expected in ((0, 0.0), (10, 3.8572417711649964),
                             (21, 4.972234693812908), (100, 7.42385868076131), (500, 10.0)):
            actual = 10 * min(1, math.log10(1 + n5) / denominator)
            self.assertAlmostEqual(actual, expected)

    def test_missing_capacity_high_respects_every_known_capacity_ceiling(self):
        item = record()
        item["inputs"]["deal_execution_capacity_5y"] = missing()
        item["inputs"]["integration_onboarding_capacity_5y"] = proxy(30, 20, 40)
        result = self.calculate(item)
        self.assertEqual(result["low"]["subfactors"]["B"]["K5"], 0)
        self.assertIsNone(result["base"]["subfactors"]["B"]["K5"])
        self.assertEqual(result["high"]["subfactors"]["B"]["K5"], 40)
        self.assertEqual(result["high"]["subfactors"]["B"]["N5"], 40)

        item = record()
        item["inputs"]["integration_onboarding_capacity_5y"] = missing()
        item["inputs"]["deal_execution_capacity_5y"] = proxy(25, 10, 35)
        result = self.calculate(item)
        self.assertEqual(result["high"]["subfactors"]["B"]["K5"], 35)
        self.assertEqual(result["high"]["subfactors"]["B"]["N5"], 35)

    def test_access_changes_b_not_p_and_buy_changes_p_not_b(self):
        first = self.calculate(record())
        item = record(); item["inputs"]["buyer_access_win_share"] = proxy(.1)
        second = self.calculate(item)
        self.assertNotEqual(first["base"]["scores"]["B"], second["base"]["scores"]["B"])
        self.assertEqual(first["base"]["scores"]["P"], second["base"]["scores"]["P"])
        item = record(); item["inputs"]["buy_mult"] = selection(8)
        third = self.calculate(item)
        self.assertEqual(first["base"]["scores"]["B"], third["base"]["scores"]["B"])
        self.assertNotEqual(first["base"]["scores"]["P"], third["base"]["scores"]["P"])

    def test_p_requires_matching_normalized_state(self):
        item = record(); item["inputs"]["downside_exit_mult"]["normalized_y5_state_digest"] = "wrong"
        with self.assertRaisesRegex(ValueError, "link the frozen y5 state"):
            self.calculate(item)

    def test_missing_exit_or_state_preserves_known_entry_score_ceiling(self):
        for missing_path in ("exit", "state"):
            item = record()
            item["inputs"]["buy_mult"] = selection(13, 13, 13)
            if missing_path == "exit":
                item["inputs"]["downside_exit_mult"] = missing()
            else:
                item["inputs"]["normalized_y5_operating_state"] = {
                    "state_id": None, "state_digest": None, "method": "ESTIMATE",
                    "evidence_state": "MISSING", "evidence_quality": "NONE", "source_ids": [],
                    "bridge_supported": False, "endpoints_supported": False,
                    "independent_validation": False, "longitudinal_validation": False,
                    "rationale_separation_passed": True}
            result = self.calculate(item)
            self.assertIsNone(result["base"]["scores"]["P"])
            self.assertLessEqual(result["high"]["scores"]["P"], 1)
            self.assertEqual(result["high"]["subfactors"]["P"]["entry_score"], 1)

    def test_missing_state_is_explicit_in_evidence_summary(self):
        item = record()
        item["inputs"]["normalized_y5_operating_state"] = {
            "state_id": None, "state_digest": None, "method": "ESTIMATE",
            "evidence_state": "MISSING", "evidence_quality": "NONE", "source_ids": [],
            "bridge_supported": False, "endpoints_supported": False,
            "independent_validation": False, "longitudinal_validation": False,
            "rationale_separation_passed": True}
        readiness = self.calculate(item)["decision"]["evidence_readiness"]
        self.assertEqual(readiness["missing_critical_inputs"], ["normalized_y5_operating_state"])
        self.assertEqual(readiness["status"], "UNPROVEN")
        self.assertEqual(readiness["assumption_critical_input_count"], 0)
        self.assertEqual(readiness["low_quality_critical_input_count"], 1)
        self.assertFalse(readiness["selection_uncertainty"])

    def test_missing_buy_support_uses_known_zero_exit_resilience_ceiling(self):
        item = record()
        item["inputs"]["buy_mult"] = missing()
        item["inputs"]["downside_exit_mult"] = proxy(0, 0, 0, state_id="d" * 64)
        result = self.calculate(item)
        self.assertIsNone(result["base"]["scores"]["P"])
        self.assertEqual(result["high"]["scores"]["P"], 0)
        self.assertEqual(result["high"]["subfactors"]["P"]["downside_exit_mult"], 0)
        self.assertEqual(result["high"]["subfactors"]["P"]["resilience_score"], 0)

        for exit_selection in (proxy(1, 0, 1, state_id="d" * 64),
                               missing()):
            item = record()
            item["inputs"]["buy_mult"] = missing()
            item["inputs"]["downside_exit_mult"] = exit_selection
            result = self.calculate(item)
            self.assertEqual(result["high"]["scores"]["P"], 10)

        item = record()
        item["inputs"]["buy_mult"] = selection(13)
        item["inputs"]["downside_exit_mult"] = missing()
        self.assertEqual(self.calculate(item)["high"]["scores"]["P"], 1)

    def test_p_entry_and_resilience_anchors(self):
        for buy, expected in ((4, 10), (6, 8), (8, 6), (10, 4), (12, 2), (14, 0)):
            item = record(); item["inputs"]["buy_mult"] = selection(buy)
            item["inputs"]["downside_exit_mult"] = proxy(buy, state_id="d" * 64)
            result = self.calculate(item)
            self.assertAlmostEqual(result["base"]["subfactors"]["P"]["entry_score"], expected)
        for ratio, expected in ((.5, 0), (.75, 5), (1, 10), (1.25, 10)):
            item = record(); item["inputs"]["downside_exit_mult"] = proxy(
                4 * ratio, state_id="d" * 64)
            self.assertAlmostEqual(self.calculate(item)["base"]["subfactors"]["P"]["resilience_score"], expected)

    def test_p_unchanged_by_c_and_survival(self):
        first = self.calculate(record())["base"]["scores"]["P"]
        item = record()
        for y in range(1, 6): item["inputs"]["commercial_retention"]["c%d" % y] = proxy(.1)
        item["inputs"]["operator_controlled_value_added_demand_share_y5"] = proxy(.3)
        self.assertEqual(self.calculate(item)["base"]["scores"]["P"], first)

    def test_constant_price_survival_boundaries(self):
        for value, expected in ((math.nextafter(.25, 0), "kill"), (.25, "pass"),
                                (math.nextafter(.5, 0), "pass"), (.5, "conditional"),
                                (math.nextafter(.75, 0), "conditional"), (.75, "hell_yes")):
            verdict, _ = scoring._survival_gate("hell_yes", value, self.t)
            self.assertEqual(verdict, expected)

    def test_unchanged_factor_cuts_and_floors(self):
        for sentinel in self.t["sentinels"]["factor_verdicts"]:
            scores = dict(zip(scoring.FACTOR_NAMES, sentinel["factors"]))
            self.assertEqual(scoring._raw_verdict(scoring.geometric_mean(scores.values()), scores, self.t),
                             sentinel["expected"])

    def test_cut_and_floor_epsilon_boundaries(self):
        cases = ((7.5, 6, "hell_yes"), (7.5, math.nextafter(6, 0), "strong"),
                 (6, 4, "strong"), (6, math.nextafter(4, 0), "conditional"),
                 (4.5, 2, "conditional"), (4.5, math.nextafter(2, 0), "pass"),
                 (3, 1, "pass"), (3, math.nextafter(1, 0), "kill"))
        for aggregate, minimum, expected in cases:
            scores = {name: 10 for name in scoring.FACTOR_NAMES}; scores["V"] = minimum
            self.assertEqual(scoring._raw_verdict(aggregate, scores, self.t), expected)

    def test_assumption_is_unproven_never_provisional(self):
        item = record(); item["inputs"]["buyer_access_win_share"] = selection(.5, state="ASSUMPTION")
        result = self.calculate(item)
        self.assertEqual(result["decision"]["evidence_readiness"]["status"], "UNPROVEN")
        self.assertEqual(result["decision"]["action"], "EVIDENCE_FIRST")

    def test_source_free_assumption_role_spec_scores_but_is_unproven(self):
        item = record(); mix = item["inputs"]["target_role_mix"]
        mix.update(spec_mode="assumption", basis_method="ESTIMATE",
                   basis_evidence_state="ASSUMPTION", basis_evidence_quality="NONE",
                   basis_source_ids=[], basis_bridge_supported=False,
                   basis_endpoints_supported=True, basis_independent_validation=False,
                   basis_longitudinal_validation=False)
        for role in mix["roles"]:
            role["removable_fraction"] = selection(.5, state="ASSUMPTION")
        result = self.calculate(item)
        self.assertIsNotNone(result["base"]["scores"]["V"])
        self.assertEqual(result["decision"]["evidence_readiness"]["status"], "UNPROVEN")

    def test_supported_unvalidated_forward_proxy_is_provisional(self):
        item = record(); item["inputs"]["buyer_access_win_share"] = proxy(.5, validated=False)
        result = self.calculate(item)
        self.assertEqual(result["decision"]["evidence_readiness"]["status"], "PROVISIONAL")

    def test_reused_vs_distinct_validation_sources_control_proxy_substantiation(self):
        reused = record(); reused["inputs"]["buyer_access_win_share"] = proxy(.5, validated=False)
        distinct = record(); distinct["inputs"]["buyer_access_win_share"] = proxy(.5, validated=True)
        self.assertEqual(self.calculate(reused)["decision"]["evidence_readiness"]["status"], "PROVISIONAL")
        self.assertEqual(self.calculate(distinct)["decision"]["evidence_readiness"]["status"], "SUBSTANTIATED")
        reused_state = record(); reused_state["inputs"]["normalized_y5_operating_state"] = state(validated=False)
        distinct_state = record(); distinct_state["inputs"]["normalized_y5_operating_state"] = state(validated=True)
        self.assertEqual(self.calculate(reused_state)["decision"]["evidence_readiness"]["status"], "PROVISIONAL")
        self.assertEqual(self.calculate(distinct_state)["decision"]["evidence_readiness"]["status"], "SUBSTANTIATED")

    def test_unsupported_endpoint_and_selection_uncertainty_are_unproven(self):
        item = record(); item["inputs"]["buyer_access_win_share"]["endpoints_supported"] = False
        self.assertEqual(self.calculate(item)["decision"]["evidence_readiness"]["status"], "UNPROVEN")
        item = record(); item["inputs"]["target_archetype"]["selection_uncertainty"] = True
        self.assertEqual(self.calculate(item)["decision"]["evidence_readiness"]["status"], "UNPROVEN")

    def test_fully_qualifying_stable_packet_is_substantiated(self):
        result = self.calculate(record())
        self.assertEqual(result["decision"]["evidence_readiness"]["status"], "SUBSTANTIATED")

    def test_evidence_labels_do_not_change_economics(self):
        direct = record(); proxy_item = record()
        # Current cash cost can be a fully supported proxy; only readiness changes.
        proxy_item["inputs"]["employee_cash_cost"] = proxy(30)
        a, b = self.calculate(direct), self.calculate(proxy_item)
        self.assertEqual({x: a[x] for x in scoring.BOUNDS}, {x: b[x] for x in scoring.BOUNDS})
        self.assertEqual(a["decision"]["economic_verdict"], b["decision"]["economic_verdict"])

    def test_missing_pivotal_input_is_indeterminate(self):
        item = record(); item["inputs"]["buyer_access_win_share"] = missing()
        result = self.calculate(item)
        self.assertIsNone(result["base"]["scores"]["B"])
        self.assertEqual(result["decision"]["economic_verdict"], "indeterminate")
        self.assertEqual(result["decision"]["action"], "EVIDENCE_FIRST")

    def test_strict_evidence_combinations(self):
        bad = []
        item = record(); item["inputs"]["buyer_access_win_share"]["source_ids"] = []; bad.append(item)
        item = record(); item["inputs"]["buy_mult"]["method"] = "ESTIMATE"; bad.append(item)
        item = record(); item["inputs"]["buy_mult"]["evidence_quality"] = "LOW"; bad.append(item)
        item = record(); item["inputs"]["buyer_access_win_share"]["bridge_supported"] = False; bad.append(item)
        for item in bad:
            with self.assertRaises(ValueError): self.calculate(item)

    def test_randomized_monotonicity(self):
        rng = random.Random(42002)
        for _ in range(250):
            base = record()
            access1, access2 = sorted((rng.random(), rng.random()))
            base["inputs"]["buyer_access_win_share"] = proxy(access1)
            low_b = self.calculate(base)["base"]["scores"]["B"]
            base["inputs"]["buyer_access_win_share"] = proxy(access2)
            high_b = self.calculate(base)["base"]["scores"]["B"]
            self.assertLessEqual(low_b, high_b)
            k1, k2 = sorted((rng.random(), rng.random()))
            base["inputs"]["implementation_investment"]["k0"] = proxy(k1)
            high_i = self.calculate(base)["base"]["scores"]["I"]
            base["inputs"]["implementation_investment"]["k0"] = proxy(k2)
            low_i = self.calculate(base)["base"]["scores"]["I"]
            self.assertGreaterEqual(high_i, low_i)

    def test_all_formula_primitive_directions(self):
        # Direct formula properties isolate every r/k/c coordinate.
        baseline_r, baseline_k, baseline_c = [.5] * 5, [.1] * 6, [.5] * 5
        base_i = scoring._implementation_score(baseline_r, baseline_k, self.t)
        base_c = scoring._commercial_score(baseline_r, baseline_c, self.t)
        base_h = scoring._h_value(baseline_r, baseline_k, baseline_c, self.t)
        for index in range(5):
            raised = list(baseline_r); raised[index] += .01
            self.assertGreaterEqual(scoring._implementation_score(raised, baseline_k, self.t), base_i)
            self.assertGreaterEqual(scoring._h_value(raised, baseline_k, baseline_c, self.t), base_h)
            captured = list(baseline_c); captured[index] += .01
            self.assertGreaterEqual(scoring._commercial_score(baseline_r, captured, self.t), base_c)
            self.assertGreaterEqual(scoring._h_value(baseline_r, baseline_k, captured, self.t), base_h)
        for index in range(6):
            raised = list(baseline_k); raised[index] += .01
            self.assertLessEqual(scoring._implementation_score(baseline_r, raised, self.t), base_i)
            self.assertLessEqual(scoring._h_value(baseline_r, raised, baseline_c, self.t), base_h)

        # End-to-end monotonic directions for V, B, and P.
        baseline = self.calculate(record())
        v0 = baseline["base"]["scores"]["V"]
        for path, replacement, direction in (
                ("employee_cash_cost", selection(35), "up"),
                ("controllable_contractor_cash_cost", selection(15), "up"),
                ("recognized_revenue", selection(120), "down")):
            item = record(); item["inputs"][path] = replacement
            actual = self.calculate(item)["base"]["scores"]["V"]
            self.assertGreaterEqual(actual, v0) if direction == "up" else self.assertLessEqual(actual, v0)
        b0 = baseline["base"]["scores"]["B"]
        for path in ("target_archetype_coverage", "five_year_sale_availability", "buyer_access_win_share"):
            item = record(); item["inputs"][path] = proxy(.25) if path != "target_archetype_coverage" else selection(.25)
            self.assertLessEqual(self.calculate(item)["base"]["scores"]["B"], b0)
        item = record(); item["dataset_inputs"]["n_band"] = selection(500)
        self.assertLessEqual(self.calculate(item)["base"]["scores"]["B"], b0)

    def test_randomized_valid_ranges_preserve_factor_s_h_order(self):
        rng = random.Random(42003)
        for _ in range(500):
            item = record()
            item["inputs"]["recognized_revenue"] = selection(100, 90, 120)
            item["inputs"]["third_party_pass_through"][0]["amount"] = selection(20, 10, 30)
            for name in ("employee_cash_cost", "controllable_contractor_cash_cost"):
                low = rng.uniform(0, 10); base = rng.uniform(low, 20); high = rng.uniform(base, 30)
                item["inputs"][name] = selection(base, low, high)
            for role in item["inputs"]["target_role_mix"]["roles"]:
                low, base, high = sorted(rng.random() for _x in range(3))
                role["removable_fraction"] = selection(base, low, high)
            ramp_base = sorted(rng.random() for _x in range(5))
            ramp_low = sorted(rng.uniform(0, x) for x in ramp_base)
            ramp_high = []
            previous = 0
            for base in ramp_base:
                previous = max(base, rng.uniform(previous, 1))
                ramp_high.append(previous)
            for index in range(5):
                item["inputs"]["implementation_realization"]["r%d" % (index + 1)] = proxy(
                    ramp_base[index], ramp_low[index], ramp_high[index])
            for year in range(6):
                low, base, high = sorted(rng.uniform(0, .3) for _x in range(3))
                item["inputs"]["implementation_investment"]["k%d" % year] = proxy(base, low, high)
            for year in range(1, 6):
                low, base, high = sorted(rng.random() for _x in range(3))
                item["inputs"]["commercial_retention"]["c%d" % year] = proxy(base, low, high)
            for name in ("target_archetype_coverage", "five_year_sale_availability",
                         "buyer_access_win_share", "operator_controlled_value_added_demand_share_y5"):
                low, base, high = sorted(rng.random() for _x in range(3))
                chosen = selection(base, low, high) if name == "target_archetype_coverage" else proxy(base, low, high)
                item["inputs"][name] = chosen
            low, base, high = sorted(rng.randint(0, 2000) for _x in range(3))
            item["dataset_inputs"]["n_band"] = selection(base, low, high)
            low, base, high = sorted(rng.uniform(.1, 15) for _x in range(3))
            item["inputs"]["buy_mult"] = selection(base, low, high)
            low, base, high = sorted(rng.uniform(0, 15) for _x in range(3))
            item["inputs"]["downside_exit_mult"] = proxy(
                base, low, high, state_id="d" * 64)
            result = self.calculate(item)
            for factor in scoring.FACTOR_NAMES:
                values = [result[b]["scores"][factor] for b in scoring.BOUNDS]
                self.assertLessEqual(values[0], values[1] + 1e-12)
                self.assertLessEqual(values[1], values[2] + 1e-12)
            scores = [result[b]["S"] for b in scoring.BOUNDS]
            self.assertLessEqual(scores[0], scores[1] + 1e-12)
            self.assertLessEqual(scores[1], scores[2] + 1e-12)
            h = [result[b]["subfactors"]["h"]["h"] for b in scoring.BOUNDS]
            self.assertLessEqual(h[0], h[1] + 1e-12)
            self.assertLessEqual(h[1], h[2] + 1e-12)


if __name__ == "__main__": unittest.main()
