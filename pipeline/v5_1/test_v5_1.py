#!/usr/bin/env python3
"""v5.1 sentinels: scoring boundaries, evidence handling, packet/review
contracts, code-owned sampling, and the deterministic ledger publication gate."""

import copy
import json
import sys
import tempfile
import unittest
from decimal import Decimal
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from score import (
    aggregate, c_score, d_score, f_score, h_score, readiness_and_action,
    scenario_envelope, tier_for,
)
from build import (
    MANDATORY_TIERS, build_site, check, compute_sample, contract_sha256_current,
    dump_json, finalize, finalize_path, render_memo, sampled_codes,
    validate_packet, validate_review,
)

DATASET = {
    "labor_share": {"value": 0.50, "method": "synthetic", "quality": "HIGH"},
    "n_band": {"value": 2000, "derivation": "synthetic", "quality": "HIGH"},
}
DATASET_EST = {
    "labor_share": {"value": 0.50, "method": "synthetic", "quality": "MED"},
    "n_band": {"value": 2000, "derivation": "margin-bridged", "quality": "ESTIMATE"},
}
GAP_DATASET = {
    "labor_share": {"value": 0.50, "method": "synthetic"},
    "n_band": {"value": 0, "derivation": "no direct series for this code", "quality": "NONE"},
}


def primitive(state="ESTIMATE", low=0.1, base=0.2, high=0.3, **extra):
    sel = {"evidence_state": state, "low": low, "base": base, "high": high,
           "rationale": "synthetic", "change_evidence": "synthetic", "source_ids": [],
           "caveats": [], **extra}
    return sel


def packet(**overrides):
    base = {
        "identity": {"naics": "541512", "title": "Synthetic", "run_id": "t1",
                     "model_id": "test", "run_date": "2026-07-22",
                     "methodology_version": "5.1", "attempt": 1},
        "lens": {"included_activities": "x", "excluded_activities": "y",
                 "customer_and_revenue_model": "z", "deviation_from_default": "none",
                 "heterogeneous": False},
        "primitives": {
            "a": primitive(state="PROXY", source_ids=["S1"], bridge="synthetic bridge"),
            "rho": primitive(low=0.3, base=0.5, high=0.7),
            "e": primitive(low=0.5, base=0.7, high=0.9),
            "s5": primitive(low=0.1, base=0.2, high=0.3),
            "q": primitive(low=0.2, base=0.3, high=0.5),
            "d5": primitive(low=0.9, base=1.0, high=1.2),
            "o": primitive(low=0.7, base=0.9, high=1.0),
        },
        "narrative": {k: "synthetic" for k in (
            "executive_view", "ai_impact", "value_capture", "firm_availability",
            "demand_durability", "risks_and_uncertainty", "principal_driver",
            "principal_weakness")},
        "sources": [{"id": "S1", "url": "https://example.com", "title": "t",
                     "access_date": "2026-07-22", "supports": "synthetic"}],
    }
    for path, value in overrides.items():
        node = base
        keys = path.split(".")
        for key in keys[:-1]:
            node = node[key]
        node[keys[-1]] = value
    return copy.deepcopy(base)


def observed_packet():
    p = packet()
    for name, sel in p["primitives"].items():
        sel["evidence_state"] = "OBSERVED"
        sel["source_ids"] = ["S1"]
        sel.pop("bridge", None)
    return p


def review_for(p, mechanics, **overrides):
    r = {"run_id": p["identity"]["run_id"], "naics": p["identity"]["naics"],
         "reviewer_model_id": "test-validator", "review_date": "2026-07-22",
         "methodology_version": "5.1", "outcome": "publishable_with_caveats",
         "mechanics": {k: mechanics[k] for k in ("identity_ok", "score_reproduces",
                                                 "memo_reproduces", "artifacts_sha256")},
         "sources_audited": [{"source_id": "S1", "reachable": True,
                              "support": "partially_supported"}],
         "material_findings": [], "caveats": ["synthetic"], "summary": "synthetic"}
    r.update(overrides)
    return r


