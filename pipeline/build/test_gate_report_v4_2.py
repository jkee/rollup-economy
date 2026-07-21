#!/usr/bin/env python3

import copy
import importlib.util
import json
from pathlib import Path
from types import SimpleNamespace
import shutil
import subprocess
import tempfile
import unittest


HERE = Path(__file__).resolve().parent


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec); spec.loader.exec_module(module)
    return module


gate = load("gate_report_v4_2_tests", HERE / "build_gate_report_v4_2.py")
fixtures = load("gate_report_scoring_fixtures", HERE / "test_v4_2_scoring.py")


class GateReportV42Tests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        for relative in (*gate.TOOLCHAIN_PATHS, "pipeline/build/thresholds_v4_2.json"):
            source = HERE.parent.parent / relative
            target = self.root / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, target)
        def passing_runner(command, **_kwargs):
            count = gate.EXPECTED_TESTS_RUN[command[-1]]
            return SimpleNamespace(
                returncode=0, stdout=b"",
                stderr=("Ran %s tests in 0.123s\n\nOK\n" % count).encode())
        self.runner = passing_runner

    def tearDown(self):
        self.temp.cleanup()

    def record(self, missing=False, missing_state=False):
        value = fixtures.record()
        if missing:
            value["inputs"]["recognized_revenue"] = fixtures.missing()
        if missing_state:
            value["inputs"]["normalized_y5_operating_state"] = {
                "state_id": None, "state_digest": None, "method": "ESTIMATE",
                "evidence_state": "MISSING", "evidence_quality": "NONE", "source_ids": [],
                "bridge_supported": False, "endpoints_supported": False,
                "independent_validation": False, "longitudinal_validation": False,
                "rationale_separation_passed": True,
            }
        value.update(fixtures.scoring.calculate(value))
        return value

    def write_records(self, missing_count, tamper=False):
        paths = []
        for index in range(5):
            value = self.record(index < missing_count)
            if tamper and index == 0:
                value["decision"]["evidence_readiness"]["missing_critical_inputs"] = []
            relative = "records/final-%s.json" % index
            path = self.root / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(json.dumps(value, sort_keys=True, separators=(",", ":")),
                            encoding="utf-8")
            paths.append(relative)
        return paths

    def test_exactly_one_critical_unbounded_record_passes(self):
        report = gate.build_report(
            self.root, "regression", self.write_records(1),
            timestamp="2026-01-01T00:00:00+00:00", runner=self.runner)
        self.assertTrue(report["passed"])
        self.assertEqual(report["critical_unbounded_count"], 1)
        flagged = [item for item in report["records"] if item["critical_unbounded"]]
        self.assertEqual(flagged[0]["critical_groups"], ["V"])
        self.assertEqual(gate.validate_report(self.root, report, runner=self.runner), report)

    def test_exactly_two_reject_and_tampered_summary_fails(self):
        report = gate.build_report(
            self.root, "holdout", self.write_records(2),
            timestamp="2026-01-01T00:00:00+00:00", runner=self.runner)
        self.assertFalse(report["passed"])
        self.assertEqual(report["critical_unbounded_count"], 2)
        with self.assertRaisesRegex(gate.GateReportError, "rejects certificate"):
            gate.validate_report(self.root, report, runner=self.runner)
        with self.assertRaisesRegex(gate.GateReportError, "differs from scorer"):
            gate.build_report(
                self.root, "regression", self.write_records(1, tamper=True),
                timestamp="2026-01-01T00:00:00+00:00", runner=self.runner)

    def test_unknown_missing_critical_path_fails_closed(self):
        with self.assertRaisesRegex(gate.GateReportError, "unknown"):
            gate.critical_group("unregistered.path")

    def test_two_missing_normalized_states_reject(self):
        paths = []
        for index in range(5):
            value = self.record(missing_state=index < 2)
            relative = "state-records/final-%s.json" % index
            path = self.root / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(json.dumps(value, sort_keys=True, separators=(",", ":")),
                            encoding="utf-8")
            paths.append(relative)
        report = gate.build_report(
            self.root, "regression", paths,
            timestamp="2026-01-01T00:00:00+00:00", runner=self.runner)
        self.assertEqual(report["critical_unbounded_count"], 2)
        self.assertFalse(report["passed"])
        self.assertEqual([item["critical_groups"] for item in report["records"][:2]],
                         [["P"], ["P"]])
        with self.assertRaisesRegex(gate.GateReportError, "rejects certificate"):
            gate.validate_report(self.root, report, runner=self.runner)

    def test_unittest_normalization_ignores_elapsed_time_but_binds_counts(self):
        first = gate.normalize_unittest_result(
            0, b"", b"Ran 17 tests in 0.101s\n\nOK (skipped=2)\n")
        second = gate.normalize_unittest_result(
            0, b"temporary /tmp/random/path\n",
            b"Ran 17 tests in 9.999s\n\nOK (skipped=2)\n")
        self.assertEqual(first, second)
        changed = gate.normalize_unittest_result(
            1, b"", b"Ran 17 tests in 0.2s\n\nFAILED (failures=1)\n")
        self.assertNotEqual(first, changed)
        spoofed = gate.normalize_unittest_result(
            1, b"Ran 17 tests in 0.1s\n\nOK\n",
            b"Ran 17 tests in 0.2s\n\nFAILED (failures=1)\n")
        self.assertEqual(spoofed["status"], "FAILED")
        skipped = gate.normalize_unittest_result(
            0, b"", b"Ran 17 tests in 0.2s\n\nOK (skipped=1)\n")
        self.assertEqual(skipped["skipped"], 1)
        def skipped_runner(command, **_kwargs):
            count = gate.EXPECTED_TESTS_RUN[command[-1]]
            return SimpleNamespace(
                returncode=0, stdout=b"spoofed OK\n",
                stderr=("Ran %s tests in 0.2s\n\nOK (skipped=1)\n" % count).encode())
        report = gate.build_report(
            self.root, "regression", self.write_records(0),
            timestamp="2026-01-01T00:00:00+00:00", runner=skipped_runner)
        self.assertFalse(report["passed"])

    def test_real_scoring_runner_normalizes_repeat_runs(self):
        command = ["python3", "-m", "unittest", "pipeline.build.test_v4_2_scoring"]
        results = []
        for _ in range(2):
            result = subprocess.run(command, cwd=HERE.parent.parent,
                                    stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                    check=False)
            results.append(gate.normalize_unittest_result(
                result.returncode, result.stdout, result.stderr))
        self.assertEqual(results[0], results[1])
        self.assertEqual(results[0]["status"], "OK")


if __name__ == "__main__":
    unittest.main()
