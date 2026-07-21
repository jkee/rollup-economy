#!/usr/bin/env python3
"""Fail-closed v4.2 campaign authority, review, lineage, and h-gate checks.

The non-economic authority machinery is inherited from the hardened v4.1
implementation, but every mutable version binding is replaced before export.
No v4.1 artifact, holdout, plan, schema, or gate certificate is accepted.
"""

import hashlib
import copy
import importlib.util
import json
import math
import os
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path


HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))


def _load(name, filename):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, filename))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


core = _load("campaign_v4_2_hardened_core", "campaign_v4_1.py")
issuer_v4_2 = _load("campaign_v4_2_issuer", "issue_campaign_v4_2.py")
gate_report_v4_2 = _load("campaign_v4_2_gate_report", "build_gate_report_v4_2.py")
runtime_linter = _load("campaign_v4_2_runtime_linter", "build_runtime_methodology_v4_2.py")

REGRESSION_CODES = ("238220", "541214", "541511", "541512", "541930")
TARGET_UNIVERSE_PATH = "pipeline/blocks/targets_phase3.json"
HOLDOUT_MEMBERSHIP_PATH = "pipeline/v4_2/holdout_membership.json"
REGRESSION_MEMBERSHIP_PATH = "pipeline/v4_2/regression_membership.json"
FROZEN_TARGET_UNIVERSE_SHA256 = "b403aaa5291b11391c51f1f85651ef55a9b53bb8b03ed13f2a2365c7c64152f2"
FROZEN_REGRESSION_SHA256 = "14fd1ee651f12cabe169f5be7658cf4bec9be2157b41a9b8fdafe7b9efa34783"
FROZEN_HOLDOUT_SHA256 = "77be1cead8d787f8f4476a009dd785629b6e9dcea61210821ebb97a084c8da71"


def _canonical_holdout():
    path = os.path.join(REPO, HOLDOUT_MEMBERSHIP_PATH)
    if not os.path.isfile(path):
        return (), None
    try:
        value = core.load_json(path)
        codes = value.get("selected_codes", [])
        digest = core.sha256(path)
        if (digest != FROZEN_HOLDOUT_SHA256
                or value.get("version") != "v4.2-holdout-2026-07-21"
                or not isinstance(codes, list) or len(codes) != 5
                or len(set(codes)) != 5 or set(codes) & set(REGRESSION_CODES)):
            return (), None
        return tuple(codes), digest
    except (OSError, ValueError, TypeError, json.JSONDecodeError):
        return (), None


HOLDOUT_CODES, HOLDOUT_MEMBERSHIP_SHA256 = _canonical_holdout()

core.CANARY_CODES = REGRESSION_CODES
core.HOLDOUT_CODES = HOLDOUT_CODES
core.HOLDOUT_MEMBERSHIP_PATH = HOLDOUT_MEMBERSHIP_PATH
core.HOLDOUT_MEMBERSHIP_SHA256 = HOLDOUT_MEMBERSHIP_SHA256
core.MANIFEST_VERSION = "review-campaign-4.2"
core.REVIEW_PROMPT_VERSION = "validator-4.2"
core.REVIEW_SCHEMA_FILENAME = "review_record_v4_2.schema.json"
core.DEVELOPMENT_SCOPE = "regression"
core.DEVELOPMENT_GATE_KEY = "regression_gate"
core.DEVELOPMENT_GATE_LABEL = "regression"
core.GATE_CERTIFICATE_VERSION = "gate-certificate-4.2"
core.GATE_CAMPAIGN_PROOF_VERSION = "gate-campaign-proof-4.2"
core.GATE_PROOF_VERSION = "gate-proof-4.2"
core.FULL_GATE_PATHS = {
    "regression_canary": {
        "certificate": "pipeline/v4_2/gates/regression/certificate.json",
        "campaign": "pipeline/v4_2/gates/regression/campaign_proof.json",
        "gate": "pipeline/v4_2/gates/regression/gate_proof.json",
        "source": "pipeline/v4_2/gates/regression/source_campaign.json",
    },
    "holdout": {
        "certificate": "pipeline/v4_2/gates/holdout/certificate.json",
        "campaign": "pipeline/v4_2/gates/holdout/campaign_proof.json",
        "gate": "pipeline/v4_2/gates/holdout/gate_proof.json",
        "source": "pipeline/v4_2/gates/holdout/source_campaign.json",
    },
}
core.issuer = issuer_v4_2
core.TOOLCHAIN_PATHS = {
    "methodology": "V4_2_RUNTIME_METHODOLOGY.md",
    "rejection_record": "V4_1_REJECTION.md",
    "thresholds": "pipeline/build/thresholds_v4_2.json",
    "dataset_schema": "pipeline/build/schemas/dataset_v4_2.schema.json",
    "industry_spec_schema": "pipeline/build/schemas/industry_spec_v4_2.schema.json",
    "packet_schema": "pipeline/build/schemas/research_packet_v4_2.schema.json",
    "run_schema": "pipeline/build/schemas/run_record_v4_2.schema.json",
    "review_schema": "pipeline/build/schemas/review_record_v4_2.schema.json",
    "claim_receipt_schema": "pipeline/build/schemas/output_claim_receipt_v4_2.schema.json",
    "scoring": "pipeline/build/v4_2_scoring.py",
    "finalizer": "pipeline/build/finalize_run_v4_2.py",
    "runner_prompt": "pipeline/template/runner_brief_v4_2.md",
    "validator_prompt": "pipeline/template/validator_brief_v4_2.md",
    "campaign_validator": "pipeline/build/campaign_v4_2.py",
    "campaign_authority_core": "pipeline/build/campaign_v4_1.py",
    "issuer": "pipeline/build/issue_campaign_v4_2.py",
    "guarded_writer": "pipeline/build/guarded_write_v4_2.py",
    "extension_validator": "pipeline/build/validate_full_scope_extension_v4_2.py",
    "extension_workflow": ".github/workflows/v4-2-full-scope-extension.yml",
    "gate_certificate_issuer": "pipeline/build/issue_gate_certificate_v4_2.py",
    "gate_certificate_core": "pipeline/build/issue_gate_certificate_v4_1.py",
}
core.TOOLCHAIN_KEYS = tuple(core.TOOLCHAIN_PATHS)
core.MECHANICS_KEYS = (
    "schema_valid", "identity_valid", "artifact_digests_valid", "toolchain_digests_valid",
    "dataset_equal", "archetype_equal", "value_basis_equal", "finalization_equal", "memo_equal",
    "arithmetic_valid", "ranges_monotonic", "r_cva_reconciliation_valid",
    "pass_through_basis_partition_valid",
    "g_reconciliation_valid", "implementation_schedules_valid", "commercial_schedule_valid",
    "buyer_access_valid", "capacity_scope_valid", "o5_k5_n5_valid",
    "p_attribution_valid", "normalized_state_digest_valid", "downside_channels_valid",
    "constant_price_survival_valid", "survival_basket_reconciliation_valid",
    "fixed_base_laspeyres_valid", "h_gate_valid",
    "readiness_valid", "gates_valid",
)
core.INPUT_REVIEW_PASS_KEYS = (
    "evidence_state_honest", "base_supported", "range_supported", "scope_supported",
    "attribution_separated",
)
core.INVARIANT_CHECKS = set(core.INVARIANT_CHECKS) | {"operating_value_viability_h_gate"}
core.BASE_INPUTS = (
    ("inputs.recognized_revenue", "score", ("low", "base", "high")),
    ("inputs.employee_cash_cost", "score", ("low", "base", "high")),
    ("inputs.controllable_contractor_cash_cost", "score", ("low", "base", "high")),
    ("inputs.target_archetype_coverage", "score", ("low", "base", "high")),
    *(("inputs.implementation_realization.r%d" % year, "score", ("low", "base", "high"))
      for year in range(1, 6)),
    *(("inputs.implementation_investment.k%d" % year, "score", ("low", "base", "high"))
      for year in range(0, 6)),
    *(("inputs.commercial_retention.c%d" % year, "score", ("low", "base", "high"))
      for year in range(1, 6)),
    ("inputs.five_year_sale_availability", "score", ("low", "base", "high")),
    ("inputs.buyer_access_win_share", "score", ("low", "base", "high")),
    ("inputs.deal_execution_capacity_5y", "score", ("low", "base", "high")),
    ("inputs.integration_onboarding_capacity_5y", "score", ("low", "base", "high")),
    ("inputs.buy_mult", "score", ("low", "base", "high")),
    ("inputs.normalized_y5_operating_state", "score", ("low", "base", "high")),
    ("inputs.downside_exit_mult", "score", ("low", "base", "high")),
    ("inputs.operator_controlled_value_added_demand_share_y5", "gate", ("low", "base", "high")),
)


