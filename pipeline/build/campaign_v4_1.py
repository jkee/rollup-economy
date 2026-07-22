#!/usr/bin/env python3
"""Fail-closed v4.1 campaign manifests, reviews, lineage, and release gates."""

import argparse
import copy
import hashlib
import importlib.util
import json
import os
import re
import subprocess
import sys
from datetime import date


HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
SCHEMAS = os.path.join(HERE, "schemas")
CANARY_CODES = ("541512", "541511", "541214", "238220", "541930")
HOLDOUT_MEMBERSHIP_PATH = "pipeline/v4_1/holdout_membership.json"
HOLDOUT_MEMBERSHIP_SHA256 = "1ca504621bcca9b5b64e7cccb08a56c3f9aeee0a623259f4f666be77c2b27e17"
HOLDOUT_CODES = ("541922", "541840", "541350", "541430", "541720")
FULL_GATE_PATHS = {
    "regression_canary": {
        "certificate": "pipeline/v4_1/gates/regression_canary/certificate.json",
        "campaign": "pipeline/v4_1/gates/regression_canary/campaign_proof.json",
        "gate": "pipeline/v4_1/gates/regression_canary/gate_proof.json",
        "source": "pipeline/v4_1/gates/regression_canary/source_campaign.json",
    },
    "holdout": {
        "certificate": "pipeline/v4_1/gates/holdout/certificate.json",
        "campaign": "pipeline/v4_1/gates/holdout/campaign_proof.json",
        "gate": "pipeline/v4_1/gates/holdout/gate_proof.json",
        "source": "pipeline/v4_1/gates/holdout/source_campaign.json",
    },
}
MANIFEST_VERSION = "review-campaign-4.1"
REVIEW_PROMPT_VERSION = "validator-4.1"
REVIEW_SCHEMA_FILENAME = "review_record_v4_1.schema.json"
DEVELOPMENT_SCOPE = "canary"
DEVELOPMENT_GATE_KEY = "canary_gate"
DEVELOPMENT_GATE_LABEL = "canary"
GATE_CERTIFICATE_VERSION = "gate-certificate-4.1"
GATE_CAMPAIGN_PROOF_VERSION = "gate-campaign-proof-4.1"
GATE_PROOF_VERSION = "gate-proof-4.1"
OPERATOR_SIGNOFF_VERSION = "root-operator-signoff-4.2"
OPERATOR_SIGNOFF_PRINCIPAL = "jkee"
OPERATOR_SIGNOFF_NAMESPACE = "rollup-economy-v4.2-root-operator-gate-signoff"
OPERATOR_SIGNOFF_ALLOWED_SIGNERS = "pipeline/v4_2/allowed_signers"
PUBLISHABLE = {"publishable", "publishable_with_caveats"}
INVARIANT_CHECKS = {
    "factor_monotonicity", "score_interval_ordering", "missingness_semantics",
    "survival_gate", "readiness_action_consistency",
}

ARTIFACT_KEYS = (
    "assembled_prompt", "packet", "dataset", "industry_spec", "execution_envelope", "record", "memo",
)
TOOLCHAIN_KEYS = (
    "methodology", "thresholds", "dataset_schema", "industry_spec_schema", "packet_schema",
    "run_schema", "review_schema", "scoring", "finalizer", "runner_prompt",
    "validator_prompt", "campaign_validator",
)
TOOLCHAIN_PATHS = {
    "methodology": "V4_1_METHODOLOGY.md",
    "thresholds": "pipeline/build/thresholds_v4_1.json",
    "dataset_schema": "pipeline/build/schemas/dataset_v4_1.schema.json",
    "industry_spec_schema": "pipeline/build/schemas/industry_spec_v4_1.schema.json",
    "packet_schema": "pipeline/build/schemas/research_packet_v4_1.schema.json",
    "run_schema": "pipeline/build/schemas/run_record_v4_1.schema.json",
    "review_schema": "pipeline/build/schemas/review_record_v4_1.schema.json",
    "scoring": "pipeline/build/v4_1_scoring.py",
    "finalizer": "pipeline/build/finalize_run_v4_1.py",
    "runner_prompt": "pipeline/template/runner_brief_v4_1.md",
    "validator_prompt": "pipeline/template/validator_brief_v4_1.md",
    "campaign_validator": "pipeline/build/campaign_v4_1.py",
}
MEMBERSHIP_PATHS = {
    "fleet_universe": "pipeline/blocks/targets_phase3.json",
    "golden_universe": "pipeline/golden/golden_set.json",
}
MECHANICS_KEYS = (
    "schema_valid", "identity_valid", "artifact_digests_valid", "toolchain_digests_valid",
    "dataset_equal", "roles_equal", "finalization_equal", "memo_equal", "arithmetic_valid",
    "ranges_monotonic", "readiness_valid", "gates_valid",
)
INPUT_REVIEW_PASS_KEYS = (
    "evidence_state_honest", "base_supported", "range_supported", "scope_supported",
)
BASE_INPUTS = (
    ("inputs.target_archetype_coverage", "score", ("low", "base", "high")),
    ("inputs.target_labor_cost_share", "score", ("low", "base", "high")),
    ("inputs.implementation_ramp.r1", "score", ("low", "base", "high")),
    ("inputs.implementation_ramp.r2", "score", ("low", "base", "high")),
    ("inputs.implementation_ramp.r3", "score", ("low", "base", "high")),
    ("inputs.implementation_ramp.r4", "score", ("low", "base", "high")),
    ("inputs.implementation_ramp.r5", "score", ("low", "base", "high")),
    ("inputs.commercial_retention", "score", ("low", "base", "high")),
    ("inputs.five_year_sale_availability", "score", ("low", "base", "high")),
    ("inputs.buy_mult", "score", ("low", "base", "high")),
    ("inputs.downside_exit_mult", "score", ("low", "base", "high")),
    ("inputs.y5_survival", "gate", ("low", "base", "high")),
    ("dataset_inputs.n_band", "score", ("low", "base", "high")),
)


def _load_module(name, filename):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, filename))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


legacy_build = _load_module("v4_1_schema_validator", "build.py")
issuer = _load_module("v4_1_issuance_validator", "issue_campaign_v4_1.py")


def _reject_constant(value):
    raise ValueError("non-standard JSON constant %r is forbidden" % value)


