#!/usr/bin/env python3
"""Tests for the scope-blind v4.2 runtime-methodology derivative."""

import importlib.util
import json
from pathlib import Path
import tempfile
import unittest


HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location(
    "runtime_methodology_v4_2_tests", HERE / "build_runtime_methodology_v4_2.py"
)
runtime = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(runtime)


def source_text(section_body="Economic content.", governance_body="Governance content."):
    parts = [runtime.SOURCE_TITLE, "", "Outcome-blind preamble may name a holdout.", ""]
    for number in range(1, 16):
        parts.extend(("## %d. Section %d" % (number, number), ""))
        parts.append(section_body if number < 12 else governance_body)
        parts.append("")
        if number == 3:
            parts.extend(("### Permitted economic subsection", "", "Details.", ""))
    return "\n".join(parts).rstrip() + "\n"


class RuntimeMethodologyV42Tests(unittest.TestCase):
    def test_extracts_exact_sections_one_through_eleven(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "source.md"
            source.write_text(source_text(), encoding="utf-8")
            result = runtime.derive_runtime_bytes(source).decode()
            self.assertTrue(result.startswith(runtime.RUNTIME_TITLE + "\n"))
            self.assertIn("## 1. Section 1", result)
            self.assertIn("## 11. Section 11", result)
            self.assertNotIn("## 12.", result)
            self.assertNotIn("Outcome-blind preamble", result)

    def test_governance_cohort_words_after_section_eleven_are_not_exposed(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "source.md"
            source.write_text(
                source_text(governance_body="holdout regression 238220 541890"),
                encoding="utf-8",
            )
            result = runtime.derive_runtime_bytes(source).decode()
            self.assertEqual([], runtime.leakage_errors(result, "runtime"))

    def test_cohort_word_inside_runtime_sections_fails_closed(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "source.md"
            source.write_text(source_text(section_body="Secret holdout assignment."), encoding="utf-8")
            with self.assertRaisesRegex(runtime.RuntimeMethodError, "holdout"):
                runtime.derive_runtime_bytes(source)

    def test_unexpected_or_missing_top_level_heading_fails(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "source.md"
            source.write_text(source_text().replace("## 8.", "## Appendix."), encoding="utf-8")
            with self.assertRaisesRegex(runtime.RuntimeMethodError, "unexpected level-2"):
                runtime.derive_runtime_bytes(source)

            source.write_text(source_text().replace("## 8. Section 8\n\nEconomic content.\n\n", ""), encoding="utf-8")
            with self.assertRaisesRegex(runtime.RuntimeMethodError, "exactly 1 through 15"):
                runtime.derive_runtime_bytes(source)

            source.write_text(source_text().replace("## 8.", "# Hidden replacement\n\n## 8."), encoding="utf-8")
            with self.assertRaisesRegex(runtime.RuntimeMethodError, "unexpected level-1"):
                runtime.derive_runtime_bytes(source)

    def test_write_and_check_are_byte_deterministic(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "source.md"
            output = Path(directory) / "runtime.md"
            source.write_text(source_text(), encoding="utf-8")
            runtime.write_or_check(source, output)
            first = output.read_bytes()
            runtime.write_or_check(source, output, check=True)
            self.assertEqual(first, runtime.derive_runtime_bytes(source))
            output.write_bytes(first + b"tamper\n")
            with self.assertRaisesRegex(runtime.RuntimeMethodError, "fresh derivation"):
                runtime.write_or_check(source, output, check=True)

    def test_visible_lint_allows_only_the_entry_own_preselected_code(self):
        own = "Research 541890 only."
        self.assertEqual([], runtime.leakage_errors(own, "prompt", allowed_naics="541890"))
        errors = runtime.leakage_errors(
            own + " Compare 541340.", "prompt", allowed_naics="541890"
        )
        self.assertTrue(any("other preselected" in error for error in errors))

    def test_visible_lint_rejects_scope_and_class_tokens(self):
        for token in (
            "regression", "holdout", "canary", "golden",
            "benchmark membership", "campaign scope", "class labels", "scope_class",
        ):
            with self.subTest(token=token):
                self.assertTrue(runtime.leakage_errors(token, "visible"))
        self.assertTrue(runtime.identifier_errors("/root/research_fleet_a1", "task"))
        self.assertTrue(runtime.structured_visibility_errors(
            {"scope": "opaque", "review_task_id": "review_holdout_a1"}, "visible",
        ))

    def test_visible_artifact_tree_checks_prompts_envelopes_and_task_ids(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / runtime.SOURCE_PATH
            source.write_text(source_text(), encoding="utf-8")
            runtime.write_or_check(source, root / runtime.OUTPUT_PATH)
            for relative in runtime.VISIBLE_TEMPLATES:
                path = root / relative
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text("Isolated target instructions.\n", encoding="utf-8")
            prompt = root / "pipeline/prompts_v4_2/541890.md"
            prompt.parent.mkdir(parents=True, exist_ok=True)
            prompt.write_text("Research 541890.\n", encoding="utf-8")
            envelope = root / "pipeline/v4_2/envelopes/opaque.json"
            envelope.parent.mkdir(parents=True, exist_ok=True)
            envelope.write_text(json.dumps({
                "naics": "541890", "kind": "target",
                "codex_task_path": "/root/research_v4_2_a1b2c3_a1",
            }), encoding="utf-8")
            self.assertEqual([], runtime.visible_artifact_errors(root))
            envelope.write_text(json.dumps({
                "naics": "541890", "kind": "fleet",
                "codex_task_path": "/root/research_holdout_a1",
            }), encoding="utf-8")
            errors = runtime.visible_artifact_errors(root)
            self.assertTrue(any("fleet" in error for error in errors))
            self.assertTrue(any("holdout" in error for error in errors))

    def test_current_full_methodology_derives_without_governance_sections(self):
        derived = runtime.derive_runtime_bytes(runtime.REPO / runtime.SOURCE_PATH).decode()
        self.assertIn("## 11. Frozen synthetic sentinels", derived)
        self.assertNotIn("## 12. Development regression campaign", derived)
        self.assertNotIn("## 15. Freeze manifest", derived)

    def test_industry_spec_schema_exposes_only_runtime_methodology(self):
        schema_path = runtime.REPO / "pipeline/build/schemas/industry_spec_v4_2.schema.json"
        schema = json.loads(schema_path.read_text(encoding="utf-8"))
        snapshot_path = schema["properties"]["methodology_snapshot"]["properties"]["path"]
        self.assertEqual({"const": runtime.OUTPUT_PATH}, snapshot_path)


if __name__ == "__main__":
    unittest.main(verbosity=2)