def _v4_2_membership_errors(manifest, root):
    errors = []
    scope = manifest.get("scope")
    membership = manifest.get("membership", {})
    if not isinstance(membership, dict):
        return ["membership must be an object"]
    scope_ref_key = {"regression": "regression_membership",
                     "holdout": "holdout_membership", "full": None}.get(scope)
    expected_keys = {"target_universe", "target_expected", "target_omitted",
                     "snapshot_sha256"}
    if scope_ref_key:
        expected_keys.add(scope_ref_key)
    elif scope == "full":
        expected_keys.update(("regression_membership", "holdout_membership"))
    else:
        return ["v4.2 scope must be regression, holdout, or full"]
    if set(membership) != expected_keys:
        errors.append("%s membership must use the exact closed v4.2 snapshot shape" % scope)
    if membership.get("snapshot_sha256") != core.membership_sha256(membership):
        errors.append("membership snapshot digest is stale")

    refs = [("target universe", "target_universe", TARGET_UNIVERSE_PATH,
             FROZEN_TARGET_UNIVERSE_SHA256)]
    if scope in ("regression", "full"):
        refs.append(("regression membership", "regression_membership",
                     REGRESSION_MEMBERSHIP_PATH, FROZEN_REGRESSION_SHA256))
    if scope in ("holdout", "full"):
        refs.append(("holdout membership", "holdout_membership",
                     HOLDOUT_MEMBERSHIP_PATH, FROZEN_HOLDOUT_SHA256))
    for label, key, path, digest in refs:
        ref = membership.get(key)
        errors.extend(core._ref_errors(label, ref, root))
        if isinstance(ref, dict) and ref.get("path") != path:
            errors.append("%s must use canonical path %s" % (label, path))
        if isinstance(ref, dict) and ref.get("sha256") != digest:
            errors.append("%s digest differs from the frozen v4.2 authority" % label)

    try:
        universe_value = core.load_json(core._absolute(root, TARGET_UNIVERSE_PATH))
        rows = universe_value.get("codes") if isinstance(universe_value, dict) else None
        universe = [row.get("naics") for row in rows] if isinstance(rows, list) else []
    except (OSError, ValueError, TypeError, AttributeError, json.JSONDecodeError):
        universe = []
    if (len(universe) != 63 or len(set(universe)) != 63
            or not all(isinstance(code, str) and re.fullmatch(r"[0-9]{6}", code)
                       for code in universe)):
        errors.append("target universe must contain exactly 63 unique six-digit codes")
        universe_set = set()
    else:
        universe_set = set(universe)

    expected = membership.get("target_expected")
    omitted = membership.get("target_omitted")
    valid_lists = True
    for label, values in (("target_expected", expected), ("target_omitted", omitted)):
        valid = (isinstance(values, list)
                 and all(isinstance(code, str) and re.fullmatch(r"[0-9]{6}", code)
                         for code in values)
                 and values == sorted(values) and len(values) == len(set(values)))
        if not valid:
            errors.append("membership %s must be a sorted unique code list" % label)
            valid_lists = False
    if valid_lists:
        if set(expected) & set(omitted):
            errors.append("membership expected and omitted codes must not overlap")
        if set(expected) | set(omitted) != universe_set:
            errors.append("membership expected/omitted union must equal the frozen 63-code universe")

    regression = set(REGRESSION_CODES)
    holdout = set(HOLDOUT_CODES)
    exact_expected = (regression if scope == "regression" else holdout if scope == "holdout"
                      else universe_set - regression - holdout)
    exact_omitted = universe_set - exact_expected
    if not valid_lists or expected != sorted(exact_expected) or omitted != sorted(exact_omitted):
        errors.append("%s membership expected/omitted partition is not exact" % scope)
    if regression & holdout or len(regression | holdout) != 10:
        errors.append("regression and holdout authorities must be exact disjoint five-code sets")
    return errors


