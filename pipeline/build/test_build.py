#!/usr/bin/env python3
"""Regression tests for the v3 build (V3_PLAN.md 2.4). stdlib unittest only.

Run: python3 pipeline/build/test_build.py -v
"""

import importlib.util
import json
import math
import os
import shutil
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
FIXTURE = os.path.join(REPO, "pipeline", "runs", "541330", "2026-07-20_sonnet_tv3_fixture.json")
THRESHOLDS = os.path.join(HERE, "thresholds.json")
SCHEMAS = os.path.join(HERE, "schemas")
EXPECTATIONS = os.path.join(HERE, "deep_dive_expectations.json")

_spec = importlib.util.spec_from_file_location("build", os.path.join(HERE, "build.py"))
build = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(build)


def expected_fixture_scores():
    """Independent recompute of the 541330 fixture with the template-3.0 formulas."""
    V = 10 * min(1.0, (0.47 * 0.3785) / 0.25)
    C = 10 * 0.55 * 0.55
    A = min(10.0, 10.0 / 3.0)
    TD = min(1.0, math.log10(7000) / 4)
    OW = min(1.0, 0.9 + 0.1)  # clamp((0.45-0.10)/0.35, 0.1, 0.9)=0.9, +0.1 succession
    CFD = min(0.9, math.log10(31) / 2)
    B = 10 * math.sqrt(TD * OW) / (1 + 0.3 * CFD)
    M = min(10.0, max(0.0, 4 * (9.0 - 4.5) / 4.5))
    S = (V * C * A * B * M) ** 0.2
    return {"V": V, "C": C, "A": A, "B": B, "M": M, "S": S}


def fixture_review(run_id="2026-07-20_sonnet_tv3_fixture", verdict="accepted",
                   record=None, thresholds=None):
    if record is None:
        with open(FIXTURE) as f:
            record = json.load(f)
    if thresholds is None:
        with open(THRESHOLDS) as f:
            thresholds = json.load(f)
    computed, _arithmetic_errors, deltas = build.recompute(record)
    decision = build.decide(
        computed["S"],
        {name: computed[name] for name in "VCABM"},
        record["cross_checks"]["terminal_value"]["class"],
        record["confidence_overall"],
        thresholds,
    )
    flags = build.record_flags(record, computed, decision, deltas)
    passed = verdict == "accepted"
    reasons = [] if passed else ["Re-research the cited value and replace the unsupported input."]
    return {
        "naics": "541330",
        "run_id": run_id,
        "review_meta": {
            "model_id": "test-validator",
            "review_date": "2026-07-20",
            "prompt_version": "validator-test-v1",
        },
        "verdict": verdict,
        "checks": {
            name: {"pass": passed, "note": "Test fixture review note."}
            for name in [
                "sources_exist",
                "figures_match_sources",
                "judgment_inputs_plausible",
                "rubric_consistent",
                "cross_checks_honest",
            ]
        },
        "source_audits": [
            dict(
                pair,
                resolves=passed,
                claim_supported=passed,
                note="Test fixture source audit.",
            )
            for pair in build.source_audit_pairs(record)
        ],
        "reasons": reasons,
        "flags_reviewed": flags,
    }


class SchemaValidatorTests(unittest.TestCase):
    """Focused coverage for the shared stdlib JSON-Schema subset."""

    def validate_unique(self, value, enabled=True):
        schema = {"type": "array", "uniqueItems": enabled}
        return build.schema_errors(value, schema, schema)

    def test_unique_scalar_items_pass(self):
        self.assertEqual(
            self.validate_unique([None, True, False, 0, 1, "1", 2.5]),
            [],
        )

    def test_duplicate_scalar_reports_first_repeated_indexes(self):
        self.assertEqual(
            self.validate_unique(["alpha", "beta", "alpha", "beta"]),
            ["$: array items at indexes 0 and 2 are not unique"],
        )

    def test_json_booleans_are_distinct_from_numbers(self):
        self.assertEqual(self.validate_unique([True, 1, False, 0]), [])

    def test_mathematically_equal_json_numbers_are_duplicates(self):
        self.assertEqual(
            self.validate_unique([1, 1.0]),
            ["$: array items at indexes 0 and 1 are not unique"],
        )

    def test_structured_values_are_canonicalized_recursively(self):
        first = {"name": "x", "nested": {"a": 1, "b": [True, None]}}
        reordered = {"nested": {"b": [True, None], "a": 1.0}, "name": "x"}
        self.assertEqual(
            self.validate_unique([first, reordered]),
            ["$: array items at indexes 0 and 1 are not unique"],
        )

    def test_array_order_remains_significant(self):
        self.assertEqual(self.validate_unique([[1, 2], [2, 1]]), [])

    def test_unique_items_false_preserves_prior_behavior(self):
        self.assertEqual(self.validate_unique([{"x": 1}, {"x": 1}], enabled=False), [])


