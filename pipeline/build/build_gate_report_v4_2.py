#!/usr/bin/env python3
"""Build and validate the deterministic v4.2 five-record gate report."""

from datetime import datetime, timezone
import hashlib
import importlib.util
import json
import re
from pathlib import Path, PureWindowsPath
import subprocess
import sys


HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
REPORT_VERSION = "v4.2-gate-report-1"
SENTINEL_MODULES = (
    "pipeline.build.test_v4_2_scoring",
    "pipeline.build.test_v4_2_finalizer",
    "pipeline.build.test_v4_2_campaign",
    "pipeline.build.test_prompt_v4_2",
    "pipeline.build.test_runtime_methodology_v4_2",
    "pipeline.build.test_holdout_v4_2",
    "pipeline.build.test_normalize_datasets_v4_2",
)
EXPECTED_TESTS_RUN = {
    "pipeline.build.test_v4_2_scoring": 49,
    "pipeline.build.test_v4_2_finalizer": 24,
    "pipeline.build.test_v4_2_campaign": 15,
    "pipeline.build.test_prompt_v4_2": 19,
    "pipeline.build.test_runtime_methodology_v4_2": 10,
    "pipeline.build.test_holdout_v4_2": 8,
    "pipeline.build.test_normalize_datasets_v4_2": 8,
}
TOOLCHAIN_PATHS = tuple("pipeline/build/%s.py" % name.rsplit(".", 1)[-1]
                        for name in SENTINEL_MODULES) + (
    "pipeline/build/v4_2_scoring.py", "pipeline/build/build_gate_report_v4_2.py")


class GateReportError(ValueError):
    pass


def normalize_unittest_result(returncode, stdout, stderr):
    """Discard timing/path diagnostics and retain deterministic test assertions."""
    del stdout  # stdout is attacker-controlled test diagnostic output, never authority.
    text = (stderr or b"").decode("utf-8", errors="replace")
    ran_matches = re.findall(r"^Ran ([0-9]+) tests? in [^\n]+$", text, re.MULTILINE)
    status_matches = re.findall(r"^(OK|FAILED)(?: \(([^\n]*)\))?$", text, re.MULTILINE)
    if len(ran_matches) != 1 or len(status_matches) != 1:
        raise GateReportError("sentinel stderr lacks one unambiguous unittest summary")
    ran, status = ran_matches[0], status_matches[0]
    counts = {"failures": 0, "errors": 0, "skipped": 0}
    for key, value in re.findall(r"(failures|errors|skipped)=([0-9]+)", status[1] or ""):
        counts[key] = int(value)
    return {"normalization_version": "python-unittest-summary-1",
            "exit_code": returncode, "tests_run": int(ran),
            "status": status[0], **counts}


def canonical_bytes(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"),
                      ensure_ascii=False, allow_nan=False).encode("utf-8")


def sha256_bytes(value):
    return hashlib.sha256(value).hexdigest()


def _path(root, relative):
    if (not isinstance(relative, str) or not relative or "\\" in relative
            or Path(relative).is_absolute() or PureWindowsPath(relative).drive
            or any(part in ("", ".", "..") for part in relative.split("/"))):
        raise GateReportError("unsafe repository path: %r" % relative)
    root = Path(root).resolve()
    path = root.joinpath(*relative.split("/")).resolve()
    try:
        path.relative_to(root)
    except ValueError as exc:
        raise GateReportError("path escapes repository") from exc
    if not path.is_file():
        raise GateReportError("required file missing: %s" % relative)
    return path


