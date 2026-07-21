#!/usr/bin/env python3

import copy
import importlib.util
import json
import os
import tempfile
import unittest
from unittest import mock


HERE = os.path.dirname(os.path.abspath(__file__))


def load_module(name, filename):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, filename))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


campaign = load_module("v4_campaign_tests", "campaign_v4.py")
fixtures = load_module("v4_campaign_fixtures", "test_v4_finalizer.py")


def write(path, value, binary=False):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if binary:
        with open(path, "wb") as handle:
            handle.write(value)
    else:
        with open(path, "w", encoding="utf-8") as handle:
            json.dump(value, handle, indent=2, ensure_ascii=False)
            handle.write("\n")


class V4CampaignTests(unittest.TestCase):
    def fixture(self, root):
        packet = fixtures.packet()
        dataset = fixtures.dataset()
        record, errors = campaign.finalizer.finalize(packet, dataset, "fleet")
        self.assertEqual(errors, [])
        code, run_id = packet["naics"], packet["run_meta"]["run_id"]
        paths = campaign._artifact_paths("fleet", code, run_id)
        absolute = {key: os.path.join(root, value) for key, value in paths.items()}
        write(absolute["packet_path"], packet)
        write(absolute["dataset_path"], dataset)
        write(absolute["record_path"], campaign.finalizer.serialize_record(record), binary=True)
        os.makedirs(os.path.dirname(absolute["memo_path"]), exist_ok=True)
        with open(absolute["memo_path"], "w", encoding="utf-8") as handle:
            handle.write(campaign.finalizer.render_memo(record))
        digests = {
            "packet_sha256": campaign.sha256(absolute["packet_path"]),
            "run_sha256": campaign.sha256(absolute["record_path"]),
            "memo_sha256": campaign.sha256(absolute["memo_path"]),
        }
        entry = {
            "kind": "fleet", "naics": code, "run_id": run_id, "attempt": 1,
            "required_research_model_id": "gpt-5.6-terra",
            "required_validator_model_id": "gpt-5.6-sol",
            "required_validator_prompt_version": "validator-4.0",
            **paths,
            "source_registry": [{
                "source_id": "S1", "url": "https://example.com/synthetic-v4", "score_driving": True,
            }],
            "artifact_digests": digests,
        }
        mechanics = {name: True for name in (
            "schema_valid", "identity_valid", "model_route_valid", "dataset_equal",
            "roles_equal", "finalization_equal", "memo_equal", "arithmetic_valid",
            "ranges_monotonic", "readiness_valid", "gates_valid",
        )}
        review = {
            "naics": code, "run_id": run_id, "artifact_digests": digests,
            "review_meta": {"model_id": "gpt-5.6-sol", "review_date": "2026-07-21", "prompt_version": "validator-4.0"},
            "outcome": "publishable", "mechanics": mechanics,
            "source_reviews": [{
                "source_id": "S1", "url": "https://example.com/synthetic-v4",
                "accessible": True, "score_driving": True, "support": "supported", "notes": "Synthetic support.",
            }],
            "input_reviews": [{
                "input_path": "scorecard.synthetic_%d" % index,
                "evidence_state_honest": True, "base_supported": True,
                "range_supported": True, "scope_supported": True, "notes": "Synthetic review.",
            } for index in range(7)],
            "findings": [], "publication_caveats": [], "summary": "All synthetic checks pass.",
        }
        write(absolute["review_path"], review)
        return entry, absolute

    def test_exact_artifacts_and_review_validate(self):
        with tempfile.TemporaryDirectory() as root:
            entry, _absolute = self.fixture(root)
            with mock.patch.object(campaign, "REPO", root):
                self.assertEqual(campaign.validate_entry(entry), [])

    def test_stale_artifact_digest_is_rejected(self):
        with tempfile.TemporaryDirectory() as root:
            entry, absolute = self.fixture(root)
            packet = campaign.load_json(absolute["packet_path"])
            packet["reviewer_note"] = "Artifact changed after the review manifest was frozen."
            write(absolute["packet_path"], packet)
            with mock.patch.object(campaign, "REPO", root):
                errors = campaign.validate_entry(entry)
            self.assertTrue(any("digests are stale" in item for item in errors))

    def test_latest_attempt_is_selected_deterministically(self):
        build = load_module("v4_build_selection_tests", "build_v4.py")
        first = {"kind": "fleet", "naics": "999999", "attempt": 1, "run_id": "r1"}
        second = copy.deepcopy(first)
        second.update({"attempt": 2, "run_id": "r2"})
        self.assertEqual(build._selected_entries({"entries": [second, first]}), [second])


if __name__ == "__main__":
    unittest.main()
