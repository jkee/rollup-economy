#!/usr/bin/env python3
"""Issue an immutable, freeze-bound v4.2 pre-run campaign plan.

This command runs before research.  It reads only frozen infrastructure,
membership, prompts, industry specifications, datasets, and externally stored
post-freeze authorization receipts.  It creates exact attempt-1 execution
envelopes, atomic output-reservation sidecars, and one canonical plan; it never
creates a packet, finalized record, memo, or review.
"""

import argparse
from contextlib import contextmanager
from datetime import date, datetime, timezone
import hashlib
import importlib.util
import io
import json
import os
from pathlib import Path, PureWindowsPath
import re
import secrets
import stat
import subprocess
import sys
import tarfile
import tempfile
from types import SimpleNamespace
import urllib.error
import urllib.request


REPO = Path(__file__).resolve().parent.parent.parent
PLAN_VERSION = "v4.2-pre-run-issuance-1"
REMEDIATION_PLAN_VERSION = "v4.2-remediation-issuance-1"
RESERVATION_VERSION = "v4.2-output-reservation-1"
CLAIM_RECEIPT_VERSION = "v4.2-output-claim-receipt-1"
FREEZE_VERSION = "v4.2-freeze-1"
PROMPT_VERSION = "v4.2-target-archetype-1"
REVIEW_PROMPT_VERSION = "validator-4.2"
REGRESSION_CODES = ("238220", "541214", "541511", "541512", "541930")
HOLDOUT_SIZE = 5
FULL_SIZE = 53
TARGETS_PATH = "pipeline/blocks/targets_phase3.json"
HOLDOUT_PATH = "pipeline/v4_2/holdout_membership.json"
REGRESSION_PATH = "pipeline/v4_2/regression_membership.json"
MODEL_ROUTES_PATH = "pipeline/v4_2/model_routes.json"
FREEZE_MANIFEST_PATH = "pipeline/v4_2/freeze_manifest.json"
FREEZE_CONTRACT_PATH = "pipeline/build/freeze_contract_v4_2.required.json"
FREEZE_VALIDATOR_PATH = "pipeline/build/freeze_contract_v4_2.py"
GITHUB_REPOSITORY = "jkee/rollup-economy"
GITHUB_API_ROOT = "https://api.github.com/repos/%s" % GITHUB_REPOSITORY
GITHUB_WEB_ROOT = "https://github.com/%s" % GITHUB_REPOSITORY
FREEZE_WORKFLOW_PATH = ".github/workflows/v4-2-freeze.yml"
FREEZE_WORKFLOW_NAME = "v4.2 freeze evidence"
EXTENSION_WORKFLOW_PATH = ".github/workflows/v4-2-full-scope-extension.yml"
EXTENSION_WORKFLOW_NAME = "v4.2 full scope extension evidence"
REGRESSION_GATE_CERTIFICATE_PATH = "pipeline/v4_2/gates/regression/certificate.json"
HOLDOUT_GATE_CERTIFICATE_PATH = "pipeline/v4_2/gates/holdout/certificate.json"
SCOPE_EXTENSION_MANIFEST_PATH = "pipeline/v4_2/full_scope_extension_manifest.json"

TOOLCHAIN_PATHS = {
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
    "campaign_validator": "pipeline/build/campaign_v4_2.py",
    "renderer": "pipeline/build/build.py",
    "dataset_normalizer": "pipeline/build/normalize_datasets_v4_2.py",
    "holdout_selector": "pipeline/build/select_holdout_v4_2.py",
    "freeze_builder": "pipeline/build/freeze_v4_2.py",
    "campaign_authority_core": "pipeline/build/campaign_v4_1.py",
    "issuer_authority_core": "pipeline/build/issue_campaign_v4_1.py",
    "prompt_assembler": "pipeline/build/assemble_prompts.py",
    "prompt_template": "pipeline/template/prompt_template_v4_2.md",
    "runner_prompt": "pipeline/template/runner_brief_v4_2.md",
    "validator_prompt": "pipeline/template/validator_brief_v4_2.md",
    "model_routes": MODEL_ROUTES_PATH,
    "change_control": "pipeline/v4_2/change_control.json",
    "freeze_plan": "pipeline/v4_2/freeze_plan.json",
    "freeze_workflow": FREEZE_WORKFLOW_PATH,
    "extension_workflow": EXTENSION_WORKFLOW_PATH,
    "extension_validator": "pipeline/build/validate_full_scope_extension_v4_2.py",
    "allowed_signers": "pipeline/v4_2/allowed_signers",
    "freeze_contract": FREEZE_CONTRACT_PATH,
    "freeze_validator": FREEZE_VALIDATOR_PATH,
    "issuer": "pipeline/build/issue_campaign_v4_2.py",
    "guarded_writer": "pipeline/build/guarded_write_v4_2.py",
    "gate_certificate_issuer": "pipeline/build/issue_gate_certificate_v4_2.py",
    "gate_certificate_core": "pipeline/build/issue_gate_certificate_v4_1.py",
}

ENVELOPE_HASH_PATHS = {
    "methodology_sha256": TOOLCHAIN_PATHS["methodology"],
    "thresholds_sha256": TOOLCHAIN_PATHS["thresholds"],
    "research_packet_schema_sha256": TOOLCHAIN_PATHS["packet_schema"],
    "dataset_schema_sha256": TOOLCHAIN_PATHS["dataset_schema"],
    "industry_spec_schema_sha256": TOOLCHAIN_PATHS["industry_spec_schema"],
    "run_record_schema_sha256": TOOLCHAIN_PATHS["run_schema"],
    "scoring_sha256": TOOLCHAIN_PATHS["scoring"],
    "finalizer_sha256": TOOLCHAIN_PATHS["finalizer"],
}


class IssueError(ValueError):
    """Raised when no safe pre-run issuance can be produced."""


def _require_private_pipe_fd(descriptor, label):
    if not isinstance(descriptor, int) or descriptor < 3:
        raise IssueError("%s must be a private descriptor >= 3" % label)
    mode = os.fstat(descriptor).st_mode
    if not (stat.S_ISFIFO(mode) or stat.S_ISSOCK(mode)):
        raise IssueError("%s must be a FIFO or socket, never a regular file or directory" % label)


def _reject_constant(value):
    raise IssueError("non-standard JSON constant %r is forbidden" % value)


