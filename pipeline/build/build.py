#!/usr/bin/env python3
"""v3 build & check — Stage 4 (V3_PRODUCT.md §6), Phase 2 (V3_PLAN.md).

Deterministic, stdlib-only, no model calls. Per run record in pipeline/runs/:
  1. versioned schema validation (v3.0 legacy through finalized v3.1.2)
  2. arithmetic recompute from stored inputs with the frozen template-3.0
     formulas — hard fail if |stored - recomputed| > 0.005 on any factor or S
  3. verdicts / gates / caps / borderline / percentile from thresholds.json
     (every cut, gate and cap is read from that file — nothing hardcoded)
  4. publication filter: v3.1.2 includes `publishable` and
     `publishable_with_caveats`; earlier versions retain accepted/wrong routing
  5. outputs: 6digit/six_data_v3.json, pipeline/build/stats.json,
     pipeline/build/flags.json, pipeline/build/reconciliation.md

Usage: python3 pipeline/build/build.py [--allow-unreviewed]
"""

import argparse
import hashlib
import importlib.util
import json
import math
import os
import re
import sys

# Absolute tolerance for stored-vs-recomputed comparison (build check
# parameter, not a rubric threshold — rubric numbers live in thresholds.json).
ARITH_TOL = 0.005

# Six-digit NAICS service universe size; replace with a datasets-derived count
# once Phase 1 lands (pipeline/datasets/ coverage report).
CODES_UNIVERSE = 1012

SECTOR_NAMES = {
    "11": "Agriculture, Forestry, Fishing and Hunting",
    "21": "Mining, Quarrying, and Oil and Gas Extraction",
    "22": "Utilities",
    "23": "Construction",
    "31": "Manufacturing", "32": "Manufacturing", "33": "Manufacturing",
    "42": "Wholesale Trade",
    "44": "Retail Trade", "45": "Retail Trade",
    "48": "Transportation and Warehousing", "49": "Transportation and Warehousing",
    "51": "Information",
    "52": "Finance and Insurance",
    "53": "Real Estate and Rental and Leasing",
    "54": "Professional, Scientific, and Technical Services",
    "55": "Management of Companies and Enterprises",
    "56": "Administrative and Support and Waste Management and Remediation Services",
    "61": "Educational Services",
    "62": "Health Care and Social Assistance",
    "71": "Arts, Entertainment, and Recreation",
    "72": "Accommodation and Food Services",
    "81": "Other Services (except Public Administration)",
    "92": "Public Administration",
}

CONF_RANK = {"LOW": 0, "MED": 1, "HIGH": 2}
URL_RE = re.compile(r"https?://[^\s<>\"']+")
SUPPORTED_TEMPLATE_VERSIONS = ("3.0", "3.1", "3.1.1", "3.1.2")
_V311_CONTRACT = None


# ---------------------------------------------------------------------------
# Minimal JSON-Schema (draft-07 subset) validator — jsonschema is unavailable
# in this environment (PEP 668). Covers everything our schemas use:
# type, required, properties, additionalProperties, enum, const, pattern,
# minLength, minimum/maximum/exclusiveMinimum, minItems/maxItems, items,
# contains, allOf, $ref (#/definitions/...), if/then/else. "format" is
# annotation-only (as in draft-07 default) and is ignored.
# ---------------------------------------------------------------------------

def _type_ok(value, t):
    if t == "object":
        return isinstance(value, dict)
    if t == "array":
        return isinstance(value, list)
    if t == "string":
        return isinstance(value, str)
    if t == "number":
        return (
            isinstance(value, (int, float))
            and not isinstance(value, bool)
            and math.isfinite(float(value))
        )
    if t == "integer":
        return (
            isinstance(value, (int, float))
            and not isinstance(value, bool)
            and math.isfinite(float(value))
            and float(value).is_integer()
        )
    if t == "boolean":
        return isinstance(value, bool)
    if t == "null":
        return value is None
    return True


def _resolve_ref(ref, root):
    node = root
    for part in ref.lstrip("#/").split("/"):
        node = node[part]
    return node


