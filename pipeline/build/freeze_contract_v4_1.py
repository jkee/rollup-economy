#!/usr/bin/env python3
"""Validate the complete v4.1 methodology-freeze and authorization contract.

This checker is intentionally independent of ``freeze_v4_1.py``.  It verifies
that a canonical freeze manifest contains every Section 14 artifact, binds the
exact regression and untouched-holdout cohorts, and is authorized by three
non-circular receipts created after the root digest exists.

It performs no commit, tag, timestamp, publication, or economic-result writes;
post-freeze validation uses only read-only Git object and signature checks.
"""

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import subprocess
import sys


REPO = Path(__file__).resolve().parent.parent.parent
DEFAULT_CONTRACT = "pipeline/build/freeze_contract_v4_1.required.json"
FREEZE_MANIFEST_VERSION = "v4.1-freeze-1"
CONTRACT_VERSION = "v4.1-section14-completeness-1"
RECEIPT_VERSION = "v4.1-authorization-receipt-1"
CANARY_CODES = ("238220", "541214", "541511", "541512", "541930")
MODEL_ROUTES = {
    "route_version": "v4.1-model-routes-1",
    "research": {"fleet": "gpt-5.6-terra", "golden": "gpt-5.6-sol"},
    "review": {"all": "gpt-5.6-sol"},
    "execution": {
        "fork_policy": "none",
        "issued_by_task_path": "/root",
        "research_role": "research",
        "review_role": "reviewer",
    },
}
CHANGE_CONTROL_PATH = "pipeline/v4_1/change_control.json"
HOLDOUT_MEMBERSHIP_PATH = "pipeline/v4_1/holdout_membership.json"
REGRESSION_MEMBERSHIP_PATH = "pipeline/v4_1/regression_membership.json"
MODEL_ROUTES_PATH = "pipeline/v4_1/model_routes.json"
TARGET_MEMBERSHIP_PATH = "pipeline/blocks/targets_phase3.json"
FREEZE_PLAN_PATH = "pipeline/v4_1/freeze_plan.json"
FREEZE_MANIFEST_PATH = "pipeline/v4_1/freeze_manifest.json"
FREEZE_CI_WORKFLOW_PATH = ".github/workflows/v4-1-freeze.yml"
GITHUB_OWNER = "jkee"
GITHUB_REPOSITORY = "rollup-economy"
ALLOWED_SIGNERS_PATH = "pipeline/v4_1/allowed_signers"
ALLOWED_SIGNER_PRINCIPAL = "jkee"
HOLDOUT_CODES = ("541922", "541840", "541350", "541430", "541720")
TARGET_CODES = (
    "238220", "523940", "524210", "531210", "541110", "541120", "541191",
    "541199", "541211", "541213", "541214", "541219", "541310", "541320",
    "541330", "541340", "541350", "541360", "541370", "541380", "541410",
    "541420", "541430", "541490", "541511", "541512", "541513", "541519",
    "541611", "541612", "541613", "541614", "541618", "541620", "541690",
    "541713", "541714", "541715", "541720", "541810", "541820", "541830",
    "541840", "541850", "541860", "541870", "541890", "541910", "541921",
    "541922", "541930", "541940", "541990", "561422", "561492", "561510",
    "561710", "561730", "621210", "621340", "621610", "811192", "812210",
)

BASE_REQUIRED_PATHS = (
    "V4_0_REJECTION.md",
    "V4_1_METHODOLOGY.md",
    "pipeline/build/assemble_prompts.py",
    "pipeline/build/campaign_v4_1.py",
    "pipeline/build/finalize_run_v4_1.py",
    "pipeline/build/freeze_contract_v4_1.py",
    "pipeline/build/freeze_contract_v4_1.required.json",
    "pipeline/build/freeze_v4_1.py",
    "pipeline/build/issue_campaign_v4_1.py",
    "pipeline/build/normalize_datasets_v4_1.py",
    "pipeline/build/schemas/dataset_v4_1.schema.json",
    "pipeline/build/schemas/industry_spec_v4_1.schema.json",
    "pipeline/build/schemas/research_packet_v4_1.schema.json",
    "pipeline/build/schemas/review_record_v4_1.schema.json",
    "pipeline/build/schemas/run_record_v4_1.schema.json",
    "pipeline/build/select_holdout_v4_1.py",
    "pipeline/build/test_freeze_contract_v4_1.py",
    "pipeline/build/test_freeze_v4_1.py",
    "pipeline/build/test_holdout_v4_1.py",
    "pipeline/build/test_issue_campaign_v4_1.py",
    "pipeline/build/test_normalize_datasets_v4_1.py",
    "pipeline/build/test_prompt_v4_1.py",
    "pipeline/build/test_v4_1_campaign.py",
    "pipeline/build/test_v4_1_finalizer.py",
    "pipeline/build/test_v4_1_scoring.py",
    "pipeline/build/thresholds_v4_1.json",
    "pipeline/build/v4_1_scoring.py",
    "pipeline/template/prompt_template_v4_1.md",
    "pipeline/template/runner_brief_v4_1.md",
    "pipeline/template/validator_brief_v4_1.md",
    TARGET_MEMBERSHIP_PATH,
    ALLOWED_SIGNERS_PATH,
    HOLDOUT_MEMBERSHIP_PATH,
    REGRESSION_MEMBERSHIP_PATH,
    MODEL_ROUTES_PATH,
    CHANGE_CONTROL_PATH,
    FREEZE_PLAN_PATH,
    FREEZE_CI_WORKFLOW_PATH,
)
BASE_SCHEMA_PATHS = {
    "pipeline/build/schemas/dataset_v4_1.schema.json",
    "pipeline/build/schemas/industry_spec_v4_1.schema.json",
    "pipeline/build/schemas/research_packet_v4_1.schema.json",
    "pipeline/build/schemas/review_record_v4_1.schema.json",
    "pipeline/build/schemas/run_record_v4_1.schema.json",
}
REQUIRED_SENTINEL_TEST = "pipeline/build/test_v4_1_scoring.py"
ISSUANCE_TOOLING_PATHS = ("pipeline/build/issue_campaign_v4_1.py",)
ISSUANCE_PATH_RE = re.compile(r"^pipeline/build/[A-Za-z0-9_.-]*issu[A-Za-z0-9_.-]*_v4_1\.py$")
HEX64_RE = re.compile(r"^[0-9a-f]{64}$")
GIT_OID_RE = re.compile(r"^[0-9a-f]{40}(?:[0-9a-f]{24})?$")
TAG_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._/-]*$")
NAICS_RE = re.compile(r"^[0-9]{6}$")