def _closed_pairs(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise IssueError("duplicate JSON key %r" % key)
        result[key] = value
    return result


def load_json(path):
    try:
        with Path(path).open("r", encoding="utf-8") as handle:
            return json.load(
                handle,
                parse_constant=_reject_constant,
                object_pairs_hook=_closed_pairs,
            )
    except FileNotFoundError as exc:
        raise IssueError("JSON file not found: %s" % path) from exc
    except json.JSONDecodeError as exc:
        raise IssueError("invalid JSON in %s: %s" % (path, exc)) from exc


def canonical_bytes(value):
    return json.dumps(
        value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False
    ).encode("utf-8")


def sha256_bytes(value):
    return hashlib.sha256(value).hexdigest()


def sha256_file(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _repository_path(root, relative, *, must_exist=False):
    if not isinstance(relative, str) or not relative or "\x00" in relative:
        raise IssueError("path must be a non-empty repository-relative string")
    windows = PureWindowsPath(relative)
    if "\\" in relative or os.path.isabs(relative) or windows.is_absolute() or windows.drive:
        raise IssueError("path must be canonical repository-relative POSIX: %s" % relative)
    parts = relative.split("/")
    if any(part in ("", ".", "..") for part in parts):
        raise IssueError("path has an unsafe component: %s" % relative)
    root = Path(root).resolve()
    path = root.joinpath(*parts).resolve()
    try:
        path.relative_to(root)
    except ValueError as exc:
        raise IssueError("path escapes repository: %s" % relative) from exc
    if must_exist and not path.is_file():
        raise IssueError("required file does not exist: %s" % relative)
    return path


def _root_sha256(files):
    digest = hashlib.sha256()
    for item in sorted(files, key=lambda row: row["path"].encode("utf-8")):
        digest.update(item["path"].encode("utf-8"))
        digest.update(b"\0")
        digest.update(str(item["byte_length"]).encode("ascii"))
        digest.update(b"\0")
        digest.update(item["sha256"].encode("ascii"))
        digest.update(b"\n")
    return digest.hexdigest()


def _git(root, *args):
    result = subprocess.run(
        ["git", "-C", str(root), *args],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        check=False,
    )
    if result.returncode:
        raise IssueError("git %s failed: %s" % (" ".join(args), result.stderr.strip()))
    return result.stdout.strip()


def _git_bytes(root, *args):
    result = subprocess.run(
        ["git", "-C", str(root), *args],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if result.returncode:
        raise IssueError(
            "git %s failed: %s" %
            (" ".join(args), result.stderr.decode("utf-8", errors="replace").strip())
        )
    return result.stdout


def _require_committed(root, relative):
    status = _git(root, "status", "--porcelain=v1", "--untracked-files=all", "--", relative)
    if status:
        raise IssueError("referenced path is uncommitted, staged, or unstaged: %s" % relative)
    _git(root, "ls-files", "--error-unmatch", "--", relative)


def _load_freeze_contract(root=REPO):
    path = _repository_path(root, FREEZE_VALIDATOR_PATH, must_exist=True)
    spec = importlib.util.spec_from_file_location("freeze_contract_v4_2_for_issuer", path)
    if spec is None or spec.loader is None:
        raise IssueError("cannot load the frozen v4.2 freeze-contract validator")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _receipt_path(root, supplied, label):
    if not isinstance(supplied, (str, os.PathLike)) or not str(supplied):
        raise IssueError("%s receipt path is required" % label)
    path = Path(supplied)
    if not path.is_absolute():
        path = Path(root) / path
    path = path.resolve()
    if not path.is_file():
        raise IssueError("%s receipt file does not exist: %s" % (label, supplied))
    return path


def _external_ref(path, supplied):
    return {
        "path": str(supplied),
        "sha256": sha256_file(path),
        "byte_length": path.stat().st_size,
    }


class _RejectRedirects(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        raise IssueError("GitHub API redirect is forbidden")


def _github_get_json(url):
    if not isinstance(url, str) or not url.startswith(GITHUB_API_ROOT + "/actions/"):
        raise IssueError("live CI verification URL is outside the exact GitHub API authority")
    request = urllib.request.Request(
        url,
        headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": "rollup-economy-v4.2-freeze-issuer",
            "X-GitHub-Api-Version": "2022-11-28",
        },
        method="GET",
    )
    try:
        with urllib.request.build_opener(_RejectRedirects()).open(request, timeout=20) as response:
            if response.geturl() != url or response.status != 200:
                raise IssueError("GitHub API returned a redirect or non-200 status")
            length = response.headers.get("Content-Length")
            if length is not None and int(length) > 2_000_000:
                raise IssueError("GitHub API response is too large")
            body = response.read(2_000_001)
    except (OSError, ValueError, urllib.error.URLError) as exc:
        raise IssueError("live GitHub CI verification failed: %s" % exc) from exc
    if len(body) > 2_000_000:
        raise IssueError("GitHub API response is too large")
    try:
        return json.loads(
            body.decode("utf-8"),
            parse_constant=_reject_constant,
            object_pairs_hook=_closed_pairs,
        )
    except (UnicodeError, json.JSONDecodeError, IssueError) as exc:
        raise IssueError("GitHub API returned malformed JSON: %s" % exc) from exc


def _api_time(value, label):
    if not isinstance(value, str) or not value:
        raise IssueError("live CI %s timestamp is missing" % label)
    normalized = value[:-1] + "+00:00" if value.endswith("Z") else value
    try:
        parsed = datetime.fromisoformat(normalized)
    except ValueError as exc:
        raise IssueError("live CI %s timestamp is invalid" % label) from exc
    if parsed.tzinfo is None or parsed.utcoffset() is None:
        raise IssueError("live CI %s timestamp lacks a timezone" % label)
    return parsed


def _verify_live_ci(ci, commit, tag, fetch_json=None, *,
                    workflow_path=FREEZE_WORKFLOW_PATH,
                    workflow_name=FREEZE_WORKFLOW_NAME,
                    artifact_prefix="v4.2-freeze-"):
    """Verify the receipt against the exact public GitHub Actions API records."""
    fetch_json = fetch_json or _github_get_json
    run_id = ci["run_id"]
    run_url = "%s/actions/runs/%s" % (GITHUB_API_ROOT, run_id)
    artifacts_url = run_url + "/artifacts"
    if (ci.get("github_owner") != "jkee"
            or ci.get("github_repository") != "rollup-economy"
            or ci.get("run_api_url") != run_url
            or ci.get("artifacts_api_url") != artifacts_url):
        raise IssueError("CI receipt does not bind the exact GitHub API authority")
    try:
        run = fetch_json(run_url)
        listing = fetch_json(artifacts_url)
    except IssueError:
        raise
    except Exception as exc:
        raise IssueError("live GitHub CI verification failed: %s" % exc) from exc
    if not isinstance(run, dict) or not isinstance(listing, dict):
        raise IssueError("live GitHub CI responses must be JSON objects")

    commit_sha, tag_name = commit["commit_sha"], tag["tag_name"]
    expected_web_run = "%s/actions/runs/%s" % (GITHUB_WEB_ROOT, run_id)
    expected_path_values = {
        workflow_path,
        "%s@refs/tags/%s" % (workflow_path, tag_name),
    }
    expected_run = {
        "id": run_id,
        "workflow_id": ci["workflow_id"],
        "run_attempt": ci["run_attempt"],
        "html_url": expected_web_run,
        "artifacts_url": artifacts_url,
        "status": "completed",
        "conclusion": "success",
        "event": ci["event"],
        "head_sha": commit_sha,
        "head_branch": tag_name,
        "name": workflow_name,
    }
    for key, expected in expected_run.items():
        if run.get(key) != expected:
            raise IssueError("live GitHub Actions run %s does not match the receipt" % key)
    if run.get("path") not in expected_path_values:
        raise IssueError("live GitHub Actions run does not bind the frozen workflow path")
    if ci["run_html_url"] != expected_web_run:
        raise IssueError("CI receipt run_html_url is not the exact authorized GitHub run URL")
    created = _api_time(run.get("created_at"), "created_at")
    started = _api_time(run.get("run_started_at"), "run_started_at")
    updated = _api_time(run.get("updated_at"), "updated_at")
    issued = _api_time(ci["issued_at"], "receipt issued_at")
    if (not created <= started <= updated <= issued
            or run.get("run_started_at") != ci["run_started_at"]
            or run.get("updated_at") != ci["run_updated_at"]):
        raise IssueError("live GitHub Actions run timestamps do not match the CI receipt")

    artifacts = listing.get("artifacts")
    if (not isinstance(listing.get("total_count"), int)
            or isinstance(listing["total_count"], bool)
            or not isinstance(artifacts, list)
            or listing["total_count"] != len(artifacts)):
        raise IssueError("live GitHub artifact listing shape/count is invalid")
    expected_name = artifact_prefix + commit_sha
    matches = [item for item in artifacts
               if isinstance(item, dict) and item.get("name") == expected_name]
    if len(matches) != 1:
        raise IssueError("live GitHub evidence must contain one exact freeze artifact")
    artifact = matches[0]
    artifact_id = artifact.get("id")
    if not isinstance(artifact_id, int) or isinstance(artifact_id, bool) or artifact_id <= 0:
        raise IssueError("live GitHub freeze artifact id is invalid")
    expected_artifact_api = "%s/actions/artifacts/%s" % (GITHUB_API_ROOT, artifact_id)
    workflow_run = artifact.get("workflow_run")
    if (artifact.get("expired") is not False
            or artifact.get("digest") != ci["artifact_digest"]
            or artifact.get("url") != expected_artifact_api
            or artifact.get("archive_download_url") != expected_artifact_api + "/zip"
            or ci["artifact_id"] != artifact_id
            or ci["artifact_name"] != expected_name
            or ci["artifact_api_url"] != expected_artifact_api
            or ci["artifact_archive_download_url"] != expected_artifact_api + "/zip"
            or not isinstance(workflow_run, dict)
            or workflow_run.get("id") != run_id
            or workflow_run.get("head_sha") != commit_sha):
        raise IssueError("live GitHub freeze artifact does not match the CI receipt")
    artifact_created = _api_time(artifact.get("created_at"), "artifact created_at")
    artifact_updated = _api_time(artifact.get("updated_at"), "artifact updated_at")
    if (artifact.get("created_at") != ci["artifact_created_at"]
            or artifact.get("updated_at") != ci["artifact_updated_at"]
            or not started <= artifact_created <= artifact_updated <= issued):
        raise IssueError("live GitHub artifact timestamps do not match the CI receipt")
    if _api_time(artifact.get("expires_at"), "artifact expires_at") <= datetime.now(timezone.utc):
        raise IssueError("live GitHub freeze artifact is expired")


def _verify_git_authority(root, manifest_relative, manifest, commit, tag,
                          authorized_head_sha=None):
    """Verify receipt claims against actual immutable git objects."""
    commit_sha = commit.get("commit_sha")
    tag_name = tag.get("tag_name")
    tag_object_sha = tag.get("tag_object_sha")
    expected_head = authorized_head_sha or commit_sha
    if _git(root, "rev-parse", "HEAD") != expected_head:
        raise IssueError("current HEAD is not exactly the authorized issuance commit")
    if _git(root, "cat-file", "-t", commit_sha) != "commit":
        raise IssueError("authorization commit receipt does not name a git commit")
    frozen_bytes = _repository_path(root, manifest_relative, must_exist=True).read_bytes()
    if _git_bytes(root, "show", "%s:%s" % (commit_sha, manifest_relative)) != frozen_bytes:
        raise IssueError("authorization commit does not contain the exact freeze manifest")

    actual_tag_object = tag_object_sha
    if _git(root, "cat-file", "-t", actual_tag_object) != "tag":
        raise IssueError("authorization tag is not an annotated tag object")
    if _git(root, "rev-parse", "%s^{commit}" % actual_tag_object) != commit_sha:
        raise IssueError("authorization tag does not peel to the frozen commit")
    tag_object = _git_bytes(root, "cat-file", "-p", actual_tag_object)
    headers, separator, message = tag_object.partition(b"\n\n")
    required_headers = {
        b"object " + commit_sha.encode("ascii"),
        b"type commit",
        b"tag " + tag_name.encode("utf-8"),
    }
    root_digest = manifest.get("root_sha256")
    if (not separator or not required_headers.issubset(set(headers.splitlines()))
            or not isinstance(root_digest, str)
            or re.search(
                rb"(?<![0-9a-f])" + root_digest.encode("ascii") + rb"(?![0-9a-f])",
                message,
            ) is None):
        raise IssueError("authorization tag message does not bind the exact freeze root")
    # Verify the immutable tag object already compared to the receipt.  A tag
    # name can be force-moved between checks; an object ID cannot.
    _git(
        root, "-c",
        "gpg.ssh.allowedSignersFile=pipeline/v4_2/allowed_signers",
        "verify-tag", "--raw", actual_tag_object,
    )


def _authorization_evidence(
        root, freeze_manifest, manifest, frozen,
        commit_receipt, tag_receipt, ci_receipt, ci_fetcher=None,
        verify_live_ci=True, authorized_head_sha=None,
        validation_root=None, git_runner=None):
    validation_root = Path(validation_root or root).resolve()
    contract_path = _repository_path(validation_root, FREEZE_CONTRACT_PATH, must_exist=True)
    manifest_path = _repository_path(validation_root, freeze_manifest, must_exist=True)
    commit_path = _receipt_path(root, commit_receipt, "commit")
    tag_path = _receipt_path(root, tag_receipt, "tag")
    ci_path = _receipt_path(root, ci_receipt, "CI")
    supplied = (commit_receipt, tag_receipt, ci_receipt)
    paths = (commit_path, tag_path, ci_path)
    before = [_external_ref(path, value) for path, value in zip(paths, supplied)]

    try:
        errors = _load_freeze_contract(validation_root).validate(
            contract_path, manifest_path, commit_path, tag_path, ci_path,
            validation_root, git_runner=git_runner,
        )
    except Exception as exc:
        raise IssueError("freeze authorization validation failed: %s" % exc) from exc
    if errors:
        raise IssueError("freeze authorization validation failed: %s" % "; ".join(errors))

    after = [_external_ref(path, value) for path, value in zip(paths, supplied)]
    if before != after:
        raise IssueError("authorization receipt changed during validation")
    commit, tag, ci = (load_json(path) for path in paths)
    if [_external_ref(path, value) for path, value in zip(paths, supplied)] != before:
        raise IssueError("authorization receipt changed while binding the issuance plan")
    _verify_git_authority(root, freeze_manifest, manifest, commit, tag,
                          authorized_head_sha=authorized_head_sha)
    if verify_live_ci:
        _verify_live_ci(ci, commit, tag, fetch_json=ci_fetcher)
    if [_external_ref(path, value) for path, value in zip(paths, supplied)] != before:
        raise IssueError("authorization receipt changed during final authorization verification")
    return {
        "contract": _frozen_ref(root, frozen, FREEZE_CONTRACT_PATH),
        "commit_receipt": before[0],
        "tag_receipt": before[1],
        "ci_receipt": before[2],
        "receipt_version": commit["receipt_version"],
        "root_sha256": commit["root_sha256"],
        "manifest_sha256": commit["manifest_sha256"],
        "commit_sha": commit["commit_sha"],
        "committed_at": commit["committed_at"],
        "tag_name": tag["tag_name"],
        "tag_object_sha": tag["tag_object_sha"],
        "tag_signer_identity": tag["signer_identity"],
        "tagged_at": tag["tagged_at"],
        "ci_workflow_path": ci["workflow_path"],
        "ci_provider": ci["provider"],
        "ci_github_owner": ci["github_owner"],
        "ci_github_repository": ci["github_repository"],
        "ci_workflow_id": ci["workflow_id"],
        "ci_run_id": ci["run_id"],
        "ci_run_attempt": ci["run_attempt"],
        "ci_run_api_url": ci["run_api_url"],
        "ci_run_html_url": ci["run_html_url"],
        "ci_artifacts_api_url": ci["artifacts_api_url"],
        "ci_event": ci["event"],
        "ci_conclusion": ci["conclusion"],
        "ci_run_started_at": ci["run_started_at"],
        "ci_run_updated_at": ci["run_updated_at"],
        "ci_artifact_id": ci["artifact_id"],
        "ci_artifact_name": ci["artifact_name"],
        "ci_artifact_api_url": ci["artifact_api_url"],
        "ci_artifact_archive_download_url": ci["artifact_archive_download_url"],
        "ci_artifact_digest": ci["artifact_digest"],
        "ci_artifact_created_at": ci["artifact_created_at"],
        "ci_artifact_updated_at": ci["artifact_updated_at"],
        "ci_issued_at": ci["issued_at"],
        "live_ci_policy": {
            "required_at_issuance": True,
            "campaign_revalidation": "immutable_receipt_only",
            "artifact_expiry_is_not_retroactive": True,
        },
    }


def validate_freeze(root, manifest_relative):
    root = Path(root).resolve()
    manifest_path = _repository_path(root, manifest_relative, must_exist=True)
    manifest = load_json(manifest_path)
    if not isinstance(manifest, dict) or set(manifest) != {
            "files", "manifest_version", "root_sha256"}:
        raise IssueError("freeze manifest must be a closed files/version/root object")
    if manifest["manifest_version"] != FREEZE_VERSION:
        raise IssueError("freeze manifest version must be %s" % FREEZE_VERSION)
    if manifest_path.read_bytes() != canonical_bytes(manifest):
        raise IssueError("freeze manifest is not exact canonical JSON")
    files = manifest["files"]
    if not isinstance(files, list) or not files:
        raise IssueError("freeze manifest files must be a non-empty array")
    paths = [item.get("path") for item in files if isinstance(item, dict)]
    if len(paths) != len(files) or len(paths) != len(set(paths)):
        raise IssueError("freeze manifest file paths must be present and unique")
    if paths != sorted(paths, key=lambda value: value.encode("utf-8")):
        raise IssueError("freeze manifest files are not bytewise path-sorted")
    by_path = {}
    for item in files:
        if set(item) != {"path", "byte_length", "sha256"}:
            raise IssueError("freeze file records must contain exactly path/byte_length/sha256")
        relative = item["path"]
        path = _repository_path(root, relative, must_exist=True)
        if item["byte_length"] != path.stat().st_size or item["sha256"] != sha256_file(path):
            raise IssueError("freeze file digest or byte length is stale: %s" % relative)
        _require_committed(root, relative)
        by_path[relative] = item
    if manifest["root_sha256"] != _root_sha256(files):
        raise IssueError("freeze root_sha256 is stale")
    _require_committed(root, manifest_relative)
    return manifest, by_path, {
        "path": manifest_relative,
        "sha256": sha256_file(manifest_path),
        "root_sha256": manifest["root_sha256"],
        "manifest_version": manifest["manifest_version"],
        "git_commit": _git(root, "rev-parse", "HEAD"),
    }


def _frozen_ref(root, frozen, relative):
    if relative not in frozen:
        raise IssueError("required path is not listed in freeze manifest: %s" % relative)
    path = _repository_path(root, relative, must_exist=True)
    item = frozen[relative]
    if item["sha256"] != sha256_file(path):
        raise IssueError("required frozen path changed: %s" % relative)
    return {"path": relative, "sha256": item["sha256"], "byte_length": item["byte_length"]}


def _targets(root, frozen):
    _frozen_ref(root, frozen, TARGETS_PATH)
    value = load_json(_repository_path(root, TARGETS_PATH, must_exist=True))
    rows = value.get("codes") if isinstance(value, dict) else None
    if not isinstance(rows, list):
        raise IssueError("target membership must contain a codes array")
    result = {}
    for row in rows:
        if not isinstance(row, dict) or not re.fullmatch(r"[0-9]{6}", str(row.get("naics"))):
            raise IssueError("target membership contains an invalid row")
        code, title = row["naics"], row.get("title")
        if code in result or not isinstance(title, str) or not title.strip():
            raise IssueError("target membership has duplicate code or invalid title")
        result[code] = title
    return result


def _model_routes(root, frozen):
    ref = _frozen_ref(root, frozen, MODEL_ROUTES_PATH)
    value = load_json(_repository_path(root, MODEL_ROUTES_PATH, must_exist=True))
    if not isinstance(value, dict) or set(value) != {
            "route_version", "research", "review", "execution"}:
        raise IssueError("model routes must be a closed version/research/review/execution object")
    if value["route_version"] != "v4.2-neutral-model-routes-1":
        raise IssueError("model route version is invalid")
    if not isinstance(value["research"], dict) or set(value["research"]) != {"target"}:
        raise IssueError("model routes research map must contain only neutral target")
    if not isinstance(value["review"], dict) or set(value["review"]) != {"all"}:
        raise IssueError("model routes review map must contain exactly all")
    if not isinstance(value["execution"], dict) or set(value["execution"]) != {
            "fork_policy", "issued_by_task_path", "research_role", "review_role"}:
        raise IssueError("model routes execution map is not closed")
    models = [value["research"]["target"], value["review"]["all"]]
    if not all(isinstance(item, str) and item.strip() for item in models):
        raise IssueError("every frozen model route must be a non-empty string")
    execution = value["execution"]
    if (execution["fork_policy"] != "none"
            or execution["issued_by_task_path"] != "/root"
            or not isinstance(execution["research_role"], str)
            or not execution["research_role"].strip()
            or not isinstance(execution["review_role"], str)
            or not execution["review_role"].strip()
            or execution["research_role"] == execution["review_role"]):
        raise IssueError("frozen execution route must be root-issued, fork-none, with distinct roles")
    return value, ref


def _membership(root, frozen, scope):
    if scope == "regression":
        ref = _frozen_ref(root, frozen, REGRESSION_PATH)
        value = load_json(_repository_path(root, REGRESSION_PATH, must_exist=True))
        if not isinstance(value, dict) or set(value) != {
                "membership_version", "purpose", "selected_codes", "selection_rule"}:
            raise IssueError("regression membership contract is not closed")
        if (value["membership_version"] != "v4.2-regression-1"
                or value["selected_codes"] != list(REGRESSION_CODES)
                or not isinstance(value["purpose"], str) or not value["purpose"].strip()
                or not isinstance(value["selection_rule"], str) or not value["selection_rule"].strip()):
            raise IssueError("regression membership does not equal the preregistered exact five")
        return list(REGRESSION_CODES), ref, None
    ref = _frozen_ref(root, frozen, HOLDOUT_PATH)
    value = load_json(_repository_path(root, HOLDOUT_PATH, must_exist=True))
    selected = value.get("selected_codes") if isinstance(value, dict) else None
    if (not isinstance(selected, list) or len(selected) != HOLDOUT_SIZE
            or len(set(selected)) != HOLDOUT_SIZE
            or not all(isinstance(code, str) and re.fullmatch(r"[0-9]{6}", code)
                       for code in selected)
            or set(selected) & set(REGRESSION_CODES)):
        raise IssueError("holdout membership is not an exact disjoint five-code cohort")
    if scope == "holdout":
        return list(selected), None, ref
    targets = _targets(root, frozen)
    codes = sorted(set(targets) - set(REGRESSION_CODES) - set(selected))
    if len(codes) != FULL_SIZE:
        raise IssueError("full Phase-4 membership must contain exactly 53 new codes")
    return codes, _frozen_ref(root, frozen, REGRESSION_PATH), ref


def _artifact_ref(root, relative):
    path = _repository_path(root, relative, must_exist=True)
    return {"path": relative, "sha256": sha256_file(path), "byte_length": path.stat().st_size}


def _validate_full_gate_certificates(root, regression_path, holdout_path, gate_validator=None):
    if regression_path != REGRESSION_GATE_CERTIFICATE_PATH:
        raise IssueError("full issuance requires the canonical regression gate certificate")
    if holdout_path != HOLDOUT_GATE_CERTIFICATE_PATH:
        raise IssueError("full issuance requires the canonical holdout gate certificate")
    refs = {
        "regression_canary": _artifact_ref(root, regression_path),
        "holdout": _artifact_ref(root, holdout_path),
    }
    if gate_validator is None:
        spec = importlib.util.spec_from_file_location(
            "issue_campaign_v4_2_gate_validator", REPO / "pipeline/build/campaign_v4_2.py")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        gate_validator = module._full_gate_certificate_errors
    errors = gate_validator({"full_gate_certificates": refs}, str(root))
    if errors:
        raise IssueError("full gate certificates are not exactly valid: %s" % "; ".join(errors))
    return refs


def _validate_scope_extension(root, manifest_relative, receipt_relative, codes,
                              base_frozen=None, base_commit_sha=None,
                              ci_fetcher=None, verify_live_ci=True,
                              contract_validator=None):
    if manifest_relative != SCOPE_EXTENSION_MANIFEST_PATH:
        raise IssueError("full issuance requires the canonical scope-extension manifest")
    manifest_path = _repository_path(root, manifest_relative, must_exist=True)
    receipt_path = _receipt_path(root, receipt_relative, "scope-extension")
    manifest, receipt = load_json(manifest_path), load_json(receipt_path)
    if manifest_path.read_bytes() != canonical_bytes(manifest) or receipt_path.read_bytes() != canonical_bytes(receipt):
        raise IssueError("scope-extension authority must be canonical JSON")
    if (not isinstance(manifest, dict) or set(manifest) != {
            "extension_version", "purpose", "base_freeze_root_sha256", "codes",
            "files", "root_sha256"}
            or manifest.get("extension_version") != "v4.2-full-scope-extension-1"
            or manifest.get("purpose") != "authorize-post-gate-full-scope-inputs"
            or manifest.get("codes") != sorted(codes)):
        raise IssueError("scope-extension manifest is not the exact closed 53-code contract")
    expected_paths = {"pipeline/prompts_v4_2/%s.md" % code for code in codes} | {
        "pipeline/specs_v4_2/%s.json" % code for code in codes}
    if base_frozen is not None:
        for directory in ("pipeline/prompts_v4_2", "pipeline/specs_v4_2"):
            actual = {
                path.relative_to(root).as_posix()
                for path in (root / directory).iterdir() if path.is_file()
            }
            authorized = {
                relative for relative in set(base_frozen) | expected_paths
                if relative.startswith(directory + "/")
            }
            if actual != authorized:
                raise IssueError("scope-extension %s inventory is not exactly authorized" % directory)
    files = manifest.get("files")
    if (not isinstance(files, list) or {item.get("path") for item in files
                                       if isinstance(item, dict)} != expected_paths):
        raise IssueError("scope-extension manifest does not contain exact prompt/spec paths")
    indexed = {}
    for item in files:
        if set(item) != {"path", "sha256", "byte_length"}:
            raise IssueError("scope-extension file references are not closed")
        path = _repository_path(root, item["path"], must_exist=True)
        if sha256_file(path) != item["sha256"] or path.stat().st_size != item["byte_length"]:
            raise IssueError("scope-extension file differs from signed manifest: %s" % item["path"])
        indexed[item["path"]] = item
    if manifest.get("root_sha256") != _root_sha256(files):
        raise IssueError("scope-extension root digest is stale")
    if (not isinstance(receipt, dict) or set(receipt) != {
            "receipt_version", "kind", "manifest_sha256", "root_sha256", "commit_sha",
            "tag_name", "tag_object_sha", "signed", "signature_verified", "signer_identity",
            "ci_receipt"}
            or receipt.get("receipt_version") != "v4.2-full-scope-extension-receipt-1"
            or receipt.get("kind") != "full_scope_extension"
            or receipt.get("manifest_sha256") != sha256_file(manifest_path)
            or receipt.get("root_sha256") != manifest["root_sha256"]
            or receipt.get("signed") is not True or receipt.get("signature_verified") is not True
            or not isinstance(receipt.get("signer_identity"), str)
            or not receipt["signer_identity"].strip()):
        raise IssueError("scope-extension signed receipt does not bind the manifest")
    ci_ref = receipt.get("ci_receipt")
    if not isinstance(ci_ref, dict) or set(ci_ref) != {"path", "sha256", "byte_length"}:
        raise IssueError("scope-extension receipt lacks an exact external CI receipt")
    ci_path = _receipt_path(root, ci_ref["path"], "scope-extension CI")
    if (sha256_file(ci_path) != ci_ref["sha256"]
            or ci_path.stat().st_size != ci_ref["byte_length"]):
        raise IssueError("scope-extension CI receipt reference is stale")
    ci = load_json(ci_path)
    if (ci.get("root_sha256") != manifest["root_sha256"]
            or ci.get("manifest_sha256") != sha256_file(manifest_path)
            or ci.get("commit_sha") != receipt["commit_sha"]
            or ci.get("tag_name") != receipt["tag_name"]):
        raise IssueError("scope-extension CI receipt does not bind C2/tag/root/manifest")
    if verify_live_ci:
        _verify_live_ci(ci, {"commit_sha": receipt["commit_sha"]},
                        {"tag_name": receipt["tag_name"]}, fetch_json=ci_fetcher,
                        workflow_path=EXTENSION_WORKFLOW_PATH,
                        workflow_name=EXTENSION_WORKFLOW_NAME,
                        artifact_prefix="v4.2-full-scope-")
    commit_sha, tag_object = receipt["commit_sha"], receipt["tag_object_sha"]
    if _git(root, "cat-file", "-t", commit_sha) != "commit" or _git(root, "cat-file", "-t", tag_object) != "tag":
        raise IssueError("scope-extension receipt does not name immutable git objects")
    if _git(root, "rev-parse", "%s^{commit}" % tag_object) != commit_sha:
        raise IssueError("scope-extension signed tag does not peel to its commit")
    if base_commit_sha is not None:
        _git(root, "merge-base", "--is-ancestor", base_commit_sha, commit_sha)
        for relative, ref in sorted((base_frozen or {}).items()):
            blob = _git_bytes(root, "show", "%s:%s" % (commit_sha, relative))
            if len(blob) != ref["byte_length"] or sha256_bytes(blob) != ref["sha256"]:
                raise IssueError("scope-extension commit changes base-freeze member: %s" % relative)
        changed = set(filter(None, _git(root, "diff", "--name-only",
                                       base_commit_sha, commit_sha).splitlines()))
        expected_changed = expected_paths | {manifest_relative}
        if changed != expected_changed:
            raise IssueError("scope-extension commit inventory differs from exact manifest + 106 inputs")
    with _isolated_git_tree(
            root, commit_sha, [manifest_relative, *sorted(indexed)]) as c2_tree:
        if (c2_tree / manifest_relative).read_bytes() != manifest_path.read_bytes():
            raise IssueError("scope-extension commit does not contain its exact manifest")
        for relative, ref in indexed.items():
            blob = (c2_tree / relative).read_bytes()
            if len(blob) != ref["byte_length"] or sha256_bytes(blob) != ref["sha256"]:
                raise IssueError("scope-extension commit does not contain exact input: %s" % relative)
    tag_bytes = _git_bytes(root, "cat-file", "-p", tag_object)
    headers, separator, message = tag_bytes.partition(b"\n\n")
    required_headers = {
        b"object " + commit_sha.encode("ascii"), b"type commit",
        b"tag " + receipt["tag_name"].encode("utf-8"),
    }
    required_message_lines = {
        b"extension-root " + manifest["root_sha256"].encode("ascii"),
    }
    if base_commit_sha is not None:
        required_message_lines.add(b"base-commit " + base_commit_sha.encode("ascii"))
    if (not separator or not required_headers.issubset(set(headers.splitlines()))
            or not required_message_lines.issubset(set(message.splitlines()))):
        raise IssueError("scope-extension tag does not bind C1, C2, name, and extension root")
    _git(root, "-c", "gpg.ssh.allowedSignersFile=pipeline/v4_2/allowed_signers",
         "verify-tag", "--raw", tag_object)
    if contract_validator is None:
        spec = importlib.util.spec_from_file_location(
            "full_scope_extension_v4_2_contract",
            REPO / "pipeline/build/validate_full_scope_extension_v4_2.py")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        contract_validator = module.validate
    contract_result = contract_validator(root, base_commit_sha)
    if (contract_result.get("codes") != sorted(codes)
            or contract_result.get("root_sha256") != manifest["root_sha256"]):
        raise IssueError("dedicated C2 semantic contract differs from signed extension")
    return indexed, {"manifest": _artifact_ref(root, manifest_relative),
                     "receipt": _external_ref(receipt_path, receipt_relative),
                     "ci_receipt": ci_ref,
                     "root_sha256": manifest["root_sha256"],
                     "commit_sha": commit_sha}


def _planned_paths(scope, code, run_id):
    base = "pipeline/v4_2"
    return {
        "packet": "%s/packets/%s.json" % (base, run_id),
        "execution_envelope": "%s/envelopes/%s.json" % (base, run_id),
        "record": "%s/runs/%s.json" % (base, run_id),
        "memo": "%s/memos/%s.md" % (base, run_id),
        "review": "%s/reviews/%s.json" % (base, run_id),
    }


def _opaque_id(seed, label, forbidden=()):
    """Derive a stable public identifier without embedding campaign/scope labels."""
    counter = 0
    while True:
        token = sha256_bytes((seed + "\0" + label + "\0" + str(counter)).encode("utf-8"))[:24]
        lowered = token.lower()
        if not any(value and value.lower() in lowered for value in forbidden):
            return token
        counter += 1


def _reservation_bytes(campaign_id, entry_id, run_id, output_kind, output_path,
                       authorized_task_path, freeze_root_sha256,
                       authorized_commit_sha, claim_token_sha256):
    return canonical_bytes({
        "reservation_version": RESERVATION_VERSION,
        "campaign_id": campaign_id,
        "entry_id": entry_id,
        "run_id": run_id,
        "output_kind": output_kind,
        "output_path": output_path,
        "authorized_task_path": authorized_task_path,
        "freeze_root_sha256": freeze_root_sha256,
        "authorized_commit_sha": authorized_commit_sha,
        "claim_token_sha256": claim_token_sha256,
        "claim_policy": "guarded_atomic_claim_consume_v4_2",
    })


def _entry_reservations(campaign_id, entry_id, run_id, planned,
                        research_task_path, finalizer_task_path, review_task_path,
                        freeze_root_sha256, authorized_commit_sha,
                        claim_token_commitments):
    owners = {
        "packet": research_task_path,
        "record": finalizer_task_path,
        "memo": finalizer_task_path,
        "review": review_task_path,
    }
    result = {}
    for kind, owner in owners.items():
        output_path = planned[kind]
        content = _reservation_bytes(
            campaign_id, entry_id, run_id, kind, output_path, owner,
            freeze_root_sha256, authorized_commit_sha,
            claim_token_commitments[kind])
        result[kind] = {
            "path": output_path + ".reservation.json",
            "sha256": sha256_bytes(content),
            "byte_length": len(content),
            "lock_path": output_path + ".claim.lock",
            "claim_receipt_path": output_path + ".claim-receipt.json",
            "claim_token_sha256": claim_token_commitments[kind],
        }
    return result


def _reservation_files(plan):
    files = {}
    for entry in plan["entries"]:
        expected = _entry_reservations(
            plan["campaign_id"], entry["entry_id"], entry["run_id"],
            entry["planned_outputs"],
            entry["research_execution"]["codex_task_path"],
            entry["finalizer_execution"]["codex_task_path"],
            entry["review_execution"]["codex_task_path"],
            plan["freeze"]["root_sha256"], plan["authorization"]["commit_sha"],
            {kind: entry["output_reservations"][kind]["claim_token_sha256"]
             for kind in ("packet", "record", "memo", "review")},
        )
        if entry.get("output_reservations") != expected:
            raise IssueError("entry output reservation references are stale")
        for kind, ref in expected.items():
            content = _reservation_bytes(
                plan["campaign_id"], entry["entry_id"], entry["run_id"], kind,
                entry["planned_outputs"][kind],
                ({"packet": entry["research_execution"]["codex_task_path"],
                  "record": entry["finalizer_execution"]["codex_task_path"],
                  "memo": entry["finalizer_execution"]["codex_task_path"],
                  "review": entry["review_execution"]["codex_task_path"]}
                 [kind]),
                plan["freeze"]["root_sha256"], plan["authorization"]["commit_sha"],
                ref["claim_token_sha256"],
            )
            if ref["path"] in files:
                raise IssueError("output reservation paths must be globally unique")
            files[ref["path"]] = content
    return files


def _claim_execution(entry, kind):
    role = {
        "packet": "research_execution",
        "record": "finalizer_execution",
        "memo": "finalizer_execution",
        "review": "review_execution",
    }.get(kind)
    if role is None:
        raise IssueError("unsupported output artifact kind: %s" % kind)
    execution = entry.get(role)
    if not isinstance(execution, dict):
        raise IssueError("entry is missing %s" % role)
    return execution


def claim_receipt_bytes(plan, plan_path, entry, kind, artifact_bytes):
    """Return the exact receipt that proves one reservation was consumed."""
    if kind not in ("packet", "record", "memo", "review"):
        raise IssueError("unsupported output artifact kind: %s" % kind)
    reservation = entry["output_reservations"][kind]
    output_path = entry["planned_outputs"][kind]
    return canonical_bytes({
        "claim_receipt_version": CLAIM_RECEIPT_VERSION,
        "plan": {
            "path": plan_path,
            "sha256": sha256_bytes(canonical_bytes(plan)),
            "plan_sha256": plan["plan_sha256"],
        },
        "campaign_id": plan["campaign_id"],
        "entry_id": entry["entry_id"],
        "run_id": entry["run_id"],
        "artifact_kind": kind,
        "artifact": {
            "path": output_path,
            "sha256": sha256_bytes(artifact_bytes),
            "byte_length": len(artifact_bytes),
        },
        "authorized_task_path": _claim_execution(entry, kind)["codex_task_path"],
        "execution": _claim_execution(entry, kind),
        "execution_envelope": entry["execution_envelope"],
        "reservation": reservation,
        "freeze_root_sha256": plan["freeze"]["root_sha256"],
        "authorized_commit_sha": plan["authorization"]["commit_sha"],
    })


def _validate_output_claim_states(root, plan_path, plan, entries=None):
    errors = []
    for entry in plan["entries"] if entries is None else entries:
        for kind in ("packet", "record", "memo", "review"):
            ref = entry["output_reservations"][kind]
            output = _repository_path(root, entry["planned_outputs"][kind])
            reservation = _repository_path(root, ref["path"])
            lock = _repository_path(root, ref["lock_path"])
            receipt = _repository_path(root, ref["claim_receipt_path"])
            present = {
                "output": output.is_file(),
                "reservation": reservation.is_file(),
                "lock": lock.exists(),
                "receipt": receipt.is_file(),
            }
            label = "%s/%s" % (entry["entry_id"], kind)
            if present == {"output": False, "reservation": True,
                           "lock": False, "receipt": False}:
                expected = _reservation_bytes(
                    plan["campaign_id"], entry["entry_id"], entry["run_id"],
                    kind, entry["planned_outputs"][kind],
                    _claim_execution(entry, kind)["codex_task_path"],
                    plan["freeze"]["root_sha256"],
                    plan["authorization"]["commit_sha"],
                    ref["claim_token_sha256"],
                )
                try:
                    if reservation.read_bytes() != expected:
                        errors.append("output reservation bytes differ from the issued plan: %s" % ref["path"])
                except OSError as exc:
                    errors.append("output reservation validation failed for %s: %s" % (ref["path"], exc))
                continue
            if present == {"output": True, "reservation": False,
                           "lock": False, "receipt": True}:
                try:
                    artifact_bytes = output.read_bytes()
                    expected = claim_receipt_bytes(plan, plan_path, entry, kind, artifact_bytes)
                    if receipt.read_bytes() != expected:
                        errors.append("output claim receipt differs from artifact and issued plan: %s" % ref["claim_receipt_path"])
                except OSError as exc:
                    errors.append("output claim receipt validation failed for %s: %s" % (label, exc))
                continue
            errors.append(
                "output claim state is neither reserved nor atomically consumed for %s: %s"
                % (label, present))
    return errors


def _plan_digest(plan):
    value = dict(plan)
    value.pop("plan_sha256", None)
    return sha256_bytes(canonical_bytes(value))


def _validate_global_task_paths(entries):
    paths = []
    for entry in entries:
        for role in ("research_execution", "finalizer_execution", "review_execution"):
            execution = entry.get(role)
            path = execution.get("codex_task_path") if isinstance(execution, dict) else None
            if not isinstance(path, str) or not re.fullmatch(r"/root/[a-z0-9_]+", path):
                raise IssueError("every research/finalizer/reviewer execution requires an exact child task path")
            paths.append(path)
    if len(paths) != len(set(paths)):
        raise IssueError("research, finalizer, and reviewer task paths must be globally unique")


def _claim_commitment_set(entry_id, supplied=None, credential_sink=None):
    kinds = ("packet", "record", "memo", "review")
    if supplied is None:
        tokens = {kind: secrets.token_urlsafe(32) for kind in kinds}
        commitments = {kind: sha256_bytes(tokens[kind].encode("utf-8")) for kind in kinds}
        if credential_sink is not None:
            credential_sink[entry_id] = tokens
        return commitments
    if (not isinstance(supplied, dict) or set(supplied) != set(kinds)
            or not all(isinstance(value, str) and re.fullmatch(r"[0-9a-f]{64}", value)
                       for value in supplied.values())):
        raise IssueError("claim token commitments must be exact per-artifact SHA-256 values")
    return dict(supplied)


@contextmanager
def _isolated_git_tree(root, commit_sha, paths):
    """Materialize an immutable regular-file-only git view for validation."""
    if (not isinstance(paths, (list, tuple)) or not paths
            or any(not isinstance(path, str) or not path for path in paths)):
        raise IssueError("isolated git validation requires exact paths")
    result = subprocess.run(
        ["git", "-C", str(root), "archive", "--format=tar", commit_sha, "--", *paths],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)
    if result.returncode:
        raise IssueError("cannot materialize authorized git tree: %s" %
                         result.stderr.decode("utf-8", errors="replace").strip())
    with tempfile.TemporaryDirectory(prefix="v4_2_c1_") as temporary:
        snapshot = Path(temporary).resolve()
        with tarfile.open(fileobj=io.BytesIO(result.stdout), mode="r:") as archive:
            for member in archive.getmembers():
                parts = member.name.split("/")
                if (member.name.startswith("/") or any(part in ("", ".", "..") for part in parts)
                        or not (member.isdir() or member.isfile())):
                    raise IssueError("git archive contains an unsafe member: %s" % member.name)
            archive.extractall(snapshot, filter="data")
        yield snapshot


def _git_runner_at(repository_root, snapshot_root=None, snapshot_commit=None):
    def runner(_validation_root, args):
        prefix = (snapshot_commit + ":") if snapshot_commit else None
        if snapshot_root is not None and len(args) >= 2:
            spec = args[-1]
            if isinstance(spec, str) and prefix and spec.startswith(prefix):
                relative = spec[len(prefix):]
                path = Path(snapshot_root) / relative
                if args[0] == "show" and path.is_file():
                    return SimpleNamespace(returncode=0, stdout=path.read_bytes(), stderr=b"")
                if args[:2] == ["cat-file", "-t"] and path.is_file():
                    return SimpleNamespace(returncode=0, stdout=b"blob\n", stderr=b"")
        return subprocess.run(
            ["git", "-C", str(repository_root), *args],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)
    return runner


def build_issuance(
        root, scope, campaign_id, run_date, freeze_manifest,
        commit_receipt, tag_receipt, ci_receipt, *, ci_fetcher=None,
        verify_live_ci=True, regression_gate_certificate=None,
        holdout_gate_certificate=None, gate_validator=None,
        scope_extension_manifest=None, scope_extension_receipt=None,
        claim_commitments=None, credential_sink=None,
        extension_contract_validator=None):
    root = Path(root).resolve()
    if freeze_manifest != FREEZE_MANIFEST_PATH:
        raise IssueError("freeze manifest path must be exactly %s" % FREEZE_MANIFEST_PATH)
    if scope not in ("regression", "holdout", "full"):
        raise IssueError("scope must be regression, holdout, or full")
    if not re.fullmatch(r"[a-z0-9]+(?:[-_][a-z0-9]+)*", campaign_id or ""):
        raise IssueError("campaign_id must be lowercase alphanumeric with '-' or '_' separators")
    try:
        parsed_date = date.fromisoformat(run_date)
    except (TypeError, ValueError) as exc:
        raise IssueError("run_date must be a real ISO date") from exc
    if parsed_date > date.today():
        raise IssueError("run_date cannot be in the future")

    manifest, frozen, freeze_ref = validate_freeze(root, freeze_manifest)
    toolchain = {
        key: _frozen_ref(root, frozen, relative)
        for key, relative in sorted(TOOLCHAIN_PATHS.items())
    }
    routes, routes_ref = _model_routes(root, frozen)
    execution_route = routes["execution"]
    research_model_id = routes["research"]["target"]
    review_model_id = routes["review"]["all"]
    targets = _targets(root, frozen)
    codes, regression_ref, holdout_ref = _membership(root, frozen, scope)
    extension_files, scope_extension = {}, None
    full_gate_certificates = None
    if scope == "full":
        base_commit_value = load_json(
            _receipt_path(root, commit_receipt, "commit")).get("commit_sha")
        extension_receipt_value = load_json(
            _receipt_path(root, scope_extension_receipt, "scope-extension"))
        extension_head_sha = extension_receipt_value.get("commit_sha")
        # Establish the exact signed C2 inventory before invoking the C1
        # current-tree completeness contract, which intentionally forbids it.
        extension_files, scope_extension = _validate_scope_extension(
            root, scope_extension_manifest, scope_extension_receipt, codes,
            base_frozen=frozen, base_commit_sha=base_commit_value,
            ci_fetcher=ci_fetcher, verify_live_ci=verify_live_ci,
            contract_validator=extension_contract_validator)
        extension_manifest = load_json(_repository_path(root, scope_extension_manifest, must_exist=True))
        if extension_manifest["base_freeze_root_sha256"] != freeze_ref["root_sha256"]:
            raise IssueError("scope extension does not bind the base freeze root")
        with _isolated_git_tree(
                root, base_commit_value, [freeze_manifest, *sorted(frozen)]) as c1_root:
            authorization = _authorization_evidence(
                root, freeze_manifest, manifest, frozen,
                commit_receipt, tag_receipt, ci_receipt, ci_fetcher=ci_fetcher,
                verify_live_ci=verify_live_ci, authorized_head_sha=extension_head_sha,
                validation_root=c1_root,
                git_runner=_git_runner_at(root, c1_root, base_commit_value))
        full_gate_certificates = _validate_full_gate_certificates(
            root, regression_gate_certificate, holdout_gate_certificate,
            gate_validator=gate_validator)
    else:
        if regression_gate_certificate is not None or holdout_gate_certificate is not None:
            raise IssueError("gate certificates may be supplied only for full issuance")
        authorization = _authorization_evidence(
            root, freeze_manifest, manifest, frozen,
            commit_receipt, tag_receipt, ci_receipt, ci_fetcher=ci_fetcher,
            verify_live_ci=verify_live_ci)
    freeze_ref["git_commit"] = authorization["commit_sha"]
    missing = sorted(set(codes) - set(targets))
    if missing:
        raise IssueError("scope membership is absent from frozen target universe: %s" % missing)

    entries, envelopes = [], {}
    seen_run_ids, seen_tasks, seen_outputs = set(), set(), set()
    for code in codes:
        title = targets[code]
        prompt_path = "pipeline/prompts_v4_2/%s.md" % code
        spec_path = "pipeline/specs_v4_2/%s.json" % code
        input_authority = dict(frozen)
        input_authority.update(extension_files)
        prompt_ref = _frozen_ref(root, input_authority, prompt_path)
        spec_ref = _frozen_ref(root, input_authority, spec_path)
        spec = load_json(_repository_path(root, spec_path, must_exist=True))
        if spec.get("spec_version") != "4.2" or spec.get("naics") != code or spec.get("title") != title:
            raise IssueError("industry spec identity mismatch for %s" % code)
        if spec.get("methodology_snapshot") != {
                "path": TOOLCHAIN_PATHS["methodology"],
                "sha256": toolchain["methodology"]["sha256"]}:
            raise IssueError("industry spec runtime-methodology binding mismatch for %s" % code)
        snapshot = spec.get("dataset_snapshot")
        if not isinstance(snapshot, dict) or set(snapshot) != {"path", "sha256"}:
            raise IssueError("industry spec dataset_snapshot is not closed for %s" % code)
        expected_dataset = "pipeline/datasets/v4_2/%s.json" % code
        if snapshot["path"] != expected_dataset:
            raise IssueError("industry spec dataset path mismatch for %s" % code)
        dataset_ref = _frozen_ref(root, frozen, expected_dataset)
        if snapshot["sha256"] != dataset_ref["sha256"]:
            raise IssueError("industry spec dataset digest mismatch for %s" % code)
        dataset = load_json(_repository_path(root, expected_dataset, must_exist=True))
        if dataset.get("dataset_version") != "4.2" or dataset.get("naics") != code or dataset.get("title") != title:
            raise IssueError("normalized dataset identity mismatch for %s" % code)

        opaque_seed = "\0".join((
            PLAN_VERSION, campaign_id, scope, run_date, code,
            freeze_ref["root_sha256"], authorization["commit_sha"],
        ))
        forbidden_tokens = (campaign_id, scope, "regression", "holdout", "full")
        public_id = _opaque_id(opaque_seed, "public-attempt-1", forbidden_tokens)
        run_id = "v42_%s_a1" % public_id
        task_root = execution_route["issued_by_task_path"]
        task_path = "%s/research_v4_2_%s_a1" % (task_root, public_id)
        finalizer_task_path = "%s/finalize_v4_2_%s_a1" % (task_root, public_id)
        review_task_path = "%s/review_v4_2_%s_a1" % (task_root, public_id)
        planned = _planned_paths(scope, code, run_id)
        if (run_id in seen_run_ids or task_path in seen_tasks
                or finalizer_task_path in seen_tasks or review_task_path in seen_tasks):
            raise IssueError("run IDs and execution task paths must be unique")
        if set(planned.values()) & seen_outputs:
            raise IssueError("planned artifact paths must be unique")
        seen_run_ids.add(run_id)
        seen_tasks.add(task_path)
        seen_tasks.add(finalizer_task_path)
        seen_tasks.add(review_task_path)
        seen_outputs.update(planned.values())

        envelope = {
            "envelope_version": "4.2",
            "kind": "target",
            "naics": code,
            "title": title,
            "run_id": run_id,
            "run_date": run_date,
            "attempt": 1,
            "remediates_run_id": None,
            "issued_by_task_path": execution_route["issued_by_task_path"],
            "codex_task_path": task_path,
            "fork_policy": execution_route["fork_policy"],
            "role": execution_route["research_role"],
            "model_id": research_model_id,
            "prompt_sha256": prompt_ref["sha256"],
            "dataset_sha256": dataset_ref["sha256"],
            "spec_sha256": spec_ref["sha256"],
        }
        for key, relative in ENVELOPE_HASH_PATHS.items():
            envelope[key] = frozen[relative]["sha256"]
        envelope_bytes = canonical_bytes(envelope)
        envelopes[planned["execution_envelope"]] = envelope_bytes
        entry_id = "entry_v42_%s_a1" % public_id
        entry = {
            "entry_id": entry_id,
            "kind": "target",
            "naics": code,
            "title": title,
            "run_id": run_id,
            "run_date": run_date,
            "attempt": 1,
            "remediates_run_id": None,
            "research_execution": {
                "issued_by_task_path": execution_route["issued_by_task_path"],
                "codex_task_path": task_path,
                "fork_policy": execution_route["fork_policy"],
                "role": execution_route["research_role"],
                "model_id": research_model_id,
            },
            "finalizer_execution": {
                "issued_by_task_path": execution_route["issued_by_task_path"],
                "codex_task_path": finalizer_task_path,
                "fork_policy": "none",
                "role": "finalizer",
            },
            "review_execution": {
                "issued_by_task_path": execution_route["issued_by_task_path"],
                "codex_task_path": review_task_path,
                "fork_policy": execution_route["fork_policy"],
                "role": execution_route["review_role"],
                "model_id": review_model_id,
                "prompt_version": REVIEW_PROMPT_VERSION,
            },
            "frozen_inputs": {
                "assembled_prompt": prompt_ref,
                "industry_spec": spec_ref,
                "dataset": dataset_ref,
            },
            "execution_envelope": {
                "path": planned["execution_envelope"],
                "sha256": sha256_bytes(envelope_bytes),
                "byte_length": len(envelope_bytes),
            },
            "planned_outputs": planned,
        }
        if claim_commitments is not None and entry_id not in claim_commitments:
            raise IssueError("claim token commitments omit an issued entry")
        supplied_commitments = None if claim_commitments is None else claim_commitments[entry_id]
        commitments = _claim_commitment_set(
            entry_id, supplied=supplied_commitments, credential_sink=credential_sink)
        entry["output_reservations"] = _entry_reservations(
            campaign_id, entry_id, run_id, planned, task_path,
            finalizer_task_path, review_task_path, freeze_ref["root_sha256"],
            authorization["commit_sha"], commitments,
        )
        entries.append(entry)

    if claim_commitments is not None and set(claim_commitments) != {entry["entry_id"] for entry in entries}:
        raise IssueError("claim token commitments contain an unknown issued entry")
    _validate_global_task_paths(entries)
    plan = {
        "plan_version": PLAN_VERSION,
        "campaign_id": campaign_id,
        "scope": scope,
        "issued_by_task_path": execution_route["issued_by_task_path"],
        "run_date": run_date,
        "prompt_version": PROMPT_VERSION,
        "research_model_id": research_model_id,
        "review_model_id": review_model_id,
        "review_prompt_version": REVIEW_PROMPT_VERSION,
        "model_routes": routes_ref,
        "freeze": freeze_ref,
        "authorization": authorization,
        "membership": {
            "codes": codes,
            "regression_manifest": regression_ref,
            "holdout_manifest": holdout_ref,
            "target_universe": _frozen_ref(root, frozen, TARGETS_PATH),
            "full_gate_certificates": full_gate_certificates,
            "scope_extension": scope_extension,
        },
        "toolchain": toolchain,
        "entries": entries,
        "predecessor_plan": None,
        "remediation_authorization": None,
    }
    plan["plan_sha256"] = _plan_digest(plan)
    return plan, envelopes


def _remediable_paths(review):
    paths = set()
    if any(isinstance(item, dict) and item.get("severity") == "fatal_mechanics"
           for item in review.get("findings", [])):
        raise IssueError("fatal-mechanics reviews are terminal and not remediable")
    material = [item for item in review.get("findings", [])
                if isinstance(item, dict) and item.get("severity") == "material"]
    if not material:
        raise IssueError("rejected review has no material remediable finding")
    allowed = set(VALUE for VALUE in (
        "inputs.recognized_revenue", "inputs.employee_cash_cost",
        "inputs.controllable_contractor_cash_cost", "inputs.target_archetype_coverage",
        "inputs.five_year_sale_availability", "inputs.buyer_access_win_share",
        "inputs.deal_execution_capacity_5y", "inputs.integration_onboarding_capacity_5y",
        "inputs.buy_mult", "inputs.normalized_y5_operating_state",
        "inputs.downside_exit_mult", "inputs.operator_controlled_value_added_demand_share_y5",
    ))
    schedule = re.compile(
        r"^inputs\.(?:implementation_realization\.r[1-5]|implementation_investment\.k[0-5]|commercial_retention\.c[1-5])$")
    for finding in material:
        item_paths = finding.get("input_paths")
        if not isinstance(item_paths, list) or not item_paths:
            raise IssueError("every material remediation finding requires exact input_paths")
        for path in item_paths:
            if path not in allowed and not schedule.fullmatch(path or ""):
                raise IssueError("finding path is not a remediable v4.2 primitive: %s" % path)
            paths.add(path)
    return sorted(paths), material


def _validate_predecessor_review(root, campaign_path, plan_path, entry, review,
                                 campaign_module=None):
    campaign = campaign_module
    if campaign is None:
        spec = importlib.util.spec_from_file_location(
            "remediation_campaign_v4_2_validator", REPO / "pipeline/build/campaign_v4_2.py")
        campaign = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(campaign)
    manifest_file = _repository_path(root, campaign_path, must_exist=True)
    manifest = load_json(manifest_file)
    if manifest_file.read_bytes() != canonical_bytes(manifest):
        raise IssueError("predecessor campaign manifest must be canonical JSON")
    manifest_errors = campaign.validate_manifest(manifest, str(root))
    if manifest_errors:
        raise IssueError("predecessor campaign manifest is invalid: %s" % "; ".join(manifest_errors))
    plan_ref = manifest.get("issuance_plan", {})
    plan_file = _repository_path(root, plan_path, must_exist=True)
    if (plan_ref.get("path") != plan_path or plan_ref.get("sha256") != sha256_file(plan_file)
            or plan_ref.get("byte_length") != plan_file.stat().st_size):
        raise IssueError("predecessor campaign does not bind the exact issuance plan")
    matches = [item for item in manifest.get("entries", [])
               if isinstance(item, dict) and item.get("entry_id") == entry["entry_id"]]
    if len(matches) != 1:
        raise IssueError("predecessor campaign must contain the exact issued entry")
    errors = campaign.review_errors(review, matches[0], manifest, str(root))
    if errors:
        raise IssueError("predecessor review is not exactly valid: %s" % "; ".join(errors))
    if review.get("outcome") != "reject" or campaign.computed_outcome(matches[0], review) != "reject":
        raise IssueError("only an exactly computed reject review is remediable")
    return manifest, matches[0]


def build_remediation_issuance(root, predecessor_plan_path, predecessor_campaign_path,
                               predecessor_entry_id,
                               predecessor_run_sha256, predecessor_review_sha256,
                               claim_commitments=None, credential_sink=None):
    """Build one deterministic attempt-2 amendment from an exact rejected attempt 1."""
    root = Path(root).resolve()
    predecessor, errors = validate_issued_plan(root, predecessor_plan_path)
    if errors:
        raise IssueError("predecessor issuance plan is not accepted: %s" % "; ".join(errors))
    if (predecessor.get("plan_version") != PLAN_VERSION
            or predecessor.get("predecessor_plan") is not None):
        raise IssueError("attempt 2 must directly remediate an original attempt-1 plan")
    matches = [item for item in predecessor["entries"]
               if item.get("entry_id") == predecessor_entry_id and item.get("attempt") == 1]
    if len(matches) != 1:
        raise IssueError("predecessor entry must be one exact attempt 1")
    first = matches[0]
    run_path = _repository_path(root, first["planned_outputs"]["record"], must_exist=True)
    review_path = _repository_path(root, first["planned_outputs"]["review"], must_exist=True)
    if sha256_file(run_path) != predecessor_run_sha256:
        raise IssueError("predecessor run digest mismatch")
    if sha256_file(review_path) != predecessor_review_sha256:
        raise IssueError("predecessor review digest mismatch")
    review = load_json(review_path)
    _validate_predecessor_review(
        root, predecessor_campaign_path, predecessor_plan_path, first, review)
    remediable_paths, findings = _remediable_paths(review)
    bundle = {
        "predecessor_entry_id": first["entry_id"],
        "predecessor_review_sha256": predecessor_review_sha256,
        "findings": findings,
    }
    bundle_bytes = canonical_bytes(bundle)

    seed = "\0".join((predecessor["plan_sha256"], first["entry_id"],
                       predecessor_run_sha256, predecessor_review_sha256))
    public_id = _opaque_id(seed, "public-attempt-2", ("regression", "holdout", "full"))
    run_id = "v42_%s_a2" % public_id
    task_root = predecessor["issued_by_task_path"]
    research_task = "%s/research_v4_2_%s_a2" % (task_root, public_id)
    finalizer_task = "%s/finalize_v4_2_%s_a2" % (task_root, public_id)
    review_task = "%s/review_v4_2_%s_a2" % (task_root, public_id)
    planned = _planned_paths(predecessor["scope"], first["naics"], run_id)
    envelope = load_json(_repository_path(
        root, first["execution_envelope"]["path"], must_exist=True))
    envelope.update({
        "run_id": run_id, "attempt": 2, "remediates_run_id": first["run_id"],
        "codex_task_path": research_task,
    })
    envelope_bytes = canonical_bytes(envelope)
    entry_id = "entry_v42_%s_a2" % public_id
    second = {
        "entry_id": entry_id, "kind": first["kind"], "naics": first["naics"],
        "title": first["title"], "run_id": run_id, "run_date": first["run_date"],
        "attempt": 2, "remediates_run_id": first["run_id"],
        "remediates_entry_id": first["entry_id"],
        "predecessor_review_sha256": predecessor_review_sha256,
        "predecessor_run_sha256": predecessor_run_sha256,
        "remediable_paths": remediable_paths,
        "research_execution": {**first["research_execution"], "codex_task_path": research_task},
        "finalizer_execution": {**first["finalizer_execution"], "codex_task_path": finalizer_task},
        "review_execution": {**first["review_execution"], "codex_task_path": review_task},
        "frozen_inputs": first["frozen_inputs"],
        "execution_envelope": {"path": planned["execution_envelope"],
                               "sha256": sha256_bytes(envelope_bytes),
                               "byte_length": len(envelope_bytes)},
        "planned_outputs": planned,
    }
    bundle_path = "pipeline/v4_2/remediations/%s.json" % run_id
    second["remediation_bundle"] = {
        "path": bundle_path, "sha256": sha256_bytes(bundle_bytes),
        "byte_length": len(bundle_bytes),
    }
    commitments = _claim_commitment_set(
        entry_id, supplied=claim_commitments, credential_sink=credential_sink)
    second["output_reservations"] = _entry_reservations(
        predecessor["campaign_id"], entry_id, run_id, planned,
        research_task, finalizer_task, review_task,
        predecessor["freeze"]["root_sha256"], predecessor["authorization"]["commit_sha"],
        commitments)
    plan = json.loads(json.dumps(predecessor))
    plan["plan_version"] = REMEDIATION_PLAN_VERSION
    plan["predecessor_plan"] = _artifact_ref(root, predecessor_plan_path)
    plan["remediation_authorization"] = {
        "predecessor_entry_id": first["entry_id"],
        "predecessor_run": _artifact_ref(root, first["planned_outputs"]["record"]),
        "predecessor_review": _artifact_ref(root, first["planned_outputs"]["review"]),
        "remediable_paths": remediable_paths,
        "remediation_bundle": second["remediation_bundle"],
        "predecessor_campaign": _artifact_ref(root, predecessor_campaign_path),
    }
    plan["entries"].append(second)
    _validate_global_task_paths(plan["entries"])
    plan["plan_sha256"] = _plan_digest(plan)
    return plan, {planned["execution_envelope"]: envelope_bytes}, {bundle_path: bundle_bytes}


def validate_issued_plan(root, plan_path, expected_scope=None, *, ci_fetcher=None):
    """Reopen and fully reproduce an issued plan for downstream consumers.

    Returns ``(plan, errors)`` and does not raise for invalid external input.
    Successful validation also proves every on-disk execution envelope and
    every output is either exactly reserved or has an exact artifact-hash-bound
    claim receipt. Live CI is intentionally not re-fetched: its issuance-time
    receipt remains immutable after GitHub artifact expiry.
    """
    root = Path(root).resolve()
    try:
        absolute = _repository_path(root, plan_path, must_exist=True)
        raw = absolute.read_bytes()
        plan = load_json(absolute)
        if not isinstance(plan, dict):
            raise IssueError("issued plan must be a JSON object")
        required_keys = {
            "plan_version", "campaign_id", "scope", "issued_by_task_path",
            "run_date", "prompt_version", "research_model_id", "review_model_id",
            "review_prompt_version", "model_routes", "freeze", "authorization",
            "membership", "toolchain", "entries", "plan_sha256",
            "predecessor_plan", "remediation_authorization",
        }
        if set(plan) != required_keys:
            raise IssueError("issued plan top-level keys are not closed")
        if raw != canonical_bytes(plan):
            raise IssueError("issued plan bytes are not canonical JSON")
        if plan.get("plan_version") not in (PLAN_VERSION, REMEDIATION_PLAN_VERSION):
            raise IssueError("issued plan version is not an accepted v4.2 issuance version")
        if plan.get("plan_sha256") != _plan_digest(plan):
            raise IssueError("issued plan self-digest is stale")
        if expected_scope is not None and plan.get("scope") != expected_scope:
            raise IssueError("issued plan scope does not match the campaign scope")
        if plan["plan_version"] == REMEDIATION_PLAN_VERSION:
            predecessor_ref = plan.get("predecessor_plan")
            remediation = plan.get("remediation_authorization")
            if (not isinstance(predecessor_ref, dict)
                    or set(predecessor_ref) != {"path", "sha256", "byte_length"}
                    or not isinstance(remediation, dict)
                    or set(remediation) != {"predecessor_entry_id", "predecessor_run",
                                            "predecessor_review", "remediable_paths",
                                            "remediation_bundle", "predecessor_campaign"}):
                raise IssueError("remediation issuance bindings are not closed")
            expected, envelopes, bundles = build_remediation_issuance(
                root, predecessor_ref["path"], remediation["predecessor_campaign"]["path"],
                remediation["predecessor_entry_id"],
                remediation["predecessor_run"]["sha256"],
                remediation["predecessor_review"]["sha256"],
                claim_commitments={
                    kind: plan["entries"][-1]["output_reservations"][kind]["claim_token_sha256"]
                    for kind in ("packet", "record", "memo", "review")})
            errors = []
            if plan != expected:
                errors.append("remediation plan differs from exact predecessor/review bindings")
            for relative, content in {**envelopes, **bundles}.items():
                try:
                    if _repository_path(root, relative, must_exist=True).read_bytes() != content:
                        errors.append("remediation issuance artifact bytes differ: %s" % relative)
                except (IssueError, OSError) as exc:
                    errors.append("remediation issuance artifact validation failed: %s" % exc)
            errors.extend(_validate_output_claim_states(root, plan_path, expected,
                                                        entries=[expected["entries"][-1]]))
            return plan, errors
        if plan.get("predecessor_plan") is not None or plan.get("remediation_authorization") is not None:
            raise IssueError("attempt-1 plan may not contain remediation bindings")
        authorization = plan.get("authorization")
        if not isinstance(authorization, dict):
            raise IssueError("issued plan authorization binding is missing")
        receipt_paths = []
        for key in ("commit_receipt", "tag_receipt", "ci_receipt"):
            ref = authorization.get(key)
            if not isinstance(ref, dict) or set(ref) != {"path", "sha256", "byte_length"}:
                raise IssueError("issued plan %s reference is not closed" % key)
            receipt_paths.append(ref["path"])

        commitments = {
            entry["entry_id"]: {
                kind: entry["output_reservations"][kind]["claim_token_sha256"]
                for kind in ("packet", "record", "memo", "review")}
            for entry in plan["entries"]
        }
        expected, envelopes = build_issuance(
            root, plan["scope"], plan["campaign_id"], plan["run_date"],
            plan["freeze"]["path"], *receipt_paths, ci_fetcher=ci_fetcher,
            verify_live_ci=False,
            regression_gate_certificate=(REGRESSION_GATE_CERTIFICATE_PATH
                                         if plan["scope"] == "full" else None),
            holdout_gate_certificate=(HOLDOUT_GATE_CERTIFICATE_PATH
                                      if plan["scope"] == "full" else None),
            scope_extension_manifest=(SCOPE_EXTENSION_MANIFEST_PATH
                                      if plan["scope"] == "full" else None),
            scope_extension_receipt=(plan.get("membership", {}).get(
                "scope_extension", {}).get("receipt", {}).get("path")
                                     if plan["scope"] == "full" else None),
            claim_commitments=commitments,
        )
        errors = []
        if plan != expected:
            errors.append("issued plan differs from its exact reconstructed frozen bindings")
        for relative, content in sorted(envelopes.items()):
            try:
                path = _repository_path(root, relative, must_exist=True)
                if path.read_bytes() != content:
                    errors.append("execution envelope bytes differ from the issued plan: %s" % relative)
            except (IssueError, OSError, UnicodeError) as exc:
                errors.append("execution envelope validation failed for %s: %s" % (relative, exc))
        errors.extend(_validate_output_claim_states(root, plan_path, expected))
        return plan, errors
    except (IssueError, OSError, UnicodeError, TypeError, KeyError, ValueError) as exc:
        return {}, ["issued plan validation failed: %s" % exc]


def _atomic_create(root, relative, content):
    target = _repository_path(root, relative)
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists():
        raise IssueError("refusing to overwrite existing path: %s" % relative)
    descriptor, temporary = tempfile.mkstemp(prefix=".%s." % target.name, dir=str(target.parent))
    try:
        with os.fdopen(descriptor, "wb") as handle:
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
        try:
            os.link(temporary, target)
        except FileExistsError as exc:
            raise IssueError("refusing to overwrite existing path: %s" % relative) from exc
    finally:
        try:
            os.unlink(temporary)
        except FileNotFoundError:
            pass


def _unlink_if_exact(root, relative, expected):
    """Remove only bytes created by this issuance transaction."""
    path = _repository_path(root, relative)
    try:
        if path.is_file() and path.read_bytes() == expected:
            path.unlink()
            return True
    except FileNotFoundError:
        pass
    return False


def _rollback_issued_transaction(root, output, plan):
    """Revoke public state when private credential delivery does not complete."""
    root = Path(root).resolve()
    plan_bytes = canonical_bytes(plan)
    reservations = _reservation_files(plan)
    # Remove the plan first so no new guarded consumer can begin.
    _unlink_if_exact(root, output, plan_bytes)
    for entry in reversed(plan.get("entries", [])):
        envelope = entry.get("execution_envelope", {})
        relative = envelope.get("path")
        if isinstance(relative, str):
            path = _repository_path(root, relative)
            try:
                content = path.read_bytes()
            except FileNotFoundError:
                content = None
            if (content is not None and len(content) == envelope.get("byte_length")
                    and sha256_bytes(content) == envelope.get("sha256")):
                path.unlink()
        for kind, ref in entry.get("output_reservations", {}).items():
            expected = reservations.get(ref.get("path"))
            if expected is not None:
                _unlink_if_exact(root, ref["path"], expected)
                _unlink_if_exact(root, ref["lock_path"], expected)
            # A receipt/output pair is transaction-owned only when every plan,
            # entry, reservation and artifact digest binding still matches.
            receipt_path = _repository_path(root, ref.get("claim_receipt_path", "invalid"))
            try:
                receipt_bytes = receipt_path.read_bytes()
                receipt = json.loads(receipt_bytes.decode("utf-8"))
                artifact = receipt.get("artifact", {})
                artifact_path = _repository_path(root, artifact.get("path", "invalid"))
                artifact_bytes = artifact_path.read_bytes()
                owned = (
                    receipt_bytes == canonical_bytes(receipt)
                    and receipt.get("plan", {}).get("plan_sha256") == plan.get("plan_sha256")
                    and receipt.get("entry_id") == entry.get("entry_id")
                    and receipt.get("artifact_kind") == kind
                    and receipt.get("reservation") == ref
                    and artifact.get("sha256") == sha256_bytes(artifact_bytes)
                    and artifact.get("byte_length") == len(artifact_bytes))
                if owned:
                    receipt_path.unlink()
                    artifact_path.unlink()
            except (FileNotFoundError, OSError, UnicodeError, ValueError, TypeError,
                    json.JSONDecodeError, IssueError):
                pass


def _require_planned_research_absent(root, plan):
    for entry in plan["entries"]:
        for key, relative in entry["planned_outputs"].items():
            if key != "execution_envelope" and _repository_path(root, relative).exists():
                raise IssueError(
                    "research/output artifact already exists before issuance: %s" % relative)


def issue(
        root, scope, campaign_id, run_date, freeze_manifest, output,
        commit_receipt, tag_receipt, ci_receipt, *, ci_fetcher=None,
        regression_gate_certificate=None, holdout_gate_certificate=None,
        gate_validator=None, scope_extension_manifest=None,
        scope_extension_receipt=None, credential_sink=None,
        extension_contract_validator=None):
    root = Path(root).resolve()
    output_path = _repository_path(root, output)
    plan, envelopes = build_issuance(
        root, scope, campaign_id, run_date, freeze_manifest,
        commit_receipt, tag_receipt, ci_receipt, ci_fetcher=ci_fetcher,
        regression_gate_certificate=regression_gate_certificate,
        holdout_gate_certificate=holdout_gate_certificate,
        gate_validator=gate_validator,
        scope_extension_manifest=scope_extension_manifest,
        scope_extension_receipt=scope_extension_receipt,
        credential_sink=credential_sink,
        extension_contract_validator=extension_contract_validator,
    )
    reservations = _reservation_files(plan)
    claim_auxiliaries = []
    for entry in plan["entries"]:
        for ref in entry["output_reservations"].values():
            claim_auxiliaries.extend((ref["lock_path"], ref["claim_receipt_path"]))
    all_outputs = list(reservations) + claim_auxiliaries + list(envelopes) + [output]
    if len(all_outputs) != len(set(all_outputs)):
        raise IssueError("plan and envelope output paths must be unique")
    for relative in all_outputs:
        if _repository_path(root, relative).exists():
            raise IssueError("refusing to overwrite existing path: %s" % relative)
    _require_planned_research_absent(root, plan)

    created = []
    try:
        # Sidecars are the atomic cooperative claims for every economic output.
        # Downstream writers must retain and match them until their own atomic
        # output create. Existing claims are never overwritten.
        for relative in sorted(reservations):
            _atomic_create(root, relative, reservations[relative])
            created.append((relative, reservations[relative]))
        _require_planned_research_absent(root, plan)
        for relative in sorted(envelopes):
            _atomic_create(root, relative, envelopes[relative])
            created.append((relative, envelopes[relative]))
        # Close the race between the initial precheck and the plan commit.  A
        # research/output artifact appearing while envelopes are being created
        # invalidates issuance and rolls the envelopes back.
        _require_planned_research_absent(root, plan)
        _atomic_create(root, output, canonical_bytes(plan))
        created.append((output, canonical_bytes(plan)))
        if output_path.read_bytes() != canonical_bytes(plan):
            raise IssueError("written issuance plan failed byte verification")
    except Exception:
        for relative, content in reversed(created):
            _unlink_if_exact(root, relative, content)
        raise
    return plan


def issue_with_credentials(*args, **kwargs):
    """Issue a plan and return its one-time capabilities only to the caller."""
    credentials = {}
    if "credential_sink" in kwargs:
        raise IssueError("credential_sink is internal to issue_with_credentials")
    plan = issue(*args, credential_sink=credentials, **kwargs)
    return plan, credentials


def issue_remediation(root, predecessor_plan_path, predecessor_campaign_path,
                      predecessor_entry_id,
                      predecessor_run_sha256, predecessor_review_sha256, output,
                      credential_sink=None):
    root = Path(root).resolve()
    plan, envelopes, bundles = build_remediation_issuance(
        root, predecessor_plan_path, predecessor_campaign_path, predecessor_entry_id,
        predecessor_run_sha256, predecessor_review_sha256,
        credential_sink=credential_sink)
    second = plan["entries"][-1]
    reservations = {}
    for relative, content in _reservation_files({**plan, "entries": [second]}).items():
        reservations[relative] = content
    paths = list(reservations) + list(envelopes) + list(bundles) + [output]
    for ref in second["output_reservations"].values():
        paths.extend((ref["lock_path"], ref["claim_receipt_path"]))
    paths.extend(second["planned_outputs"][kind]
                 for kind in ("packet", "record", "memo", "review"))
    if len(paths) != len(set(paths)):
        raise IssueError("remediation issuance paths are not unique")
    for relative in paths:
        if _repository_path(root, relative).exists():
            raise IssueError("refusing to overwrite existing remediation path: %s" % relative)
    created = []
    try:
        for relative, content in sorted({**reservations, **envelopes, **bundles}.items()):
            _atomic_create(root, relative, content)
            created.append(relative)
        _atomic_create(root, output, canonical_bytes(plan))
        created.append(output)
    except Exception:
        for relative in reversed(created):
            try:
                _repository_path(root, relative).unlink()
            except FileNotFoundError:
                pass
        raise
    return plan


def issue_remediation_with_credentials(*args, **kwargs):
    credentials = {}
    if "credential_sink" in kwargs:
        raise IssueError("credential_sink is internal to issue_remediation_with_credentials")
    plan = issue_remediation(*args, credential_sink=credentials, **kwargs)
    return plan, credentials


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=str(REPO))
    parser.add_argument("--scope", required=True, choices=("regression", "holdout", "full"))
    parser.add_argument("--campaign-id", required=True)
    parser.add_argument("--run-date", required=True)
    parser.add_argument("--freeze-manifest", required=True,
                        help="repository-relative canonical v4.2 freeze manifest")
    parser.add_argument("--commit-receipt", required=True,
                        help="post-freeze commit receipt (absolute or repository-relative)")
    parser.add_argument("--tag-receipt", required=True,
                        help="signed annotated-tag receipt (absolute or repository-relative)")
    parser.add_argument("--ci-receipt", required=True,
                        help="external CI timestamp receipt (absolute or repository-relative)")
    parser.add_argument("--output", required=True,
                        help="repository-relative immutable issuance-plan path")
    parser.add_argument("--regression-gate-certificate")
    parser.add_argument("--holdout-gate-certificate")
    parser.add_argument("--scope-extension-manifest")
    parser.add_argument("--scope-extension-receipt")
    parser.add_argument("--credentials-fd", type=int, required=True,
                        help="already-open FIFO/socket FD >=3 for ephemeral claim credentials")
    args = parser.parse_args(argv)
    plan = None
    try:
        _require_private_pipe_fd(args.credentials_fd, "credentials-fd")
        plan, credentials = issue_with_credentials(
            args.repo_root, args.scope, args.campaign_id, args.run_date,
            args.freeze_manifest, args.output,
            args.commit_receipt, args.tag_receipt, args.ci_receipt,
            regression_gate_certificate=args.regression_gate_certificate,
            holdout_gate_certificate=args.holdout_gate_certificate,
            scope_extension_manifest=args.scope_extension_manifest,
            scope_extension_receipt=args.scope_extension_receipt,
        )
        payload = canonical_bytes({"plan_sha256": plan["plan_sha256"],
                                   "claim_credentials": credentials})
        written = 0
        while written < len(payload):
            count = os.write(args.credentials_fd, payload[written:])
            if count <= 0:
                raise OSError("credential pipe closed before complete delivery")
            written += count
    except (IssueError, OSError, UnicodeError, TypeError) as exc:
        if plan is not None:
            _rollback_issued_transaction(args.repo_root, args.output, plan)
        print("ISSUANCE FAILED: %s" % exc, file=sys.stderr)
        return 1
    print("OK: issued %s entries; plan_sha256=%s" % (len(plan["entries"]), plan["plan_sha256"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
