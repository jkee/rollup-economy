#!/usr/bin/env python3

import copy
import importlib.util
import json
import os
import unittest


HERE = os.path.dirname(os.path.abspath(__file__))


def load_module(name, filename):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, filename))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


finalizer = load_module("v4_finalizer_tests", "finalize_run_v4.py")


def selection(value, low, high, state="PROXY", method="ESTIMATE", quality="MED"):
    return {
        "value": value,
        "range": {"low": low, "high": high},
        "method": method,
        "evidence_state": state,
        "evidence_quality": quality,
        "confidence": "MED",
        "source_ids": ["S1"] if state in ("DIRECT", "PROXY") else [],
        "rationale": "Synthetic selection with enough explanation for deterministic tests.",
        "caveats": [],
    }


def text_selection(value):
    item = selection(0, 0, 0)
    item.pop("range")
    item["value"] = value
    return item


def dataset():
    return {
        "naics": "999999",
        "title": "Synthetic Services",
        "labor_share": {"value": 0.5, "method": "synthetic", "quality": "HIGH"},
        "role_mix": {
            "occupations": [
                {"soc": "11-0001", "title": "Synthetic role", "wage_share": 0.8}
            ],
            "quality": "HIGH"
        },
        "n_total": {"value": 2000, "source": "synthetic", "quality": "HIGH"},
        "n_band": {"value": 1000, "derivation": "synthetic", "quality": "HIGH"}
    }


def packet(model="gpt-5.6-terra"):
    long_text = "Synthetic narrative text long enough to satisfy the packet contract and test deterministic rendering behavior."
    return {
        "naics": "999999",
        "title": "Synthetic Services",
        "run_meta": {
            "model_id": model,
            "run_date": "2026-07-21",
            "run_id": "2026-07-21_synthetic_v4_999999",
            "template_version": "4.0",
            "prompt_version": "v4.0-target-archetype-1",
            "attempt": 1
        },
        "narrative": {name: long_text for name in (
            "executive_view", "target_archetype", "how_ai_changes_work", "value_capture",
            "adoption_timing", "buyability", "valuation", "operator_survival",
            "risks_and_uncertainty")},
        "sources": [{
            "id": "S1", "url": "https://example.com/synthetic-v4", "title": "Synthetic source",
            "access_date": "2026-07-21", "what_it_supports": "Synthetic score inputs only."
        }],
        "dataset_fallbacks": {},
        "scorecard": {
            "ai_replaceable_share": {
                "method": "ESTIMATE", "evidence_state": "PROXY", "evidence_quality": "MED",
                "confidence": "MED", "source_ids": ["S1"], "rationale": long_text, "caveats": [],
                "role_judgments": [
                    {"soc": "11-0001", "within_role_automatable_fraction": 0.5, "range": {"low": 0.3, "high": 0.7}, "rationale": long_text},
                    {"soc": "RESIDUAL", "within_role_automatable_fraction": 0.4, "range": {"low": 0.2, "high": 0.6}, "rationale": long_text}
                ]
            },
            "target_archetype": {
                "name": "Synthetic recurring operator",
                "inclusion_criteria": ["Recurring accountable service"],
                "exclusion_criteria": ["Pure product resale"],
                "selection_basis": long_text,
                "coverage": selection(0.6, 0.4, 0.8)
            },
            "retained_savings_share_24m": selection(0.55, 0.35, 0.7),
            "t50_years": selection(2.0, 1.0, 4.0),
            "current_adoption_pct": selection(0.4, 0.25, 0.49),
            "historical_analogs": text_selection("Prior workflow software adoption is the relevant analogy."),
            "seller_supply_signal": {
                **text_selection("NORMAL"),
                "plausible_values": ["NORMAL", "EXCESS"]
            },
            "active_consolidators": selection(4, 2, 8),
            "buy_mult": selection(6.0, 5.0, 7.0),
            "exit_mult": selection(7.5, 6.0, 9.0),
            "pricing_structure": text_selection("Recurring fixed-fee contracts with annual renewal."),
            "operator_survival": {
                **text_selection("DURABLE"),
                "plausible_values": ["DURABLE", "PRESSURED"]
            }
        },
        "cross_checks": {
            "uplift_vs_timing_consistent": long_text,
            "capture_vs_survival_separated": long_text,
            "no_deal_evidence_in_VA": long_text,
            "multiple_neutrality_acknowledged": long_text
        },
        "disclosures": {
            "dataset_mismatch": {"applies": False, "description": "", "sensitivity": []},
            "market_boundary": {"applies": False, "subsegments": [], "selection_basis": long_text}
        },
        "confidence_overall": "MED",
        "heterogeneous": False,
        "top_uncertain_inputs": [{"input": "retained_savings_share_24m", "range": "0.35-0.70", "score_impact": long_text}],
        "reviewer_note": ""
    }


