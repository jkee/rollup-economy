#!/usr/bin/env python3
"""Build and lint the scope-blind v4.2 runtime methodology derivative."""

import argparse
import json
from pathlib import Path
import re
import sys


REPO = Path(__file__).resolve().parent.parent.parent
SOURCE_PATH = "V4_2_METHODOLOGY.md"
OUTPUT_PATH = "V4_2_RUNTIME_METHODOLOGY.md"
SOURCE_TITLE = "# AI Roll-Up Map — v4.2 Methodology"
RUNTIME_TITLE = "# AI Roll-Up Map — v4.2 Runtime Methodology"
DERIVATION_NOTE = "<!-- Deterministically derived from Sections 1–11; do not edit. -->"
SECTION_RE = re.compile(r"^## ([0-9]+)\.\s+(.+)$")
REGRESSION_CODES = ("238220", "541214", "541511", "541512", "541930")
HOLDOUT_CODES = ("541890", "541340", "541370", "541199", "541420")
PRESELECTED_CODES = frozenset((*REGRESSION_CODES, *HOLDOUT_CODES))
CLASS_PATTERNS = (
    ("regression", re.compile(r"(?<![A-Za-z0-9])regression(?![A-Za-z0-9])", re.IGNORECASE)),
    ("holdout", re.compile(r"(?<![A-Za-z0-9])holdout(?![A-Za-z0-9])", re.IGNORECASE)),
    ("canary", re.compile(r"(?<![A-Za-z0-9])canary(?![A-Za-z0-9])", re.IGNORECASE)),
    ("golden", re.compile(r"(?<![A-Za-z0-9])golden(?![A-Za-z0-9])", re.IGNORECASE)),
    ("benchmark membership", re.compile(r"\bbenchmark[ _-]+membership\b", re.IGNORECASE)),
    ("campaign scope", re.compile(r"\bcampaign[ _-]+scope\b", re.IGNORECASE)),
    ("class label", re.compile(r"\bclass[ _-]+labels?\b", re.IGNORECASE)),
    ("scope class", re.compile(r"\bscope[_ -]?class\b", re.IGNORECASE)),
)
CLASS_VALUES = frozenset(("regression", "holdout", "canary", "golden", "fleet"))
SCOPE_CLASS_KEYS = frozenset((
    "scope", "campaign_scope", "benchmark_class", "class", "class_label",
))
VISIBLE_TEMPLATES = (
    "pipeline/template/prompt_template_v4_2.md",
    "pipeline/template/runner_brief_v4_2.md",
    "pipeline/template/validator_brief_v4_2.md",
)


class RuntimeMethodError(ValueError):
    """Raised when derivation or leakage lint fails closed."""


def _read_text(path):
    data = Path(path).read_bytes()
    if b"\r" in data:
        raise RuntimeMethodError("methodology must use canonical LF newlines")
    try:
        return data.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise RuntimeMethodError("methodology must be UTF-8") from exc


def _section_boundaries(text):
    lines = text.splitlines(keepends=True)
    if not lines or lines[0].rstrip("\n") != SOURCE_TITLE:
        raise RuntimeMethodError("unexpected v4.2 methodology title")
    headings = []
    for index, line in enumerate(lines):
        if index and line.startswith("# "):
            raise RuntimeMethodError("unexpected level-1 heading: %s" % line.rstrip())
        if line.startswith("## "):
            match = SECTION_RE.fullmatch(line.rstrip("\n"))
            if not match:
                raise RuntimeMethodError("unexpected level-2 heading: %s" % line.rstrip())
            headings.append((int(match.group(1)), index, match.group(2)))
    numbers = [number for number, _, _ in headings]
    if numbers != list(range(1, 16)):
        raise RuntimeMethodError("top-level methodology sections must be exactly 1 through 15")
    return lines, headings


def leakage_errors(text, label, allowed_naics=None):
    """Return benchmark-assignment leaks in one runner/reviewer-visible value."""
    errors = []
    allowed = {allowed_naics} if allowed_naics in PRESELECTED_CODES else set()
    found_codes = {code for code in PRESELECTED_CODES if re.search(
        r"(?<![0-9])%s(?![0-9])" % code, text
    )}
    leaked_codes = sorted(found_codes - allowed)
    if leaked_codes:
        errors.append("%s exposes other preselected NAICS codes: %s" % (label, leaked_codes))
    for name, pattern in CLASS_PATTERNS:
        if pattern.search(text):
            errors.append("%s exposes forbidden benchmark class token: %s" % (label, name))
    return errors


def identifier_errors(value, label):
    """Reject scope/class words embedded in supposedly opaque identifiers."""
    errors = []
    for token in CLASS_VALUES:
        pattern = re.compile(
            r"(?<![A-Za-z0-9])%s(?![A-Za-z0-9])" % re.escape(token), re.IGNORECASE
        )
        if pattern.search(value):
            errors.append("%s exposes forbidden class token: %s" % (label, token))
    return errors