def _selection_bound(selection, bound, inverted=False):
    if not isinstance(selection, dict):
        return None
    if bound == "base":
        return selection.get("value")
    key = "high" if inverted and bound == "low" else "low" if inverted else bound
    return selection.get("range", {}).get(key)


def _h_record_errors(record):
    errors = []
    inputs = record.get("inputs", {})
    realization = inputs.get("implementation_realization", {})
    investment = inputs.get("implementation_investment", {})
    retention = inputs.get("commercial_retention", {})
    scenarios = record.get("scenarios", {})
    tolerance = 1e-9
    weights = [1.0 / (1.1 ** year) for year in range(1, 6)]
    for bound in ("low", "base", "high"):
        scenario = scenarios.get(bound, {})
        g_value = scenario.get("subfactors", {}).get("V", {}).get("G")
        scores = scenario.get("scores", {})
        actual = scenario.get("subfactors", {}).get("h", {})
        if not isinstance(actual, dict) or set(actual) != {
                "discounted_retained_realization", "discounted_investment", "h", "gate_triggered"}:
            errors.append("%s scenario h diagnostic must use the exact closed v4.2 shape" % bound)
            continue
        structural_zero = (isinstance(g_value, (int, float)) and not isinstance(g_value, bool)
                           and math.isfinite(g_value) and g_value == 0)
        unresolved_g = g_value is None or g_value in ("UNBOUNDED", "NEGATIVE_UNBOUNDED")
        if structural_zero:
            if scores.get("V") != 0 or scores.get("I") != 0:
                errors.append("%s scenario G=0 requires structural V=0 and I=0" % bound)
        elif unresolved_g:
            expected_score = None if bound == "base" else 0.0 if bound == "low" else 10.0
            if scores.get("V") != expected_score or scores.get("I") != expected_score:
                errors.append("%s scenario missing/unbounded G has inconsistent V/I support" % bound)
        elif (not isinstance(g_value, (int, float)) or isinstance(g_value, bool)
              or not math.isfinite(g_value) or g_value < 0):
            errors.append("%s scenario V.G must be nonnegative finite, null, or unbounded" % bound)
        r = [_selection_bound(realization.get("r%d" % year), bound) for year in range(1, 6)]
        c = [_selection_bound(retention.get("c%d" % year), bound) for year in range(1, 6)]
        k = [_selection_bound(investment.get("k%d" % year), bound, inverted=True)
             for year in range(0, 6)]
        if any(value is None for value in r + c + k):
            if actual.get("h") is not None or (bound == "base" and actual.get("gate_triggered") is not None):
                errors.append("%s scenario unresolved h must remain null" % bound)
            continue
        retained = sum(r[index] * c[index] * weights[index] for index in range(5))
        discounted_investment = k[0] + sum(k[index + 1] * weights[index] for index in range(5))
        h_value = retained - discounted_investment
        expected_gate = h_value <= 0
        for key, expected in (("discounted_retained_realization", retained),
                              ("discounted_investment", discounted_investment), ("h", h_value)):
            value = actual.get(key)
            if not isinstance(value, (int, float)) or isinstance(value, bool) or not math.isfinite(value):
                errors.append("%s scenario h.%s must be finite" % (bound, key))
            elif abs(value - expected) > tolerance:
                errors.append("%s scenario h.%s differs from primitive inputs" % (bound, key))
        if actual.get("gate_triggered") is not expected_gate:
            errors.append("%s scenario h gate must trigger iff h <= 0" % bound)
    base_g = scenarios.get("base", {}).get("subfactors", {}).get("V", {}).get("G")
    decision = record.get("decision")
    if isinstance(decision, dict):
        verdict = decision.get("economic_verdict")
        reasons = decision.get("gate_reasons", [])
        if isinstance(base_g, (int, float)) and not isinstance(base_g, bool) and base_g == 0:
            if verdict != "kill":
                errors.append("base G=0 must produce a structural factor kill")
        elif base_g is None or base_g in ("UNBOUNDED", "NEGATIVE_UNBOUNDED"):
            if verdict != "indeterminate":
                errors.append("missing/unbounded base G must remain economically indeterminate")
    return errors


_base_build_input_registry = core.build_input_registry
_base_input_value = core._input_value


def _v4_2_build_input_registry(record, industry_spec=None):
    rows = _base_build_input_registry(record, industry_spec)
    spec_roles = {item.get("title"): item for item in
                  (industry_spec or {}).get("value_basis", {}).get("roles", [])}
    for row in rows:
        if row["input_path"].startswith("inputs.target_role_mix.roles[role_id=") \
                and row["input_path"].endswith(".cost_weight"):
            role_name = row["input_path"].split("[role_id=", 1)[1].split("]", 1)[0]
            row["source_ids"] = sorted(set(spec_roles.get(role_name, {}).get("source_ids", [])))
    for item in sorted(record.get("inputs", {}).get("third_party_pass_through", []),
                       key=lambda value: value.get("cost_id", "")):
        selection = item.get("amount", {})
        rows.append({
            "input_path": "inputs.third_party_pass_through[cost_id=%s].amount" % item.get("cost_id"),
            "driving_class": "score", "source_ids": sorted(set(selection.get("source_ids", []))),
            "required_bounds": ["low", "base", "high"],
        })
    return sorted(rows, key=lambda item: item["input_path"])


def _v4_2_input_value(record, industry_spec, path):
    if path.startswith("inputs.third_party_pass_through[cost_id="):
        cost_id = path.split("[cost_id=", 1)[1].split("]", 1)[0]
        return next(item["amount"] for item in record["inputs"]["third_party_pass_through"]
                    if item["cost_id"] == cost_id)
    return _base_input_value(record, industry_spec, path)


