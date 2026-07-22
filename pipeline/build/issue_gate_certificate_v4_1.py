#!/usr/bin/env python3
"""Issue a full-scope prerequisite certificate from an accepted v4.1 gate."""

import argparse
from datetime import date
import importlib.util
import os
from pathlib import Path


HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent


def _load_campaign():
    spec = importlib.util.spec_from_file_location("campaign_v4_1_for_gate_issuer",
                                                  HERE / "campaign_v4_1.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


campaign = _load_campaign()


class CertificateError(ValueError):
    pass


def _create(path, value, created):
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        raise CertificateError("refusing to overwrite gate artifact: %s" % path)
    with path.open("xb") as handle:
        handle.write(campaign.canonical_bytes(value))
    created.append(path)


def issue(root, manifest_path, certificate_task_path, issued_at=None):
    root = Path(root).resolve()
    manifest_file = Path(manifest_path)
    if not manifest_file.is_absolute():
        manifest_file = root / manifest_file
    manifest_file = manifest_file.resolve()
    try:
        relative_manifest = manifest_file.relative_to(root).as_posix()
    except ValueError as exc:
        raise CertificateError("campaign manifest must be inside the repository") from exc
    manifest = campaign.load_json(str(manifest_file))
    scope = manifest.get("scope")
    if scope not in (campaign.DEVELOPMENT_SCOPE, "holdout"):
        raise CertificateError("only %s or holdout campaigns can be certified" %
                               campaign.DEVELOPMENT_SCOPE)
    if (not isinstance(certificate_task_path, str)
            or not certificate_task_path.startswith("/root/")
            or certificate_task_path == "/root/"):
        raise CertificateError("certificate task must be an exact root-issued child task")
    issued_at = issued_at or date.today().isoformat()
    try:
        issued_date = date.fromisoformat(issued_at)
    except (TypeError, ValueError) as exc:
        raise CertificateError("issued_at must be a real ISO date") from exc
    if issued_date > date.today():
        raise CertificateError("issued_at cannot be in the future")

    status, errors = campaign.evaluate_campaign(manifest, str(root))
    gate_status = (campaign.DEVELOPMENT_GATE_KEY + "_passed"
                   if scope == campaign.DEVELOPMENT_SCOPE else "holdout_gate_passed")
    if errors or status.get("campaign_accepted") is not True or status.get(gate_status) is not True:
        raise CertificateError("campaign gate is not exactly accepted: %s" % "; ".join(errors))
    name = "regression_canary" if scope == campaign.DEVELOPMENT_SCOPE else "holdout"
    paths = campaign.FULL_GATE_PATHS[name]
    selected_ids = status["selected_entry_ids"]
    selected = {item["entry_id"]: item for item in manifest["entries"]
                if item["entry_id"] in selected_ids}
    proof_entries = []
    for entry_id in selected_ids:
        entry = selected[entry_id]
        envelope = campaign.load_json(str(root / entry["artifacts"]["execution_envelope"]["path"]))
        review = campaign.load_json(str(root / entry["review_path"]))
        proof_entries.append({
            "entry_id": entry_id, "naics": entry["naics"],
            "research_execution": {key: envelope[key] for key in
                                   ("issued_by_task_path", "codex_task_path", "fork_policy", "role")},
            "review_execution": dict(review["execution"]),
            "review_sha256": campaign.sha256(str(root / entry["review_path"])),
            "outcome": review["outcome"],
        })
    campaign_proof = {
        "proof_version": campaign.GATE_CAMPAIGN_PROOF_VERSION, "scope": scope,
        "source_manifest": {"path": paths["source"],
                            "sha256": campaign.value_sha256(manifest)},
        "entries": proof_entries,
    }
    campaign_root = campaign.value_sha256(campaign_proof)
    gate_key = campaign.DEVELOPMENT_GATE_KEY if scope == campaign.DEVELOPMENT_SCOPE else "holdout_gate"
    gate = manifest[gate_key]
    operator_contract = campaign.MANIFEST_VERSION == "review-campaign-4.2"
    if operator_contract:
        proof_signoff = gate["operator_signoff"]
        signoff_field = "operator_signoff"
        report_field = "sentinel_gate_report"
        report_value = gate["sentinel_gate_report"]
    else:
        invariant = campaign.load_json(str(root / gate["invariant_report"]["path"]))
        signoff = campaign.load_json(str(root / gate["human_sense_signoff"]["path"]))
        proof_signoff = {key: value for key, value in signoff.items()
                         if key != "campaign_binding_sha256"}
        signoff_field = "signoff"
        report_field = "invariant_checks"
        report_value = invariant["checks"]
    gate_proof = {
        "proof_version": campaign.GATE_PROOF_VERSION, "scope": scope,
        "campaign_root_sha256": campaign_root, "accepted": True,
        "selected_entry_ids": selected_ids,
        "review_digests": status["review_digests"],
        report_field: report_value, signoff_field: proof_signoff,
    }
    created = []
    try:
        _create(root / paths["source"], manifest, created)
        _create(root / paths["campaign"], campaign_proof, created)
        _create(root / paths["gate"], gate_proof, created)
        certificate = {
            "certificate_version": campaign.GATE_CERTIFICATE_VERSION, "scope": scope,
            "campaign_root_sha256": campaign_root,
            "gate_root_sha256": campaign.value_sha256(gate_proof),
            "accepted": True,
            "selected_codes": sorted(item["naics"] for item in proof_entries),
            "issued_by_task_path": "/root", "codex_task_path": certificate_task_path,
            "issued_at": issued_at,
            "campaign_artifact": campaign.artifact_ref(paths["campaign"], str(root)),
            "gate_artifact": campaign.artifact_ref(paths["gate"], str(root)),
        }
        certificate["certificate_binding_sha256"] = campaign.value_sha256(certificate)
        _create(root / paths["certificate"], certificate, created)
    except Exception:
        for path in reversed(created):
            try:
                path.unlink()
            except FileNotFoundError:
                pass
        raise
    return certificate


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=str(REPO))
    parser.add_argument("--manifest", required=True)
    parser.add_argument("--certificate-task-path", required=True)
    parser.add_argument("--issued-at")
    args = parser.parse_args(argv)
    try:
        certificate = issue(args.root, args.manifest, args.certificate_task_path, args.issued_at)
    except (CertificateError, OSError, ValueError) as exc:
        print("GATE CERTIFICATE FAILED: %s" % exc)
        return 1
    print("OK: issued %s gate certificate %s" %
          (certificate["scope"], certificate["certificate_binding_sha256"]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
