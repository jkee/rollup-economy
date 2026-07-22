#!/usr/bin/env python3
"""Versioned prompt assembler — deterministic, stdlib-only, no model calls.

Reads pipeline/blocks/targets_phase3.json; for each code merges
pipeline/blocks/<naics>.json + pipeline/datasets/derived/<naics>.json into the
frozen template pipeline/template/prompt_template_v3.md and writes
pipeline/prompts/<naics>.md.

Generation-time placeholders filled here:
  {{NAICS}} {{TITLE}} {{ROLE_HINTS}} {{SOURCE_HINTS}} {{CAPTURE_QUESTIONS}}
  {{TERMINAL_VALUE_QUESTION}} {{SPECIAL_NOTES}} {{DATASET_INPUTS_JSON}}
Runtime placeholders left verbatim for the Phase-4 runner:
  {{MODEL_ID}} {{RUN_DATE}} {{RUN_ID}} {{PROMPT_VERSION}}

Legacy routes read v3/v4 blocks. The v4.1 and v4.2 routes read only their
per-industry specification plus the pinned dataset and never read a legacy
block.

Missing legacy block file -> skip with warning. Invalid input or leftover
placeholder -> hard fail. v4.1 supports exact canary/full membership plus an
explicit partial-canary mode while specifications are being prepared. v4.2 is
strict: canary, holdout, and full scopes require complete exact membership and
never permit partial assembly.
--check: validate only (re-render in memory, compare against files on disk).

Two runs over the same inputs are byte-identical by construction: pure string
assembly, no timestamps, no randomness, no dict-order dependence beyond the
input files themselves.
"""

import argparse
import hashlib
import importlib.util
import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent.parent
TARGETS_PATH = REPO / "pipeline" / "blocks" / "targets_phase3.json"
BLOCKS_DIR = REPO / "pipeline" / "blocks"
DERIVED_DIR = REPO / "pipeline" / "datasets" / "derived"
SPECS_V4_1_DIR = REPO / "pipeline" / "specs_v4_1"
SPEC_V4_1_SCHEMA = REPO / "pipeline" / "build" / "schemas" / "industry_spec_v4_1.schema.json"
CANARY_V4_1_CODES = {"238220", "541214", "541511", "541512", "541930"}
HOLDOUT_MEMBERSHIP_PATH = REPO / "pipeline" / "v4_1" / "holdout_membership.json"
HOLDOUT_V4_1_CODES = ("541922", "541840", "541350", "541430", "541720")
SPECS_V4_2_DIR = REPO / "pipeline" / "specs_v4_2"
SPEC_V4_2_SCHEMA = REPO / "pipeline" / "build" / "schemas" / "industry_spec_v4_2.schema.json"
DATASET_V4_2_SCHEMA = REPO / "pipeline" / "build" / "schemas" / "dataset_v4_2.schema.json"
METHODOLOGY_V4_2_PATH = REPO / "V4_2_RUNTIME_METHODOLOGY.md"
GOVERNANCE_METHODOLOGY_V4_2_PATH = REPO / "V4_2_METHODOLOGY.md"
CANARY_V4_2_CODES = {"238220", "541214", "541511", "541512", "541930"}
REGRESSION_V4_2_MEMBERSHIP_PATH = REPO / "pipeline" / "v4_2" / "regression_membership.json"
REGRESSION_V4_2_VERSION = "v4.2-regression-1"
HOLDOUT_V4_2_MEMBERSHIP_PATH = REPO / "pipeline" / "v4_2" / "holdout_membership.json"
HOLDOUT_V4_2_VERSION = "v4.2-holdout-2026-07-21"
HOLDOUT_V4_2_CODES = ("541890", "541340", "541370", "541199", "541420")

VERSION_PATHS = {
    "3.0": {
        "template": REPO / "pipeline" / "template" / "prompt_template_v3.md",
        "prompts": REPO / "pipeline" / "prompts",
    },
    "3.1": {
        "template": REPO / "pipeline" / "template" / "prompt_template_v3_1.md",
        "prompts": REPO / "pipeline" / "prompts_v3_1",
    },
    "3.1.1": {
        "template": REPO / "pipeline" / "template" / "prompt_template_v3_1_1.md",
        "prompts": REPO / "pipeline" / "prompts_v3_1_1",
    },
    "3.1.2": {
        "template": REPO / "pipeline" / "template" / "prompt_template_v3_1_2.md",
        "prompts": REPO / "pipeline" / "prompts_v3_1_2",
    },
    "4.0": {
        "template": REPO / "pipeline" / "template" / "prompt_template_v4.md",
        "prompts": REPO / "pipeline" / "prompts_v4",
    },
    "4.1": {
        "template": REPO / "pipeline" / "template" / "prompt_template_v4_1.md",
        "prompts": REPO / "pipeline" / "prompts_v4_1",
        "specs": SPECS_V4_1_DIR,
    },
    "4.2": {
        "template": REPO / "pipeline" / "template" / "prompt_template_v4_2.md",
        "prompts": REPO / "pipeline" / "prompts_v4_2",
        "specs": SPECS_V4_2_DIR,
    },
}

RUNTIME_PLACEHOLDERS = {"{{MODEL_ID}}", "{{RUN_DATE}}", "{{RUN_ID}}", "{{PROMPT_VERSION}}"}
PLACEHOLDER_RE = re.compile(r"\{\{[^{}]*\}\}")

V4_2_PROMPT_CONTRACT_MARKERS = (
    "ACCRUAL_RECOGNIZED_REVENUE",
    "TRAILING_TWELVE_MONTHS",
    "pass_through_presentation",
    "capacity_type",
    "capacity_horizon",
    "capacity_calculation",
    "DEAL_EXECUTION",
    "INTEGRATION_ONBOARDING",
    "MAXIMUM_TARGET_COUNT",
    "NON_DUPLICATIVE_TARGET_COUNT",
    "anchor.anchor_basis",
    "ENTRY_EQUIVALENT_COMPARABLE_MULTIPLE_LEVEL",
    "point-identified",
    "low = base = high",
    "range.low = value = range.high",
    "No ordering is imposed on `r1` through `r5`",
    "five-year r interval box",
    "at most 32 distinct box vertices",
    "convex hull",
    "incompatible low-I/low-C or high-I/high-C bundles",
)

BLOCK_KEYS = [
    "role_hints",
    "source_hints",
    "capture_questions",
    "terminal_value_question",
    "special_notes",
    "research_gaps",
]
DATASET_FIELDS = ["labor_share", "role_mix", "n_total", "n_band"]
V4_1_DATASET_KEYS = {
    "dataset_version", "snapshot_id", "naics", "title", "labor_share",
    "n_total", "n_band", "role_mix", "provenance",
}

ROLE_HINT_KEYS = ["role", "oews_basis", "approx_share_of_wage_bill", "automatable", "note"]
SOURCE_HINT_KEYS = ["area", "source", "why", "uncertain_exists"]
GAP_KEYS = ["input", "instruction"]

V4_1_SPEC_KEYS = {
    "spec_version", "naics", "title", "dataset_snapshot", "target_archetype",
    "value_basis", "source_hints", "research_questions", "special_notes",
}
V4_1_QUESTION_KEYS = {
    "implementation", "commercial_retention", "sale_availability",
    "valuation_robustness", "operator_survival",
}
V4_1_FORBIDDEN = {
    "legacy distribution-retention field": re.compile(r"\bpi[_ -]?dist\b", re.IGNORECASE),
    "legacy moat field": re.compile(r"\bpi[_ -]?moat\b", re.IGNORECASE),
    "legacy owner-age field": re.compile(r"\bowners[_ -]?60plus(?:_pct)?\b", re.IGNORECASE),
    "benchmark-set disclosure": re.compile(r"\bgolden(?:[- ]set)?\b", re.IGNORECASE),
    "winner label": re.compile(r"\bwinner\b", re.IGNORECASE),
    "melter label": re.compile(r"\bmelter\b", re.IGNORECASE),
    "control label": re.compile(r"\bcontrol[- ](?:code|class|label)\b", re.IGNORECASE),
    "role-basis override instruction": re.compile(
        r"\brebuild\b[^\n.]{0,120}\b(?:V|value[- ]basis|role[- ]mix|role[- ]basis)\b",
        re.IGNORECASE,
    ),
}

