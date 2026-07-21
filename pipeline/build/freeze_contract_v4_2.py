#!/usr/bin/env python3
"""Derive and validate the complete v4.2 §15 freeze and authorization."""

import argparse
from datetime import datetime, timezone
import hashlib
import importlib.util
import json
from pathlib import Path, PurePosixPath
import re
import subprocess
import sys


REPO = Path(__file__).resolve().parent.parent.parent
CONTRACT_PATH = "pipeline/build/freeze_contract_v4_2.required.json"
PLAN_PATH = "pipeline/v4_2/freeze_plan.json"
MANIFEST_PATH = "pipeline/v4_2/freeze_manifest.json"
HOLDOUT_PATH = "pipeline/v4_2/holdout_membership.json"
REGRESSION_PATH = "pipeline/v4_2/regression_membership.json"
ROUTES_PATH = "pipeline/v4_2/model_routes.json"
CHANGE_CONTROL_PATH = "pipeline/v4_2/change_control.json"
ALLOWED_SIGNERS_PATH = "pipeline/v4_2/allowed_signers"
WORKFLOW_PATH = ".github/workflows/v4-2-freeze.yml"
EXTENSION_WORKFLOW_PATH = ".github/workflows/v4-2-full-scope-extension.yml"
TARGETS_PATH = "pipeline/blocks/targets_phase3.json"
GOLDEN_PATH = "pipeline/golden/golden_set.json"
CONTRACT_VERSION = "v4.2-section15-completeness-1"
MANIFEST_VERSION = "v4.2-freeze-1"
RECEIPT_VERSION = "v4.2-authorization-receipt-1"
SIGNER_PRINCIPAL = "jkee"
GITHUB_OWNER = "jkee"
GITHUB_REPOSITORY = "rollup-economy"
REGRESSION_CODES = ("238220", "541214", "541511", "541512", "541930")
HOLDOUT_CODES = ("541890", "541340", "541370", "541199", "541420")
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
TEMPLATES = (
    "pipeline/template/prompt_template_v4_2.md",
    "pipeline/template/runner_brief_v4_2.md",
    "pipeline/template/validator_brief_v4_2.md",
)
REQUIRED_SCHEMAS = (
    "pipeline/build/schemas/dataset_v4_2.schema.json",
    "pipeline/build/schemas/industry_spec_v4_2.schema.json",
    "pipeline/build/schemas/output_claim_receipt_v4_2.schema.json",
    "pipeline/build/schemas/research_packet_v4_2.schema.json",
    "pipeline/build/schemas/review_record_v4_2.schema.json",
    "pipeline/build/schemas/run_record_v4_2.schema.json",
)
CRITICAL_BUILD_PATHS = (
    "pipeline/build/build_gate_report_v4_2.py",
    "pipeline/build/build_runtime_methodology_v4_2.py",
    "pipeline/build/campaign_v4_2.py",
    "pipeline/build/finalize_run_v4_2.py",
    "pipeline/build/freeze_contract_v4_2.py",
    "pipeline/build/freeze_v4_2.py",
    "pipeline/build/guarded_write_v4_2.py",
    "pipeline/build/issue_campaign_v4_2.py",
    "pipeline/build/issue_gate_certificate_v4_2.py",
    "pipeline/build/normalize_datasets_v4_2.py",
    "pipeline/build/select_holdout_v4_2.py",
    "pipeline/build/test_freeze_contract_v4_2.py",
    "pipeline/build/test_full_issuance_authority_v4_2.py",
    "pipeline/build/test_gate_report_v4_2.py",
    "pipeline/build/test_guarded_write_v4_2.py",
    "pipeline/build/test_holdout_v4_2.py",
    "pipeline/build/test_issue_campaign_v4_2.py",
    "pipeline/build/test_normalize_datasets_v4_2.py",
    "pipeline/build/test_prompt_v4_2.py",
    "pipeline/build/test_remediation_comparator_v4_2.py",
    "pipeline/build/test_remediation_issuance_v4_2.py",
    "pipeline/build/test_runtime_methodology_v4_2.py",
    "pipeline/build/test_v4_2_campaign.py",
    "pipeline/build/test_v4_2_finalizer.py",
    "pipeline/build/test_v4_2_scoring.py",
    "pipeline/build/test_validate_full_scope_extension_v4_2.py",
    "pipeline/build/validate_full_scope_extension_v4_2.py",
    "pipeline/build/v4_2_scoring.py",
)
BASE_PATHS = (
    WORKFLOW_PATH, EXTENSION_WORKFLOW_PATH, "V4_1_REJECTION.md", "V4_2_METHODOLOGY.md",
    "V4_2_RUNTIME_METHODOLOGY.md", TARGETS_PATH,
    GOLDEN_PATH, "pipeline/build/assemble_prompts.py", "pipeline/build/build.py",
    "pipeline/build/campaign_v4_1.py", "pipeline/build/issue_campaign_v4_1.py",
    "pipeline/build/issue_gate_certificate_v4_1.py", CONTRACT_PATH,
    "pipeline/build/normalize_datasets_v4_1.py",
    "pipeline/build/schemas/dataset_v4_1.schema.json",
    "pipeline/build/thresholds_v4_2.json", *TEMPLATES, ALLOWED_SIGNERS_PATH,
    CHANGE_CONTROL_PATH, PLAN_PATH, HOLDOUT_PATH, ROUTES_PATH, REGRESSION_PATH,
)
MODEL_ROUTES = {
    "route_version": "v4.2-neutral-model-routes-1",
    "research": {"target": "gpt-5.6-terra"},
    "review": {"all": "gpt-5.6-sol"},
    "execution": {
        "fork_policy": "none", "issued_by_task_path": "/root",
        "research_role": "research", "review_role": "reviewer",
    },
}
CHANGE_CONTROL = {
    "change_control_version": "v4.2-change-control-1",
    "allowed_new_version_triggers": [
        "mathematical_directionality_or_sentinel_failure",
        "construct_contradiction_or_double_count",
        "schema_scoring_or_reproduction_mismatch",
        "review_or_evidence_contract_failure",
        "preregistered_evidence_infeasibility",
    ],
    "forbidden_triggers": [
        "named_score", "named_rank", "named_color", "named_verdict",
        "named_distribution", "named_movement_from_earlier_version",
    ],
    "evidence_infeasibility_rule": {
        "critical_unbounded_count": 2, "set_size": 5,
        "treatment": "reject_v4_2_and_create_v4_3_with_new_salted_untouched_holdout",
    },
    "viewed_holdout_treatment": "burned_for_future_methodology_versions",
    "replacement_version_rule": "new_salt_and_untouched_holdout_required",
    "superseded_artifact_treatment": "preserve_without_reinterpretation",
}
REGRESSION_MEMBERSHIP = {
    "membership_version": "v4.2-regression-1",
    "purpose": "Disclosed development regression set; not holdout evidence",
    "selected_codes": list(REGRESSION_CODES),
    "selection_rule": (
        "The fixed five-record evidence-feasibility set disclosed in "
        "V4_2_METHODOLOGY.md section 12"
    ),
}
HEX64 = re.compile(r"^[0-9a-f]{64}$")
GIT_OID = re.compile(r"^[0-9a-f]{40}(?:[0-9a-f]{24})?$")
NAICS = re.compile(r"^[0-9]{6}$")
TAG = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._/-]*$")


