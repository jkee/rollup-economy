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
REVIEW = os.path.join(REPO, "pipeline", "review", "541330.json")
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


class BuildHarness(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp(prefix="v3build_test_")
        self.addCleanup(shutil.rmtree, self.tmp)

    def make_tree(self, name, record=None, thresholds=None):
        """Isolated runs/review/out tree; returns kwargs for build.run_build."""
        root = os.path.join(self.tmp, name)
        runs = os.path.join(root, "runs", "541330")
        review = os.path.join(root, "review")
        out = os.path.join(root, "out")
        for d in (runs, review, out):
            os.makedirs(d)
        if record is None:
            with open(FIXTURE) as f:
                record = json.load(f)
        with open(os.path.join(runs, "2026-07-20_sonnet_tv3_fixture.json"), "w") as f:
            json.dump(record, f, indent=2)
        shutil.copy(REVIEW, os.path.join(review, "541330.json"))
        th_path = os.path.join(root, "thresholds.json")
        if thresholds is None:
            shutil.copy(THRESHOLDS, th_path)
        else:
            with open(th_path, "w") as f:
                json.dump(thresholds, f, indent=2)
        return dict(
            repo_root=root,
            runs_dir=os.path.join(root, "runs"),
            review_dir=review,
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


if __name__ == "__main__":
    unittest.main(verbosity=2)
