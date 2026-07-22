#!/usr/bin/env python3
"""Issue an immutable, freeze-bound v4.1 pre-run campaign plan.

This command runs before research.  It reads only frozen infrastructure,
membership, prompts, industry specifications, datasets, and externally stored
post-freeze authorization receipts.  It creates exact attempt-1 execution
envelopes plus one canonical plan; it never creates a packet, finalized record,
memo, or review.
"""

import argparse
from datetime import date, datetime, timezone
import hashlib
import importlib.util
import json
import os
from pathlib import Path, PureWindowsPath
import re
import subprocess
import sys
import tempfile
import urllib.error
import urllib.request


REPO = Path(__file__).resolve().parent.parent.parent
PLAN_VERSION = "v4.1-pre-run-issuance-1"
FREEZE_VERSION = "v4.1-freeze-1"
PROMPT_VERSION = "v4.1-target-archetype-1"
REVIEW_PROMPT_VERSION = "validator-4.1"
CANARY_CODES = ("238220", "541214", "541511", "541512", "541930")
HOLDOUT_CODES = ("541922", "541840", "541350", "541430", "541720")
TARGETS_PATH = "pipeline/blocks/targets_phase3.json"
HOLDOUT_PATH = "pipeline/v4_1/holdout_membership.json"
REGRESSION_PATH = "pipeline/v4_1/regression_membership.json"
MODEL_ROUTES_PATH = "pipeline/v4_1/model_routes.json"
FREEZE_MANIFEST_PATH = "pipeline/v4_1/freeze_manifest.json"
FREEZE_CONTRACT_PATH = "pipeline/build/freeze_contract_v4_1.required.json"
FREEZE_VALIDATOR_PATH = "pipeline/build/freeze_contract_v4_1.py"
GITHUB_REPOSITORY = "jkee/rollup-economy"
GITHUB_API_ROOT = "https://api.github.com/repos/%s" % GITHUB_REPOSITORY
GITHUB_WEB_ROOT = "https://github.com/%s" % GITHUB_REPOSITORY
FREEZE_WORKFLOW_PATH = ".github/workflows/v4-1-freeze.yml"
FREEZE_WORKFLOW_NAME = "v4.1 freeze evidence"

