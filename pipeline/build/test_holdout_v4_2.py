#!/usr/bin/env python3

import hashlib
import importlib.util
import io
import json
import os
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout


HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))


def load_selector():
    spec = importlib.util.spec_from_file_location(
        "select_holdout_v4_2_tests", os.path.join(HERE, "select_holdout_v4_2.py"))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


selector = load_selector()


def write(path, value):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        if isinstance(value, str):
            handle.write(value)
        else:
            json.dump(value, handle)


def fixture_root(codes):
    temp = tempfile.TemporaryDirectory()
    root = temp.name
    write(os.path.join(root, "V4_2_METHODOLOGY.md"), "# frozen v4.2\n")
    write(os.path.join(root, "pipeline/blocks/targets_phase3.json"), {
        "codes": [{"naics": code} for code in codes],
    })
    write(os.path.join(root, "pipeline/golden/golden_set.json"), {"codes": []})
    for index, code in enumerate(codes):
        legacy_path = os.path.join(root, "pipeline/datasets/derived/%s.json" % code)
        write(legacy_path, {
            "naics": code,
            "labor_share": {"value": (index + 1) / 100.0},
        })
        with open(legacy_path, "rb") as handle:
            legacy_sha = hashlib.sha256(handle.read()).hexdigest()
        write(os.path.join(root, "pipeline/datasets/v4_1/%s.json" % code), {
            "dataset_version": "4.1",
            "snapshot_id": "fixture-%s" % code,
            "naics": code,
            "labor_share": {"value": (index + 1) / 100.0, "quality": "MED", "basis": "fixture"},
            "provenance": {
                "derivation_version": "fixture-v1",
                "source_manifest_sha256": legacy_sha,
            },
        })
    return temp