V4_2_SPEC_KEYS = {
    "spec_version", "naics", "title", "methodology_snapshot",
    "dataset_snapshot", "target_archetype", "value_basis", "source_hints",
    "research_questions", "special_notes",
}
V4_2_QUESTION_KEYS = {
    "controllable_value_added", "operational_realization",
    "commercial_retention", "sale_availability", "buyer_access_win",
    "valuation_robustness", "operator_survival",
}
V4_2_VALUE_BASIS_KEYS = {
    "mode", "scope", "controllable_value_added_boundary",
    "approved_pass_through_categories", "employee_cash_cost_id",
    "controllable_contractor_cash_cost_id", "roles", "sources", "rationale",
    "caveats",
}
V4_2_SPEC_FORBIDDEN = {
    **V4_1_FORBIDDEN,
    "economic tier label": re.compile(
        r"(?:\bhell[_ -]?yes\b|"
        r"\b(?:verdict|tier|outcome)\s*(?:is|=|:)?\s*"
        r"(?:strong|conditional|pass|kill)\b|"
        r"\b(?:strong|conditional|pass|kill)\s+"
        r"(?:verdict|tier|outcome)\b)",
        re.IGNORECASE,
    ),
    "decision action label": re.compile(
        r"(?:\b(?:deep[_ -]?dive|evidence[_ -]?first|deprioritize)\b|"
        r"\b(?:action|decision)\s*(?:is|=|:)?\s*(?:selective|avoid)\b|"
        r"\b(?:selective|avoid)\s+(?:action|decision)\b)",
        re.IGNORECASE,
    ),
    "score or verdict hint": re.compile(
        r"\b(?:expected|target|desired|prior|likely)\s+"
        r"(?:score|verdict|tier|rank|percentile|outcome|color)\b"
        r"\s*(?:is|=|:)\s*[A-Za-z0-9_.-]+",
        re.IGNORECASE,
    ),
    "numeric score hint": re.compile(
        r"\b(?:expected|target|desired|prior|likely)\s+"
        r"(?:score|rank|percentile)\s+(?:of\s+)?-?[0-9]",
        re.IGNORECASE,
    ),
    "traffic-light outcome hint": re.compile(
        r"\b(?:green|red|yellow)\s+(?:industry|code|outcome|verdict|tier)\b",
        re.IGNORECASE,
    ),
}


class AssembleError(Exception):
    pass


class _JsonContractError(ValueError):
    pass


_SCHEMA_VALIDATOR = None
_RUNTIME_LINTER = None


def fail(naics, msg):
    raise AssembleError(f"[{naics}] {msg}")


def _reject_json_constant(value):
    raise _JsonContractError("non-standard JSON constant %r is forbidden" % value)


def _closed_pairs(pairs):
    """Match the v4.2 issuer/finalizer duplicate-key rejection contract."""
    result = {}
    for key, value in pairs:
        if key in result:
            raise _JsonContractError("duplicate JSON key %r" % key)
        result[key] = value
    return result


def _read_json(naics, path, label, strict_v4_2=False):
    try:
        kwargs = {}
        if strict_v4_2:
            kwargs = {
                "parse_constant": _reject_json_constant,
                "object_pairs_hook": _closed_pairs,
            }
        return json.loads(path.read_text(encoding="utf-8"), **kwargs)
    except FileNotFoundError:
        fail(naics, f"{label} not found: {path}")
    except (json.JSONDecodeError, _JsonContractError) as exc:
        fail(naics, f"{label} is not valid JSON: {exc}")


def _sha256(path):
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _schema_errors(value, schema):
    """Use the repository's stdlib schema validator before semantic checks."""
    global _SCHEMA_VALIDATOR
    if _SCHEMA_VALIDATOR is None:
        validator_path = Path(__file__).resolve().parent / "build.py"
        module_spec = importlib.util.spec_from_file_location(
            "prompt_assembler_schema_validator", validator_path
        )
        if module_spec is None or module_spec.loader is None:
            raise AssembleError(f"could not load schema validator: {validator_path}")
        _SCHEMA_VALIDATOR = importlib.util.module_from_spec(module_spec)
        module_spec.loader.exec_module(_SCHEMA_VALIDATOR)
    return _SCHEMA_VALIDATOR.schema_errors(value, schema, schema)


def _runtime_leakage_errors(text, label, allowed_naics=None):
    """Use the single runtime-visibility linter shared with freeze tooling."""
    global _RUNTIME_LINTER
    if _RUNTIME_LINTER is None:
        linter_path = Path(__file__).resolve().parent / "build_runtime_methodology_v4_2.py"
        module_spec = importlib.util.spec_from_file_location(
            "prompt_assembler_runtime_linter", linter_path
        )
        if module_spec is None or module_spec.loader is None:
            raise AssembleError(f"could not load runtime leakage linter: {linter_path}")
        _RUNTIME_LINTER = importlib.util.module_from_spec(module_spec)
        module_spec.loader.exec_module(_RUNTIME_LINTER)
    return _RUNTIME_LINTER.leakage_errors(text, label, allowed_naics=allowed_naics)


def semantic_lint_v4_1(naics, text, label="v4.1 content"):
    violations = []
    for name, pattern in V4_1_FORBIDDEN.items():
        match = pattern.search(text)
        if match:
            violations.append(f"{name} ({match.group(0)!r})")
    if violations:
        fail(naics, f"{label} contains forbidden semantic leakage: {', '.join(violations)}")


def semantic_lint_v4_2_spec(naics, text, label="v4.2 industry spec"):
    """Reject legacy/class/outcome hints from model-visible v4.2 spec text."""
    violations = []
    for name, pattern in V4_2_SPEC_FORBIDDEN.items():
        match = pattern.search(text)
        if match:
            violations.append(f"{name} ({match.group(0)!r})")
    allowed_naics = naics if re.fullmatch(r"[0-9]{6}", str(naics)) else None
    violations.extend(_runtime_leakage_errors(text, label, allowed_naics))
    if violations:
        fail(naics, f"{label} contains forbidden semantic leakage: {', '.join(violations)}")


def validate_v4_2_prompt_contract(naics, text, label="v4.2 prompt"):
    """Fail closed when a model-visible prompt omits an authoritative construct."""
    missing = [marker for marker in V4_2_PROMPT_CONTRACT_MARKERS if marker not in text]
    if missing:
        fail(naics, f"{label} missing v4.2 contract marker(s): {', '.join(missing)}")


def _require_exact_keys(naics, value, required, label):
    if not isinstance(value, dict):
        fail(naics, f"{label} must be an object")
    actual = set(value)
    missing, extra = sorted(set(required) - actual), sorted(actual - set(required))
    if missing:
        fail(naics, f"{label} missing key(s): {', '.join(missing)}")
    if extra:
        fail(naics, f"{label} has unexpected key(s): {', '.join(extra)}")


def _require_strings(naics, values, label, minimum=1):
    if not isinstance(values, list) or len(values) < minimum:
        fail(naics, f"{label} must contain at least {minimum} item(s)")
    if not all(isinstance(item, str) and item.strip() for item in values):
        fail(naics, f"{label} entries must be non-empty strings")