def schema_errors(value, schema, root, path="$"):
    """Return a list of human-readable validation errors (empty = valid)."""
    errs = []
    if "$ref" in schema:
        return schema_errors(value, _resolve_ref(schema["$ref"], root), root, path)
    for subschema in schema.get("allOf", []):
        errs.extend(schema_errors(value, subschema, root, path))

    t = schema.get("type")
    if t is not None:
        types = t if isinstance(t, list) else [t]
        if not any(_type_ok(value, x) for x in types):
            return ["%s: expected type %s, got %s" % (path, t, type(value).__name__)]

    if "enum" in schema and value not in schema["enum"]:
        errs.append("%s: %r not one of %s" % (path, value, schema["enum"]))
    if "const" in schema and value != schema["const"]:
        errs.append("%s: %r != const %r" % (path, value, schema["const"]))

    if isinstance(value, str):
        if "pattern" in schema and not re.search(schema["pattern"], value):
            errs.append("%s: %r does not match pattern %s" % (path, value, schema["pattern"]))
        if "minLength" in schema and len(value) < schema["minLength"]:
            errs.append("%s: string shorter than minLength %d" % (path, schema["minLength"]))

    if isinstance(value, (int, float)) and not isinstance(value, bool):
        if "minimum" in schema and value < schema["minimum"]:
            errs.append("%s: %s < minimum %s" % (path, value, schema["minimum"]))
        if "maximum" in schema and value > schema["maximum"]:
            errs.append("%s: %s > maximum %s" % (path, value, schema["maximum"]))
        if "exclusiveMinimum" in schema and value <= schema["exclusiveMinimum"]:
            errs.append("%s: %s <= exclusiveMinimum %s" % (path, value, schema["exclusiveMinimum"]))

    if isinstance(value, dict):
        for key in schema.get("required", []):
            if key not in value:
                errs.append("%s: missing required key %r" % (path, key))
        props = schema.get("properties", {})
        for key, sub in props.items():
            if key in value:
                errs.extend(schema_errors(value[key], sub, root, "%s.%s" % (path, key)))
        if schema.get("additionalProperties") is False:
            for key in value:
                if key not in props:
                    errs.append("%s: additional property %r not allowed" % (path, key))

    if isinstance(value, list):
        if "minItems" in schema and len(value) < schema["minItems"]:
            errs.append("%s: fewer than minItems %d" % (path, schema["minItems"]))
        if "maxItems" in schema and len(value) > schema["maxItems"]:
            errs.append("%s: more than maxItems %d" % (path, schema["maxItems"]))
        if "items" in schema:
            for i, item in enumerate(value):
                errs.extend(schema_errors(item, schema["items"], root, "%s[%d]" % (path, i)))
        if "contains" in schema:
            if not any(not schema_errors(item, schema["contains"], root, path) for item in value):
                errs.append("%s: no item satisfies 'contains' %s" % (path, json.dumps(schema["contains"])))

    if "if" in schema:
        condition_matches = not schema_errors(value, schema["if"], root, path)
        if condition_matches and "then" in schema:
            errs.extend(schema_errors(value, schema["then"], root, path))
        elif not condition_matches and "else" in schema:
            errs.extend(schema_errors(value, schema["else"], root, path))

    return errs


def evidence_contract_errors(record):
    """Return finalized v3.1.1 evidence errors; older versions are untouched."""
    global _V311_CONTRACT
    if record.get("run_meta", {}).get("template_version") != "3.1.1":
        return []
    if _V311_CONTRACT is None:
        contract_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "evidence_contract_v3_1_1.py",
        )
        spec = importlib.util.spec_from_file_location(
            "evidence_contract_v311_build", contract_path
        )
        _V311_CONTRACT = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(_V311_CONTRACT)
    return _V311_CONTRACT.final_record_semantic_errors(record)


# ---------------------------------------------------------------------------
# Arithmetic calculation/recompute — frozen formulas shared by all v3 versions.
# v3.1+ clarifies the already-at-50% t50 boundary: t50=0 maps to A=10.
# ---------------------------------------------------------------------------

def clamp(x, lo, hi):
    return max(lo, min(hi, x))


def calculate(rec):
    """Calculate factor scores and S from inputs, without trusting stored scores.

    v3.1+ finalization uses this function to write scores in plain Python.
    Returns (computed: dict, errors: list).
    """
    naics = rec["naics"]
    errs = []
    ds = rec["dataset_inputs"]
    inp = rec["inputs"]

    ars_sum = sum(
        role["labor_share_of_total"] * role["within_role_automatable_fraction"]
        for role in inp["ai_replaceable_share"]["breakdown_by_role"]
    )

    labor_share = ds["labor_share"]["value"]
    uses_v31_semantics = rec.get("run_meta", {}).get("template_version") in (
        "3.1", "3.1.1", "3.1.2"
    )
    # Preserve v3.0 recompute semantics for frozen historical artifacts. v3.1
    # uses the Python-calculated role sum directly; its stored value is output,
    # not model input.
    ars_for_score = (
        ars_sum if uses_v31_semantics else inp["ai_replaceable_share"]["value"]
    )
    v_raw = labor_share * ars_for_score
    V = 10.0 * min(1.0, v_raw / 0.25)
    C = 10.0 * inp["pi_dist"]["value"] * inp["pi_moat"]["value"]

    adoption = inp["current_adoption_pct"]["value"]
    t50 = inp["t50_years"]["value"]
    if uses_v31_semantics and isinstance(adoption, (int, float)) and not isinstance(adoption, bool):
        if adoption >= 0.5 and t50 != 0:
            errs.append(
                "%s: v3.1+ t50_years must be 0 when current_adoption_pct >= 0.5"
                % naics
            )
        if adoption < 0.5 and t50 <= 0:
            errs.append(
                "%s: v3.1+ t50_years must be > 0 when current_adoption_pct < 0.5"
                % naics
            )
    if t50 < 0:
        errs.append("%s: t50_years must be >= 0, got %s" % (naics, t50))
        A = 0.0
    elif t50 == 0:
        A = 10.0
    else:
        A = min(10.0, 10.0 / t50)

    n_band = ds["n_band"]["value"]
    TD = clamp(math.log10(n_band) / 4.0, 0.0, 1.0) if n_band >= 1 else 0.0
    owners = inp["owners_60plus_pct"]
    OW = clamp((owners["value"] - 0.10) / 0.35, 0.1, 0.9)
    if owners["succession_shortage_documented"]["value"]:
        OW = min(1.0, OW + 0.1)
    consolidators = inp["active_consolidators"]["value"]
    if consolidators < 0:
        errs.append("%s: active_consolidators must be >= 0, got %s"
                    % (naics, consolidators))
        consolidators = 0
    CFD = min(0.9, math.log10(1 + consolidators) / 2.0)
    B = 10.0 * math.sqrt(TD * OW) / (1.0 + 0.3 * CFD)

    buy = inp["buy_mult"]["value"]
    exit_ = inp["exit_mult"]["value"]
    if buy <= 0:
        errs.append("%s: buy_mult must be > 0, got %s" % (naics, buy))
        M = 0.0
    else:
        M = clamp(4.0 * (exit_ - buy) / buy, 0.0, 10.0)

    S = (V * C * A * B * M) ** 0.2
    return {
        "V": V,
        "C": C,
        "A": A,
        "B": B,
        "M": M,
        "S": S,
        "V_raw": v_raw,
        "TD": TD,
        "OW": OW,
        "CFD": CFD,
        "ai_replaceable_share": ars_sum,
    }, errs


