#!/usr/bin/env python3

import copy
import importlib.util
import os
import unittest


HERE = os.path.dirname(os.path.abspath(__file__))
SPEC = importlib.util.spec_from_file_location("v4_scoring_tests", os.path.join(HERE, "v4_scoring.py"))
scoring = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(scoring)


def selection(value, low=None, high=None, state="DIRECT", quality="MED"):
    return {
        "value": value,
        "range": {"low": value if low is None else low, "high": value if high is None else high},
        "method": "OBSERVED" if state == "DIRECT" else "ESTIMATE",
        "evidence_state": state,
        "evidence_quality": quality,
        "confidence": "MED",
        "source_ids": ["S1"] if state not in ("ASSUMPTION", "MISSING") else [],
        "rationale": "synthetic",
        "caveats": [],
    }


def record():
    return {
        "dataset_inputs": {
            "labor_share": {"value": 0.25},
            "n_band": {"value": 10000},
        },
        "inputs": {
            "ai_replaceable_share": {
                "evidence_state": "DIRECT",
                "evidence_quality": "MED",
                "breakdown_by_role": [{
                    "labor_share_of_total": 1.0,
                    "within_role_automatable_fraction": 1.0,
                    "range": {"low": 0.8, "high": 1.0},
                }]
            },
            "target_archetype": {"coverage": selection(1.0, 0.8, 1.0)},
            "retained_savings_share_24m": selection(0.8, 0.6, 0.9),
            "t50_years": selection(0.0, 0.0, 1.0),
            "seller_supply_signal": {
                **selection("NORMAL"),
                "plausible_values": ["NORMAL"],
            },
            "active_consolidators": selection(0, 0, 2),
            "buy_mult": selection(8.0, 7.0, 9.0),
            "exit_mult": selection(10.0, 9.0, 12.0),
            "operator_survival": {
                **selection("DURABLE"),
                "plausible_values": ["DURABLE"],
            },
        },
    }