class ScoringSentinels(unittest.TestCase):
    def test_factor_anchors(self):
        self.assertEqual(h_score(1, 1, 0.25), Decimal(10))
        self.assertEqual(h_score(0.5, 0.5, 0.5), Decimal(5))
        self.assertEqual(h_score(0, 1, 1), Decimal(0))
        self.assertEqual(f_score(0, 1, 1), Decimal(0))
        self.assertEqual(f_score(500, 1, 1), Decimal(10))
        self.assertEqual(f_score(5000, 1, 1), Decimal(10))
        self.assertEqual(c_score(0), Decimal(0))
        self.assertEqual(c_score("0.25"), Decimal(5))
        self.assertEqual(c_score("0.50"), Decimal(10))
        self.assertEqual(c_score("0.80"), Decimal(10))
        self.assertEqual(d_score("1.2", 1), Decimal(10))
        self.assertEqual(d_score("0.5", "0.5"), Decimal("2.5"))

    def test_tier_cut_boundaries(self):
        for A, L, tier in [("7.5", "6", "HIGHEST_PRIORITY"),
                           ("7.499999999999", "6", "PRIORITY"),
                           ("7.5", "5.999999999999", "PRIORITY"),
                           ("6.0", "4", "PRIORITY"),
                           ("4.5", "2", "CONDITIONAL"),
                           ("3.0", "1", "LOW_PRIORITY"),
                           ("2.999999999999", "1", "STRUCTURAL_OUT"),
                           ("9", "0.5", "STRUCTURAL_OUT")]:
            self.assertEqual(tier_for(Decimal(A), Decimal(L)), tier, (A, L))

    def test_weak_link_gates(self):
        result = aggregate({"H": Decimal("1.69"), "F": Decimal("7.75"),
                            "C": Decimal("7.19"), "D": Decimal(9)})
        self.assertGreater(result["A"], Decimal("6"))
        self.assertEqual(result["tier"], "LOW_PRIORITY")

    def test_all_tiers_reachable(self):
        tiers = set()
        for value in ("9", "6.5", "5", "3.5", "0.5"):
            factors = {name: Decimal(value) for name in "HFCD"}
            tiers.add(aggregate(factors)["tier"])
        self.assertEqual(len(tiers), 5)

    def test_envelope_and_missing(self):
        ranges = {name: {"low": Decimal(4), "base": Decimal(5), "high": Decimal(6)}
                  for name in "HFCD"}
        env = scenario_envelope(ranges)
        self.assertEqual(env["state_count"], 81)
        self.assertIsNotNone(env["base"])
        missing = dict(ranges, H={"low": None, "base": None, "high": None})
        env2 = scenario_envelope(missing)
        self.assertIsNone(env2["base"])
        self.assertEqual(env2["missing_factors"], ["H"])
        self.assertEqual(readiness_and_action(["OBSERVED", "MISSING"], env2),
                         ("STRESS_TEST_ONLY", "EVIDENCE_FIRST"))

    def test_readiness_action_mapping(self):
        env = scenario_envelope({name: {"low": Decimal(8), "base": Decimal(9), "high": Decimal(10)}
                                 for name in "HFCD"})
        self.assertEqual(readiness_and_action(["ESTIMATE", "OBSERVED"], env),
                         ("MODEL_CONDITIONED", "VALIDATE_ASSUMPTIONS"))
        self.assertEqual(readiness_and_action(["PROXY", "OBSERVED"], env),
                         ("PROVISIONAL", "ADVANCE_TO_STAGE2"))
        self.assertEqual(readiness_and_action(["OBSERVED"], env),
                         ("SUBSTANTIATED", "ADVANCE_TO_STAGE2"))
        low = scenario_envelope({name: {"low": Decimal("0.2"), "base": Decimal("0.5"), "high": Decimal("0.8")}
                                 for name in "HFCD"})
        self.assertEqual(readiness_and_action(["OBSERVED"], low),
                         ("SUBSTANTIATED", "DEPRIORITIZE"))
        with self.assertRaises(ValueError):
            readiness_and_action(["ELICITED_ASSUMPTION"], env)


