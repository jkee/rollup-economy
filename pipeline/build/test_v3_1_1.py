#!/usr/bin/env python3
"""Synthetic tests for the non-prompt v3.1.1 evidence boundary.

These tests do not read, write or rerun a production industry record.
"""

import copy
import importlib.util
import json
import math
import os
import shutil
import tempfile
import unittest


HERE = os.path.dirname(os.path.abspath(__file__))
SCHEMAS = os.path.join(HERE, "schemas")


def load_module(name, filename):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, filename))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


build = load_module("build_v311_tests", "build.py")
finalizer = load_module("finalizer_v311_tests", "finalize_run_v3_1_1.py")
contract = load_module("contract_v311_tests", "evidence_contract_v3_1_1.py")
campaign = load_module("campaign_v311_tests", "review_campaign.py")


def fact(fact_id, quote):
    return {
        "id": fact_id,
        "url": "https://example.com/%s" % fact_id.lower(),
        "title": "Synthetic source %s" % fact_id,
        "quote": quote,
        "access_date": "2026-07-21",
        "scope": {
            "population": "Synthetic target-industry firms",
            "geography": "United States",
            "unit": "share of firms",
            "period": "2026",
            "industry_mismatch": "none",
        },
    }


def estimate(value):
    return {
        "value": value,
        "method": "ESTIMATE",
        "evidence_quality": "NONE",
        "fact_ids": [],
        "rationale": "Synthetic bounded judgment.",
        "plausible_range": "Synthetic bounded range.",
        "estimate_basis": {
            "starting_fact_ids": [],
            "scope_mismatches": ["none; no source fact is used"],
            "bridge_steps": ["Use the stated synthetic fixture assumptions."],
            "judgment_step": "Select the bounded synthetic value by explicit judgment.",
        },
    }


def observed(value, fact_id):
    return {
        "value": value,
        "method": "OBSERVED",
        "evidence_quality": "HIGH",
        "fact_ids": [fact_id],
        "rationale": "The selected value repeats the cited source value.",
        "plausible_range": "Exact synthetic observation.",
        "observed_value": value,
    }


def calculated(value, fact_id):
    return {
        "value": value,
        "method": "CALCULATED",
        "evidence_quality": "HIGH",
        "fact_ids": [fact_id],
        "rationale": "Safe arithmetic over one fact-backed operand.",
        "plausible_range": "Exact synthetic calculation.",
        "calculation": {
            "expression": "years",
            "operands": [{"name": "years", "value": value, "fact_id": fact_id}],
        },
    }


def dataset():
    return {
        "naics": "999999",
        "title": "Synthetic Industry",
        "labor_share": {
            "value": 0.5,
            "method": "Synthetic deterministic method",
            "quality": "HIGH",
        },
        "role_mix": {
            "oews_level": "synthetic",
            "occupations": [
                {
                    "soc": "11-1111",
                    "title": "Synthetic Managers",
                    "emp_share": 0.6,
                    "wage_share": 0.6,
                },
                {
                    "soc": "22-2222",
                    "title": "Synthetic Specialists",
                    "emp_share": 0.3,
                    "wage_share": 0.3,
                },
            ],
            "quality": "HIGH",
        },
        "n_total": {
            "value": 1000,
            "source": "Synthetic deterministic source",
            "quality": "HIGH",
        },
        "n_band": {
            "value": 100,
            "derivation": "Synthetic deterministic chain",
            "quality": "HIGH",
        },
    }


