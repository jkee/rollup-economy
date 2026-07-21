#!/usr/bin/env python3
"""Consume or deterministically recover one v4.2 guarded output reservation."""

import argparse
import hmac
import importlib.util
import json
import os
from pathlib import Path
import stat
import sys


HERE = Path(__file__).resolve().parent
_SPEC = importlib.util.spec_from_file_location(
    "guarded_writer_issue_campaign_v4_2", HERE / "issue_campaign_v4_2.py")
issuer = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(issuer)

ARTIFACT_KINDS = ("packet", "record", "memo", "review")


def _require_private_pipe_fd(descriptor):
    if not isinstance(descriptor, int) or descriptor < 3:
        raise issuer.IssueError("claim-token-fd must be a private descriptor >= 3")
    mode = os.fstat(descriptor).st_mode
    if not (stat.S_ISFIFO(mode) or stat.S_ISSOCK(mode)):
        raise issuer.IssueError(
            "claim-token-fd must be a FIFO or socket, never a regular file or directory")


def _entry(plan, entry_id):
    matches = [entry for entry in plan["entries"] if entry.get("entry_id") == entry_id]
    if len(matches) != 1:
        raise issuer.IssueError("entry_id must select exactly one issued entry")
    return matches[0]


def _validate_artifact(kind, content, entry):
    if not content:
        raise issuer.IssueError("artifact must not be empty")
    if kind == "memo":
        try:
            content.decode("utf-8")
        except UnicodeDecodeError as exc:
            raise issuer.IssueError("memo must be UTF-8") from exc
        return
    try:
        value = json.loads(
            content.decode("utf-8"), parse_constant=issuer._reject_constant,
            object_pairs_hook=issuer._closed_pairs)
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise issuer.IssueError("%s artifact must be strict JSON" % kind) from exc
    if not isinstance(value, dict):
        raise issuer.IssueError("%s artifact must be a JSON object" % kind)
    if kind == "packet":
        valid = value.get("naics") == entry["naics"] and value.get("title") == entry["title"]
    elif kind == "record":
        meta = value.get("run_meta")
        valid = (value.get("naics") == entry["naics"]
                 and value.get("title") == entry["title"]
                 and isinstance(meta, dict) and meta.get("run_id") == entry["run_id"])
    else:
        valid = value.get("entry_id") == entry["entry_id"]
    if not valid:
        raise issuer.IssueError("%s artifact identity does not match the issued entry" % kind)