def _validate_value_basis_v4_1(naics, basis):
    cash_key = "labor_contractor_cash_cost_share"
    keys = {"mode", "scope", cash_key, "roles", "sources", "rationale", "caveats"}
    if "bridge" in basis:
        keys.add("bridge")
    _require_exact_keys(naics, basis, keys, "value_basis")
    mode = basis["mode"]
    if mode not in ("dataset", "target_specific", "assumption", "missing"):
        fail(naics, "value_basis.mode must be dataset, target_specific, assumption, or missing")
    for name in ("scope", "rationale"):
        if not isinstance(basis[name], str) or not basis[name].strip():
            fail(naics, f"value_basis.{name} must be a non-empty string")
    if not isinstance(basis["caveats"], list) or not all(
        isinstance(item, str) and item.strip() for item in basis["caveats"]
    ):
        fail(naics, "value_basis.caveats must be an array of non-empty strings")
    if not isinstance(basis["roles"], list) or not isinstance(basis["sources"], list):
        fail(naics, "value_basis.roles and sources must be arrays")

    bridge = basis.get("bridge")
    bridge_keys = {"population", "geography", "period", "unit", "business_model"}
    if bridge is not None:
        _require_exact_keys(naics, bridge, bridge_keys, "value_basis.bridge")
        if not all(isinstance(bridge[name], str) and bridge[name].strip() for name in bridge_keys):
            fail(naics, "value_basis.bridge fields must be non-empty strings")
    if mode != "dataset" and bridge is not None:
        fail(naics, f"value_basis mode {mode} requires bridge to be null")

    if mode in ("dataset", "missing"):
        if basis[cash_key] is not None or basis["roles"] or basis["sources"]:
            fail(naics, f"value_basis mode {mode} requires null cash-cost share and empty roles/sources")
        return

    labor = basis[cash_key]
    if mode == "target_specific":
        labor_keys = {"value", "range", "evidence_quality", "source_ids", "rationale", "caveats"}
        center_key = "value"
    else:
        labor_keys = {
            "base", "range", "evidence_state", "evidence_quality",
            "source_ids", "rationale", "caveats",
        }
        center_key = "base"
    _require_exact_keys(naics, labor, labor_keys, f"value_basis.{cash_key}")
    numeric = (int, float)
    if isinstance(labor[center_key], bool) or not isinstance(labor[center_key], numeric):
        fail(naics, f"value_basis.{cash_key}.{center_key} must be numeric")
    _require_exact_keys(naics, labor["range"], {"low", "high"}, f"value_basis.{cash_key}.range")
    low, center, high = labor["range"]["low"], labor[center_key], labor["range"]["high"]
    if any(isinstance(item, bool) or not isinstance(item, numeric) for item in (low, center, high)):
        fail(naics, f"value_basis.{cash_key} range must be numeric")
    if not (0 <= low <= center <= high <= 1):
        fail(naics, f"value_basis.{cash_key} must satisfy 0 <= low <= {center_key} <= high <= 1")
    if mode == "target_specific":
        if labor["evidence_quality"] not in ("HIGH", "MED", "LOW"):
            fail(naics, f"value_basis.{cash_key}.evidence_quality is invalid")
        _require_strings(naics, labor["source_ids"], f"value_basis.{cash_key}.source_ids")
    else:
        if labor["evidence_state"] != "ASSUMPTION" or labor["evidence_quality"] != "NONE":
            fail(naics, f"assumption value basis requires ASSUMPTION/NONE evidence labels")
        if labor["source_ids"] != []:
            fail(naics, f"assumption value basis cannot claim cash-cost sources")
    if not isinstance(labor["rationale"], str) or not labor["rationale"].strip():
        fail(naics, f"value_basis.{cash_key}.rationale must be non-empty")
    if not isinstance(labor["caveats"], list) or not all(
        isinstance(item, str) and item.strip() for item in labor["caveats"]
    ):
        fail(naics, f"value_basis.{cash_key}.caveats must be an array")

    if not basis["roles"]:
        fail(naics, f"{mode} value basis requires roles")
    if mode == "target_specific" and not basis["sources"]:
        fail(naics, "target_specific value basis requires sources")
    if mode == "assumption" and basis["sources"]:
        fail(naics, "assumption value basis cannot claim sources")
    source_ids = []
    for index, source in enumerate(basis["sources"]):
        _require_exact_keys(naics, source, {"id", "url", "title", "vintage"}, f"value_basis.sources[{index}]")
        if not re.fullmatch(r"B[1-9][0-9]*", str(source["id"])):
            fail(naics, f"value_basis.sources[{index}].id is invalid")
        if not isinstance(source["url"], str) or not re.match(r"^https?://", source["url"]):
            fail(naics, f"value_basis.sources[{index}].url must be HTTP(S)")
        if not all(isinstance(source[name], str) and source[name].strip() for name in ("title", "vintage")):
            fail(naics, f"value_basis.sources[{index}] title/vintage must be non-empty")
        source_ids.append(source["id"])
    if len(source_ids) != len(set(source_ids)):
        fail(naics, "value_basis source IDs must be unique")
    source_set = set(source_ids)
    if not set(labor["source_ids"]).issubset(source_set):
        fail(naics, f"value_basis.{cash_key} references unknown basis sources")

    role_ids, total = [], 0.0
    for index, role in enumerate(basis["roles"]):
        _require_exact_keys(
            naics, role,
            {"role_id", "title", "role_cash_cost_weight", "source_ids", "rationale"},
            f"value_basis.roles[{index}]",
        )
        if not re.fullmatch(r"[A-Z0-9][A-Z0-9._-]*", str(role["role_id"])):
            fail(naics, f"value_basis.roles[{index}].role_id is invalid")
        share = role["role_cash_cost_weight"]
        if isinstance(share, bool) or not isinstance(share, numeric) or not 0 < share <= 1:
            fail(naics, f"value_basis.roles[{index}].role_cash_cost_weight must be in (0, 1]")
        if mode == "target_specific":
            _require_strings(naics, role["source_ids"], f"value_basis.roles[{index}].source_ids")
        elif role["source_ids"] != []:
            fail(naics, f"assumption value_basis.roles[{index}] cannot claim sources")
        if not set(role["source_ids"]).issubset(source_set):
            fail(naics, f"value_basis.roles[{index}] references unknown basis sources")
        if not all(isinstance(role[name], str) and role[name].strip() for name in ("title", "rationale")):
            fail(naics, f"value_basis.roles[{index}] title/rationale must be non-empty")
        role_ids.append(role["role_id"])
        total += float(share)
    if len(role_ids) != len(set(role_ids)):
        fail(naics, "value_basis role IDs must be unique")
    if abs(total - 1.0) > 1e-9:
        fail(naics, f"{mode} role weights must sum to 1.0 (got {total:.12g})")


def _count_range_v4_1(naics, value, label):
    _require_exact_keys(naics, value, {"base", "low", "high"}, label)
    numbers = (value["low"], value["base"], value["high"])
    if any(isinstance(item, bool) or not isinstance(item, (int, float)) for item in numbers):
        fail(naics, f"{label} values must be numeric")
    if not 0 <= numbers[0] <= numbers[1] <= numbers[2]:
        fail(naics, f"{label} must satisfy 0 <= low <= base <= high")
    return tuple(float(item) for item in numbers)


def _validate_target_archetype_v4_1(naics, archetype):
    keys = {
        "selected_id", "alternatives", "residual", "enumeration_coverage",
        "sources", "selection_basis", "selection_uncertainty",
    }
    _require_exact_keys(naics, archetype, keys, "target_archetype")
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", str(archetype["selected_id"])):
        fail(naics, "target_archetype.selected_id must be lowercase kebab-case")
    if not isinstance(archetype["alternatives"], list) or not archetype["alternatives"]:
        fail(naics, "target_archetype.alternatives must be non-empty")
    if not isinstance(archetype["sources"], list):
        fail(naics, "target_archetype.sources must be an array")
    if not isinstance(archetype["selection_uncertainty"], bool):
        fail(naics, "target_archetype.selection_uncertainty must be boolean")
    if not isinstance(archetype["selection_basis"], str) or not archetype["selection_basis"].strip():
        fail(naics, "target_archetype.selection_basis must be non-empty")

    source_ids = []
    for index, source in enumerate(archetype["sources"]):
        _require_exact_keys(naics, source, {"id", "url", "title", "vintage"}, f"target_archetype.sources[{index}]")
        if not re.fullmatch(r"A[1-9][0-9]*", str(source["id"])):
            fail(naics, f"target_archetype.sources[{index}].id is invalid")
        if not isinstance(source["url"], str) or not re.match(r"^https?://", source["url"]):
            fail(naics, f"target_archetype.sources[{index}].url must be HTTP(S)")
        if not all(isinstance(source[name], str) and source[name].strip() for name in ("title", "vintage")):
            fail(naics, f"target_archetype.sources[{index}] title/vintage must be non-empty")
        source_ids.append(source["id"])
    if len(source_ids) != len(set(source_ids)):
        fail(naics, "target_archetype source IDs must be unique")
    source_set = set(source_ids)

    option_ids, counts = [], {}
    option_keys = {"id", "name", "inclusion_criteria", "exclusion_criteria", "band_count", "source_ids", "rationale"}
    for index, option in enumerate(archetype["alternatives"]):
        label = f"target_archetype.alternatives[{index}]"
        _require_exact_keys(naics, option, option_keys, label)
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", str(option["id"])):
            fail(naics, f"{label}.id must be lowercase kebab-case")
        if not all(isinstance(option[name], str) and option[name].strip() for name in ("name", "rationale")):
            fail(naics, f"{label} name/rationale must be non-empty")
        _require_strings(naics, option["inclusion_criteria"], f"{label}.inclusion_criteria")
        _require_strings(naics, option["exclusion_criteria"], f"{label}.exclusion_criteria")
        if not isinstance(option["source_ids"], list) or not all(isinstance(item, str) for item in option["source_ids"]):
            fail(naics, f"{label}.source_ids must be an array of strings")
        if not set(option["source_ids"]).issubset(source_set):
            fail(naics, f"{label} references unknown archetype sources")
        counts[option["id"]] = _count_range_v4_1(naics, option["band_count"], f"{label}.band_count")
        option_ids.append(option["id"])
    if len(option_ids) != len(set(option_ids)):
        fail(naics, "target_archetype alternative IDs must be unique")
    selected = archetype["selected_id"]
    if selected not in counts:
        fail(naics, "target_archetype.selected_id must identify an enumerated alternative")
    ordered = sorted(counts, key=lambda item: (-counts[item][1], item))
    if selected != ordered[0]:
        fail(
            naics,
            "target_archetype selection must have the largest base band count, "
            "using the lexicographically smallest ID to break a tie",
        )
    selection_is_uncertain = False
    if len(ordered) > 1:
        first, second = counts[ordered[0]], counts[ordered[1]]
        close_bases = first[1] == 0 or (first[1] - second[1]) / first[1] < 0.10
        ranges_overlap = second[2] >= first[0]
        selection_is_uncertain = close_bases or ranges_overlap
    if archetype["selection_uncertainty"] != selection_is_uncertain:
        fail(
            naics,
            "target_archetype.selection_uncertainty must be true exactly when the two "
            "largest base counts are within 10% or their supported ranges overlap",
        )

    residual = archetype["residual"]
    _require_exact_keys(naics, residual, {"name", "band_count", "rationale"}, "target_archetype.residual")
    if not all(isinstance(residual[name], str) and residual[name].strip() for name in ("name", "rationale")):
        fail(naics, "target_archetype.residual name/rationale must be non-empty")
    _count_range_v4_1(naics, residual["band_count"], "target_archetype.residual.band_count")
    coverage = archetype["enumeration_coverage"]
    _require_exact_keys(naics, coverage, {"base", "low", "high"}, "target_archetype.enumeration_coverage")
    values = coverage["low"], coverage["base"], coverage["high"]
    if any(isinstance(item, bool) or not isinstance(item, (int, float)) for item in values):
        fail(naics, "target_archetype.enumeration_coverage must be numeric")
    if not 0 <= values[0] <= values[1] <= values[2] <= 1 or values[1] < 0.8:
        fail(naics, "target_archetype enumeration must cover at least 80% at base")


