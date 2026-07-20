#!/usr/bin/env python3
"""Focused v3.1.1 prompt, assembly and validator-binding tests.

These tests render prompts in memory only. They do not create campaign artifacts.
"""

import hashlib
import importlib.util
import json
import os
from pathlib import Path
import unittest


HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


assemble = load_module(
    "assemble_v311_prompt_tests", HERE / "assemble_prompts.py"
)


class V311PromptLayerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.template_path = (
            REPO / "pipeline" / "template" / "prompt_template_v3_1_1.md"
        )
        cls.runner_path = (
            REPO / "pipeline" / "template" / "runner_brief_v3_1_1.md"
        )
        cls.validator_path = (
            REPO / "pipeline" / "template" / "validator_brief_v3_1_1.md"
        )
        cls.template = cls.template_path.read_text(encoding="utf-8")
        cls.runner = cls.runner_path.read_text(encoding="utf-8")
        cls.validator = cls.validator_path.read_text(encoding="utf-8")

    def test_version_routing_is_explicit_and_separate(self):
        route = assemble.VERSION_PATHS["3.1.1"]
        self.assertEqual(route["template"], self.template_path)
        self.assertEqual(
            route["prompts"], REPO / "pipeline" / "prompts_v3_1_1"
        )
        self.assertNotEqual(route["template"], assemble.VERSION_PATHS["3.1"]["template"])
        self.assertNotEqual(route["prompts"], assemble.VERSION_PATHS["3.1"]["prompts"])

    def test_template_binds_schema_and_python_owned_fields(self):
        required = (
            "research_draft_v3_1_1.schema.json",
            '"template_version": "3.1.1"',
            "do **not** author final provenance",
            "role weights",
            "role contributions",
            "factor scores",
            "uplift",
            "verdict",
        )
        for phrase in required:
            self.assertIn(phrase, self.template)

    def test_template_preserves_c1_c4_and_method_boundary(self):
        for marker in ("C1", "C2", "C3", "C4"):
            self.assertIn(marker, self.template)
        for method in ("OBSERVED", "CALCULATED", "ESTIMATE"):
            self.assertIn(method, self.template)
        self.assertIn("A cited background fact does not turn an estimate", self.template)
        self.assertIn("Any judgmental mapping makes this method invalid", self.template)
        self.assertIn("every starting fact ID", self.template)
        self.assertIn("explicit judgmental step", self.template)
        self.assertIn("not reported", self.template)
        self.assertIn("Unicode (`…`) ellipses are forbidden", self.template)

    def test_template_requires_complete_final_self_audit(self):
        for phrase in (
            "Enumerate every `evidence_facts[].url`",
            "Enumerate every fact ID",
            "For every selected input",
            "For every `OBSERVED` selection",
            "For every `CALCULATED` selection",
            "For every judgmental bridge",
            "succession_shortage_documented",
        ):
            self.assertIn(phrase, self.template)

    def test_runner_binds_models_isolation_and_plain_python(self):
        for phrase in (
            "gpt-5.6-terra",
            "gpt-5.6-sol",
            "at most two codes",
            "may not delegate",
            "Do NOT spawn",
            "research_draft_v3_1_1.schema.json",
            "finalize_run_v3_1_1.py",
            "Never use --force",
            "build.source_audit_pairs()",
            "complete structured estimate_basis",
        ):
            self.assertIn(phrase, self.runner)

    def test_validator_binds_full_depth_sol_and_existing_schema(self):
        for phrase in (
            "gpt-5.6-sol",
            "full depth",
            "validator-3.1.1",
            "review_record.schema.json",
            "OBSERVED: verify directly",
            "CALCULATED: verify every operand",
            "ESTIMATE: require a complete structured estimate_basis",
            "source support the atomic fact",
            "terminal-value logic",
            "Return accepted",
            "Return wrong",
            "Every wrong verdict must also set the corresponding review check",
            "succession_shortage_documented directly",
        ):
            self.assertIn(phrase, self.validator)

    def test_all_target_prompts_render_twice_byte_identically_in_memory(self):
        targets = json.loads(assemble.TARGETS_PATH.read_text(encoding="utf-8"))
        rendered_first = {}
        rendered_second = {}
        for entry in targets["codes"]:
            naics = entry["naics"]
            title = entry["title"]
            first = assemble.assemble_one(naics, title, self.template, "3.1.1")
            second = assemble.assemble_one(naics, title, self.template, "3.1.1")
            assemble.validate_prompt_text(naics, first)
            assemble.validate_prompt_text(naics, second)
            rendered_first[naics] = first.encode("utf-8")
            rendered_second[naics] = second.encode("utf-8")
        self.assertEqual(len(rendered_first), 63)
        self.assertEqual(set(rendered_first), set(rendered_second))
        self.assertEqual(rendered_first, rendered_second)
        self.assertEqual(
            set(assemble.RUNTIME_PLACEHOLDERS),
            set(assemble.PLACEHOLDER_RE.findall(rendered_first["524210"].decode())),
        )

    def test_null_dataset_rule_uses_v311_method_contract(self):
        rendered = assemble.render_dataset_inputs(
            "999999",
            {
                "research_gaps": [
                    {"input": "labor_share", "instruction": "Research the gap."}
                ]
            },
            {
                "labor_share": {"value": None},
                "role_mix": {"occupations": []},
                "n_total": {"value": 1},
                "n_band": {"value": 1},
            },
            "3.1.1",
        )
        self.assertIn("v3.1.1", rendered)
        self.assertIn("`OBSERVED`", rendered)
        self.assertIn("`CALCULATED`", rendered)
        self.assertIn("`ESTIMATE`", rendered)

    def test_frozen_v30_and_v31_prompt_artifacts_are_unchanged(self):
        expected = {
            "pipeline/template/prompt_template_v3.md": "57d1ff51afd7a74d02b9334e17b7cbf79f3151d372521df91b00618c2e9e82dd",
            "pipeline/template/prompt_template_v3_1.md": "b639675d4defe72b7741b1f7fc08805b94f1445eeb762108fb294920f3d6176e",
            "pipeline/template/runner_brief_v3_1.md": "40252013ec431c34c130766d72e89dd7dce29fa39a860bf8b3eeeafc305b023c",
            "pipeline/template/validator_brief_v3_1.md": "2925d96585114b0a01e4be31ae13e7f243f4f4af2e2cc2fcc8067d1ec96e1a64",
        }
        for relative, digest in expected.items():
            actual = hashlib.sha256((REPO / relative).read_bytes()).hexdigest()
            self.assertEqual(actual, digest, relative)


if __name__ == "__main__":
    unittest.main(verbosity=2)