def _closed_pairs(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate JSON key %r" % key)
        result[key] = value
    return result


def load_json(path):
    with open(path, "r", encoding="utf-8") as handle:
        return json.load(handle, parse_constant=_reject_constant, object_pairs_hook=_closed_pairs)


def write_json(path, value):
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        json.dump(value, handle, indent=2, ensure_ascii=False, allow_nan=False)
        handle.write("\n")


def canonical_bytes(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False).encode("utf-8")


def value_sha256(value):
    return hashlib.sha256(canonical_bytes(value)).hexdigest()


def _is_sha256(value):
    return isinstance(value, str) and len(value) == 64 and all(char in "0123456789abcdef" for char in value)


def _is_nonzero_sha256(value):
    return _is_sha256(value) and value != "0" * 64


def sha256(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _absolute(root, relative):
    if not isinstance(relative, str) or not relative or os.path.isabs(relative):
        raise ValueError("artifact path must be a non-empty repository-relative path")
    root_real = os.path.realpath(root)
    path = os.path.realpath(os.path.join(root_real, relative))
    if os.path.commonpath((root_real, path)) != root_real:
        raise ValueError("artifact path escapes repository: %s" % relative)
    return path


def artifact_ref(path, root=REPO):
    absolute = _absolute(root, path)
    return {"path": path, "sha256": sha256(absolute)}


def _ref_errors(label, ref, root):
    errors = []
    if not isinstance(ref, dict) or set(ref) != {"path", "sha256"}:
        return ["%s must contain exactly path and sha256" % label]
    try:
        path = _absolute(root, ref["path"])
        if not os.path.isfile(path):
            errors.append("%s missing: %s" % (label, ref["path"]))
        elif sha256(path) != ref["sha256"]:
            errors.append("%s digest is stale" % label)
    except (OSError, TypeError, ValueError) as exc:
        errors.append("%s invalid: %s" % (label, exc))
    return errors


def _operator_artifact_digests(selected, review_hashes):
    """Return the closed artifact-digest set covered by a gate signoff."""
    result = {}
    for entry in sorted(selected, key=lambda item: item["entry_id"]):
        refs = entry.get("artifacts", {})
        digests = {key: refs.get(key, {}).get("sha256") for key in ARTIFACT_KEYS}
        digests["review"] = review_hashes.get(entry["entry_id"])
        result[entry["entry_id"]] = digests
    return result


def _operator_signoff_errors(manifest, selected, review_hashes, root, gate, label):
    """Verify the v4.2 root/operator payload and its detached SSH signature.

    The signature authenticates the frozen ``jkee`` principal.  It is not proof
    of a human act and deliberately makes no such claim.
    """
    errors = []
    signoff = gate.get("operator_signoff")
    if not isinstance(signoff, dict) or set(signoff) != {"payload", "signature"}:
        return [label + " operator_signoff must contain exact payload/signature refs"]
    for key in ("payload", "signature"):
        errors.extend(_ref_errors(label + " operator signoff " + key, signoff.get(key), root))
    if errors:
        return errors
    payload_path = _absolute(root, signoff["payload"]["path"])
    signature_path = _absolute(root, signoff["signature"]["path"])
    try:
        payload = load_json(payload_path)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        return [label + " operator signoff payload is invalid: %s" % exc]
    required = {
        "signoff_version", "campaign_binding_sha256", "gate_report_sha256",
        "artifact_digests", "decision", "signer_principal", "signed_at", "notes",
        "selected_entry_ids", "review_digests", "git_context",
    }
    if not isinstance(payload, dict) or set(payload) != required:
        return [label + " operator signoff payload is not the closed v4.2 contract"]
    with open(payload_path, "rb") as payload_handle:
        payload_bytes = payload_handle.read()
    if payload_bytes != canonical_bytes(payload):
        errors.append(label + " operator signoff payload must be canonical JSON")
    if payload.get("signoff_version") != OPERATOR_SIGNOFF_VERSION:
        errors.append(label + " operator signoff version is invalid")
    if payload.get("campaign_binding_sha256") != campaign_binding_sha256(manifest):
        errors.append(label + " operator signoff does not bind this campaign")
    invariant = gate.get("invariant_report", {})
    if payload.get("gate_report_sha256") != invariant.get("sha256"):
        errors.append(label + " operator signoff does not bind the exact gate report")
    entry_ids = sorted(item["entry_id"] for item in selected)
    expected_reviews = dict(sorted(
        (entry_id, review_hashes[entry_id]) for entry_id in entry_ids
        if entry_id in review_hashes))
    if payload.get("selected_entry_ids") != entry_ids:
        errors.append(label + " operator signoff selected entries differ")
    if payload.get("review_digests") != expected_reviews:
        errors.append(label + " operator signoff review digests differ")
    expected_artifacts = _operator_artifact_digests(selected, review_hashes)
    if payload.get("artifact_digests") != expected_artifacts:
        errors.append(label + " operator signoff artifact digests differ")
    elif any(not _is_nonzero_sha256(digest) for values in expected_artifacts.values()
             for digest in values.values()):
        errors.append(label + " operator signoff requires every exact artifact digest")
    if (payload.get("decision") != "approve"
            or payload.get("signer_principal") != OPERATOR_SIGNOFF_PRINCIPAL
            or not isinstance(payload.get("notes"), str) or not payload["notes"].strip()):
        errors.append(label + " operator cryptographic signoff must explicitly approve")
    try:
        signed_at = date.fromisoformat(payload.get("signed_at", ""))
        if signed_at > date.today():
            errors.append(label + " operator signoff date cannot be in the future")
    except (TypeError, ValueError):
        errors.append(label + " operator signoff date must be a real ISO date")
    git_context = payload.get("git_context")
    oid = re.compile(r"[0-9a-f]{40}")
    if (not isinstance(git_context, dict)
            or set(git_context) != {"commit_sha", "tag_name", "tag_object_sha"}
            or not oid.fullmatch(git_context.get("commit_sha", ""))
            or not oid.fullmatch(git_context.get("tag_object_sha", ""))
            or not isinstance(git_context.get("tag_name"), str)
            or not re.fullmatch(r"v4\.2-[A-Za-z0-9._-]+", git_context["tag_name"])):
        errors.append(label + " operator signoff git context is invalid")
    else:
        commands = (
            (["git", "-C", root, "rev-parse", "refs/tags/%s^{tag}" % git_context["tag_name"]],
             git_context["tag_object_sha"], "tag object"),
            (["git", "-C", root, "rev-parse", "%s^{commit}" % git_context["tag_object_sha"]],
             git_context["commit_sha"], "tag commit"),
        )
        for command, expected, description in commands:
            result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                    text=True, check=False)
            if result.returncode or result.stdout.strip() != expected:
                errors.append(label + " operator signoff %s does not match repository" % description)
        verify_tag = subprocess.run(
            ["git", "-C", root, "-c", "gpg.ssh.allowedSignersFile=" +
             OPERATOR_SIGNOFF_ALLOWED_SIGNERS, "verify-tag", "--raw",
             git_context["tag_object_sha"]],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)
        if verify_tag.returncode:
            errors.append(label + " operator signoff git tag signature is not verified")
    allowed_signers = _absolute(root, OPERATOR_SIGNOFF_ALLOWED_SIGNERS)
    verify = subprocess.run(
        ["ssh-keygen", "-Y", "verify", "-f", allowed_signers,
         "-I", OPERATOR_SIGNOFF_PRINCIPAL, "-n", OPERATOR_SIGNOFF_NAMESPACE,
         "-s", signature_path], input=canonical_bytes(payload),
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)
    if verify.returncode:
        errors.append(label + " operator signoff SSH signature is not verified")
    return errors


def manifest_sha256(manifest):
    """Hash the frozen pre-review campaign, excluding post-review gate outputs."""
    value = dict(manifest)
    value.pop("manifest_sha256", None)
    value.pop(DEVELOPMENT_GATE_KEY, None)
    value.pop("holdout_gate", None)
    return value_sha256(value)


def campaign_binding_sha256(manifest):
    """Hash pre-review campaign content without circular gate-output references."""
    return manifest_sha256(manifest)


def review_binding_sha256(manifest, entry):
    """Bind one review to immutable campaign context and its exact entry.

    This remains stable when a rejected attempt 1 later gains an attempt 2, while
    avoiding a caller-supplied historical-manifest escape hatch.
    """
    context_keys = (
        "manifest_version", "campaign_id", "scope", "toolchain", "membership",
        "partial_authorization", "full_gate_certificates", "freeze", "authorization",
    )
    context = {key: manifest[key] for key in context_keys if key in manifest}
    return value_sha256({"campaign_context": context, "entry": entry})


def membership_sha256(membership):
    value = dict(membership)
    value.pop("snapshot_sha256", None)
    return value_sha256(value)


def _codes_from_source(ref, root):
    value = load_json(_absolute(root, ref["path"]))
    rows = value.get("codes", value) if isinstance(value, dict) else value
    result = []
    for row in rows:
        result.append(row["naics"] if isinstance(row, dict) else row)
    return sorted(result)


def _issuance_errors(manifest, root):
    errors = []
    plan_ref = manifest.get("issuance_plan")
    errors.extend(_ref_errors("issuance plan", plan_ref, root))
    if errors:
        return errors
    plan, plan_errors = issuer.validate_issued_plan(root, plan_ref["path"], manifest.get("scope"))
    errors.extend(plan_errors)
    if not isinstance(plan, dict) or not plan:
        return errors or ["issuance plan validation returned no plan"]
    if plan_ref.get("sha256") != sha256(_absolute(root, plan_ref["path"])):
        errors.append("issuance plan reference digest is stale")
    if manifest.get("campaign_id") != plan.get("campaign_id"):
        errors.append("issuance plan campaign_id differs from campaign manifest")
    if manifest.get("freeze") != plan.get("freeze"):
        errors.append("campaign freeze binding differs from issuance plan")
    if manifest.get("authorization") != plan.get("authorization"):
        errors.append("campaign authorization binding differs from issuance plan")
    freeze = plan.get("freeze", {})
    if (not isinstance(freeze, dict) or not _is_nonzero_sha256(freeze.get("root_sha256"))
            or not _is_nonzero_sha256(freeze.get("sha256"))
            or not _is_nonzero_sha256(freeze.get("git_commit"))):
        errors.append("issuance plan lacks exact nonzero freeze root/manifest/commit bindings")
    authorization = plan.get("authorization", {})
    if not isinstance(authorization, dict):
        errors.append("issuance plan authorization must be an object")
    else:
        for key in ("contract", "commit_receipt", "tag_receipt", "ci_receipt"):
            ref = authorization.get(key)
            if not isinstance(ref, dict) or not {"path", "sha256"} <= set(ref):
                errors.append("issuance plan authorization %s reference is missing" % key)
    expected_codes = sorted(
        manifest.get("membership", {}).get("fleet_expected", [])
        + manifest.get("membership", {}).get("golden_expected", []))
    if plan.get("membership", {}).get("codes") != expected_codes:
        errors.append("issuance plan membership differs from campaign membership")
    plan_toolchain = plan.get("toolchain", {})
    for key, ref in manifest.get("toolchain", {}).items():
        planned_ref = plan_toolchain.get(key)
        if not isinstance(planned_ref, dict) or any(planned_ref.get(field) != ref.get(field)
                                                    for field in ("path", "sha256")):
            errors.append("issuance plan toolchain %s differs from campaign" % key)
    plan_entries = {item.get("entry_id"): item for item in plan.get("entries", [])
                    if isinstance(item, dict)}
    if len(plan_entries) != len(plan.get("entries", [])):
        errors.append("issuance plan entry identities must be unique")
    manifest_entries = manifest.get("entries", [])
    if set(plan_entries) != {item.get("entry_id") for item in manifest_entries if isinstance(item, dict)}:
        errors.append("campaign entries must exactly equal issued plan entries")
    for entry in manifest_entries:
        planned = plan_entries.get(entry.get("entry_id"))
        if not isinstance(planned, dict):
            continue
        if entry.get("issuance_entry_sha256") != value_sha256(planned):
            errors.append("%s issuance entry binding is stale" % entry.get("entry_id"))
        for key in ("kind", "naics", "run_id", "attempt"):
            if planned.get(key) != entry.get(key):
                errors.append("%s issued %s differs" % (entry.get("entry_id"), key))
        frozen_inputs = planned.get("frozen_inputs", {})
        for planned_key, artifact_key in (("assembled_prompt", "assembled_prompt"),
                                          ("industry_spec", "industry_spec"),
                                          ("dataset", "dataset")):
            planned_ref = frozen_inputs.get(planned_key, {})
            actual_ref = entry.get("artifacts", {}).get(artifact_key, {})
            if any(planned_ref.get(field) != actual_ref.get(field) for field in ("path", "sha256")):
                errors.append("%s issued frozen %s differs" % (entry.get("entry_id"), planned_key))
        envelope_ref = planned.get("execution_envelope", {})
        actual_envelope = entry.get("artifacts", {}).get("execution_envelope", {})
        if any(envelope_ref.get(field) != actual_envelope.get(field) for field in ("path", "sha256")):
            errors.append("%s execution envelope was not the issued envelope" % entry.get("entry_id"))
        outputs = planned.get("planned_outputs", {})
        expected_outputs = {
            "packet": entry.get("artifacts", {}).get("packet", {}).get("path"),
            "execution_envelope": actual_envelope.get("path"),
            "record": entry.get("artifacts", {}).get("record", {}).get("path"),
            "memo": entry.get("artifacts", {}).get("memo", {}).get("path"),
            "review": entry.get("review_path"),
        }
        if outputs != expected_outputs:
            errors.append("%s artifact paths differ from the issued plan" % entry.get("entry_id"))
    return errors


def _full_gate_certificate_errors(manifest, root):
    errors = []
    certificates = manifest.get("full_gate_certificates")
    if not isinstance(certificates, dict) or set(certificates) != {"regression_canary", "holdout"}:
        return ["full campaign requires exact regression_canary and holdout gate certificates"]
    expected = {
        "regression_canary": (DEVELOPMENT_SCOPE, sorted(CANARY_CODES)),
        "holdout": ("holdout", sorted(HOLDOUT_CODES)),
    }
    for name, (scope, codes) in expected.items():
        ref = certificates.get(name)
        ref_errors = _ref_errors("full %s gate certificate" % name, ref, root)
        errors.extend(ref_errors)
        if ref_errors:
            continue
        canonical = FULL_GATE_PATHS[name]
        if ref.get("path") != canonical["certificate"]:
            errors.append("full %s certificate must use canonical path %s" %
                          (name, canonical["certificate"]))
            continue
        certificate = load_json(_absolute(root, ref["path"]))
        required = {
            "certificate_version", "scope", "campaign_root_sha256", "gate_root_sha256",
            "accepted", "selected_codes", "issued_by_task_path", "codex_task_path", "issued_at",
            "campaign_artifact", "gate_artifact", "certificate_binding_sha256",
        }
        if not isinstance(certificate, dict) or set(certificate) != required:
            errors.append("full %s gate certificate must use the closed v4.1 contract" % name)
            continue
        if certificate.get("certificate_version") != GATE_CERTIFICATE_VERSION:
            errors.append("full %s gate certificate version is invalid" % name)
        binding_value = dict(certificate)
        binding_value.pop("certificate_binding_sha256", None)
        if certificate.get("certificate_binding_sha256") != value_sha256(binding_value):
            errors.append("full %s gate certificate binding is stale" % name)
        if (certificate.get("scope") != scope or certificate.get("accepted") is not True
                or certificate.get("selected_codes") != codes):
            errors.append("full %s gate certificate is not an exact accepted %s result" % (name, scope))
        if not _is_nonzero_sha256(certificate.get("campaign_root_sha256")):
            errors.append("full %s campaign root digest is invalid" % name)
        if not _is_nonzero_sha256(certificate.get("gate_root_sha256")):
            errors.append("full %s gate root digest is invalid" % name)
        for artifact_key, path_key in (("campaign_artifact", "campaign"), ("gate_artifact", "gate")):
            artifact_ref = certificate.get(artifact_key)
            artifact_errors = _ref_errors("full %s %s" % (name, artifact_key), artifact_ref, root)
            errors.extend(artifact_errors)
            if isinstance(artifact_ref, dict) and artifact_ref.get("path") != canonical[path_key]:
                errors.append("full %s %s must use canonical path %s" %
                              (name, artifact_key, canonical[path_key]))
        if errors and any(item.startswith("full %s " % name) for item in errors):
            continue
        campaign_proof = load_json(_absolute(root, certificate["campaign_artifact"]["path"]))
        campaign_required = {"proof_version", "scope", "source_manifest", "entries"}
        if not isinstance(campaign_proof, dict) or set(campaign_proof) != campaign_required:
            errors.append("full %s campaign proof must use the closed v4.1 contract" % name)
            continue
        if certificate.get("campaign_root_sha256") != value_sha256(campaign_proof):
            errors.append("full %s campaign root does not match the exact campaign artifact" % name)
        source_ref = campaign_proof.get("source_manifest")
        source_errors = _ref_errors("full %s source campaign" % name, source_ref, root)
        errors.extend(source_errors)
        if isinstance(source_ref, dict) and source_ref.get("path") != canonical["source"]:
            errors.append("full %s source campaign must use canonical path %s" %
                          (name, canonical["source"]))
        if source_errors:
            continue
        source_manifest = load_json(_absolute(root, source_ref["path"]))
        source_status, source_validation_errors = _certificate_source_status(source_manifest, root)
        if (source_validation_errors or source_manifest.get("scope") != scope
                or source_status.get("campaign_accepted") is not True):
            errors.append("full %s source campaign is not an exactly accepted campaign" % name)
            continue
        entries = campaign_proof.get("entries", [])
        entry_required = {
            "entry_id", "naics", "research_execution", "review_execution",
            "review_sha256", "outcome",
        }
        if (campaign_proof.get("proof_version") != GATE_CAMPAIGN_PROOF_VERSION
                or campaign_proof.get("scope") != scope or not isinstance(entries, list)
                or len(entries) != 5 or any(not isinstance(item, dict) or set(item) != entry_required
                                            for item in entries)):
            errors.append("full %s campaign proof is not an exact five-entry %s proof" % (name, scope))
            continue
        if sorted(item.get("naics") for item in entries) != codes:
            errors.append("full %s campaign proof selected codes differ" % name)
        source_entries = {item.get("entry_id"): item for item in source_manifest.get("entries", [])
                          if isinstance(item, dict)}
        if source_status.get("selected_entry_ids") != sorted(item["entry_id"] for item in entries):
            errors.append("full %s campaign proof selections differ from source campaign" % name)
        research_tasks, review_tasks = [], []
        for item in entries:
            errors.extend("full %s campaign proof: %s" % (name, error) for error in
                          _execution_errors(item.get("research_execution", {}), "research"))
            errors.extend("full %s campaign proof: %s" % (name, error) for error in
                          _execution_errors(item.get("review_execution", {}), "reviewer",
                                            item.get("research_execution", {})))
            research_tasks.append(item.get("research_execution", {}).get("codex_task_path"))
            review_tasks.append(item.get("review_execution", {}).get("codex_task_path"))
            if not _is_nonzero_sha256(item.get("review_sha256")) or item.get("outcome") not in PUBLISHABLE:
                errors.append("full %s campaign proof requires exact publishable review digests" % name)
            source_entry = source_entries.get(item["entry_id"], {})
            try:
                source_envelope = load_json(_absolute(
                    root, source_entry["artifacts"]["execution_envelope"]["path"]))
                source_review = load_json(_absolute(root, source_entry["review_path"]))
                source_review_sha = sha256(_absolute(root, source_entry["review_path"]))
            except (OSError, ValueError, TypeError, KeyError, json.JSONDecodeError):
                errors.append("full %s campaign proof cannot reopen exact source artifacts" % name)
            else:
                expected_research = {key: source_envelope.get(key) for key in
                                     ("issued_by_task_path", "codex_task_path", "fork_policy", "role")}
                if (item["naics"] != source_entry.get("naics")
                        or item["research_execution"] != expected_research
                        or item["review_execution"] != source_review.get("execution")
                        or item["review_sha256"] != source_review_sha
                        or item["outcome"] != source_review.get("outcome")):
                    errors.append("full %s campaign proof differs from exact source artifacts" % name)
        if (len(set(research_tasks)) != 5 or len(set(review_tasks)) != 5
                or set(research_tasks) & set(review_tasks)):
            errors.append("full %s campaign proof executions are not globally independent" % name)

        gate_proof = load_json(_absolute(root, certificate["gate_artifact"]["path"]))
        operator_contract = MANIFEST_VERSION == "review-campaign-4.2"
        signoff_field = "operator_signoff" if operator_contract else "signoff"
        report_field = "sentinel_gate_report" if operator_contract else "invariant_checks"
        gate_required = {
            "proof_version", "scope", "campaign_root_sha256", "accepted", "selected_entry_ids",
            "review_digests", report_field, signoff_field,
        }
        if not isinstance(gate_proof, dict) or set(gate_proof) != gate_required:
            errors.append("full %s gate proof must use the closed v4.1 contract" % name)
            continue
        if certificate.get("gate_root_sha256") != value_sha256(gate_proof):
            errors.append("full %s gate root does not match the exact gate artifact" % name)
        entry_ids = sorted(item["entry_id"] for item in entries)
        review_digests = dict(sorted((item["entry_id"], item["review_sha256"]) for item in entries))
        if (gate_proof.get("proof_version") != GATE_PROOF_VERSION
                or gate_proof.get("scope") != scope
                or gate_proof.get("campaign_root_sha256") != value_sha256(campaign_proof)
                or gate_proof.get("accepted") is not True
                or gate_proof.get("selected_entry_ids") != entry_ids
                or gate_proof.get("review_digests") != review_digests
                or gate_proof.get("review_digests") != source_status.get("review_digests")
                or (not operator_contract and (
                    set(gate_proof.get("invariant_checks", {})) != INVARIANT_CHECKS
                    or not all(value is True for value in
                               gate_proof.get("invariant_checks", {}).values())))):
            errors.append("full %s gate proof does not exactly accept the campaign and reviews" % name)
        if operator_contract:
            source_gate = source_manifest.get(
                DEVELOPMENT_GATE_KEY if scope == DEVELOPMENT_SCOPE else "holdout_gate", {})
            if gate_proof.get("operator_signoff") != source_gate.get("operator_signoff"):
                errors.append("full %s gate proof operator signoff differs from source" % name)
            if gate_proof.get("sentinel_gate_report") != source_gate.get("sentinel_gate_report"):
                errors.append("full %s gate proof sentinel report differs from source" % name)
            selected_source = [source_entries[entry_id] for entry_id in entry_ids
                               if entry_id in source_entries]
            errors.extend(
                "full %s gate proof: %s" % (name, item)
                for item in _operator_signoff_errors(
                    source_manifest, selected_source, source_status.get("review_digests", {}),
                    root, source_gate, name))
            signoff = None
        else:
            signoff = gate_proof.get("signoff", {})
        signoff_required = {
            "decision", "reviewer_identity", "signed_at", "notes", "selected_entry_ids",
            "review_digests", "signoff_execution", "commit_sha256",
        }
        identity = signoff.get("reviewer_identity") if isinstance(signoff, dict) else None
        execution = signoff.get("signoff_execution", {}) if isinstance(signoff, dict) else {}
        if (not operator_contract and (not isinstance(signoff, dict) or set(signoff) != signoff_required
                or signoff.get("decision") != "approve"
                or not isinstance(identity, str) or "@" not in identity or len(identity) < 6
                or not signoff.get("notes") or signoff.get("selected_entry_ids") != entry_ids
                or signoff.get("review_digests") != review_digests
                or not _is_nonzero_sha256(signoff.get("commit_sha256"))
                or not isinstance(execution, dict)
                or set(execution) != {"issued_by_task_path", "codex_task_path", "role"}
                or execution.get("issued_by_task_path") != "/root"
                or execution.get("role") != "human_signoff"
                or not isinstance(execution.get("codex_task_path"), str)
                or not execution["codex_task_path"].startswith("/root/")
                or execution["codex_task_path"] == "/root/"
                or execution["codex_task_path"] in set(research_tasks + review_tasks))):
            errors.append("full %s gate proof lacks an exact independent human signoff" % name)
        if not operator_contract:
            try:
                if date.fromisoformat(signoff.get("signed_at", "")) > date.today():
                    errors.append("full %s gate proof signoff date cannot be in the future" % name)
            except (TypeError, ValueError):
                errors.append("full %s gate proof signoff date must be a real ISO date" % name)
        execution = {
            "issued_by_task_path": certificate.get("issued_by_task_path"),
            "codex_task_path": certificate.get("codex_task_path"),
            "fork_policy": "none", "role": "gate_certificate",
        }
        if execution["issued_by_task_path"] != "/root":
            errors.append("full %s gate certificate must be root-issued" % name)
        task_path = execution["codex_task_path"]
        if not isinstance(task_path, str) or not task_path.startswith("/root/") or task_path == "/root/":
            errors.append("full %s gate certificate requires a child task path" % name)
        try:
            issued_at = date.fromisoformat(certificate.get("issued_at", ""))
            if issued_at > date.today():
                errors.append("full %s gate certificate date cannot be in the future" % name)
        except (TypeError, ValueError):
            errors.append("full %s gate certificate date must be a real ISO date" % name)
    return errors


def _selection(record, path):
    node = record
    for part in path.split("."):
        node = node[part]
    return node


def build_input_registry(record, industry_spec=None):
    rows = []
    for path, driving_class, bounds in BASE_INPUTS:
        selection = _selection(record, path)
        rows.append({
            "input_path": path,
            "driving_class": driving_class,
            "source_ids": sorted(set(selection.get("source_ids", []))),
            "required_bounds": list(bounds),
        })
    roles = record["inputs"]["target_role_mix"].get("roles", [])
    spec_roles = {
        item.get("role_id"): item for item in
        (industry_spec or {}).get("value_basis", {}).get("roles", [])
    }
    def role_id(role):
        return role.get("role_id", role.get("role"))
    for role in sorted(roles, key=role_id):
        selection = role["removable_fraction"]
        name = role_id(role)
        rows.append({
            "input_path": "inputs.target_role_mix.roles[role_id=%s].cost_weight" % name,
            "driving_class": "score",
            "source_ids": sorted(set(spec_roles.get(name, {}).get("source_ids", []))),
            "required_bounds": ["frozen"],
        })
        rows.append({
            "input_path": "inputs.target_role_mix.roles[role_id=%s].removable_fraction" % name,
            "driving_class": "score",
            "source_ids": sorted(set(selection.get("source_ids", []))),
            "required_bounds": ["low", "base", "high"],
        })
    archetype = (industry_spec or {}).get("target_archetype", {})
    alternatives = archetype.get("alternatives", [])
    for alternative in sorted(alternatives, key=lambda item: item.get("id", "")):
        name = alternative.get("id")
        rows.append({
            "input_path": "industry_spec.target_archetype.alternatives[id=%s].band_count" % name,
            "driving_class": "gate",
            "source_ids": sorted(set(alternative.get("source_ids", []))),
            "required_bounds": ["low", "base", "high"],
        })
    if alternatives:
        selected = next((item for item in alternatives
                         if item.get("id") == archetype.get("selected_id")), {})
        all_sources = sorted({source_id for item in alternatives
                              for source_id in item.get("source_ids", [])})
        rows.extend((
            {
                "input_path": "industry_spec.target_archetype.selected_id",
                "driving_class": "gate",
                "source_ids": sorted(set(selected.get("source_ids", []))),
                "required_bounds": ["frozen"],
            },
            {
                "input_path": "industry_spec.target_archetype.enumeration_coverage",
                "driving_class": "gate",
                "source_ids": all_sources,
                "required_bounds": ["low", "base", "high"],
            },
            {
                "input_path": "industry_spec.target_archetype.residual.band_count",
                "driving_class": "gate",
                "source_ids": [],
                "required_bounds": ["low", "base", "high"],
            },
        ))
    return sorted(rows, key=lambda item: item["input_path"])


def build_source_registry(record, input_registry=None, industry_spec=None):
    input_registry = input_registry or build_input_registry(record)
    uses = {}
    classes = {}
    for item in input_registry:
        for source_id in item["source_ids"]:
            uses.setdefault(source_id, set()).add(item["input_path"])
            classes.setdefault(source_id, set()).add(item["driving_class"])
    rows = []
    sources = list(record.get("sources", []))
    if industry_spec:
        sources.extend(industry_spec.get("target_archetype", {}).get("sources", []))
        sources.extend(industry_spec.get("value_basis", {}).get("sources", []))
    for source in sources:
        source_id = source["id"]
        driving_classes = sorted(classes.get(source_id, {"context"}))
        rows.append({
            "source_id": source_id,
            "url": source["url"],
            "input_paths": sorted(uses.get(source_id, set())),
            "driving_classes": driving_classes,
            "score_driving": bool(set(driving_classes) & {"score", "readiness", "gate"}),
        })
    return sorted(rows, key=lambda item: item["source_id"])


def declared_caveats(record, industry_spec=None):
    caveats = []
    for row in build_input_registry(record):
        path = row["input_path"]
        if path.startswith("industry_spec."):
            continue
        if path.endswith(".cost_weight"):
            continue
        if ".roles[role_id=" in path:
            role_name = path.split("[role_id=", 1)[1].split("]", 1)[0]
            role = next(item for item in record["inputs"]["target_role_mix"]["roles"]
                        if item.get("role_id", item.get("role")) == role_name)
            selection = role["removable_fraction"]
        else:
            selection = _selection(record, path)
        for caveat in selection.get("caveats", []):
            caveats.append("%s: %s" % (path, caveat))
    for caveat in record["inputs"]["target_role_mix"].get("caveats", []):
        caveats.append("inputs.target_role_mix: %s" % caveat)
    for caveat in (industry_spec or {}).get("value_basis", {}).get("caveats", []):
        caveats.append("industry_spec.value_basis: %s" % caveat)
    return list(dict.fromkeys(caveats))


def artifact_digests(entry):
    return {key + "_sha256": entry["artifacts"][key]["sha256"] for key in ARTIFACT_KEYS}


def toolchain_digests(manifest):
    return {key: manifest["toolchain"][key]["sha256"] for key in TOOLCHAIN_KEYS}


def finding_fingerprint(finding):
    return value_sha256({
        "defect_rule_id": finding.get("defect_rule_id"),
        "category": finding.get("category"),
        "input_paths": sorted(finding.get("input_paths", [])),
    })


def _execution_errors(execution, role, research_execution=None):
    errors = []
    if execution.get("issued_by_task_path") != "/root":
        errors.append("%s execution must be root-issued" % role)
    task_path = execution.get("codex_task_path")
    if not isinstance(task_path, str) or not task_path.startswith("/root/") or task_path == "/root/":
        errors.append("%s execution requires a non-root Codex task path" % role)
    if execution.get("role") != role:
        errors.append("execution role must be %s" % role)
    if execution.get("fork_policy") not in ("none", "isolated"):
        errors.append("%s execution fork policy is not isolated" % role)
    if research_execution and task_path == research_execution.get("codex_task_path"):
        errors.append("research and reviewer executions must differ")
    return errors


def _extra_record_errors(_record):
    """Version-specific deterministic record checks; v4.1 has no extra hook."""
    return []


def _entry_errors(entry, manifest, root):
    if not isinstance(entry, dict):
        return ["entry must be an object"]
    errors = []
    expected_entry_id = "%s:%s:%s" % (entry.get("kind"), entry.get("naics"), entry.get("run_id"))
    if entry.get("entry_id") != expected_entry_id:
        errors.append("entry_id mismatch")
    if entry.get("kind") not in ("fleet", "golden"):
        errors.append("entry kind must be fleet or golden")
    if entry.get("attempt") not in (1, 2):
        errors.append("attempt must be 1 or 2")
    if not _is_nonzero_sha256(entry.get("issuance_entry_sha256")):
        errors.append("entry requires an exact issued-plan binding")
    if "review_manifest_sha256" in entry:
        errors.append("review manifest binding is derived and may not be caller-supplied")
    if set(entry.get("artifacts", {})) != set(ARTIFACT_KEYS):
        errors.append("artifact registry must contain exactly %s" % (ARTIFACT_KEYS,))
        return errors
    for key in ARTIFACT_KEYS:
        errors.extend(_ref_errors("%s %s" % (entry.get("entry_id"), key), entry["artifacts"][key], root))
    if errors:
        return errors
    try:
        packet = load_json(_absolute(root, entry["artifacts"]["packet"]["path"]))
        record = load_json(_absolute(root, entry["artifacts"]["record"]["path"]))
        dataset = load_json(_absolute(root, entry["artifacts"]["dataset"]["path"]))
        industry_spec = load_json(_absolute(root, entry["artifacts"]["industry_spec"]["path"]))
        execution_envelope = load_json(_absolute(root, entry["artifacts"]["execution_envelope"]["path"]))
    except (OSError, ValueError, TypeError, json.JSONDecodeError) as exc:
        return errors + ["entry JSON load failed: %s" % exc]
    for label, value in (("packet", packet), ("record", record), ("dataset", dataset)):
        if value.get("naics") != entry.get("naics"):
            errors.append("%s NAICS mismatch" % label)
    errors.extend(_extra_record_errors(record))
    if record.get("run_meta", {}).get("run_id") != entry.get("run_id"):
        errors.append("record run ID mismatch")
    if record.get("run_meta", {}).get("attempt") != entry.get("attempt"):
        errors.append("record attempt mismatch")
    expected_model = "gpt-5.6-terra" if entry.get("kind") == "fleet" else "gpt-5.6-sol"
    if execution_envelope.get("kind") != entry.get("kind"):
        errors.append("execution envelope kind mismatch")
    if execution_envelope.get("naics") != entry.get("naics") or execution_envelope.get("run_id") != entry.get("run_id"):
        errors.append("execution envelope identity mismatch")
    if execution_envelope.get("attempt") != entry.get("attempt"):
        errors.append("execution envelope attempt mismatch")
    if execution_envelope.get("model_id") != expected_model:
        errors.append("execution envelope model route mismatch")
    errors.extend(_execution_errors(execution_envelope, "research"))
    if execution_envelope.get("fork_policy") != "none":
        errors.append("research execution envelope fork_policy must be none")
    envelope_bindings = {
        "prompt_sha256": entry["artifacts"]["assembled_prompt"]["sha256"],
        "dataset_sha256": entry["artifacts"]["dataset"]["sha256"],
        "spec_sha256": entry["artifacts"]["industry_spec"]["sha256"],
        "methodology_sha256": manifest["toolchain"]["methodology"]["sha256"],
        "thresholds_sha256": manifest["toolchain"]["thresholds"]["sha256"],
        "research_packet_schema_sha256": manifest["toolchain"]["packet_schema"]["sha256"],
        "dataset_schema_sha256": manifest["toolchain"]["dataset_schema"]["sha256"],
        "industry_spec_schema_sha256": manifest["toolchain"]["industry_spec_schema"]["sha256"],
        "run_record_schema_sha256": manifest["toolchain"]["run_schema"]["sha256"],
        "scoring_sha256": manifest["toolchain"]["scoring"]["sha256"],
        "finalizer_sha256": manifest["toolchain"]["finalizer"]["sha256"],
    }
    for key, digest in envelope_bindings.items():
        if execution_envelope.get(key) != digest:
            errors.append("execution envelope %s differs from frozen manifest" % key)
    provenance = record.get("artifact_provenance", {})
    if provenance.get("execution_envelope") != execution_envelope:
        errors.append("record execution-envelope content differs from manifest artifact")
    if provenance.get("execution_envelope_sha256") != entry["artifacts"]["execution_envelope"]["sha256"]:
        errors.append("record execution-envelope provenance differs from manifest")
    if provenance.get("packet_sha256") != entry["artifacts"]["packet"]["sha256"]:
        errors.append("record packet provenance differs from manifest")
    run_meta = record.get("run_meta", {})
    for key in ("model_id", "issued_by_task_path", "codex_task_path", "fork_policy"):
        if run_meta.get(key) != execution_envelope.get(key):
            errors.append("record %s differs from execution envelope" % key)
    if entry.get("attempt") == 2:
        errors.extend(_ref_errors("%s remediation bundle" % entry.get("entry_id"),
                                  entry.get("remediation_bundle"), root))
    expected_inputs = build_input_registry(record, industry_spec)
    input_paths = [item["input_path"] for item in expected_inputs]
    if len(input_paths) != len(set(input_paths)):
        errors.append("finalized record produces duplicate input registry paths")
    if entry.get("input_registry") != expected_inputs:
        errors.append("input registry differs from finalized record")
    expected_sources = build_source_registry(record, expected_inputs, industry_spec)
    source_ids = [item["source_id"] for item in expected_sources]
    if len(source_ids) != len(set(source_ids)):
        errors.append("finalized artifacts produce duplicate source registry identities")
    if entry.get("source_registry") != expected_sources:
        errors.append("source registry differs from finalized record")
    if entry.get("authored_caveats") != declared_caveats(record, industry_spec):
        errors.append("authored caveat registry differs from finalized record")
    return errors


def _membership_errors(manifest, root):
    errors = []
    scope = manifest.get("scope")
    membership = manifest.get("membership", {})
    if not isinstance(membership, dict):
        return ["membership must be an object"]
    if scope not in (DEVELOPMENT_SCOPE, "holdout", "full", "partial"):
        return ["scope must be %s, holdout, full, or partial" % DEVELOPMENT_SCOPE]
    if membership.get("snapshot_sha256") != membership_sha256(membership):
        errors.append("membership snapshot digest is stale")
    for key in ("fleet_universe", "golden_universe"):
        errors.extend(_ref_errors("membership %s" % key, membership.get(key), root))
        if isinstance(membership.get(key), dict) and membership[key].get("path") != MEMBERSHIP_PATHS[key]:
            errors.append("membership %s must use canonical path %s" % (key, MEMBERSHIP_PATHS[key]))
    for key in ("fleet_expected", "golden_expected", "fleet_omitted", "golden_omitted"):
        value = membership.get(key)
        if not isinstance(value, list) or value != sorted(set(value)):
            errors.append("membership %s must be a sorted unique list" % key)
    if errors:
        return errors
    fleet_universe = _codes_from_source(membership["fleet_universe"], root)
    golden_universe = _codes_from_source(membership["golden_universe"], root)
    fleet, golden = membership["fleet_expected"], membership["golden_expected"]
    omitted_fleet, omitted_golden = membership["fleet_omitted"], membership["golden_omitted"]
    if scope == DEVELOPMENT_SCOPE:
        if fleet != sorted(CANARY_CODES) or golden or omitted_fleet or omitted_golden:
            errors.append("canary membership must be exactly the five preregistered fleet codes")
        if "holdout_membership" in membership:
            errors.append("canary membership may not carry holdout membership")
    elif scope == "holdout":
        ref = membership.get("holdout_membership")
        errors.extend(_ref_errors("holdout membership", ref, root))
        if isinstance(ref, dict) and ref.get("path") != HOLDOUT_MEMBERSHIP_PATH:
            errors.append("holdout membership must use canonical path %s" % HOLDOUT_MEMBERSHIP_PATH)
        if isinstance(ref, dict) and ref.get("sha256") != HOLDOUT_MEMBERSHIP_SHA256:
            errors.append("holdout membership digest differs from the frozen section-12 selection")
        if not errors:
            holdout = load_json(_absolute(root, ref["path"]))
            codes = holdout.get("selected_codes") if isinstance(holdout, dict) else None
            if (not isinstance(codes, list) or len(codes) != 5 or len(codes) != len(set(codes))
                    or any(not isinstance(code, str) for code in codes)):
                errors.append("holdout membership must contain exactly five unique selected codes")
            elif sorted(codes) != sorted(HOLDOUT_CODES):
                errors.append("holdout membership selected codes differ from the frozen section-12 selection")
            elif fleet != sorted(codes) or golden or omitted_fleet or omitted_golden:
                errors.append("holdout campaign membership must exactly equal frozen selected_codes")
    elif scope == "full":
        if "holdout_membership" in membership:
            errors.append("full membership may not be conflated with holdout membership")
        if fleet != fleet_universe or golden != golden_universe or omitted_fleet or omitted_golden:
            errors.append("full membership must equal both frozen universes with no omissions")
        errors.extend(_full_gate_certificate_errors(manifest, root))
    else:
        if "holdout_membership" in membership:
            errors.append("partial membership may not be conflated with holdout membership")
        authorization = manifest.get("partial_authorization")
        if not isinstance(authorization, dict) or set(authorization) != {"approved_by", "approved_at", "reason"}:
            errors.append("partial membership requires closed approved_by/approved_at/reason authorization")
        else:
            if not all(isinstance(authorization[key], str) and authorization[key].strip()
                       for key in ("approved_by", "approved_at", "reason")):
                errors.append("partial authorization fields must be non-empty strings")
            try:
                date.fromisoformat(authorization["approved_at"])
            except (TypeError, ValueError):
                errors.append("partial authorization approved_at must be a real ISO date")
        if sorted(fleet + omitted_fleet) != fleet_universe or set(fleet) & set(omitted_fleet):
            errors.append("partial fleet membership and omissions must partition the universe")
        if sorted(golden + omitted_golden) != golden_universe or set(golden) & set(omitted_golden):
            errors.append("partial golden membership and omissions must partition the universe")
    return errors


def freeze_manifest(campaign_id, scope, entries, root=REPO, fleet_expected=None,
                    golden_expected=None, partial_authorization=None, full_gate_certificates=None,
                    issuance_plan_path=None):
    """Create a frozen manifest from already-written exact v4.1 entry artifacts."""
    if scope not in (DEVELOPMENT_SCOPE, "holdout", "full", "partial"):
        raise ValueError("scope must be %s, holdout, full, or partial" % DEVELOPMENT_SCOPE)
    if not issuance_plan_path:
        raise ValueError("issuance_plan_path is required; campaign entries may not be self-issued")
    plan, plan_errors = issuer.validate_issued_plan(root, issuance_plan_path, scope)
    if plan_errors:
        raise ValueError("cannot bind invalid issuance plan: " + "; ".join(plan_errors))
    plan_entries = {item["entry_id"]: item for item in plan.get("entries", [])}
    entries = copy.deepcopy(entries)
    if set(plan_entries) != {item.get("entry_id") for item in entries}:
        raise ValueError("campaign entries must exactly equal issued plan entries")
    for entry in entries:
        entry["issuance_entry_sha256"] = value_sha256(plan_entries[entry["entry_id"]])
    toolchain = {key: artifact_ref(TOOLCHAIN_PATHS[key], root) for key in TOOLCHAIN_KEYS}
    universe_refs = {key: artifact_ref(path, root) for key, path in MEMBERSHIP_PATHS.items()}
    fleet_universe = _codes_from_source(universe_refs["fleet_universe"], root)
    golden_universe = _codes_from_source(universe_refs["golden_universe"], root)
    if scope == DEVELOPMENT_SCOPE:
        fleet, golden, fleet_omitted, golden_omitted = sorted(CANARY_CODES), [], [], []
    elif scope == "holdout":
        holdout_ref = artifact_ref(HOLDOUT_MEMBERSHIP_PATH, root)
        holdout = load_json(_absolute(root, HOLDOUT_MEMBERSHIP_PATH))
        fleet = sorted(holdout.get("selected_codes", []))
        golden, fleet_omitted, golden_omitted = [], [], []
    elif scope == "full":
        fleet, golden, fleet_omitted, golden_omitted = fleet_universe, golden_universe, [], []
    else:
        fleet = sorted(set(fleet_expected or []))
        golden = sorted(set(golden_expected or []))
        fleet_omitted = sorted(set(fleet_universe) - set(fleet))
        golden_omitted = sorted(set(golden_universe) - set(golden))
    membership = {
        **universe_refs,
        "fleet_expected": fleet, "golden_expected": golden,
        "fleet_omitted": fleet_omitted, "golden_omitted": golden_omitted,
    }
    if scope == "holdout":
        membership["holdout_membership"] = holdout_ref
    membership["snapshot_sha256"] = membership_sha256(membership)
    manifest = {
        "manifest_version": MANIFEST_VERSION, "campaign_id": campaign_id, "scope": scope,
        "toolchain": toolchain, "membership": membership,
        "entries": sorted(entries, key=lambda item: (item["kind"], item["naics"], item["attempt"], item["run_id"])),
        "issuance_plan": artifact_ref(issuance_plan_path, root),
        "freeze": copy.deepcopy(plan["freeze"]),
        "authorization": copy.deepcopy(plan["authorization"]),
    }
    if scope == "partial":
        manifest["partial_authorization"] = partial_authorization
    if scope == "full":
        manifest["full_gate_certificates"] = full_gate_certificates
    manifest["manifest_sha256"] = manifest_sha256(manifest)
    errors = validate_manifest(manifest, root)
    if errors:
        raise ValueError("cannot freeze invalid v4.1 manifest: " + "; ".join(errors))
    return manifest


def validate_manifest(manifest, root=REPO):
    if not isinstance(manifest, dict):
        return ["manifest must be an object"]
    errors = []
    if manifest.get("manifest_version") != MANIFEST_VERSION:
        errors.append("manifest_version must be %s" % MANIFEST_VERSION)
    for key in ("issuance_plan", "freeze", "authorization"):
        if key not in manifest:
            errors.append("campaign manifest requires %s binding" % key)
    if manifest.get("manifest_sha256") != manifest_sha256(manifest):
        errors.append("manifest digest is stale")
    if set(manifest.get("toolchain", {})) != set(TOOLCHAIN_KEYS):
        errors.append("toolchain must contain exactly %s" % (TOOLCHAIN_KEYS,))
    else:
        for key in TOOLCHAIN_KEYS:
            errors.extend(_ref_errors("toolchain %s" % key, manifest["toolchain"][key], root))
            if manifest["toolchain"][key].get("path") != TOOLCHAIN_PATHS[key]:
                errors.append("toolchain %s must use canonical path %s" % (key, TOOLCHAIN_PATHS[key]))
    errors.extend(_membership_errors(manifest, root))
    entries = manifest.get("entries")
    if not isinstance(entries, list):
        return errors + ["entries must be an array"]
    identities = [item.get("entry_id") for item in entries if isinstance(item, dict)]
    if len(identities) != len(entries) or len(identities) != len(set(identities)):
        errors.append("entry identities must be unique")
    for entry in entries:
        label = entry.get("entry_id", "entry") if isinstance(entry, dict) else "entry"
        errors.extend("%s: %s" % (label, item) for item in _entry_errors(entry, manifest, root))
    errors.extend(_issuance_errors(manifest, root))
    if any(not isinstance(item, dict) for item in entries):
        return errors
    review_paths = [item.get("review_path") for item in entries]
    if len(review_paths) != len(set(review_paths)):
        errors.append("review paths must be unique per entry")
    for key in ("assembled_prompt", "packet", "execution_envelope", "record", "memo"):
        paths = [item.get("artifacts", {}).get(key, {}).get("path") for item in entries]
        if len(paths) != len(set(paths)):
            errors.append("%s artifact paths must be unique per entry" % key)
    membership = manifest.get("membership", {})
    expected = {("fleet", code) for code in membership.get("fleet_expected", [])}
    expected |= {("golden", code) for code in membership.get("golden_expected", [])}
    actual = {(item.get("kind"), item.get("naics")) for item in entries}
    if actual != expected:
        errors.append("entry membership differs from frozen expected membership")
    by_code = {}
    by_id = {item.get("entry_id"): item for item in entries}
    for entry in entries:
        by_code.setdefault((entry.get("kind"), entry.get("naics")), []).append(entry)
    for key, attempts in by_code.items():
        by_attempt = {}
        for entry in attempts:
            by_attempt.setdefault(entry.get("attempt"), []).append(entry)
        if set(by_attempt) - {1, 2} or len(by_attempt.get(1, [])) != 1 or len(by_attempt.get(2, [])) > 1:
            errors.append("%s/%s must have exactly one attempt 1 and at most one attempt 2" % key)
            continue
        first = by_attempt[1][0]
        if first.get("remediates_entry_id") is not None or first.get("predecessor_review_sha256") is not None:
            errors.append("%s attempt 1 may not declare remediation lineage" % first["entry_id"])
        if 2 in by_attempt:
            second = by_attempt[2][0]
            if second.get("remediates_entry_id") != first["entry_id"] or by_id.get(second.get("remediates_entry_id")) is not first:
                errors.append("%s attempt 2 must remediate its exact attempt 1" % second["entry_id"])
            if not _is_sha256(second.get("predecessor_review_sha256")):
                errors.append("%s attempt 2 requires predecessor review digest" % second["entry_id"])
            if not isinstance(second.get("remediation_bundle"), dict):
                errors.append("%s attempt 2 requires an exact remediation bundle" % second["entry_id"])
            try:
                envelope = load_json(_absolute(root, second["artifacts"]["execution_envelope"]["path"]))
            except (OSError, ValueError, TypeError, KeyError, json.JSONDecodeError) as exc:
                errors.append("%s cannot verify remediation envelope: %s" % (second["entry_id"], exc))
            else:
                if envelope.get("remediates_run_id") != first["run_id"]:
                    errors.append("%s execution envelope must remediate the predecessor run ID" % second["entry_id"])
    return errors


def _finding_maps(review):
    findings = [item for item in review.get("findings", []) if isinstance(item, dict)]
    by_input, by_source = {}, {}
    for finding in findings:
        for path in finding.get("input_paths", []):
            by_input.setdefault(path, []).append(finding)
        for source_id in finding.get("source_ids", []):
            by_source.setdefault(source_id, []).append(finding)
    return findings, by_input, by_source


def expected_caveats(entry, review):
    if not isinstance(review, dict):
        return list(entry.get("authored_caveats", []))
    result = list(entry.get("authored_caveats", []))
    for finding in review.get("findings", []):
        if not isinstance(finding, dict):
            continue
        if finding.get("severity") == "caveat":
            caveat = finding.get("publication_caveat")
            if caveat and caveat not in result:
                result.append(caveat)
    return result


def computed_outcome(entry, review):
    if not isinstance(review, dict):
        return "invalid"
    mechanics_ok = set(review.get("mechanics", {})) == set(MECHANICS_KEYS) and all(
        review["mechanics"].get(key) is True for key in MECHANICS_KEYS
    )
    severities = {item.get("severity") for item in review.get("findings", []) if isinstance(item, dict)}
    if not mechanics_ok or "fatal_mechanics" in severities:
        return "invalid"
    if "material" in severities:
        return "reject"
    source_by_id = {item.get("source_id"): item for item in review.get("source_reviews", []) if isinstance(item, dict)}
    for source in entry.get("source_registry", []):
        item = source_by_id.get(source["source_id"], {})
        if source["score_driving"] and (item.get("accessible") is not True or item.get("support") in ("unsupported", "not_score_driving")):
            return "reject"
    input_by_path = {item.get("input_path"): item for item in review.get("input_reviews", []) if isinstance(item, dict)}
    for input_item in entry.get("input_registry", []):
        item = input_by_path.get(input_item["input_path"], {})
        if any(item.get(key) is not True for key in INPUT_REVIEW_PASS_KEYS):
            return "reject"
    if expected_caveats(entry, review):
        return "publishable_with_caveats"
    return "publishable"


def review_errors(review, entry, manifest, root=REPO):
    schema = load_json(os.path.join(SCHEMAS, REVIEW_SCHEMA_FILENAME))
    errors = legacy_build.schema_errors(review, schema, schema)
    if not isinstance(review, dict):
        return errors + ["review must be an object"]
    if review.get("entry_id") != entry.get("entry_id"):
        errors.append("review entry identity mismatch")
    expected_review_manifest = review_binding_sha256(manifest, entry)
    if review.get("manifest_sha256") != expected_review_manifest:
        errors.append("review does not bind its frozen manifest revision")
    if review.get("artifact_digests") != artifact_digests(entry):
        errors.append("review artifact digests differ from manifest")
    if review.get("toolchain_digests") != toolchain_digests(manifest):
        errors.append("review toolchain digests differ from manifest")
    research_execution = {}
    research_run_date = None
    try:
        envelope = load_json(_absolute(root, entry["artifacts"]["execution_envelope"]["path"]))
        research_execution = envelope
        research_run_date = date.fromisoformat(envelope.get("run_date", ""))
    except (OSError, ValueError, TypeError, json.JSONDecodeError) as exc:
        errors.append("cannot load research execution envelope: %s" % exc)
    errors.extend(_execution_errors(review.get("execution", {}), "reviewer", research_execution))
    try:
        plan = load_json(_absolute(root, manifest["issuance_plan"]["path"]))
        planned_entry = next(item for item in plan.get("entries", [])
                             if item.get("entry_id") == entry.get("entry_id"))
        planned_review = planned_entry.get("review_execution", {})
        expected_execution = {key: planned_review.get(key) for key in
                              ("issued_by_task_path", "codex_task_path", "model_id",
                               "fork_policy", "role")}
        if review.get("execution") != expected_execution:
            errors.append("review execution differs from the issued review task")
    except (OSError, ValueError, TypeError, KeyError, StopIteration, json.JSONDecodeError) as exc:
        errors.append("cannot bind review to issued plan: %s" % exc)
    meta = review.get("review_meta", {})
    if meta.get("model_id") != "gpt-5.6-sol" or meta.get("prompt_version") != REVIEW_PROMPT_VERSION:
        errors.append("review model/prompt route mismatch")
    try:
        review_date = date.fromisoformat(meta.get("review_date", ""))
        if review_date > date.today():
            errors.append("review date cannot be in the future")
        if research_run_date and review_date < research_run_date:
            errors.append("review date cannot precede research run date")
    except (TypeError, ValueError):
        errors.append("review date must be a real ISO date")

    expected_sources = entry.get("source_registry", [])
    actual_sources = review.get("source_reviews", [])
    source_ids = [item.get("source_id") for item in actual_sources if isinstance(item, dict)]
    if len(source_ids) != len(actual_sources) or len(source_ids) != len(set(source_ids)):
        errors.append("source reviews must have unique source identities")
    actual_by_source = {item.get("source_id"): item for item in actual_sources if isinstance(item, dict)}
    if set(actual_by_source) != {item["source_id"] for item in expected_sources}:
        errors.append("source review coverage must exactly equal source registry")
    for source in expected_sources:
        item = actual_by_source.get(source["source_id"], {})
        for key in ("url", "score_driving"):
            if item.get(key) != source[key]:
                errors.append("source %s %s differs from registry" % (source["source_id"], key))
        if sorted(item.get("input_paths", [])) != source["input_paths"]:
            errors.append("source %s input paths differ from registry" % source["source_id"])
        if item.get("accessible") is False and item.get("support") == "supported":
            errors.append("inaccessible source %s cannot be supported" % source["source_id"])
        if item.get("support") == "not_score_driving" and source["score_driving"]:
            errors.append("score-driving source %s cannot be not_score_driving" % source["source_id"])

    expected_inputs = entry.get("input_registry", [])
    actual_inputs = review.get("input_reviews", [])
    input_paths = [item.get("input_path") for item in actual_inputs if isinstance(item, dict)]
    if len(input_paths) != len(actual_inputs) or len(input_paths) != len(set(input_paths)):
        errors.append("input reviews must have unique input paths")
    actual_by_input = {item.get("input_path"): item for item in actual_inputs if isinstance(item, dict)}
    if set(actual_by_input) != {item["input_path"] for item in expected_inputs}:
        errors.append("input review coverage must exactly equal input registry")
    for expected in expected_inputs:
        item = actual_by_input.get(expected["input_path"], {})
        if sorted(item.get("reviewed_bounds", [])) != sorted(expected["required_bounds"]):
            errors.append("input %s reviewed bounds differ from registry" % expected["input_path"])

    findings, by_input, by_source = _finding_maps(review)
    finding_ids = [item.get("finding_id") for item in findings]
    if len(finding_ids) != len(set(finding_ids)):
        errors.append("finding IDs must be unique")
    for finding in findings:
        if finding.get("fingerprint") != finding_fingerprint(finding):
            errors.append("finding %s fingerprint mismatch" % finding.get("finding_id"))
        if finding.get("severity") == "material" and not finding.get("causal_effect", "").strip():
            errors.append("material finding %s requires causal effect" % finding.get("finding_id"))
        if finding.get("severity") == "caveat" and not finding.get("publication_caveat"):
            errors.append("caveat finding %s requires publication_caveat" % finding.get("finding_id"))
        if finding.get("severity") != "caveat" and finding.get("publication_caveat"):
            errors.append("only caveat findings may set publication_caveat")
        if set(finding.get("input_paths", [])) - {item["input_path"] for item in expected_inputs}:
            errors.append("finding %s references unknown input" % finding.get("finding_id"))
        if set(finding.get("source_ids", [])) - {item["source_id"] for item in expected_sources}:
            errors.append("finding %s references unknown source" % finding.get("finding_id"))
    for source in expected_sources:
        item = actual_by_source.get(source["source_id"], {})
        requires_material = source["score_driving"] and (
            item.get("accessible") is not True or item.get("support") in ("unsupported", "not_score_driving")
        )
        if requires_material and not any(finding.get("severity") == "material" for finding in by_source.get(source["source_id"], [])):
            errors.append("unsupported score-driving source %s requires a material finding" % source["source_id"])
        if item.get("support") == "partially_supported" and not by_source.get(source["source_id"]):
            errors.append("partially supported source %s requires a linked finding" % source["source_id"])
    for expected in expected_inputs:
        item = actual_by_input.get(expected["input_path"], {})
        failed = any(item.get(key) is not True for key in INPUT_REVIEW_PASS_KEYS)
        if failed and not any(finding.get("severity") == "material" for finding in by_input.get(expected["input_path"], [])):
            errors.append("unsupported input %s requires a material finding" % expected["input_path"])

    caveats = expected_caveats(entry, review)
    if review.get("publication_caveats") != caveats:
        errors.append("publication caveats must equal exact authored/reviewer caveat union")
    expected_outcome = computed_outcome(entry, review)
    if review.get("outcome") != expected_outcome:
        errors.append("outcome must be computed as %s" % expected_outcome)
    return errors


def _review_path(entry, root):
    return _absolute(root, entry["review_path"])


def _input_value(record, industry_spec, path):
    if path.startswith("industry_spec.target_archetype.alternatives[id="):
        alternative_id = path.split("[id=", 1)[1].split("]", 1)[0]
        return next(item["band_count"] for item in industry_spec["target_archetype"]["alternatives"]
                    if item["id"] == alternative_id)
    if path == "industry_spec.target_archetype.selected_id":
        return industry_spec["target_archetype"]["selected_id"]
    if path == "industry_spec.target_archetype.enumeration_coverage":
        return industry_spec["target_archetype"]["enumeration_coverage"]
    if path == "industry_spec.target_archetype.residual.band_count":
        return industry_spec["target_archetype"]["residual"]["band_count"]
    if ".roles[role_id=" in path:
        role_id = path.split("[role_id=", 1)[1].split("]", 1)[0]
        role = next(item for item in record["inputs"]["target_role_mix"]["roles"]
                    if item.get("role_id", item.get("role")) == role_id)
        return role["cost_weight"] if path.endswith(".cost_weight") else role["removable_fraction"]
    return _selection(record, path)


def _remediation_semantic_errors(first, second, findings, root):
    errors = []
    linked_inputs = {path for finding in findings for path in finding.get("input_paths", [])}
    linked_sources = {source for finding in findings for source in finding.get("source_ids", [])}
    for source in first.get("source_registry", []):
        if source.get("source_id") in linked_sources:
            linked_inputs.update(source.get("input_paths", []))

    def load_artifacts(entry):
        return {
            key: load_json(_absolute(root, entry["artifacts"][key]["path"]))
            for key in ("packet", "dataset", "industry_spec", "record")
        }
    try:
        old, new = load_artifacts(first), load_artifacts(second)
    except (OSError, ValueError, TypeError, KeyError, json.JSONDecodeError) as exc:
        return ["cannot compare remediation semantics: %s" % exc]
    if old["dataset"] != new["dataset"]:
        errors.append("attempt 2 may not change the frozen dataset")

    old_rows = {item["input_path"]: item for item in first.get("input_registry", [])}
    new_rows = {item["input_path"]: item for item in second.get("input_registry", [])}
    for path in sorted(set(old_rows) | set(new_rows)):
        changed = old_rows.get(path) != new_rows.get(path)
        if not changed and path in old_rows and path in new_rows:
            try:
                changed = _input_value(old["record"], old["industry_spec"], path) != _input_value(
                    new["record"], new["industry_spec"], path)
            except (KeyError, StopIteration, TypeError):
                changed = True
        if changed and path not in linked_inputs:
            errors.append("attempt 2 changes unlinked input %s" % path)
    old_sources = {item["source_id"]: item for item in first.get("source_registry", [])}
    new_sources = {item["source_id"]: item for item in second.get("source_registry", [])}
    for source_id in sorted(set(old_sources) | set(new_sources)):
        old_row, new_row = old_sources.get(source_id), new_sources.get(source_id)
        affected_inputs = set((old_row or {}).get("input_paths", [])) | set(
            (new_row or {}).get("input_paths", []))
        if old_row != new_row and source_id not in linked_sources and not (affected_inputs & linked_inputs):
            errors.append("attempt 2 changes unlinked source %s" % source_id)

    old_packet, new_packet = copy.deepcopy(old["packet"]), copy.deepcopy(new["packet"])
    for packet in (old_packet, new_packet):
        packet.pop("run_meta", None)
    packet_map = {
        "inputs.target_archetype_coverage": ("inputs", "target_archetype_coverage"),
        "inputs.commercial_retention": ("inputs", "commercial_capture_share"),
        "inputs.five_year_sale_availability": ("inputs", "five_year_sale_availability"),
        "inputs.buy_mult": ("inputs", "buy_multiple"),
        "inputs.downside_exit_mult": ("inputs", "downside_exit_multiple"),
        "inputs.y5_survival": ("inputs", "operator_controlled_demand_share_y5"),
        "dataset_inputs.n_band": ("dataset_fallbacks", "n_band"),
    }
    for input_path, (section, key) in packet_map.items():
        if input_path in linked_inputs:
            for packet in (old_packet, new_packet):
                if key in packet.get(section, {}):
                    packet[section][key] = "<authorized-remediation>"
    for path in linked_inputs:
        if path.startswith("inputs.implementation_ramp.r"):
            try:
                index = int(path.rsplit("r", 1)[1]) - 1
            except (TypeError, ValueError):
                continue
            for packet in (old_packet, new_packet):
                ramp = packet.get("inputs", {}).get("implementation_realization", {})
                for key in ("value", "low", "high"):
                    if isinstance(ramp.get(key), list) and 0 <= index < len(ramp[key]):
                        ramp[key][index] = "<authorized-remediation>"
        if path.startswith("inputs.target_role_mix.roles[role_id=") and path.endswith(".removable_fraction"):
            role_id = path.split("[role_id=", 1)[1].split("]", 1)[0]
            for packet in (old_packet, new_packet):
                roles = packet.get("inputs", {}).get("target_role_judgments", {}).get("roles", [])
                for index, role in enumerate(roles):
                    if role.get("role_id") == role_id:
                        roles[index] = "<authorized-remediation>"
    if old_packet != new_packet:
        errors.append("attempt 2 changes packet content outside predecessor-linked inputs")

    old_spec, new_spec = copy.deepcopy(old["industry_spec"]), copy.deepcopy(new["industry_spec"])
    alternative_count_linked = any(
        path.startswith("industry_spec.target_archetype.alternatives[id=")
        for path in linked_inputs
    )
    for path in linked_inputs:
        if path.startswith("industry_spec.target_archetype.alternatives[id="):
            alternative_id = path.split("[id=", 1)[1].split("]", 1)[0]
            for spec in (old_spec, new_spec):
                alternative = next((item for item in spec["target_archetype"]["alternatives"]
                                    if item.get("id") == alternative_id), None)
                if alternative is not None:
                    alternative["band_count"] = "<authorized-remediation>"
        elif path == "industry_spec.target_archetype.selected_id":
            old_spec["target_archetype"]["selected_id"] = "<authorized-remediation>"
            new_spec["target_archetype"]["selected_id"] = "<authorized-remediation>"
        elif path == "industry_spec.target_archetype.enumeration_coverage":
            old_spec["target_archetype"]["enumeration_coverage"] = "<authorized-remediation>"
            new_spec["target_archetype"]["enumeration_coverage"] = "<authorized-remediation>"
        elif path == "industry_spec.target_archetype.residual.band_count":
            old_spec["target_archetype"]["residual"]["band_count"] = "<authorized-remediation>"
            new_spec["target_archetype"]["residual"]["band_count"] = "<authorized-remediation>"
        elif path == "inputs.target_labor_cost_share":
            for spec in (old_spec, new_spec):
                if "labor_contractor_cash_cost_share" in spec.get("value_basis", {}):
                    spec["value_basis"]["labor_contractor_cash_cost_share"] = "<authorized-remediation>"
        elif path.startswith("inputs.target_role_mix.roles[role_id=") and path.endswith(".cost_weight"):
            role_id = path.split("[role_id=", 1)[1].split("]", 1)[0]
            for spec in (old_spec, new_spec):
                role = next((item for item in spec.get("value_basis", {}).get("roles", [])
                             if item.get("role_id") == role_id), None)
                if role is not None:
                    role["role_cash_cost_weight"] = "<authorized-remediation>"
    if alternative_count_linked:
        # These fields are deterministic consequences of alternative counts under
        # the frozen largest-base/reconciliation rules; no other archetype sibling is masked.
        for spec in (old_spec, new_spec):
            archetype = spec["target_archetype"]
            archetype["selected_id"] = "<deterministic-dependent>"
            archetype["selection_uncertainty"] = "<deterministic-dependent>"
            archetype["enumeration_coverage"]["base"] = "<deterministic-dependent>"
            archetype["residual"]["band_count"]["base"] = "<deterministic-dependent>"
    if old_spec != new_spec:
        errors.append("attempt 2 changes industry spec outside predecessor-linked inputs")
    return errors


def evaluate_campaign(manifest, root=REPO, require_reviews=True):
    errors = validate_manifest(manifest, root)
    reviews, review_hashes, loaded_reviews = {}, {}, {}
    for entry in manifest.get("entries", []):
        path = _review_path(entry, root)
        if not os.path.isfile(path):
            if require_reviews:
                errors.append("%s review missing" % entry["entry_id"])
            continue
        try:
            review = load_json(path)
        except (OSError, ValueError, json.JSONDecodeError) as exc:
            errors.append("%s review load failed: %s" % (entry["entry_id"], exc))
            continue
        if not isinstance(review, dict):
            errors.append("%s review must be an object" % entry["entry_id"])
            continue
        loaded_reviews[entry["entry_id"]] = review
        item_errors = review_errors(review, entry, manifest, root)
        errors.extend("%s: %s" % (entry["entry_id"], item) for item in item_errors)
        if not item_errors:
            reviews[entry["entry_id"]] = review
            review_hashes[entry["entry_id"]] = sha256(path)

    research_tasks = []
    for entry in manifest.get("entries", []):
        try:
            envelope = load_json(_absolute(root, entry["artifacts"]["execution_envelope"]["path"]))
        except (OSError, ValueError, TypeError, KeyError, json.JSONDecodeError):
            continue
        research_tasks.append(envelope.get("codex_task_path"))
    reviewer_tasks = [review.get("execution", {}).get("codex_task_path")
                      for review in loaded_reviews.values()]
    concrete_reviewer_tasks = [item for item in reviewer_tasks if isinstance(item, str)]
    if len(concrete_reviewer_tasks) != len(set(concrete_reviewer_tasks)):
        errors.append("reviewer codex_task_path must be globally unique per entry")
    if set(concrete_reviewer_tasks) & set(research_tasks):
        errors.append("every reviewer task must be distinct from all research tasks")

    by_code = {}
    for entry in manifest.get("entries", []):
        by_code.setdefault((entry["kind"], entry["naics"]), []).append(entry)
    selected = []
    for attempts in by_code.values():
        attempts = sorted(attempts, key=lambda item: item["attempt"])
        selected.append(attempts[-1])
        if len(attempts) == 2:
            first, second = attempts
            prior = reviews.get(first["entry_id"])
            if prior and prior["outcome"] not in ("reject", "invalid"):
                errors.append("%s remediates a predecessor that was not reject/invalid" % second["entry_id"])
            if prior and second.get("predecessor_review_sha256") != review_hashes.get(first["entry_id"]):
                errors.append("%s predecessor review digest mismatch" % second["entry_id"])
            if prior and isinstance(second.get("remediation_bundle"), dict):
                try:
                    bundle = load_json(_absolute(root, second["remediation_bundle"]["path"]))
                except (OSError, ValueError, TypeError, json.JSONDecodeError) as exc:
                    errors.append("%s remediation bundle load failed: %s" % (second["entry_id"], exc))
                else:
                    expected_findings = [item for item in prior.get("findings", [])
                                         if item.get("severity") in ("material", "fatal_mechanics")]
                    if bundle != {
                        "predecessor_entry_id": first["entry_id"],
                        "predecessor_review_sha256": review_hashes.get(first["entry_id"]),
                        "findings": expected_findings,
                    }:
                        errors.append("%s remediation bundle is not the exact predecessor defect set" % second["entry_id"])
                    else:
                        errors.extend("%s: %s" % (second["entry_id"], item) for item in
                                      _remediation_semantic_errors(first, second, expected_findings, root))

    membership_complete = not any("membership" in item or "must have exactly one attempt 1" in item for item in errors)
    reviews_complete = len(reviews) == len(manifest.get("entries", []))
    published = [item for item in selected if reviews.get(item["entry_id"], {}).get("outcome") in PUBLISHABLE]
    publication_complete = len(published) == len(selected) and bool(selected)
    status = {
        "membership_complete": membership_complete,
        "reviews_complete": reviews_complete,
        "publication_complete": publication_complete,
        "selected_records": len(selected),
        "published_records": len(published),
        "publication_coverage": 0.0 if not selected else len(published) / float(len(selected)),
        "selected_entry_ids": sorted(item["entry_id"] for item in selected),
        "review_digests": dict(sorted(review_hashes.items())),
    }
    if manifest.get("scope") == DEVELOPMENT_SCOPE:
        errors.extend(_canary_errors(manifest, selected, reviews, review_hashes, root))
        status[DEVELOPMENT_GATE_KEY + "_passed"] = not any(
            item.startswith(DEVELOPMENT_GATE_LABEL + " gate:") for item in errors)
    elif manifest.get("scope") == "holdout":
        errors.extend(_holdout_errors(manifest, selected, reviews, review_hashes, root))
        status["holdout_gate_passed"] = not any(item.startswith("holdout gate:") for item in errors)
    status["campaign_accepted"] = not errors and reviews_complete and (
        (manifest.get("scope") != DEVELOPMENT_SCOPE or status.get(DEVELOPMENT_GATE_KEY + "_passed"))
        and (manifest.get("scope") != "holdout" or status.get("holdout_gate_passed"))
    )
    return status, errors


def _certificate_source_status(manifest, root):
    """Reopen the source campaign through the normal validator (patchable in fixtures only)."""
    return evaluate_campaign(manifest, root)


def _canary_errors(manifest, selected, reviews, review_hashes, root):
    return _five_code_gate_errors(
        manifest, selected, reviews, review_hashes, root,
        label=DEVELOPMENT_GATE_LABEL, codes=CANARY_CODES, gate_key=DEVELOPMENT_GATE_KEY,
    )


def _holdout_errors(manifest, selected, reviews, review_hashes, root):
    return _five_code_gate_errors(
        manifest, selected, reviews, review_hashes, root,
        label="holdout", codes=HOLDOUT_CODES, gate_key="holdout_gate",
    )


def _five_code_gate_errors(manifest, selected, reviews, review_hashes, root, label, codes, gate_key):
    errors = []
    def fail(message):
        errors.append(label + " gate: " + message)
    if len(selected) != 5 or {(item["kind"], item["naics"]) for item in selected} != {
        ("fleet", code) for code in codes
    }:
        fail("selected membership is not exact 5/5")
    if any(reviews.get(item["entry_id"], {}).get("outcome") not in PUBLISHABLE for item in selected):
        fail("all 5 selected reviews must be publishable")
    by_code = {}
    for entry in manifest.get("entries", []):
        by_code.setdefault((entry["kind"], entry["naics"]), []).append(entry)
    for attempts in by_code.values():
        if len(attempts) != 2:
            continue
        first, second = sorted(attempts, key=lambda item: item["attempt"])
        prior = reviews.get(first["entry_id"], {})
        current = reviews.get(second["entry_id"], {})
        old = {item.get("fingerprint") for item in prior.get("findings", [])
               if item.get("severity") in ("material", "fatal_mechanics")}
        new = {item.get("fingerprint") for item in current.get("findings", [])
               if item.get("severity") in ("material", "fatal_mechanics")}
        if old & new:
            fail("attempt 2 repeats a material/fatal defect")
    gate = manifest.get(gate_key, {})
    signoff_key = ("operator_signoff" if MANIFEST_VERSION == "review-campaign-4.2"
                   else "human_sense_signoff")
    report_key = ("sentinel_gate_report" if MANIFEST_VERSION == "review-campaign-4.2"
                  else "invariant_report")
    for key in (report_key, signoff_key):
        ref = gate.get(key)
        if key in ("operator_signoff", "sentinel_gate_report"):
            ref_errors = [] if isinstance(ref, dict) else ["operator_signoff must be an object"]
        else:
            ref_errors = _ref_errors("%s %s" % (label, key), ref, root)
        for item in ref_errors:
            fail(item)
    if errors:
        return errors
    if MANIFEST_VERSION == "review-campaign-4.2":
        for item in _operator_signoff_errors(
                manifest, selected, review_hashes, root, gate, label):
            fail(item)
        return errors
    invariant = load_json(_absolute(root, gate["invariant_report"]["path"]))
    if not isinstance(invariant, dict):
        return errors + [label + " gate: invariant report must be an object"]
    if set(invariant) != {"campaign_binding_sha256", "passed", "checks"}:
        fail("invariant report must be a closed campaign_binding_sha256/passed/checks object")
    binding = campaign_binding_sha256(manifest)
    if invariant.get("campaign_binding_sha256") != binding or invariant.get("passed") is not True:
        fail("invariant report must pass and bind this campaign")
    checks = invariant.get("checks")
    if (not isinstance(checks, dict) or set(checks) != INVARIANT_CHECKS
            or not all(value is True for value in checks.values())):
        fail("every required invariant check must be present and explicitly true")
    signoff = load_json(_absolute(root, gate["human_sense_signoff"]["path"]))
    if not isinstance(signoff, dict):
        return errors + [label + " gate: human signoff must be an object"]
    if set(signoff) != {"campaign_binding_sha256", "decision", "reviewer_identity", "signed_at",
                        "notes", "selected_entry_ids", "review_digests", "signoff_execution",
                        "commit_sha256"}:
        fail("human signoff must use the closed v4.1 signoff contract")
    if signoff.get("campaign_binding_sha256") != binding:
        fail("human signoff does not bind this campaign")
    identity = signoff.get("reviewer_identity")
    if (signoff.get("decision") != "approve" or not isinstance(identity, str)
            or "@" not in identity or len(identity) < 6 or not signoff.get("notes")):
        fail("human economic-sense signoff must approve")
    execution = signoff.get("signoff_execution", {})
    if (not isinstance(execution, dict)
            or set(execution) != {"issued_by_task_path", "codex_task_path", "role"}
            or execution.get("issued_by_task_path") != "/root"
            or execution.get("role") != "human_signoff"
            or not isinstance(execution.get("codex_task_path"), str)
            or not execution["codex_task_path"].startswith("/root/")
            or execution["codex_task_path"] == "/root/"):
        fail("human signoff requires a closed root-issued execution receipt")
    if not _is_nonzero_sha256(signoff.get("commit_sha256")):
        fail("human signoff requires a verifiable commit digest")
    occupied_tasks = set()
    for entry in manifest.get("entries", []):
        try:
            research = load_json(_absolute(root, entry["artifacts"]["execution_envelope"]["path"]))
            occupied_tasks.add(research.get("codex_task_path"))
        except (OSError, ValueError, TypeError, KeyError, json.JSONDecodeError):
            pass
        review = reviews.get(entry["entry_id"], {})
        occupied_tasks.add(review.get("execution", {}).get("codex_task_path"))
    if execution.get("codex_task_path") in occupied_tasks:
        fail("human signoff execution must be distinct from research and review tasks")
    try:
        signed_at = date.fromisoformat(signoff.get("signed_at", ""))
        if signed_at > date.today():
            fail("human signoff signed_at cannot be in the future")
    except (TypeError, ValueError):
        fail("human signoff signed_at must be a real ISO date")
    if signoff.get("selected_entry_ids") != sorted(item["entry_id"] for item in selected):
        fail("human signoff selected entries differ")
    selected_review_digests = {
        item["entry_id"]: review_hashes[item["entry_id"]]
        for item in selected if item["entry_id"] in review_hashes
    }
    if signoff.get("review_digests") != dict(sorted(selected_review_digests.items())):
        fail("human signoff review digests differ")
    return errors


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", required=True)
    parser.add_argument("--allow-missing-reviews", action="store_true")
    args = parser.parse_args(argv)
    try:
        manifest = load_json(args.manifest)
        status, errors = evaluate_campaign(manifest, require_reviews=not args.allow_missing_reviews)
    except (OSError, ValueError, KeyError, TypeError, json.JSONDecodeError) as exc:
        print("v4.1 campaign error: %s" % exc, file=sys.stderr)
        return 1
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1
    print(json.dumps(status, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
