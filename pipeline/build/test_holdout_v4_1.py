#!/usr/bin/env python3

import hashlib
import importlib.util
import json
import os
import tempfile
import unittest


HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))


def load_selector():
    spec = importlib.util.spec_from_file_location(
        "select_holdout_v4_1_tests", os.path.join(HERE, "select_holdout_v4_1.py"))
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
    write(os.path.join(root, "V4_1_METHODOLOGY.md"), "# frozen\n")
    write(os.path.join(root, "pipeline/blocks/targets_phase3.json"), {
        "codes": [{"naics": code} for code in codes],
    })
    write(os.path.join(root, "pipeline/golden/golden_set.json"), {"codes": []})
    for index, code in enumerate(codes):
        write(os.path.join(root, "pipeline/datasets/derived/%s.json" % code), {
            "naics": code,
            "labor_share": {"value": (index + 1) / 100.0},
        })
    return temp


class HoldoutV41Tests(unittest.TestCase):
    def test_current_frozen_selection_is_exact_and_balanced(self):
        membership = selector.build_membership(REPO)
        self.assertEqual(
            membership["selected_codes"],
            ["541922", "541840", "541350", "541430", "541720"],
        )
        sizes = [len(item["candidates"]) for item in membership["bins"]]
        self.assertEqual(len(sizes), 5)
        self.assertLessEqual(max(sizes) - min(sizes), 1)
        ordered = membership["eligible_inputs"]
        self.assertEqual(
            [item["naics"] for item in ordered],
            sorted(
                [item["naics"] for item in ordered],
                key=lambda code: next((row["labor_share"], row["naics"])
                                      for row in ordered if row["naics"] == code),
            ),
        )

    def test_each_bin_winner_is_salted_minimum_hash(self):
        membership = selector.build_membership(REPO)
        for bin_ in membership["bins"]:
            hashes = [item["selection_hash"] for item in bin_["candidates"]]
            self.assertEqual(bin_["selected_hash"], min(hashes))
            self.assertEqual(
                bin_["selected_hash"],
                hashlib.sha256(
                    (selector.SALT + bin_["selected_naics"]).encode("utf-8")).hexdigest(),
            )

    def test_write_and_check_reproduce_byte_identically(self):
        codes = ["100001", "100002", "100003", "100004", "100005", "100006"]
        with fixture_root(codes) as root:
            self.assertEqual(selector.main(["--repo-root", root]), 0)
            output = os.path.join(root, selector.OUTPUT_PATH)
            with open(output, "rb") as handle:
                first = handle.read()
            self.assertEqual(selector.main(["--repo-root", root, "--check"]), 0)
            with open(output, "rb") as handle:
                self.assertEqual(first, handle.read())
            with open(output, "ab") as handle:
                handle.write(b"stale")
            self.assertEqual(selector.main(["--repo-root", root, "--check"]), 1)

    def test_preexisting_v41_result_is_excluded_without_reading_contents(self):
        codes = ["100001", "100002", "100003", "100004", "100005", "100006"]
        with fixture_root(codes) as root:
            path = os.path.join(root, "pipeline/v4_1/packets/100003/manual-result.json")
            write(path, "not json and never parsed")
            membership = selector.build_membership(root)
            self.assertEqual(membership["preexisting_v4_1_result_codes"], ["100003"])
            self.assertNotIn("100003", [item["naics"] for item in membership["eligible_inputs"]])

    def test_source_digests_cover_every_eligible_dataset(self):
        membership = selector.build_membership(REPO)
        paths = [item["path"] for item in membership["source_digests"]]
        self.assertEqual(paths, sorted(paths))
        for row in membership["eligible_inputs"]:
            self.assertIn(row["dataset"], membership["source_digests"])


if __name__ == "__main__":
    unittest.main()