def guarded_write(root, plan_path, entry_id, artifact_kind, authorized_task_path,
                  claim_token, source_path, *, after_claim=None):
    """Create one authorized artifact and an immutable plan/hash-bound receipt."""
    root = Path(root).resolve()
    if artifact_kind not in ARTIFACT_KINDS:
        raise issuer.IssueError("unsupported output artifact kind: %s" % artifact_kind)
    plan, errors = issuer.validate_issued_plan(root, plan_path)
    if errors:
        raise issuer.IssueError("issued plan is not valid: %s" % "; ".join(errors))
    entry = _entry(plan, entry_id)
    execution = issuer._claim_execution(entry, artifact_kind)
    if authorized_task_path != execution["codex_task_path"]:
        raise issuer.IssueError("task path is not authorized for this entry and artifact kind")
    if not isinstance(claim_token, str) or not claim_token:
        raise issuer.IssueError("claim token is required")
    supplied_commitment = issuer.sha256_bytes(claim_token.encode("utf-8"))
    expected_commitment = entry["output_reservations"][artifact_kind]["claim_token_sha256"]
    if not hmac.compare_digest(supplied_commitment, expected_commitment):
        raise issuer.IssueError("claim token does not match the issued capability")

    source = issuer._repository_path(root, source_path, must_exist=True)
    content = source.read_bytes()
    _validate_artifact(artifact_kind, content, entry)
    ref = entry["output_reservations"][artifact_kind]
    output_relative = entry["planned_outputs"][artifact_kind]
    forbidden = {output_relative, ref["path"], ref["lock_path"], ref["claim_receipt_path"], plan_path}
    if source_path in forbidden:
        raise issuer.IssueError("source path overlaps guarded protocol state")

    plan_bytes = issuer._repository_path(root, plan_path, must_exist=True).read_bytes()
    expected_reservation = issuer._reservation_bytes(
        plan["campaign_id"], entry["entry_id"], entry["run_id"], artifact_kind,
        output_relative, authorized_task_path, plan["freeze"]["root_sha256"],
        plan["authorization"]["commit_sha"], expected_commitment)
    reservation = issuer._repository_path(root, ref["path"])
    lock = issuer._repository_path(root, ref["lock_path"])
    output = issuer._repository_path(root, output_relative)
    receipt = issuer._repository_path(root, ref["claim_receipt_path"])
    if output.exists() or receipt.exists() or lock.exists():
        raise issuer.IssueError("artifact reservation is already consumed or in progress")
    try:
        if reservation.read_bytes() != expected_reservation:
            raise issuer.IssueError("reservation does not match the issued owner/kind/path")
    except FileNotFoundError as exc:
        raise issuer.IssueError("artifact reservation is absent or already consumed") from exc

    claimed = artifact_created = receipt_created = False
    try:
        lock.parent.mkdir(parents=True, exist_ok=True)
        try:
            os.link(reservation, lock)
        except FileExistsError as exc:
            raise issuer.IssueError("artifact reservation is being consumed") from exc
        except FileNotFoundError as exc:
            raise issuer.IssueError("artifact reservation lost the claim race") from exc
        claimed = True
        if lock.read_bytes() != expected_reservation:
            raise issuer.IssueError("claimed reservation bytes are stale")
        reservation.unlink()
        if after_claim is not None:
            after_claim()
        if issuer._repository_path(root, plan_path, must_exist=True).read_bytes() != plan_bytes:
            raise issuer.IssueError("issued plan changed during claim consumption")
        issuer._atomic_create(root, output_relative, content)
        artifact_created = True
        if output.read_bytes() != content:
            raise issuer.IssueError("written artifact failed byte verification")
        receipt_bytes = issuer.claim_receipt_bytes(plan, plan_path, entry, artifact_kind, content)
        issuer._atomic_create(root, ref["claim_receipt_path"], receipt_bytes)
        receipt_created = True
        if receipt.read_bytes() != receipt_bytes:
            raise issuer.IssueError("written claim receipt failed byte verification")
        lock.unlink()
        return json.loads(receipt_bytes.decode("utf-8"))
    except Exception:
        if claimed and not receipt_created:
            if artifact_created:
                try:
                    output.unlink()
                except FileNotFoundError:
                    pass
            restored = reservation.exists()
            if not restored and lock.exists():
                try:
                    os.link(lock, reservation)
                    restored = True
                except FileExistsError:
                    restored = True
            if restored:
                try:
                    lock.unlink()
                except FileNotFoundError:
                    pass
        raise


