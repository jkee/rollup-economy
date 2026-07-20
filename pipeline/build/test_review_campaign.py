#!/usr/bin/env python3
"""Focused tests for the deterministic Stage-5 review campaign tooling."""

import copy
import importlib.util
import json
import os
import shutil
import tempfile
import unittest
from unittest import mock


HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
_spec = importlib.util.spec_from_file_location(
    "review_campaign", os.path.join(HERE, "review_campaign.py")
)
campaign = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(campaign)


LOOSE_SCHEMA = {
    "type": "object",
    "required": [
        "naics", "run_id", "review_meta", "verdict", "checks", "reasons",
        "flags_reviewed", "source_audits",
    ],
    "properties": {
        "naics": {"type": "string"},
        "run_id": {"type": "string"},
        "review_meta": {"type": "object"},
        "verdict": {"enum": ["accepted", "wrong"]},
        "checks": {"type": "object"},
        "reasons": {"type": "array"},
        "flags_reviewed": {"type": "array"},
        "source_audits": {"type": "array"},
    },
}


class ProductionManifest(unittest.TestCase):
    def test_exact_current_campaign_is_deterministic(self):
        first = campaign.build_manifest(REPO)
        second = campaign.build_manifest(REPO)
        self.assertEqual(first, second)
        self.assertEqual(
            first["counts"], {"fleet": 63, "golden": 20, "total": 83}
        )
        self.assertEqual(len(first["records"]), 83)
        identities = [
            (entry["kind"], entry["naics"], entry["run_id"])
            for entry in first["records"]
        ]
        self.assertEqual(len(identities), len(set(identities)))
        self.assertEqual(identities[:63], sorted(identities[:63]))
        self.assertEqual(identities[63:], sorted(identities[63:]))
        for entry in first["records"]:
            for dependency in ("record_path", "prompt_path", "dataset_path"):
                self.assertTrue(
                    os.path.isfile(os.path.join(REPO, entry[dependency])),
                    "%s missing for %s" % (dependency, entry["run_id"]),
                )
            pairs = [
                (audit["input_path"], audit["url"])
                for audit in entry["expected_source_audits"]
            ]
            self.assertEqual(pairs, sorted(set(pairs)))

    def test_embedded_and_dedicated_urls_are_both_found(self):
        record = {
            "dataset_inputs": {
                "derived": "See https://dataset.example.com/derivation."
            },
            "inputs": {
                "research": {
                    "url": "https://example.com/report",
                    "figure_quoted": "See https://example.org/finding.",
                },
                "judgment": {
                    "sources": [
                        "Study (https://example.net/study?q=1).",
                        "https://example.com/report",
                    ]
                },
            }
        }
        self.assertEqual(campaign.source_audit_pairs(record), [
            {
                "input_path": "dataset_inputs.derived",
                "url": "https://dataset.example.com/derivation",
            },
            {
                "input_path": "inputs.judgment.sources[0]",
                "url": "https://example.net/study?q=1",
            },
            {
                "input_path": "inputs.judgment.sources[1]",
                "url": "https://example.com/report",
            },
            {
                "input_path": "inputs.research.figure_quoted",
                "url": "https://example.org/finding",
            },
            {
                "input_path": "inputs.research.url",
                "url": "https://example.com/report",
            },
        ])

    def test_membership_mismatch_names_missing_and_unexpected_codes(self):
        with self.assertRaisesRegex(
            ValueError,
            r"missing=\['123456'\].*unexpected=\['654321'\]",
        ):
            campaign.assert_exact_membership(
                {"111111", "654321"},
                {"111111", "123456"},
                "test records",
            )

    def test_manifest_membership_matches_declared_sources(self):
        manifest = campaign.build_manifest(REPO)
        fleet = {
            entry["naics"] for entry in manifest["records"]
            if entry["kind"] == "fleet"
        }
        golden = {
            entry["naics"] for entry in manifest["records"]
            if entry["kind"] == "golden"
        }
        self.assertEqual(
            fleet,
            campaign._declared_codes(
                os.path.join(REPO, "pipeline", "blocks",
                             "targets_phase3.json"),
                "fleet target list",
            ),
        )
        self.assertEqual(
            golden,
            campaign._declared_codes(
                os.path.join(REPO, "pipeline", "golden",
                             "golden_set.json"),
                "golden set",
            ),
        )


