#!/usr/bin/env python3
"""Normalize the frozen 63-code legacy dataset into the v4.2 schema.

This is a deterministic structural translation only.  It carries forward the
industry identity, labor share, firm counts, band count, occupation identities
and shares, and their legacy provenance.  It does not create controllable
value-added revenue, pass-through, or any other economic input.  Invalid or
absent legacy shares/counts are represented fail-closed as ``null``/``NONE``.

``--check`` rebuilds every record in memory and requires the checked-in v4.2
output set to be byte-identical.  Legacy and v4.1 inputs are never written.
"""

import argparse
import importlib.util
import math
import re
import sys
from pathlib import Path


HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
DEFAULT_TARGETS = REPO / "pipeline" / "blocks" / "targets_phase3.json"
DEFAULT_INPUT_DIR = REPO / "pipeline" / "datasets" / "derived"
DEFAULT_OUTPUT_DIR = REPO / "pipeline" / "datasets" / "v4_2"
SCHEMA_PATH = HERE / "schemas" / "dataset_v4_2.schema.json"
DERIVATION_VERSION = "normalize-v4.2-1"
DATASET_VERSION = "4.2"
EXPECTED_CODE_COUNT = 63
SHARE_TOLERANCE = 1e-9


def _load_v4_1_normalizer():
    """Reuse only the already-audited legacy parser and deterministic helpers."""
    path = HERE / "normalize_datasets_v4_1.py"
    spec = importlib.util.spec_from_file_location("normalize_datasets_v4_1_for_v4_2", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


legacy = _load_v4_1_normalizer()
NormalizeError = legacy.NormalizeError


def validate_output(value):
    schema = legacy.load_json(SCHEMA_PATH)
    errors = legacy.schema_validator.schema_errors(value, schema, schema)
    if errors:
        raise NormalizeError("normalized dataset schema errors: %s" % "; ".join(errors))

    roles = value["role_mix"]["occupations"]
    if len({item["soc"] for item in roles}) != len(roles):
        raise NormalizeError("normalized role_mix SOC identities must be unique")
    for field in ("employment_share", "wage_share"):
        if sum(float(item[field]) for item in roles) > 1 + SHARE_TOLERANCE:
            raise NormalizeError("normalized role_mix %s sum exceeds 1" % field)

    labor = value["labor_share"]
    if labor["value"] is None and labor["quality"] != "NONE":
        raise NormalizeError("normalized null labor_share.value requires quality NONE")
    band = value["n_band"]
    if band["value"] is None and band["quality"] != "NONE":
        raise NormalizeError("normalized null n_band.value requires quality NONE")
    if band["value"] is not None and band["value"] > value["n_total"]["value"]:
        raise NormalizeError("normalized n_band.value may not exceed n_total.value")
    return value


def normalize(source, source_sha256, expected_code=None, expected_title=None):
    source = legacy.validate_legacy(
        source,
        expected_code=expected_code,
        expected_title=expected_title,
    )
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
    labor_value = (
        legacy_labor_value
        if legacy_labor_value is not None
        and math.isfinite(float(legacy_labor_value))
        and 0 <= float(legacy_labor_value) <= 1
        else None
    )
    labor_quality = (
        legacy._quality(source["labor_share"]["quality"], "labor_share")
        if labor_value is not None
        else "NONE"
    )

    band_value = source["n_band"]["value"]
    band_quality = (
        legacy._quality(source["n_band"]["quality"], "n_band")
        if band_value is not None
        else "NONE"
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
            "quality": legacy._quality(source["n_total"]["quality"], "n_total"),
            "basis": source["n_total"]["source"],
        },
        "n_band": {
            "value": band_value,
            "quality": band_quality,
            "basis": source["n_band"]["derivation"],
        },
        "role_mix": {
            "basis": source["role_mix"]["oews_level"],
            "quality": legacy._quality(source["role_mix"]["quality"], "role_mix"),
            "occupations": occupations,
        },
        "provenance": {
            "derivation_version": DERIVATION_VERSION,
            "source_manifest_sha256": source_sha256,
            "vintage": legacy._legacy_vintage(source),
        },
    }
    return validate_output(value)


def build_all(targets_path=DEFAULT_TARGETS, input_dir=DEFAULT_INPUT_DIR):
    input_dir = Path(input_dir)
    records = {}
    targets = legacy.load_targets(targets_path)
    if len(targets) != EXPECTED_CODE_COUNT:
        raise NormalizeError("target membership must contain exactly %d codes" % EXPECTED_CODE_COUNT)
    for code, title in targets:
        source_path = input_dir / (code + ".json")
        records[code] = normalize(
            legacy.load_json(source_path),
            legacy.sha256_file(source_path),
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
        extras = sorted(
            path.name for path in output_dir.glob("*.json")
            if path.name not in expected_names
        )
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
            if actual != legacy.serialized_bytes(value):
                raise NormalizeError("normalized output differs from fresh generation: %s" % output)
            validate_output(legacy.load_json(output))
        return records

    output_dir.mkdir(parents=True, exist_ok=True)
    for code, value in records.items():
        (output_dir / (code + ".json")).write_bytes(legacy.serialized_bytes(value))
    return records


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--targets", default=str(DEFAULT_TARGETS))
    parser.add_argument("--input-dir", default=str(DEFAULT_INPUT_DIR))
    parser.add_argument("--output-dir", default=str(DEFAULT_OUTPUT_DIR))
    parser.add_argument(
        "--check",
        action="store_true",
        help="require all 63 outputs to equal fresh deterministic generation",
    )
    args = parser.parse_args(argv)
    try:
        records = run(
            check=args.check,
            targets_path=Path(args.targets),
            input_dir=Path(args.input_dir),
            output_dir=Path(args.output_dir),
        )
        action = "verified" if args.check else "wrote"
        print("OK: %s %d normalized v4.2 datasets" % (action, len(records)))
    except (NormalizeError, OSError, UnicodeError, ValueError) as exc:
        print("NORMALIZE FAILED: %s" % exc, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
