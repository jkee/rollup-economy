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


normalizer = load_module("normalize_datasets_v4_1_tests", "normalize_datasets_v4_1.py")


class NormalizeDatasetsV41Tests(unittest.TestCase):
    def legacy(self, code):
        path = REPO / "pipeline" / "datasets" / "derived" / (code + ".json")
        return path, json.loads(path.read_text(encoding="utf-8"))

    def normalized(self, code):
        path, source = self.legacy(code)
        return normalizer.normalize(source, hashlib.sha256(path.read_bytes()).hexdigest())

    def test_maps_fields_basis_quality_vintage_and_exact_source_digest(self):
        path, source = self.legacy("541214")
        value = self.normalized("541214")
        self.assertEqual(value["dataset_version"], "4.1")
        self.assertEqual(value["snapshot_id"], "normalize-v4.1-1-541214")
        self.assertEqual(value["labor_share"]["basis"], source["labor_share"]["method"])
        self.assertEqual(value["n_total"]["basis"], source["n_total"]["source"])
        self.assertEqual(value["n_band"]["basis"], source["n_band"]["derivation"])
        self.assertEqual(value["n_band"]["quality"], "LOW")
        self.assertEqual(value["role_mix"]["basis"], source["role_mix"]["oews_level"])
        self.assertEqual(value["provenance"]["derivation_version"], "normalize-v4.1-1")
        self.assertEqual(
            value["provenance"]["source_manifest_sha256"],
            hashlib.sha256(path.read_bytes()).hexdigest(),
        )
        self.assertEqual(
            value["provenance"]["vintage"],
            source["labor_share"]["year"] + " | " + source["n_total"]["year"],
        )
        for legacy_role, role in zip(source["role_mix"]["occupations"], value["role_mix"]["occupations"]):
            self.assertEqual(role["employment_share"], legacy_role["emp_share"])
            self.assertNotIn("emp_share", role)

    def test_null_n_band_values_are_preserved_and_estimate_maps_to_low(self):
        for code in ("523940", "541120"):
            with self.subTest(code=code):
                _path, source = self.legacy(code)
                value = self.normalized(code)
                self.assertIsNone(source["n_band"]["value"])
                self.assertIsNone(value["n_band"]["value"])
                self.assertEqual(source["n_band"]["quality"], "ESTIMATE")
                self.assertEqual(value["n_band"]["quality"], "LOW")

    def test_impossible_legacy_labor_share_becomes_missing_not_clamped(self):
        _path, source = self.legacy("541618")
        value = self.normalized("541618")
        self.assertEqual(source["labor_share"]["value"], 1.3991)
        self.assertIsNone(value["labor_share"]["value"])
        self.assertEqual(value["labor_share"]["quality"], "NONE")
        self.assertEqual(value["labor_share"]["basis"], source["labor_share"]["method"])

    def test_541930_veterinary_role_identities_and_shares_are_not_relabelled(self):
        _path, source = self.legacy("541930")
        value = self.normalized("541930")
        legacy = [
            (item["soc"], item["title"], item["emp_share"], item["wage_share"])
            for item in source["role_mix"]["occupations"]
        ]
        normalized = [
            (item["soc"], item["title"], item["employment_share"], item["wage_share"])
            for item in value["role_mix"]["occupations"]
        ]
        self.assertEqual(normalized, legacy)
        self.assertEqual(normalized[0][0:2], ("29-2056", "Veterinary Technologists and Technicians"))
        self.assertEqual(normalized[1][0:2], ("31-9096", "Veterinary Assistants and Laboratory Animal Caretakers"))
        self.assertEqual(normalized[2][0:2], ("29-1131", "Veterinarians"))

    def test_builds_and_schema_validates_exactly_the_frozen_63_codes(self):
        records = normalizer.build_all()
        self.assertEqual(len(records), 63)
        self.assertEqual(list(records), [row["naics"] for row in json.loads(
            (REPO / "pipeline" / "blocks" / "targets_phase3.json").read_text(encoding="utf-8")
        )["codes"]])
        for value in records.values():
            self.assertIs(normalizer.validate_output(value), value)

    def test_write_and_check_are_byte_identical_and_do_not_modify_sources(self):
        source_paths = sorted((REPO / "pipeline" / "datasets" / "derived").glob("*.json"))
        before = {path: hashlib.sha256(path.read_bytes()).hexdigest() for path in source_paths}
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "v4_1"
            first = normalizer.run(output_dir=output)
            checked = normalizer.run(check=True, output_dir=output)
            self.assertEqual(first, checked)
            self.assertEqual(len(list(output.glob("*.json"))), 63)
            victim = output / "541214.json"
            victim.write_bytes(victim.read_bytes() + b" ")
            with self.assertRaisesRegex(normalizer.NormalizeError, "differs from fresh generation"):
                normalizer.run(check=True, output_dir=output)
        after = {path: hashlib.sha256(path.read_bytes()).hexdigest() for path in source_paths}
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