def validate_industry_spec_v4_1(naics, title, spec):
    _require_exact_keys(naics, spec, V4_1_SPEC_KEYS, "industry spec")
    if spec["spec_version"] != "4.1":
        fail(naics, "industry spec version must be exactly 4.1")
    if spec["naics"] != naics or spec["title"] != title:
        fail(naics, "industry spec identity differs from frozen target membership")

    snapshot = spec["dataset_snapshot"]
    _require_exact_keys(naics, snapshot, {"path", "sha256"}, "dataset_snapshot")
    expected_path = f"pipeline/datasets/v4_1/{naics}.json"
    if snapshot["path"] != expected_path:
        fail(naics, f"dataset_snapshot.path must be exactly {expected_path}")
    if not re.fullmatch(r"[0-9a-f]{64}", str(snapshot["sha256"])):
        fail(naics, "dataset_snapshot.sha256 must be a lowercase SHA-256 digest")

    _validate_target_archetype_v4_1(naics, spec["target_archetype"])

    _validate_value_basis_v4_1(naics, spec["value_basis"])

    if not isinstance(spec["source_hints"], list) or not spec["source_hints"]:
        fail(naics, "source_hints must be a non-empty array")
    for index, hint in enumerate(spec["source_hints"]):
        _require_exact_keys(naics, hint, {"area", "source", "why", "uncertain_exists"}, f"source_hints[{index}]")
        if not all(isinstance(hint[name], str) and hint[name].strip() for name in ("area", "source", "why")):
            fail(naics, f"source_hints[{index}] text fields must be non-empty")
        if not isinstance(hint["uncertain_exists"], bool):
            fail(naics, f"source_hints[{index}].uncertain_exists must be boolean")

    questions = spec["research_questions"]
    _require_exact_keys(naics, questions, V4_1_QUESTION_KEYS, "research_questions")
    for name in sorted(V4_1_QUESTION_KEYS):
        _require_strings(naics, questions[name], f"research_questions.{name}")
    if not isinstance(spec["special_notes"], list) or not all(
        isinstance(item, str) and item.strip() for item in spec["special_notes"]
    ):
        fail(naics, "special_notes must be an array of non-empty strings")

    semantic_lint_v4_1(
        naics, json.dumps(spec, sort_keys=True, ensure_ascii=False), "industry spec"
    )


def _validate_source_namespaces_v4_2(naics, spec):
    """Keep archetype and value-basis registry IDs closed and disjoint."""
    if not isinstance(spec, dict):
        return
    archetype = spec.get("target_archetype")
    basis = spec.get("value_basis")
    if not isinstance(archetype, dict) or not isinstance(basis, dict):
        return
    archetype_sources = archetype.get("sources")
    basis_sources = basis.get("sources")
    if not isinstance(archetype_sources, list) or not isinstance(basis_sources, list):
        return
    archetype_ids = [
        source.get("id") for source in archetype_sources if isinstance(source, dict)
    ]
    basis_ids = [
        source.get("id") for source in basis_sources if isinstance(source, dict)
    ]
    collisions = sorted(
        {item for item in archetype_ids if isinstance(item, str)}
        & {item for item in basis_ids if isinstance(item, str)}
    )
    if collisions:
        fail(
            naics,
            "archetype and value-basis source ID namespaces collide: "
            + ", ".join(collisions),
        )
    if any(not re.fullmatch(r"A[1-9][0-9]*", str(item)) for item in archetype_ids):
        fail(naics, "target_archetype source IDs must use the A* namespace")
    if any(not re.fullmatch(r"B[1-9][0-9]*", str(item)) for item in basis_ids):
        fail(naics, "value-basis source IDs must use the B* namespace")