CHANGE_CONTROL = {
    "change_control_version": "v4.1-change-control-1",
    "allowed_new_version_triggers": [
        "mathematical_or_monotonicity_failure",
        "construct_contradiction",
        "schema_scoring_or_reproduction_mismatch",
        "frozen_review_or_evidence_contract_failure",
        "preregistered_evidence_infeasibility",
    ],
    "forbidden_triggers": [
        "named_industry_score",
        "named_industry_rank",
        "named_industry_verdict",
        "named_industry_color",
        "named_industry_movement_from_v4_0",
    ],
    "evidence_infeasibility_rule": {
        "critical_unbounded_count": 2,
        "set_size": 5,
        "treatment": "reject_v4_1_and_create_new_version_with_new_salted_holdout",
    },
    "viewed_holdout_treatment": "burned_for_later_methodology_versions",
    "superseded_artifact_treatment": "preserve_without_reinterpretation",
}

REGRESSION_MEMBERSHIP = {
    "membership_version": "v4.1-regression-1",
    "purpose": "Disclosed development regression set; not holdout evidence",
    "selected_codes": list(CANARY_CODES),
    "selection_rule": "The five v4.0 canary codes whose outputs were viewed before v4.1 was authored",
}

EXPECTED_VERSIONED_BUILD_PATHS = {
    path for path in BASE_REQUIRED_PATHS
    if path.startswith("pipeline/build/") and path.endswith(".py") and "v4_1" in path
}
EXPECTED_VERSIONED_TEMPLATE_PATHS = {
    path for path in BASE_REQUIRED_PATHS
    if path.startswith("pipeline/template/") and "v4_1" in path
}


class ContractError(ValueError):
    """Raised for a malformed or incomplete freeze contract."""


def _reject_constant(value):
    raise ContractError("non-standard JSON constant %r is forbidden" % value)