def draft():
    owner = estimate(0.3)
    return {
        "naics": "999999",
        "title": "Synthetic Industry",
        "run_meta": {
            "model_id": "gpt-5.6-terra",
            "run_date": "2026-07-21",
            "run_id": "synthetic-v311-s1-999999",
            "template_version": "3.1.1",
            "prompt_version": "synthetic-v3.1.1-prompt",
        },
        "evidence_facts": [
            fact("F1", "Thirty percent of firms report material use."),
            fact("F2", "The transition takes four years."),
        ],
        "dataset_fallbacks": {},
        "inputs": {
            "ai_replaceable_share": {
                "role_judgments": [
                    {
                        "soc": "11-1111",
                        "within_role_automatable_fraction": 0.2,
                        "rationale": "Synthetic management-task judgment.",
                        "plausible_range": "0.1-0.3",
                    },
                    {
                        "soc": "22-2222",
                        "within_role_automatable_fraction": 0.6,
                        "rationale": "Synthetic specialist-task judgment.",
                        "plausible_range": "0.5-0.7",
                    },
                    {
                        "soc": "RESIDUAL",
                        "within_role_automatable_fraction": 0.4,
                        "rationale": "Synthetic residual-task judgment.",
                        "plausible_range": "0.3-0.5",
                    },
                ],
                "evidence_quality": "NONE",
                "fact_ids": [],
                "estimate_basis": {
                    "starting_fact_ids": [],
                    "scope_mismatches": ["none; no source fact is used"],
                    "bridge_steps": ["Judge each supplied role's task mix."],
                    "judgment_step": "Select each bounded role fraction by explicit judgment.",
                },
            },
            "pi_dist": estimate(0.5),
            "pi_moat": estimate(0.5),
            "t50_years": calculated(4.0, "F2"),
            "current_adoption_pct": observed(0.3, "F1"),
            "historical_analogs": estimate("Synthetic gradual analog"),
            "owners_60plus_pct": {
                "selection": owner,
                "succession_shortage_documented": estimate(False),
            },
            "active_consolidators": estimate(2),
            "buy_mult": estimate(4.0),
            "exit_mult": estimate(8.0),
            "pricing_structure": estimate("Synthetic fixed-fee structure"),
        },
        "cross_checks": {
            "uplift_vs_A_consistent": "Synthetic consistency explanation.",
            "terminal_value": {
                "class": "DURABLE",
                "justification": "Synthetic paid demand survives.",
            },
            "no_proxy_confirmed": "Synthetic V/A exclude deal evidence.",
            "pricing_model_deflation": "Synthetic repricing maps into capture.",
        },
        "disclosures": {
            "dataset_mismatch": {
                "applies": False,
                "description": "",
                "sensitivity": [],
            },
            "market_boundary": {
                "applies": False,
                "subsegments": [],
                "dominant_subsegment": "",
                "selection_basis": "",
            },
        },
        "confidence_overall": "LOW",
        "heterogeneous": False,
        "top_uncertain_inputs": [
            {
                "input": "t50_years",
                "plausible_range": "2-6 years",
                "score_impact": "Synthetic sensitivity description.",
            }
        ],
        "reviewer_note": "Synthetic fixture; not a production record.",
    }