def _v4_2_declared_caveats(record, industry_spec=None):
    caveats = []
    for row in _v4_2_build_input_registry(record, industry_spec):
        path = row["input_path"]
        if path.startswith("industry_spec.") or path.endswith(".cost_weight"):
            continue
        try:
            selection = _v4_2_input_value(record, industry_spec or {}, path)
        except (KeyError, StopIteration, TypeError):
            continue
        for caveat in selection.get("caveats", []) if isinstance(selection, dict) else []:
            caveats.append("%s: %s" % (path, caveat))
    for caveat in record.get("inputs", {}).get("target_role_mix", {}).get("caveats", []):
        caveats.append("inputs.target_role_mix: %s" % caveat)
    for caveat in (industry_spec or {}).get("value_basis", {}).get("caveats", []):
        caveats.append("industry_spec.value_basis: %s" % caveat)
    return list(dict.fromkeys(caveats))


V4_2_REMEDIATION_PACKET_PATHS = {
    "inputs.recognized_revenue": ("inputs", "recognized_revenue"),
    "inputs.employee_cash_cost": ("inputs", "employee_cash_cost"),
    "inputs.controllable_contractor_cash_cost": ("inputs", "controllable_contractor_cash_cost"),
    "inputs.target_archetype_coverage": ("inputs", "target_archetype_coverage"),
    "inputs.five_year_sale_availability": ("inputs", "five_year_sale_availability"),
    "inputs.buyer_access_win_share": ("inputs", "buyer_access_win_share"),
    "inputs.deal_execution_capacity_5y": ("inputs", "deal_execution_capacity_5y"),
    "inputs.integration_onboarding_capacity_5y":
        ("inputs", "integration_onboarding_capacity_5y"),
    "inputs.buy_mult": ("inputs", "buy_multiple"),
    "inputs.normalized_y5_operating_state": ("inputs", "normalized_y5_operating_state"),
    "inputs.downside_exit_mult": ("inputs", "downside_exit_multiple"),
    "inputs.operator_controlled_value_added_demand_share_y5":
        ("inputs", "operator_controlled_value_added_demand_share_y5"),
}


def _v4_2_remediation_semantic_errors(first, second, findings, root):
    """Allow only exact v4.2 predecessor-linked primitive edits."""
    errors = []
    linked_inputs = {path for finding in findings for path in finding.get("input_paths", [])}
    linked_sources = {source for finding in findings for source in finding.get("source_ids", [])}
    for source in first.get("source_registry", []):
        if source.get("source_id") in linked_sources:
            linked_inputs.update(source.get("input_paths", []))
    try:
        old = {key: core.load_json(core._absolute(root, first["artifacts"][key]["path"]))
               for key in ("packet", "dataset", "industry_spec", "record")}
        new = {key: core.load_json(core._absolute(root, second["artifacts"][key]["path"]))
               for key in ("packet", "dataset", "industry_spec", "record")}
    except (OSError, ValueError, TypeError, KeyError, json.JSONDecodeError) as exc:
        return ["cannot compare remediation semantics: %s" % exc]
    if old["dataset"] != new["dataset"]:
        errors.append("attempt 2 may not change the frozen dataset")
    if old["industry_spec"] != new["industry_spec"]:
        errors.append("attempt 2 may not change the frozen industry spec")

    old_rows = {item["input_path"]: item for item in first.get("input_registry", [])}
    new_rows = {item["input_path"]: item for item in second.get("input_registry", [])}
    for path in sorted(set(old_rows) | set(new_rows)):
        changed = old_rows.get(path) != new_rows.get(path)
        if not changed and path in old_rows and path in new_rows:
            try:
                changed = _v4_2_input_value(old["record"], old["industry_spec"], path) != \
                    _v4_2_input_value(new["record"], new["industry_spec"], path)
            except (KeyError, StopIteration, TypeError):
                changed = True
        if changed and path not in linked_inputs:
            errors.append("attempt 2 changes unlinked input %s" % path)

    old_sources = {item["source_id"]: item for item in first.get("source_registry", [])}
    new_sources = {item["source_id"]: item for item in second.get("source_registry", [])}
    authorized_source_changes = set(linked_sources)
    for source_id in sorted(set(old_sources) | set(new_sources)):
        old_row, new_row = old_sources.get(source_id), new_sources.get(source_id)
        if old_row == new_row:
            continue
        affected = set((old_row or {}).get("input_paths", [])) | set(
            (new_row or {}).get("input_paths", []))
        if source_id in linked_sources or (affected and affected <= linked_inputs):
            authorized_source_changes.add(source_id)
        else:
            errors.append("attempt 2 changes source outside exact linked inputs: %s" % source_id)

    old_packet, new_packet = copy.deepcopy(old["packet"]), copy.deepcopy(new["packet"])
    for packet in (old_packet, new_packet):
        packet.pop("run_meta", None)
        for path in linked_inputs:
            location = V4_2_REMEDIATION_PACKET_PATHS.get(path)
            if location:
                packet.get(location[0], {}).pop(location[1], None)
                continue
            match = re.fullmatch(
                r"inputs\.(implementation_realization|implementation_investment|commercial_retention)\.([rkc][0-5])",
                path)
            if match:
                packet.get("inputs", {}).get(match.group(1), {}).pop(match.group(2), None)
        if authorized_source_changes:
            packet["sources"] = [row for row in packet.get("sources", [])
                                 if row.get("id") not in authorized_source_changes]
    if old_packet != new_packet:
        errors.append("attempt 2 changes packet content outside predecessor-linked v4.2 primitives")
    return errors


core._membership_errors = _v4_2_membership_errors
core._extra_record_errors = _h_record_errors
core._remediation_semantic_errors = _v4_2_remediation_semantic_errors
core.build_input_registry = _v4_2_build_input_registry
core._input_value = _v4_2_input_value
core.declared_caveats = _v4_2_declared_caveats

_CORE_ENTRY_ERRORS = core._entry_errors