def recompute(rec):
    """Recompute all factor scores and S from stored inputs.

    Returns (computed: dict, errors: list, deltas: dict). errors non-empty =
    the record's own numbers cannot be reproduced (hard build failure).
    """
    naics = rec["naics"]
    errs = []
    deltas = {}
    inp = rec["inputs"]

    def check(name, stored, recomputed):
        d = abs(stored - recomputed)
        deltas[name] = d
        if d > ARITH_TOL:
            errs.append("%s: %s stored=%.6f recomputed=%.6f |delta|=%.6f > %s"
                        % (naics, name, stored, recomputed, d, ARITH_TOL))

    computed, calc_errs = calculate(rec)
    errs.extend(calc_errs)

    # ai_replaceable_share = sum(role contributions); each contribution checked
    ars = inp["ai_replaceable_share"]
    for i, role in enumerate(ars["breakdown_by_role"]):
        contrib = role["labor_share_of_total"] * role["within_role_automatable_fraction"]
        check("ai_replaceable_share.breakdown_by_role[%d](%s).contribution" % (i, role["role"]),
              role["contribution"], contrib)
    check("ai_replaceable_share", ars["value"], computed["ai_replaceable_share"])
    for f in ["V", "C", "A", "B", "M"]:
        check(f, rec["scores"][f]["score"], computed[f])
    check("S", rec["S"], computed["S"])
    return computed, errs, deltas


# ---------------------------------------------------------------------------
# Verdict engine — every number/name read from thresholds.json.
# ---------------------------------------------------------------------------

def decide(S, factors, terminal, confidence, th):
    """Return dict: verdict, gate_blocked, capped_by, borderline, nearest_cut."""
    cuts = sorted(th["verdict_cuts"].items(), key=lambda kv: -kv[1])
    verdict_rank = {"kill": 0}
    for i, (name, _) in enumerate(reversed(cuts)):
        verdict_rank[name] = i + 1

    gate_blocked = False
    capped_by = []

    if any(v < th["kill"]["any_factor_below"] for v in factors.values()):
        verdict = "kill"
        killed_by_floor = True
    else:
        killed_by_floor = False
        verdict = "kill"
        for name, cut in cuts:
            if S >= cut:
                verdict = name
                break
        # hell_yes gates (P6): S clearing the cut is necessary, not sufficient
        gates = th.get("gates", {})
        if verdict in gates:
            g = gates[verdict]
            ok = (all(v >= g["min_each_factor"] for v in factors.values())
                  and terminal in g["terminal_value"]
                  and CONF_RANK[confidence] >= CONF_RANK[g["min_confidence"]])
            if not ok:
                gate_blocked = True
                idx = [n for n, _ in cuts].index(verdict)
                verdict = cuts[idx + 1][0] if idx + 1 < len(cuts) else "kill"
        # caps from T and confidence
        for cap_kind, key in [("terminal_value", terminal), ("confidence", confidence)]:
            cap = th["caps"].get(cap_kind, {}).get(key)
            if cap is not None and verdict_rank[verdict] > verdict_rank[cap]:
                verdict = cap
                capped_by.append("%s:%s" % (cap_kind, key))

    nearest_name, nearest_cut = min(cuts, key=lambda kv: abs(S - kv[1]))
    borderline = abs(S - nearest_cut) <= th["borderline_epsilon"]
    return {
        "verdict": verdict,
        "killed_by_factor_floor": killed_by_floor,
        "gate_blocked": gate_blocked,
        "capped_by": capped_by,
        "borderline": borderline,
        "nearest_cut": {"name": nearest_name, "value": nearest_cut,
                        "distance": abs(S - nearest_cut)},
    }


# ---------------------------------------------------------------------------
# Record discovery & acceptance
# ---------------------------------------------------------------------------