def _load_scoring(root):
    path = _path(root, "pipeline/build/v4_2_scoring.py")
    spec = importlib.util.spec_from_file_location("gate_report_v4_2_scoring", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def critical_group(path):
    exact = {
        "recognized_revenue": "V", "employee_cash_cost": "V",
        "controllable_contractor_cash_cost": "V", "target_role_mix": "V",
        "R_cva": "V", "G": "I/H", "h": "I/H", "n_band": "B",
        "target_archetype_coverage": "B", "five_year_sale_availability": "B",
        "buyer_access_win_share": "B", "deal_execution_capacity_5y": "B",
        "integration_onboarding_capacity_5y": "B", "buy_mult": "P",
        "normalized_y5_operating_state": "P", "downside_exit_mult": "P",
        "operator_controlled_value_added_demand_share_y5": "SURVIVAL",
    }
    if path in exact:
        return exact[path]
    prefixes = (
        ("third_party_pass_through.", "V"), ("target_role_mix.", "V"),
        ("implementation_realization.", "I/H"),
        ("implementation_investment.", "I/H"),
        ("commercial_retention.", "C"),
    )
    for prefix, group in prefixes:
        if path.startswith(prefix) and len(path) > len(prefix):
            return group
    raise GateReportError("unknown missing-critical path: %s" % path)


def build_report(root, scope, record_paths, timestamp=None, runner=subprocess.run):
    root = Path(root).resolve()
    if scope not in ("regression", "holdout"):
        raise GateReportError("gate scope must be regression or holdout")
    if not isinstance(record_paths, list) or len(record_paths) != 5 or len(set(record_paths)) != 5:
        raise GateReportError("gate report requires exactly five distinct final records")
    scoring = _load_scoring(root)
    records = []
    for relative in sorted(record_paths):
        path = _path(root, relative)
        raw = path.read_bytes()
        try:
            record = json.loads(raw.decode("utf-8"))
        except (UnicodeError, json.JSONDecodeError) as exc:
            raise GateReportError("invalid final record: %s" % relative) from exc
        recalculated = scoring.calculate(record)
        expected = recalculated["decision"]["evidence_readiness"]
        stored = record.get("decision", {}).get("evidence_readiness")
        if stored != expected:
            raise GateReportError("stored missing-critical summary differs from scorer: %s" % relative)
        paths = sorted(expected.get("missing_critical_inputs", []))
        groups = sorted({critical_group(item) for item in paths})
        records.append({
            "path": relative, "sha256": sha256_bytes(raw), "byte_length": len(raw),
            "missing_critical_inputs": paths, "critical_groups": groups,
            "critical_unbounded": bool(paths),
        })
    toolchain = []
    for relative in TOOLCHAIN_PATHS:
        content = _path(root, relative).read_bytes()
        toolchain.append({"path": relative, "sha256": sha256_bytes(content),
                          "byte_length": len(content)})
    sentinels = []
    for module in SENTINEL_MODULES:
        command = [sys.executable, "-m", "unittest", module]
        result = runner(command, cwd=str(root), stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE, check=False)
        stdout = result.stdout.encode() if isinstance(result.stdout, str) else result.stdout
        stderr = result.stderr.encode() if isinstance(result.stderr, str) else result.stderr
        normalized = normalize_unittest_result(
            result.returncode, stdout or b"", stderr or b"")
        if normalized["tests_run"] != EXPECTED_TESTS_RUN[module]:
            raise GateReportError("sentinel test count differs for %s" % module)
        sentinels.append({"command": command, "cwd": ".", "result": normalized})
    timestamp = timestamp or datetime.now(timezone.utc).isoformat()
    try:
        parsed = datetime.fromisoformat(timestamp.replace("Z", "+00:00"))
    except (TypeError, ValueError) as exc:
        raise GateReportError("timestamp must be ISO-8601") from exc
    if parsed.tzinfo is None or parsed > datetime.now(timezone.utc).astimezone(parsed.tzinfo):
        raise GateReportError("timestamp must be timezone-aware and not future")
    count = sum(item["critical_unbounded"] for item in records)
    report = {
        "report_version": REPORT_VERSION, "scope": scope, "timestamp": timestamp,
        "records": records, "critical_unbounded_count": count,
        "critical_unbounded_rule": {"pass_maximum": 1, "reject_minimum": 2,
                                    "replacement_version_required_on_reject": True},
        "toolchain": toolchain, "sentinels": sentinels,
        "passed": count <= 1 and all(
            item["result"]["exit_code"] == 0 and item["result"]["status"] == "OK"
            and item["result"]["failures"] == item["result"]["errors"] ==
            item["result"]["skipped"] == 0
            for item in sentinels),
    }
    return report


def validate_report(root, report, runner=subprocess.run):
    if not isinstance(report, dict) or report.get("report_version") != REPORT_VERSION:
        raise GateReportError("gate report version is invalid")
    rebuilt = build_report(root, report.get("scope"),
                           [item.get("path") for item in report.get("records", [])],
                           timestamp=report.get("timestamp"), runner=runner)
    if report != rebuilt:
        raise GateReportError("gate report differs from deterministic reconstruction")
    if report["passed"] is not True:
        raise GateReportError("gate report rejects certificate issuance")
    return report