V4_2_MANIFEST_BASE_KEYS = {
    "manifest_version", "campaign_id", "scope", "toolchain", "membership", "entries",
    "issuance_plan", "freeze", "authorization", "manifest_sha256",
}
V4_2_ENTRY_BASE_KEYS = {
    "entry_id", "kind", "naics", "title", "run_id", "run_date", "attempt",
    "remediates_run_id", "issuance_entry_sha256", "artifacts", "review_path",
    "input_registry", "source_registry", "authored_caveats",
}
V4_2_ATTEMPT_2_KEYS = {
    "remediates_entry_id", "predecessor_review_sha256", "predecessor_run_sha256",
    "remediable_paths", "remediation_bundle",
}
V4_2_PLAN_IDENTITY_KEYS = (
    "entry_id", "kind", "naics", "title", "run_id", "run_date", "attempt",
    "remediates_run_id",
)
V4_2_PLAN_LINEAGE_KEYS = (
    "remediates_entry_id", "predecessor_review_sha256", "predecessor_run_sha256",
    "remediable_paths",
)
_OUTCOME_HINT = re.compile(
    r"\b(?:expected[ _-]?outcome|prior[ _-]?(?:result|outcome)|"
    r"previous[ _-]?(?:result|outcome)|preselected[ _-]?(?:result|outcome))\b",
    re.IGNORECASE,
)
OPERATOR_SIGNOFF_VERSION = "root-operator-signoff-4.2"
OPERATOR_SIGNOFF_PRINCIPAL = "jkee"
OPERATOR_SIGNOFF_NAMESPACE = "rollup-economy-v4.2-root-operator-gate-signoff"
OPERATOR_SIGNOFF_ALLOWED_SIGNERS = "pipeline/v4_2/allowed_signers"
GATE_SENTINEL_RUNNER = subprocess.run


def _gate_ref_errors(label, ref, root):
    if not isinstance(ref, dict) or set(ref) != {"path", "sha256", "byte_length"}:
        return [label + " must contain exact path/sha256/byte_length"]
    try:
        path = core._absolute(root, ref["path"])
        content = Path(path).read_bytes()
        if len(content) != ref["byte_length"] or core.sha256(path) != ref["sha256"]:
            return [label + " digest/length is stale"]
    except (OSError, TypeError, ValueError) as exc:
        return [label + " is invalid: %s" % exc]
    return []


def gate_entries_root(manifest, selected, review_hashes):
    value = {
        "scope": manifest.get("scope"), "campaign_id": manifest.get("campaign_id"),
        "issuance_plan_sha256": manifest.get("issuance_plan", {}).get("sha256"),
        "entries": [
            {"entry": entry, "review_sha256": review_hashes.get(entry.get("entry_id"))}
            for entry in sorted(selected, key=lambda item: item.get("entry_id", ""))
        ],
    }
    return core.value_sha256(value)


def _v4_2_operator_signoff_errors(manifest, selected, review_hashes, root, gate, label):
    errors = []
    report_ref = gate.get("sentinel_gate_report")
    errors.extend(_gate_ref_errors(label + " sentinel gate report", report_ref, root))
    signoff = gate.get("operator_signoff")
    if not isinstance(signoff, dict) or set(signoff) != {"payload", "signature"}:
        return errors + [label + " operator_signoff requires payload/signature refs"]
    errors.extend(_gate_ref_errors(label + " operator payload", signoff.get("payload"), root))
    errors.extend(_gate_ref_errors(label + " operator signature", signoff.get("signature"), root))
    if errors:
        return errors
    report_path = core._absolute(root, report_ref["path"])
    try:
        report = core.load_json(report_path)
        gate_report_v4_2.validate_report(root, report, runner=GATE_SENTINEL_RUNNER)
    except Exception as exc:
        return [label + " sentinel gate report failed deterministic validation: %s" % exc]
    expected_records = sorted(
        entry.get("artifacts", {}).get("record", {}).get("path") for entry in selected)
    if (report.get("scope") != manifest.get("scope")
            or sorted(item.get("path") for item in report.get("records", [])) != expected_records):
        errors.append(label + " sentinel gate report does not cover exact selected records")
    payload_path = core._absolute(root, signoff["payload"]["path"])
    signature_path = core._absolute(root, signoff["signature"]["path"])
    payload_bytes = Path(payload_path).read_bytes()
    payload = core.load_json(payload_path)
    required = {
        "signoff_version", "scope", "campaign_id", "issuance_plan_sha256",
        "entries_artifacts_reviews_root_sha256", "sentinel_gate_report_sha256",
        "decision", "timestamp", "git_context", "signer_principal",
        "signature_namespace",
    }
    if not isinstance(payload, dict) or set(payload) != required:
        return errors + [label + " operator payload is not the closed v4.2 contract"]
    if payload_bytes != core.canonical_bytes(payload):
        errors.append(label + " operator payload must be canonical JSON")
    expected = {
        "signoff_version": OPERATOR_SIGNOFF_VERSION,
        "scope": manifest.get("scope"), "campaign_id": manifest.get("campaign_id"),
        "issuance_plan_sha256": manifest.get("issuance_plan", {}).get("sha256"),
        "entries_artifacts_reviews_root_sha256": gate_entries_root(
            manifest, selected, review_hashes),
        "sentinel_gate_report_sha256": report_ref["sha256"],
        "decision": "approve", "signer_principal": OPERATOR_SIGNOFF_PRINCIPAL,
        "signature_namespace": OPERATOR_SIGNOFF_NAMESPACE,
    }
    for key, value in expected.items():
        if payload.get(key) != value:
            errors.append(label + " operator payload %s binding differs" % key)
    try:
        timestamp = datetime.fromisoformat(payload.get("timestamp", "").replace("Z", "+00:00"))
        if timestamp.tzinfo is None or timestamp > datetime.now(timezone.utc).astimezone(timestamp.tzinfo):
            raise ValueError
    except (TypeError, ValueError):
        errors.append(label + " operator timestamp must be timezone-aware and not future")
    context = payload.get("git_context")
    oid = re.compile(r"[0-9a-f]{40}")
    if (not isinstance(context, dict)
            or set(context) != {"commit_sha", "tag_name", "tag_object_sha"}
            or not oid.fullmatch(context.get("commit_sha", ""))
            or not oid.fullmatch(context.get("tag_object_sha", ""))
            or not re.fullmatch(r"v4\.2-[A-Za-z0-9._-]+", context.get("tag_name", ""))):
        errors.append(label + " operator git context is invalid")
    else:
        checks = (("refs/tags/%s^{tag}" % context["tag_name"], context["tag_object_sha"]),
                  ("%s^{commit}" % context["tag_object_sha"], context["commit_sha"]))
        for expression, expected_oid in checks:
            result = subprocess.run(["git", "-C", root, "rev-parse", expression],
                                    stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                    text=True, check=False)
            if result.returncode or result.stdout.strip() != expected_oid:
                errors.append(label + " operator git context differs from repository")
        result = subprocess.run(
            ["git", "-C", root, "-c", "gpg.ssh.allowedSignersFile=" +
             OPERATOR_SIGNOFF_ALLOWED_SIGNERS, "verify-tag", "--raw", context["tag_object_sha"]],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)
        if result.returncode:
            errors.append(label + " operator git tag signature is not verified")
    result = subprocess.run(
        ["ssh-keygen", "-Y", "verify", "-f",
         core._absolute(root, OPERATOR_SIGNOFF_ALLOWED_SIGNERS),
         "-I", OPERATOR_SIGNOFF_PRINCIPAL, "-n", OPERATOR_SIGNOFF_NAMESPACE,
         "-s", signature_path], input=payload_bytes,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)
    if result.returncode:
        errors.append(label + " operator SSH signature is not verified")
    return errors