def _validate_value_basis_v4_2(naics, basis):
    _require_exact_keys(naics, basis, V4_2_VALUE_BASIS_KEYS, "v4.2 value_basis")
    mode = basis["mode"]
    if mode not in ("target_specific", "assumption", "missing"):
        fail(naics, "v4.2 value_basis.mode must be target_specific, assumption, or missing")
    for name in ("scope", "controllable_value_added_boundary", "rationale"):
        if not isinstance(basis[name], str) or not basis[name].strip():
            fail(naics, f"v4.2 value_basis.{name} must be a non-empty string")
    if not isinstance(basis["approved_pass_through_categories"], list) or not all(
        isinstance(item, str) and item.strip()
        for item in basis["approved_pass_through_categories"]
    ):
        fail(naics, "v4.2 approved_pass_through_categories must be an array of non-empty strings")
    if len(basis["approved_pass_through_categories"]) != len(
        set(basis["approved_pass_through_categories"])
    ):
        fail(naics, "v4.2 approved_pass_through_categories must be unique")
    if not isinstance(basis["caveats"], list) or not all(
        isinstance(item, str) and item.strip() for item in basis["caveats"]
    ):
        fail(naics, "v4.2 value_basis.caveats must be an array of non-empty strings")
    if not isinstance(basis["roles"], list) or not isinstance(basis["sources"], list):
        fail(naics, "v4.2 value_basis roles and sources must be arrays")

    cash_ids = (basis["employee_cash_cost_id"], basis["controllable_contractor_cash_cost_id"])
    for name, value in zip(
        ("employee_cash_cost_id", "controllable_contractor_cash_cost_id"), cash_ids
    ):
        if value is not None and not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]*", str(value)):
            fail(naics, f"v4.2 value_basis.{name} is invalid")

    if mode == "missing":
        if any(item is not None for item in cash_ids) or basis["roles"] or basis["sources"]:
            fail(naics, "missing v4.2 value basis requires null cash IDs and empty roles/sources")
        return
    if any(item is None for item in cash_ids):
        fail(naics, f"{mode} v4.2 value basis requires both cash-cost IDs")
    if cash_ids[0] == cash_ids[1]:
        fail(naics, "v4.2 employee and contractor cash-cost IDs must be distinct")

    source_ids = []
    for index, source in enumerate(basis["sources"]):
        label = f"v4.2 value_basis.sources[{index}]"
        _require_exact_keys(naics, source, {"id", "url", "title", "vintage"}, label)
        if not re.fullmatch(r"B[1-9][0-9]*", str(source["id"])):
            fail(naics, f"{label}.id is invalid")
        if not isinstance(source["url"], str) or not re.match(r"^https?://", source["url"]):
            fail(naics, f"{label}.url must be HTTP(S)")
        if not all(isinstance(source[name], str) and source[name].strip() for name in ("title", "vintage")):
            fail(naics, f"{label} title/vintage must be non-empty")
        source_ids.append(source["id"])
    if len(source_ids) != len(set(source_ids)):
        fail(naics, "v4.2 value-basis source IDs must be unique")
    if mode == "target_specific" and not source_ids:
        fail(naics, "target_specific v4.2 value basis requires sources")
    if mode == "assumption" and source_ids:
        fail(naics, "assumption v4.2 value basis must be source-free")
    source_set = set(source_ids)

    role_ids, role_titles, total = [], [], 0.0
    for index, role in enumerate(basis["roles"]):
        label = f"v4.2 value_basis.roles[{index}]"
        _require_exact_keys(
            naics, role,
            {
                "role_id", "title", "role_cash_cost_weight", "method",
                "evidence_quality", "source_ids", "rationale",
            },
            label,
        )
        if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]*", str(role["role_id"])):
            fail(naics, f"{label}.role_id is invalid")
        if mode == "target_specific":
            if role["method"] not in ("OBSERVED", "CALCULATED"):
                fail(naics, f"{label}.method must be OBSERVED or CALCULATED")
            if role["evidence_quality"] not in ("HIGH", "MED"):
                fail(naics, f"{label}.evidence_quality must be HIGH or MED")
        elif role["method"] != "ESTIMATE" or role["evidence_quality"] != "NONE":
            fail(naics, f"{label} assumption role must use ESTIMATE/NONE")
        share = role["role_cash_cost_weight"]
        if isinstance(share, bool) or not isinstance(share, (int, float)) or not 0 < share <= 1:
            fail(naics, f"{label}.role_cash_cost_weight must be in (0, 1]")
        if mode == "target_specific":
            _require_strings(naics, role["source_ids"], f"{label}.source_ids")
        elif role["source_ids"] != []:
            fail(naics, f"{label} assumption role must be source-free")
        if len(role["source_ids"]) != len(set(role["source_ids"])):
            fail(naics, f"{label}.source_ids must be unique")
        if not set(role["source_ids"]).issubset(source_set):
            fail(naics, f"{label} references unknown value-basis sources")
        if not all(isinstance(role[name], str) and role[name].strip() for name in ("title", "rationale")):
            fail(naics, f"{label} title/rationale must be non-empty")
        role_ids.append(role["role_id"])
        role_titles.append(role["title"])
        total += float(share)
    if not role_ids or len(role_ids) != len(set(role_ids)):
        fail(naics, f"{mode} v4.2 value basis requires unique roles")
    if len(role_titles) != len(set(role_titles)):
        fail(naics, f"{mode} v4.2 value basis requires unique role titles")
    if abs(total - 1.0) > 1e-12:
        fail(naics, f"v4.2 role cash-cost weights must sum to 1.0 (got {total:.12g})")


def validate_industry_spec_v4_2(naics, title, spec):
    _validate_source_namespaces_v4_2(naics, spec)
    schema = _read_json(
        naics, SPEC_V4_2_SCHEMA, "v4.2 industry spec schema", strict_v4_2=True
    )
    schema_violations = _schema_errors(spec, schema)
    if schema_violations:
        fail(
            naics,
            "v4.2 industry spec schema validation failed: "
            + "; ".join(schema_violations[:20]),
        )
    _require_exact_keys(naics, spec, V4_2_SPEC_KEYS, "v4.2 industry spec")
    if spec["spec_version"] != "4.2":
        fail(naics, "industry spec version must be exactly 4.2")
    if spec["naics"] != naics or spec["title"] != title:
        fail(naics, "v4.2 industry spec identity differs from frozen target membership")

    methodology = spec["methodology_snapshot"]
    _require_exact_keys(naics, methodology, {"path", "sha256"}, "methodology_snapshot")
    if methodology["path"] != "V4_2_RUNTIME_METHODOLOGY.md":
        fail(naics, "methodology_snapshot.path must be exactly V4_2_RUNTIME_METHODOLOGY.md")
    if not re.fullmatch(r"[0-9a-f]{64}", str(methodology["sha256"])):
        fail(naics, "methodology_snapshot.sha256 must be a lowercase SHA-256 digest")

    snapshot = spec["dataset_snapshot"]
    _require_exact_keys(naics, snapshot, {"path", "sha256"}, "dataset_snapshot")
    expected_dataset = f"pipeline/datasets/v4_2/{naics}.json"
    if snapshot["path"] != expected_dataset:
        fail(naics, f"dataset_snapshot.path must be exactly {expected_dataset}")
    if not re.fullmatch(r"[0-9a-f]{64}", str(snapshot["sha256"])):
        fail(naics, "dataset_snapshot.sha256 must be a lowercase SHA-256 digest")

    # v4.2 retains the objective one-record archetype contract unchanged.
    _validate_target_archetype_v4_1(naics, spec["target_archetype"])
    _validate_value_basis_v4_2(naics, spec["value_basis"])

    if not isinstance(spec["source_hints"], list) or not spec["source_hints"]:
        fail(naics, "v4.2 source_hints must be a non-empty array")
    for index, hint in enumerate(spec["source_hints"]):
        label = f"v4.2 source_hints[{index}]"
        _require_exact_keys(naics, hint, {"area", "source", "why", "uncertain_exists"}, label)
        if not all(isinstance(hint[name], str) and hint[name].strip() for name in ("area", "source", "why")):
            fail(naics, f"{label} text fields must be non-empty")
        if not isinstance(hint["uncertain_exists"], bool):
            fail(naics, f"{label}.uncertain_exists must be boolean")

    questions = spec["research_questions"]
    _require_exact_keys(naics, questions, V4_2_QUESTION_KEYS, "v4.2 research_questions")
    for name in sorted(V4_2_QUESTION_KEYS):
        _require_strings(naics, questions[name], f"v4.2 research_questions.{name}")
    if not isinstance(spec["special_notes"], list) or not all(
        isinstance(item, str) and item.strip() for item in spec["special_notes"]
    ):
        fail(naics, "v4.2 special_notes must be an array of non-empty strings")

    semantic_lint_v4_2_spec(
        naics, json.dumps(spec, sort_keys=True, ensure_ascii=False), "v4.2 industry spec"
    )


def validate_block(naics, block):
    if not isinstance(block, dict):
        fail(naics, "block is not a JSON object")
    missing = [k for k in BLOCK_KEYS if k not in block]
    if missing:
        fail(naics, f"block missing key(s): {', '.join(missing)}")
    extra = [k for k in block if k not in BLOCK_KEYS]
    if extra:
        fail(naics, f"block has unexpected key(s): {', '.join(extra)}")

    rh = block["role_hints"]
    if not isinstance(rh, list) or not rh:
        fail(naics, "role_hints must be a non-empty array")
    for i, item in enumerate(rh):
        if not isinstance(item, dict):
            fail(naics, f"role_hints[{i}] is not an object")
        for k in ROLE_HINT_KEYS:
            if k not in item:
                fail(naics, f"role_hints[{i}] missing '{k}'")

    sh = block["source_hints"]
    if not isinstance(sh, list) or not sh:
        fail(naics, "source_hints must be a non-empty array")
    for i, item in enumerate(sh):
        if not isinstance(item, dict):
            fail(naics, f"source_hints[{i}] is not an object")
        for k in SOURCE_HINT_KEYS:
            if k not in item:
                fail(naics, f"source_hints[{i}] missing '{k}'")

    cq = block["capture_questions"]
    if not isinstance(cq, list) or not (3 <= len(cq) <= 5):
        n = len(cq) if isinstance(cq, list) else "non-array"
        fail(naics, f"capture_questions must be an array of 3-5 strings (got {n})")
    if not all(isinstance(q, str) and q.strip() for q in cq):
        fail(naics, "capture_questions entries must be non-empty strings")

    tv = block["terminal_value_question"]
    if not isinstance(tv, str) or not tv.strip():
        fail(naics, "terminal_value_question must be a non-empty string")

    sn = block["special_notes"]
    if not isinstance(sn, list) or not sn or not all(isinstance(s, str) and s.strip() for s in sn):
        fail(naics, "special_notes must be a non-empty array of non-empty strings")

    gaps = block["research_gaps"]
    if not isinstance(gaps, list):
        fail(naics, "research_gaps must be an array (empty when no gaps)")
    for i, item in enumerate(gaps):
        if not isinstance(item, dict):
            fail(naics, f"research_gaps[{i}] is not an object")
        for k in GAP_KEYS:
            if k not in item or not item[k]:
                fail(naics, f"research_gaps[{i}] missing '{k}'")
        if item["input"] not in ("labor_share", "n_band"):
            fail(naics, f"research_gaps[{i}].input must be 'labor_share' or 'n_band' (got {item['input']!r})")