TOOLCHAIN_PATHS = {
    "methodology": "V4_1_METHODOLOGY.md",
    "rejection_record": "V4_0_REJECTION.md",
    "thresholds": "pipeline/build/thresholds_v4_1.json",
    "dataset_schema": "pipeline/build/schemas/dataset_v4_1.schema.json",
    "industry_spec_schema": "pipeline/build/schemas/industry_spec_v4_1.schema.json",
    "packet_schema": "pipeline/build/schemas/research_packet_v4_1.schema.json",
    "run_schema": "pipeline/build/schemas/run_record_v4_1.schema.json",
    "review_schema": "pipeline/build/schemas/review_record_v4_1.schema.json",
    "scoring": "pipeline/build/v4_1_scoring.py",
    "finalizer": "pipeline/build/finalize_run_v4_1.py",
    "campaign_validator": "pipeline/build/campaign_v4_1.py",
    "prompt_assembler": "pipeline/build/assemble_prompts.py",
    "prompt_template": "pipeline/template/prompt_template_v4_1.md",
    "runner_prompt": "pipeline/template/runner_brief_v4_1.md",
    "validator_prompt": "pipeline/template/validator_brief_v4_1.md",
    "model_routes": MODEL_ROUTES_PATH,
    "allowed_signers": "pipeline/v4_1/allowed_signers",
    "freeze_contract": FREEZE_CONTRACT_PATH,
    "freeze_validator": FREEZE_VALIDATOR_PATH,
    "issuer": "pipeline/build/issue_campaign_v4_1.py",
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
    spec = importlib.util.spec_from_file_location("freeze_contract_v4_1_for_issuer", path)
    if spec is None or spec.loader is None:
        raise IssueError("cannot load the frozen v4.1 freeze-contract validator")
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
            "User-Agent": "rollup-economy-v4.1-freeze-issuer",
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


def _verify_live_ci(ci, commit, tag, fetch_json=None):
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
        FREEZE_WORKFLOW_PATH,
        "%s@refs/tags/%s" % (FREEZE_WORKFLOW_PATH, tag_name),
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
        "name": FREEZE_WORKFLOW_NAME,
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
    expected_name = "v4.1-freeze-%s" % commit_sha
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


def _verify_git_authority(root, manifest_relative, manifest, commit, tag):
    """Verify receipt claims against actual immutable git objects."""
    commit_sha = commit.get("commit_sha")
    tag_name = tag.get("tag_name")
    tag_object_sha = tag.get("tag_object_sha")
    if _git(root, "rev-parse", "HEAD") != commit_sha:
        raise IssueError("current HEAD is not exactly the authorized freeze commit")
    if _git(root, "cat-file", "-t", commit_sha) != "commit":
        raise IssueError("authorization commit receipt does not name a git commit")
    frozen_bytes = _repository_path(root, manifest_relative, must_exist=True).read_bytes()
    if _git_bytes(root, "show", "%s:%s" % (commit_sha, manifest_relative)) != frozen_bytes:
        raise IssueError("authorization commit does not contain the exact freeze manifest")

    actual_tag_object = _git(root, "rev-parse", "refs/tags/%s^{tag}" % tag_name)
    if actual_tag_object != tag_object_sha:
        raise IssueError("authorization tag object SHA does not match the receipt")
    if _git(root, "cat-file", "-t", actual_tag_object) != "tag":
        raise IssueError("authorization tag is not an annotated tag object")
    if _git(root, "rev-parse", "refs/tags/%s^{commit}" % tag_name) != commit_sha:
        raise IssueError("authorization tag does not peel to the frozen commit")
    tag_object = _git_bytes(root, "cat-file", "-p", actual_tag_object)
    _headers, separator, message = tag_object.partition(b"\n\n")
    root_digest = manifest.get("root_sha256")
    if (not separator or not isinstance(root_digest, str)
            or re.search(
                rb"(?<![0-9a-f])" + root_digest.encode("ascii") + rb"(?![0-9a-f])",
                message,
            ) is None):
        raise IssueError("authorization tag message does not bind the exact freeze root")
    _git(root, "verify-tag", tag_name)


def _authorization_evidence(
        root, freeze_manifest, manifest, frozen,
        commit_receipt, tag_receipt, ci_receipt, ci_fetcher=None):
    contract_path = _repository_path(root, FREEZE_CONTRACT_PATH, must_exist=True)
    manifest_path = _repository_path(root, freeze_manifest, must_exist=True)
    commit_path = _receipt_path(root, commit_receipt, "commit")
    tag_path = _receipt_path(root, tag_receipt, "tag")
    ci_path = _receipt_path(root, ci_receipt, "CI")
    supplied = (commit_receipt, tag_receipt, ci_receipt)
    paths = (commit_path, tag_path, ci_path)
    before = [_external_ref(path, value) for path, value in zip(paths, supplied)]

    try:
        errors = _load_freeze_contract(root).validate(
            contract_path, manifest_path, commit_path, tag_path, ci_path, root,
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
    _verify_git_authority(root, freeze_manifest, manifest, commit, tag)
    _verify_live_ci(ci, commit, tag, fetch_json=ci_fetcher)
    if [_external_ref(path, value) for path, value in zip(paths, supplied)] != before:
        raise IssueError("authorization receipt changed during live CI verification")
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
    if value["route_version"] != "v4.1-model-routes-1":
        raise IssueError("model route version is invalid")
    if not isinstance(value["research"], dict) or set(value["research"]) != {"fleet", "golden"}:
        raise IssueError("model routes research map must contain exactly fleet and golden")
    if not isinstance(value["review"], dict) or set(value["review"]) != {"all"}:
        raise IssueError("model routes review map must contain exactly all")
    if not isinstance(value["execution"], dict) or set(value["execution"]) != {
            "fork_policy", "issued_by_task_path", "research_role", "review_role"}:
        raise IssueError("model routes execution map is not closed")
    models = [value["research"]["fleet"], value["research"]["golden"], value["review"]["all"]]
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
    if scope == "canary":
        ref = _frozen_ref(root, frozen, REGRESSION_PATH)
        value = load_json(_repository_path(root, REGRESSION_PATH, must_exist=True))
        if not isinstance(value, dict) or set(value) != {
                "membership_version", "purpose", "selected_codes", "selection_rule"}:
            raise IssueError("regression membership contract is not closed")
        if (value["membership_version"] != "v4.1-regression-1"
                or value["selected_codes"] != list(CANARY_CODES)
                or not isinstance(value["purpose"], str) or not value["purpose"].strip()
                or not isinstance(value["selection_rule"], str) or not value["selection_rule"].strip()):
            raise IssueError("regression membership does not equal the preregistered exact five")
        return list(CANARY_CODES), ref, None
    ref = _frozen_ref(root, frozen, HOLDOUT_PATH)
    value = load_json(_repository_path(root, HOLDOUT_PATH, must_exist=True))
    selected = value.get("selected_codes") if isinstance(value, dict) else None
    if selected != list(HOLDOUT_CODES):
        raise IssueError("holdout membership does not equal the preregistered exact five")
    return list(HOLDOUT_CODES), None, ref


def _planned_paths(scope, code, run_id):
    base = "pipeline/v4_1"
    return {
        "packet": "%s/packets/%s/%s.json" % (base, code, run_id),
        "execution_envelope": "%s/envelopes/%s/%s.json" % (base, code, run_id),
        "record": "%s/runs/%s/%s.json" % (base, code, run_id),
        "memo": "%s/memos/%s/%s.md" % (base, code, run_id),
        "review": "%s/reviews/%s/%s.json" % (base, code, run_id),
    }


def _plan_digest(plan):
    value = dict(plan)
    value.pop("plan_sha256", None)
    return sha256_bytes(canonical_bytes(value))


def _validate_global_task_paths(entries):
    paths = []
    for entry in entries:
        for role in ("research_execution", "review_execution"):
            execution = entry.get(role)
            path = execution.get("codex_task_path") if isinstance(execution, dict) else None
            if not isinstance(path, str) or not re.fullmatch(r"/root/[a-z0-9_]+", path):
                raise IssueError("every research/reviewer execution requires an exact child task path")
            paths.append(path)
    if len(paths) != len(set(paths)):
        raise IssueError("research and reviewer task paths must be globally unique")


def build_issuance(
        root, scope, campaign_id, run_date, freeze_manifest,
        commit_receipt, tag_receipt, ci_receipt, *, ci_fetcher=None):
    root = Path(root).resolve()
    if freeze_manifest != FREEZE_MANIFEST_PATH:
        raise IssueError("freeze manifest path must be exactly %s" % FREEZE_MANIFEST_PATH)
    if scope not in ("canary", "holdout"):
        raise IssueError("scope must be canary or holdout")
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
    authorization = _authorization_evidence(
        root, freeze_manifest, manifest, frozen,
        commit_receipt, tag_receipt, ci_receipt, ci_fetcher=ci_fetcher,
    )
    freeze_ref["git_commit"] = authorization["commit_sha"]
    routes, routes_ref = _model_routes(root, frozen)
    execution_route = routes["execution"]
    research_model_id = routes["research"]["fleet"]
    review_model_id = routes["review"]["all"]
    targets = _targets(root, frozen)
    codes, regression_ref, holdout_ref = _membership(root, frozen, scope)
    missing = sorted(set(codes) - set(targets))
    if missing:
        raise IssueError("scope membership is absent from frozen target universe: %s" % missing)

    entries, envelopes = [], {}
    seen_run_ids, seen_tasks, seen_outputs = set(), set(), set()
    for code in codes:
        title = targets[code]
        prompt_path = "pipeline/prompts_v4_1/%s.md" % code
        spec_path = "pipeline/specs_v4_1/%s.json" % code
        prompt_ref = _frozen_ref(root, frozen, prompt_path)
        spec_ref = _frozen_ref(root, frozen, spec_path)
        spec = load_json(_repository_path(root, spec_path, must_exist=True))
        if spec.get("spec_version") != "4.1" or spec.get("naics") != code or spec.get("title") != title:
            raise IssueError("industry spec identity mismatch for %s" % code)
        snapshot = spec.get("dataset_snapshot")
        if not isinstance(snapshot, dict) or set(snapshot) != {"path", "sha256"}:
            raise IssueError("industry spec dataset_snapshot is not closed for %s" % code)
        expected_dataset = "pipeline/datasets/v4_1/%s.json" % code
        if snapshot["path"] != expected_dataset:
            raise IssueError("industry spec dataset path mismatch for %s" % code)
        dataset_ref = _frozen_ref(root, frozen, expected_dataset)
        if snapshot["sha256"] != dataset_ref["sha256"]:
            raise IssueError("industry spec dataset digest mismatch for %s" % code)
        dataset = load_json(_repository_path(root, expected_dataset, must_exist=True))
        if dataset.get("dataset_version") != "4.1" or dataset.get("naics") != code or dataset.get("title") != title:
            raise IssueError("normalized dataset identity mismatch for %s" % code)

        run_id = "%s_%s_v4_1_%s_a1" % (run_date, scope, code)
        task_campaign = campaign_id.replace("-", "_")
        task_root = execution_route["issued_by_task_path"]
        task_path = "%s/research_v4_1_%s_%s_a1" % (task_root, task_campaign, code)
        review_task_path = "%s/review_v4_1_%s_%s_a1" % (task_root, task_campaign, code)
        planned = _planned_paths(scope, code, run_id)
        if run_id in seen_run_ids or task_path in seen_tasks or review_task_path in seen_tasks:
            raise IssueError("run IDs and research task paths must be unique")
        if set(planned.values()) & seen_outputs:
            raise IssueError("planned artifact paths must be unique")
        seen_run_ids.add(run_id)
        seen_tasks.add(task_path)
        seen_tasks.add(review_task_path)
        seen_outputs.update(planned.values())

        envelope = {
            "envelope_version": "4.1",
            "kind": "fleet",
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
        entries.append({
            "entry_id": "fleet:%s:%s" % (code, run_id),
            "kind": "fleet",
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
        })

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
        },
        "toolchain": toolchain,
        "entries": entries,
    }
    plan["plan_sha256"] = _plan_digest(plan)
    return plan, envelopes


def validate_issued_plan(root, plan_path, expected_scope=None, *, ci_fetcher=None):
    """Reopen and fully reproduce an issued plan for downstream consumers.

    Returns ``(plan, errors)`` and does not raise for invalid external input.
    Successful validation also proves every on-disk execution envelope equals
    the deterministic bytes committed by the plan.
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
        }
        if set(plan) != required_keys:
            raise IssueError("issued plan top-level keys are not closed")
        if raw != canonical_bytes(plan):
            raise IssueError("issued plan bytes are not canonical JSON")
        if plan.get("plan_version") != PLAN_VERSION:
            raise IssueError("issued plan version is not %s" % PLAN_VERSION)
        if plan.get("plan_sha256") != _plan_digest(plan):
            raise IssueError("issued plan self-digest is stale")
        if expected_scope is not None and plan.get("scope") != expected_scope:
            raise IssueError("issued plan scope does not match the campaign scope")
        authorization = plan.get("authorization")
        if not isinstance(authorization, dict):
            raise IssueError("issued plan authorization binding is missing")
        receipt_paths = []
        for key in ("commit_receipt", "tag_receipt", "ci_receipt"):
            ref = authorization.get(key)
            if not isinstance(ref, dict) or set(ref) != {"path", "sha256", "byte_length"}:
                raise IssueError("issued plan %s reference is not closed" % key)
            receipt_paths.append(ref["path"])

        expected, envelopes = build_issuance(
            root, plan["scope"], plan["campaign_id"], plan["run_date"],
            plan["freeze"]["path"], *receipt_paths, ci_fetcher=ci_fetcher,
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


def _require_planned_research_absent(root, plan):
    for entry in plan["entries"]:
        for key, relative in entry["planned_outputs"].items():
            if key != "execution_envelope" and _repository_path(root, relative).exists():
                raise IssueError(
                    "research/output artifact already exists before issuance: %s" % relative)


def issue(
        root, scope, campaign_id, run_date, freeze_manifest, output,
        commit_receipt, tag_receipt, ci_receipt, *, ci_fetcher=None):
    root = Path(root).resolve()
    output_path = _repository_path(root, output)
    plan, envelopes = build_issuance(
        root, scope, campaign_id, run_date, freeze_manifest,
        commit_receipt, tag_receipt, ci_receipt, ci_fetcher=ci_fetcher,
    )
    all_outputs = list(envelopes) + [output]
    if len(all_outputs) != len(set(all_outputs)):
        raise IssueError("plan and envelope output paths must be unique")
    for relative in all_outputs:
        if _repository_path(root, relative).exists():
            raise IssueError("refusing to overwrite existing path: %s" % relative)
    _require_planned_research_absent(root, plan)

    created = []
    try:
        for relative in sorted(envelopes):
            _atomic_create(root, relative, envelopes[relative])
            created.append(relative)
        # Close the race between the initial precheck and the plan commit.  A
        # research/output artifact appearing while envelopes are being created
        # invalidates issuance and rolls the envelopes back.
        _require_planned_research_absent(root, plan)
        _atomic_create(root, output, canonical_bytes(plan))
        created.append(output)
        if output_path.read_bytes() != canonical_bytes(plan):
            raise IssueError("written issuance plan failed byte verification")
    except Exception:
        for relative in reversed(created):
            try:
                _repository_path(root, relative).unlink()
            except FileNotFoundError:
                pass
        raise
    return plan


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=str(REPO))
    parser.add_argument("--scope", required=True, choices=("canary", "holdout"))
    parser.add_argument("--campaign-id", required=True)
    parser.add_argument("--run-date", required=True)
    parser.add_argument("--freeze-manifest", required=True,
                        help="repository-relative canonical v4.1 freeze manifest")
    parser.add_argument("--commit-receipt", required=True,
                        help="post-freeze commit receipt (absolute or repository-relative)")
    parser.add_argument("--tag-receipt", required=True,
                        help="signed annotated-tag receipt (absolute or repository-relative)")
    parser.add_argument("--ci-receipt", required=True,
                        help="external CI timestamp receipt (absolute or repository-relative)")
    parser.add_argument("--output", required=True,
                        help="repository-relative immutable issuance-plan path")
    args = parser.parse_args(argv)
    try:
        plan = issue(
            args.repo_root, args.scope, args.campaign_id, args.run_date,
            args.freeze_manifest, args.output,
            args.commit_receipt, args.tag_receipt, args.ci_receipt,
        )
    except (IssueError, OSError, UnicodeError, TypeError) as exc:
        print("ISSUANCE FAILED: %s" % exc, file=sys.stderr)
        return 1
    print("OK: issued %s entries; plan_sha256=%s" % (len(plan["entries"]), plan["plan_sha256"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