core._operator_signoff_errors = _v4_2_operator_signoff_errors


def _v4_2_manifest_shape_errors(manifest):
    if not isinstance(manifest, dict):
        return ["manifest must be an object"]
    allowed = set(V4_2_MANIFEST_BASE_KEYS)
    optional = {"regression": {"regression_gate"}, "holdout": {"holdout_gate"},
                "full": {"full_gate_certificates"}}.get(manifest.get("scope"), set())
    unknown = set(manifest) - allowed - optional
    missing = allowed - set(manifest)
    errors = []
    if unknown:
        errors.append("campaign manifest contains unknown keys: %s" % sorted(unknown))
    if missing:
        errors.append("campaign manifest is missing required keys: %s" % sorted(missing))
    if manifest.get("scope") == "full" and "full_gate_certificates" not in manifest:
        errors.append("full campaign requires gate certificate bindings")
    gate_key = {"regression": "regression_gate", "holdout": "holdout_gate"}.get(
        manifest.get("scope"))
    if gate_key is not None and gate_key in manifest:
        gate = manifest.get(gate_key)
        if not isinstance(gate, dict) or set(gate) != {
                "sentinel_gate_report", "operator_signoff"}:
            errors.append("%s must contain exact sentinel_gate_report/operator_signoff" % gate_key)
    return errors


def _v4_2_entry_shape_errors(entry):
    if not isinstance(entry, dict):
        return ["entry must be an object"]
    expected = set(V4_2_ENTRY_BASE_KEYS)
    if entry.get("attempt") == 2:
        expected.update(V4_2_ATTEMPT_2_KEYS)
    if set(entry) != expected:
        return ["attempt %s entry must use the exact closed v4.2 key set" %
                entry.get("attempt")]
    if entry.get("attempt") == 1 and entry.get("remediates_run_id") is not None:
        return ["attempt 1 remediates_run_id must be null"]
    return []


def _v4_2_entry_leakage_errors(entry):
    if not isinstance(entry, dict):
        return []
    visible_keys = {
        "entry_id", "kind", "naics", "title", "run_id", "run_date", "attempt",
        "remediates_run_id", "input_registry", "source_registry", "authored_caveats",
    } | (V4_2_ATTEMPT_2_KEYS - {"remediation_bundle"})
    visible = {key: entry[key] for key in visible_keys if key in entry}
    errors = runtime_linter.structured_visibility_errors(entry, "campaign entry")
    text = core.canonical_bytes(visible).decode("utf-8")
    errors.extend(runtime_linter.leakage_errors(
        text, "campaign entry", allowed_naics=entry.get("naics")))
    # ``authored_caveats`` is deterministically regenerated from the frozen
    # pre-run record/spec inputs.  It can legitimately explain that an input
    # does not encode an "expected outcome"; treating that phrase as leaked
    # result knowledge makes a valid frozen campaign impossible to manifest.
    # Continue scanning all other reviewer-visible entry metadata.
    outcome_visible = dict(entry)
    outcome_visible.pop("authored_caveats", None)
    if _OUTCOME_HINT.search(core.canonical_bytes(outcome_visible).decode("utf-8")):
        errors.append("campaign entry exposes a forbidden prior/expected outcome hint")
    return errors


def _v4_2_entry_errors(entry, manifest, root):
    closure_errors = _v4_2_entry_shape_errors(entry)
    leakage_errors = _v4_2_entry_leakage_errors(entry)
    errors = [item for item in _CORE_ENTRY_ERRORS(entry, manifest, root)
              if item not in ("entry_id mismatch", "entry kind must be fleet or golden",
                              "execution envelope model route mismatch")]
    errors = closure_errors + leakage_errors + errors
    if not isinstance(entry, dict):
        return errors
    entry_id = entry.get("entry_id") if isinstance(entry, dict) else None
    if not isinstance(entry_id, str) or not re.fullmatch(r"entry_v42_[0-9a-f]{24}_a[12]", entry_id):
        errors.append("entry_id must be an opaque v4.2 issued identifier")
    if entry.get("kind") != "target":
        errors.append("entry kind must be the neutral target class")
    try:
        envelope = core.load_json(core._absolute(
            root, entry["artifacts"]["execution_envelope"]["path"]))
    except (OSError, ValueError, TypeError, KeyError, json.JSONDecodeError):
        return errors
    if envelope.get("kind") != "target" or envelope.get("model_id") != "gpt-5.6-terra":
        errors.append("execution envelope must use neutral target kind and target model route")
    return errors