def render_role_hints(block):
    lines = []
    for item in block["role_hints"]:
        auto = item["automatable"]
        auto_txt = {True: "yes", False: "no"}.get(auto, str(auto))
        lines.append(
            f"- **{item['role']}** — {item['approx_share_of_wage_bill']} of wage bill "
            f"(OEWS basis: {item['oews_basis']}); automatable: {auto_txt}. {item['note']}"
        )
    return "\n".join(lines)


def render_source_hints(block):
    lines = []
    for item in block["source_hints"]:
        suffix = " *(existence unverified — confirm this source still exists/publishes before relying on it)*" if item["uncertain_exists"] else ""
        lines.append(f"- ({item['area']}) {item['source']} — {item['why']}{suffix}")
    return "\n".join(lines)


def render_capture_questions(block):
    return "\n".join(f"- {q}" for q in block["capture_questions"])


def render_special_notes(block):
    return "\n".join(f"- {s}" for s in block["special_notes"])


def render_dataset_inputs(naics, block, dataset, template_version):
    missing = [f for f in DATASET_FIELDS if f not in dataset]
    if missing:
        fail(naics, f"dataset record missing field(s): {', '.join(missing)}")
    subset = {f: dataset[f] for f in DATASET_FIELDS}
    body = "```json\n" + json.dumps(subset, indent=2, ensure_ascii=False) + "\n```"
    gaps = block["research_gaps"]
    if gaps:
        gap_lines = "\n".join(f"- `{g['input']}`: {g['instruction']}" for g in gaps)
        if template_version == "4.0":
            fallback_rule = (
                "provide the value in `dataset_fallbacks` using the v4 numeric "
                "selection shape, including numeric low/base/high range and explicit "
                "evidence state; use `MISSING` rather than invented precision"
            )
        elif template_version == "3.1.2":
            fallback_rule = (
                "provide the value in `dataset_fallbacks` using the compact v3.1.2 "
                "selection shape; use `OBSERVED` only for an exact sourced value, "
                "`CALCULATED` only for safe source-backed arithmetic, and `ESTIMATE` "
                "for any judgmental bridge, with range, confidence and candid caveats"
            )
        elif template_version == "3.1.1":
            fallback_rule = (
                "provide the value in `dataset_fallbacks` using the v3.1.1 "
                "selection contract; use `OBSERVED` only for an exact sourced value, "
                "`CALCULATED` only for fully reproducible fact-backed arithmetic, and "
                "`ESTIMATE` for any judgmental bridge"
            )
        elif template_version == "3.1":
            fallback_rule = (
                "provide the value in `dataset_fallbacks`, show the full v3.1 evidence "
                "chain, and use `provenance_type: ESTIMATE` when no source directly "
                "establishes it"
            )
        else:
            fallback_rule = (
                "research the value yourself, show the full derivation chain, and mark "
                "it quality `ESTIMATE`"
            )
        body += (
            "\n\n**Research gaps — documented exception to core rule 6 (V3_PLAN.md 3.1).** "
            "The dataset input(s) below are null in the provided record. For these inputs ONLY, "
            + fallback_rule
            + ". Every other dataset input remains provided — do not re-research it.\n\n"
            + gap_lines
        )
    return body