class HoldoutV42Tests(unittest.TestCase):
    def test_v42_control_artifacts_match_methodology_contract(self):
        def load(relative):
            with open(os.path.join(REPO, relative), "r", encoding="utf-8") as handle:
                return json.load(handle)

        regression = load("pipeline/v4_2/regression_membership.json")
        self.assertEqual(regression["membership_version"], "v4.2-regression-1")
        self.assertEqual(regression["selected_codes"], sorted(selector.DEVELOPMENT_CODES))

        routes = load("pipeline/v4_2/model_routes.json")
        self.assertEqual(routes["route_version"], "v4.2-neutral-model-routes-1")
        self.assertEqual(routes["research"], {"target": "gpt-5.6-terra"})
        self.assertEqual(routes["review"], {"all": "gpt-5.6-sol"})

        control = load("pipeline/v4_2/change_control.json")
        self.assertEqual(control["change_control_version"], "v4.2-change-control-1")
        self.assertEqual(control["evidence_infeasibility_rule"]["critical_unbounded_count"], 2)
        self.assertEqual(control["evidence_infeasibility_rule"]["set_size"], 5)
        self.assertIn("named_distribution", control["forbidden_triggers"])
        self.assertEqual(
            control["replacement_version_rule"],
            "new_salt_and_untouched_holdout_required",
        )

    def test_current_frozen_selection_is_exact_and_balanced(self):
        membership = selector.build_membership(REPO)
        self.assertEqual(
            membership["selected_codes"],
            ["541890", "541340", "541370", "541199", "541420"],
        )
        self.assertEqual([len(item["candidates"]) for item in membership["bins"]], [9, 8, 8, 8, 8])
        self.assertEqual(len(membership["eligible_inputs"]), 41)
        ordered = membership["eligible_inputs"]
        anomalous = next(item for item in ordered if item["naics"] == "541618")
        self.assertEqual(anomalous["labor_share"], 1.3991)
        self.assertIsNone(anomalous["normalization_boundary"]["normalized_labor_share"])
        self.assertEqual(
            [(item["labor_share"], item["naics"]) for item in ordered],
            sorted((item["labor_share"], item["naics"]) for item in ordered),
        )

        relative_repo = os.path.relpath(REPO, os.getcwd())
        self.assertEqual(
            selector.build_membership(relative_repo)["selected_codes"],
            list(selector.EXPECTED_SELECTED_CODES),
        )

    def test_each_bin_winner_is_new_salted_minimum_hash(self):
        membership = selector.build_membership(REPO)
        self.assertEqual(membership["selection"]["salt"], selector.SALT)
        self.assertNotEqual(selector.SALT, "rollup-v4.1-holdout-2026-07-21|")
        for bin_ in membership["bins"]:
            hashes = [item["selection_hash"] for item in bin_["candidates"]]
            self.assertEqual(bin_["selected_hash"], min(hashes))
            self.assertEqual(
                bin_["selected_hash"],
                hashlib.sha256((selector.SALT + bin_["selected_naics"]).encode("utf-8")).hexdigest(),
            )

    def test_write_and_check_are_byte_identical_without_touching_v41(self):
        codes = ["100001", "100002", "100003", "100004", "100005", "100006"]
        with fixture_root(codes) as root:
            v41 = os.path.join(root, "pipeline/v4_1/holdout_membership.json")
            write(v41, "v4.1 sentinel\n")
            with open(v41, "rb") as handle:
                before = handle.read()
            captured = io.StringIO()
            with redirect_stdout(captured), redirect_stderr(captured):
                self.assertEqual(selector.main(["--repo-root", root]), 0)
            output = os.path.join(root, selector.OUTPUT_PATH)
            with open(output, "rb") as handle:
                first = handle.read()
            with redirect_stdout(captured), redirect_stderr(captured):
                self.assertEqual(selector.main(["--repo-root", root, "--check"]), 0)
            with open(output, "rb") as handle:
                self.assertEqual(first, handle.read())
            with open(v41, "rb") as handle:
                self.assertEqual(before, handle.read())
            with open(output, "ab") as handle:
                handle.write(b"stale")
            with redirect_stdout(captured), redirect_stderr(captured):
                self.assertEqual(selector.main(["--repo-root", root, "--check"]), 1)

    def test_prior_and_prefreeze_outputs_are_excluded_without_parsing(self):
        codes = [
            "100001", "100002", "100003", "100004", "100005",
            "100006", "100007", "100008", "100009",
        ]
        with fixture_root(codes) as root:
            write(os.path.join(root, "pipeline/v4/packets/100002/result.json"), "not json")
            write(os.path.join(root, "pipeline/v4_1/reviews/100003/result.json"), "not json")
            write(os.path.join(root, "pipeline/v4_2/memos/100004/result.md"), "not json")
            membership = selector.build_membership(root)
            exclusions = membership["exclusions"]
            self.assertEqual(exclusions["generated_prior_economic_output_codes"]["v4_0"], ["100002"])
            self.assertEqual(exclusions["generated_prior_economic_output_codes"]["v4_1"], ["100003"])
            self.assertEqual(exclusions["prefreeze_v4_2_result_codes"], ["100004"])
            eligible = {item["naics"] for item in membership["eligible_inputs"]}
            self.assertTrue({"100002", "100003", "100004"}.isdisjoint(eligible))

    def test_opaque_output_id_digit_substrings_are_not_naics(self):
        self.assertIsNone(selector._code_from_path(
            "pipeline/v4_2/runs/v42_d77baefe700494d3c4279f43_a1.json"
        ))
        self.assertEqual("541512", selector._code_from_path(
            "pipeline/v4/runs/541512/2026-07-21_canary.json"
        ))

    def test_normalization_boundary_binds_legacy_bytes_and_allows_normalized_null(self):
        codes = ["100001", "100002", "100003", "100004", "100005", "100006"]
        with fixture_root(codes) as root:
            membership = selector.build_membership(root)
            first = membership["eligible_inputs"][0]
            self.assertIsNotNone(first["labor_share"])
            self.assertEqual(first["normalization_boundary"]["dataset_version"], "4.1")
            self.assertEqual(
                first["normalization_boundary"]["source_manifest_sha256"],
                first["legacy_selection_input"]["sha256"],
            )
            normalized = os.path.join(root, "pipeline/datasets/v4_1/100001.json")
            with open(normalized, "r", encoding="utf-8") as handle:
                value = json.load(handle)
            value["provenance"]["source_manifest_sha256"] = "0" * 64
            write(normalized, value)
            with self.assertRaisesRegex(ValueError, "does not bind legacy"):
                selector.build_membership(root)

            # Restore provenance, then prove the normalized value itself is
            # also part of the fail-closed translation boundary.
            with open(normalized, "r", encoding="utf-8") as handle:
                value = json.load(handle)
            value["provenance"]["source_manifest_sha256"] = first["legacy_selection_input"]["sha256"]
            value["labor_share"]["value"] = 0.99
            write(normalized, value)
            with self.assertRaisesRegex(ValueError, "translation mismatch"):
                selector.build_membership(root)

    def test_current_exclusions_are_materialized_without_v41_economic_outputs(self):
        membership = selector.build_membership(REPO)
        exclusions = membership["exclusions"]
        self.assertEqual(exclusions["disclosed_development_codes"], sorted(selector.DEVELOPMENT_CODES))
        self.assertEqual(exclusions["generated_prior_economic_output_codes"]["v4_0"], sorted(selector.DEVELOPMENT_CODES))
        self.assertEqual(exclusions["generated_prior_economic_output_codes"]["v4_1"], [])
        self.assertEqual(exclusions["prefreeze_v4_2_result_codes"], [])

    def test_source_digests_cover_both_sides_of_normalization_boundary(self):
        membership = selector.build_membership(REPO)
        paths = [item["path"] for item in membership["source_digests"]]
        self.assertEqual(paths, sorted(paths))
        for row in membership["eligible_inputs"]:
            self.assertIn(row["legacy_selection_input"], membership["source_digests"])
            self.assertIn(row["normalized_dataset"], membership["source_digests"])


if __name__ == "__main__":
    unittest.main()