class V311BoundaryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open(os.path.join(SCHEMAS, "research_draft_v3_1_1.schema.json")) as f:
            cls.draft_schema = json.load(f)
        with open(os.path.join(SCHEMAS, "run_record_v3_1_1.schema.json")) as f:
            cls.run_schema = json.load(f)

    def schema_errors(self, value):
        return build.schema_errors(value, self.draft_schema, self.draft_schema)

    def build_record(self, record):
        root = tempfile.mkdtemp(prefix="v311_build_test_")
        self.addCleanup(shutil.rmtree, root)
        runs = os.path.join(root, "runs", "999999")
        reviews = os.path.join(root, "reviews")
        output = os.path.join(root, "output")
        os.makedirs(runs)
        os.makedirs(reviews)
        os.makedirs(output)
        with open(os.path.join(runs, "synthetic.json"), "w") as handle:
            json.dump(record, handle)
        return build.run_build(
            repo_root=root,
            allow_unreviewed=True,
            runs_dir=os.path.join(root, "runs"),
            review_dir=reviews,
            thresholds_path=os.path.join(HERE, "thresholds.json"),
            schemas_dir=SCHEMAS,
            expectations_path=os.path.join(root, "missing-expectations.json"),
            site_out=os.path.join(output, "site.json"),
            stats_out=os.path.join(output, "stats.json"),
            flags_out=os.path.join(output, "flags.json"),
            reconciliation_out=os.path.join(output, "reconciliation.md"),
        )

    def test_valid_draft_finalizes_and_builds(self):
        source = draft()
        self.assertEqual(self.schema_errors(source), [])
        record, errors = finalizer.finalize(source, dataset())
        self.assertEqual(errors, [])
        self.assertEqual(
            build.schema_errors(record, self.run_schema, self.run_schema), []
        )
        self.assertEqual(record["inputs"]["current_adoption_pct"]["provenance_type"], "DIRECT")
        self.assertEqual(record["inputs"]["t50_years"]["provenance_type"], "DERIVED")
        self.assertEqual(record["inputs"]["pi_dist"]["provenance_type"], "ESTIMATE")
        self.assertEqual(contract.final_record_semantic_errors(record), [])
        result = self.build_record(record)
        self.assertTrue(result["ok"], result.get("errors"))

    def test_ellipsis_quote_is_rejected(self):
        source = draft()
        source["evidence_facts"][0]["quote"] = "Thirty percent ... report use."
        self.assertIn("ellipses are forbidden", "\n".join(contract.semantic_errors(source)))
        source["evidence_facts"][0]["quote"] = "Thirty percent . . . report use."
        self.assertIn("ellipses are forbidden", "\n".join(contract.semantic_errors(source)))
        source["evidence_facts"][0]["quote"] = "Thirty percent … report use."
        self.assertIn("ellipses are forbidden", "\n".join(contract.semantic_errors(source)))

    def test_exact_research_model_ids_are_fail_closed(self):
        source = draft()
        source["run_meta"]["model_id"] = "Terra"
        self.assertIn("not one of", "\n".join(self.schema_errors(source)))
        source["run_meta"]["model_id"] = "gpt-5.6-sol"
        self.assertEqual(self.schema_errors(source), [])

    def test_estimate_basis_requires_complete_structured_bridge(self):
        source = draft()
        del source["inputs"]["pi_dist"]["estimate_basis"]["judgment_step"]
        self.assertIn(
            "missing required key 'judgment_step'",
            "\n".join(self.schema_errors(source)),
        )
        source = draft()
        source["inputs"]["pi_dist"]["fact_ids"] = ["F1"]
        source["inputs"]["pi_dist"]["evidence_quality"] = "MED"
        self.assertIn(
            "starting_fact_ids must match fact_ids exactly",
            "\n".join(contract.semantic_errors(source)),
        )

    def test_succession_shortage_is_a_fact_bound_selection(self):
        source = draft()
        shortage = source["inputs"]["owners_60plus_pct"][
            "succession_shortage_documented"
        ]
        shortage["value"] = True
        self.assertIn(
            "value=true requires OBSERVED",
            "\n".join(contract.semantic_errors(source)),
        )

        source = draft()
        source["inputs"]["owners_60plus_pct"][
            "succession_shortage_documented"
        ] = observed(True, "F1")
        record, errors = finalizer.finalize(source, dataset())
        self.assertEqual(errors, [])
        finalized = record["inputs"]["owners_60plus_pct"][
            "succession_shortage_documented"
        ]
        self.assertEqual(finalized["method"], "OBSERVED")
        self.assertEqual(finalized["provenance_type"], "DIRECT")

    def test_missing_geography_is_rejected_by_schema(self):
        source = draft()
        del source["evidence_facts"][0]["scope"]["geography"]
        self.assertIn("missing required key 'geography'", "\n".join(self.schema_errors(source)))
        record, errors = finalizer.finalize(source, dataset())
        self.assertIsNone(record)
        self.assertIn("missing required key 'geography'", "\n".join(errors))

    def test_calculated_requires_reproducible_value(self):
        source = draft()
        source["inputs"]["t50_years"]["value"] = 5.0
        errors = contract.semantic_errors(source)
        self.assertIn("does not equal formula result", "\n".join(errors))

    def test_unsafe_calculation_is_rejected(self):
        source = draft()
        source["inputs"]["t50_years"]["calculation"]["expression"] = "years ** 2"
        self.assertIn("only operand names", "\n".join(contract.semantic_errors(source)))

    def test_calculation_cannot_hide_behind_unused_fact_operand(self):
        source = draft()
        source["inputs"]["t50_years"]["calculation"]["expression"] = "4"
        self.assertIn("must reference at least one operand", "\n".join(contract.semantic_errors(source)))

    def test_nonfinite_numbers_are_not_schema_numbers(self):
        source = draft()
        source["inputs"]["pi_dist"]["value"] = math.nan
        self.assertIn("expected type number", "\n".join(self.schema_errors(source)))

    def test_impossible_dates_are_rejected(self):
        source = draft()
        source["evidence_facts"][0]["access_date"] = "2026-02-30"
        self.assertIn("must be a real ISO date", "\n".join(contract.semantic_errors(source)))

    def test_observed_requires_exact_repetition(self):
        source = draft()
        source["inputs"]["current_adoption_pct"]["observed_value"] = 0.31
        self.assertIn("must equal observed_value exactly", "\n".join(contract.semantic_errors(source)))

    def test_unknown_fact_and_quality_mismatch_are_rejected(self):
        source = draft()
        source["inputs"]["buy_mult"]["fact_ids"] = ["F99"]
        source["inputs"]["buy_mult"]["evidence_quality"] = "MED"
        errors = "\n".join(contract.semantic_errors(source))
        self.assertIn("unknown facts", errors)
        source["inputs"]["buy_mult"]["fact_ids"] = []
        self.assertIn("empty fact_ids requires evidence_quality NONE", "\n".join(contract.semantic_errors(source)))

    def test_heterogeneous_record_requires_structured_boundary(self):
        source = draft()
        source["heterogeneous"] = True
        self.assertIn("heterogeneous=true requires", "\n".join(contract.semantic_errors(source)))

    def test_build_independently_rejects_altered_provenance(self):
        record, errors = finalizer.finalize(draft(), dataset())
        self.assertEqual(errors, [])
        record["inputs"]["pi_dist"]["provenance_type"] = "DIRECT"
        result = self.build_record(record)
        self.assertFalse(result["ok"])
        self.assertIn("does not match Python mapping", "\n".join(result["errors"]))

    def test_build_rejects_role_share_not_injected_from_dataset(self):
        record, errors = finalizer.finalize(draft(), dataset())
        self.assertEqual(errors, [])
        role = record["inputs"]["ai_replaceable_share"]["breakdown_by_role"][0]
        role["labor_share_of_total"] = 0.5
        role["contribution"] = 0.5 * role["within_role_automatable_fraction"]
        computed, calc_errors = build.calculate(record)
        self.assertEqual(calc_errors, [])
        record["inputs"]["ai_replaceable_share"]["value"] = computed[
            "ai_replaceable_share"
        ]
        record["scores"] = {
            name: {"arithmetic": record["scores"][name]["arithmetic"], "score": computed[name]}
            for name in "VCABM"
        }
        record["S"] = computed["S"]
        result = self.build_record(record)
        self.assertFalse(result["ok"])
        self.assertIn("does not match injected", "\n".join(result["errors"]))

    def test_build_acceptance_requires_exact_sol_validator_model(self):
        record, errors = finalizer.finalize(draft(), dataset())
        self.assertEqual(errors, [])
        root = tempfile.mkdtemp(prefix="v311_review_model_test_")
        self.addCleanup(shutil.rmtree, root)
        review_dir = os.path.join(root, "review")
        review_path = os.path.join(
            review_dir, record["naics"], record["run_meta"]["run_id"] + ".json"
        )
        os.makedirs(os.path.dirname(review_path))
        with open(os.path.join(SCHEMAS, "review_record.schema.json")) as handle:
            review_schema = json.load(handle)
        computed, arithmetic_errors, deltas = build.recompute(record)
        self.assertEqual(arithmetic_errors, [])
        with open(os.path.join(HERE, "thresholds.json")) as handle:
            thresholds = json.load(handle)
        decision = build.decide(
            computed["S"],
            {name: computed[name] for name in "VCABM"},
            record["cross_checks"]["terminal_value"]["class"],
            record["confidence_overall"],
            thresholds,
        )
        flags = build.record_flags(record, computed, decision, deltas)
        expected_audits = build.source_audit_pairs(record)
        review = {
            "naics": record["naics"],
            "run_id": record["run_meta"]["run_id"],
            "review_meta": {
                "model_id": "Sol",
                "review_date": "2026-07-21",
                "prompt_version": "validator-3.1.1",
            },
            "verdict": "accepted",
            "checks": {
                name: {"pass": True, "note": "Synthetic pass."}
                for name in campaign.CHECK_NAMES
            },
            "source_audits": [
                {
                    "input_path": item["input_path"],
                    "url": item["url"],
                    "resolves": True,
                    "claim_supported": True,
                    "note": "Synthetic source audit pass.",
                }
                for item in expected_audits
            ],
            "reasons": [],
            "flags_reviewed": flags,
        }
        with open(review_path, "w") as handle:
            json.dump(review, handle)
        status, _summary, model_errors = build.acceptance_status(
            record["naics"], record, review_dir, review_schema, expected_audits, flags
        )
        self.assertEqual(status, "pending")
        self.assertIn("does not match required", "\n".join(model_errors))

        review["review_meta"]["model_id"] = "gpt-5.6-sol"
        with open(review_path, "w") as handle:
            json.dump(review, handle)
        status, _summary, model_errors = build.acceptance_status(
            record["naics"], record, review_dir, review_schema, expected_audits, flags
        )
        self.assertEqual(model_errors, [])
        self.assertEqual(status, "accepted")

    def test_build_rejects_sol_as_v311_fleet_research_model(self):
        source = draft()
        source["run_meta"]["model_id"] = "gpt-5.6-sol"
        record, errors = finalizer.finalize(source, dataset())
        self.assertEqual(errors, [])
        result = self.build_record(record)
        self.assertFalse(result["ok"])
        self.assertIn("fleet model_id", "\n".join(result["errors"]))

    def test_review_campaign_routes_future_v311_dependencies(self):
        record, errors = finalizer.finalize(draft(), dataset())
        self.assertEqual(errors, [])
        root = tempfile.mkdtemp(prefix="v311_campaign_test_")
        self.addCleanup(shutil.rmtree, root)
        prompt_dir = os.path.join(root, "pipeline", "prompts_v3_1_1")
        dataset_dir = os.path.join(root, "pipeline", "datasets", "derived")
        run_dir = os.path.join(root, "pipeline", "runs", "999999")
        schema_dir = os.path.join(root, "pipeline", "build", "schemas")
        os.makedirs(prompt_dir)
        os.makedirs(dataset_dir)
        os.makedirs(run_dir)
        os.makedirs(schema_dir)
        shutil.copy(
            os.path.join(SCHEMAS, "run_record_v3_1_1.schema.json"), schema_dir
        )
        with open(os.path.join(prompt_dir, "999999.md"), "w") as handle:
            handle.write("synthetic future v3.1.1 prompt\n")
        with open(os.path.join(dataset_dir, "999999.json"), "w") as handle:
            json.dump(dataset(), handle)
        run_path = os.path.join(run_dir, "synthetic.json")
        with open(run_path, "w") as handle:
            json.dump(record, handle)
        with open(os.path.join(HERE, "thresholds.json")) as handle:
            thresholds = json.load(handle)
        entry = campaign._campaign_entry(
            root, "fleet", run_path, record, thresholds
        )
        self.assertEqual(
            entry["prompt_path"],
            os.path.join("pipeline", "prompts_v3_1_1", "999999.md"),
        )
        self.assertEqual(
            entry["required_validator_prompt_version"], "validator-3.1.1"
        )
        self.assertEqual(entry["required_research_model_id"], "gpt-5.6-terra")
        self.assertEqual(entry["required_validator_model_id"], "gpt-5.6-sol")

        wrong_fleet = copy.deepcopy(record)
        wrong_fleet["run_meta"]["model_id"] = "gpt-5.6-sol"
        with self.assertRaisesRegex(ValueError, "fleet v3.1.1 model_id"):
            campaign._campaign_entry(root, "fleet", run_path, wrong_fleet, thresholds)

        golden = campaign._campaign_entry(
            root, "golden", run_path, wrong_fleet, thresholds
        )
        self.assertEqual(golden["required_research_model_id"], "gpt-5.6-sol")

        review = {
            "naics": record["naics"],
            "run_id": record["run_meta"]["run_id"],
            "review_meta": {
                "model_id": "Sol",
                "review_date": "2026-07-21",
                "prompt_version": "validator-3.1.1",
            },
            "verdict": "accepted",
            "checks": {
                name: {"pass": True, "note": "Synthetic pass."}
                for name in campaign.CHECK_NAMES
            },
            "source_audits": [
                {
                    "input_path": item["input_path"],
                    "url": item["url"],
                    "resolves": True,
                    "claim_supported": True,
                    "note": "Synthetic source audit pass.",
                }
                for item in entry["expected_source_audits"]
            ],
            "reasons": [],
            "flags_reviewed": copy.deepcopy(entry["stage4_flags"]),
        }
        self.assertIn(
            "review model_id 'Sol' != required 'gpt-5.6-sol'",
            "\n".join(campaign.review_semantic_errors(review, entry)),
        )
        review["review_meta"]["model_id"] = "gpt-5.6-sol"
        self.assertEqual(campaign.review_semantic_errors(review, entry), [])

        wrong = copy.deepcopy(review)
        wrong["verdict"] = "wrong"
        wrong["reasons"] = [
            "inputs.pi_dist has an unreasonable selected-value bridge."
        ]
        self.assertIn(
            "wrong requires at least one failed check or source audit",
            "\n".join(campaign.review_semantic_errors(wrong, entry)),
        )
        wrong["checks"]["judgment_inputs_plausible"]["pass"] = False
        self.assertEqual(campaign.review_semantic_errors(wrong, entry), [])

    def test_urls_outside_fact_table_are_rejected(self):
        source = draft()
        source["inputs"]["buy_mult"]["estimate_basis"][
            "judgment_step"
        ] += " https://example.com/hidden"
        self.assertIn("URLs are permitted only", "\n".join(contract.semantic_errors(source)))


if __name__ == "__main__":
    unittest.main(verbosity=2)
