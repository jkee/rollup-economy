import math
import sys
import unittest
from decimal import Decimal
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import v4_3_minimal_scoring as scoring


class MinimalV43Tests(unittest.TestCase):
    def test_unknown_is_not_measured_low(self):
        unknown = {name: {"low": Decimal(2), "base": Decimal(5), "high": Decimal(8)} for name in scoring.FACTOR_NAMES}
        unknown["C"] = {"low": None, "base": None, "high": None}
        envelope = scoring.scenario_envelope(unknown)
        self.assertIsNone(envelope["base"])
        self.assertIn("C", envelope["missing_factors"])
        self.assertEqual(scoring.readiness_and_action(["MISSING"], envelope), ("STRESS_TEST_ONLY", "EVIDENCE_FIRST"))

        measured_low = {name: {"low": Decimal(0), "base": Decimal(0), "high": Decimal(0)} for name in scoring.FACTOR_NAMES}
        measured = scoring.scenario_envelope(measured_low)
        self.assertEqual(measured["base"]["tier"], "STRUCTURAL_OUT")

    def test_bounded_elicitation_for_c_and_d(self):
        self.assertLess(scoring.c_score("0.10"), scoring.c_score("0.25"))
        self.assertLess(scoring.d_score("0.7", "0.4"), scoring.d_score("1.0", "0.8"))
        self.assertEqual(scoring.c_score("0.50"), Decimal("10.000000000000"))
        self.assertEqual(scoring.d_score("1.2", "1"), Decimal("10.000000000000"))

    def test_h_and_f_have_empirical_anchors(self):
        self.assertGreater(scoring.h_score("0.4", "0.5", "0.5"), 0)
        self.assertGreater(scoring.f_score(100, "0.75", "0.20"), 0)
        self.assertEqual(scoring.f_score(0, "0.75", "0.20"), 0)

    def test_all_tiers_reachable(self):
        cases = {
            "HIGHEST_PRIORITY": Decimal("8"),
            "PRIORITY": Decimal("6.5"),
            "CONDITIONAL": Decimal("5"),
            "LOW_PRIORITY": Decimal("3.5"),
            "STRUCTURAL_OUT": Decimal("0.5"),
        }
        for expected, value in cases.items():
            result = scoring.aggregate({name: value for name in scoring.FACTOR_NAMES})
            self.assertEqual(result["tier"], expected)

    def test_deterministic_envelope_and_no_nonfinite(self):
        ranges = {name: {"low": Decimal(2), "base": Decimal(5), "high": Decimal(8)} for name in scoring.FACTOR_NAMES}
        first = scoring.json_decimal(scoring.scenario_envelope(ranges))
        second = scoring.json_decimal(scoring.scenario_envelope(ranges))
        self.assertEqual(first, second)
        self.assertEqual(first["state_count"], 81)
        for state in (first["base"], first["low"], first["high"]):
            self.assertTrue(math.isfinite(state["A"]))
            self.assertTrue(math.isfinite(state["L"]))


if __name__ == "__main__":
    unittest.main()