class ContractSentinels(unittest.TestCase):
    def test_valid_packet_passes(self):
        self.assertEqual(validate_packet(packet()), [])

    def test_prose_range_rejected(self):
        errors = validate_packet(packet(**{"primitives.q": primitive(low="10%-20%", base=0.15, high=0.2)}))
        self.assertTrue(any("never prose" in e for e in errors))

    def test_disordered_range_rejected(self):
        errors = validate_packet(packet(**{"primitives.q": primitive(low=0.5, base=0.3, high=0.6)}))
        self.assertTrue(any("low <= base <= high" in e for e in errors))

    def test_missing_must_be_null(self):
        errors = validate_packet(packet(**{"primitives.q": primitive(state="MISSING")}))
        self.assertTrue(any("must be null for MISSING" in e for e in errors))

    def test_observed_requires_source_and_proxy_requires_bridge(self):
        errors = validate_packet(packet(**{"primitives.q": primitive(state="OBSERVED")}))
        self.assertTrue(any("requires at least one source" in e for e in errors))
        errors = validate_packet(packet(**{"primitives.q": primitive(state="PROXY", source_ids=["S1"])}))
        self.assertTrue(any("bridge" in e for e in errors))

    def test_unknown_source_id_rejected(self):
        errors = validate_packet(packet(**{"primitives.q": primitive(source_ids=["S99"])}))
        self.assertTrue(any("unknown source" in e for e in errors))

    def test_domain_enforced(self):
        errors = validate_packet(packet(**{"primitives.o": primitive(low=0.5, base=0.9, high=1.5)}))
        self.assertTrue(any("outside domain" in e for e in errors))

    def test_format_patterns_enforced(self):
        errors = validate_packet(packet(**{"identity.naics": "5415"}))
        self.assertTrue(any("six digits" in e for e in errors))
        errors = validate_packet(packet(**{"identity.run_date": "22/07/2026"}))
        self.assertTrue(any("YYYY-MM-DD" in e for e in errors))
        p = packet()
        p["sources"][0]["id"] = "src-1"
        self.assertTrue(any("S<number>" in e for e in validate_packet(p)))
        p = packet()
        p["sources"][0]["access_date"] = "July 2026"
        self.assertTrue(any("access_date" in e for e in validate_packet(p)))

    def test_empty_bridge_and_missing_sources_rejected(self):
        errors = validate_packet(packet(**{"primitives.a": primitive(state="PROXY", source_ids=["S1"], bridge="  ")}))
        self.assertTrue(any("bridge" in e for e in errors))
        errors = validate_packet(packet(**{"primitives.q": primitive(
            state="MISSING", low=None, base=None, high=None, source_ids=["S1"])}))
        self.assertTrue(any("must be empty for MISSING" in e for e in errors))

    def test_unknown_keys_rejected_everywhere(self):
        p = packet()
        p["tier_hint"] = "HIGHEST_PRIORITY"
        self.assertTrue(any("unknown keys" in e for e in validate_packet(p)))
        p = packet()
        p["primitives"]["q"]["desired_score"] = 10
        self.assertTrue(any("unknown keys" in e for e in validate_packet(p)))
        p = packet()
        p["primitives"]["l"] = primitive()
        self.assertTrue(any("dataset-injected" in e for e in validate_packet(p)))


