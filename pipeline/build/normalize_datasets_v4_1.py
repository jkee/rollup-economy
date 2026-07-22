#!/usr/bin/env python3
"""Normalize the frozen 63-code legacy dataset into the v4.1 schema.

This is a structural translation only.  In particular, occupation identities
and shares are copied verbatim, null values remain null, and no missing value
is inferred.  ``--check`` rebuilds every record in memory and requires the
checked-in output set to be byte-identical.
"""

import argparse
import hashlib
import importlib.util
import json
import math
import re
import sys
from pathlib import Path


HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
DEFAULT_TARGETS = REPO / "pipeline" / "blocks" / "targets_phase3.json"
DEFAULT_INPUT_DIR = REPO / "pipeline" / "datasets" / "derived"
DEFAULT_OUTPUT_DIR = REPO / "pipeline" / "datasets" / "v4_1"
SCHEMA_PATH = HERE / "schemas" / "dataset_v4_1.schema.json"
DERIVATION_VERSION = "normalize-v4.1-1"
DATASET_VERSION = "4.1"
EXPECTED_CODE_COUNT = 63
QUALITY_MAP = {
    "HIGH": "HIGH",
    "MED": "MED",
    "LOW": "LOW",
    "NONE": "NONE",
    "ESTIMATE": "LOW",
}
SOC_RE = re.compile(r"^[0-9]{2}-[0-9]{4}$")
CODE_RE = re.compile(r"^[0-9]{6}$")
SHARE_TOLERANCE = 1e-9


class NormalizeError(ValueError):
    """Raised when a legacy source or normalized output is invalid."""


