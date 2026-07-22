#!/usr/bin/env python3
"""v5.1 finalizer, integrity checker, and site builder (stdlib only, deterministic).

Subcommands:
  validate <packet.json>            check the packet contract; exit nonzero on failure
  finalize <packet.json>            validate, inject dataset inputs, score, write
                                    score.json and memo.md beside the packet
  check <run_dir>                   deterministic integrity check: identity, byte
                                    reproduction of score.json and memo.md, artifact
                                    digest, contract-hash drift. Its output is what a
                                    review's `mechanics` block must copy — models
                                    never self-assess bytes.
  validate-review <run_dir>         validate review.json against the exact current
                                    artifact bytes; required before a review is
                                    accepted or committed
  audit-state                       reconcile git state, contract hash, campaign
                                    state, on-disk artifacts, and sample membership;
                                    run at every operator session start
  site                              verify integrity + review validity for every
                                    code in every closed block, then write
                                    6digit/six_data_v5_1.json (provisional
                                    sampled-validation screen). Integrity failures
                                    abort the build (fail closed). There is no
                                    unreviewed bypass: unsampled records publish as
                                    not_reviewed by design; sampled records need an
                                    accepted review or a reviewed exclusion.

Code owns arithmetic, contract validation, sample selection, and the publication
gate. It never judges whether a source truly supports a claim — that is the
validator model's job.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from score import (  # noqa: E402
    EVIDENCE_STATES, FACTOR_NAMES, c_score, d_score, f_score, h_score,
    json_decimal, readiness_and_action, scenario_envelope,
)

ROOT = Path(__file__).resolve().parents[2]
V5 = Path(__file__).resolve().parent
RUNS = V5 / "runs"
DATASETS = ROOT / "pipeline" / "datasets" / "derived"
SITE_OUT = ROOT / "6digit" / "six_data_v5_1.json"
METHODOLOGY_VERSION = "5.1"
TARGETS_PATH = V5 / "targets.json"
STATE_PATH = V5 / "campaign_state.json"
SITE_LABEL = "provisional sampled-validation screen"
# Frozen sampling constants (V5_1_PLAN.md sampling contract). The seed is part
# of the frozen contract surface; changing it is a new methodology version.
SAMPLE_SEED = "v5.1-freeze-2026-07-22"
RANDOM_FRACTION = 0.10
RANDOM_MINIMUM = 3
MANDATORY_TIERS = ("HIGHEST_PRIORITY", "PRIORITY")
BLOCK_STATUSES = ("todo", "research", "review", "remedy", "closed", "descoped")
# The frozen contract surface covered by contract_sha256, in fixed order.
CONTRACT_FILES = ("methodology.md", "research_brief.md", "validator_brief.md",
                  "research_packet.schema.json", "review.schema.json",
                  "thresholds.json", "score.py", "build.py", "assignment.py",
                  "targets.json")

# Researched primitives per factor with their semantic domains. l and n are
# dataset-injected, never researched.
RESEARCHED = {
    "H": (("a", 0.0, 1.0), ("rho", 0.0, 1.0)),
    "F": (("e", 0.0, 1.0), ("s5", 0.0, 1.0)),
    "C": (("q", 0.0, 1.0),),
    "D": (("d5", 0.0, None), ("o", 0.0, 1.0)),
}
PRIMITIVE_NAMES = tuple(name for spec in RESEARCHED.values() for name, *_ in spec)
NARRATIVE_SECTIONS = (
    "executive_view", "ai_impact", "value_capture", "firm_availability",
    "demand_durability", "risks_and_uncertainty",
)
# The enforced key sets. The .schema.json files document the same contract;
# a divergence between them is a bug in this file or the schema, never a
# permitted extension. Unknown keys are rejected so a packet cannot smuggle
# outcome hints or side-channel fields.
ALLOWED_KEYS = {
    "packet": {"identity", "lens", "primitives", "narrative", "sources"},
    "identity": {"naics", "title", "run_id", "model_id", "run_date",
                 "methodology_version", "attempt"},
    "lens": {"included_activities", "excluded_activities",
             "customer_and_revenue_model", "deviation_from_default", "heterogeneous"},
    "primitive": {"evidence_state", "low", "base", "high", "bridge", "rationale",
                  "change_evidence", "source_ids", "caveats"},
    "narrative": set(NARRATIVE_SECTIONS) | {"principal_driver", "principal_weakness"},
    "source": {"id", "url", "title", "access_date", "supports"},
    "review": {"run_id", "naics", "reviewer_model_id", "review_date",
               "methodology_version", "outcome", "mechanics", "sources_audited",
               "material_findings", "caveats", "summary"},
    "mechanics": {"identity_ok", "score_reproduces", "memo_reproduces", "artifacts_sha256"},
    "audit": {"source_id", "reachable", "support", "note"},
}
SUPPORT_LEVELS = ("supported", "partially_supported", "unsupported", "not_score_driving")
WEAKNESS = {"OBSERVED": 0, "PROXY": 1, "ESTIMATE": 2, "MISSING": 3}
ACCEPTED = ("publishable", "publishable_with_caveats")
OUTCOMES = ACCEPTED + ("reject", "invalid")
FINDING_CATEGORIES = {"unsupported_claim", "fabricated_or_unreachable_source",
                      "reversed_semantics", "undisclosed_proxy", "double_counting",
                      "lens_shopping", "incoherent_range", "absence_as_zero"}
DATASET_GAP = re.compile(r"no (?:direct )?(?:series|data)|gap|missing", re.I)
NAICS_RE = re.compile(r"^[0-9]{6}$")
DATE_RE = re.compile(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$")
SOURCE_ID_RE = re.compile(r"^S[0-9]+$")
INTERVAL_SCOPE = "research-input sensitivity with dataset anchors (l, n) held fixed"
TIER_RANK = {"STRUCTURAL_OUT": 0, "LOW_PRIORITY": 1, "CONDITIONAL": 2,
             "PRIORITY": 3, "HIGHEST_PRIORITY": 4}


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def dump_json(obj) -> str:
    return json.dumps(obj, indent=1, sort_keys=True, ensure_ascii=False) + "\n"


def is_number(value) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value)


def git_commit() -> str | None:
    try:
        out = subprocess.run(["git", "-C", str(ROOT), "rev-parse", "HEAD"],
                             capture_output=True, text=True, timeout=10)
        return out.stdout.strip() or None if out.returncode == 0 else None
    except OSError:
        return None


def contract_sha256_current() -> str:
    """Hash the frozen contract surface. This — not the runtime git HEAD —
    is the freeze identity every artifact carries and every gate re-checks."""
    digest = hashlib.sha256()
    for name in CONTRACT_FILES:
        digest.update(name.encode())
        digest.update(b"\x00")
        digest.update((V5 / name).read_bytes())
        digest.update(b"\x00")
    return digest.hexdigest()


def load_targets(targets: dict | None = None) -> dict:
    return targets if targets is not None else load_json(TARGETS_PATH)


def load_state(state: dict | None = None) -> dict:
    return state if state is not None else load_json(STATE_PATH)


def attempt1_score(code_dir: Path) -> dict | None:
    """The attempt-1 score is the frozen sampling basis: the sample is computed
    when a block's research completes, before any remediation, and must
    recompute identically afterwards."""
    for run_dir in sorted(code_dir.iterdir()) if code_dir.is_dir() else []:
        score_path = run_dir / "score.json"
        if score_path.exists():
            score = load_json(score_path)
            if score.get("identity", {}).get("attempt") == 1:
                return score
    return None


def compute_sample(block_id: str, targets: dict | None = None,
                   runs: Path = RUNS) -> dict:
    """Deterministic, code-owned sample for one block (frozen contract):
    mandatory = every attempt-1 base tier in MANDATORY_TIERS; random =
    ceil(RANDOM_FRACTION x frame) with RANDOM_MINIMUM, ordered by
    sha256(seed + naics); canaries are excluded from both the frame and the
    denominator and form their own 100%-reviewed stratum."""
    targets = load_targets(targets)
    block_codes = [c for c in targets["codes"] if c["block"] == block_id]
    if not block_codes:
        raise ValueError(f"unknown block {block_id!r}")
    canary = sorted(c["naics"] for c in block_codes if c.get("canary"))
    mandatory, frame, missing = [], [], []
    for code in block_codes:
        naics = code["naics"]
        if naics in canary:
            continue
        score = attempt1_score(runs / naics)
        if score is None:
            missing.append(naics)
        elif score.get("tier") in MANDATORY_TIERS:
            mandatory.append(naics)
        else:
            frame.append(naics)
    if missing:
        raise ValueError(
            f"block {block_id}: sample needs a finalized attempt-1 score for every "
            f"non-canary code; missing {sorted(missing)}")
    k = min(len(frame), max(RANDOM_MINIMUM, math.ceil(RANDOM_FRACTION * len(frame))))
    ordered = sorted(frame, key=lambda naics: hashlib.sha256(
        (SAMPLE_SEED + naics).encode()).hexdigest())
    return {"seed": SAMPLE_SEED, "mandatory": sorted(mandatory),
            "random": sorted(ordered[:k]), "canary": canary}


def sampled_codes(sample: dict) -> set[str]:
    return set(sample["mandatory"]) | set(sample["random"]) | set(sample["canary"])


def _unknown_keys(obj: dict, allowed_key: str, where: str, errors: list[str]) -> None:
    extra = set(obj) - ALLOWED_KEYS[allowed_key]
    if extra:
        errors.append(f"{where}: unknown keys {sorted(extra)}")


def validate_packet(packet: dict) -> list[str]:
    errors: list[str] = []

    def need(obj, field, kind, where):
        value = obj.get(field)
        if not isinstance(value, kind) or (isinstance(value, str) and not value.strip()):
            errors.append(f"{where}.{field}: required {kind.__name__}")
            return None
        return value

    if not isinstance(packet, dict):
        return ["packet: must be an object"]
    _unknown_keys(packet, "packet", "packet", errors)

    identity = packet.get("identity") or {}
    _unknown_keys(identity, "identity", "identity", errors)
    for field in ("naics", "title", "run_id", "model_id", "run_date"):
        need(identity, field, str, "identity")
    if isinstance(identity.get("naics"), str) and not NAICS_RE.match(identity["naics"]):
        errors.append("identity.naics: must be six digits")
    if isinstance(identity.get("run_date"), str) and not DATE_RE.match(identity["run_date"]):
        errors.append("identity.run_date: must be YYYY-MM-DD")
    if identity.get("methodology_version") != METHODOLOGY_VERSION:
        errors.append("identity.methodology_version: must be %r" % METHODOLOGY_VERSION)
    if not isinstance(identity.get("attempt"), int) or identity.get("attempt") not in (1, 2):
        errors.append("identity.attempt: must be 1 or 2")

    lens = packet.get("lens") or {}
    _unknown_keys(lens, "lens", "lens", errors)
    for field in ("included_activities", "excluded_activities", "customer_and_revenue_model",
                  "deviation_from_default"):
        need(lens, field, str, "lens")
    if not isinstance(lens.get("heterogeneous"), bool):
        errors.append("lens.heterogeneous: required bool")

    sources = packet.get("sources")
    source_ids = set()
    if not isinstance(sources, list) or not sources:
        errors.append("sources: required nonempty list")
    else:
        for i, src in enumerate(sources):
            where = f"sources[{i}]"
            _unknown_keys(src, "source", where, errors)
            sid = need(src, "id", str, where)
            for field in ("url", "title", "access_date", "supports"):
                need(src, field, str, where)
            if isinstance(src.get("access_date"), str) and not DATE_RE.match(src["access_date"]):
                errors.append(f"{where}.access_date: must be YYYY-MM-DD")
            if sid:
                if not SOURCE_ID_RE.match(sid):
                    errors.append(f"{where}.id: must match S<number>")
                if sid in source_ids:
                    errors.append(f"{where}.id: duplicate {sid!r}")
                source_ids.add(sid)

    primitives = packet.get("primitives") or {}
    extra = set(primitives) - set(PRIMITIVE_NAMES)
    if extra:
        errors.append(f"primitives: unknown primitives {sorted(extra)} — l and n are dataset-injected")
    for factor, spec in RESEARCHED.items():
        for name, dom_low, dom_high in spec:
            sel = primitives.get(name)
            where = f"primitives.{name}"
            if not isinstance(sel, dict):
                errors.append(f"{where}: required object")
                continue
            _unknown_keys(sel, "primitive", where, errors)
            state = sel.get("evidence_state")
            if state not in EVIDENCE_STATES:
                errors.append(f"{where}.evidence_state: must be one of {EVIDENCE_STATES}")
                continue
            need(sel, "rationale", str, where)
            need(sel, "change_evidence", str, where)
            if not isinstance(sel.get("caveats"), list):
                errors.append(f"{where}.caveats: required list (may be empty)")
            ids = sel.get("source_ids")
            if not isinstance(ids, list):
                errors.append(f"{where}.source_ids: required list")
                ids = []
            for sid in ids:
                if sid not in source_ids:
                    errors.append(f"{where}.source_ids: unknown source {sid!r}")
            if state == "MISSING":
                for field in ("low", "base", "high"):
                    if sel.get(field) is not None:
                        errors.append(f"{where}.{field}: must be null for MISSING")
                if ids:
                    errors.append(f"{where}.source_ids: must be empty for MISSING")
                continue
            low, base, high = sel.get("low"), sel.get("base"), sel.get("high")
            if not (is_number(low) and is_number(base) and is_number(high)):
                errors.append(f"{where}: low/base/high must be finite numbers, never prose")
                continue
            if not (low <= base <= high):
                errors.append(f"{where}: requires low <= base <= high")
            for field, value in (("low", low), ("base", base), ("high", high)):
                if value < dom_low or (dom_high is not None and value > dom_high):
                    errors.append(f"{where}.{field}: outside domain [{dom_low}, {dom_high}]")
            if state in ("OBSERVED", "PROXY") and not ids:
                errors.append(f"{where}: {state} requires at least one source id")
            if state == "PROXY" and not (isinstance(sel.get("bridge"), str) and sel["bridge"].strip()):
                errors.append(f"{where}.bridge: PROXY requires a stated population/quantity bridge")

    narrative = packet.get("narrative") or {}
    _unknown_keys(narrative, "narrative", "narrative", errors)
    for section in NARRATIVE_SECTIONS:
        need(narrative, section, str, "narrative")
    for field in ("principal_driver", "principal_weakness"):
        need(narrative, field, str, "narrative")

    return errors


def dataset_leaf(dataset: dict, key: str) -> dict:
    """Map a dataset input to a leaf, honoring the dataset's own provenance.

    Dataset values are frozen point values for cross-industry comparability,
    but they are only OBSERVED when their recorded quality says so; a derived
    or estimated series is an ESTIMATE and weighs on readiness accordingly.
    """
    entry = dataset.get(key) or {}
    value = entry.get("value")
    detail = " ".join(str(entry.get(k, "")) for k in ("method", "derivation", "source"))
    if value is None or (value == 0 and DATASET_GAP.search(detail)):
        return {"evidence_state": "MISSING", "value": None,
                "rationale": f"dataset {key} has no defensible value", "detail": detail.strip()}
    quality = str(entry.get("quality", "")).upper()
    state = "OBSERVED" if quality in ("HIGH", "MED") else "ESTIMATE"
    return {"evidence_state": state, "value": value,
            "quality": entry.get("quality"), "detail": detail.strip()}


def finalize(packet: dict, dataset: dict, commit: str | None = None,
             contract: str | None = None) -> dict:
    errors = validate_packet(packet)
    if errors:
        raise ValueError("packet contract failed:\n  " + "\n  ".join(errors))

    prims = packet["primitives"]
    l_leaf = dataset_leaf(dataset, "labor_share")
    n_leaf = dataset_leaf(dataset, "n_band")
    resolved = {"l": l_leaf, "n": n_leaf, **{name: prims[name] for name in PRIMITIVE_NAMES}}

    def rng(name):
        sel = prims[name]
        if sel["evidence_state"] == "MISSING":
            return None
        return sel["low"], sel["base"], sel["high"]

    factor_ranges, factor_meta = {}, {}
    specs = {
        "H": (l_leaf, ("a", "rho"), lambda l, a, r: h_score(l, a, r)),
        "F": (n_leaf, ("e", "s5"), lambda n, e, s: f_score(n, e, s)),
        "C": (None, ("q",), lambda q: c_score(q)),
        "D": (None, ("d5", "o"), lambda d, o: d_score(d, o)),
    }
    for factor, (injected, names, fn) in specs.items():
        parts = [rng(name) for name in names]
        states = [prims[name]["evidence_state"] for name in names]
        if injected is not None:
            states.append(injected["evidence_state"])
        state = max(states, key=WEAKNESS.get)
        factor_meta[factor] = {"evidence_state": state, "primitives": list(names)}
        if any(part is None for part in parts) or (injected is not None and injected["value"] is None):
            factor_ranges[factor] = {"low": None, "base": None, "high": None}
            continue
        prefix = (injected["value"],) if injected is not None else ()
        low, base, high = (fn(*prefix, *[part[i] for part in parts]) for i in range(3))
        factor_ranges[factor] = {"low": low, "base": base, "high": high}

    envelope = {**scenario_envelope(factor_ranges), "interval_scope": INTERVAL_SCOPE}
    all_states = [leaf["evidence_state"] for leaf in resolved.values()]
    readiness, action = readiness_and_action(all_states, envelope)
    base = envelope["base"]

    caveats = []
    for name, sel in resolved.items():
        for caveat in sel.get("caveats", []) or []:
            caveats.append(f"{name}: {caveat}")

    return json_decimal({
        "identity": packet["identity"],
        "methodology_version": METHODOLOGY_VERSION,
        "methodology_commit": commit,
        "contract_sha256": contract,
        "lens": packet["lens"],
        "primitives": resolved,
        "factors": {name: {**factor_ranges[name], **factor_meta[name]} for name in FACTOR_NAMES},
        "A": base["A"] if base else None,
        "L": base["L"] if base else None,
        "tier": base["tier"] if base else None,
        "envelope": envelope,
        "tier_interval": envelope["tier_interval"],
        "robust_tier": envelope["robust_tier"],
        "readiness": readiness,
        "action": action,
        "principal_driver": packet["narrative"]["principal_driver"],
        "principal_weakness": packet["narrative"]["principal_weakness"],
        "caveats": caveats,
    })


def render_memo(packet: dict, score: dict) -> str:
    identity, narrative = packet["identity"], packet["narrative"]
    lines = [
        f"# {identity['naics']} — {identity['title']}",
        "",
        f"*v5 Stage 1 research memo. Run `{identity['run_id']}`, model `{identity['model_id']}`, "
        f"{identity['run_date']}, attempt {identity['attempt']}.*",
        "",
        f"**Base tier:** {score['tier'] or 'no base (evidence-first)'} · "
        f"A {'—' if score['A'] is None else format(score['A'], '.2f')} · "
        f"L {'—' if score['L'] is None else format(score['L'], '.2f')} · "
        f"interval {score['tier_interval'][0]} → {score['tier_interval'][1]} · "
        f"readiness {score['readiness']} · action {score['action']}",
        "",
        f"**Driver:** {narrative['principal_driver']}",
        f"**Weakness:** {narrative['principal_weakness']}",
        "",
        "## Business-model lens",
        f"- Included: {packet['lens']['included_activities']}",
        f"- Excluded: {packet['lens']['excluded_activities']}",
        f"- Customer and revenue model: {packet['lens']['customer_and_revenue_model']}",
        f"- Deviation from default lens: {packet['lens']['deviation_from_default']}",
    ]
    titles = {
        "executive_view": "Executive view", "ai_impact": "How AI changes the work",
        "value_capture": "Value capture", "firm_availability": "Firm availability",
        "demand_durability": "Demand durability", "risks_and_uncertainty": "Risks and uncertainty",
    }
    for section in NARRATIVE_SECTIONS:
        lines += ["", f"## {titles[section]}", narrative[section]]

    lines += ["", "## Scorecard", "",
              "| Primitive | Low | Base | High | Evidence | Sources |", "|---|---|---|---|---|---|"]
    for name, sel in score["primitives"].items():
        fmt = lambda v: "—" if v is None else f"{v:g}" if isinstance(v, (int, float)) else str(v)
        srcs = ", ".join(sel.get("source_ids", []) or []) or "—"
        lines.append(f"| {name} | {fmt(sel.get('low'))} | {fmt(sel.get('value', sel.get('base')))} "
                     f"| {fmt(sel.get('high'))} | {sel['evidence_state']} | {srcs} |")
    lines += ["", "| Factor | Low | Base | High | Evidence |", "|---|---|---|---|---|"]
    for name in FACTOR_NAMES:
        f = score["factors"][name]
        fmt = lambda v: "—" if v is None else f"{v:.2f}"
        lines.append(f"| {name} | {fmt(f['low'])} | {fmt(f['base'])} | {fmt(f['high'])} | {f['evidence_state']} |")

    if score["caveats"]:
        lines += ["", "## Caveats"] + [f"- {c}" for c in score["caveats"]]
    lines += ["", "## Sources"]
    for src in packet["sources"]:
        lines.append(f"- **{src['id']}** — [{src['title']}]({src['url']}) (accessed {src['access_date']}): {src['supports']}")
    return "\n".join(lines) + "\n"


def finalize_path(packet_path: Path) -> Path:
    packet = load_json(packet_path)
    naics = packet.get("identity", {}).get("naics", "")
    dataset = load_json(DATASETS / f"{naics}.json")
    score = finalize(packet, dataset, commit=git_commit(),
                     contract=contract_sha256_current())
    out_dir = packet_path.parent
    (out_dir / "score.json").write_text(dump_json(score), encoding="utf-8")
    (out_dir / "memo.md").write_text(render_memo(packet, score), encoding="utf-8")
    return out_dir / "score.json"


def artifacts_sha256(run_dir: Path) -> str:
    digest = hashlib.sha256()
    for name in ("packet.json", "score.json", "memo.md"):
        digest.update(name.encode())
        digest.update(b"\x00")
        digest.update((run_dir / name).read_bytes())
        digest.update(b"\x00")
    return digest.hexdigest()


def check(run_dir: Path) -> dict:
    """Deterministic integrity check for one run directory.

    This — not any model's self-report — is the source of a review's
    `mechanics` block, and `site` re-runs it before publishing anything.
    """
    result = {"identity_ok": False, "score_reproduces": False,
              "memo_reproduces": False, "artifacts_sha256": None, "errors": []}
    packet_path, score_path, memo_path = (run_dir / n for n in ("packet.json", "score.json", "memo.md"))
    for path in (packet_path, score_path, memo_path):
        if not path.exists():
            result["errors"].append(f"missing {path.name}")
    if result["errors"]:
        return result

    packet, stored = load_json(packet_path), load_json(score_path)
    identity = packet.get("identity", {})
    problems = []
    if run_dir.name != identity.get("run_id"):
        problems.append(f"run directory {run_dir.name!r} != identity.run_id {identity.get('run_id')!r}")
    if run_dir.parent.name != identity.get("naics"):
        problems.append(f"code directory {run_dir.parent.name!r} != identity.naics {identity.get('naics')!r}")
    if stored.get("identity") != identity:
        problems.append("score.json identity differs from packet identity")
    result["identity_ok"] = not problems
    result["errors"] += problems

    try:
        dataset = load_json(DATASETS / f"{identity.get('naics')}.json")
        fresh = finalize(packet, dataset, commit=stored.get("methodology_commit"),
                         contract=stored.get("contract_sha256"))
    except (ValueError, OSError) as exc:
        result["errors"].append(f"re-finalization failed: {exc}")
        return result
    result["score_reproduces"] = dump_json(fresh) == score_path.read_text(encoding="utf-8")
    if not result["score_reproduces"]:
        result["errors"].append("score.json does not reproduce from packet + dataset")
    result["memo_reproduces"] = render_memo(packet, fresh) == memo_path.read_text(encoding="utf-8")
    if not result["memo_reproduces"]:
        result["errors"].append("memo.md does not reproduce from packet + score")
    if stored.get("contract_sha256") != contract_sha256_current():
        result["errors"].append(
            "contract drift: score.json contract_sha256 does not match the current "
            "frozen contract surface")
    result["artifacts_sha256"] = artifacts_sha256(run_dir)
    return result


def validate_review(review: dict, packet: dict, mechanics: dict) -> list[str]:
    errors: list[str] = []
    if not isinstance(review, dict):
        return ["review: must be an object"]
    _unknown_keys(review, "review", "review", errors)
    for field in ("run_id", "naics", "reviewer_model_id", "review_date", "summary"):
        if not isinstance(review.get(field), str) or not review.get(field, "").strip():
            errors.append(f"review.{field}: required string")
    if review.get("methodology_version") != METHODOLOGY_VERSION:
        errors.append("review.methodology_version: must be %r" % METHODOLOGY_VERSION)
    outcome = review.get("outcome")
    if outcome not in OUTCOMES:
        errors.append(f"review.outcome: must be one of {OUTCOMES}")

    identity = packet.get("identity", {})
    if review.get("run_id") != identity.get("run_id"):
        errors.append("review.run_id does not match packet identity")
    if review.get("naics") != identity.get("naics"):
        errors.append("review.naics does not match packet identity")

    rm = review.get("mechanics")
    if not isinstance(rm, dict):
        errors.append("review.mechanics: required object (copied from build.py check)")
    else:
        _unknown_keys(rm, "mechanics", "review.mechanics", errors)
        for field in ("identity_ok", "score_reproduces", "memo_reproduces"):
            if rm.get(field) is not True and outcome != "invalid":
                errors.append(f"review.mechanics.{field}: false requires outcome invalid")
            if rm.get(field) != mechanics.get(field):
                errors.append(f"review.mechanics.{field}: does not match the deterministic check")
        if rm.get("artifacts_sha256") != mechanics.get("artifacts_sha256"):
            errors.append("review.mechanics.artifacts_sha256: reviewed artifacts differ from current bytes")

    findings = review.get("material_findings")
    if not isinstance(findings, list):
        errors.append("review.material_findings: required list")
        findings = []
    for i, finding in enumerate(findings):
        where = f"review.material_findings[{i}]"
        if not isinstance(finding, dict):
            errors.append(f"{where}: must be an object")
            continue
        if finding.get("category") not in FINDING_CATEGORIES:
            errors.append(f"{where}.category: unknown")
        for field in ("finding", "materiality"):
            if not isinstance(finding.get(field), str) or not finding.get(field, "").strip():
                errors.append(f"{where}.{field}: required string")
    if outcome in ACCEPTED and findings:
        errors.append("review.outcome: a publishable outcome cannot carry material findings")
    if outcome == "reject" and not findings:
        errors.append("review.outcome: reject requires at least one material finding")
    if not isinstance(review.get("caveats"), list):
        errors.append("review.caveats: required list")
    audited = review.get("sources_audited")
    if not isinstance(audited, list):
        errors.append("review.sources_audited: required list")
    else:
        packet_source_ids = {s.get("id") for s in packet.get("sources") or [] if isinstance(s, dict)}
        audited_ids: set[str] = set()
        for i, entry in enumerate(audited):
            where = f"review.sources_audited[{i}]"
            if not isinstance(entry, dict):
                errors.append(f"{where}: must be an object")
                continue
            _unknown_keys(entry, "audit", where, errors)
            sid = entry.get("source_id")
            if not isinstance(sid, str) or not sid:
                errors.append(f"{where}.source_id: required string")
            else:
                if sid not in packet_source_ids:
                    errors.append(f"{where}.source_id: unknown source {sid!r}")
                if sid in audited_ids:
                    errors.append(f"{where}.source_id: duplicate audit of {sid!r}")
                audited_ids.add(sid)
            if not isinstance(entry.get("reachable"), bool):
                errors.append(f"{where}.reachable: required bool")
            if entry.get("support") not in SUPPORT_LEVELS:
                errors.append(f"{where}.support: must be one of {SUPPORT_LEVELS}")
            if "note" in entry and not isinstance(entry["note"], str):
                errors.append(f"{where}.note: must be a string")
        cited = set()
        for sel in (packet.get("primitives") or {}).values():
            if isinstance(sel, dict):
                cited.update(sel.get("source_ids") or [])
        for sid in sorted(cited - audited_ids):
            errors.append(f"review.sources_audited: primitive-cited source {sid} was not audited")
    return errors


def collect_attempts(code_dir: Path, integrity_errors: list[str]):
    """Load a code's attempts and enforce attempt numbering/sequencing.
    Returns the latest attempt tuple or None (error already recorded)."""
    attempts = []
    for run_dir in sorted(code_dir.iterdir()) if code_dir.is_dir() else []:
        if not (run_dir / "packet.json").exists() or not (run_dir / "score.json").exists():
            continue
        review_path = run_dir / "review.json"
        attempts.append((load_json(run_dir / "packet.json"), load_json(run_dir / "score.json"),
                         load_json(review_path) if review_path.exists() else None, run_dir))
    if not attempts:
        integrity_errors.append(f"{code_dir}: no finalized run")
        return None
    numbers = sorted(a[0].get("identity", {}).get("attempt") for a in attempts)
    if numbers not in ([1], [1, 2]):
        integrity_errors.append(f"{code_dir}: attempt numbers must be [1] or [1, 2], got {numbers}")
        return None
    if numbers == [1, 2]:
        first = next(a for a in attempts if a[0]["identity"]["attempt"] == 1)
        outcome1 = (first[2] or {}).get("outcome")
        if outcome1 not in ("reject", "invalid"):
            integrity_errors.append(
                f"{code_dir}: attempt 2 requires attempt 1 reviewed reject/invalid, got {outcome1!r}")
            return None
    return max(attempts, key=lambda a: a[0]["identity"]["attempt"])


def build_site(runs: Path = RUNS, site_out: Path = SITE_OUT,
               targets: dict | None = None, state: dict | None = None) -> dict:
    """Fail-closed publication over the closed-block ledger.

    Only codes in blocks marked `closed` in campaign_state.json publish. Per
    closed block the sample is recomputed from the frozen seed and attempt-1
    scores and must match the recorded assignment. A sampled code publishes
    with its accepted review or becomes a reviewed exclusion; an unsampled
    code publishes as not_reviewed by design. There is no bypass.
    """
    targets, state = load_targets(targets), load_state(state)
    statuses = {bid: entry.get("status") for bid, entry in state.get("blocks", {}).items()}
    closed = sorted(bid for bid, s in statuses.items() if s == "closed")
    records, exclusions, integrity_errors = [], [], []

    for block_id in closed:
        try:
            expected = compute_sample(block_id, targets, runs)
        except ValueError as exc:
            integrity_errors.append(f"block {block_id}: {exc}")
            continue
        recorded = state.get("blocks", {}).get(block_id, {}).get("sample")
        if recorded != expected:
            integrity_errors.append(
                f"block {block_id}: recorded sample drifts from deterministic recomputation")
            continue
        sampled = sampled_codes(expected)
        for code in (c for c in targets["codes"] if c["block"] == block_id):
            naics = code["naics"]
            code_dir = runs / naics
            if not code_dir.is_dir():
                integrity_errors.append(f"closed block {block_id}: {naics} has no run directory")
                continue
            latest = collect_attempts(code_dir, integrity_errors)
            if latest is None:
                continue
            packet, score, review, run_dir = latest

            # The publication gate: nothing enters the site without passing the
            # deterministic integrity check, and any review must itself be
            # valid and bound to the exact current bytes.
            mechanics = check(run_dir)
            if mechanics["errors"]:
                integrity_errors += [f"{run_dir}: {e}" for e in mechanics["errors"]]
                continue
            if review is not None:
                review_errors = validate_review(review, packet, mechanics)
                if review_errors:
                    integrity_errors += [f"{run_dir}: {e}" for e in review_errors]
                    continue
                if review["outcome"] not in ACCEPTED:
                    # Terminal reviewed exclusion — closes the block, listed.
                    exclusions.append({"naics": naics, "block": block_id,
                                       "run_id": run_dir.name,
                                       "outcome": review["outcome"],
                                       "material_findings": review.get("material_findings", []),
                                       "summary": review.get("summary")})
                    continue
            elif naics in sampled:
                integrity_errors.append(
                    f"closed block {block_id}: sampled code {naics} ({run_dir.name}) "
                    "has no review — a sampled record needs an accepted review or a "
                    "reviewed exclusion")
                continue

            records.append({
                **{k: score[k] for k in ("A", "L", "tier", "tier_interval", "robust_tier",
                                         "readiness", "action", "factors", "primitives",
                                         "principal_driver", "principal_weakness", "caveats", "lens")},
                "naics": naics,
                "title": packet["identity"]["title"],
                "block": block_id,
                "independent_review": "accepted" if review else "not_reviewed",
                "run_id": run_dir.name,
                "run_meta": {**packet["identity"],
                             "methodology_commit": score.get("methodology_commit"),
                             "contract_sha256": score.get("contract_sha256")},
                "memo": str((run_dir / "memo.md").relative_to(ROOT)) if run_dir.is_relative_to(ROOT) else str(run_dir / "memo.md"),
                "sources": packet["sources"],
                "review": {"outcome": review["outcome"],
                           "material_findings": review.get("material_findings", []),
                           "caveats": review.get("caveats", []),
                           "sources_audited": review.get("sources_audited", []),
                           "artifacts_sha256": review["mechanics"]["artifacts_sha256"]} if review else None,
            })

    if integrity_errors:
        raise SystemExit("site build failed closed on integrity errors:\n  " + "\n  ".join(integrity_errors))

    def order(record):
        interval_low = TIER_RANK[record["tier_interval"][0]]
        base_a = record["A"] if record["A"] is not None else -1
        base_l = record["L"] if record["L"] is not None else -1
        return (-interval_low, -base_a, -base_l, record["naics"])

    records.sort(key=order)
    for i, record in enumerate(records, 1):
        record["order"] = i  # navigation order, not a precise rank claim

    universe = len(targets["codes"])
    reviewed = sum(1 for r in records if r["independent_review"] == "accepted")
    strata = {"mandatory": 0, "random": 0, "canary": 0}
    for block_id in closed:
        sample = state["blocks"][block_id]["sample"]
        for stratum in strata:
            strata[stratum] += len(sample[stratum])
    site = {
        "_generated": "pipeline/v5_1/build.py — deterministic; do not hand-edit",
        "methodology_version": METHODOLOGY_VERSION,
        "label": SITE_LABEL,
        "coverage": {
            "universe": universe,
            "published": len(records),
            "blocks_closed": closed,
            "blocks_pending": sorted(b for b, s in statuses.items()
                                     if s not in ("closed", "descoped")),
            "blocks_descoped": sorted(b for b, s in statuses.items() if s == "descoped"),
            "independently_reviewed": reviewed,
            "reviewed_share": round(reviewed / len(records), 4) if records else None,
        },
        "records": records,
        "exclusions": exclusions,
        "summary": {
            "published": len(records),
            "excluded": len(exclusions),
            "independent_review": _count(records, "independent_review"),
            "sample_strata": strata,
            "tiers": _count(records, "tier"),
            "readiness": _count(records, "readiness"),
            "actions": _count(records, "action"),
            "robust_tiers": sum(1 for r in records if r["robust_tier"]),
        },
    }
    site_out.write_text(dump_json(site), encoding="utf-8")
    return site


def audit_state(runs: Path = RUNS) -> dict:
    """Reconcile git, contract hash, campaign state, artifacts, and samples.
    The operator runs this at every session start and stops on any error."""
    errors, warnings, info = [], [], {}
    state, targets = load_state(), load_targets()
    known = {c["naics"] for c in targets["codes"]}
    current = contract_sha256_current()
    info["contract_sha256"] = current
    info["launch_approved"] = state.get("launch_approved")
    info["canary_approved"] = state.get("canary_approved")

    recorded = state.get("contract_sha256")
    if recorded is None:
        errors.append("campaign_state.json: contract_sha256 not recorded (freeze incomplete)")
    elif recorded != current:
        errors.append("contract drift: campaign_state.json contract_sha256 does not match "
                      "the current frozen contract surface")

    try:
        branch = subprocess.run(["git", "-C", str(ROOT), "rev-parse", "--abbrev-ref", "HEAD"],
                                capture_output=True, text=True, timeout=10).stdout.strip()
        info["branch"] = branch
        upstream = subprocess.run(
            ["git", "-C", str(ROOT), "rev-list", "--left-right", "--count", "@{u}...HEAD"],
            capture_output=True, text=True, timeout=10)
        if upstream.returncode == 0:
            behind, ahead = upstream.stdout.split()
            info["vs_upstream"] = {"behind": int(behind), "ahead": int(ahead)}
        else:
            warnings.append("no upstream configured for the current branch")
        dirty = subprocess.run(
            ["git", "-C", str(ROOT), "status", "--porcelain", "--"] +
            [str(V5 / name) for name in CONTRACT_FILES],
            capture_output=True, text=True, timeout=10).stdout.strip()
        if dirty:
            errors.append("uncommitted changes to frozen contract files:\n" + dirty)
    except OSError:
        warnings.append("git unavailable; branch reconciliation skipped")

    if set(state.get("blocks", {})) != {c["block"] for c in targets["codes"]}:
        errors.append("campaign_state.json blocks do not match targets.json blocks")
    for block_id, entry in state.get("blocks", {}).items():
        if entry.get("status") not in BLOCK_STATUSES:
            errors.append(f"block {block_id}: unknown status {entry.get('status')!r}")
        if "sample" in entry:
            try:
                if entry["sample"] != compute_sample(block_id, targets, runs):
                    errors.append(f"block {block_id}: recorded sample drifts from "
                                  "deterministic recomputation")
            except ValueError as exc:
                errors.append(f"block {block_id}: {exc}")

    for code_dir in sorted(runs.iterdir()) if runs.exists() else []:
        if code_dir.is_dir() and code_dir.name not in known:
            errors.append(f"runs/{code_dir.name}: not a code in targets.json")
        elif code_dir.is_dir():
            for run_dir in sorted(code_dir.iterdir()):
                score_path = run_dir / "score.json"
                if score_path.exists():
                    stored = load_json(score_path).get("contract_sha256")
                    if stored != current:
                        errors.append(f"{run_dir}: score contract_sha256 does not match "
                                      "the current frozen contract surface")

    if any(s.get("status") == "closed" for s in state.get("blocks", {}).values()):
        import tempfile
        with tempfile.TemporaryDirectory() as tmp:
            try:
                build_site(runs=runs, site_out=Path(tmp) / "site.json")
            except SystemExit as exc:
                errors.append(f"closed blocks fail the publication gate: {exc}")

    return {"errors": errors, "warnings": warnings, "info": info}


def _count(records, key):
    out: dict[str, int] = {}
    for record in records:
        out[str(record[key])] = out.get(str(record[key]), 0) + 1
    return dict(sorted(out.items()))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="cmd", required=True)
    p_validate = sub.add_parser("validate")
    p_validate.add_argument("packet", type=Path)
    p_finalize = sub.add_parser("finalize")
    p_finalize.add_argument("packet", type=Path)
    p_check = sub.add_parser("check")
    p_check.add_argument("run_dir", type=Path)
    p_review = sub.add_parser("validate-review")
    p_review.add_argument("run_dir", type=Path)
    sub.add_parser("audit-state")
    sub.add_parser("site")
    args = parser.parse_args()

    if args.cmd == "validate":
        errors = validate_packet(load_json(args.packet))
        for error in errors:
            print("ERROR:", error)
        print("OK" if not errors else f"{len(errors)} contract errors")
        return 1 if errors else 0
    if args.cmd == "finalize":
        out = finalize_path(args.packet)
        print("wrote", out, "and", out.parent / "memo.md")
        return 0
    if args.cmd == "check":
        result = check(args.run_dir)
        print(json.dumps(result, indent=1))
        return 1 if result["errors"] else 0
    if args.cmd == "validate-review":
        review_path = args.run_dir / "review.json"
        if not review_path.exists():
            print("ERROR: no review.json in", args.run_dir)
            return 1
        mechanics = check(args.run_dir)
        if mechanics["errors"]:
            for error in mechanics["errors"]:
                print("ERROR:", error)
            return 1
        errors = validate_review(load_json(review_path),
                                 load_json(args.run_dir / "packet.json"), mechanics)
        for error in errors:
            print("ERROR:", error)
        print("OK" if not errors else f"{len(errors)} review errors")
        return 1 if errors else 0
    if args.cmd == "audit-state":
        result = audit_state()
        print(json.dumps(result, indent=1))
        return 1 if result["errors"] else 0
    if args.cmd == "site":
        site = build_site()
        cov = site["coverage"]
        print(f"published {cov['published']}/{cov['universe']} "
              f"({len(cov['blocks_closed'])} closed blocks), "
              f"excluded {site['summary']['excluded']}, "
              f"reviewed {cov['independently_reviewed']} -> {SITE_OUT}")
        return 0
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