class FinalizeSentinels(unittest.TestCase):
    def test_end_to_end_and_determinism(self):
        p = packet()
        score1 = finalize(p, DATASET)
        score2 = finalize(copy.deepcopy(p), copy.deepcopy(DATASET))
        self.assertEqual(json.dumps(score1, sort_keys=True), json.dumps(score2, sort_keys=True))
        self.assertEqual(render_memo(p, score1), render_memo(p, score1))
        self.assertIn(score1["tier"], ("STRUCTURAL_OUT", "LOW_PRIORITY", "CONDITIONAL",
                                       "PRIORITY", "HIGHEST_PRIORITY"))
        self.assertEqual(score1["readiness"], "MODEL_CONDITIONED")
        self.assertEqual(score1["action"], "VALIDATE_ASSUMPTIONS")
        # Factor state is the weakest of its primitives: a=PROXY, rho=ESTIMATE -> ESTIMATE.
        self.assertEqual(score1["factors"]["H"]["evidence_state"], "ESTIMATE")
        all_proxy = packet(**{"primitives.rho": primitive(state="PROXY", low=0.3, base=0.5,
                                                          high=0.7, source_ids=["S1"],
                                                          bridge="synthetic bridge")})
        self.assertEqual(finalize(all_proxy, DATASET)["factors"]["H"]["evidence_state"], "PROXY")
        for name in "HFCD":
            f = score1["factors"][name]
            self.assertLessEqual(f["low"], f["base"])
            self.assertLessEqual(f["base"], f["high"])

    def test_dataset_gap_is_missing_not_zero(self):
        score = finalize(packet(), GAP_DATASET)
        self.assertIsNone(score["factors"]["F"]["base"])
        self.assertIsNone(score["tier"])
        self.assertEqual(score["readiness"], "STRESS_TEST_ONLY")
        self.assertEqual(score["action"], "EVIDENCE_FIRST")
        self.assertEqual(score["envelope"]["missing_factors"], ["F"])

    def test_dataset_provenance_honored(self):
        # An all-OBSERVED research packet is SUBSTANTIATED only when the
        # dataset inputs are themselves observed-quality; a margin-bridged
        # ESTIMATE firm count must drag readiness down (Sol finding #2).
        good = finalize(observed_packet(), DATASET)
        self.assertEqual(good["readiness"], "SUBSTANTIATED")
        est = finalize(observed_packet(), DATASET_EST)
        self.assertEqual(est["primitives"]["n"]["evidence_state"], "ESTIMATE")
        self.assertEqual(est["factors"]["F"]["evidence_state"], "ESTIMATE")
        self.assertEqual(est["readiness"], "MODEL_CONDITIONED")
        self.assertEqual(est["action"], "VALIDATE_ASSUMPTIONS")

    def test_score_invariant_under_evidence_state(self):
        # v4.0 lesson: evidence state changes readiness/action, never economics.
        est, obs = finalize(packet(), DATASET), None
        p = packet()
        for sel in p["primitives"].values():
            sel["evidence_state"] = "OBSERVED"
            sel["source_ids"] = ["S1"]
            sel.pop("bridge", None)
        obs = finalize(p, DATASET)
        for name in "HFCD":
            self.assertEqual(est["factors"][name]["base"], obs["factors"][name]["base"], name)
        self.assertEqual((est["A"], est["L"], est["tier"]), (obs["A"], obs["L"], obs["tier"]))
        self.assertNotEqual(est["readiness"], obs["readiness"])

    def test_invalid_packet_fails_closed(self):
        bad = packet(**{"primitives.q": primitive(low=0.5, base=0.3, high=0.6)})
        with self.assertRaises(ValueError):
            finalize(bad, DATASET)


class ReviewContractSentinels(unittest.TestCase):
    MECH = {"identity_ok": True, "score_reproduces": True, "memo_reproduces": True,
            "artifacts_sha256": "a" * 64}

    def test_valid_review_passes(self):
        self.assertEqual(validate_review(review_for(packet(), self.MECH), packet(), self.MECH), [])

    def test_publishable_with_material_findings_rejected(self):
        r = review_for(packet(), self.MECH, material_findings=[
            {"category": "unsupported_claim", "finding": "x", "materiality": "y"}])
        errors = validate_review(r, packet(), self.MECH)
        self.assertTrue(any("cannot carry material findings" in e for e in errors))

    def test_reject_requires_findings(self):
        r = review_for(packet(), self.MECH, outcome="reject")
        errors = validate_review(r, packet(), self.MECH)
        self.assertTrue(any("requires at least one material finding" in e for e in errors))

    def test_identity_mismatch_rejected(self):
        r = review_for(packet(), self.MECH, naics="999999")
        errors = validate_review(r, packet(), self.MECH)
        self.assertTrue(any("does not match packet identity" in e for e in errors))

    def test_stale_digest_rejected(self):
        r = review_for(packet(), self.MECH)
        current = dict(self.MECH, artifacts_sha256="b" * 64)
        errors = validate_review(r, packet(), current)
        self.assertTrue(any("artifacts differ from current bytes" in e for e in errors))

    def test_score_driving_sources_must_be_audited(self):
        # Primitive `a` is PROXY on S1; a review that never audited S1 is invalid.
        r = review_for(packet(), self.MECH, sources_audited=[])
        errors = validate_review(r, packet(), self.MECH)
        self.assertTrue(any("S1 was not audited" in e for e in errors))

    def test_estimate_cited_sources_must_be_audited(self):
        # Coverage is any primitive-cited source, not just OBSERVED/PROXY.
        p = packet(**{"primitives.q": primitive(source_ids=["S2"])})
        p["sources"].append({"id": "S2", "url": "https://example.com/2", "title": "t2",
                             "access_date": "2026-07-22", "supports": "synthetic"})
        errors = validate_review(review_for(p, self.MECH), p, self.MECH)
        self.assertTrue(any("S2 was not audited" in e for e in errors))

    def test_audit_entries_fully_validated(self):
        # Sol's canary-readiness blocker: {"source_id": "S1"} alone must fail.
        r = review_for(packet(), self.MECH, sources_audited=[{"source_id": "S1"}])
        errors = validate_review(r, packet(), self.MECH)
        self.assertTrue(any("reachable: required bool" in e for e in errors))
        self.assertTrue(any("support: must be one of" in e for e in errors))
        r = review_for(packet(), self.MECH, sources_audited=[
            {"source_id": "S1", "reachable": True, "support": "looks fine"}])
        errors = validate_review(r, packet(), self.MECH)
        self.assertTrue(any("support: must be one of" in e for e in errors))
        r = review_for(packet(), self.MECH, sources_audited=[
            {"source_id": "S99", "reachable": True, "support": "supported"},
            {"source_id": "S1", "reachable": True, "support": "supported"},
            {"source_id": "S1", "reachable": True, "support": "supported"}])
        errors = validate_review(r, packet(), self.MECH)
        self.assertTrue(any("unknown source 'S99'" in e for e in errors))
        self.assertTrue(any("duplicate audit of 'S1'" in e for e in errors))
        r = review_for(packet(), self.MECH, sources_audited=[
            {"source_id": "S1", "reachable": True, "support": "supported", "vibe": "good"}])
        errors = validate_review(r, packet(), self.MECH)
        self.assertTrue(any("unknown keys" in e for e in errors))

    def test_false_mechanics_requires_invalid(self):
        mech = dict(self.MECH, score_reproduces=False)
        r = review_for(packet(), mech)
        errors = validate_review(r, packet(), mech)
        self.assertTrue(any("false requires outcome invalid" in e for e in errors))
        r_invalid = review_for(packet(), mech, outcome="invalid")
        self.assertEqual(validate_review(r_invalid, packet(), mech), [])