def _load_schema_validator():
    spec = importlib.util.spec_from_file_location("dataset_v4_1_schema_validator", HERE / "build.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


schema_validator = _load_schema_validator()


def _reject_constant(value):
    raise NormalizeError("non-standard JSON constant %r is forbidden" % value)


def _reject_duplicate_keys(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise NormalizeError("duplicate JSON key %r" % key)
        result[key] = value
    return result


def load_json(path):
    try:
        with Path(path).open("r", encoding="utf-8") as handle:
            return json.load(
                handle,
                parse_constant=_reject_constant,
                object_pairs_hook=_reject_duplicate_keys,
            )
    except FileNotFoundError as exc:
        raise NormalizeError("JSON file not found: %s" % path) from exc
    except json.JSONDecodeError as exc:
        raise NormalizeError("invalid JSON in %s: %s" % (path, exc)) from exc


def sha256_file(path):
    digest = hashlib.sha256()
    try:
        with Path(path).open("rb") as handle:
            for chunk in iter(lambda: handle.read(65536), b""):
                digest.update(chunk)
    except FileNotFoundError as exc:
        raise NormalizeError("source file not found: %s" % path) from exc
    return digest.hexdigest()


def serialized_bytes(value):
    return (json.dumps(value, indent=2, ensure_ascii=False, allow_nan=False) + "\n").encode("utf-8")


def _is_number(value):
    return (
        isinstance(value, (int, float))
        and not isinstance(value, bool)
        and math.isfinite(float(value))
    )


def _require_object(value, label):
    if not isinstance(value, dict):
        raise NormalizeError("%s must be an object" % label)
    return value


def _require_string(value, label, allow_empty=False):
    if not isinstance(value, str) or (not allow_empty and not value.strip()):
        raise NormalizeError("%s must be %sa non-empty string" % (
            label, "" if not allow_empty else "a string or "))
    return value


def _quality(value, label):
    try:
        return QUALITY_MAP[value]
    except (KeyError, TypeError) as exc:
        raise NormalizeError("%s has unsupported legacy quality %r" % (label, value)) from exc


def _share(value, label, nullable=False):
    if value is None and nullable:
        return None
    if not _is_number(value) or not 0 <= float(value) <= 1:
        raise NormalizeError("%s must be a finite share from 0 to 1%s" % (
            label, " or null" if nullable else ""))
    return value


def _count(value, label, nullable=False):
    if value is None and nullable:
        return None
    if not isinstance(value, int) or isinstance(value, bool) or value < 0:
        raise NormalizeError("%s must be a non-negative integer%s" % (
            label, " or null" if nullable else ""))
    return value


def _legacy_vintage(source):
    """Compose provenance only from the legacy year fields, preserving order."""
    years = []
    for label, section in (("labor_share.year", "labor_share"), ("n_total.year", "n_total")):
        year = _require_string(source[section].get("year"), label, allow_empty=True).strip()
        if year and year not in years:
            years.append(year)
    if not years:
        raise NormalizeError("legacy labor_share.year and n_total.year are both empty")
    return " | ".join(years)


def validate_legacy(source, expected_code=None, expected_title=None):
    source = _require_object(source, "legacy dataset")
    required = {"naics", "title", "labor_share", "n_total", "n_band", "role_mix"}
    missing = sorted(required - set(source))
    if missing:
        raise NormalizeError("legacy dataset missing fields: %s" % ", ".join(missing))

    code = _require_string(source["naics"], "legacy naics")
    title = _require_string(source["title"], "legacy title")
    if not CODE_RE.fullmatch(code):
        raise NormalizeError("legacy naics must contain exactly six digits")
    if expected_code is not None and code != expected_code:
        raise NormalizeError("legacy naics %s does not match target %s" % (code, expected_code))
    if expected_title is not None and title != expected_title:
        raise NormalizeError("legacy title for %s differs from target membership" % code)

    labor = _require_object(source["labor_share"], "labor_share")
    labor_value = labor.get("value")
    if labor_value is not None and (not _is_number(labor_value) or float(labor_value) < 0):
        raise NormalizeError("labor_share.value must be a finite non-negative number or null")
    _quality(labor.get("quality"), "labor_share")
    _require_string(labor.get("method"), "labor_share.method")
    _require_string(labor.get("year"), "labor_share.year", allow_empty=True)

    total = _require_object(source["n_total"], "n_total")
    _count(total.get("value"), "n_total.value")
    _quality(total.get("quality"), "n_total")
    _require_string(total.get("source"), "n_total.source")
    _require_string(total.get("year"), "n_total.year", allow_empty=True)

    band = _require_object(source["n_band"], "n_band")
    band_value = _count(band.get("value"), "n_band.value", nullable=True)
    _quality(band.get("quality"), "n_band")
    _require_string(band.get("derivation"), "n_band.derivation")
    if band_value is not None and band_value > total["value"]:
        raise NormalizeError("n_band.value may not exceed n_total.value")

    role_mix = _require_object(source["role_mix"], "role_mix")
    _require_string(role_mix.get("oews_level"), "role_mix.oews_level")
    _quality(role_mix.get("quality"), "role_mix")
    occupations = role_mix.get("occupations")
    if not isinstance(occupations, list) or not occupations:
        raise NormalizeError("role_mix.occupations must be a non-empty array")
    seen = set()
    for index, occupation in enumerate(occupations):
        item = _require_object(occupation, "role_mix.occupations[%d]" % index)
        required_role = {"soc", "title", "emp_share", "wage_share"}
        if set(item) != required_role:
            raise NormalizeError(
                "role_mix.occupations[%d] must contain exactly %s" %
                (index, ", ".join(sorted(required_role)))
            )
        soc = _require_string(item["soc"], "role_mix.occupations[%d].soc" % index)
        if not SOC_RE.fullmatch(soc):
            raise NormalizeError("invalid SOC identity %r" % soc)
        if soc in seen:
            raise NormalizeError("duplicate legacy SOC identity %s" % soc)
        seen.add(soc)
        _require_string(item["title"], "role_mix.occupations[%d].title" % index)
        _share(item["emp_share"], "role_mix.occupations[%d].emp_share" % index)
        _share(item["wage_share"], "role_mix.occupations[%d].wage_share" % index)
    for field in ("emp_share", "wage_share"):
        if sum(float(item[field]) for item in occupations) > 1 + SHARE_TOLERANCE:
            raise NormalizeError("legacy role_mix %s sum exceeds 1" % field)
    _legacy_vintage(source)
    return source


def validate_output(value):
    schema = load_json(SCHEMA_PATH)
    errors = schema_validator.schema_errors(value, schema, schema)
    if errors:
        raise NormalizeError("normalized dataset schema errors: %s" % "; ".join(errors))

    roles = value["role_mix"]["occupations"]
    if len({item["soc"] for item in roles}) != len(roles):
        raise NormalizeError("normalized role_mix SOC identities must be unique")
    for field in ("employment_share", "wage_share"):
        if sum(float(item[field]) for item in roles) > 1 + SHARE_TOLERANCE:
            raise NormalizeError("normalized role_mix %s sum exceeds 1" % field)
    band = value["n_band"]["value"]
    if band is not None and band > value["n_total"]["value"]:
        raise NormalizeError("normalized n_band.value may not exceed n_total.value")
    return value


def normalize(source, source_sha256, expected_code=None, expected_title=None):
    source = validate_legacy(source, expected_code=expected_code, expected_title=expected_title)
    if not isinstance(source_sha256, str) or not re.fullmatch(r"[0-9a-f]{64}", source_sha256):
        raise NormalizeError("source_sha256 must be a lowercase SHA-256 digest")

    occupations = [
        {
            "soc": item["soc"],
            "title": item["title"],
            "employment_share": item["emp_share"],
            "wage_share": item["wage_share"],
        }
        for item in source["role_mix"]["occupations"]
    ]
    legacy_labor_value = source["labor_share"]["value"]
    # A ratio above one cannot satisfy the normalized share contract.  Null is
    # the only fail-closed, non-invented representation; clamping would create
    # a value the source does not contain.  The exact source basis and digest
    # remain attached so the reason is auditable.
    labor_value = (
        None if legacy_labor_value is not None and float(legacy_labor_value) > 1
        else legacy_labor_value
    )
    labor_quality = (
        "NONE" if labor_value is None and legacy_labor_value is not None
        else _quality(source["labor_share"]["quality"], "labor_share")
    )
    value = {
        "dataset_version": DATASET_VERSION,
        "snapshot_id": "%s-%s" % (DERIVATION_VERSION, source["naics"]),
        "naics": source["naics"],
        "title": source["title"],
        "labor_share": {
            "value": labor_value,
            "quality": labor_quality,
            "basis": source["labor_share"]["method"],
        },
        "n_total": {
            "value": source["n_total"]["value"],
            "quality": _quality(source["n_total"]["quality"], "n_total"),
            "basis": source["n_total"]["source"],
        },
        "n_band": {
            "value": source["n_band"]["value"],
            "quality": _quality(source["n_band"]["quality"], "n_band"),
            "basis": source["n_band"]["derivation"],
        },
        "role_mix": {
            "basis": source["role_mix"]["oews_level"],
            "quality": _quality(source["role_mix"]["quality"], "role_mix"),
            "occupations": occupations,
        },
        "provenance": {
            "derivation_version": DERIVATION_VERSION,
            "source_manifest_sha256": source_sha256,
            "vintage": _legacy_vintage(source),
        },
    }
    return validate_output(value)


def load_targets(path):
    value = load_json(path)
    if not isinstance(value, dict) or not isinstance(value.get("codes"), list):
        raise NormalizeError("target membership must contain a codes array")
    rows = value["codes"]
    if len(rows) != EXPECTED_CODE_COUNT:
        raise NormalizeError("target membership must contain exactly %d codes, got %d" % (
            EXPECTED_CODE_COUNT, len(rows)))
    result = []
    seen = set()
    for index, row in enumerate(rows):
        row = _require_object(row, "targets.codes[%d]" % index)
        code = _require_string(row.get("naics"), "targets.codes[%d].naics" % index)
        title = _require_string(row.get("title"), "targets.codes[%d].title" % index)
        if not CODE_RE.fullmatch(code):
            raise NormalizeError("invalid target NAICS %r" % code)
        if code in seen:
            raise NormalizeError("duplicate target NAICS %s" % code)
        seen.add(code)
        result.append((code, title))
    return result


def build_all(targets_path=DEFAULT_TARGETS, input_dir=DEFAULT_INPUT_DIR):
    input_dir = Path(input_dir)
    records = {}
    for code, title in load_targets(targets_path):
        source_path = input_dir / (code + ".json")
        source = load_json(source_path)
        records[code] = normalize(
            source,
            sha256_file(source_path),
            expected_code=code,
            expected_title=title,
        )
    return records


def run(check=False, targets_path=DEFAULT_TARGETS, input_dir=DEFAULT_INPUT_DIR,
        output_dir=DEFAULT_OUTPUT_DIR):
    records = build_all(targets_path=targets_path, input_dir=input_dir)
    output_dir = Path(output_dir)
    expected_names = {code + ".json" for code in records}

    if output_dir.exists():
        extras = sorted(path.name for path in output_dir.glob("*.json") if path.name not in expected_names)
        if extras:
            raise NormalizeError("unexpected normalized dataset files: %s" % ", ".join(extras))
    elif check:
        raise NormalizeError("normalized dataset directory not found for --check: %s" % output_dir)

    if check:
        for code, value in records.items():
            output = output_dir / (code + ".json")
            try:
                actual = output.read_bytes()
            except FileNotFoundError as exc:
                raise NormalizeError("normalized output missing for --check: %s" % output) from exc
            expected = serialized_bytes(value)
            if actual != expected:
                raise NormalizeError("normalized output differs from fresh generation: %s" % output)
            # Parse and schema-check the on-disk value independently too.
            validate_output(load_json(output))
        return records

    output_dir.mkdir(parents=True, exist_ok=True)
    for code, value in records.items():
        (output_dir / (code + ".json")).write_bytes(serialized_bytes(value))
    return records


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--targets", default=str(DEFAULT_TARGETS))
    parser.add_argument("--input-dir", default=str(DEFAULT_INPUT_DIR))
    parser.add_argument("--output-dir", default=str(DEFAULT_OUTPUT_DIR))
    parser.add_argument("--check", action="store_true",
                        help="require all 63 outputs to equal fresh deterministic generation")
    args = parser.parse_args(argv)
    try:
        records = run(
            check=args.check,
            targets_path=Path(args.targets),
            input_dir=Path(args.input_dir),
            output_dir=Path(args.output_dir),
        )
        action = "verified" if args.check else "wrote"
        print("OK: %s %d normalized v4.1 datasets" % (action, len(records)))
    except (NormalizeError, OSError, UnicodeError, ValueError) as exc:
        print("NORMALIZE FAILED: %s" % exc, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