class ReviewValidation(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp(prefix="review_campaign_test_")
        self.addCleanup(shutil.rmtree, self.tmp)
        self.review_dir = os.path.join(self.tmp, "reviews")
        os.makedirs(os.path.join(self.review_dir, "123456"))
        self.schema_path = os.path.join(self.tmp, "schema.json")
        self.manifest_path = os.path.join(self.tmp, "manifest.json")
        with open(self.schema_path, "w", encoding="utf-8") as f:
            json.dump(LOOSE_SCHEMA, f)
        self.entry = {
            "kind": "fleet",
            "naics": "123456",
            "run_id": "fleet-s1-123456",
            "record_path": "record.json",
            "prompt_path": "prompt.md",
            "dataset_path": "dataset.json",
            "review_path": "unused/by-test.json",
            "stage4_flags": ["LOW_CONFIDENCE"],
            "expected_source_audits": [
                {"input_path": "inputs.metric.url",
                 "url": "https://example.com/source"}
            ],
        }
        with open(self.manifest_path, "w", encoding="utf-8") as f:
            json.dump({
                "manifest_version": "review-campaign-1",
                "counts": {"fleet": 1, "golden": 0, "total": 1},
                "records": [self.entry],
            }, f)
        self.review_path = os.path.join(
            self.review_dir, "123456", "fleet-s1-123456.json"
        )
        self.review = {
            "naics": "123456",
            "run_id": "fleet-s1-123456",
            "review_meta": {"model_id": "Sol", "review_date": "2026-07-20"},
            "verdict": "accepted",
            "checks": {
                name: {"pass": True, "note": "Checked independently."}
                for name in campaign.CHECK_NAMES
            },
            "reasons": [],
            "flags_reviewed": [
                {"flag": "LOW_CONFIDENCE", "note": "Addressed."}
            ],
            "source_audits": [{
                "input_path": "inputs.metric.url",
                "url": "https://example.com/source",
                "resolves": True,
                "claim_supported": True,
                "note": "Figure appears in source.",
            }],
        }

    def run_validation(self):
        return campaign.validate_campaign(
            repo_root=self.tmp,
            manifest_path=self.manifest_path,
            review_dir=self.review_dir,
            schema_path=self.schema_path,
            check_freshness=False,
        )

    def write_review(self, review=None):
        with open(self.review_path, "w", encoding="utf-8") as f:
            json.dump(review or self.review, f)

    def test_missing_and_valid_accepted_counts(self):
        missing = self.run_validation()
        self.assertEqual(
            missing["counts"],
            {"missing": 1, "accepted": 0, "wrong": 0, "invalid": 0},
        )
        self.write_review()
        accepted = self.run_validation()
        self.assertEqual(
            accepted["counts"],
            {"missing": 0, "accepted": 1, "wrong": 0, "invalid": 0},
        )
        self.assertEqual(accepted["errors"], [])

    def test_incomplete_source_coverage_is_invalid(self):
        review = copy.deepcopy(self.review)
        review["source_audits"] = []
        self.write_review(review)
        result = self.run_validation()
        self.assertEqual(result["counts"]["invalid"], 1)
        self.assertIn("missing source audits", "\n".join(result["errors"]))

    def test_wrong_requires_reason_and_observed_failure(self):
        review = copy.deepcopy(self.review)
        review["verdict"] = "wrong"
        review["reasons"] = ["The cited figure is not present at the URL."]
        self.write_review(review)
        result = self.run_validation()
        self.assertEqual(result["counts"]["invalid"], 1)
        self.assertIn("at least one failed", "\n".join(result["errors"]))

        review["checks"]["figures_match_sources"]["pass"] = False
        review["source_audits"][0]["claim_supported"] = False
        self.write_review(review)
        result = self.run_validation()
        self.assertEqual(
            result["counts"],
            {"missing": 0, "accepted": 0, "wrong": 1, "invalid": 0},
        )

    def test_identity_and_flag_mismatch_are_invalid(self):
        review = copy.deepcopy(self.review)
        review["run_id"] = "stale-run"
        review["flags_reviewed"] = []
        self.write_review(review)
        result = self.run_validation()
        self.assertEqual(result["counts"]["invalid"], 1)
        message = "\n".join(result["errors"])
        self.assertIn("run_id", message)
        self.assertIn("flags_reviewed mismatch", message)

    def test_cli_missing_reviews_fail_unless_explicitly_allowed(self):
        incomplete = {
            "counts": {
                "missing": 1, "accepted": 0, "wrong": 0, "invalid": 0,
            },
            "errors": [],
        }
        with mock.patch.object(
            campaign, "validate_campaign", return_value=incomplete
        ):
            self.assertEqual(campaign.main(["validate"]), 1)
            self.assertEqual(
                campaign.main(["validate", "--allow-missing"]), 0
            )


if __name__ == "__main__":
    unittest.main()