class BuildHarness(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp(prefix="v3build_test_")
        self.addCleanup(shutil.rmtree, self.tmp)

    def make_tree(self, name, record=None, thresholds=None, review=None):
        """Isolated runs/review/out tree; returns kwargs for build.run_build."""
        root = os.path.join(self.tmp, name)
        runs = os.path.join(root, "runs", "541330")
        review_dir = os.path.join(root, "review")
        out = os.path.join(root, "out")
        for d in (runs, review_dir, out):
            os.makedirs(d)
        if record is None:
            with open(FIXTURE) as f:
                record = json.load(f)
        with open(os.path.join(runs, "2026-07-20_sonnet_tv3_fixture.json"), "w") as f:
            json.dump(record, f, indent=2)
        if review is None:
            review = fixture_review(
                record["run_meta"]["run_id"], record=record,
                thresholds=thresholds,
            )
        review_naics_dir = os.path.join(review_dir, review["naics"])
        os.makedirs(review_naics_dir)
        with open(os.path.join(review_naics_dir, record["run_meta"]["run_id"] + ".json"), "w") as f:
            json.dump(review, f, indent=2)
        th_path = os.path.join(root, "thresholds.json")
        if thresholds is None:
            shutil.copy(THRESHOLDS, th_path)
        else:
            with open(th_path, "w") as f:
                json.dump(thresholds, f, indent=2)
        return dict(
            repo_root=root,
            runs_dir=os.path.join(root, "runs"),
            review_dir=review_dir,
            thresholds_path=th_path,
            schemas_dir=SCHEMAS,
            expectations_path=EXPECTATIONS,
            site_out=os.path.join(out, "six_data_v3.json"),
            stats_out=os.path.join(out, "stats.json"),
            flags_out=os.path.join(out, "flags.json"),
            reconciliation_out=os.path.join(out, "reconciliation.md"),
        )

    def test_fixture_passes(self):
        """The 541330 fixture builds clean; scores and verdict match an independent recompute."""
        cfg = self.make_tree("pass")
        result = build.run_build(**cfg)
        self.assertTrue(result["ok"], "build failed: %s" % result.get("errors"))
        with open(cfg["site_out"]) as f:
            site = json.load(f)
        self.assertEqual(len(site["records"]), 1)
        rec = site["records"][0]
        exp = expected_fixture_scores()
        self.assertEqual(rec["naics"], "541330")
        self.assertEqual(rec["verdict"], "conditional")
        self.assertEqual(rec["acceptance"]["status"], "accepted")
        self.assertFalse(rec["borderline"])
        self.assertFalse(rec["gate_blocked"])
        self.assertAlmostEqual(rec["S"], exp["S"], places=9)
        self.assertAlmostEqual(rec["S"], 4.70248066342042, places=9)
        for f_ in ["V", "C", "A", "B", "M"]:
            self.assertAlmostEqual(rec["scores"][f_], exp[f_], places=9)

    def test_corrupted_arithmetic_fails(self):
        """Perturbing one stored score by 0.05 fails the build, naming the mismatch."""
        with open(FIXTURE) as f:
            record = json.load(f)
        record["scores"]["V"]["score"] += 0.05
        cfg = self.make_tree("corrupt", record=record)
        result = build.run_build(**cfg)
        self.assertFalse(result["ok"])
        msg = "\n".join(result["errors"])
        self.assertIn("541330", msg)
        self.assertIn("V stored=", msg)
        self.assertIn("recomputed=", msg)
        # nothing published on failure
        self.assertFalse(os.path.exists(cfg["site_out"]))

    def test_threshold_coupling(self):
        """Changing a cut in thresholds.json changes the verdict — nothing is hardcoded."""
        cfg = self.make_tree("base")
        base = build.run_build(**cfg)
        self.assertTrue(base["ok"])
        with open(cfg["site_out"]) as f:
            base_verdict = json.load(f)["records"][0]["verdict"]

        with open(THRESHOLDS) as f:
            th = json.load(f)
        th["verdict_cuts"]["strong"] = 4.5  # below the fixture's S ≈ 4.70
        cfg2 = self.make_tree("moved_cut", thresholds=th)
        moved = build.run_build(**cfg2)
        self.assertTrue(moved["ok"])
        with open(cfg2["site_out"]) as f:
            moved_verdict = json.load(f)["records"][0]["verdict"]

        self.assertEqual(base_verdict, "conditional")
        self.assertEqual(moved_verdict, "strong")
        self.assertNotEqual(base_verdict, moved_verdict)

    def test_determinism(self):
        """Two consecutive builds produce byte-identical outputs."""
        cfg1 = self.make_tree("det1")
        cfg2 = self.make_tree("det2")
        self.assertTrue(build.run_build(**cfg1)["ok"])
        self.assertTrue(build.run_build(**cfg2)["ok"])
        for key in ["site_out", "stats_out", "flags_out", "reconciliation_out"]:
            with open(cfg1[key], "rb") as f1, open(cfg2[key], "rb") as f2:
                self.assertEqual(f1.read(), f2.read(),
                                 "output %s not byte-identical across builds" % key)

    def test_review_must_match_exact_run_id(self):
        """A review at the exact path with a different embedded run_id is invalid."""
        review = fixture_review("different-run-id")
        cfg = self.make_tree("review_run_mismatch", review=review)
        result = build.run_build(**cfg)
        self.assertFalse(result["ok"])
        self.assertIn("does not match current run_id", "\n".join(result["errors"]))

    def test_same_naics_multiple_reviews_selects_exact_run(self):
        """Sibling reviews for the same NAICS do not override the exact-run review."""
        cfg = self.make_tree("multiple_reviews")
        sibling = fixture_review("older-run", verdict="wrong")
        sibling_path = os.path.join(cfg["review_dir"], "541330", "older-run.json")
        with open(sibling_path, "w") as f:
            json.dump(sibling, f, indent=2)
        result = build.run_build(**cfg)
        self.assertTrue(result["ok"], result.get("errors"))
        self.assertEqual(result["site"]["records"][0]["acceptance"]["status"], "accepted")
        self.assertEqual(
            result["site"]["records"][0]["acceptance"]["review"]["run_id"],
            "2026-07-20_sonnet_tv3_fixture",
        )

    def test_attempt_two_wins_even_when_attempt_one_run_id_sorts_later(self):
        runs_dir = os.path.join(self.tmp, "attempt_selection", "621210")
        os.makedirs(runs_dir)
        fixtures = [
            ("2026-07-21_gpt-5.6-terra_v312rf1_621210", 1),
            ("2026-07-21_gpt-5.6-terra_v312r2_621210", 2),
        ]
        for run_id, attempt in fixtures:
            with open(os.path.join(runs_dir, run_id + ".json"), "w") as handle:
                json.dump({
                    "run_meta": {
                        "template_version": "3.1.2",
                        "run_date": "2026-07-21",
                        "run_id": run_id,
                        "attempt": attempt,
                    }
                }, handle)
        records, legacy = build.discover_runs(os.path.dirname(runs_dir))
        self.assertEqual([], legacy)
        self.assertEqual(fixtures[1][0], records["621210"][1]["run_meta"]["run_id"])

    def test_accepted_review_with_failed_check_is_invalid(self):
        """An accepted verdict cannot conceal a failed validator check."""
        review = fixture_review()
        review["checks"]["figures_match_sources"]["pass"] = False
        cfg = self.make_tree("accepted_failed_check", review=review)
        result = build.run_build(**cfg)
        self.assertFalse(result["ok"])
        self.assertIn(
            "$.checks.figures_match_sources.pass: False != const True",
            "\n".join(result["errors"]),
        )

    def test_accepted_review_with_failed_source_audit_is_invalid(self):
        """Every source audit must resolve and support its claim before acceptance."""
        review = fixture_review()
        review["source_audits"][0]["claim_supported"] = False
        cfg = self.make_tree("accepted_failed_source", review=review)
        result = build.run_build(**cfg)
        self.assertFalse(result["ok"])
        self.assertIn(
            "$.source_audits[0].claim_supported: False != const True",
            "\n".join(result["errors"]),
        )

    def test_accepted_review_with_incomplete_source_coverage_is_invalid(self):
        """An accepted review cannot omit a citation found in the run record."""
        review = fixture_review()
        review["source_audits"].pop()
        cfg = self.make_tree("accepted_incomplete_sources", review=review)
        result = build.run_build(**cfg)
        self.assertFalse(result["ok"])
        self.assertIn("source_audits coverage mismatch", "\n".join(result["errors"]))

    def test_accepted_review_with_incomplete_flag_coverage_is_invalid(self):
        """An accepted review must address every deterministic Stage-4 flag."""
        with open(FIXTURE) as f:
            record = json.load(f)
        record["confidence_overall"] = "LOW"
        review = fixture_review(record=record)
        review["flags_reviewed"] = []
        cfg = self.make_tree("accepted_incomplete_flags", record=record, review=review)
        result = build.run_build(**cfg)
        self.assertFalse(result["ok"])
        self.assertIn("flags_reviewed coverage mismatch", "\n".join(result["errors"]))

    def test_wrong_review_may_have_no_source_audits(self):
        """A no-citation record can be rejected without fabricating an audit entry."""
        review = fixture_review(verdict="wrong")
        review["source_audits"] = []
        with open(os.path.join(SCHEMAS, "review_record.schema.json")) as f:
            schema = json.load(f)
        self.assertEqual(build.schema_errors(review, schema, schema), [])

    def test_accepted_review_requires_source_audit(self):
        """Acceptance requires positive evidence from at least one audited source."""
        review = fixture_review()
        review["source_audits"] = []
        cfg = self.make_tree("accepted_no_sources", review=review)
        result = build.run_build(**cfg)
        self.assertFalse(result["ok"])
        self.assertIn("$.source_audits: fewer than minItems 1", "\n".join(result["errors"]))


class VerdictEngine(unittest.TestCase):
    """decide() paths the single fixture cannot reach: gates, caps, floor."""

    @classmethod
    def setUpClass(cls):
        with open(THRESHOLDS) as f:
            cls.th = json.load(f)

    def decide(self, S, factors, terminal="DURABLE", confidence="HIGH"):
        return build.decide(S, factors, terminal, confidence, self.th)

    def test_hell_yes_when_all_gates_pass(self):
        f = {k: 7.5 for k in "VCABM"}
        self.assertEqual(self.decide(7.5, f)["verdict"], "hell_yes")

    def test_gate_blocked_downgrades_to_strong(self):
        f = dict({k: 8.0 for k in "VCABM"}, M=5.5)  # below the 6.0 factor gate
        r = self.decide(7.5, f)
        self.assertEqual(r["verdict"], "strong")
        self.assertTrue(r["gate_blocked"])

    def test_melting_caps_at_pass(self):
        f = {k: 6.5 for k in "VCABM"}
        r = self.decide(6.0, f, terminal="MELTING")
        self.assertEqual(r["verdict"], "pass")
        self.assertIn("terminal_value:MELTING", r["capped_by"])

    def test_low_confidence_caps_at_conditional(self):
        f = {k: 6.5 for k in "VCABM"}
        r = self.decide(6.0, f, confidence="LOW")
        self.assertEqual(r["verdict"], "conditional")

    def test_factor_floor_kills(self):
        f = dict({k: 7.0 for k in "VCABM"}, M=0.5)  # below the 1.0 kill floor
        self.assertEqual(self.decide(5.0, f)["verdict"], "kill")

    def test_borderline_flag_near_cut(self):
        f = {k: 5.0 for k in "VCABM"}
        cut = self.th["verdict_cuts"]["strong"]
        eps = self.th["borderline_epsilon"]
        self.assertTrue(self.decide(cut - eps / 2, f)["borderline"])
        self.assertFalse(self.decide(cut - 3 * eps, f)["borderline"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