class ContractError(ValueError):
    """A closed v4.2 freeze or authorization contract failed."""


def _closed_pairs(pairs):
    value = {}
    for key, item in pairs:
        if key in value:
            raise ContractError("duplicate JSON key %r" % key)
        value[key] = item
    return value


def _reject_constant(value):
    raise ContractError("non-standard JSON constant %r is forbidden" % value)


def load_json(path):
    with Path(path).open("r", encoding="utf-8") as handle:
        return json.load(
            handle, object_pairs_hook=_closed_pairs, parse_constant=_reject_constant,
        )


def canonical_bytes(value):
    return json.dumps(
        value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False,
    ).encode("utf-8")


def sha256_bytes(value):
    return hashlib.sha256(value).hexdigest()


def sha256_file(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def repository_file(root, relative, must_exist=True):
    if not isinstance(relative, str) or not relative or "\\" in relative or "\0" in relative:
        raise ContractError("path must be a repository-relative POSIX string")
    pure = PurePosixPath(relative)
    if pure.is_absolute() or any(part in ("", ".", "..") for part in pure.parts):
        raise ContractError("unsafe repository path: %s" % relative)
    root = Path(root).resolve()
    path = root.joinpath(*pure.parts).resolve()
    try:
        path.relative_to(root)
    except ValueError as exc:
        raise ContractError("path escapes repository: %s" % relative) from exc
    if must_exist and not path.is_file():
        raise ContractError("required file does not exist: %s" % relative)
    return path


def root_sha256(files):
    digest = hashlib.sha256()
    for item in sorted(files, key=lambda row: row["path"].encode("utf-8")):
        digest.update(item["path"].encode("utf-8")); digest.update(b"\0")
        digest.update(str(item["byte_length"]).encode("ascii")); digest.update(b"\0")
        digest.update(item["sha256"].encode("ascii")); digest.update(b"\n")
    return digest.hexdigest()


def _iso_timestamp(value, label):
    if not isinstance(value, str) or not value:
        raise ContractError("%s must be an ISO-8601 timestamp" % label)
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


def _discover(root):
    root = Path(root)
    build = sorted(
        path.relative_to(root).as_posix()
        for path in (root / "pipeline/build").glob("*v4_2*.py") if path.is_file()
    )
    schemas = sorted(
        path.relative_to(root).as_posix()
        for path in (root / "pipeline/build/schemas").glob("*_v4_2.schema.json")
        if path.is_file()
    )
    templates = sorted(
        path.relative_to(root).as_posix()
        for path in (root / "pipeline/template").glob("*v4_2*") if path.is_file()
    )
    return build, schemas, templates


def contract_errors(contract, root=REPO):
    keys = {
        "contract_version", "methodology_version", "freeze_manifest_version",
        "regression_codes", "holdout_codes", "base_paths", "versioned_build_paths",
        "versioned_schema_paths", "versioned_template_paths", "model_routes",
        "dataset_contract", "selected_artifact_contract",
    }
    if not isinstance(contract, dict):
        return ["contract must be an object"]
    errors = []
    if set(contract) != keys:
        errors.append("contract keys are not closed")
    expected_scalars = {
        "contract_version": CONTRACT_VERSION, "methodology_version": "4.2",
        "freeze_manifest_version": MANIFEST_VERSION,
        "regression_codes": list(REGRESSION_CODES), "holdout_codes": list(HOLDOUT_CODES),
        "base_paths": sorted(BASE_PATHS), "model_routes": MODEL_ROUTES,
        "dataset_contract": {
            "count": 63, "directory": "pipeline/datasets/v4_2",
            "dataset_version": "4.2", "derivation_version": "normalize-v4.2-1",
            "legacy_source_directory": "pipeline/datasets/derived",
            "holdout_snapshot_directory": "pipeline/datasets/v4_1",
        },
        "selected_artifact_contract": {
            "count": 10, "spec_directory": "pipeline/specs_v4_2",
            "prompt_directory": "pipeline/prompts_v4_2",
            "codes": sorted((*REGRESSION_CODES, *HOLDOUT_CODES)),
        },
    }
    for key, expected in expected_scalars.items():
        if contract.get(key) != expected:
            errors.append("%s differs from the exact v4.2 contract" % key)
    build, schemas, templates = _discover(root)
    if contract.get("versioned_build_paths") != build:
        errors.append("versioned_build_paths must equal every discovered v4.2 build artifact")
    if not set(CRITICAL_BUILD_PATHS).issubset(build):
        errors.append("critical v4.2 build artifacts are missing: %s" %
                      sorted(set(CRITICAL_BUILD_PATHS) - set(build)))
    if contract.get("versioned_schema_paths") != schemas:
        errors.append("versioned_schema_paths must equal every discovered v4.2 schema")
    if not set(REQUIRED_SCHEMAS).issubset(schemas):
        errors.append("required v4.2 schemas are missing")
    if contract.get("versioned_template_paths") != templates or templates != sorted(TEMPLATES):
        errors.append("versioned_template_paths must equal the exact three v4.2 templates")
    return errors


def _target_codes(root):
    targets = load_json(repository_file(root, TARGETS_PATH))
    if not isinstance(targets, dict) or set(targets) != {"version", "description", "codes"}:
        raise ContractError("target membership is not closed")
    codes = []
    for row in targets.get("codes", []):
        if (not isinstance(row, dict) or set(row) != {"naics", "title", "golden"}
                or not isinstance(row.get("naics"), str) or not NAICS.fullmatch(row["naics"])):
            raise ContractError("target membership row is malformed")
        codes.append(row["naics"])
    if codes != list(TARGET_CODES) or len(set(codes)) != 63:
        raise ContractError("target membership differs from the exact 63-code fleet")
    return codes


def _membership_errors(root):
    errors = []
    try:
        regression = load_json(repository_file(root, REGRESSION_PATH))
        if regression != REGRESSION_MEMBERSHIP:
            errors.append("regression membership differs from the exact disclosed cohort")
        holdout = load_json(repository_file(root, HOLDOUT_PATH))
        if holdout.get("selected_codes") != list(HOLDOUT_CODES):
            errors.append("holdout membership differs from the exact salted selection")
        bins = holdout.get("bins")
        if (not isinstance(bins, list) or len(bins) != 5
                or [item.get("selected_naics") for item in bins if isinstance(item, dict)]
                != list(HOLDOUT_CODES)):
            errors.append("holdout bins do not bind the exact selected cohort")
        source_digests = holdout.get("source_digests")
        if not isinstance(source_digests, list) or len(source_digests) != 85:
            errors.append("holdout membership must bind exactly 85 selection source digests")
        else:
            seen = set()
            for record in source_digests:
                if (not isinstance(record, dict)
                        or set(record) != {"path", "byte_length", "sha256"}
                        or record.get("path") in seen):
                    errors.append("holdout source-digest records must be closed and unique")
                    break
                seen.add(record["path"])
                try:
                    path = repository_file(root, record["path"])
                    if (path.stat().st_size != record["byte_length"]
                            or sha256_file(path) != record["sha256"]):
                        errors.append("holdout source digest is stale: %s" % record["path"])
                        break
                except (ContractError, TypeError, KeyError) as exc:
                    errors.append("holdout source digest is invalid: %s" % exc)
                    break
    except (OSError, ValueError, TypeError, json.JSONDecodeError) as exc:
        errors.append("membership validation failed: %s" % exc)
    return errors


def _dataset_errors(root):
    errors = []
    root = Path(root)
    expected = set(TARGET_CODES)
    exact_directories = {
        "v4.2 normalized": root / "pipeline/datasets/v4_2",
        "v4.1 holdout snapshot": root / "pipeline/datasets/v4_1",
    }
    for label, directory in exact_directories.items():
        actual = {path.stem for path in directory.glob("*.json") if path.is_file()}
        if actual != expected:
            errors.append("%s datasets must equal the exact 63-code fleet" % label)
    legacy = {
        path.stem for path in (root / "pipeline/datasets/derived").glob("*.json")
        if path.is_file()
    }
    if not expected.issubset(legacy):
        errors.append("legacy source datasets omit required target-fleet inputs")
    for code in TARGET_CODES:
        try:
            value = load_json(root / "pipeline/datasets/v4_2" / (code + ".json"))
            provenance = value.get("provenance") if isinstance(value, dict) else None
            source = root / "pipeline/datasets/derived" / (code + ".json")
            if (value.get("dataset_version") != "4.2" or value.get("naics") != code
                    or not isinstance(provenance, dict)
                    or provenance.get("derivation_version") != "normalize-v4.2-1"
                    or provenance.get("source_manifest_sha256") != sha256_file(source)):
                errors.append("v4.2 dataset provenance/digest mismatch: %s" % code)
        except (OSError, ValueError, TypeError, json.JSONDecodeError) as exc:
            errors.append("v4.2 dataset validation failed for %s: %s" % (code, exc))
    return errors


def _runtime_methodology_errors(root):
    """Bind the public derivative to a fresh build from the full governance method."""
    root = Path(root).resolve()
    builder_path = root / "pipeline/build/build_runtime_methodology_v4_2.py"
    try:
        spec = importlib.util.spec_from_file_location(
            "freeze_runtime_methodology_v4_2", builder_path,
        )
        if spec is None or spec.loader is None:
            return ["v4.2 runtime methodology builder cannot be loaded"]
        builder = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(builder)
        expected = builder.derive_runtime_bytes(root / "V4_2_METHODOLOGY.md")
        actual = (root / "V4_2_RUNTIME_METHODOLOGY.md").read_bytes()
        if actual != expected:
            return ["v4.2 runtime methodology differs from fresh deterministic derivation"]
    except Exception as exc:
        return ["v4.2 runtime methodology validation failed: %s" % exc]
    return []


def required_paths(contract, root=REPO):
    errors = contract_errors(contract, root)
    if errors:
        raise ContractError("; ".join(errors))
    _target_codes(root)
    membership_errors = _membership_errors(root)
    dataset_errors = _dataset_errors(root)
    runtime_errors = _runtime_methodology_errors(root)
    if membership_errors or dataset_errors or runtime_errors:
        raise ContractError("; ".join((*membership_errors, *dataset_errors, *runtime_errors)))
    if load_json(repository_file(root, ROUTES_PATH)) != MODEL_ROUTES:
        raise ContractError("model routes differ from the exact v4.2 routes")
    if load_json(repository_file(root, CHANGE_CONTROL_PATH)) != CHANGE_CONTROL:
        raise ContractError("change control differs from the outcome-independent rubric")
    selected = set((*REGRESSION_CODES, *HOLDOUT_CODES))
    root = Path(root)
    specs = {path.stem for path in (root / "pipeline/specs_v4_2").glob("*.json") if path.is_file()}
    prompts = {path.stem for path in (root / "pipeline/prompts_v4_2").glob("*.md") if path.is_file()}
    if specs != selected or prompts != selected:
        raise ContractError("v4.2 specs and prompts must each equal the exact ten preselected codes")
    methodology_digest = sha256_file(root / "V4_2_RUNTIME_METHODOLOGY.md")
    target_rows = load_json(root / TARGETS_PATH)["codes"]
    titles = {row["naics"]: row["title"] for row in target_rows}
    for code in selected:
        spec = load_json(root / "pipeline/specs_v4_2" / (code + ".json"))
        dataset_path = "pipeline/datasets/v4_2/%s.json" % code
        expected_dataset = {
            "path": dataset_path,
            "sha256": sha256_file(root / dataset_path),
        }
        expected_methodology = {
            "path": "V4_2_RUNTIME_METHODOLOGY.md", "sha256": methodology_digest,
        }
        if (spec.get("spec_version") != "4.2" or spec.get("naics") != code
                or spec.get("title") != titles[code]
                or spec.get("dataset_snapshot") != expected_dataset
                or spec.get("methodology_snapshot") != expected_methodology):
            raise ContractError("v4.2 spec snapshot binding is invalid: %s" % code)
    paths = set(contract["base_paths"])
    paths.update(contract["versioned_build_paths"])
    paths.update(contract["versioned_schema_paths"])
    paths.update(contract["versioned_template_paths"])
    for code in TARGET_CODES:
        paths.add("pipeline/datasets/v4_2/%s.json" % code)
        paths.add("pipeline/datasets/v4_1/%s.json" % code)
        paths.add("pipeline/datasets/derived/%s.json" % code)
    for code in selected:
        paths.add("pipeline/specs_v4_2/%s.json" % code)
        paths.add("pipeline/prompts_v4_2/%s.md" % code)
    for relative in paths:
        if relative != PLAN_PATH:
            repository_file(root, relative)
    return sorted(paths, key=lambda path: path.encode("utf-8"))


def derive_freeze_plan(contract_path=CONTRACT_PATH, root=REPO):
    root = Path(root).resolve()
    contract = load_json(repository_file(root, contract_path))
    return {"files": required_paths(contract, root)}


def write_or_check_plan(contract_path=CONTRACT_PATH, root=REPO, check=False):
    root = Path(root).resolve()
    output = repository_file(root, PLAN_PATH, must_exist=False)
    expected = canonical_bytes(derive_freeze_plan(contract_path, root))
    if check:
        if output.read_bytes() != expected:
            raise ContractError("freeze plan differs from canonical §15 derivation")
    else:
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_bytes(expected)
    return output


def _manifest_errors(manifest, manifest_path, root):
    errors, members = [], {}
    if not isinstance(manifest, dict) or set(manifest) != {"files", "manifest_version", "root_sha256"}:
        return ["freeze manifest is not a closed files/version/root object"], members
    if manifest.get("manifest_version") != MANIFEST_VERSION:
        errors.append("freeze manifest version mismatch")
    files = manifest.get("files")
    if not isinstance(files, list) or not files:
        return errors + ["freeze manifest files must be non-empty"], members
    paths = [item.get("path") for item in files if isinstance(item, dict)]
    if (len(paths) != len(files) or not all(isinstance(path, str) for path in paths)
            or paths != sorted(set(paths), key=lambda path: path.encode("utf-8"))):
        errors.append("freeze manifest paths must be bytewise sorted, unique strings")
    structurally_valid = True
    for item in files:
        if not isinstance(item, dict) or set(item) != {"path", "byte_length", "sha256"}:
            errors.append("freeze manifest member is not closed")
            structurally_valid = False
            continue
        path, length, digest = item["path"], item["byte_length"], item["sha256"]
        if (not isinstance(length, int) or isinstance(length, bool) or length < 0
                or not isinstance(digest, str) or not HEX64.fullmatch(digest)):
            errors.append("freeze manifest member metadata is malformed: %r" % path)
            structurally_valid = False
            continue
        try:
            absolute = repository_file(root, path)
            if absolute.stat().st_size != length or sha256_file(absolute) != digest:
                errors.append("freeze manifest member is stale: %s" % path)
            members[path] = item
        except ContractError as exc:
            errors.append(str(exc)); structurally_valid = False
    if structurally_valid and root_sha256(files) != manifest.get("root_sha256"):
        errors.append("freeze manifest root digest is stale")
    try:
        if Path(manifest_path).read_bytes() != canonical_bytes(manifest):
            errors.append("freeze manifest is not canonical compact JSON")
    except OSError as exc:
        errors.append("cannot read freeze manifest: %s" % exc)
    return errors, members


def artifact_completeness_errors(contract, manifest, manifest_path, root=REPO):
    errors = contract_errors(contract, root)
    manifest_errors, members = _manifest_errors(manifest, manifest_path, root)
    errors.extend(manifest_errors)
    try:
        required = required_paths(contract, root)
        missing = sorted(set(required) - set(members))
        extra = sorted(set(members) - set(required))
        if missing:
            errors.append("freeze manifest omits required paths: %s" % missing)
        if extra:
            errors.append("freeze manifest contains paths outside the closed plan: %s" % extra)
    except (OSError, ValueError, TypeError, json.JSONDecodeError) as exc:
        errors.append("cannot derive complete v4.2 freeze paths: %s" % exc)
    return errors


def _run_git(root, args):
    return subprocess.run(
        ["git", "-C", str(Path(root).resolve()), *args], stdout=subprocess.PIPE,
        stderr=subprocess.PIPE, check=False,
    )


def _git(root, args, label, runner):
    result = runner(root, args)
    if result.returncode:
        detail = result.stderr.decode("utf-8", errors="replace").strip()
        raise ContractError("%s failed%s" % (label, ": " + detail if detail else ""))
    return result.stdout


def _receipt_common(receipt, kind, root_digest, manifest_digest):
    if not isinstance(receipt, dict) or receipt.get("receipt_version") != RECEIPT_VERSION:
        raise ContractError("%s receipt version is invalid" % kind)
    if receipt.get("kind") != kind or receipt.get("root_sha256") != root_digest:
        raise ContractError("%s receipt does not bind the freeze root" % kind)
    if receipt.get("manifest_sha256") != manifest_digest:
        raise ContractError("%s receipt does not bind the manifest bytes" % kind)


def _git_authorization(manifest, manifest_path, commit, tag, root, runner):
    root = Path(root).resolve(); manifest_path = Path(manifest_path).resolve()
    try:
        relative = manifest_path.relative_to(root).as_posix()
    except ValueError as exc:
        raise ContractError("manifest is outside the repository") from exc
    if relative != MANIFEST_PATH:
        raise ContractError("manifest path must be exactly %s" % MANIFEST_PATH)
    commit_sha, tag_oid = commit["commit_sha"], tag["tag_object_sha"]
    _git(root, ["cat-file", "-e", commit_sha + "^{commit}"], "commit verification", runner)
    if _git(root, ["show", "%s:%s" % (commit_sha, relative)], "manifest blob lookup", runner) != manifest_path.read_bytes():
        raise ContractError("authorized commit does not contain exact manifest bytes")
    for item in manifest["files"]:
        spec = "%s:%s" % (commit_sha, item["path"])
        if _git(root, ["cat-file", "-t", spec], "member type verification", runner).strip() != b"blob":
            raise ContractError("authorized member is not a Git blob: %s" % item["path"])
        content = _git(root, ["show", spec], "member blob lookup", runner)
        if len(content) != item["byte_length"] or sha256_bytes(content) != item["sha256"]:
            raise ContractError("authorized commit member digest mismatch: %s" % item["path"])
    if _git(root, ["cat-file", "-t", tag_oid], "immutable tag type verification", runner).strip() != b"tag":
        raise ContractError("captured tag object is not annotated")
    payload = _git(root, ["cat-file", "-p", tag_oid], "immutable tag lookup", runner)
    header, separator, message = payload.partition(b"\n\n")
    lines = header.splitlines()
    required_headers = {
        b"object " + commit_sha.encode("ascii"), b"type commit",
        b"tag " + tag["tag_name"].encode("utf-8"),
    }
    if not separator or not required_headers.issubset(set(lines)):
        raise ContractError("immutable tag object does not directly bind commit and name")
    if manifest["root_sha256"].encode("ascii") not in message:
        raise ContractError("immutable tag message does not bind root digest")
    if b"-----BEGIN SSH SIGNATURE-----" not in message:
        raise ContractError("immutable tag object lacks an SSH signature")
    allowed = repository_file(root, ALLOWED_SIGNERS_PATH).read_text(encoding="utf-8")
    principals = {
        principal for line in allowed.splitlines() if line.strip() and not line.lstrip().startswith("#")
        for principal in line.split()[0].split(",")
    }
    if principals != {SIGNER_PRINCIPAL} or tag["signer_identity"] != SIGNER_PRINCIPAL:
        raise ContractError("tag signer differs from exact frozen principal")
    _git(root, ["-c", "gpg.ssh.allowedSignersFile=" + ALLOWED_SIGNERS_PATH,
                "verify-tag", "--raw", tag_oid], "immutable tag signature verification", runner)


def authorization_errors(manifest, manifest_path, commit, tag, ci, root=REPO, git_runner=None):
    errors = []
    root_digest = manifest.get("root_sha256") if isinstance(manifest, dict) else None
    if not isinstance(root_digest, str) or not HEX64.fullmatch(root_digest):
        return ["cannot authorize invalid freeze root"]
    try:
        manifest_digest = sha256_file(manifest_path)
        commit_keys = {"receipt_version", "kind", "root_sha256", "manifest_sha256", "commit_sha", "committed_at"}
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
        _receipt_common(commit, "commit", root_digest, manifest_digest)
        if set(commit) != commit_keys or not GIT_OID.fullmatch(commit.get("commit_sha", "")):
            raise ContractError("commit receipt is not closed and valid")
        committed_at = _iso_timestamp(commit["committed_at"], "commit.committed_at")
        _receipt_common(tag, "tag", root_digest, manifest_digest)
        if set(tag) != tag_keys or tag.get("commit_sha") != commit["commit_sha"]:
            raise ContractError("tag receipt is not closed or commit-bound")
        if (not GIT_OID.fullmatch(tag.get("tag_object_sha", ""))
                or not TAG.fullmatch(tag.get("tag_name", ""))
                or not tag["tag_name"].startswith("v4.2-freeze-")
                or tag.get("annotated") is not True or tag.get("signed") is not True
                or tag.get("signature_verified") is not True):
            raise ContractError("tag receipt is not an annotated signed v4.2 freeze tag")
        tagged_at = _iso_timestamp(tag["tagged_at"], "tag.tagged_at")
        if tagged_at < committed_at:
            raise ContractError("tag predates commit")
        _receipt_common(ci, "ci", root_digest, manifest_digest)
        if set(ci) != ci_keys or ci.get("commit_sha") != commit["commit_sha"] or ci.get("tag_name") != tag["tag_name"]:
            raise ContractError("CI receipt is not closed or commit/tag-bound")
        if (ci.get("provider") != "github-actions" or ci.get("github_owner") != GITHUB_OWNER
                or ci.get("github_repository") != GITHUB_REPOSITORY
                or ci.get("workflow_path") != WORKFLOW_PATH):
            raise ContractError("CI receipt does not bind exact GitHub repository/workflow")
        for key in ("workflow_id", "run_id", "run_attempt", "artifact_id"):
            if not isinstance(ci.get(key), int) or isinstance(ci[key], bool) or ci[key] <= 0:
                raise ContractError("CI %s must be a positive integer" % key)
        api = "https://api.github.com/repos/%s/%s" % (GITHUB_OWNER, GITHUB_REPOSITORY)
        run_api = "%s/actions/runs/%s" % (api, ci["run_id"])
        artifact_api = "%s/actions/artifacts/%s" % (api, ci["artifact_id"])
        exact = {
            "run_api_url": run_api,
            "run_html_url": "https://github.com/%s/%s/actions/runs/%s" %
                            (GITHUB_OWNER, GITHUB_REPOSITORY, ci["run_id"]),
            "artifacts_api_url": run_api + "/artifacts",
            "artifact_api_url": artifact_api,
            "artifact_archive_download_url": artifact_api + "/zip",
            "artifact_name": "v4.2-freeze-" + commit["commit_sha"],
        }
        if any(ci.get(key) != value for key, value in exact.items()):
            raise ContractError("CI receipt contains a noncanonical proof URL or artifact name")
        if (ci.get("event") != "push" or ci.get("conclusion") != "success"
                or not isinstance(ci.get("artifact_digest"), str)
                or not ci["artifact_digest"].startswith("sha256:")
                or not HEX64.fullmatch(ci["artifact_digest"][7:])):
            raise ContractError("CI receipt event/conclusion/artifact digest is invalid")
        started = _iso_timestamp(ci["run_started_at"], "ci.run_started_at")
        updated = _iso_timestamp(ci["run_updated_at"], "ci.run_updated_at")
        created = _iso_timestamp(ci["artifact_created_at"], "ci.artifact_created_at")
        artifact_updated = _iso_timestamp(ci["artifact_updated_at"], "ci.artifact_updated_at")
        issued = _iso_timestamp(ci["issued_at"], "ci.issued_at")
        if started < tagged_at or updated < started or created < started or artifact_updated < created or issued < max(updated, artifact_updated):
            raise ContractError("CI receipt timestamps are not causally ordered")
        _git_authorization(manifest, manifest_path, commit, tag, root, git_runner or _run_git)
    except (OSError, UnicodeError, ValueError, TypeError, KeyError, json.JSONDecodeError, ContractError) as exc:
        errors.append(str(exc))
    return errors


def validate(contract_path, manifest_path, commit_path, tag_path, ci_path, root=REPO,
             git_runner=None):
    try:
        contract = load_json(contract_path); manifest = load_json(manifest_path)
        commit = load_json(commit_path); tag = load_json(tag_path); ci = load_json(ci_path)
    except (OSError, ValueError, json.JSONDecodeError, ContractError) as exc:
        return ["freeze contract input failed: %s" % exc]
    errors = artifact_completeness_errors(contract, manifest, manifest_path, root)
    errors.extend(authorization_errors(
        manifest, manifest_path, commit, tag, ci, root=root, git_runner=git_runner,
    ))
    return errors


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--contract", default=CONTRACT_PATH)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--write-plan", action="store_true")
    mode.add_argument("--check-plan", action="store_true")
    parser.add_argument("--manifest"); parser.add_argument("--commit-receipt")
    parser.add_argument("--tag-receipt"); parser.add_argument("--ci-receipt")
    parser.add_argument("--repo-root", default=str(REPO))
    args = parser.parse_args(argv)
    if args.write_plan or args.check_plan:
        try:
            output = write_or_check_plan(
                args.contract, Path(args.repo_root), check=args.check_plan,
            )
            print("OK: %s canonical v4.2 freeze plan: %s" %
                  ("verified" if args.check_plan else "wrote", output))
            return 0
        except (OSError, ValueError, TypeError, json.JSONDecodeError, ContractError) as exc:
            print("V4.2 FREEZE PLAN FAILED: %s" % exc, file=sys.stderr); return 1
    required = (args.manifest, args.commit_receipt, args.tag_receipt, args.ci_receipt)
    if not all(required):
        parser.error("authorization validation requires manifest and all three receipts")
    errors = validate(
        args.contract, args.manifest, args.commit_receipt, args.tag_receipt,
        args.ci_receipt, Path(args.repo_root),
    )
    if errors:
        for error in errors:
            print("V4.2 FREEZE CONTRACT FAILED: %s" % error, file=sys.stderr)
        return 1
    print("OK: v4.2 §15 completeness and authorization verified")
    return 0


if __name__ == "__main__":
    sys.exit(main())
