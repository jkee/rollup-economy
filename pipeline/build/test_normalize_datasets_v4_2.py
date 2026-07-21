#!/usr/bin/env python3

import hashlib
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest


HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent


def load_module(name, filename):
    spec = importlib.util.spec_from_file_location(name, HERE / filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


normalizer = load_module("normalize_datasets_v4_2_tests", "normalize_datasets_v4_2.py")


class NormalizeDatasetsV42Tests(unittest.TestCase):
    def legacy(self, code):
        path = REPO / "pipeline" / "datasets" / "derived" / (code + ".json")
        return path, json.loads(path.read_text(encoding="utf-8"))

    def normalized(self, code):
        path, source = self.legacy(code)
        return normalizer.normalize(source, hashlib.sha256(path.read_bytes()).hexdigest())

    def test_maps_only_deterministic_industry_inputs_and_exact_provenance(self):
        path, source = self.legacy("541214")
        value = self.normalized("541214")
        self.assertEqual(value["dataset_version"], "4.2")
        self.assertEqual(value["snapshot_id"], "normalize-v4.2-1-541214")
        self.assertEqual(value["labor_share"]["basis"], source["labor_share"]["method"])
        self.assertEqual(value["n_total"]["basis"], source["n_total"]["source"])
        self.assertEqual(value["n_band"]["basis"], source["n_band"]["derivation"])
        self.assertEqual(value["n_band"]["quality"], "LOW")
        self.assertEqual(value["role_mix"]["basis"], source["role_mix"]["oews_level"])
        self.assertEqual(value["provenance"]["derivation_version"], "normalize-v4.2-1")
        self.assertEqual(
            value["provenance"]["source_manifest_sha256"],
            hashlib.sha256(path.read_bytes()).hexdigest(),
        )
        self.assertEqual(
            value["provenance"]["vintage"],
            source["labor_share"]["year"] + " | " + source["n_total"]["year"],
        )
        self.assertEqual(
            set(value),
            {
                "dataset_version", "snapshot_id", "naics", "title", "labor_share",
                "n_total", "n_band", "role_mix", "provenance",
            },
        )
        serialized = json.dumps(value).lower()
        for forbidden in (
            "recognized_revenue", "pass_through", "r_cva", "controllable_value_added",
            "employee_cash_cost", "contractor_cash_cost",
        ):
            self.assertNotIn(forbidden, serialized)

    def test_null_band_values_are_preserved_and_forced_to_none_quality(self):
        for code in ("523940", "541120"):
            with self.subTest(code=code):
                _path, source = self.legacy(code)
                value = self.normalized(code)
                self.assertIsNone(source["n_band"]["value"])
                self.assertIsNone(value["n_band"]["value"])
                self.assertEqual(value["n_band"]["quality"], "NONE")

    def test_impossible_legacy_labor_share_becomes_null_none_not_clamped(self):
        _path, source = self.legacy("541618")
        value = self.normalized("541618")
        self.assertEqual(source["labor_share"]["value"], 1.3991)
        self.assertIsNone(value["labor_share"]["value"])
        self.assertEqual(value["labor_share"]["quality"], "NONE")
        self.assertEqual(value["labor_share"]["basis"], source["labor_share"]["method"])

    def test_null_values_with_non_none_quality_fail_closed(self):
        value = self.normalized("541120")
        value["n_band"]["quality"] = "LOW"
        with self.assertRaisesRegex(normalizer.NormalizeError, "quality"):
            normalizer.validate_output(value)

    def test_541930_role_identities_and_shares_are_copied_exactly(self):
        _path, source = self.legacy("541930")
        value = self.normalized("541930")
        legacy_roles = [
            (item["soc"], item["title"], item["emp_share"], item["wage_share"])
            for item in source["role_mix"]["occupations"]
        ]
        normalized_roles = [
            (item["soc"], item["title"], item["employment_share"], item["wage_share"])
            for item in value["role_mix"]["occupations"]
        ]
        self.assertEqual(normalized_roles, legacy_roles)

    def test_builds_and_schema_validates_exactly_the_frozen_63_codes(self):
        records = normalizer.build_all()
        targets = json.loads(
            (REPO / "pipeline" / "blocks" / "targets_phase3.json").read_text(encoding="utf-8")
        )["codes"]
        self.assertEqual(len(records), 63)
        self.assertEqual(list(records), [row["naics"] for row in targets])
        for value in records.values():
            self.assertIs(normalizer.validate_output(value), value)

    def test_write_check_are_byte_identical_and_preserve_legacy_and_v4_1(self):
        protected_paths = sorted(
            (REPO / "pipeline" / "datasets" / "derived").glob("*.json")
        ) + sorted(
            (REPO / "pipeline" / "datasets" / "v4_1").glob("*.json")
        )
        before = {path: hashlib.sha256(path.read_bytes()).hexdigest() for path in protected_paths}
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "v4_2"
            first = normalizer.run(output_dir=output)
            checked = normalizer.run(check=True, output_dir=output)
            self.assertEqual(first, checked)
            self.assertEqual(len(list(output.glob("*.json"))), 63)
            victim = output / "541214.json"
            victim.write_bytes(victim.read_bytes() + b" ")
            with self.assertRaisesRegex(normalizer.NormalizeError, "differs from fresh generation"):
                normalizer.run(check=True, output_dir=output)
        after = {path: hashlib.sha256(path.read_bytes()).hexdigest() for path in protected_paths}
        self.assertEqual(after, before)

    def test_rejects_relabelled_membership_identity(self):
        path, source = self.legacy("541930")
        changed = json.loads(json.dumps(source))
        changed["title"] = "Veterinary Services"
        with self.assertRaisesRegex(normalizer.NormalizeError, "differs from target membership"):
            normalizer.normalize(
                changed,
                hashlib.sha256(path.read_bytes()).hexdigest(),
                expected_code="541930",
                expected_title="Translation and Interpretation Services",
            )


if __name__ == "__main__":
    unittest.main()