FLEET_CODES = ("541511", "541512", "541513", "541519")


def fleet_targets(codes=FLEET_CODES, canary=()):
    return {"codes": [{"naics": n, "title": "Synthetic", "block": "B",
                       **({"canary": True} if n in canary else {})} for n in codes]}


class SamplingSentinels(unittest.TestCase):
    """The sample is code-owned and deterministic: frozen seed, mandatory
    top-tier stratum, min-3 random stratum, canaries outside the frame."""

    def _fleet_runs(self, tmp: Path, codes=FLEET_CODES):
        for naics in codes:
            p = packet(**{"identity.naics": naics, "identity.run_id": f"{naics}-t1"})
            run_dir = tmp / "runs" / naics / f"{naics}-t1"
            run_dir.mkdir(parents=True)
            (run_dir / "packet.json").write_text(json.dumps(p, indent=1), encoding="utf-8")
            finalize_path(run_dir / "packet.json")

    def test_deterministic_min3_and_strata(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp = Path(tmpdir)
            self._fleet_runs(tmp)
            targets = fleet_targets()
            s1 = compute_sample("B", targets, runs=tmp / "runs")
            s2 = compute_sample("B", targets, runs=tmp / "runs")
            self.assertEqual(s1, s2)
            # Stratum membership is consistent with each attempt-1 base tier.
            for naics in FLEET_CODES:
                score = json.loads((tmp / "runs" / naics / f"{naics}-t1" / "score.json").read_text())
                if score["tier"] in MANDATORY_TIERS:
                    self.assertIn(naics, s1["mandatory"])
                else:
                    self.assertNotIn(naics, s1["mandatory"])
            # min-3 rule on the non-mandatory frame.
            frame = [n for n in FLEET_CODES if n not in s1["mandatory"]]
            self.assertEqual(len(s1["random"]), min(len(frame), 3))
            self.assertTrue(set(s1["random"]) <= set(frame))

    def test_canary_outside_frame_and_denominator(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp = Path(tmpdir)
            self._fleet_runs(tmp)
            sample = compute_sample("B", fleet_targets(canary=("541511",)), runs=tmp / "runs")
            self.assertEqual(sample["canary"], ["541511"])
            self.assertNotIn("541511", sample["mandatory"])
            self.assertNotIn("541511", sample["random"])

    def test_incomplete_block_refuses_to_sample(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp = Path(tmpdir)
            self._fleet_runs(tmp, codes=FLEET_CODES[:3])
            with self.assertRaises(ValueError):
                compute_sample("B", fleet_targets(), runs=tmp / "runs")


class PublicationGateSentinels(unittest.TestCase):
    """End-to-end ledger gate: only closed blocks publish; a sampled record
    needs an accepted review or a reviewed exclusion; an unsampled record
    publishes as not_reviewed by design; nothing bypasses integrity."""

    def _run(self, tmp: Path, naics: str, run_id: str, attempt: int = 1):
        p = packet(**{"identity.naics": naics, "identity.run_id": run_id,
                      "identity.attempt": attempt})
        run_dir = tmp / "runs" / naics / run_id
        run_dir.mkdir(parents=True)
        (run_dir / "packet.json").write_text(json.dumps(p, indent=1), encoding="utf-8")
        finalize_path(run_dir / "packet.json")
        mechanics = check(run_dir)
        self.assertEqual(mechanics["errors"], [], mechanics)
        return p, run_dir, mechanics

    def _fleet(self, tmp: Path, codes=FLEET_CODES, canary=()):
        meta = {naics: self._run(tmp, naics, f"{naics}-t1") for naics in codes}
        targets = fleet_targets(codes, canary)
        sample = compute_sample("B", targets, runs=tmp / "runs")
        state = {"contract_sha256": contract_sha256_current(),
                 "blocks": {"B": {"status": "closed", "sample": sample}}}
        return targets, state, sample, meta

    def _review(self, meta, naics, **overrides):
        p, run_dir, mech = meta[naics]
        (run_dir / "review.json").write_text(
            json.dumps(review_for(p, mech, **overrides)), encoding="utf-8")

    def test_sampled_without_review_fails_closed(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp = Path(tmpdir)
            targets, state, sample, meta = self._fleet(tmp)
            with self.assertRaises(SystemExit):
                build_site(runs=tmp / "runs", site_out=tmp / "six.json",
                           targets=targets, state=state)

    def test_ledger_sampled_and_unsampled_publication(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp = Path(tmpdir)
            targets, state, sample, meta = self._fleet(tmp)
            for naics in sampled_codes(sample):
                self._review(meta, naics)
            site = build_site(runs=tmp / "runs", site_out=tmp / "six.json",
                              targets=targets, state=state)
            self.assertEqual(site["summary"]["published"], 4)
            self.assertEqual(site["label"], "provisional sampled-validation screen")
            self.assertEqual(site["coverage"]["universe"], 4)
            self.assertEqual(site["coverage"]["blocks_closed"], ["B"])
            unsampled = set(FLEET_CODES) - sampled_codes(sample)
            self.assertEqual(len(unsampled), 1)
            by_naics = {r["naics"]: r for r in site["records"]}
            for naics in FLEET_CODES:
                record = by_naics[naics]
                if naics in unsampled:
                    self.assertEqual(record["independent_review"], "not_reviewed")
                    self.assertIsNone(record["review"])
                else:
                    self.assertEqual(record["independent_review"], "accepted")
                    self.assertEqual(record["review"]["outcome"], "publishable_with_caveats")
            self.assertEqual(site["summary"]["independent_review"],
                             {"accepted": 3, "not_reviewed": 1})

    def test_open_block_publishes_nothing(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp = Path(tmpdir)
            targets, state, sample, meta = self._fleet(tmp)
            state["blocks"]["B"] = {"status": "research"}
            site = build_site(runs=tmp / "runs", site_out=tmp / "six.json",
                              targets=targets, state=state)
            self.assertEqual(site["summary"]["published"], 0)
            self.assertEqual(site["coverage"]["blocks_pending"], ["B"])

    def test_sample_drift_fails_closed(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp = Path(tmpdir)
            targets, state, sample, meta = self._fleet(tmp)
            for naics in sampled_codes(sample):
                self._review(meta, naics)
            state["blocks"]["B"]["sample"] = dict(sample, random=sample["random"][:-1])
            with self.assertRaises(SystemExit):
                build_site(runs=tmp / "runs", site_out=tmp / "six.json",
                           targets=targets, state=state)

    def test_missing_run_in_closed_block_fails_closed(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp = Path(tmpdir)
            targets, state, sample, meta = self._fleet(tmp)
            wider = fleet_targets(codes=FLEET_CODES + ("541611",))
            with self.assertRaises(SystemExit):
                build_site(runs=tmp / "runs", site_out=tmp / "six.json",
                           targets=wider, state=state)

    def test_reviewed_exclusion_closes_and_remediation_republishes(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp = Path(tmpdir)
            targets, state, sample, meta = self._fleet(tmp)
            rejected = sorted(sampled_codes(sample))[0]
            for naics in sampled_codes(sample):
                if naics == rejected:
                    self._review(meta, naics, outcome="reject", material_findings=[
                        {"category": "unsupported_claim", "finding": "x",
                         "materiality": "correcting q would change the base tier"}])
                else:
                    self._review(meta, naics)
            site = build_site(runs=tmp / "runs", site_out=tmp / "six.json",
                              targets=targets, state=state)
            self.assertEqual(site["summary"]["published"], 3)
            self.assertEqual(site["exclusions"][0]["naics"], rejected)
            self.assertTrue(site["exclusions"][0]["material_findings"])
            # The single remediation attempt, accepted, republishes the code.
            p2, dir2, mech2 = self._run(tmp, rejected, f"{rejected}-t2", attempt=2)
            (dir2 / "review.json").write_text(
                json.dumps(review_for(p2, mech2)), encoding="utf-8")
            site = build_site(runs=tmp / "runs", site_out=tmp / "six.json",
                              targets=targets, state=state)
            self.assertEqual(site["summary"]["published"], 4)
            self.assertEqual(site["exclusions"], [])
            by_naics = {r["naics"]: r for r in site["records"]}
            self.assertEqual(by_naics[rejected]["run_id"], f"{rejected}-t2")

    def test_tampered_score_fails_closed(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp = Path(tmpdir)
            targets, state, sample, meta = self._fleet(tmp)
            for naics in sampled_codes(sample):
                self._review(meta, naics)
            victim = sorted(sampled_codes(sample))[0]
            run_dir = meta[victim][1]
            score = json.loads((run_dir / "score.json").read_text())
            score["A"] = 9.99
            (run_dir / "score.json").write_text(json.dumps(score, indent=1, sort_keys=True) + "\n")
            with self.assertRaises(SystemExit):
                build_site(runs=tmp / "runs", site_out=tmp / "six.json",
                           targets=targets, state=state)

    def test_stale_review_digest_fails_closed(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp = Path(tmpdir)
            targets, state, sample, meta = self._fleet(tmp)
            for naics in sampled_codes(sample):
                self._review(meta, naics)
            victim = sorted(sampled_codes(sample))[0]
            p, run_dir, mech = meta[victim]
            (run_dir / "review.json").write_text(json.dumps(
                review_for(p, dict(mech, artifacts_sha256="c" * 64))), encoding="utf-8")
            with self.assertRaises(SystemExit):
                build_site(runs=tmp / "runs", site_out=tmp / "six.json",
                           targets=targets, state=state)

    def test_attempt_sequencing_fail_closed(self):
        # Attempt 2 after an ACCEPTED attempt 1 is rejected — remediation is
        # only permitted for reject/invalid.
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp = Path(tmpdir)
            targets, state, sample, meta = self._fleet(tmp)
            for naics in sampled_codes(sample):
                self._review(meta, naics)
            victim = sorted(sampled_codes(sample))[0]
            p2, dir2, mech2 = self._run(tmp, victim, f"{victim}-t2", attempt=2)
            (dir2 / "review.json").write_text(
                json.dumps(review_for(p2, mech2)), encoding="utf-8")
            with self.assertRaises(SystemExit):
                build_site(runs=tmp / "runs", site_out=tmp / "six.json",
                           targets=targets, state=state)

    def test_contract_drift_fails_check(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp = Path(tmpdir)
            p, run_dir, mech = self._run(tmp, "541512", "541512-t1")
            score = json.loads((run_dir / "score.json").read_text())
            score["contract_sha256"] = "0" * 64
            (run_dir / "score.json").write_text(dump_json(score))
            result = check(run_dir)
            self.assertTrue(any("contract drift" in e for e in result["errors"]))


if __name__ == "__main__":
    unittest.main(verbosity=2)
