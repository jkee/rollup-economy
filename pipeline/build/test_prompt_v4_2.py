#!/usr/bin/env python3
"""v4.2 outcome-neutral spec, prompt assembly, membership, and leakage tests."""

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
    module_spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(module_spec)
    module_spec.loader.exec_module(module)
    return module


assemble = load_module("assemble_prompt_v42_tests", HERE / "assemble_prompts.py")


def normalized_dataset(code="541512", title="Computer Systems Design Services"):
    return {
        "dataset_version": "4.2",
        "snapshot_id": f"fixture-{code}",
        "naics": code,
        "title": title,
        "labor_share": {"value": 0.5, "quality": "MED", "basis": "Fixture share."},
        "n_total": {"value": 100, "quality": "HIGH", "basis": "Fixture count."},
        "n_band": {"value": 50, "quality": "MED", "basis": "Fixture band count."},
        "role_mix": {
            "basis": "Fixture role mix.",
            "quality": "MED",
            "occupations": [{
                "soc": "15-1252", "title": "Software Developers",
                "employment_share": 1.0, "wage_share": 1.0,
            }],
        },
        "provenance": {
            "derivation_version": "fixture-v4.2",
            "source_manifest_sha256": "1" * 64,
            "vintage": "2026",
        },
    }


def fixture_spec(methodology_sha="0" * 64, dataset_sha="0" * 64,
                 code="541512", title="Computer Systems Design Services"):
    return {
        "spec_version": "4.2",
        "naics": code,
        "title": title,
        "methodology_snapshot": {
            "path": "V4_2_RUNTIME_METHODOLOGY.md", "sha256": methodology_sha,
        },
        "dataset_snapshot": {
            "path": f"pipeline/datasets/v4_2/{code}.json", "sha256": dataset_sha,
        },
        "target_archetype": {
            "selected_id": "recurring-smb-operator",
            "alternatives": [{
                "id": "recurring-smb-operator",
                "name": "Recurring-services SMB operator",
                "inclusion_criteria": ["Recurring accountable services"],
                "exclusion_criteria": ["Pure product resale"],
                "band_count": {"base": 80, "low": 70, "high": 90},
                "source_ids": ["A1"],
                "rationale": "Largest objectively enumerated band population.",
            }],
            "residual": {
                "name": "Other business models",
                "band_count": {"base": 20, "low": 10, "high": 30},
                "rationale": "Named remainder outside the selected model.",
            },
            "enumeration_coverage": {"base": 1.0, "low": 0.9, "high": 1.0},
            "sources": [{
                "id": "A1", "url": "https://example.com/archetype",
                "title": "Archetype source", "vintage": "2026",
            }],
            "selection_basis": "Largest base count under the frozen rule.",
            "selection_uncertainty": False,
        },
        "value_basis": {
            "mode": "target_specific",
            "scope": "The fixed target archetype's controllable delivery cash costs.",
            "controllable_value_added_boundary": "Revenue less documented outside pass-through.",
            "approved_pass_through_categories": ["outside cloud resale"],
            "employee_cash_cost_id": "employee-cash",
            "controllable_contractor_cash_cost_id": "contractor-cash",
            "roles": [{
                "role_id": "delivery", "title": "Delivery",
                "role_cash_cost_weight": 1.0, "method": "OBSERVED",
                "evidence_quality": "MED", "source_ids": ["B1"],
                "rationale": "Target-specific delivery cost basis.",
            }],
            "sources": [{
                "id": "B1", "url": "https://example.com/value-basis",
                "title": "Value-basis source", "vintage": "2026",
            }],
            "rationale": "Source-backed controllable cash-cost structure.",
            "caveats": ["Individual targets may vary."],
        },
        "source_hints": [{
            "area": "operational realization", "source": "Current primary survey",
            "why": "Measures deployment realization.", "uncertain_exists": False,
        }],
        "research_questions": {
            "controllable_value_added": ["Which documented categories are outside pass-through?"],
            "operational_realization": ["What r and k schedules are feasible?"],
            "commercial_retention": ["What c schedule follows contract renewal?"],
            "sale_availability": ["What share is sale-available within five years?"],
            "buyer_access_win": ["What conditional share can the reference buyer access and win?"],
            "valuation_robustness": ["What comparable entry and downside multiples apply?"],
            "operator_survival": ["What constant-real-price value-added demand remains?"],
        },
        "special_notes": ["Keep all primitive channels separate."],
    }