def recover_claim(root, plan_path, entry_id, artifact_kind, authorized_task_path,
                  claim_token):
    """Recover an interrupted guarded write without mutating conflicting state."""
    root = Path(root).resolve()
    plan_file = issuer._repository_path(root, plan_path, must_exist=True)
    plan_bytes = plan_file.read_bytes()
    plan = issuer.load_json(plan_file)
    if (not isinstance(plan, dict) or plan_bytes != issuer.canonical_bytes(plan)
            or plan.get("plan_sha256") != issuer._plan_digest(plan)):
        raise issuer.IssueError("recovery requires the exact canonical issued plan")
    entry = _entry(plan, entry_id)
    execution = issuer._claim_execution(entry, artifact_kind)
    if authorized_task_path != execution.get("codex_task_path"):
        raise issuer.IssueError("task path is not authorized for recovery")
    if not isinstance(claim_token, str) or not claim_token:
        raise issuer.IssueError("claim token is required for recovery")
    commitment = issuer.sha256_bytes(claim_token.encode("utf-8"))
    ref = entry["output_reservations"][artifact_kind]
    if not hmac.compare_digest(commitment, ref["claim_token_sha256"]):
        raise issuer.IssueError("claim token does not match the recovery capability")
    output_relative = entry["planned_outputs"][artifact_kind]
    expected = issuer._reservation_bytes(
        plan["campaign_id"], entry["entry_id"], entry["run_id"], artifact_kind,
        output_relative, authorized_task_path, plan["freeze"]["root_sha256"],
        plan["authorization"]["commit_sha"], commitment)
    reservation = issuer._repository_path(root, ref["path"])
    lock = issuer._repository_path(root, ref["lock_path"])
    output = issuer._repository_path(root, output_relative)
    receipt = issuer._repository_path(root, ref["claim_receipt_path"])
    state = (reservation.exists(), lock.exists(), output.exists(), receipt.exists())
    if state[3] or not state[1] or state[0]:
        raise issuer.IssueError("claim state is not an interrupted recoverable state: %s" %
                                (state,))
    if lock.read_bytes() != expected:
        raise issuer.IssueError("recovery lock bytes differ from the exact reservation")
    if not state[2]:
        # Crash after lock acquisition/reservation removal but before output.
        try:
            os.link(lock, reservation)
        except FileExistsError as exc:
            raise issuer.IssueError("recovery reservation appeared concurrently") from exc
        if reservation.read_bytes() != expected:
            reservation.unlink()
            raise issuer.IssueError("recovered reservation byte verification failed")
        lock.unlink()
        return {"recovery": "reservation_restored", "entry_id": entry_id,
                "artifact_kind": artifact_kind}
    # Crash after the exact output create but before receipt commit.
    content = output.read_bytes()
    _validate_artifact(artifact_kind, content, entry)
    receipt_bytes = issuer.claim_receipt_bytes(plan, plan_path, entry, artifact_kind, content)
    issuer._atomic_create(root, ref["claim_receipt_path"], receipt_bytes)
    if receipt.read_bytes() != receipt_bytes:
        issuer._unlink_if_exact(root, ref["claim_receipt_path"], receipt_bytes)
        raise issuer.IssueError("recovered receipt byte verification failed")
    lock.unlink()
    return json.loads(receipt_bytes.decode("utf-8"))


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=str(issuer.REPO))
    parser.add_argument("--plan", required=True)
    parser.add_argument("--entry-id", required=True)
    parser.add_argument("--artifact-kind", required=True, choices=ARTIFACT_KINDS)
    parser.add_argument("--authorized-task-path", required=True)
    parser.add_argument("--claim-token-fd", type=int, required=True,
                        help="private pipe FD >=3 containing only the exact claim token")
    parser.add_argument("--source", help="private staged source (required unless --recover)")
    parser.add_argument("--recover", action="store_true",
                        help="recover a lock-only or exact output-plus-lock crash state")
    args = parser.parse_args(argv)
    try:
        _require_private_pipe_fd(args.claim_token_fd)
        chunks, total = [], 0
        while True:
            chunk = os.read(args.claim_token_fd, 4096)
            if not chunk:
                break
            total += len(chunk)
            if total > 4096:
                raise issuer.IssueError("claim token input is too large")
            chunks.append(chunk)
        claim_token = b"".join(chunks).decode("utf-8")
        if args.recover:
            receipt = recover_claim(
                args.repo_root, args.plan, args.entry_id, args.artifact_kind,
                args.authorized_task_path, claim_token)
        else:
            if not args.source:
                raise issuer.IssueError("--source is required for a new guarded write")
            receipt = guarded_write(
                args.repo_root, args.plan, args.entry_id, args.artifact_kind,
                args.authorized_task_path, claim_token, args.source)
    except (issuer.IssueError, OSError, UnicodeError, TypeError, ValueError) as exc:
        print("GUARDED WRITE FAILED: %s" % exc, file=sys.stderr)
        return 1
    if args.recover and receipt.get("recovery") == "reservation_restored":
        print("OK: restored %s reservation" % args.artifact_kind)
    else:
        print("OK: consumed %s reservation; artifact_sha256=%s" % (
            args.artifact_kind, receipt["artifact"]["sha256"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