core._entry_errors = _v4_2_entry_errors

_CORE_ISSUANCE_ERRORS = core._issuance_errors


def _ref_projection(ref):
    if not isinstance(ref, dict):
        return ref
    return {key: ref.get(key) for key in ("path", "sha256")}


def _v4_2_plan_binding_errors(manifest, plan):
    errors = []
    membership = manifest.get("membership", {})
    plan_membership = plan.get("membership", {}) if isinstance(plan, dict) else {}
    if plan_membership.get("codes") != membership.get("target_expected"):
        errors.append("issuance plan membership differs from campaign membership")
    bindings = (("target_universe", "target_universe"),
                ("regression_membership", "regression_manifest"),
                ("holdout_membership", "holdout_manifest"))
    for campaign_key, plan_key in bindings:
        if campaign_key in membership and _ref_projection(plan_membership.get(plan_key)) != \
                membership.get(campaign_key):
            errors.append("issuance plan %s differs from campaign membership" % plan_key)
        if campaign_key not in membership and plan_membership.get(plan_key) is not None:
            errors.append("issuance plan carries an unauthorized %s" % plan_key)
    planned_certificates = plan_membership.get("full_gate_certificates")
    if isinstance(planned_certificates, dict):
        planned_certificates = {key: _ref_projection(ref)
                                for key, ref in planned_certificates.items()}
    if manifest.get("scope") == "full":
        if manifest.get("full_gate_certificates") != planned_certificates:
            errors.append("full campaign gate certificates differ from the issued plan")
    elif planned_certificates is not None:
        errors.append("non-full issuance plan may not carry gate certificates")

    plan_entries = {item.get("entry_id"): item for item in plan.get("entries", [])
                    if isinstance(item, dict)}
    for entry in manifest.get("entries", []):
        if not isinstance(entry, dict):
            continue
        planned = plan_entries.get(entry.get("entry_id"))
        if not isinstance(planned, dict):
            continue
        keys = V4_2_PLAN_IDENTITY_KEYS + (V4_2_PLAN_LINEAGE_KEYS
                                         if entry.get("attempt") == 2 else ())
        for key in keys:
            if entry.get(key) != planned.get(key):
                errors.append("%s issued %s differs" % (entry.get("entry_id"), key))
        if entry.get("attempt") == 2 and entry.get("remediation_bundle") != \
                _ref_projection(planned.get("remediation_bundle")):
            errors.append("%s issued remediation_bundle differs" % entry.get("entry_id"))
    return errors


def _v4_2_issuance_errors(manifest, root):
    obsolete_v4_1_errors = {
        "issuance plan membership differs from campaign membership",
        # v4.1 incorrectly applies its 64-hex content-digest predicate to the
        # Git commit OID.  v4.2's issuer/freeze contract separately validates
        # the exact 40-hex commit, signed annotated tag, and CI receipt.
        "issuance plan lacks exact nonzero freeze root/manifest/commit bindings",
    }
    errors = [item for item in _CORE_ISSUANCE_ERRORS(manifest, root)
              if item not in obsolete_v4_1_errors]
    plan_ref = manifest.get("issuance_plan", {})
    try:
        plan, _plan_errors = issuer_v4_2.validate_issued_plan(
            root, plan_ref.get("path"), manifest.get("scope"))
    except (OSError, TypeError, ValueError):
        plan = {}
    if isinstance(plan, dict) and plan:
        errors.extend(_v4_2_plan_binding_errors(manifest, plan))
    return errors


core._issuance_errors = _v4_2_issuance_errors

_CORE_VALIDATE_MANIFEST = core.validate_manifest


def _v4_2_validate_manifest(manifest, root=REPO):
    shape_errors = _v4_2_manifest_shape_errors(manifest)
    if not isinstance(manifest, dict):
        return shape_errors
    errors = shape_errors + _CORE_VALIDATE_MANIFEST(manifest, root)
    expected = {("target", code) for code in
                manifest.get("membership", {}).get("target_expected", [])}
    actual = {(item.get("kind"), item.get("naics"))
              for item in manifest.get("entries", []) if isinstance(item, dict)}
    if actual == expected:
        errors = [item for item in errors if item != "entry membership differs from frozen expected membership"]
    elif "entry membership differs from frozen expected membership" not in errors:
        errors.append("entry membership differs from frozen expected membership")
    if manifest.get("scope") == "full":
        errors.extend(core._full_gate_certificate_errors(manifest, root))
    return errors


core.validate_manifest = _v4_2_validate_manifest

_CORE_FIVE_CODE_GATE_ERRORS = core._five_code_gate_errors


def _v4_2_five_code_gate_errors(manifest, selected, reviews, review_hashes, root,
                                label, codes, gate_key):
    errors = _CORE_FIVE_CODE_GATE_ERRORS(
        manifest, selected, reviews, review_hashes, root, label, codes, gate_key)
    if len(selected) == 5 and {(item["kind"], item["naics"]) for item in selected} == {
            ("target", code) for code in codes}:
        errors = [item for item in errors
                  if item != label + " gate: selected membership is not exact 5/5"]
    return errors


core._five_code_gate_errors = _v4_2_five_code_gate_errors

_CORE_FREEZE_MANIFEST = core.freeze_manifest