def _closed_pairs(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ContractError("duplicate JSON key %r" % key)
        result[key] = value
    return result


def load_json(path):
    with Path(path).open("r", encoding="utf-8") as handle:
        return json.load(handle, parse_constant=_reject_constant, object_pairs_hook=_closed_pairs)


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


def _repo_file(root, relative, *, must_exist=True):
    if not isinstance(relative, str) or not relative or "\x00" in relative or "\\" in relative:
        raise ContractError("path must be a non-empty repository-relative POSIX path")
    pure = PurePosixPath(relative)
    if pure.is_absolute() or any(part in ("", ".", "..") for part in pure.parts):
        raise ContractError("path must be canonical and repository-relative: %s" % relative)
    root = Path(root).resolve()
    candidate = root.joinpath(*pure.parts).resolve()
    try:
        candidate.relative_to(root)
    except ValueError as exc:
        raise ContractError("path escapes repository: %s" % relative) from exc
    if must_exist and not candidate.is_file():
        raise ContractError("required file does not exist: %s" % relative)
    return candidate


def root_sha256(files):
    digest = hashlib.sha256()
    for item in sorted(files, key=lambda row: row["path"].encode("utf-8")):
        digest.update(item["path"].encode("utf-8"))
        digest.update(b"\0")
        digest.update(str(item["byte_length"]).encode("ascii"))
        digest.update(b"\0")
        digest.update(item["sha256"].encode("ascii"))
        digest.update(b"\n")
    return digest.hexdigest()


def _iso_timestamp(value, label):
    if not isinstance(value, str) or not value:
        raise ContractError("%s must be a non-empty ISO-8601 timestamp" % label)
    normalized = value[:-1] + "+00:00" if value.endswith("Z") else value
    try:
        parsed = datetime.fromisoformat(normalized)
    except ValueError as exc:
        raise ContractError("%s must be an ISO-8601 timestamp" % label) from exc
    if parsed.tzinfo is None or parsed.utcoffset() is None:
        raise ContractError("%s must include a timezone" % label)
    if parsed > datetime.now(timezone.utc).astimezone(parsed.tzinfo):
        raise ContractError("%s cannot be in the future" % label)
    return parsed


def contract_errors(contract):
    errors = []
    required_keys = {
        "contract_version", "methodology_version", "freeze_manifest_version",
        "canary_codes", "holdout_membership_path", "required_exact_paths",
        "issuance_tooling_paths", "sentinel_test_paths", "change_control_path",
        "model_routes",
    }
    if not isinstance(contract, dict):
        return ["contract must be an object"]
    if set(contract) != required_keys:
        errors.append("contract keys must be exactly %s" % sorted(required_keys))
    if contract.get("contract_version") != CONTRACT_VERSION:
        errors.append("contract_version must be %s" % CONTRACT_VERSION)
    if contract.get("methodology_version") != "4.1":
        errors.append("methodology_version must be 4.1")
    if contract.get("freeze_manifest_version") != FREEZE_MANIFEST_VERSION:
        errors.append("freeze_manifest_version must be %s" % FREEZE_MANIFEST_VERSION)
    if contract.get("canary_codes") != list(CANARY_CODES):
        errors.append("canary_codes must equal the exact disclosed regression cohort")
    if contract.get("holdout_membership_path") != HOLDOUT_MEMBERSHIP_PATH:
        errors.append("holdout_membership_path is not canonical")
    if contract.get("change_control_path") != CHANGE_CONTROL_PATH:
        errors.append("change_control_path is not canonical")
    if contract.get("model_routes") != MODEL_ROUTES:
        errors.append("model_routes differ from the exact v4.1 routes")

    exact = contract.get("required_exact_paths")
    if (not isinstance(exact, list) or not all(isinstance(path, str) for path in exact)
            or exact != sorted(set(exact))):
        errors.append("required_exact_paths must be a sorted unique list")
    elif set(exact) != set(BASE_REQUIRED_PATHS):
        errors.append("required_exact_paths must equal the closed Section 14 base paths; "
                      "missing=%s extra=%s" % (
                          sorted(set(BASE_REQUIRED_PATHS) - set(exact)),
                          sorted(set(exact) - set(BASE_REQUIRED_PATHS)),
                      ))

    issuance = contract.get("issuance_tooling_paths")
    if issuance != list(ISSUANCE_TOOLING_PATHS):
        errors.append("issuance_tooling_paths must equal the exact v4.1 issuance tool contract")
    elif not all(ISSUANCE_PATH_RE.fullmatch(path) for path in issuance):
        errors.append("every issuance tooling path must be a versioned v4.1 issuance script")

    sentinels = contract.get("sentinel_test_paths")
    if sentinels != [REQUIRED_SENTINEL_TEST]:
        errors.append("sentinel_test_paths must equal the frozen v4.1 scoring sentinel suite")
    return errors


def _manifest_errors(manifest, manifest_path, root):
    errors = []
    if not isinstance(manifest, dict) or set(manifest) != {"files", "manifest_version", "root_sha256"}:
        return ["freeze manifest must be a closed files/manifest_version/root_sha256 object"], {}
    if manifest.get("manifest_version") != FREEZE_MANIFEST_VERSION:
        errors.append("freeze manifest version mismatch")
    files = manifest.get("files")
    if not isinstance(files, list) or not files:
        return errors + ["freeze manifest files must be a non-empty array"], {}
    paths = [item.get("path") for item in files if isinstance(item, dict)]
    paths_are_strings = len(paths) == len(files) and all(isinstance(path, str) for path in paths)
    if not paths_are_strings or paths != sorted(paths, key=lambda value: value.encode("utf-8")):
        errors.append("freeze manifest files must be sorted bytewise by path")
    if paths_are_strings and len(paths) != len(set(paths)):
        errors.append("freeze manifest paths must be unique")
    members = {}
    structurally_valid = True
    for index, item in enumerate(files):
        if not isinstance(item, dict) or set(item) != {"path", "byte_length", "sha256"}:
            errors.append("freeze manifest file %d must contain exactly path/byte_length/sha256" % index)
            structurally_valid = False
            continue
        path, length, digest = item["path"], item["byte_length"], item["sha256"]
        if not isinstance(length, int) or isinstance(length, bool) or length < 0:
            errors.append("freeze manifest byte_length is invalid for %r" % path)
            structurally_valid = False
        if not isinstance(digest, str) or not HEX64_RE.fullmatch(digest):
            errors.append("freeze manifest SHA-256 is invalid for %r" % path)
            structurally_valid = False
        try:
            absolute = _repo_file(root, path)
        except ContractError as exc:
            errors.append(str(exc))
            structurally_valid = False
            continue
        if isinstance(length, int) and absolute.stat().st_size != length:
            errors.append("freeze manifest byte length is stale: %s" % path)
        if isinstance(digest, str) and sha256_file(absolute) != digest:
            errors.append("freeze manifest digest is stale: %s" % path)
        members[path] = item
    if structurally_valid and paths_are_strings and root_sha256(files) != manifest.get("root_sha256"):
        errors.append("freeze manifest root digest is stale")
    elif not structurally_valid or not paths_are_strings:
        errors.append("freeze manifest root digest cannot be verified from malformed file entries")
    try:
        actual_bytes = Path(manifest_path).read_bytes()
        if actual_bytes != canonical_bytes(manifest):
            errors.append("freeze manifest bytes are not canonical compact JSON")
    except OSError as exc:
        errors.append("cannot read freeze manifest bytes: %s" % exc)
    return errors, members


def _holdout_codes(membership):
    if not isinstance(membership, dict):
        raise ContractError("holdout membership must be an object")
    regression = membership.get("regression_codes")
    selected = membership.get("selected_codes")
    if regression != sorted(CANARY_CODES):
        raise ContractError("holdout membership regression_codes differ from the exact canary")
    selected_valid = (isinstance(selected, list) and len(selected) == 5
                      and all(isinstance(code, str) and NAICS_RE.fullmatch(code) for code in selected))
    if not selected_valid or len(set(selected)) != 5:
        raise ContractError("holdout selected_codes must contain exactly five unique NAICS codes")
    if selected != list(HOLDOUT_CODES):
        raise ContractError("holdout selected_codes differ from the exact frozen selection")
    if set(selected) & set(CANARY_CODES):
        raise ContractError("holdout selected_codes overlap the regression canary")
    bins = membership.get("bins")
    if not isinstance(bins, list) or len(bins) != 5:
        raise ContractError("holdout membership must contain exactly five selection bins")
    if [item.get("selected_naics") for item in bins if isinstance(item, dict)] != selected:
        raise ContractError("holdout selected_codes differ from bin winners")
    return selected


def _target_codes(targets):
    if not isinstance(targets, dict) or set(targets) != {"version", "description", "codes"}:
        raise ContractError("target membership must be a closed version/description/codes object")
    rows = targets.get("codes")
    if not isinstance(rows, list) or len(rows) != 63:
        raise ContractError("target membership must contain exactly 63 rows")
    codes = []
    for row in rows:
        if not isinstance(row, dict) or set(row) != {"naics", "title", "golden"}:
            raise ContractError("each target row must contain exactly naics/title/golden")
        code = row.get("naics")
        if (not isinstance(code, str) or not NAICS_RE.fullmatch(code)
                or not isinstance(row.get("title"), str) or not row["title"].strip()
                or not isinstance(row.get("golden"), bool)):
            raise ContractError("target row values are malformed")
        codes.append(code)
    if len(set(codes)) != 63 or codes != list(TARGET_CODES):
        raise ContractError("target membership differs from the exact 63-code v4.1 fleet")
    return codes


def required_paths(contract, membership, root):
    """Return every repository artifact that must appear in the freeze manifest."""
    errors = contract_errors(contract)
    if errors:
        raise ContractError("; ".join(errors))
    holdout = _holdout_codes(membership)
    required = set(contract["required_exact_paths"])
    required.update(contract["issuance_tooling_paths"])
    required.update(contract["sentinel_test_paths"])

    root = Path(root)
    targets = load_json(_repo_file(root, TARGET_MEMBERSHIP_PATH))
    target_codes = _target_codes(targets)
    schema_dir = root / "pipeline" / "build" / "schemas"
    discovered_schemas = {
        path.relative_to(root).as_posix()
        for path in schema_dir.glob("*_v4_1.schema.json") if path.is_file()
    }
    if not BASE_SCHEMA_PATHS.issubset(discovered_schemas):
        raise ContractError("repository omits required v4.1 schemas: %s" %
                            sorted(BASE_SCHEMA_PATHS - discovered_schemas))
    required.update(discovered_schemas)

    discovered_build = {
        path.relative_to(root).as_posix()
        for path in (root / "pipeline" / "build").glob("*v4_1*.py") if path.is_file()
    }
    if discovered_build != EXPECTED_VERSIONED_BUILD_PATHS:
        raise ContractError(
            "ambiguous v4.1 build artifacts; expected=%s actual=%s" %
            (sorted(EXPECTED_VERSIONED_BUILD_PATHS), sorted(discovered_build))
        )
    discovered_templates = {
        path.relative_to(root).as_posix()
        for path in (root / "pipeline" / "template").glob("*v4_1*") if path.is_file()
    }
    if discovered_templates != EXPECTED_VERSIONED_TEMPLATE_PATHS:
        raise ContractError(
            "ambiguous v4.1 templates; expected=%s actual=%s" %
            (sorted(EXPECTED_VERSIONED_TEMPLATE_PATHS), sorted(discovered_templates))
        )

    selected_codes = (*CANARY_CODES, *holdout)
    for code in selected_codes:
        required.add("pipeline/specs_v4_1/%s.json" % code)
        required.add("pipeline/prompts_v4_1/%s.md" % code)
    for code in target_codes:
        required.add("pipeline/datasets/v4_1/%s.json" % code)

    expected_selected = set(selected_codes)
    discovered_specs = {
        path.stem for path in (root / "pipeline" / "specs_v4_1").glob("*.json") if path.is_file()
    }
    discovered_prompts = {
        path.stem for path in (root / "pipeline" / "prompts_v4_1").glob("*.md") if path.is_file()
    }
    discovered_datasets = {
        path.stem for path in (root / "pipeline" / "datasets" / "v4_1").glob("*.json")
        if path.is_file()
    }
    if discovered_specs != expected_selected:
        raise ContractError("v4.1 specs must equal the exact ten selected codes")
    if discovered_prompts != expected_selected:
        raise ContractError("v4.1 prompts must equal the exact ten selected codes")
    if discovered_datasets != set(TARGET_CODES):
        raise ContractError("normalized v4.1 datasets must equal the exact 63-code fleet")
    return sorted(required, key=lambda value: value.encode("utf-8"))


def derive_freeze_plan(contract_path=DEFAULT_CONTRACT, root=REPO):
    """Derive the complete canonical pre-commit plan from frozen memberships."""
    root = Path(root).resolve()
    contract_file = _repo_file(root, contract_path)
    contract = load_json(contract_file)
    membership = load_json(_repo_file(root, HOLDOUT_MEMBERSHIP_PATH))
    paths = required_paths(contract, membership, root)
    for relative in paths:
        if relative != FREEZE_PLAN_PATH:
            _repo_file(root, relative)
    return {"files": paths}


def write_or_check_freeze_plan(contract_path=DEFAULT_CONTRACT, root=REPO, *, check=False):
    """Write or byte-check the hard-bound canonical freeze plan."""
    root = Path(root).resolve()
    expected = canonical_bytes(derive_freeze_plan(contract_path, root))
    output = _repo_file(root, FREEZE_PLAN_PATH, must_exist=False)
    if check:
        if output.read_bytes() != expected:
            raise ContractError("freeze plan differs from the derived canonical completeness plan")
    else:
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_bytes(expected)
    return output


def artifact_completeness_errors(contract, manifest, manifest_path, root=REPO):
    errors = contract_errors(contract)
    manifest_errors, members = _manifest_errors(manifest, manifest_path, root)
    errors.extend(manifest_errors)
    try:
        membership = load_json(_repo_file(root, HOLDOUT_MEMBERSHIP_PATH))
        required = required_paths(contract, membership, root)
    except (OSError, json.JSONDecodeError, ContractError, TypeError, ValueError) as exc:
        return errors + ["cannot derive required freeze membership: %s" % exc]
    missing = sorted(set(required) - set(members), key=lambda value: value.encode("utf-8"))
    if missing:
        errors.append("freeze manifest omits required paths: %s" % missing)
    unexpected = sorted(set(members) - set(required), key=lambda value: value.encode("utf-8"))
    if unexpected:
        errors.append("freeze manifest contains paths outside the closed freeze plan: %s" % unexpected)

    try:
        change_control = load_json(_repo_file(root, CHANGE_CONTROL_PATH))
        if change_control != CHANGE_CONTROL:
            errors.append("change-control artifact differs from the frozen outcome-independent contract")
    except (OSError, json.JSONDecodeError, ContractError, ValueError) as exc:
        errors.append("change-control artifact is invalid: %s" % exc)
    try:
        regression = load_json(_repo_file(root, REGRESSION_MEMBERSHIP_PATH))
        if regression != REGRESSION_MEMBERSHIP:
            errors.append("regression-membership artifact differs from the exact disclosed cohort")
    except (OSError, json.JSONDecodeError, ContractError, ValueError) as exc:
        errors.append("regression-membership artifact is invalid: %s" % exc)
    try:
        routes = load_json(_repo_file(root, MODEL_ROUTES_PATH))
        if routes != MODEL_ROUTES:
            errors.append("model-routes artifact differs from the exact v4.1 routing contract")
    except (OSError, json.JSONDecodeError, ContractError, ValueError) as exc:
        errors.append("model-routes artifact is invalid: %s" % exc)
    return errors


def _receipt_common(receipt, kind, root_digest, manifest_digest):
    if not isinstance(receipt, dict):
        raise ContractError("%s receipt must be an object" % kind)
    if receipt.get("receipt_version") != RECEIPT_VERSION or receipt.get("kind") != kind:
        raise ContractError("%s receipt version/kind mismatch" % kind)
    if receipt.get("root_sha256") != root_digest:
        raise ContractError("%s receipt does not bind the freeze root" % kind)
    if receipt.get("manifest_sha256") != manifest_digest:
        raise ContractError("%s receipt does not bind the exact freeze manifest bytes" % kind)


def _run_git(root, args):
    return subprocess.run(
        ["git", "-C", str(Path(root).resolve()), *args],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )


def _git_output(root, args, label, git_runner):
    completed = git_runner(root, args)
    if completed.returncode != 0:
        detail = completed.stderr.decode("utf-8", errors="replace").strip()
        raise ContractError("%s failed%s" % (label, ": " + detail if detail else ""))
    return completed.stdout


def _repository_authorization_errors(
        manifest, manifest_path, commit, tag, root, git_runner=None):
    """Verify the receipts against actual immutable Git objects, read-only."""
    errors = []
    git_runner = git_runner or _run_git
    root = Path(root).resolve()
    manifest_path = Path(manifest_path).resolve()
    try:
        manifest_relative = manifest_path.relative_to(root).as_posix()
    except ValueError:
        return ["freeze manifest must be inside the repository for Git authorization"]
    if manifest_relative != FREEZE_MANIFEST_PATH:
        return ["freeze manifest must use the canonical repository path %s" %
                FREEZE_MANIFEST_PATH]
    try:
        commit_sha = commit["commit_sha"]
        tag_name = tag["tag_name"]
        tag_ref = "refs/tags/" + tag_name
        _git_output(root, ["cat-file", "-e", commit_sha + "^{commit}"],
                    "commit object verification", git_runner)
        committed_manifest = _git_output(
            root, ["show", "%s:%s" % (commit_sha, manifest_relative)],
            "committed freeze-manifest lookup", git_runner,
        )
        if committed_manifest != manifest_path.read_bytes():
            raise ContractError("commit does not contain the exact freeze manifest bytes")
        for item in manifest.get("files", []):
            if (not isinstance(item, dict)
                    or set(item) != {"path", "byte_length", "sha256"}):
                raise ContractError("cannot authorize malformed freeze-manifest members")
            object_spec = "%s:%s" % (commit_sha, item["path"])
            object_type = _git_output(
                root, ["cat-file", "-t", object_spec],
                "frozen member object-type verification for %s" % item["path"], git_runner,
            ).strip()
            if object_type != b"blob":
                raise ContractError("frozen manifest member is not a Git blob: %s" % item["path"])
            committed_bytes = _git_output(
                root, ["show", object_spec],
                "frozen member lookup for %s" % item["path"], git_runner,
            )
            if (len(committed_bytes) != item["byte_length"]
                    or sha256_bytes(committed_bytes) != item["sha256"]):
                raise ContractError(
                    "authorized commit bytes differ from frozen member digest: %s" % item["path"]
                )

        tag_type = _git_output(root, ["cat-file", "-t", tag_ref],
                               "tag object type verification", git_runner).strip()
        if tag_type != b"tag":
            raise ContractError("freeze tag is not an actual annotated tag object")
        actual_tag_oid = _git_output(root, ["rev-parse", tag_ref],
                                     "tag object identity verification", git_runner).decode().strip()
        if actual_tag_oid != tag["tag_object_sha"]:
            raise ContractError("tag receipt tag_object_sha differs from the actual tag object")
        actual_commit = _git_output(root, ["rev-parse", tag_ref + "^{commit}"],
                                    "tag commit verification", git_runner).decode().strip()
        if actual_commit != commit_sha:
            raise ContractError("annotated tag does not point to the receipt commit")
        tag_object = _git_output(root, ["cat-file", "-p", tag_ref],
                                 "annotated tag payload verification", git_runner)
        header, separator, message = tag_object.partition(b"\n\n")
        expected_headers = (b"object " + commit_sha.encode("ascii"), b"type commit")
        if not separator or any(line not in header.splitlines() for line in expected_headers):
            raise ContractError("annotated tag does not directly identify the receipt commit")
        if manifest["root_sha256"].encode("ascii") not in message:
            raise ContractError("annotated tag message does not bind the freeze root digest")
        if b"-----BEGIN SSH SIGNATURE-----" not in message:
            raise ContractError("annotated tag does not contain an SSH signature")
        allowed_signers = _repo_file(root, ALLOWED_SIGNERS_PATH).read_text(encoding="utf-8")
        principals = set()
        for line in allowed_signers.splitlines():
            stripped = line.strip()
            if not stripped or stripped.startswith("#"):
                continue
            fields = stripped.split()
            if len(fields) < 3:
                raise ContractError("frozen SSH allowed-signers file is malformed")
            principals.update(fields[0].split(","))
        if principals != {ALLOWED_SIGNER_PRINCIPAL}:
            raise ContractError("frozen SSH allowed-signers principal must be exactly %s" %
                                ALLOWED_SIGNER_PRINCIPAL)
        if tag.get("signer_identity") != ALLOWED_SIGNER_PRINCIPAL:
            raise ContractError("tag receipt signer_identity does not match the frozen principal")
        _git_output(root, [
            "-c", "gpg.ssh.allowedSignersFile=" + ALLOWED_SIGNERS_PATH,
            "verify-tag", "--raw", tag_ref,
        ],
                    "cryptographic tag-signature verification", git_runner)
    except (ContractError, KeyError, OSError, UnicodeError) as exc:
        errors.append(str(exc))
    return errors


def authorization_errors(manifest, manifest_path, commit, tag, ci, root=REPO, git_runner=None):
    errors = []
    root_digest = manifest.get("root_sha256") if isinstance(manifest, dict) else None
    try:
        manifest_digest = sha256_file(manifest_path)
    except OSError as exc:
        return ["cannot hash freeze manifest for authorization: %s" % exc]
    if not isinstance(root_digest, str) or not HEX64_RE.fullmatch(root_digest):
        return ["cannot authorize an invalid freeze root digest"]

    commit_keys = {
        "receipt_version", "kind", "root_sha256", "manifest_sha256", "commit_sha",
        "committed_at",
    }
    tag_keys = {
        "receipt_version", "kind", "root_sha256", "manifest_sha256", "commit_sha",
        "tag_name", "tag_object_sha", "annotated", "signed", "signature_verified",
        "signer_identity", "tagged_at",
    }
    ci_keys = {
        "receipt_version", "kind", "root_sha256", "manifest_sha256", "commit_sha",
        "tag_name", "provider", "github_owner", "github_repository", "workflow_path",
        "workflow_id", "run_id", "run_attempt", "run_api_url", "run_html_url",
        "artifacts_api_url", "event", "conclusion", "run_started_at", "run_updated_at",
        "artifact_id", "artifact_name", "artifact_api_url", "artifact_archive_download_url",
        "artifact_digest", "artifact_created_at", "artifact_updated_at", "issued_at",
    }
    try:
        _receipt_common(commit, "commit", root_digest, manifest_digest)
        if set(commit) != commit_keys:
            raise ContractError("commit receipt keys are not closed")
        if not isinstance(commit.get("commit_sha"), str) or not GIT_OID_RE.fullmatch(commit["commit_sha"]):
            raise ContractError("commit receipt commit_sha is invalid")
        committed_at = _iso_timestamp(commit.get("committed_at"), "commit.committed_at")

        _receipt_common(tag, "tag", root_digest, manifest_digest)
        if set(tag) != tag_keys:
            raise ContractError("tag receipt keys are not closed")
        if tag.get("commit_sha") != commit["commit_sha"]:
            raise ContractError("tag receipt commit does not match commit receipt")
        if not isinstance(tag.get("tag_object_sha"), str) or not GIT_OID_RE.fullmatch(tag["tag_object_sha"]):
            raise ContractError("tag receipt tag_object_sha is invalid")
        if not isinstance(tag.get("tag_name"), str) or not TAG_RE.fullmatch(tag["tag_name"]):
            raise ContractError("tag receipt tag_name is invalid")
        if not tag["tag_name"].startswith("v4.1-freeze-"):
            raise ContractError("tag receipt tag_name is outside the frozen release namespace")
        if tag.get("annotated") is not True or tag.get("signed") is not True or tag.get("signature_verified") is not True:
            raise ContractError("tag receipt must attest an annotated, signed, verified tag")
        if not isinstance(tag.get("signer_identity"), str) or not tag["signer_identity"].strip():
            raise ContractError("tag receipt signer_identity is required")
        tagged_at = _iso_timestamp(tag.get("tagged_at"), "tag.tagged_at")
        if tagged_at < committed_at:
            raise ContractError("tag receipt predates the frozen commit")

        _receipt_common(ci, "ci", root_digest, manifest_digest)
        if set(ci) != ci_keys:
            raise ContractError("CI receipt keys are not closed")
        if ci.get("commit_sha") != commit["commit_sha"] or ci.get("tag_name") != tag["tag_name"]:
            raise ContractError("CI receipt does not bind the commit and tag")
        if ci.get("workflow_path") != FREEZE_CI_WORKFLOW_PATH:
            raise ContractError("CI receipt does not bind the frozen verification workflow")
        if ci.get("provider") != "github-actions":
            raise ContractError("CI receipt provider must be github-actions")
        if (ci.get("github_owner") != GITHUB_OWNER
                or ci.get("github_repository") != GITHUB_REPOSITORY):
            raise ContractError("CI receipt must bind the exact GitHub owner/repository")
        if (not isinstance(ci.get("workflow_id"), int) or isinstance(ci["workflow_id"], bool)
                or ci["workflow_id"] <= 0):
            raise ContractError("CI receipt workflow_id must be a positive integer")
        if not isinstance(ci.get("run_id"), int) or isinstance(ci["run_id"], bool) or ci["run_id"] <= 0:
            raise ContractError("CI receipt run_id must be a positive integer")
        if (not isinstance(ci.get("run_attempt"), int) or isinstance(ci["run_attempt"], bool)
                or ci["run_attempt"] <= 0):
            raise ContractError("CI receipt run_attempt must be a positive integer")
        api_base = "https://api.github.com/repos/%s/%s" % (GITHUB_OWNER, GITHUB_REPOSITORY)
        run_api_url = "%s/actions/runs/%s" % (api_base, ci["run_id"])
        expected_urls = {
            "run_api_url": run_api_url,
            "run_html_url": "https://github.com/%s/%s/actions/runs/%s" %
                            (GITHUB_OWNER, GITHUB_REPOSITORY, ci["run_id"]),
            "artifacts_api_url": run_api_url + "/artifacts",
        }
        for key, expected in expected_urls.items():
            if ci.get(key) != expected:
                raise ContractError("CI receipt %s is not the exact GitHub proof URL" % key)
        if not isinstance(ci.get("artifact_id"), int) or isinstance(ci["artifact_id"], bool) or ci["artifact_id"] <= 0:
            raise ContractError("CI receipt artifact_id must be a positive integer")
        artifact_api_url = "%s/actions/artifacts/%s" % (api_base, ci["artifact_id"])
        if ci.get("artifact_api_url") != artifact_api_url:
            raise ContractError("CI receipt artifact_api_url is not canonical")
        if ci.get("artifact_archive_download_url") != artifact_api_url + "/zip":
            raise ContractError("CI receipt artifact_archive_download_url is not canonical")
        if ci.get("artifact_name") != "v4.1-freeze-" + commit["commit_sha"]:
            raise ContractError("CI receipt artifact_name does not bind the frozen commit")
        digest = ci.get("artifact_digest")
        if (not isinstance(digest, str) or not digest.startswith("sha256:")
                or not HEX64_RE.fullmatch(digest[7:])):
            raise ContractError("CI receipt artifact_digest must be a GitHub SHA-256 digest")
        if ci.get("event") != "push":
            raise ContractError("CI receipt event must be push")
        if ci.get("conclusion") != "success":
            raise ContractError("CI receipt conclusion must be success")
        run_started_at = _iso_timestamp(ci.get("run_started_at"), "ci.run_started_at")
        run_updated_at = _iso_timestamp(ci.get("run_updated_at"), "ci.run_updated_at")
        artifact_created_at = _iso_timestamp(
            ci.get("artifact_created_at"), "ci.artifact_created_at"
        )
        artifact_updated_at = _iso_timestamp(
            ci.get("artifact_updated_at"), "ci.artifact_updated_at"
        )
        issued_at = _iso_timestamp(ci.get("issued_at"), "ci.issued_at")
        if run_started_at < tagged_at:
            raise ContractError("CI run predates the signed tag")
        if run_updated_at < run_started_at:
            raise ContractError("CI run update predates its start")
        if artifact_created_at < run_started_at:
            raise ContractError("CI artifact predates its run")
        if artifact_updated_at < artifact_created_at:
            raise ContractError("CI artifact update predates its creation")
        if issued_at < max(run_updated_at, artifact_updated_at):
            raise ContractError("CI receipt predates the GitHub evidence timestamps")
    except ContractError as exc:
        errors.append(str(exc))
    if not errors:
        errors.extend(_repository_authorization_errors(
            manifest, manifest_path, commit, tag, root, git_runner=git_runner,
        ))
    return errors


def validate(contract_path, manifest_path, commit_path, tag_path, ci_path, root=REPO,
             git_runner=None):
    errors = []
    try:
        contract = load_json(contract_path)
        manifest = load_json(manifest_path)
        commit = load_json(commit_path)
        tag = load_json(tag_path)
        ci = load_json(ci_path)
    except (OSError, json.JSONDecodeError, ContractError, ValueError) as exc:
        return ["freeze-contract input failed: %s" % exc]
    errors.extend(artifact_completeness_errors(contract, manifest, manifest_path, root))
    errors.extend(authorization_errors(
        manifest, manifest_path, commit, tag, ci, root=root, git_runner=git_runner,
    ))
    return errors


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--contract", default=DEFAULT_CONTRACT)
    plan_mode = parser.add_mutually_exclusive_group()
    plan_mode.add_argument("--write-plan", action="store_true")
    plan_mode.add_argument("--check-plan", action="store_true")
    parser.add_argument("--manifest")
    parser.add_argument("--commit-receipt")
    parser.add_argument("--tag-receipt")
    parser.add_argument("--ci-receipt")
    parser.add_argument("--repo-root", default=str(REPO))
    args = parser.parse_args(argv)
    if args.write_plan or args.check_plan:
        try:
            output = write_or_check_freeze_plan(
                args.contract, Path(args.repo_root), check=args.check_plan,
            )
        except (OSError, json.JSONDecodeError, ContractError, ValueError) as exc:
            print("FREEZE PLAN FAILED: %s" % exc, file=sys.stderr)
            return 1
        verb = "verified" if args.check_plan else "wrote"
        print("OK: %s canonical v4.1 freeze plan: %s" % (verb, output))
        return 0
    missing_args = [
        name for name, value in (
            ("--manifest", args.manifest),
            ("--commit-receipt", args.commit_receipt),
            ("--tag-receipt", args.tag_receipt),
            ("--ci-receipt", args.ci_receipt),
        ) if not value
    ]
    if missing_args:
        parser.error("authorization validation requires %s" % ", ".join(missing_args))
    errors = validate(
        args.contract, args.manifest, args.commit_receipt, args.tag_receipt,
        args.ci_receipt, Path(args.repo_root),
    )
    if errors:
        print("V4.1 FREEZE CONTRACT FAILED:", file=sys.stderr)
        for error in errors:
            print("  " + error, file=sys.stderr)
        return 1
    print("OK: v4.1 Section 14 artifacts and authorization receipts are complete")
    return 0


if __name__ == "__main__":
    sys.exit(main())
