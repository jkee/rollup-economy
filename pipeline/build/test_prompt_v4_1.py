#!/usr/bin/env python3
"""v4.1 class-neutral spec, prompt assembly, and semantic-lint tests."""

import copy
import hashlib
import importlib.util
import json
import tempfile
from pathlib import Path
import unittest
from unittest import mock


HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


assemble = load_module("assemble_prompt_v41_tests", HERE / "assemble_prompts.py")


def normalized_dataset(code="541512", title="Computer Systems Design Services", n_band=None):
    return {
        "dataset_version": "4.1",
        "snapshot_id": f"fixture-{code}",
        "naics": code,
        "title": title,
        "labor_share": {"value": 0.5, "quality": "MED", "basis": "Fixture normalized share."},
        "n_total": {"value": 100, "quality": "HIGH", "basis": "Fixture normalized count."},
        "n_band": {
            "value": n_band,
            "quality": "NONE" if n_band is None else "MED",
            "basis": "Fixture normalized band count; null is an admissible missing value.",
        },
        "role_mix": {
            "basis": "Fixture normalized role mix.",
            "quality": "MED",
            "occupations": [{
                "soc": "15-1252", "title": "Software Developers",
                "employment_share": 1.0, "wage_share": 1.0,
            }],
        },
        "provenance": {
            "derivation_version": "fixture-v1",
            "source_manifest_sha256": "1" * 64,
            "vintage": "2026",
        },
    }


def fixture_spec(code="541512", title="Computer Systems Design Services", dataset_sha256=None):
    return {
        "spec_version": "4.1",
        "naics": code,
        "title": title,
        "dataset_snapshot": {
            "path": f"pipeline/datasets/v4_1/{code}.json",
            "sha256": dataset_sha256 or "0" * 64,
        },
        "target_archetype": {
            "selected_id": "recurring-smb-operator",
            "alternatives": [{
                "id": "recurring-smb-operator",
                "name": "Recurring-services SMB operator",
                "inclusion_criteria": ["Recurring accountable services"],
                "exclusion_criteria": ["Pure product resale"],
                "band_count": {"base": 70, "low": 60, "high": 80},
                "source_ids": [],
                "rationale": "Largest objectively enumerated band population.",
            }],
            "residual": {
                "name": "Other business models",
                "band_count": {"base": 30, "low": 20, "high": 40},
                "rationale": "Named remainder outside the selected operating model.",
            },
            "enumeration_coverage": {"base": 1.0, "low": 0.9, "high": 1.0},
            "sources": [],
            "selection_basis": "Selected solely because it has the largest base band count.",
            "selection_uncertainty": False,
        },
        "value_basis": {
            "mode": "dataset",
            "scope": "The pinned NAICS employee cash-cost and role basis.",
            "labor_contractor_cash_cost_share": None,
            "roles": [],
            "sources": [],
            "bridge": None,
            "rationale": "The supplied occupation basis reasonably represents the fixed archetype.",
            "caveats": ["The published occupation level is broader than any individual target."],
        },
        "source_hints": [{
            "area": "implementation",
            "source": "A current primary industry survey",
            "why": "Measures operational realization rather than experimentation.",
            "uncertain_exists": False,
        }],
        "research_questions": {
            "implementation": ["What low/base/high r1-r5 schedules are operationally feasible?"],
            "commercial_retention": ["How are realized savings repriced at renewal?"],
            "sale_availability": ["What share of band firms is plausibly for sale within five years?"],
            "valuation_robustness": ["Are all-in entry and downside exit earnings bases comparable?"],
            "operator_survival": ["What share of baseline demand remains operator-controlled and paid in year five?"],
        },
        "special_notes": ["Keep cash removal separate from operational realization."],
    }