def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def sha256_file(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _trim_embedded_url(url):
    """Remove prose punctuation while preserving balanced URL parentheses."""
    url = url.rstrip(".,;:]}")
    while url.endswith(")") and url.count(")") > url.count("("):
        url = url[:-1]
    return url


def source_audit_pairs(record):
    """Return every distinct (JSON path, HTTP(S) URL) citation in a record."""
    found = set()

    def walk(value, path):
        if isinstance(value, dict):
            for key in sorted(value):
                child_path = "%s.%s" % (path, key) if path else key
                walk(value[key], child_path)
        elif isinstance(value, list):
            for index, item in enumerate(value):
                walk(item, "%s[%d]" % (path, index))
        elif isinstance(value, str):
            for match in URL_RE.findall(value):
                url = _trim_embedded_url(match)
                if url:
                    found.add((path, url))

    walk(record, "")
    return [
        {"input_path": path, "url": url}
        for path, url in sorted(found, key=lambda pair: (pair[0], pair[1]))
    ]


def v312_score_driving_source_ids(record):
    """Return source IDs referenced by a v3.1.2 finalized score input."""
    found = set()

    def walk(value):
        if isinstance(value, dict):
            ids = value.get("source_ids")
            if isinstance(ids, list):
                found.update(item for item in ids if isinstance(item, str))
            for child in value.values():
                walk(child)
        elif isinstance(value, list):
            for child in value:
                walk(child)

    walk(record.get("inputs", {}))
    for name in ("labor_share", "n_band"):
        value = record.get("dataset_inputs", {}).get(name)
        if isinstance(value, dict) and value.get("provenance_type"):
            walk(value)
    return found


def v312_declared_caveats(record):
    """Canonical publication strings for model-authored score-input caveats."""
    found = []

    def add(path, value):
        if not isinstance(value, dict):
            return
        for caveat in value.get("caveats", []):
            found.append("%s: %s" % (path, caveat))
        if path == "inputs.owners_60plus_pct":
            add(path + ".succession_shortage_documented",
                value.get("succession_shortage_documented"))

    for name, value in record.get("inputs", {}).items():
        add("inputs.%s" % name, value)
    for name in ("labor_share", "n_band"):
        value = record.get("dataset_inputs", {}).get(name)
        if isinstance(value, dict) and value.get("provenance_type"):
            add("dataset_inputs.%s" % name, value)
    return found


def discover_runs(runs_dir):
    """Latest v3 run record per code (by run_date, then run_id).

    Returns (records: {naics: (path, record)}, legacy_skipped: [paths]).
    Files without a v3 run_meta block (e.g. the archived tv2 prototype) are
    skipped as legacy, not validated.
    """
    records, legacy = {}, []
    for naics in sorted(os.listdir(runs_dir)):
        d = os.path.join(runs_dir, naics)
        if not (os.path.isdir(d) and re.fullmatch(r"[0-9]{6}", naics)):
            continue
        candidates = []
        for fn in sorted(os.listdir(d)):
            if not fn.endswith(".json"):
                continue
            path = os.path.join(d, fn)
            rec = load_json(path)
            meta = rec.get("run_meta")
            if not (isinstance(meta, dict)
                    and str(meta.get("template_version", "")).startswith("3")):
                legacy.append(path)
                continue
            candidates.append((str(meta.get("run_date", "")), str(meta.get("run_id", "")), path, rec))
        if candidates:
            candidates.sort(key=lambda c: (c[0], c[1]))
            _, _, path, rec = candidates[-1]
            records[naics] = (path, rec)
    return records, legacy


def acceptance_status(naics, rec, review_dir, review_schema,
                      expected_source_audits, expected_flags,
                      expected_artifact_digests=None):
    """Return (status, review_summary, errors). status: accepted|pending|rejected."""
    run_id = rec["run_meta"]["run_id"]
    if (not run_id or os.path.basename(run_id) != run_id
            or os.path.sep in run_id
            or (os.path.altsep and os.path.altsep in run_id)):
        return "pending", {"note": "unsafe run_id cannot be mapped to a review file"}, [
            "%s (review): unsafe run_id %r" % (naics, run_id)
        ]
    path = os.path.join(review_dir, naics, run_id + ".json")
    if not os.path.isfile(path):
        return "pending", {"note": "no review record for run_id %r" % run_id}, []
    review = load_json(path)
    template_version = rec.get("run_meta", {}).get("template_version")
    errs = ["%s (review): %s" % (naics, e)
            for e in schema_errors(review, review_schema, review_schema)]
    if review.get("naics") != naics:
        errs.append("%s (review): review naics %r does not match directory %r"
                    % (naics, review.get("naics"), naics))
    if review.get("run_id") != run_id:
        errs.append("%s (review): review run_id %r does not match current run_id %r"
                    % (naics, review.get("run_id"), run_id))
    if template_version == "3.1.2":
        if review.get("artifact_digests") != expected_artifact_digests:
            errs.append("%s (review): artifact digests do not match exact packet/run/memo bytes" % naics)
        score_driving_ids = v312_score_driving_source_ids(rec)
        actual_sources = [
            (item.get("source_id"), item.get("url"))
            for item in review.get("source_reviews", [])
            if isinstance(item, dict)
        ]
        expected_sources = [(item["id"], item["url"]) for item in rec["sources"]]
        if len(actual_sources) != len(set(actual_sources)):
            errs.append("%s (review): source_reviews contains duplicates" % naics)
        if set(actual_sources) != set(expected_sources):
            errs.append(
                "%s (review): source review coverage mismatch: missing=%s unexpected=%s"
                % (naics, sorted(set(expected_sources) - set(actual_sources)),
                   sorted(set(actual_sources) - set(expected_sources)))
            )
        source_review_by_id = {
            item.get("source_id"): item
            for item in review.get("source_reviews", [])
            if isinstance(item, dict)
        }
        for source in rec["sources"]:
            source_id = source["id"]
            item = source_review_by_id.get(source_id, {})
            expected_driving = source_id in score_driving_ids
            if item.get("score_driving") is not expected_driving:
                errs.append(
                    "%s (review): source %s score_driving must be %s"
                    % (naics, source_id, expected_driving)
                )
        mechanics = review.get("mechanics", {})
        mechanics_ok = isinstance(mechanics, dict) and mechanics and all(
            value is True for value in mechanics.values()
        )
        findings = review.get("findings", [])
        severities = [item.get("severity") for item in findings if isinstance(item, dict)]
        outcome = review.get("outcome")
        declared_caveats = v312_declared_caveats(rec)
        publication_caveats = review.get("publication_caveats", [])
        missing_declared = sorted(set(declared_caveats) - set(publication_caveats))
        if missing_declared:
            errs.append(
                "%s (review): publication_caveats omit authored caveats %s"
                % (naics, missing_declared)
            )
        driving_failures = [
            item for source_id, item in source_review_by_id.items()
            if source_id in score_driving_ids
            and (item.get("accessible") is not True
                 or item.get("support") in ("unsupported", "not_score_driving"))
        ]
        caveat_finding_text = [
            item.get("publication_caveat") for item in findings
            if isinstance(item, dict) and item.get("severity") == "caveat"
        ]
        if any(not value or value not in publication_caveats for value in caveat_finding_text):
            errs.append("%s (review): every caveat finding must be copied to publication_caveats" % naics)
        if driving_failures and mechanics_ok and outcome != "reject":
            errs.append(
                "%s (review): inaccessible/unsupported score-driving evidence requires reject"
                % naics
            )
        if (not mechanics_ok or "fatal_mechanics" in severities) and outcome != "invalid":
            errs.append("%s (review): failed mechanics requires invalid" % naics)
        if outcome == "publishable" and (findings or publication_caveats or declared_caveats):
            errs.append("%s (review): publishable requires no findings or caveats" % naics)
        if outcome == "publishable_with_caveats":
            if not mechanics_ok:
                errs.append("%s (review): publishable_with_caveats requires all mechanics" % naics)
            if any(value != "caveat" for value in severities):
                errs.append("%s (review): publishable_with_caveats allows caveat findings only" % naics)
            if not publication_caveats:
                errs.append("%s (review): caveat outcome requires publication_caveats" % naics)
        if outcome == "publishable" and not mechanics_ok:
            errs.append("%s (review): publishable requires all mechanics" % naics)
        if outcome == "reject":
            if not mechanics_ok:
                errs.append("%s (review): reject requires mechanics pass; otherwise invalid" % naics)
            if "material" not in severities:
                errs.append("%s (review): reject requires a material finding" % naics)
            if "fatal_mechanics" in severities:
                errs.append("%s (review): fatal_mechanics requires invalid, never reject" % naics)
        if outcome == "invalid" and mechanics_ok and "fatal_mechanics" not in severities:
            errs.append("%s (review): invalid requires failed mechanics or fatal_mechanics" % naics)
        if outcome in ("publishable", "publishable_with_caveats") and any(
                value in ("material", "fatal_mechanics") for value in severities):
            errs.append("%s (review): publishable outcomes cannot contain material/fatal findings" % naics)
        if errs:
            return "pending", {"note": "invalid review record"}, errs
        summary = {
            "run_id": review["run_id"],
            "model_id": review["review_meta"]["model_id"],
            "review_date": review["review_meta"]["review_date"],
            "prompt_version": review["review_meta"]["prompt_version"],
            "outcome": outcome,
            "publication_caveats": review["publication_caveats"],
            "summary": review["summary"],
        }
        return ("accepted" if outcome in ("publishable", "publishable_with_caveats") else "rejected"), summary, []

    expected_review_prompt = {
        "3.1": "validator-3.1",
        "3.1.1": "validator-3.1.1",
    }.get(rec.get("run_meta", {}).get("template_version"))
    actual_review_prompt = review.get("review_meta", {}).get("prompt_version")
    if (expected_review_prompt is not None
            and actual_review_prompt != expected_review_prompt):
        errs.append(
            "%s (review): review prompt_version %r does not match required %r"
            % (naics, actual_review_prompt, expected_review_prompt)
        )
    expected_review_model = {
        "3.1.1": "gpt-5.6-sol",
    }.get(rec.get("run_meta", {}).get("template_version"))
    actual_review_model = review.get("review_meta", {}).get("model_id")
    if (expected_review_model is not None
            and actual_review_model != expected_review_model):
        errs.append(
            "%s (review): review model_id %r does not match required %r"
            % (naics, actual_review_model, expected_review_model)
        )
    raw_audits = review.get("source_audits", [])
    if not isinstance(raw_audits, list):
        raw_audits = []
    actual_audits = [
        (audit.get("input_path"), audit.get("url"))
        for audit in raw_audits
        if isinstance(audit, dict)
    ]
    expected_audits = {
        (audit["input_path"], audit["url"])
        for audit in expected_source_audits
    }
    actual_audit_set = set(actual_audits)
    if len(actual_audits) != len(actual_audit_set):
        errs.append("%s (review): source_audits contains duplicate input_path/url pairs"
                    % naics)
    if actual_audit_set != expected_audits:
        errs.append("%s (review): source_audits coverage mismatch: missing=%s unexpected=%s"
                    % (naics,
                       sorted(expected_audits - actual_audit_set),
                       sorted(actual_audit_set - expected_audits)))
    raw_flags = review.get("flags_reviewed", [])
    if not isinstance(raw_flags, list):
        raw_flags = []
    actual_flag_set = set(raw_flags) if all(
        isinstance(flag, str) for flag in raw_flags
    ) else set()
    expected_flag_set = set(expected_flags)
    if len(raw_flags) != len(actual_flag_set):
        errs.append("%s (review): flags_reviewed contains duplicate or invalid flags"
                    % naics)
    if actual_flag_set != expected_flag_set:
        errs.append("%s (review): flags_reviewed coverage mismatch: missing=%s unexpected=%s"
                    % (naics,
                       sorted(expected_flag_set - actual_flag_set),
                       sorted(actual_flag_set - expected_flag_set)))
    if errs:
        return "pending", {"note": "invalid review record"}, errs
    summary = {
        "run_id": review["run_id"],
        "model_id": review["review_meta"]["model_id"],
        "review_date": review["review_meta"]["review_date"],
        "prompt_version": review["review_meta"]["prompt_version"],
        "verdict": review["verdict"],
    }
    if review["verdict"] == "wrong":
        summary["reasons"] = review["reasons"]
        return "rejected", summary, []
    return "accepted", summary, []


# ---------------------------------------------------------------------------
# Flags for the Stage-5 validator
# ---------------------------------------------------------------------------

def record_flags(rec, computed, decision, deltas):
    flags = []
    if rec["confidence_overall"] == "LOW":
        flags.append("LOW_CONFIDENCE")
    if decision["borderline"]:
        flags.append("BORDERLINE: |S - %s cut %.2f| = %.4f"
                     % (decision["nearest_cut"]["name"], decision["nearest_cut"]["value"],
                        decision["nearest_cut"]["distance"]))
    if decision["gate_blocked"]:
        flags.append("GATE_BLOCKED: S cleared the top cut but a hell_yes gate failed")
    uplift = rec["cross_checks"]["uplift_pp"]
    if uplift < 3 and computed["A"] >= 5:
        flags.append("CROSS_CHECK_TENSION: uplift_pp %.2f < 3 while A %.2f >= 5"
                     % (uplift, computed["A"]))
    inp = rec["inputs"]
    if rec.get("run_meta", {}).get("template_version") in ("3.1", "3.1.1", "3.1.2"):
        estimates = sorted(
            name for name, value in inp.items()
            if isinstance(value, dict)
            and value.get("provenance_type") == "ESTIMATE"
        )
        estimates.extend(sorted(
            "dataset_inputs.%s" % name
            for name in ("labor_share", "n_band")
            if isinstance(rec.get("dataset_inputs", {}).get(name), dict)
            and rec["dataset_inputs"][name].get("provenance_type") == "ESTIMATE"
        ))
        if rec.get("run_meta", {}).get("template_version") in ("3.1.1", "3.1.2"):
            succession = inp.get("owners_60plus_pct", {}).get(
                "succession_shortage_documented", {}
            )
            if succession.get("provenance_type") == "ESTIMATE":
                estimates.append(
                    "owners_60plus_pct.succession_shortage_documented"
                )
        estimate_label = "provenance_type ESTIMATE"
    else:
        estimates = sorted(name for name, value in inp.items()
                           if isinstance(value, dict)
                           and value.get("quality") == "ESTIMATE")
        estimate_label = "quality ESTIMATE"
    if len(estimates) >= 3:
        flags.append("ESTIMATE_HEAVY: %d inputs with %s (%s)"
                     % (len(estimates), estimate_label, ", ".join(estimates)))
    nonzero = sorted(name for name, d in deltas.items() if 1e-12 < d <= ARITH_TOL)
    if nonzero:
        flags.append("ARITH_DELTA_WITHIN_TOL: nonzero stored-vs-recomputed deltas on %s"
                     % ", ".join(nonzero))
    return flags


# ---------------------------------------------------------------------------
# Build
# ---------------------------------------------------------------------------

def run_build(repo_root, allow_unreviewed=False, runs_dir=None, review_dir=None,
              thresholds_path=None, schemas_dir=None, expectations_path=None,
              site_out=None, stats_out=None, flags_out=None, reconciliation_out=None):
    runs_dir = runs_dir or os.path.join(repo_root, "pipeline", "runs")
    review_dir = review_dir or os.path.join(repo_root, "pipeline", "review")
    thresholds_path = thresholds_path or os.path.join(repo_root, "pipeline", "build", "thresholds.json")
    schemas_dir = schemas_dir or os.path.join(repo_root, "pipeline", "build", "schemas")
    expectations_path = expectations_path or os.path.join(repo_root, "pipeline", "build", "deep_dive_expectations.json")
    site_out = site_out or os.path.join(repo_root, "6digit", "six_data_v3.json")
    stats_out = stats_out or os.path.join(repo_root, "pipeline", "build", "stats.json")
    flags_out = flags_out or os.path.join(repo_root, "pipeline", "build", "flags.json")
    reconciliation_out = reconciliation_out or os.path.join(repo_root, "pipeline", "build", "reconciliation.md")

    th = load_json(thresholds_path)
    run_schemas = {
        "3.0": load_json(os.path.join(schemas_dir, "run_record.schema.json")),
        "3.1": load_json(os.path.join(schemas_dir, "run_record_v3_1.schema.json")),
        "3.1.1": load_json(os.path.join(schemas_dir, "run_record_v3_1_1.schema.json")),
        "3.1.2": load_json(os.path.join(schemas_dir, "run_record_v3_1_2.schema.json")),
    }
    review_schema = load_json(os.path.join(schemas_dir, "review_record.schema.json"))
    review_schema_v312 = load_json(os.path.join(schemas_dir, "review_record_v3_1_2.schema.json"))

    records, legacy = discover_runs(runs_dir)
    errors = []
    built = {}  # naics -> dict

    for naics in sorted(records):
        path, rec = records[naics]
        # 1. schema validation
        template_version = rec.get("run_meta", {}).get("template_version")
        if template_version not in run_schemas:
            errors.append(
                "%s (%s): unsupported template_version %r; supported versions are %s"
                % (
                    naics,
                    os.path.basename(path),
                    template_version,
                    ", ".join(SUPPORTED_TEMPLATE_VERSIONS),
                )
            )
            continue
        if (template_version == "3.1.1"
                and rec.get("run_meta", {}).get("model_id") != "gpt-5.6-terra"):
            errors.append(
                "%s (%s): v3.1.1 fleet model_id %r does not match required %r"
                % (
                    naics,
                    path,
                    rec.get("run_meta", {}).get("model_id"),
                    "gpt-5.6-terra",
                )
            )
            continue
        if (template_version == "3.1.2"
                and rec.get("run_meta", {}).get("model_id") != "gpt-5.6-terra"):
            errors.append(
                "%s (%s): v3.1.2 fleet model_id %r does not match required %r"
                % (naics, path, rec.get("run_meta", {}).get("model_id"), "gpt-5.6-terra")
            )
            continue
        run_schema = run_schemas[template_version]
        errs = ["%s (%s): %s" % (naics, os.path.basename(path), e)
                for e in schema_errors(rec, run_schema, run_schema)]
        if rec.get("naics") != naics:
            errs.append("%s: record naics %r does not match directory %r"
                        % (naics, rec.get("naics"), naics))
        if template_version == "3.1.1":
            errs.extend(
                "%s (%s): %s" % (naics, os.path.basename(path), error)
                for error in evidence_contract_errors(rec)
            )
        if errs:
            errors.extend(errs)
            continue
        # 2. arithmetic recompute (hard fail on mismatch)
        computed, arith_errs, deltas = recompute(rec)
        if arith_errs:
            errors.extend(arith_errs)
            continue
        # 3. verdict
        factors = {f: computed[f] for f in ["V", "C", "A", "B", "M"]}
        decision = decide(computed["S"], factors,
                          rec["cross_checks"]["terminal_value"]["class"],
                          rec["confidence_overall"], th)
        if template_version == "3.1.2" and rec.get("decision") != decision:
            errors.append(
                "%s (%s): stored deterministic decision differs from fresh recompute"
                % (naics, os.path.basename(path))
            )
            continue
        flags = record_flags(rec, computed, decision, deltas)
        # 4. acceptance
        artifact_digests = None
        if template_version == "3.1.2":
            run_id = rec["run_meta"]["run_id"]
            packet_path = os.path.join(repo_root, "pipeline", "packets", naics, run_id + ".json")
            memo_path = os.path.join(repo_root, "pipeline", "memos", naics, run_id + ".md")
            missing_artifacts = [item for item in (packet_path, memo_path) if not os.path.isfile(item)]
            if missing_artifacts:
                errors.append("%s: missing canonical packet/memo artifacts %s" % (naics, missing_artifacts))
                continue
            artifact_digests = {
                "packet_sha256": sha256_file(packet_path),
                "run_sha256": sha256_file(path),
                "memo_sha256": sha256_file(memo_path),
            }
        status, review_summary, review_errs = acceptance_status(
            naics, rec, review_dir,
            review_schema_v312 if template_version == "3.1.2" else review_schema,
            source_audit_pairs(rec), flags, artifact_digests,
        )
        errors.extend(review_errs)
        built[naics] = {"rec": rec, "computed": computed, "decision": decision,
                        "deltas": deltas, "flags": flags,
                        "acceptance": status, "review": review_summary}

    if errors:
        return {"ok": False, "errors": errors}

    # percentile of S across all built codes (display context only, P4/§5)
    all_S = sorted(v["computed"]["S"] for v in built.values())
    n = len(all_S)

    site_records = []
    flag_records = []
    verdict_counts = {}
    conf_dist = {}
    borderline_count = 0
    gate_blocked_count = 0
    pending, rejected, published = [], [], []

    for naics in sorted(built):
        b = built[naics]
        rec, computed, decision = b["rec"], b["computed"], b["decision"]
        flags = b["flags"]
        flag_records.append({"naics": naics, "run_id": rec["run_meta"]["run_id"],
                             "verdict": decision["verdict"], "acceptance": b["acceptance"],
                             "flags": flags})
        if b["acceptance"] == "rejected":
            rejected.append(naics)
            continue
        if b["acceptance"] == "pending":
            pending.append(naics)
            if not allow_unreviewed:
                continue
        published.append(naics)
        percentile = 100.0 * sum(1 for s in all_S if s <= computed["S"]) / n
        verdict_counts[decision["verdict"]] = verdict_counts.get(decision["verdict"], 0) + 1
        conf_dist[rec["confidence_overall"]] = conf_dist.get(rec["confidence_overall"], 0) + 1
        borderline_count += 1 if decision["borderline"] else 0
        gate_blocked_count += 1 if decision["gate_blocked"] else 0
        site_records.append({
            "naics": naics,
            "title": rec["title"],
            "sector": {"code": naics[:2], "name": SECTOR_NAMES.get(naics[:2], "Unknown")},
            "scores": {f: computed[f] for f in ["V", "C", "A", "B", "M"]},
            "S": computed["S"],
            "verdict": decision["verdict"],
            "borderline": decision["borderline"],
            "gate_blocked": decision["gate_blocked"],
            "capped_by": decision["capped_by"],
            "confidence": rec["confidence_overall"],
            "terminal_value": rec["cross_checks"]["terminal_value"]["class"],
            "heterogeneous": rec["heterogeneous"],
            "percentile": percentile,
            "run_meta": rec["run_meta"],
            "acceptance": {"status": b["acceptance"], "review": b["review"]},
            "flags": flags,
            "evidence": {
                "dataset_inputs": rec["dataset_inputs"],
                "inputs": rec["inputs"],
                "subfactors": {k: computed[k] for k in ["V_raw", "TD", "OW", "CFD"]},
                "cross_checks": rec["cross_checks"],
                "top_uncertain_inputs": rec["top_uncertain_inputs"],
                "reviewer_note": rec["reviewer_note"],
            },
        })
        if rec.get("run_meta", {}).get("template_version") == "3.1.2":
            site_records[-1]["research_memo"] = rec["narrative"]
            site_records[-1]["sources"] = rec["sources"]
            site_records[-1]["publication_caveats"] = b["review"].get(
                "publication_caveats", []
            )

    site = {
        "_generated": "pipeline/build/build.py — GENERATED, never hand-edited (V3_PRODUCT.md P1/P3/P8)",
        "thresholds_version": th["version"],
        "allow_unreviewed": allow_unreviewed,
        "records": site_records,
    }
    stats = {
        "_generated": "pipeline/build/build.py — single source for README/methodology numbers (P8)",
        "thresholds_version": th["version"],
        "allow_unreviewed": allow_unreviewed,
        "run_records_latest_per_code": len(records),
        "legacy_records_skipped": len(legacy),
        "built": len(built),
        "published": len(published),
        "pending_review": pending,
        "rejected": rejected,
        "verdict_counts": {k: verdict_counts[k] for k in sorted(verdict_counts)},
        "borderline_count": borderline_count,
        "gate_blocked_count": gate_blocked_count,
        "confidence_distribution": {k: conf_dist[k] for k in sorted(conf_dist)},
        "coverage": {
            "codes_universe": CODES_UNIVERSE,
            "codes_built": len(built),
            "codes_published": len(published),
            "published_pct": round(100.0 * len(published) / CODES_UNIVERSE, 2),
        },
    }
    flags_doc = {
        "_generated": "pipeline/build/build.py — per-record focus list for the Stage-5 validator",
        "records": flag_records,
    }

    reconciliation = build_reconciliation(expectations_path, built)

    for path, doc in [(site_out, site), (stats_out, stats), (flags_out, flags_doc)]:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(doc, f, indent=2, ensure_ascii=False)
            f.write("\n")
    with open(reconciliation_out, "w", encoding="utf-8") as f:
        f.write(reconciliation)

    return {"ok": True, "errors": [], "stats": stats, "site": site,
            "flags": flags_doc, "outputs": [site_out, stats_out, flags_out, reconciliation_out]}


def build_reconciliation(expectations_path, built):
    lines = [
        "# Deep-dive reconciliation — GENERATED by pipeline/build/build.py",
        "",
        "Compares built v3 verdicts against the stances recorded in",
        "`pipeline/build/deep_dive_expectations.json` (human-curated-pending-review,",
        "extracted from `deep-dives/*.html`). A divergence means the screen and the",
        "deep-dive disagree and someone should look (V3_PRODUCT.md §7.4).",
        "",
    ]
    if not os.path.isfile(expectations_path):
        lines.append("**deep_dive_expectations.json not found — reconciliation skipped.**")
        return "\n".join(lines) + "\n"
    exp = load_json(expectations_path)
    divergent, consistent, unbuilt = [], [], []
    lines.append("| NAICS | Deep-dive verdict | Stance | Expected v3 verdicts | Built v3 verdict | Status |")
    lines.append("|---|---|---|---|---|---|")
    for e in exp["expectations"]:
        naics = e["naics"]
        if naics in built:
            verdict = built[naics]["decision"]["verdict"]
            if verdict in e["expected_verdicts"]:
                status = "consistent"
                consistent.append(naics)
            else:
                status = "**DIVERGES**"
                divergent.append(naics)
        else:
            verdict = "—"
            status = "no v3 run yet"
            unbuilt.append(naics)
        lines.append("| %s %s | %s | %s | %s | %s | %s |"
                     % (naics, e["title"], e["deep_dive_verdict"], e["stance"],
                        ", ".join(e["expected_verdicts"]), verdict, status))
    lines.append("")
    lines.append("**Summary:** %d deep-dives · %d consistent · %d divergent · %d without a v3 run yet."
                 % (len(exp["expectations"]), len(consistent), len(divergent), len(unbuilt)))
    if divergent:
        lines.append("")
        lines.append("Divergent codes: " + ", ".join(divergent))
    extra = sorted(set(built) - {e["naics"] for e in exp["expectations"]})
    if extra:
        lines.append("")
        lines.append("Built codes without a deep-dive (not reconciled): " + ", ".join(extra))
    return "\n".join(lines) + "\n"


def main(argv=None):
    default_root = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
    p = argparse.ArgumentParser(description="v3 deterministic build & check (Stage 4)")
    p.add_argument("--repo-root", default=default_root)
    p.add_argument("--allow-unreviewed", action="store_true",
                   help="publish records without an accepted review (development/pilot only)")
    p.add_argument("--runs-dir")
    p.add_argument("--review-dir")
    p.add_argument("--thresholds")
    p.add_argument("--schemas-dir")
    p.add_argument("--expectations")
    p.add_argument("--site-out")
    p.add_argument("--stats-out")
    p.add_argument("--flags-out")
    p.add_argument("--reconciliation-out")
    a = p.parse_args(argv)

    result = run_build(a.repo_root, allow_unreviewed=a.allow_unreviewed,
                       runs_dir=a.runs_dir, review_dir=a.review_dir,
                       thresholds_path=a.thresholds, schemas_dir=a.schemas_dir,
                       expectations_path=a.expectations, site_out=a.site_out,
                       stats_out=a.stats_out, flags_out=a.flags_out,
                       reconciliation_out=a.reconciliation_out)
    if not result["ok"]:
        print("BUILD FAILED — %d error(s):" % len(result["errors"]), file=sys.stderr)
        for e in result["errors"]:
            print("  " + e, file=sys.stderr)
        return 1
    s = result["stats"]
    print("build ok: %d built, %d published, %d pending review, %d rejected"
          % (s["built"], s["published"], len(s["pending_review"]), len(s["rejected"])))
    print("verdicts: %s · borderline: %d" % (s["verdict_counts"], s["borderline_count"]))
    for path in result["outputs"]:
        print("wrote " + path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