class V4ScoringTests(unittest.TestCase):
    def setUp(self):
        self.thresholds = scoring.load_thresholds()

    def test_m_anchors_are_exact_and_flat_is_neutral(self):
        for spread, expected in self.thresholds["m_anchors"]:
            self.assertAlmostEqual(scoring.m_score(spread, self.thresholds["m_anchors"]), expected)
        self.assertEqual(scoring.m_score(0.0, self.thresholds["m_anchors"]), 5.0)

    def test_adoption_curve_semantic_anchors(self):
        for years, expected in ((0, 10), (1, 7.5), (3, 5), (6, 10 / 3), (9, 2.5)):
            self.assertAlmostEqual(scoring.adoption_score(years), expected)

    def test_hell_yes_is_reachable(self):
        result = scoring.calculate(record(), self.thresholds)
        self.assertEqual(result["decision"]["economic_verdict"], "hell_yes")
        self.assertEqual(result["decision"]["action"], "DEEP_DIVE")

    def test_every_verdict_tier_is_reachable(self):
        cases = []

        hell_yes = record()
        cases.append((hell_yes, "hell_yes"))

        strong = record()
        strong["dataset_inputs"]["n_band"]["value"] = 100
        strong["inputs"]["retained_savings_share_24m"] = selection(0.5)
        strong["inputs"]["t50_years"] = selection(3.0)
        strong["inputs"]["buy_mult"] = selection(8.0)
        strong["inputs"]["exit_mult"] = selection(8.0)
        cases.append((strong, "strong"))

        conditional = copy.deepcopy(strong)
        conditional["inputs"]["retained_savings_share_24m"] = selection(0.25)
        cases.append((conditional, "conditional"))

        pass_case = copy.deepcopy(strong)
        pass_case["dataset_inputs"]["n_band"]["value"] = 16
        pass_case["inputs"]["ai_replaceable_share"]["breakdown_by_role"][0].update({
            "within_role_automatable_fraction": 0.2,
            "range": {"low": 0.2, "high": 0.2},
        })
        pass_case["inputs"]["retained_savings_share_24m"] = selection(0.3)
        pass_case["inputs"]["t50_years"] = selection(6.0)
        cases.append((pass_case, "pass"))

        kill = copy.deepcopy(pass_case)
        kill["inputs"]["operator_survival"] = {
            **selection("MELTING"),
            "plausible_values": ["MELTING"],
        }
        cases.append((kill, "kill"))

        actual = [scoring.calculate(item, self.thresholds)["decision"]["economic_verdict"] for item, _ in cases]
        self.assertEqual(actual, [expected for _, expected in cases])

    def test_missing_multiple_evidence_is_neutral_but_unproven(self):
        item = record()
        item["inputs"]["buy_mult"] = selection(None, state="MISSING", quality="NONE")
        item["inputs"]["exit_mult"] = selection(None, state="MISSING", quality="NONE")
        result = scoring.calculate(item, self.thresholds)
        self.assertEqual(result["base"]["scores"]["M"], 5.0)
        self.assertEqual(result["low"]["scores"]["M"], 0.0)
        self.assertEqual(result["high"]["scores"]["M"], 10.0)
        self.assertEqual(result["decision"]["evidence_readiness"]["status"], "UNPROVEN")
        self.assertNotIn("direct_M_below_floor", result["decision"]["gate_reasons"])

    def test_missing_capture_is_neutral_but_unproven(self):
        item = record()
        item["inputs"]["retained_savings_share_24m"] = selection(None, state="MISSING", quality="NONE")
        result = scoring.calculate(item, self.thresholds)
        self.assertEqual(result["base"]["scores"]["C"], 5.0)
        self.assertEqual(result["low"]["scores"]["C"], 0.0)
        self.assertEqual(result["high"]["scores"]["C"], 10.0)
        self.assertEqual(result["decision"]["evidence_readiness"]["status"], "UNPROVEN")

    def test_direct_dead_capture_is_kill(self):
        item = record()
        item["inputs"]["retained_savings_share_24m"] = selection(0.05)
        result = scoring.calculate(item, self.thresholds)
        self.assertEqual(result["decision"]["economic_verdict"], "kill")
        self.assertIn("direct_C_below_floor", result["decision"]["gate_reasons"])

    def test_disintermediation_caps_at_pass(self):
        item = record()
        item["inputs"]["operator_survival"] = {
            **selection("DISINTERMEDIATED"),
            "plausible_values": ["DISINTERMEDIATED"],
        }
        result = scoring.calculate(item, self.thresholds)
        self.assertEqual(result["decision"]["raw_verdict"], "hell_yes")
        self.assertEqual(result["decision"]["economic_verdict"], "pass")
        self.assertEqual(result["decision"]["action"], "DEPRIORITIZE")

    def test_assumption_makes_result_provisional(self):
        item = record()
        item["inputs"]["active_consolidators"] = selection(5, 0, 20, state="ASSUMPTION", quality="NONE")
        result = scoring.calculate(item, self.thresholds)
        self.assertEqual(result["decision"]["evidence_readiness"]["status"], "PROVISIONAL")

    def test_operator_survival_assumption_makes_result_unproven(self):
        item = record()
        item["inputs"]["operator_survival"] = {
            **selection("DURABLE", state="ASSUMPTION", quality="NONE"),
            "plausible_values": ["PRESSURED", "DURABLE"],
        }
        result = scoring.calculate(item, self.thresholds)
        self.assertEqual(result["decision"]["evidence_readiness"]["status"], "UNPROVEN")

    def test_score_driving_ai_assumption_makes_result_provisional(self):
        item = record()
        item["inputs"]["ai_replaceable_share"].update({
            "evidence_state": "ASSUMPTION", "evidence_quality": "NONE",
        })
        result = scoring.calculate(item, self.thresholds)
        self.assertEqual(result["decision"]["evidence_readiness"]["status"], "PROVISIONAL")

    def test_plausible_survival_classes_drive_verdict_sensitivity(self):
        item = record()
        item["inputs"]["operator_survival"]["plausible_values"] = ["MELTING", "DURABLE"]
        result = scoring.calculate(item, self.thresholds)
        sensitivity = result["decision"]["sensitivity"]
        self.assertEqual(sensitivity["low_operator_survival"], "MELTING")
        self.assertEqual(sensitivity["high_operator_survival"], "DURABLE")
        self.assertEqual(sensitivity["low_verdict"], "kill")
        self.assertEqual(sensitivity["high_verdict"], "hell_yes")
        self.assertTrue(sensitivity["cross_tier"])

    def test_worse_inputs_do_not_improve_base_score(self):
        good = scoring.calculate(record(), self.thresholds)["base"]["S"]
        mutations = []
        for path, value in (
            (("retained_savings_share_24m",), selection(0.6, 0.6, 0.6)),
            (("t50_years",), selection(3.0, 3.0, 3.0)),
            (("target_archetype", "coverage"), selection(0.5, 0.5, 0.5)),
            (("active_consolidators",), selection(10, 10, 10)),
            (("exit_mult",), selection(8.0, 8.0, 8.0)),
        ):
            item = record()
            target = item["inputs"]
            for part in path[:-1]:
                target = target[part]
            target[path[-1]] = value
            mutations.append(scoring.calculate(item, self.thresholds)["base"]["S"])
        self.assertTrue(all(value <= good for value in mutations))


if __name__ == "__main__":
    unittest.main()
