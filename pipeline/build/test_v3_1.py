#!/usr/bin/env python3
"""Synthetic tests for the v3.1 draft -> Python final record boundary.

These tests do not read, write or rerun any production industry record.
"""

import copy
import contextlib
import importlib.util
import io
import json
import os
import shutil
import tempfile
import unittest
from pathlib import Path

HERE = os.path.dirname(os.path.abspath(__file__))
SCHEMAS = os.path.join(HERE, "schemas")

_build_spec = importlib.util.spec_from_file_location("build", os.path.join(HERE, "build.py"))
build = importlib.util.module_from_spec(_build_spec)
_build_spec.loader.exec_module(build)

_finalize_spec = importlib.util.spec_from_file_location(
    "finalize_v31", os.path.join(HERE, "finalize_run_v3_1.py")
)
finalize = importlib.util.module_from_spec(_finalize_spec)
_finalize_spec.loader.exec_module(finalize)

_assemble_spec = importlib.util.spec_from_file_location(
    "assemble_v31", os.path.join(HERE, "assemble_prompts.py")
)
assemble = importlib.util.module_from_spec(_assemble_spec)
_assemble_spec.loader.exec_module(assemble)

_campaign_spec = importlib.util.spec_from_file_location(
    "review_campaign_v31", os.path.join(HERE, "review_campaign.py")
)
campaign = importlib.util.module_from_spec(_campaign_spec)
_campaign_spec.loader.exec_module(campaign)


def citation():
    return {
        "url": "https://example.com/adoption",
        "title": "Synthetic adoption source",
        "figure_quoted": "Thirty percent of firms report material use.",
        "access_date": "2026-07-20",
        "scope": "Synthetic US target-industry firms; percentage of firms.",
    }


def evidence(value, provenance="ESTIMATE", quality="NONE", citations=None):
    return {
        "value": value,
        "provenance_type": provenance,
        "evidence_quality": quality,
        "source_fact": (
            "Synthetic source reports 30% material firm adoption."
            if citations else
            "No source directly establishes this selected value."
        ),
        "derivation": (
            "Use the directly reported value."
            if provenance == "DIRECT" else
            "Open estimate with stated basis for this synthetic fixture."
        ),
        "plausible_range": "synthetic bounded range",
        "citations": citations or [],
    }