def assemble_one(naics, title, template, template_version):
    block_path = BLOCKS_DIR / f"{naics}.json"
    dataset_path = DERIVED_DIR / f"{naics}.json"
    if not dataset_path.exists():
        fail(naics, f"derived dataset record not found: {dataset_path}")
    try:
        block = json.loads(block_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        fail(naics, f"block file is not valid JSON: {e}")
    dataset = json.loads(dataset_path.read_text(encoding="utf-8"))

    validate_block(naics, block)

    replacements = {
        "{{NAICS}}": naics,
        "{{TITLE}}": title,
        "{{ROLE_HINTS}}": render_role_hints(block),
        "{{SOURCE_HINTS}}": render_source_hints(block),
        "{{CAPTURE_QUESTIONS}}": render_capture_questions(block),
        "{{TERMINAL_VALUE_QUESTION}}": block["terminal_value_question"].strip(),
        "{{SPECIAL_NOTES}}": render_special_notes(block),
        "{{DATASET_INPUTS_JSON}}": render_dataset_inputs(
            naics, block, dataset, template_version
        ),
    }
    text = template
    for ph, value in replacements.items():
        text = text.replace(ph, value)
    return text


def _render_list(items):
    return "\n".join(f"- {item}" for item in items) if items else "- None."


def _render_source_hints_v4_1(hints):
    lines = []
    for item in hints:
        suffix = " Confirm availability before relying on it." if item["uncertain_exists"] else ""
        lines.append(f"- **{item['area']} — {item['source']}**: {item['why']}{suffix}")
    return "\n".join(lines)


def assemble_v4_1_one(naics, title, template):
    """Render v4.1 from a class-neutral spec and its pinned dataset only."""
    spec_path = SPECS_V4_1_DIR / f"{naics}.json"
    spec = _read_json(naics, spec_path, "v4.1 industry spec")
    validate_industry_spec_v4_1(naics, title, spec)

    relative_dataset = Path(spec["dataset_snapshot"]["path"])
    dataset_path = REPO / relative_dataset
    dataset = _read_json(naics, dataset_path, "pinned dataset")
    _require_exact_keys(naics, dataset, V4_1_DATASET_KEYS, "normalized v4.1 dataset")
    if dataset["dataset_version"] != "4.1":
        fail(naics, "normalized dataset version must be exactly 4.1")
    if not isinstance(dataset["snapshot_id"], str) or not dataset["snapshot_id"].strip():
        fail(naics, "normalized dataset snapshot_id must be non-empty")
    if dataset.get("naics") != naics or dataset.get("title") != title:
        fail(naics, "pinned dataset identity differs from industry spec")
    actual_digest = _sha256(dataset_path)
    expected_digest = spec["dataset_snapshot"]["sha256"]
    if actual_digest != expected_digest:
        fail(naics, f"pinned dataset digest mismatch: expected {expected_digest}, got {actual_digest}")
    questions = spec["research_questions"]
    replacements = {
        "{{NAICS}}": naics,
        "{{TITLE}}": title,
        "{{TARGET_ARCHETYPE_JSON}}": json.dumps(spec["target_archetype"], indent=2, ensure_ascii=False),
        "{{VALUE_BASIS_JSON}}": json.dumps(spec["value_basis"], indent=2, ensure_ascii=False),
        "{{DATASET_PATH}}": spec["dataset_snapshot"]["path"],
        "{{DATASET_SHA256}}": expected_digest,
        "{{DATASET_INPUTS_JSON}}": json.dumps(dataset, indent=2, ensure_ascii=False),
        "{{SOURCE_HINTS}}": _render_source_hints_v4_1(spec["source_hints"]),
        "{{IMPLEMENTATION_QUESTIONS}}": _render_list(questions["implementation"]),
        "{{COMMERCIAL_RETENTION_QUESTIONS}}": _render_list(questions["commercial_retention"]),
        "{{SALE_AVAILABILITY_QUESTIONS}}": _render_list(questions["sale_availability"]),
        "{{VALUATION_ROBUSTNESS_QUESTIONS}}": _render_list(questions["valuation_robustness"]),
        "{{SURVIVAL_QUESTIONS}}": _render_list(questions["operator_survival"]),
        "{{SPECIAL_NOTES}}": _render_list(spec["special_notes"]),
    }
    text = template
    for placeholder, value in replacements.items():
        text = text.replace(placeholder, value)
    validate_prompt_text(naics, text, semantic_v4_1=True)
    return text


def assemble_v4_2_one(naics, title, template):
    """Render v4.2 from one outcome-neutral spec and its digest-pinned inputs."""
    semantic_lint_v4_2_spec("TEMPLATE", template, "v4.2 prompt template")
    validate_v4_2_prompt_contract("TEMPLATE", template, "v4.2 prompt template")
    if not SPEC_V4_2_SCHEMA.is_file():
        fail(naics, f"v4.2 industry spec schema not found: {SPEC_V4_2_SCHEMA}")
    spec_path = SPECS_V4_2_DIR / f"{naics}.json"
    spec = _read_json(
        naics, spec_path, "v4.2 industry spec", strict_v4_2=True
    )
    validate_industry_spec_v4_2(naics, title, spec)

    methodology_path = REPO / spec["methodology_snapshot"]["path"]
    if not methodology_path.is_file():
        fail(naics, f"pinned v4.2 methodology not found: {methodology_path}")
    actual_methodology_digest = _sha256(methodology_path)
    expected_methodology_digest = spec["methodology_snapshot"]["sha256"]
    if actual_methodology_digest != expected_methodology_digest:
        fail(
            naics,
            "pinned methodology digest mismatch: expected "
            f"{expected_methodology_digest}, got {actual_methodology_digest}",
        )

    dataset_path = REPO / spec["dataset_snapshot"]["path"]
    dataset = _read_json(
        naics, dataset_path, "pinned v4.2 dataset", strict_v4_2=True
    )
    dataset_schema = _read_json(
        naics, DATASET_V4_2_SCHEMA, "v4.2 dataset schema", strict_v4_2=True
    )
    dataset_schema_violations = _schema_errors(dataset, dataset_schema)
    if dataset_schema_violations:
        fail(
            naics,
            "pinned v4.2 dataset schema validation failed: "
            + "; ".join(dataset_schema_violations[:20]),
        )
    if not isinstance(dataset, dict):
        fail(naics, "pinned v4.2 dataset must be an object")
    required_dataset = {"dataset_version", "snapshot_id", "naics", "title", "n_band", "provenance"}
    missing_dataset = sorted(required_dataset - set(dataset))
    if missing_dataset:
        fail(naics, f"pinned v4.2 dataset missing key(s): {', '.join(missing_dataset)}")
    if dataset["dataset_version"] != "4.2":
        fail(naics, "normalized dataset version must be exactly 4.2")
    if not isinstance(dataset["snapshot_id"], str) or not dataset["snapshot_id"].strip():
        fail(naics, "normalized v4.2 dataset snapshot_id must be non-empty")
    if dataset.get("naics") != naics or dataset.get("title") != title:
        fail(naics, "pinned v4.2 dataset identity differs from industry spec")
    actual_dataset_digest = _sha256(dataset_path)
    expected_dataset_digest = spec["dataset_snapshot"]["sha256"]
    if actual_dataset_digest != expected_dataset_digest:
        fail(
            naics,
            "pinned dataset digest mismatch: expected "
            f"{expected_dataset_digest}, got {actual_dataset_digest}",
        )

    spec_digest = _sha256(spec_path)
    questions = spec["research_questions"]
    replacements = {
        "{{NAICS}}": naics,
        "{{TITLE}}": title,
        "{{SPEC_PATH}}": f"pipeline/specs_v4_2/{naics}.json",
        "{{SPEC_SHA256}}": spec_digest,
        "{{METHODOLOGY_PATH}}": spec["methodology_snapshot"]["path"],
        "{{METHODOLOGY_SHA256}}": expected_methodology_digest,
        "{{DATASET_PATH}}": spec["dataset_snapshot"]["path"],
        "{{DATASET_SHA256}}": expected_dataset_digest,
        "{{INDUSTRY_SPEC_JSON}}": json.dumps(spec, indent=2, ensure_ascii=False),
        "{{DATASET_INPUTS_JSON}}": json.dumps(dataset, indent=2, ensure_ascii=False),
        "{{SOURCE_HINTS}}": _render_source_hints_v4_1(spec["source_hints"]),
        "{{VALUE_ADDED_QUESTIONS}}": _render_list(questions["controllable_value_added"]),
        "{{IMPLEMENTATION_QUESTIONS}}": _render_list(questions["operational_realization"]),
        "{{COMMERCIAL_RETENTION_QUESTIONS}}": _render_list(questions["commercial_retention"]),
        "{{SALE_AVAILABILITY_QUESTIONS}}": _render_list(questions["sale_availability"]),
        "{{BUYER_ACCESS_WIN_QUESTIONS}}": _render_list(questions["buyer_access_win"]),
        "{{VALUATION_ROBUSTNESS_QUESTIONS}}": _render_list(questions["valuation_robustness"]),
        "{{SURVIVAL_QUESTIONS}}": _render_list(questions["operator_survival"]),
        "{{SPECIAL_NOTES}}": _render_list(spec["special_notes"]),
    }
    text = template
    for placeholder, value in replacements.items():
        text = text.replace(placeholder, value)
    validate_prompt_text(naics, text, semantic_v4_2=True, exact_runtime=True)
    return text


def validate_prompt_text(
    naics, text, semantic_v4_1=False, semantic_v4_2=False,
    exact_runtime=False,
):
    leftovers = sorted(set(PLACEHOLDER_RE.findall(text)) - RUNTIME_PLACEHOLDERS)
    if leftovers:
        fail(naics, f"unfilled placeholder(s) in assembled prompt: {', '.join(leftovers)}")
    missing_runtime = sorted(ph for ph in RUNTIME_PLACEHOLDERS if ph not in text)
    if missing_runtime:
        fail(naics, f"runtime placeholder(s) missing from assembled prompt: {', '.join(missing_runtime)}")
    if exact_runtime:
        wrong_counts = sorted(
            placeholder for placeholder in RUNTIME_PLACEHOLDERS
            if text.count(placeholder) != 1
        )
        if wrong_counts:
            fail(
                naics,
                "runtime placeholder(s) must appear exactly once: "
                + ", ".join(wrong_counts),
            )
    if semantic_v4_1:
        semantic_lint_v4_1(naics, text, "assembled prompt")
    if semantic_v4_2:
        semantic_lint_v4_2_spec(naics, text, "assembled v4.2 prompt")
        validate_v4_2_prompt_contract(naics, text, "assembled v4.2 prompt")


def _target_entries(strict_v4_2=False):
    targets = _read_json(
        "TARGETS", TARGETS_PATH, "target membership", strict_v4_2=strict_v4_2
    )
    entries = targets.get("codes") if isinstance(targets, dict) else None
    if not isinstance(entries, list):
        raise AssembleError("[TARGETS] target membership must contain a codes array")
    return entries


def _v4_1_entries(entries, scope, allow_partial):
    if allow_partial and scope != "canary":
        raise AssembleError("[4.1] --allow-partial is permitted only with --scope canary")
    by_code = {entry["naics"]: entry for entry in entries}
    if scope == "canary":
        required = CANARY_V4_1_CODES
    elif scope == "holdout":
        membership = _read_json("HOLDOUT", HOLDOUT_MEMBERSHIP_PATH, "frozen holdout membership")
        if not isinstance(membership, dict) or membership.get("version") != "v4.1-holdout-2026-07-21":
            raise AssembleError("[4.1] frozen holdout membership version is invalid")
        selected = membership.get("selected_codes")
        if selected != list(HOLDOUT_V4_1_CODES) or len(set(selected or [])) != len(HOLDOUT_V4_1_CODES):
            raise AssembleError("[4.1] holdout selected_codes differ from exact frozen membership")
        bins = membership.get("bins")
        if not isinstance(bins, list) or len(bins) != len(HOLDOUT_V4_1_CODES):
            raise AssembleError("[4.1] frozen holdout membership must contain exactly five bins")
        bin_codes = [item.get("selected_naics") if isinstance(item, dict) else None for item in bins]
        if bin_codes != list(HOLDOUT_V4_1_CODES):
            raise AssembleError("[4.1] holdout bins differ from exact frozen membership")
        required = set(HOLDOUT_V4_1_CODES)
    else:
        required = set(by_code)
    if scope == "canary" and not required.issubset(by_code):
        raise AssembleError("[4.1] canary membership is not a subset of frozen targets")
    if scope == "holdout" and not required.issubset(by_code):
        raise AssembleError("[4.1] holdout membership is not a subset of frozen targets")
    available = {
        path.stem for path in SPECS_V4_1_DIR.glob("*.json")
        if re.fullmatch(r"[0-9]{6}", path.stem)
    } if SPECS_V4_1_DIR.is_dir() else set()
    unexpected = sorted(available - set(by_code))
    if unexpected:
        raise AssembleError(f"[4.1] unexpected industry specs outside frozen membership: {' '.join(unexpected)}")
    selected = required & available
    missing = sorted(required - available)
    if missing and not allow_partial:
        raise AssembleError(f"[4.1] missing required {scope} industry specs: {' '.join(missing)}")
    if allow_partial and not selected:
        raise AssembleError("[4.1] partial canary mode requires at least one available canary spec")
    return [by_code[code] for code in sorted(selected)], missing


def _v4_2_entries(entries, scope):
    """Select exact frozen v4.2 scope membership; partial assembly is forbidden."""
    by_code = {entry["naics"]: entry for entry in entries}
    target_codes = set(by_code)
    if len(by_code) != len(entries):
        raise AssembleError("[4.2] frozen target membership contains duplicate codes")

    if scope == "canary":
        membership = _read_json(
            "REGRESSION", REGRESSION_V4_2_MEMBERSHIP_PATH,
            "frozen v4.2 regression membership",
            strict_v4_2=True,
        )
        if not isinstance(membership, dict):
            raise AssembleError("[4.2] frozen regression membership must be an object")
        selected = membership.get("selected_codes")
        exact = sorted(CANARY_V4_2_CODES)
        if membership.get("membership_version") != REGRESSION_V4_2_VERSION:
            raise AssembleError("[4.2] frozen regression membership version is invalid")
        if selected != exact or len(set(selected or [])) != len(exact):
            raise AssembleError("[4.2] regression selected_codes differ from exact frozen membership")
        required = set(exact)
    elif scope == "holdout":
        membership = _read_json(
            "HOLDOUT", HOLDOUT_V4_2_MEMBERSHIP_PATH,
            "frozen v4.2 holdout membership",
            strict_v4_2=True,
        )
        if not isinstance(membership, dict) or membership.get("version") != HOLDOUT_V4_2_VERSION:
            raise AssembleError("[4.2] frozen holdout membership version is invalid")
        selected = membership.get("selected_codes")
        if selected != list(HOLDOUT_V4_2_CODES) or len(set(selected or [])) != 5:
            raise AssembleError("[4.2] holdout selected_codes differ from exact frozen membership")
        bins = membership.get("bins")
        if not isinstance(bins, list) or len(bins) != 5:
            raise AssembleError("[4.2] frozen holdout membership must contain exactly five bins")
        bin_codes = [item.get("selected_naics") if isinstance(item, dict) else None for item in bins]
        if bin_codes != selected:
            raise AssembleError("[4.2] holdout bins differ from exact selected_codes membership")
        if set(selected) & CANARY_V4_2_CODES:
            raise AssembleError("[4.2] frozen holdout membership overlaps the regression set")
        method_records = [
            item for item in membership.get("source_digests", [])
            if isinstance(item, dict) and item.get("path") == "V4_2_METHODOLOGY.md"
        ]
        if len(method_records) != 1 or method_records[0].get("sha256") != _sha256(GOVERNANCE_METHODOLOGY_V4_2_PATH):
            raise AssembleError("[4.2] holdout authority does not bind the current methodology digest")
        required = set(selected)
    else:
        if len(target_codes) != 63:
            raise AssembleError(
                f"[4.2] full frozen target membership must contain exactly 63 codes (got {len(target_codes)})"
            )
        required = target_codes

    if not required.issubset(target_codes):
        raise AssembleError(f"[4.2] {scope} membership is not a subset of frozen targets")
    available = {
        path.stem for path in SPECS_V4_2_DIR.glob("*.json")
        if re.fullmatch(r"[0-9]{6}", path.stem)
    } if SPECS_V4_2_DIR.is_dir() else set()
    unexpected = sorted(available - target_codes)
    if unexpected:
        raise AssembleError(
            "[4.2] unexpected industry specs outside frozen membership: "
            + " ".join(unexpected)
        )
    missing = sorted(required - available)
    if missing:
        raise AssembleError(
            f"[4.2] missing required {scope} industry specs: " + " ".join(missing)
        )
    return [by_code[code] for code in sorted(required)], []


def main(argv=None):
    parser = argparse.ArgumentParser(description="Assemble versioned per-code prompts deterministically.")
    parser.add_argument("--check", action="store_true", help="Validate only: re-render in memory and compare against prompts on disk; write nothing.")
    parser.add_argument("--lint", action="store_true", help="Run semantic lint. This is automatic for v4.1 and accepted for explicit preflight commands.")
    parser.add_argument(
        "--scope", choices=("canary", "holdout", "full"), default="full",
        help="v4.1/v4.2 membership scope. Canary and holdout are exact frozen sets; full requires all targets.",
    )
    parser.add_argument(
        "--allow-partial", action="store_true",
        help="v4.1 canary only: process the available non-empty subset while specs arrive.",
    )
    parser.add_argument(
        "--template-version",
        choices=sorted(VERSION_PATHS),
        default="3.0",
        help="Contract to assemble. Defaults to 3.0 so existing prompts remain untouched.",
    )
    args = parser.parse_args(argv)

    if args.template_version not in ("4.1", "4.2") and (
        args.scope != "full" or args.allow_partial or args.lint
    ):
        parser.error("--scope, --allow-partial, and --lint are v4.1/v4.2-only options")
    if args.template_version == "4.2" and args.allow_partial:
        parser.error("--allow-partial is forbidden for v4.2")

    try:
        target_entries = _target_entries(strict_v4_2=args.template_version == "4.2")
        version_paths = VERSION_PATHS[args.template_version]
        template = version_paths["template"].read_text(encoding="utf-8")
        prompts_dir = version_paths["prompts"]
        if args.template_version == "4.1":
            semantic_lint_v4_1("TEMPLATE", template, "v4.1 prompt template")
            selected_entries, missing_specs = _v4_1_entries(target_entries, args.scope, args.allow_partial)
        elif args.template_version == "4.2":
            semantic_lint_v4_2_spec("TEMPLATE", template, "v4.2 prompt template")
            validate_v4_2_prompt_contract("TEMPLATE", template, "v4.2 prompt template")
            selected_entries, missing_specs = _v4_2_entries(target_entries, args.scope)
        else:
            selected_entries, missing_specs = target_entries, []
    except (AssembleError, OSError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1
    if not args.check:
        prompts_dir.mkdir(parents=True, exist_ok=True)

    skipped, written, checked, errors = [], [], [], []

    for entry in selected_entries:
        naics, title = entry["naics"], entry["title"]
        if args.template_version not in ("4.1", "4.2"):
            block_path = BLOCKS_DIR / f"{naics}.json"
            if not block_path.exists():
                skipped.append(naics)
                continue
        try:
            if args.template_version == "4.1":
                text = assemble_v4_1_one(naics, title, template)
            elif args.template_version == "4.2":
                text = assemble_v4_2_one(naics, title, template)
            else:
                text = assemble_one(naics, title, template, args.template_version)
                validate_prompt_text(naics, text)
            out_path = prompts_dir / f"{naics}.md"
            if args.check:
                if not out_path.exists():
                    fail(naics, f"--check: prompt file missing on disk: {out_path}")
                on_disk = out_path.read_text(encoding="utf-8")
                if on_disk != text:
                    fail(naics, f"--check: {out_path} differs from freshly assembled text (stale — re-run assemble_prompts.py)")
                checked.append(naics)
            else:
                out_path.write_text(text, encoding="utf-8")
                written.append(naics)
        except AssembleError as e:
            errors.append(str(e))

    if args.template_version in ("4.1", "4.2") and args.scope == "full" and not errors:
        actual_prompts = {
            path.stem for path in prompts_dir.glob("*.md")
            if re.fullmatch(r"[0-9]{6}", path.stem)
        } if prompts_dir.is_dir() else set()
        expected_prompts = {entry["naics"] for entry in target_entries}
        if actual_prompts != expected_prompts:
            errors.append(
                "[%s] full prompt membership mismatch: missing=%s unexpected=%s" % (
                    args.template_version,
                    " ".join(sorted(expected_prompts - actual_prompts)) or "none",
                    " ".join(sorted(actual_prompts - expected_prompts)) or "none",
                )
            )

    if skipped:
        print(f"WARNING: {len(skipped)} code(s) skipped — no block file yet in {BLOCKS_DIR}/:")
        print("  " + " ".join(skipped))
    if written:
        print(f"OK: wrote {len(written)} prompt(s) to {prompts_dir}/: " + " ".join(written))
    if checked:
        print(f"OK: {len(checked)} prompt(s) validated against disk: " + " ".join(checked))
    if missing_specs and args.allow_partial:
        print(f"PARTIAL: {len(missing_specs)} canary spec(s) not present yet: " + " ".join(missing_specs))
    if errors:
        print(f"FAIL: {len(errors)} error(s):", file=sys.stderr)
        for e in errors:
            print("  " + e, file=sys.stderr)
        return 1
    if not (written or checked or skipped):
        print("Nothing to do: targets list is empty.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