def structured_visibility_errors(value, label):
    """Reject class-valued fields and leaky task identifiers recursively."""
    errors = []
    if isinstance(value, dict):
        for key, item in value.items():
            lowered_key = str(key).lower()
            if lowered_key in SCOPE_CLASS_KEYS:
                errors.append("%s.%s exposes forbidden scope/class field" %
                              (label, key))
            elif (lowered_key == "kind" and isinstance(item, str)
                    and item.lower() in CLASS_VALUES):
                errors.append("%s.%s exposes forbidden class value: %s" %
                              (label, key, item))
            if (isinstance(item, str)
                    and (lowered_key in ("run_id", "entry_id")
                         or lowered_key.endswith("task_path")
                         or lowered_key.endswith("task_id"))):
                errors.extend(identifier_errors(item, "%s.%s" % (label, key)))
            errors.extend(structured_visibility_errors(item, "%s.%s" % (label, key)))
    elif isinstance(value, list):
        for index, item in enumerate(value):
            errors.extend(structured_visibility_errors(item, "%s[%d]" % (label, index)))
    return errors


def derive_runtime_bytes(source_path=SOURCE_PATH):
    """Extract exactly Sections 1–11 from a structurally valid methodology."""
    text = _read_text(source_path)
    lines, headings = _section_boundaries(text)
    section_one = headings[0][1]
    section_twelve = headings[11][1]
    body = "".join(lines[section_one:section_twelve])
    if not body.endswith("\n"):
        body += "\n"
    errors = leakage_errors(body, "runtime methodology")
    if errors:
        raise RuntimeMethodError("; ".join(errors))
    runtime = RUNTIME_TITLE + "\n\n" + DERIVATION_NOTE + "\n\n" + body
    _runtime_structure(runtime)
    return runtime.encode("utf-8")


def _runtime_structure(text):
    lines = text.splitlines(keepends=True)
    if not lines or lines[0].rstrip("\n") != RUNTIME_TITLE:
        raise RuntimeMethodError("unexpected runtime methodology title")
    headings = []
    for index, line in enumerate(lines):
        if index and line.startswith("# "):
            raise RuntimeMethodError("unexpected runtime level-1 heading")
        if line.startswith("## "):
            match = SECTION_RE.fullmatch(line.rstrip("\n"))
            if not match:
                raise RuntimeMethodError("unexpected runtime level-2 heading")
            headings.append((int(match.group(1)), index, match.group(2)))
    if [number for number, _, _ in headings] != list(range(1, 12)):
        raise RuntimeMethodError("runtime methodology does not contain exactly Sections 1–11")
    return lines, headings


def write_or_check(source_path=SOURCE_PATH, output_path=OUTPUT_PATH, check=False):
    expected = derive_runtime_bytes(source_path)
    output = Path(output_path)
    if check:
        if output.read_bytes() != expected:
            raise RuntimeMethodError("runtime methodology differs from fresh derivation")
    else:
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_bytes(expected)
    return output


def visible_artifact_errors(root=REPO):
    """Lint on-disk runner/reviewer-visible methods, prompts, and envelopes."""
    root = Path(root)
    errors = []
    runtime = root / OUTPUT_PATH
    try:
        runtime_text = _read_text(runtime)
        _runtime_structure(runtime_text)
        errors.extend(leakage_errors(runtime_text, OUTPUT_PATH))
    except (OSError, RuntimeMethodError) as exc:
        errors.append("%s is invalid: %s" % (OUTPUT_PATH, exc))
    for relative in VISIBLE_TEMPLATES:
        path = root / relative
        try:
            errors.extend(leakage_errors(_read_text(path), relative))
        except (OSError, RuntimeMethodError) as exc:
            errors.append("%s is invalid: %s" % (relative, exc))
    prompt_dir = root / "pipeline/prompts_v4_2"
    for path in sorted(prompt_dir.glob("*.md")):
        code = path.stem if path.stem in PRESELECTED_CODES else None
        try:
            errors.extend(leakage_errors(
                _read_text(path), path.relative_to(root).as_posix(), allowed_naics=code,
            ))
        except (OSError, RuntimeMethodError) as exc:
            errors.append("%s is invalid: %s" % (path, exc))
    envelope_dir = root / "pipeline/v4_2/envelopes"
    for path in sorted(envelope_dir.rglob("*.json")) if envelope_dir.exists() else ():
        code = None
        try:
            value = json.loads(path.read_text(encoding="utf-8"))
            candidate = value.get("naics") if isinstance(value, dict) else None
            code = candidate if candidate in PRESELECTED_CODES else None
            text = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
            errors.extend(leakage_errors(
                text, path.relative_to(root).as_posix(), allowed_naics=code,
            ))
            errors.extend(structured_visibility_errors(
                value, path.relative_to(root).as_posix(),
            ))
        except (OSError, UnicodeError, json.JSONDecodeError) as exc:
            errors.append("visible envelope is invalid: %s: %s" % (path, exc))
    return errors


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", default=SOURCE_PATH)
    parser.add_argument("--output", default=OUTPUT_PATH)
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--lint-visible", action="store_true")
    parser.add_argument("--repo-root", default=str(REPO))
    args = parser.parse_args(argv)
    root = Path(args.repo_root).resolve()
    source = Path(args.source)
    if not source.is_absolute():
        source = root / source
    output = Path(args.output)
    if not output.is_absolute():
        output = root / output
    try:
        result = write_or_check(source, output, check=args.check)
        if args.lint_visible:
            errors = visible_artifact_errors(root)
            if errors:
                raise RuntimeMethodError("; ".join(errors))
        print("OK: %s v4.2 runtime methodology: %s" %
              ("verified" if args.check else "wrote", result))
        return 0
    except (OSError, UnicodeError, RuntimeMethodError) as exc:
        print("V4.2 RUNTIME METHODOLOGY FAILED: %s" % exc, file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