class V42PromptInfrastructureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.template = (REPO / "pipeline/template/prompt_template_v4_2.md").read_text()
        cls.runner = (REPO / "pipeline/template/runner_brief_v4_2.md").read_text()
        cls.validator = (REPO / "pipeline/template/validator_brief_v4_2.md").read_text()

    def test_route_is_separate_and_strict(self):
        route = assemble.VERSION_PATHS["4.2"]
        self.assertEqual(route["template"], REPO / "pipeline/template/prompt_template_v4_2.md")
        self.assertEqual(route["prompts"], REPO / "pipeline/prompts_v4_2")
        self.assertEqual(route["specs"], REPO / "pipeline/specs_v4_2")
        self.assertNotEqual(route["template"], assemble.VERSION_PATHS["4.1"]["template"])

    def test_schema_contract_matches_assembler(self):
        schema = json.loads(assemble.SPEC_V4_2_SCHEMA.read_text())
        self.assertEqual(set(schema["required"]), assemble.V4_2_SPEC_KEYS)
        questions = schema["properties"]["research_questions"]["required"]
        self.assertEqual(set(questions), assemble.V4_2_QUESTION_KEYS)
        basis = schema["definitions"]["value_basis"]
        self.assertEqual(set(basis["required"]), assemble.V4_2_VALUE_BASIS_KEYS)
        self.assertEqual(
            basis["properties"]["mode"]["enum"],
            ["target_specific", "assumption", "missing"],
        )
        self.assertEqual(
            schema["definitions"]["target_archetype"]["properties"]["sources"]
            ["items"]["allOf"][1]["properties"]["id"]["pattern"],
            "^A[1-9][0-9]*$",
        )
        self.assertEqual(
            basis["properties"]["sources"]["items"]["allOf"][1]
            ["properties"]["id"]["pattern"],
            "^B[1-9][0-9]*$",
        )

    def test_packet_schema_exposes_closed_a_through_d_runtime_contract(self):
        schema = json.loads(
            (REPO / "pipeline/build/schemas/research_packet_v4_2.schema.json").read_text()
        )
        inputs = schema["properties"]["inputs"]
        self.assertTrue({
            "deal_execution_capacity_5y", "integration_onboarding_capacity_5y",
            "normalized_y5_operating_state", "downside_exit_multiple",
            "operator_controlled_value_added_demand_share_y5",
        }.issubset(inputs["required"]))
        reconciliation = schema["definitions"]["pass_through_reconciliation"]
        self.assertEqual(
            set(reconciliation["required"]),
            {"revenue_basis", "included_cost_ids", "already_netted_cost_ids", "evidence"},
        )
        accounting = schema["definitions"]["recognized_accounting_basis"]
        self.assertEqual(
            set(accounting["required"]),
            {"recognition_standard", "measurement_period", "pass_through_presentation"},
        )
        self.assertEqual(
            accounting["properties"]["recognition_standard"]["const"],
            "ACCRUAL_RECOGNIZED_REVENUE",
        )
        self.assertEqual(
            accounting["properties"]["measurement_period"]["const"],
            "TRAILING_TWELVE_MONTHS",
        )
        self.assertEqual(
            accounting["properties"]["pass_through_presentation"]["enum"],
            ["GROSS_OF_ALL", "NET_OF_ALL", "MIXED"],
        )
        capacity = schema["definitions"]["capacity_scope"]["properties"]
        self.assertEqual(capacity["horizon_years"]["const"], 5)
        self.assertEqual(capacity["geography"]["const"], "UNITED_STATES")
        horizon = schema["definitions"]["capacity_horizon"]["properties"]
        self.assertEqual(horizon["start"]["const"], "ENTRY_DATE")
        self.assertEqual(horizon["end"]["const"], "END_OF_YEAR_5")
        calculation = schema["definitions"]["capacity_calculation"]["properties"]
        self.assertEqual(calculation["measure"]["const"], "MAXIMUM_TARGET_COUNT")
        self.assertEqual(
            calculation["aggregation"]["const"], "NON_DUPLICATIVE_TARGET_COUNT"
        )
        self.assertEqual(
            schema["definitions"]["deal_capacity_selection"]["allOf"][1]
            ["properties"]["capacity_type"]["const"],
            "DEAL_EXECUTION",
        )
        self.assertEqual(
            schema["definitions"]["integration_capacity_selection"]["allOf"][1]
            ["properties"]["capacity_type"]["const"],
            "INTEGRATION_ONBOARDING",
        )
        state = schema["definitions"]["normalized_state"]["properties"]
        for dimension in (
            "accounting", "size", "service_mix", "customer_concentration",
            "management_depth", "platform_quality",
        ):
            self.assertIn("HOLD_ENTRY_REFERENCE", state[dimension]["enum"])
        channels = schema["definitions"]["multiple_adjustment"]["properties"]["channel"]["enum"]
        self.assertEqual(len(channels), 3)
        anchor_basis = schema["definitions"]["anchor_basis"]["properties"]
        self.assertEqual(
            anchor_basis["channel"]["const"],
            "ENTRY_EQUIVALENT_COMPARABLE_MULTIPLE_LEVEL",
        )
        self.assertEqual(anchor_basis["state_reference"]["const"], "ENTRY_TARGET_ARCHETYPE")
        self.assertEqual(anchor_basis["scenario_policy"]["const"], "ONE_STATE_LOW_BASE_HIGH")
        assertions = schema["definitions"]["fixed_base_assertions"]["properties"]
        self.assertEqual(assertions["index_method"]["const"], "FIXED_BASE_LASPEYRES_CVA")
        self.assertEqual(
            assertions["basket_scope"]["const"], "EXHAUSTIVE_BASELINE_SERVICES_ONLY"
        )

    def test_runtime_placeholders_are_exact_and_unique(self):
        found = assemble.PLACEHOLDER_RE.findall(self.template)
        for placeholder in assemble.RUNTIME_PLACEHOLDERS:
            self.assertEqual(found.count(placeholder), 1)
        duplicate = "\n".join(sorted(assemble.RUNTIME_PLACEHOLDERS)) + "\n{{MODEL_ID}}"
        with self.assertRaisesRegex(assemble.AssembleError, "exactly once"):
            assemble.validate_prompt_text("541512", duplicate, exact_runtime=True)

    def test_instruction_surfaces_cover_new_constructs_without_leakage(self):
        required = (
            "controllable value-added", "pass-through", "r1", "r5", "k0", "k5",
            "c1", "c5", "sale availability", "access/win", "normalized_y5_operating_state",
            "h =", "ASSUMPTION", "MISSING", "UNPROVEN",
            "recognized_revenue", "accounting_basis",
            "validation_source_ids_disjoint_from_primary_support",
            "pass_through_reconciliation", "deal_execution_capacity_5y",
            "integration_onboarding_capacity_5y", "capacity_scope",
            "FIXED_BASE_LASPEYRES_CVA", "EXHAUSTIVE_BASELINE_SERVICES_ONLY",
            "HOLD_ENTRY_REFERENCE", "ENTRY_TARGET_ARCHETYPE",
            "ONE_STATE_LOW_BASE_HIGH", "NO_SPONSOR_TRANSFORMATION",
            "EXTERNAL_DISCOUNT_RATE_ENVIRONMENT",
            "ENTRY_EQUIVALENT_COMPARABLE_MULTIPLE_LEVEL",
            "PRIVATE_TRANSACTION_LIQUIDITY", "neutral kind `target`",
            "ACCRUAL_RECOGNIZED_REVENUE", "TRAILING_TWELVE_MONTHS",
            "pass_through_presentation", "capacity_type", "capacity_horizon",
            "capacity_calculation", "DEAL_EXECUTION", "INTEGRATION_ONBOARDING",
            "MAXIMUM_TARGET_COUNT", "NON_DUPLICATIVE_TARGET_COUNT",
            "anchor.anchor_basis", "point-identified", "low = base = high",
            "range.low = value = range.high",
            "No ordering is imposed on `r1` through `r5`",
            "five-year r interval box", "at most 32 distinct box vertices",
            "convex hull",
            "incompatible low-I/low-C or high-I/high-C bundles",
        )
        combined = "\n".join((self.template, self.runner, self.validator))
        for phrase in required:
            self.assertIn(phrase, combined)
        for label, text in (("template", self.template), ("runner", self.runner), ("validator", self.validator)):
            assemble.semantic_lint_v4_2_spec(label, text, label)
        for code in assemble.CANARY_V4_2_CODES:
            self.assertNotIn(code, combined)

    def test_prompt_contract_markers_fail_closed(self):
        assemble.validate_v4_2_prompt_contract("TEMPLATE", self.template)
        for marker in assemble.V4_2_PROMPT_CONTRACT_MARKERS:
            with self.subTest(marker=marker), self.assertRaisesRegex(
                assemble.AssembleError, "missing v4.2 contract marker"
            ):
                assemble.validate_v4_2_prompt_contract(
                    "TEMPLATE", self.template.replace(marker, "REMOVED")
                )

    def test_private_guarded_write_instructions_are_preserved(self):
        for label, brief, kind in (
            ("runner", self.runner, "packet"),
            ("validator", self.validator, "review"),
        ):
            with self.subTest(label=label):
                normalized = " ".join(brief.split())
                self.assertIn("private temporary repository path", brief)
                self.assertTrue(
                    "private pipe FD" in brief
                    or "anonymous FIFO or Unix-socket FD" in normalized
                )
                self.assertIn(
                    "Regular files and directories are forbidden credential endpoints",
                    normalized,
                )
                self.assertIn("Direct writes to the planned", normalized)
                self.assertIn(f"artifact kind `{kind}`", normalized)
                for forbidden_sink in (
                    "repository file", "envelope", "artifact",
                    "command argument", "log", "response",
                ):
                    self.assertIn(forbidden_sink, brief)
        self.assertIn("private temporary record/memo paths", self.runner)

    def test_render_is_byte_identical_and_digest_pinned(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            specs = root / "pipeline/specs_v4_2"
            datasets = root / "pipeline/datasets/v4_2"
            specs.mkdir(parents=True)
            datasets.mkdir(parents=True)
            methodology = root / "V4_2_RUNTIME_METHODOLOGY.md"
            methodology.write_text("fixture methodology\n")
            methodology_sha = hashlib.sha256(methodology.read_bytes()).hexdigest()
            dataset_path = datasets / "541512.json"
            dataset_path.write_text(json.dumps(normalized_dataset(), sort_keys=True))
            dataset_sha = hashlib.sha256(dataset_path.read_bytes()).hexdigest()
            spec = fixture_spec(methodology_sha, dataset_sha)
            spec_path = specs / "541512.json"
            spec_path.write_text(json.dumps(spec, sort_keys=True))
            spec_sha = hashlib.sha256(spec_path.read_bytes()).hexdigest()
            with mock.patch.object(assemble, "REPO", root), mock.patch.object(
                assemble, "SPECS_V4_2_DIR", specs
            ):
                first = assemble.assemble_v4_2_one("541512", spec["title"], self.template)
                second = assemble.assemble_v4_2_one("541512", spec["title"], self.template)
        self.assertEqual(first, second)
        for digest in (methodology_sha, dataset_sha, spec_sha):
            self.assertIn(digest, first)
        self.assertEqual(set(assemble.PLACEHOLDER_RE.findall(first)), assemble.RUNTIME_PLACEHOLDERS)

    def test_methodology_and_dataset_digest_mismatches_fail_closed(self):
        for field in ("methodology_snapshot", "dataset_snapshot"):
            with self.subTest(field=field), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                specs = root / "pipeline/specs_v4_2"
                datasets = root / "pipeline/datasets/v4_2"
                specs.mkdir(parents=True)
                datasets.mkdir(parents=True)
                method = root / "V4_2_RUNTIME_METHODOLOGY.md"
                method.write_text("method\n")
                dataset_path = datasets / "541512.json"
                dataset_path.write_text(json.dumps(normalized_dataset()))
                spec = fixture_spec(
                    hashlib.sha256(method.read_bytes()).hexdigest(),
                    hashlib.sha256(dataset_path.read_bytes()).hexdigest(),
                )
                spec[field]["sha256"] = "f" * 64
                (specs / "541512.json").write_text(json.dumps(spec))
                with mock.patch.object(assemble, "REPO", root), mock.patch.object(
                    assemble, "SPECS_V4_2_DIR", specs
                ):
                    with self.assertRaisesRegex(assemble.AssembleError, "digest mismatch"):
                        assemble.assemble_v4_2_one("541512", spec["title"], self.template)

    def test_v42_spec_and_dataset_duplicate_json_keys_fail_closed(self):
        for duplicate_target in ("spec", "dataset"):
            with self.subTest(duplicate_target=duplicate_target), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                specs = root / "pipeline/specs_v4_2"
                datasets = root / "pipeline/datasets/v4_2"
                specs.mkdir(parents=True)
                datasets.mkdir(parents=True)
                method = root / "V4_2_RUNTIME_METHODOLOGY.md"
                method.write_text("method\n")
                dataset = normalized_dataset()
                dataset_text = json.dumps(dataset, sort_keys=True)
                if duplicate_target == "dataset":
                    dataset_text = dataset_text[:-1] + ', "naics": "541512"}'
                dataset_path = datasets / "541512.json"
                dataset_path.write_text(dataset_text)
                spec = fixture_spec(
                    hashlib.sha256(method.read_bytes()).hexdigest(),
                    hashlib.sha256(dataset_path.read_bytes()).hexdigest(),
                )
                spec_text = json.dumps(spec, sort_keys=True)
                if duplicate_target == "spec":
                    spec_text = spec_text[:-1] + ', "naics": "541512"}'
                (specs / "541512.json").write_text(spec_text)
                with mock.patch.object(assemble, "REPO", root), mock.patch.object(
                    assemble, "SPECS_V4_2_DIR", specs
                ):
                    with self.assertRaisesRegex(assemble.AssembleError, "duplicate JSON key 'naics'"):
                        assemble.assemble_v4_2_one("541512", spec["title"], self.template)

    def test_strict_json_is_scoped_to_v42(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "duplicate.json"
            path.write_text('{"value": 1, "value": 2}')
            self.assertEqual(assemble._read_json("LEGACY", path, "legacy"), {"value": 2})
            with self.assertRaisesRegex(assemble.AssembleError, "duplicate JSON key 'value'"):
                assemble._read_json("V42", path, "v4.2", strict_v4_2=True)

    def test_value_basis_schema_and_semantics_are_fail_closed(self):
        spec = fixture_spec()
        assemble.validate_industry_spec_v4_2(spec["naics"], spec["title"], spec)
        cases = []
        duplicate_cost = copy.deepcopy(spec)
        duplicate_cost["value_basis"]["controllable_contractor_cash_cost_id"] = "employee-cash"
        cases.append(duplicate_cost)
        bad_sum = copy.deepcopy(spec)
        bad_sum["value_basis"]["roles"][0]["role_cash_cost_weight"] = 0.9
        cases.append(bad_sum)
        duplicate_pass = copy.deepcopy(spec)
        duplicate_pass["value_basis"]["approved_pass_through_categories"] *= 2
        cases.append(duplicate_pass)
        no_method = copy.deepcopy(spec)
        no_method["value_basis"]["roles"][0].pop("method")
        cases.append(no_method)
        duplicate_title = copy.deepcopy(spec)
        duplicate_title["value_basis"]["roles"][0]["role_cash_cost_weight"] = 0.5
        second_role = copy.deepcopy(duplicate_title["value_basis"]["roles"][0])
        second_role["role_id"] = "delivery-two"
        duplicate_title["value_basis"]["roles"].append(second_role)
        cases.append(duplicate_title)
        for broken in cases:
            with self.subTest(broken=broken["value_basis"]), self.assertRaises(assemble.AssembleError):
                assemble.validate_industry_spec_v4_2(broken["naics"], broken["title"], broken)

    def test_source_namespaces_are_disjoint_and_collision_fails_first(self):
        spec = fixture_spec()
        assemble.validate_industry_spec_v4_2(spec["naics"], spec["title"], spec)
        spec["value_basis"]["sources"][0]["id"] = "A1"
        spec["value_basis"]["roles"][0]["source_ids"] = ["A1"]
        with self.assertRaisesRegex(assemble.AssembleError, "namespaces collide: A1"):
            assemble.validate_industry_spec_v4_2(spec["naics"], spec["title"], spec)

    def test_duplicate_role_titles_fail_closed(self):
        spec = fixture_spec()
        spec["value_basis"]["roles"][0]["role_cash_cost_weight"] = 0.5
        second_role = copy.deepcopy(spec["value_basis"]["roles"][0])
        second_role["role_id"] = "delivery-two"
        spec["value_basis"]["roles"].append(second_role)
        with self.assertRaisesRegex(assemble.AssembleError, "unique role titles"):
            assemble.validate_industry_spec_v4_2(spec["naics"], spec["title"], spec)

    def test_only_runtime_methodology_is_model_visible(self):
        spec = fixture_spec()
        assemble.validate_industry_spec_v4_2(spec["naics"], spec["title"], spec)
        spec["methodology_snapshot"]["path"] = "V4_2_METHODOLOGY.md"
        with self.assertRaisesRegex(assemble.AssembleError, "schema validation failed"):
            assemble.validate_industry_spec_v4_2(spec["naics"], spec["title"], spec)

    def test_assumption_basis_is_prefrozen_source_free_and_unproven(self):
        spec = fixture_spec()
        basis = spec["value_basis"]
        basis["mode"] = "assumption"
        basis["sources"] = []
        basis["roles"][0].update({
            "method": "ESTIMATE", "evidence_quality": "NONE", "source_ids": [],
        })
        basis["rationale"] = "Pre-frozen source-free bounded role taxonomy."
        assemble.validate_industry_spec_v4_2(spec["naics"], spec["title"], spec)

        sourced = copy.deepcopy(spec)
        sourced["value_basis"]["sources"] = [{
            "id": "B1", "url": "https://example.com/basis",
            "title": "Basis source", "vintage": "2026",
        }]
        sourced["value_basis"]["roles"][0]["source_ids"] = ["B1"]
        with self.assertRaises(assemble.AssembleError):
            assemble.validate_industry_spec_v4_2(sourced["naics"], sourced["title"], sourced)

        measured = copy.deepcopy(spec)
        measured["value_basis"]["roles"][0]["method"] = "OBSERVED"
        measured["value_basis"]["roles"][0]["evidence_quality"] = "MED"
        with self.assertRaises(assemble.AssembleError):
            assemble.validate_industry_spec_v4_2(measured["naics"], measured["title"], measured)

        for text in (self.template, self.runner, self.validator):
            self.assertIn("UNPROVEN", text)
            self.assertIn("source-free", text)

    def test_leakage_lint_rejects_outcome_and_benchmark_hints(self):
        examples = (
            "This is in the golden set.", "winner label", "expected verdict: strong",
            "target tier is pass", "expected score = 8", "decision: avoid",
            "deep dive", "red industry outcome", "benchmark membership",
            "campaign scope", "class labels", "scope_class", "holdout",
            "canary", "regression",
        )
        for text in examples:
            with self.subTest(text=text), self.assertRaises(assemble.AssembleError):
                assemble.semantic_lint_v4_2_spec("999999", text)
        assemble.semantic_lint_v4_2_spec(
            "999999",
            "Use strong evidence, avoid double counting, and encode no expected outcome.",
        )

    def test_exact_canary_and_holdout_membership_and_missing_specs(self):
        entries = [{"naics": code, "title": code} for code in sorted(
            assemble.CANARY_V4_2_CODES | {"541890", "541340", "541370", "541199", "541420"}
        )]
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            specs = root / "specs"
            specs.mkdir()
            regression = root / "regression.json"
            regression.write_text(json.dumps({
                "membership_version": assemble.REGRESSION_V4_2_VERSION,
                "selected_codes": sorted(assemble.CANARY_V4_2_CODES),
            }))
            methodology = root / "V4_2_METHODOLOGY.md"
            methodology.write_text("method\n")
            holdout_codes = ["541890", "541340", "541370", "541199", "541420"]
            holdout = root / "holdout.json"
            holdout.write_text(json.dumps({
                "version": assemble.HOLDOUT_V4_2_VERSION,
                "selected_codes": holdout_codes,
                "bins": [{"selected_naics": code} for code in holdout_codes],
                "source_digests": [{
                    "path": "V4_2_METHODOLOGY.md",
                    "sha256": hashlib.sha256(methodology.read_bytes()).hexdigest(),
                }],
            }))
            patches = (
                mock.patch.object(assemble, "SPECS_V4_2_DIR", specs),
                mock.patch.object(assemble, "REGRESSION_V4_2_MEMBERSHIP_PATH", regression),
                mock.patch.object(assemble, "HOLDOUT_V4_2_MEMBERSHIP_PATH", holdout),
                mock.patch.object(assemble, "GOVERNANCE_METHODOLOGY_V4_2_PATH", methodology),
            )
            with patches[0], patches[1], patches[2], patches[3]:
                with self.assertRaisesRegex(assemble.AssembleError, "exactly 63"):
                    assemble._v4_2_entries(entries, "full")
                with self.assertRaisesRegex(assemble.AssembleError, "missing required canary"):
                    assemble._v4_2_entries(entries, "canary")
                for code in assemble.CANARY_V4_2_CODES:
                    (specs / f"{code}.json").write_text("{}")
                selected, missing = assemble._v4_2_entries(entries, "canary")
                self.assertEqual([item["naics"] for item in selected], sorted(assemble.CANARY_V4_2_CODES))
                self.assertEqual(missing, [])
                for code in holdout_codes:
                    (specs / f"{code}.json").write_text("{}")
                selected, _ = assemble._v4_2_entries(entries, "holdout")
                self.assertEqual([item["naics"] for item in selected], sorted(holdout_codes))

    def test_main_rejects_partial_v42_before_assembly(self):
        with self.assertRaises(SystemExit):
            assemble.main(["--template-version", "4.2", "--scope", "canary", "--allow-partial"])


if __name__ == "__main__":
    unittest.main()
