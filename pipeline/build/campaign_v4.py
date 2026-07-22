#!/usr/bin/env python3
"""Generate and validate exact-artifact v4 canary/full campaign manifests."""

import argparse
import hashlib
import importlib.util
import json
import os
import sys


HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
V4 = os.path.join(REPO, "pipeline", "v4")
SCHEMAS = os.path.join(HERE, "schemas")
CANARY_CODES = ("541512", "541511", "541214", "238220", "541930")


def load_module(name, filename):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, filename))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


finalizer = load_module("v4_campaign_finalizer", "finalize_run_v4.py")
legacy_build = finalizer.legacy_build


def load_json(path):
    with open(path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def write_json(path, value):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        json.dump(value, handle, indent=2, ensure_ascii=False)
        handle.write("\n")


def sha256(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def expected_codes(scope):
    if scope == "canary":
        return set(CANARY_CODES), set()
    fleet = {item["naics"] for item in load_json(os.path.join(REPO, "pipeline", "blocks", "targets_phase3.json"))["codes"]}
    golden = {item["naics"] for item in load_json(os.path.join(REPO, "pipeline", "golden", "golden_set.json"))["codes"]}
    return fleet, golden


def _artifact_paths(kind, code, run_id):
    record_root = "runs" if kind == "fleet" else "golden"
    return {
        "packet_path": os.path.join("pipeline", "v4", "packets", code, run_id + ".json"),
        "record_path": os.path.join("pipeline", "v4", record_root, code, run_id + ".json"),
        "memo_path": os.path.join("pipeline", "v4", "memos", code, run_id + ".md"),
        "review_path": os.path.join("pipeline", "v4", "reviews", code, run_id + ".json"),
        "dataset_path": os.path.join("pipeline", "datasets", "derived", code + ".json"),
    }


def discover(scope, allow_missing=False):
    fleet_codes, golden_codes = expected_codes(scope)
    entries = []
    for kind, codes, record_root in (("fleet", fleet_codes, "runs"), ("golden", golden_codes, "golden")):
        for code in sorted(codes):
            code_dir = os.path.join(V4, record_root, code)
            files = sorted(name for name in os.listdir(code_dir) if name.endswith(".json")) if os.path.isdir(code_dir) else []
            if not files:
                if allow_missing:
                    continue
                raise ValueError("missing v4 %s record for %s" % (kind, code))
            for filename in files:
                path = os.path.join(code_dir, filename)
                record = load_json(path)
                if record.get("run_meta", {}).get("template_version") != "4.0":
                    continue
                run_id = record["run_meta"]["run_id"]
                paths = _artifact_paths(kind, code, run_id)
                absolute = {key: os.path.join(REPO, value) for key, value in paths.items()}
                for key in ("packet_path", "record_path", "memo_path", "dataset_path"):
                    if not os.path.isfile(absolute[key]):
                        raise ValueError("%s missing for %s/%s" % (key, code, run_id))
                packet = load_json(absolute["packet_path"])
                entries.append({
                    "kind": kind,
                    "naics": code,
                    "run_id": run_id,
                    "attempt": record["run_meta"]["attempt"],
                    "required_research_model_id": "gpt-5.6-terra" if kind == "fleet" else "gpt-5.6-sol",
                    "required_validator_model_id": "gpt-5.6-sol",
                    "required_validator_prompt_version": "validator-4.0",
                    **paths,
                    "source_registry": [
                        {"source_id": source["id"], "url": source["url"], "score_driving": any(
                            source["id"] in selection.get("source_ids", [])
                            for _path, selection in finalizer._iter_selections(packet)
                        )}
                        for source in packet["sources"]
                    ],
                    "artifact_digests": {
                        "packet_sha256": sha256(absolute["packet_path"]),
                        "run_sha256": sha256(absolute["record_path"]),
                        "memo_sha256": sha256(absolute["memo_path"]),
                    },
                })
    entries.sort(key=lambda item: (item["kind"], item["naics"], item["attempt"], item["run_id"]))
    return entries


def generate(scope, path, allow_missing=False):
    entries = discover(scope, allow_missing=allow_missing)
    manifest = {
        "manifest_version": "review-campaign-4.0",
        "scope": scope,
        "canary_codes": list(CANARY_CODES),
        "entries": entries,
    }
    write_json(path, manifest)
    return manifest


def validate_entry(entry, require_review=True):
    errors = []
    absolute = {key: os.path.join(REPO, entry[key]) for key in (
        "packet_path", "record_path", "memo_path", "review_path", "dataset_path")}
    packet, record, dataset = (load_json(absolute[key]) for key in ("packet_path", "record_path", "dataset_path"))
    packet_schema = load_json(os.path.join(SCHEMAS, "research_packet_v4.schema.json"))
    record_schema = load_json(os.path.join(SCHEMAS, "run_record_v4.schema.json"))
    errors.extend("packet: " + item for item in legacy_build.schema_errors(packet, packet_schema, packet_schema))
    errors.extend("record: " + item for item in legacy_build.schema_errors(record, record_schema, record_schema))
    if packet.get("naics") != entry["naics"] or record.get("naics") != entry["naics"]:
        errors.append("NAICS identity mismatch")
    if packet.get("run_meta", {}).get("run_id") != entry["run_id"] or record.get("run_meta", {}).get("run_id") != entry["run_id"]:
        errors.append("run identity mismatch")
    if packet.get("run_meta", {}).get("model_id") != entry["required_research_model_id"]:
        errors.append("research model route mismatch")
    fresh, final_errors = finalizer.finalize(packet, dataset, entry["kind"])
    errors.extend("finalizer: " + item for item in final_errors)
    if fresh is not None:
        with open(absolute["record_path"], "rb") as handle:
            if handle.read() != finalizer.serialize_record(fresh):
                errors.append("fresh finalized record differs")
        with open(absolute["memo_path"], "r", encoding="utf-8") as handle:
            if handle.read() != finalizer.render_memo(fresh):
                errors.append("fresh memo differs")
    actual_digests = {
        "packet_sha256": sha256(absolute["packet_path"]),
        "run_sha256": sha256(absolute["record_path"]),
        "memo_sha256": sha256(absolute["memo_path"]),
    }
    if actual_digests != entry["artifact_digests"]:
        errors.append("manifest artifact digests are stale")

    if not os.path.isfile(absolute["review_path"]):
        if require_review:
            errors.append("review missing")
        return errors
    review = load_json(absolute["review_path"])
    review_schema = load_json(os.path.join(SCHEMAS, "review_record_v4.schema.json"))
    errors.extend("review: " + item for item in legacy_build.schema_errors(review, review_schema, review_schema))
    if review.get("naics") != entry["naics"] or review.get("run_id") != entry["run_id"]:
        errors.append("review identity mismatch")
    if review.get("artifact_digests") != entry["artifact_digests"]:
        errors.append("review digests do not bind manifest artifacts")
    meta = review.get("review_meta", {})
    if meta.get("model_id") != entry["required_validator_model_id"] or meta.get("prompt_version") != entry["required_validator_prompt_version"]:
        errors.append("review model/prompt route mismatch")
    expected_sources = {(item["source_id"], item["url"], item["score_driving"]) for item in entry["source_registry"]}
    actual_sources = {(item["source_id"], item["url"], item["score_driving"]) for item in review.get("source_reviews", [])}
    if expected_sources != actual_sources:
        errors.append("review source registry coverage mismatch")
    outcome = review.get("outcome")
    material = [item for item in review.get("findings", []) if item.get("severity") == "material"]
    fatal = [item for item in review.get("findings", []) if item.get("severity") == "fatal_mechanics"]
    mechanics_ok = all(review.get("mechanics", {}).values()) if review.get("mechanics") else False
    if outcome == "invalid" and not (fatal or not mechanics_ok):
        errors.append("invalid requires failed mechanics/fatal finding")
    if outcome == "reject" and not material:
        errors.append("reject requires material finding")
    if outcome in ("publishable", "publishable_with_caveats") and (material or fatal or not mechanics_ok):
        errors.append("publishable tier cannot contain material/fatal/failed mechanics")
    if outcome == "publishable" and (review.get("findings") or review.get("publication_caveats")):
        errors.append("publishable must have no findings/caveats")
    return errors


def validate(path, require_review=True):
    manifest = load_json(path)
    fresh = {
        "manifest_version": "review-campaign-4.0",
        "scope": manifest["scope"],
        "canary_codes": list(CANARY_CODES),
        "entries": discover(manifest["scope"], allow_missing=False),
    }
    errors = []
    if fresh != manifest:
        errors.append("manifest is stale; regenerate before validating")
    for entry in manifest["entries"]:
        label = "%s/%s" % (entry["naics"], entry["run_id"])
        errors.extend("%s: %s" % (label, item) for item in validate_entry(entry, require_review=require_review))
    return errors


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    generate_parser = sub.add_parser("generate")
    generate_parser.add_argument("--scope", choices=("canary", "full"), required=True)
    generate_parser.add_argument("--manifest", required=True)
    generate_parser.add_argument("--allow-missing", action="store_true")
    validate_parser = sub.add_parser("validate")
    validate_parser.add_argument("--manifest", required=True)
    validate_parser.add_argument("--allow-missing-reviews", action="store_true")
    args = parser.parse_args(argv)
    try:
        if args.command == "generate":
            manifest = generate(args.scope, args.manifest, allow_missing=args.allow_missing)
            print("generated v4 %s manifest with %d entries" % (args.scope, len(manifest["entries"])))
        else:
            errors = validate(args.manifest, require_review=not args.allow_missing_reviews)
            if errors:
                for item in errors:
                    print(item, file=sys.stderr)
                return 1
            print("validated v4 manifest: %s" % args.manifest)
    except (OSError, ValueError, KeyError) as exc:
        print("v4 campaign error: %s" % exc, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