class V41PromptInfrastructureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.template = (REPO / "pipeline" / "template" / "prompt_template_v4_1.md").read_text(encoding="utf-8")
        cls.runner = (REPO / "pipeline" / "template" / "runner_brief_v4_1.md").read_text(encoding="utf-8")
        cls.validator = (REPO / "pipeline" / "template" / "validator_brief_v4_1.md").read_text(encoding="utf-8")

    def test_route_is_separate_and_spec_backed(self):
        route = assemble.VERSION_PATHS["4.1"]
        self.assertEqual(route["template"], REPO / "pipeline" / "template" / "prompt_template_v4_1.md")
        self.assertEqual(route["prompts"], REPO / "pipeline" / "prompts_v4_1")
        self.assertEqual(route["specs"], REPO / "pipeline" / "specs_v4_1")
        self.assertNotEqual(route["template"], assemble.VERSION_PATHS["4.0"]["template"])

    def test_schema_has_four_explicit_value_basis_modes(self):
        schema = json.loads(assemble.SPEC_V4_1_SCHEMA.read_text(encoding="utf-8"))
        modes = schema["definitions"]["value_basis"]["properties"]["mode"]["enum"]
        self.assertEqual(modes, ["dataset", "target_specific", "assumption", "missing"])
        archetype = schema["definitions"]["target_archetype"]
        self.assertEqual(archetype["properties"]["selection_uncertainty"]["type"], "boolean")
        self.assertNotIn("separate_records_required", archetype["properties"])
        self.assertFalse(schema["additionalProperties"])

    def test_overlapping_archetypes_are_one_uncertain_primary_record(self):
        spec = fixture_spec()
        spec["target_archetype"]["alternatives"].append({
            "id": "project-led-operator",
            "name": "Project-led operator",
            "inclusion_criteria": ["Project-based accountable services"],
            "exclusion_criteria": ["Recurring managed-services contracts"],
            "band_count": {"base": 68, "low": 55, "high": 82},
            "source_ids": [],
            "rationale": "Second-largest mutually exclusive operating model.",
        })
        spec["target_archetype"]["selection_uncertainty"] = True
        assemble.validate_industry_spec_v4_1(spec["naics"], spec["title"], spec)

        broken = copy.deepcopy(spec)
        broken["target_archetype"]["selection_uncertainty"] = False
        with self.assertRaisesRegex(assemble.AssembleError, "must be true exactly"):
            assemble.validate_industry_spec_v4_1(broken["naics"], broken["title"], broken)

        self.assertIn("readiness to `UNPROVEN`", self.template)
        self.assertIn("NAICS-wide claim", self.runner)

    def test_largest_base_tie_uses_lexicographically_smallest_id(self):
        spec = fixture_spec()
        spec["target_archetype"]["alternatives"].append({
            "id": "alternate-operator",
            "name": "Alternate operator",
            "inclusion_criteria": ["Alternate accountable service"],
            "exclusion_criteria": ["Recurring managed service"],
            "band_count": {"base": 70, "low": 55, "high": 85},
            "source_ids": [],
            "rationale": "Equal largest base population.",
        })
        spec["target_archetype"]["selection_uncertainty"] = True
        with self.assertRaisesRegex(assemble.AssembleError, "lexicographically smallest"):
            assemble.validate_industry_spec_v4_1(spec["naics"], spec["title"], spec)

        spec["target_archetype"]["selected_id"] = "alternate-operator"
        assemble.validate_industry_spec_v4_1(spec["naics"], spec["title"], spec)

    def test_normalized_null_n_band_renders_without_legacy_blocks(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            specs = root / "specs"
            datasets = root / "pipeline" / "datasets" / "v4_1"
            specs.mkdir()
            datasets.mkdir(parents=True)
            dataset_path = datasets / "541512.json"
            dataset_path.write_text(json.dumps(normalized_dataset()), encoding="utf-8")
            digest = hashlib.sha256(dataset_path.read_bytes()).hexdigest()
            spec = fixture_spec(dataset_sha256=digest)
            (specs / "541512.json").write_text(json.dumps(spec), encoding="utf-8")
            with mock.patch.object(assemble, "SPECS_V4_1_DIR", specs), mock.patch.object(
                assemble, "BLOCKS_DIR", specs / "does-not-exist"
            ), mock.patch.object(assemble, "REPO", root):
                first = assemble.assemble_v4_1_one("541512", "Computer Systems Design Services", self.template)
                second = assemble.assemble_v4_1_one("541512", "Computer Systems Design Services", self.template)
        self.assertEqual(first, second)
        self.assertIn('"mode": "dataset"', first)
        self.assertIn(digest, first)
        self.assertIn('"value": null', first)
        self.assertIn('"source_manifest_sha256"', first)
        self.assertEqual(set(assemble.PLACEHOLDER_RE.findall(first)), assemble.RUNTIME_PLACEHOLDERS)

    def test_direct_legacy_derived_dataset_path_is_rejected(self):
        spec = fixture_spec()
        spec["dataset_snapshot"]["path"] = "pipeline/datasets/derived/541512.json"
        with self.assertRaisesRegex(assemble.AssembleError, "datasets/v4_1/541512.json"):
            assemble.validate_industry_spec_v4_1(spec["naics"], spec["title"], spec)

    def test_target_specific_requires_complete_unit_sum_and_sources(self):
        spec = fixture_spec()
        spec["value_basis"] = {
            "mode": "target_specific",
            "scope": "The fixed archetype's employee-and-contractor cash-cost basis.",
            "labor_contractor_cash_cost_share": {
                "value": 0.5, "range": {"low": 0.4, "high": 0.6},
                "evidence_quality": "MED", "source_ids": ["B1"],
                "rationale": "Approved source-backed labor share.", "caveats": [],
            },
            "roles": [
                {"role_id": "DELIVERY", "title": "Delivery", "role_cash_cost_weight": 0.7, "source_ids": ["B1"], "rationale": "Approved cash-cost basis."},
                {"role_id": "ADMIN", "title": "Administration", "role_cash_cost_weight": 0.3, "source_ids": ["B1"], "rationale": "Approved cash-cost basis."},
            ],
            "sources": [{"id": "B1", "url": "https://example.com/basis", "title": "Basis source", "vintage": "2026"}],
            "bridge": None,
            "rationale": "A target-specific basis replaces an unrepresentative parent mix.",
            "caveats": [],
        }
        assemble.validate_industry_spec_v4_1(spec["naics"], spec["title"], spec)
        broken = copy.deepcopy(spec)
        broken["value_basis"]["roles"][1]["role_cash_cost_weight"] = 0.2
        with self.assertRaisesRegex(assemble.AssembleError, "sum to 1.0"):
            assemble.validate_industry_spec_v4_1(broken["naics"], broken["title"], broken)

    def test_dataset_bridge_is_closed_and_non_dataset_modes_forbid_it(self):
        bridge = {
            "population": "US establishments in the normalized NAICS population",
            "geography": "United States",
            "period": "Normalized source vintage",
            "unit": "Employee and contractor cash cost",
            "business_model": "Fixed target archetype versus broad NAICS population",
        }
        absent = fixture_spec()
        absent["value_basis"].pop("bridge")
        assemble.validate_industry_spec_v4_1(absent["naics"], absent["title"], absent)

        spec = fixture_spec()
        spec["value_basis"]["bridge"] = bridge
        assemble.validate_industry_spec_v4_1(spec["naics"], spec["title"], spec)

        incomplete = copy.deepcopy(spec)
        incomplete["value_basis"]["bridge"].pop("unit")
        with self.assertRaisesRegex(assemble.AssembleError, "missing key.*unit"):
            assemble.validate_industry_spec_v4_1(incomplete["naics"], incomplete["title"], incomplete)

        spec["value_basis"]["mode"] = "missing"
        with self.assertRaisesRegex(assemble.AssembleError, "requires bridge to be null"):
            assemble.validate_industry_spec_v4_1(spec["naics"], spec["title"], spec)

    def test_assumption_basis_is_bounded_source_free_and_unproven(self):
        spec = fixture_spec()
        spec["value_basis"] = {
            "mode": "assumption",
            "scope": "Pre-frozen target-archetype employee-and-contractor cash cost.",
            "labor_contractor_cash_cost_share": {
                "base": 0.55, "range": {"low": 0.4, "high": 0.7},
                "evidence_state": "ASSUMPTION", "evidence_quality": "NONE",
                "source_ids": [], "rationale": "Defensible class-neutral bound.",
                "caveats": ["Not directly evidenced."],
            },
            "roles": [
                {"role_id": "DELIVERY", "title": "Delivery", "role_cash_cost_weight": 0.7, "source_ids": [], "rationale": "Fixed pre-research role."},
                {"role_id": "ADMIN", "title": "Administration", "role_cash_cost_weight": 0.3, "source_ids": [], "rationale": "Fixed pre-research role."},
            ],
            "sources": [],
            "bridge": None,
            "rationale": "Bounded structure is more honest than a bad broad-industry proxy.",
            "caveats": ["Forces readiness UNPROVEN."],
        }
        assemble.validate_industry_spec_v4_1(spec["naics"], spec["title"], spec)

        sourced = copy.deepcopy(spec)
        sourced["value_basis"]["roles"][0]["source_ids"] = ["B1"]
        with self.assertRaisesRegex(assemble.AssembleError, "cannot claim sources"):
            assemble.validate_industry_spec_v4_1(sourced["naics"], sourced["title"], sourced)

        self.assertIn("force readiness to `UNPROVEN`", self.template)

    def test_missing_mode_forbids_authored_weights(self):
        spec = fixture_spec()
        spec["value_basis"]["mode"] = "missing"
        assemble.validate_industry_spec_v4_1(spec["naics"], spec["title"], spec)
        spec["value_basis"]["roles"] = [{"invented": True}]
        with self.assertRaisesRegex(assemble.AssembleError, "empty roles/sources"):
            assemble.validate_industry_spec_v4_1(spec["naics"], spec["title"], spec)

    def test_dataset_digest_is_fail_closed(self):
        spec = fixture_spec()
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            specs = root / "specs"
            datasets = root / "pipeline" / "datasets" / "v4_1"
            specs.mkdir()
            datasets.mkdir(parents=True)
            (datasets / "541512.json").write_text(json.dumps(normalized_dataset()), encoding="utf-8")
            (specs / "541512.json").write_text(json.dumps(spec), encoding="utf-8")
            with mock.patch.object(assemble, "SPECS_V4_1_DIR", specs), mock.patch.object(assemble, "REPO", root):
                with self.assertRaisesRegex(assemble.AssembleError, "digest mismatch"):
                    assemble.assemble_v4_1_one("541512", "Computer Systems Design Services", self.template)

    def test_semantic_lint_rejects_every_legacy_or_class_signal(self):
        examples = (
            "Use pi_dist here.", "Use pi moat here.", "Estimate owners_60plus_pct.",
            "This is in the golden set.", "Treat it as a winner.", "It is a melter.",
            "CONTROL-CODE WARNING", "Rebuild the V role breakdown.",
            "Rebuild the role basis used for V.",
        )
        for text in examples:
            with self.subTest(text=text), self.assertRaises(assemble.AssembleError):
                assemble.semantic_lint_v4_1("999999", text)

    def test_all_v41_instruction_surfaces_are_semantically_clean(self):
        for label, text in (("template", self.template), ("runner", self.runner), ("validator", self.validator)):
            with self.subTest(label=label):
                assemble.semantic_lint_v4_1(label, text)

    def test_partial_canary_and_exact_modes(self):
        entries = json.loads(assemble.TARGETS_PATH.read_text(encoding="utf-8"))["codes"]
        with tempfile.TemporaryDirectory() as directory:
            specs = Path(directory)
            (specs / "541512.json").write_text("{}", encoding="utf-8")
            with mock.patch.object(assemble, "SPECS_V4_1_DIR", specs):
                selected, missing = assemble._v4_1_entries(entries, "canary", True)
                self.assertEqual([item["naics"] for item in selected], ["541512"])
                self.assertEqual(len(missing), 4)
                with self.assertRaisesRegex(assemble.AssembleError, "missing required canary"):
                    assemble._v4_1_entries(entries, "canary", False)
                with self.assertRaisesRegex(assemble.AssembleError, "permitted only"):
                    assemble._v4_1_entries(entries, "full", True)

    def test_holdout_scope_is_exact_and_rejects_wrong_or_mixed_membership(self):
        entries = json.loads(assemble.TARGETS_PATH.read_text(encoding="utf-8"))["codes"]
        exact = list(assemble.HOLDOUT_V4_1_CODES)
        membership = {
            "version": "v4.1-holdout-2026-07-21",
            "selected_codes": exact,
            "bins": [{"selected_naics": code} for code in exact],
        }
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            specs = root / "specs"
            specs.mkdir()
            for code in exact:
                (specs / f"{code}.json").write_text("{}", encoding="utf-8")
            # A canary spec may coexist in the shared spec directory but must
            # never enter holdout selection.
            (specs / "238220.json").write_text("{}", encoding="utf-8")
            membership_path = root / "holdout.json"
            membership_path.write_text(json.dumps(membership), encoding="utf-8")
            with mock.patch.object(assemble, "SPECS_V4_1_DIR", specs), mock.patch.object(
                assemble, "HOLDOUT_MEMBERSHIP_PATH", membership_path
            ):
                selected, missing = assemble._v4_1_entries(entries, "holdout", False)
                self.assertEqual([item["naics"] for item in selected], sorted(exact))
                self.assertEqual(missing, [])
                with self.assertRaisesRegex(assemble.AssembleError, "permitted only"):
                    assemble._v4_1_entries(entries, "holdout", True)

                mixed = copy.deepcopy(membership)
                mixed["selected_codes"][-1] = "238220"
                membership_path.write_text(json.dumps(mixed), encoding="utf-8")
                with self.assertRaisesRegex(assemble.AssembleError, "differ from exact frozen"):
                    assemble._v4_1_entries(entries, "holdout", False)

                wrong_bins = copy.deepcopy(membership)
                wrong_bins["bins"][0]["selected_naics"] = "541214"
                membership_path.write_text(json.dumps(wrong_bins), encoding="utf-8")
                with self.assertRaisesRegex(assemble.AssembleError, "bins differ"):
                    assemble._v4_1_entries(entries, "holdout", False)

    def test_current_canary_and_holdout_specs_bind_normalized_datasets_exactly(self):
        expected = set(assemble.CANARY_V4_1_CODES) | set(assemble.HOLDOUT_V4_1_CODES)
        actual = {path.stem for path in assemble.SPECS_V4_1_DIR.glob("*.json")}
        self.assertTrue(expected.issubset(actual))
        for code in sorted(expected):
            with self.subTest(code=code):
                spec = json.loads((assemble.SPECS_V4_1_DIR / f"{code}.json").read_text(encoding="utf-8"))
                expected_path = f"pipeline/datasets/v4_1/{code}.json"
                self.assertEqual(spec["dataset_snapshot"]["path"], expected_path)
                dataset_path = REPO / expected_path
                self.assertEqual(
                    spec["dataset_snapshot"]["sha256"],
                    hashlib.sha256(dataset_path.read_bytes()).hexdigest(),
                )

    def test_research_prompt_is_route_neutral(self):
        lower = self.template.lower()
        self.assertNotIn("gpt-5.6-terra", lower)
        self.assertNotIn("gpt-5.6-sol", lower)
        self.assertNotIn("known outcome", lower)
        self.assertIn("same class-neutral prompt bytes", self.runner)


if __name__ == "__main__":
    unittest.main(verbosity=2)