class V4FinalizerTests(unittest.TestCase):
    def test_packet_schema_and_finalization(self):
        source = packet()
        schema = finalizer.load_json(os.path.join(HERE, "schemas", "research_packet_v4.schema.json"))
        self.assertEqual(finalizer.legacy_build.schema_errors(source, schema, schema), [])
        record, errors = finalizer.finalize(source, dataset(), "fleet")
        self.assertEqual(errors, [])
        self.assertEqual(record["run_meta"]["finalizer_version"], "finalizer-4.0")
        self.assertLessEqual(record["S"]["low"], record["S"]["base"])
        self.assertLessEqual(record["S"]["base"], record["S"]["high"])

    def test_finalization_and_memo_are_deterministic(self):
        first, errors = finalizer.finalize(packet(), dataset(), "fleet")
        self.assertEqual(errors, [])
        second, errors = finalizer.finalize(packet(), dataset(), "fleet")
        self.assertEqual(errors, [])
        self.assertEqual(finalizer.serialize_record(first), finalizer.serialize_record(second))
        self.assertEqual(finalizer.render_memo(first), finalizer.render_memo(second))

    def test_wrong_model_route_fails(self):
        record, errors = finalizer.finalize(packet(model="gpt-5.6-sol"), dataset(), "fleet")
        self.assertIsNone(record)
        self.assertTrue(any("model_id" in item for item in errors))

    def test_range_ordering_fails(self):
        source = packet()
        source["scorecard"]["buy_mult"]["range"] = {"low": 7.0, "high": 5.0}
        record, errors = finalizer.finalize(source, dataset(), "fleet")
        self.assertIsNone(record)
        self.assertTrue(any("low <= value <= high" in item for item in errors))

    def test_missing_is_not_disguised_numeric_value(self):
        source = packet()
        source["scorecard"]["exit_mult"].update({
            "value": 7.5, "range": {"low": 6.0, "high": 9.0}, "method": "ESTIMATE",
            "evidence_state": "MISSING", "evidence_quality": "NONE", "source_ids": []
        })
        record, errors = finalizer.finalize(source, dataset(), "fleet")
        self.assertIsNone(record)
        self.assertTrue(any("MISSING requires null value/range" in item for item in errors))

    def test_prior_artifact_is_not_a_v4_packet(self):
        source = packet()
        source["run_meta"]["template_version"] = "3.1.2"
        schema = finalizer.load_json(os.path.join(HERE, "schemas", "research_packet_v4.schema.json"))
        errors = finalizer.legacy_build.schema_errors(source, schema, schema)
        self.assertTrue(errors)

    def test_base_class_must_be_in_plausible_classes(self):
        source = packet()
        source["scorecard"]["operator_survival"]["plausible_values"] = ["PRESSURED"]
        record, errors = finalizer.finalize(source, dataset(), "fleet")
        self.assertIsNone(record)
        self.assertTrue(any("base value must appear" in item for item in errors))


if __name__ == "__main__":
    unittest.main()