def _v4_2_freeze_manifest(campaign_id, scope, entries, root=REPO, fleet_expected=None,
                          golden_expected=None, partial_authorization=None,
                          full_gate_certificates=None, issuance_plan_path=None):
    if scope not in ("regression", "holdout", "full"):
        raise ValueError("v4.2 scope must be regression, holdout, or full")
    if fleet_expected is not None or golden_expected is not None or partial_authorization is not None:
        raise ValueError("v4.2 freeze forbids obsolete fleet/golden/partial routing fields")
    if not issuance_plan_path:
        raise ValueError("issuance_plan_path is required; campaign entries may not be self-issued")
    if not isinstance(entries, list) or any(not isinstance(entry, dict) for entry in entries):
        raise ValueError("campaign entries must be an array of closed objects")
    plan, plan_errors = issuer_v4_2.validate_issued_plan(root, issuance_plan_path, scope)
    if plan_errors:
        raise ValueError("cannot bind invalid v4.2 issuance plan: " + "; ".join(plan_errors))
    expected_codes = sorted(plan.get("membership", {}).get("codes", []))
    expected_size = issuer_v4_2.FULL_SIZE if scope == "full" else 5
    if len(expected_codes) != expected_size:
        raise ValueError("%s plan must issue exactly %d targets" % (scope, expected_size))
    plan_entries = {item["entry_id"]: item for item in plan.get("entries", [])}
    if len(plan_entries) != len(plan.get("entries", [])):
        raise ValueError("issued plan entry identities must be unique")
    entries = copy.deepcopy(entries)
    if set(plan_entries) != {item.get("entry_id") for item in entries
                             if isinstance(item, dict)}:
        raise ValueError("campaign entries must exactly equal issued plan entries")
    for entry in entries:
        expected_input_keys = set(V4_2_ENTRY_BASE_KEYS)
        if entry.get("attempt") == 2:
            expected_input_keys.update(V4_2_ATTEMPT_2_KEYS)
        expected_input_keys.remove("issuance_entry_sha256")
        if set(entry) != expected_input_keys:
            raise ValueError("campaign entry input contains missing or unvalidated extra keys")
    for entry in entries:
        entry["issuance_entry_sha256"] = core.value_sha256(plan_entries[entry["entry_id"]])
    toolchain = {key: core.artifact_ref(core.TOOLCHAIN_PATHS[key], root)
                 for key in core.TOOLCHAIN_KEYS}
    plan_membership = plan.get("membership", {})
    universe_value = core.load_json(core._absolute(root, TARGET_UNIVERSE_PATH))
    universe_codes = sorted(row["naics"] for row in universe_value["codes"])
    membership = {
        "target_universe": _ref_projection(plan_membership.get("target_universe")),
        "target_expected": expected_codes,
        "target_omitted": sorted(set(universe_codes) - set(expected_codes)),
    }
    if scope in ("regression", "full"):
        membership["regression_membership"] = _ref_projection(
            plan_membership.get("regression_manifest"))
    if scope in ("holdout", "full"):
        membership["holdout_membership"] = _ref_projection(
            plan_membership.get("holdout_manifest"))
    membership["snapshot_sha256"] = core.membership_sha256(membership)
    manifest = {
        "manifest_version": core.MANIFEST_VERSION, "campaign_id": campaign_id,
        "scope": scope, "toolchain": toolchain, "membership": membership,
        "entries": sorted(entries, key=lambda item: (
            item["kind"], item["naics"], item["attempt"], item["run_id"])),
        "issuance_plan": core.artifact_ref(issuance_plan_path, root),
        "freeze": copy.deepcopy(plan["freeze"]),
        "authorization": copy.deepcopy(plan["authorization"]),
    }
    if scope == "full":
        planned_certificates = {
            key: _ref_projection(ref) for key, ref in
            plan_membership.get("full_gate_certificates", {}).items()
        }
        if full_gate_certificates is not None:
            if not isinstance(full_gate_certificates, dict):
                raise ValueError("full gate certificates must be an object")
            supplied = {key: _ref_projection(ref)
                        for key, ref in full_gate_certificates.items()}
            if supplied != planned_certificates:
                raise ValueError("full gate certificates differ from the issued plan")
        manifest["full_gate_certificates"] = planned_certificates
    elif full_gate_certificates is not None:
        raise ValueError("gate certificates may be supplied only for full scope")
    manifest["manifest_sha256"] = core.manifest_sha256(manifest)
    errors = core.validate_manifest(manifest, root)
    if errors:
        raise ValueError("cannot freeze invalid v4.2 manifest: " + "; ".join(errors))
    return manifest


core.freeze_manifest = _v4_2_freeze_manifest

_CORE_EVALUATE_CAMPAIGN = core.evaluate_campaign


def _v4_2_evaluate_campaign(manifest, root=REPO, require_reviews=True):
    status, errors = _CORE_EVALUATE_CAMPAIGN(manifest, root, require_reviews)
    by_target = {}
    for entry in manifest.get("entries", []):
        if isinstance(entry, dict):
            by_target.setdefault(entry.get("naics"), []).append(entry)
    for attempts in by_target.values():
        second = next((item for item in attempts if item.get("attempt") == 2), None)
        first = next((item for item in attempts if item.get("attempt") == 1), None)
        if second is None or first is None:
            continue
        try:
            prior = core.load_json(core._absolute(root, first["review_path"]))
        except (OSError, ValueError, TypeError, KeyError, json.JSONDecodeError):
            continue
        fatal = any(isinstance(item, dict) and item.get("severity") == "fatal_mechanics"
                    for item in prior.get("findings", []))
        if prior.get("outcome") != "reject" or fatal:
            errors.append("%s attempt 2 requires a non-fatal exact reject predecessor" %
                          second.get("entry_id"))
    if errors:
        status["campaign_accepted"] = False
    return status, errors


core.evaluate_campaign = _v4_2_evaluate_campaign

# Export the configured hardened API. Functions retain core's globals, which
# have already been replaced with v4.2-only contracts above.
for _name in dir(core):
    if not _name.startswith("__"):
        globals()[_name] = getattr(core, _name)

CANARY_CODES = REGRESSION_CODES
HOLDOUT_CODES = core.HOLDOUT_CODES
TOOLCHAIN_PATHS = core.TOOLCHAIN_PATHS
TOOLCHAIN_KEYS = core.TOOLCHAIN_KEYS
MANIFEST_VERSION = core.MANIFEST_VERSION
REVIEW_PROMPT_VERSION = core.REVIEW_PROMPT_VERSION
MECHANICS_KEYS = core.MECHANICS_KEYS
INPUT_REVIEW_PASS_KEYS = core.INPUT_REVIEW_PASS_KEYS
INVARIANT_CHECKS = core.INVARIANT_CHECKS
BASE_INPUTS = core.BASE_INPUTS


if __name__ == "__main__":
    raise SystemExit(core.main())