def judgment(value):
    result = evidence(value)
    result["rationale"] = "Synthetic bounded mechanism judgment."
    return result


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
                    "emp_share": 0.5,
                    "wage_share": 0.6,
                },
                {
                    "soc": "22-2222",
                    "title": "Synthetic Specialists",
                    "emp_share": 0.4,
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
    owner = evidence(0.3)
    owner["succession_shortage_documented"] = {
        "value": False,
        "evidence": "No documented shortage in this synthetic fixture.",
    }
    return {
        "naics": "999999",
        "title": "Synthetic Industry",
        "run_meta": {
            "model_id": "synthetic-model",
            "run_date": "2026-07-20",
            "run_id": "synthetic-s1-999999",
            "template_version": "3.1",
            "prompt_version": "synthetic-prompt",
        },
        "dataset_fallbacks": {},
        "inputs": {
            "ai_replaceable_share": {
                "role_judgments": [
                    {
                        "soc": "11-1111",
                        "within_role_automatable_fraction": 0.2,
                        "rationale": "Synthetic management task rationale.",
                        "plausible_range": "0.1-0.3",
                    },
                    {
                        "soc": "22-2222",
                        "within_role_automatable_fraction": 0.6,
                        "rationale": "Synthetic specialist task rationale.",
                        "plausible_range": "0.5-0.7",
                    },
                    {
                        "soc": "RESIDUAL",
                        "within_role_automatable_fraction": 0.4,
                        "rationale": "Synthetic residual task rationale.",
                        "plausible_range": "0.3-0.5",
                    },
                ],
                "provenance_type": "ESTIMATE",
                "evidence_quality": "NONE",
                "source_fact": "No source directly establishes role fractions.",
                "derivation": "Open task-level estimates for the synthetic fixture.",
                "citations": [],
            },
            "pi_dist": judgment(0.5),
            "pi_moat": judgment(0.5),
            "t50_years": evidence(4.0),
            "current_adoption_pct": evidence(
                0.3, provenance="DIRECT", quality="HIGH", citations=[citation()]
            ),
            "historical_analogs": evidence("Synthetic gradual analog"),
            "owners_60plus_pct": owner,
            "active_consolidators": evidence(2),
            "buy_mult": evidence(4.0),
            "exit_mult": evidence(8.0),
            "pricing_structure": evidence("Synthetic fixed-fee structure"),
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
        "confidence_overall": "LOW",
        "heterogeneous": False,
        "top_uncertain_inputs": [
            {
                "input": "t50_years",
                "plausible_range": "2-6 years",
                "score_impact": "Synthetic sensitivity description.",
            }
        ],
        "reviewer_note": "Synthetic fixture; not a production industry record.",
    }


class V31Finalizer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open(os.path.join(SCHEMAS, "research_draft_v3_1.schema.json")) as handle:
            cls.draft_schema = json.load(handle)
        with open(os.path.join(SCHEMAS, "run_record_v3_1.schema.json")) as handle:
            cls.run_schema = json.load(handle)

    def assertDraftSchema(self, value):
        self.assertEqual(
            build.schema_errors(value, self.draft_schema, self.draft_schema),
            [],
        )

    def test_finalizer_injects_roles_and_scores(self):
        source_draft = draft()
        source_dataset = dataset()
        self.assertDraftSchema(source_draft)
        record, errors = finalize.finalize(source_draft, source_dataset)
        self.assertEqual(errors, [])
        self.assertEqual(
            build.schema_errors(record, self.run_schema, self.run_schema),
            [],
        )
        self.assertEqual(record["dataset_inputs"], {
            key: source_dataset[key]
            for key in ("labor_share", "role_mix", "n_total", "n_band")
        })
        self.assertEqual(record["run_meta"]["finalizer_version"], "finalizer-3.1")
        roles = record["inputs"]["ai_replaceable_share"]["breakdown_by_role"]
        self.assertEqual([role["soc"] for role in roles], [
            "11-1111", "22-2222", "RESIDUAL"
        ])
        self.assertEqual([role["role"] for role in roles], [
            "Synthetic Managers",
            "Synthetic Specialists",
            "Unlisted occupations / residual wage share",
        ])
        self.assertAlmostEqual(
            record["inputs"]["ai_replaceable_share"]["value"],
            0.6 * 0.2 + 0.3 * 0.6 + 0.1 * 0.4,
        )
        _computed, arithmetic_errors, _deltas = build.recompute(record)
        self.assertEqual(arithmetic_errors, [])

    def test_missing_supplied_soc_is_rejected(self):
        source_draft = draft()
        source_draft["inputs"]["ai_replaceable_share"]["role_judgments"].pop(1)
        _record, errors = finalize.finalize(source_draft, dataset())
        self.assertIn("role judgments missing supplied SOC codes", "\n".join(errors))

    def test_fallback_for_non_null_dataset_is_rejected(self):
        source_draft = draft()
        source_draft["dataset_fallbacks"]["labor_share"] = evidence(0.4)
        _record, errors = finalize.finalize(source_draft, dataset())
        self.assertIn("fallback is forbidden", "\n".join(errors))

    def test_dataset_fallback_bounds_are_enforced(self):
        source_draft = draft()
        source_dataset = dataset()
        source_dataset["labor_share"]["value"] = None
        source_draft["dataset_fallbacks"]["labor_share"] = evidence(-0.1)
        _record, errors = finalize.finalize(source_draft, source_dataset)
        self.assertIn(
            "effective labor_share.value must be a nonnegative number",
            "\n".join(errors),
        )

        # Dataset derivation deliberately preserves labor-compensation/revenue
        # anomalies above 1.0; the invariant is nonnegative, not a fraction cap.
        source_draft["dataset_fallbacks"]["labor_share"]["value"] = 2.0
        record, errors = finalize.finalize(source_draft, source_dataset)
        self.assertEqual(errors, [])
        self.assertEqual(record["dataset_inputs"]["labor_share"]["value"], 2.0)

        source_draft = draft()
        source_dataset = dataset()
        source_dataset["n_band"]["value"] = None
        source_draft["dataset_fallbacks"]["n_band"] = evidence(-1)
        _record, errors = finalize.finalize(source_draft, source_dataset)
        self.assertIn(
            "effective n_band.value must be a nonnegative integer",
            "\n".join(errors),
        )
        source_draft["dataset_fallbacks"]["n_band"]["value"] = 100.0
        record, errors = finalize.finalize(source_draft, source_dataset)
        self.assertEqual(errors, [])
        self.assertEqual(record["dataset_inputs"]["n_band"]["value"], 100.0)
        source_draft["dataset_fallbacks"]["n_band"]["value"] = 100.5
        _record, errors = finalize.finalize(source_draft, source_dataset)
        self.assertIn(
            "effective n_band.value must be a nonnegative integer",
            "\n".join(errors),
        )

    def test_url_outside_atomic_citation_is_rejected(self):
        source_draft = draft()
        source_draft["inputs"]["buy_mult"]["derivation"] += " https://example.com/hidden"
        _record, errors = finalize.finalize(source_draft, dataset())
        self.assertIn("URLs are permitted only in citations[].url", "\n".join(errors))

    def test_evidence_quality_axis_is_independent_and_consistent(self):
        source_draft = draft()
        source_draft["inputs"]["buy_mult"]["evidence_quality"] = "MED"
        _record, errors = finalize.finalize(source_draft, dataset())
        self.assertIn("empty citations requires evidence_quality NONE", "\n".join(errors))

    def test_t50_boundary_is_deterministic(self):
        source_draft = draft()
        source_draft["inputs"]["current_adoption_pct"]["value"] = 0.55
        source_draft["inputs"]["t50_years"]["value"] = 2.0
        _record, errors = finalize.finalize(source_draft, dataset())
        self.assertIn("t50_years must be 0", "\n".join(errors))

        source_draft["inputs"]["t50_years"]["value"] = 0
        record, errors = finalize.finalize(source_draft, dataset())
        self.assertEqual(errors, [])
        self.assertEqual(record["scores"]["A"]["score"], 10.0)

    def test_estimate_flags_use_provenance_not_evidence_quality(self):
        record, errors = finalize.finalize(draft(), dataset())
        self.assertEqual(errors, [])
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
        self.assertTrue(any(
            flag.startswith("ESTIMATE_HEAVY:") and "provenance_type ESTIMATE" in flag
            for flag in flags
        ))

    def test_estimate_flags_include_dataset_fallbacks(self):
        source_draft = draft()
        source_dataset = dataset()
        source_dataset["labor_share"]["value"] = None
        source_draft["dataset_fallbacks"]["labor_share"] = evidence(0.4)
        record, errors = finalize.finalize(source_draft, source_dataset)
        self.assertEqual(errors, [])
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
        estimate_flag = next(
            flag for flag in flags if flag.startswith("ESTIMATE_HEAVY:")
        )
        self.assertIn("dataset_inputs.labor_share", estimate_flag)

    def test_final_schema_rejects_invalid_scoring_types(self):
        record, errors = finalize.finalize(draft(), dataset())
        self.assertEqual(errors, [])
        record["inputs"]["buy_mult"]["value"] = "four"
        errors = build.schema_errors(record, self.run_schema, self.run_schema)
        self.assertIn(
            "$.inputs.buy_mult.value: expected type number, got str",
            errors,
        )

    def test_build_selects_v31_schema(self):
        record, errors = finalize.finalize(draft(), dataset())
        self.assertEqual(errors, [])
        root = tempfile.mkdtemp(prefix="v31_build_test_")
        self.addCleanup(shutil.rmtree, root)
        runs = os.path.join(root, "runs", "999999")
        reviews = os.path.join(root, "reviews")
        output = os.path.join(root, "output")
        os.makedirs(runs)
        os.makedirs(reviews)
        os.makedirs(output)
        with open(os.path.join(runs, "synthetic.json"), "w") as handle:
            json.dump(record, handle)
        result = build.run_build(
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
        self.assertTrue(result["ok"], result.get("errors"))
        self.assertEqual(result["stats"]["built"], 1)
        self.assertEqual(result["stats"]["published"], 1)

    def test_v31_build_rejects_missing_finalizer_marker(self):
        record, errors = finalize.finalize(draft(), dataset())
        self.assertEqual(errors, [])
        del record["run_meta"]["finalizer_version"]
        self.assertIn(
            "$.run_meta: missing required key 'finalizer_version'",
            build.schema_errors(record, self.run_schema, self.run_schema),
        )

    def test_build_and_campaign_reject_unknown_template_version(self):
        record, errors = finalize.finalize(draft(), dataset())
        self.assertEqual(errors, [])
        record["run_meta"]["template_version"] = "3.2"
        root = tempfile.mkdtemp(prefix="v31_unknown_version_")
        self.addCleanup(shutil.rmtree, root)
        runs = os.path.join(root, "runs", "999999")
        reviews = os.path.join(root, "reviews")
        output = os.path.join(root, "output")
        os.makedirs(runs)
        os.makedirs(reviews)
        os.makedirs(output)
        run_path = os.path.join(runs, "synthetic.json")
        with open(run_path, "w") as handle:
            json.dump(record, handle)
        result = build.run_build(
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
        self.assertFalse(result["ok"])
        self.assertIn("unsupported template_version '3.2'", "\n".join(result["errors"]))
        with open(os.path.join(HERE, "thresholds.json")) as handle:
            thresholds = json.load(handle)
        with self.assertRaisesRegex(ValueError, "unsupported template_version '3.2'"):
            campaign._campaign_entry(
                root, "fleet", run_path, record, thresholds
            )

    def test_v31_prompt_renders_in_memory_without_writing(self):
        template_path = assemble.VERSION_PATHS["3.1"]["template"]
        template = template_path.read_text(encoding="utf-8")
        rendered = assemble.assemble_one(
            "541420", "Industrial Design Services", template, "3.1"
        )
        assemble.validate_prompt_text("541420", rendered)
        self.assertIn("Template version: 3.1", rendered)
        self.assertIn("do not copy them into the draft", rendered)
        self.assertIn("{{MODEL_ID}}", rendered)

    def test_v31_prompt_assembly_creates_output_directory(self):
        root = tempfile.mkdtemp(prefix="v31_prompt_assembly_")
        self.addCleanup(shutil.rmtree, root)
        prompts_dir = Path(root) / "nested" / "prompts_v3_1"
        original = assemble.VERSION_PATHS["3.1"]["prompts"]
        assemble.VERSION_PATHS["3.1"]["prompts"] = prompts_dir
        self.addCleanup(
            assemble.VERSION_PATHS["3.1"].__setitem__, "prompts", original
        )
        with contextlib.redirect_stdout(io.StringIO()):
            assemble.main(["--template-version", "3.1"])
        self.assertTrue(prompts_dir.is_dir())
        self.assertTrue((prompts_dir / "541420.md").is_file())

    def test_v31_acceptance_requires_validator_v31(self):
        record, errors = finalize.finalize(draft(), dataset())
        self.assertEqual(errors, [])
        root = tempfile.mkdtemp(prefix="v31_review_binding_")
        self.addCleanup(shutil.rmtree, root)
        review_dir = os.path.join(root, "review")
        review_naics_dir = os.path.join(review_dir, record["naics"])
        os.makedirs(review_naics_dir)
        expected_audits = build.source_audit_pairs(record)
        review = {
            "naics": record["naics"],
            "run_id": record["run_meta"]["run_id"],
            "review_meta": {
                "model_id": "Sol",
                "review_date": "2026-07-20",
                "prompt_version": "validator-3.0",
            },
            "verdict": "accepted",
            "checks": {
                name: {"pass": True, "note": "Synthetic full-depth check."}
                for name in campaign.CHECK_NAMES
            },
            "source_audits": [
                dict(
                    pair,
                    resolves=True,
                    claim_supported=True,
                    note="Synthetic source audit.",
                )
                for pair in expected_audits
            ],
            "reasons": [],
            "flags_reviewed": [],
        }
        review_path = os.path.join(
            review_naics_dir, record["run_meta"]["run_id"] + ".json"
        )
        with open(review_path, "w") as handle:
            json.dump(review, handle)
        with open(os.path.join(SCHEMAS, "review_record.schema.json")) as handle:
            review_schema = json.load(handle)
        status, _summary, errors = build.acceptance_status(
            record["naics"],
            record,
            review_dir,
            review_schema,
            expected_audits,
            [],
        )
        self.assertEqual(status, "pending")
        self.assertIn("does not match required 'validator-3.1'", "\n".join(errors))

        review["review_meta"]["prompt_version"] = "validator-3.1"
        with open(review_path, "w") as handle:
            json.dump(review, handle)
        status, _summary, errors = build.acceptance_status(
            record["naics"],
            record,
            review_dir,
            review_schema,
            expected_audits,
            [],
        )
        self.assertEqual(errors, [])
        self.assertEqual(status, "accepted")

    def test_review_campaign_routes_v31_prompt_path(self):
        record, errors = finalize.finalize(draft(), dataset())
        self.assertEqual(errors, [])
        root = tempfile.mkdtemp(prefix="v31_campaign_test_")
        self.addCleanup(shutil.rmtree, root)
        prompt_dir = os.path.join(root, "pipeline", "prompts_v3_1")
        dataset_dir = os.path.join(root, "pipeline", "datasets", "derived")
        run_dir = os.path.join(root, "pipeline", "runs", "999999")
        schema_dir = os.path.join(root, "pipeline", "build", "schemas")
        os.makedirs(prompt_dir)
        os.makedirs(dataset_dir)
        os.makedirs(run_dir)
        os.makedirs(schema_dir)
        shutil.copy(
            os.path.join(SCHEMAS, "run_record_v3_1.schema.json"),
            schema_dir,
        )
        with open(os.path.join(prompt_dir, "999999.md"), "w") as handle:
            handle.write("synthetic v3.1 prompt\n")
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
            os.path.join("pipeline", "prompts_v3_1", "999999.md"),
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
