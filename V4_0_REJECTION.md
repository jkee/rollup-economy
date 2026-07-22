# v4.0 Methodology Rejection Record

> **Historical:** preserved v4 development record; v5 supersedes this line of work.

**Decision date:** 2026-07-21

**Decision:** reject v4.0 as a publication or campaign instrument; preserve all
v4.0 artifacts as immutable development diagnostics.

This rejection does not alter any v3 or v4.0 byte. It invalidates v4.0 scores,
verdicts, readiness labels, and actions for publication, fleet comparison,
campaign acceptance, or threshold calibration. v4.1 is a new instrument, not
a reinterpretation of v4.0.

## 1. Reproduced defects

The rejection follows a skeptical methodology and implementation audit. The
following defects were reproduced before accepting any v4.0 review.

1. **Nonportable cuts and failed weak-link semantics.** v4.0 retained v3 cuts
   after materially redefining factors, especially making a flat multiple M=5.
   With four factors at 10, a fifth factor of approximately 0.504 still reached
   `strong`. Ten-percent commercial retention, C=1, could produce S≈6.31.
2. **Evidence-dependent economics.** The same C or M value could be `kill` when
   DIRECT and non-kill when PROXY or ASSUMPTION. Weaker evidence could therefore
   improve the economic verdict.
3. **Arbitrary missing-data decisions.** Neutral defaults created base scores
   from unavailable evidence. Missing AI role values and missing operator
   survival still required score- or gate-driving authored choices. UNPROVEN
   pass/conditional outputs could produce `DEPRIORITIZE` or `SELECTIVE` despite
   intervals spanning `kill` through `strong` or `hell_yes`.
4. **Outcome-selective archetypes.** “Dominant or most investable” allowed
   discretionary selection after considering economics. Coverage adjusted B,
   while V continued to use broader NAICS role weights, so the stated unit of
   analysis was inconsistent across factors.
5. **Invalid adoption construct.** A rewarded rapid market-wide diffusion,
   which is not acquirer implementation speed and can instead shorten the
   arbitrage window or increase commercial pressure.
6. **Incomplete valuation construct.** M treated flat 4x→4x and 12x→12x as
   equivalent, lacked a holding period and consistent exit entity, and could
   embed successful scale transformation in an exit comp.
7. **Buyer-competition double count.** Active consolidators penalized B while
   also influencing entry price in M, and their possible positive effect on
   exit liquidity was not modeled consistently.
8. **Overstated readiness.** `SUBSTANTIATED` was reachable using all MED proxies
   or with one pivotal LOW input and did not require decision stability or
   supported role-level endpoints.
9. **Capture/survival overlap.** C included repricing and competitive response,
   while PRESSURED survival also included price pressure. A narrative request
   for separate horizons did not prevent double counting.
10. **Canary acceptance did not test validity.** Five honest UNPROVEN records
    with maximally broad intervals could satisfy the written publication
    concept. Named outcomes were excluded, but no frozen sentinel or economic-
    sense rubric replaced them.
11. **The validator did not enforce the written gate.** An internally
    consistent `reject` or `invalid` review could validate; exact accepted
    lineage, at-most-one remediation, repeated defects, human review, and all
    monotonicity conditions were not enforced together.
12. **Unauditable anti-outcome freeze.** `frozen: true` and a date were
    self-assertions rather than a committed, signed, externally timestamped
    code/config/prompt digest. “Method defect” was not bounded as a revision
    trigger after results were viewed.
13. **Incomplete threshold contract.** V, A, and B anchors, seller adjustments,
    competition caps, readiness mappings, actions, and sensitivity semantics
    were distributed through hard-coded Python rather than one complete frozen
    contract.
14. **Sensitivity-label mismatch.** The displayed envelope was a simultaneous
    corner sensitivity, not a statistical interval, and `CROSS_TIER` compared
    gated endpoint verdicts rather than implementing its documented numeric-cut
    meaning.

These are method defects requiring a new version. They are not publication
caveats that can be repaired by adding prose to individual records.

## 2. Invalidated five-record development run

Five v4.0 attempt-1 packets were finalized before rejection. The values below
are reproduced from their exact finalized records.

| NAICS | Run ID | S low/base/high | Raw verdict | Gated verdict | Readiness | Action |
|---|---|---:|---|---|---|---|
| 238220 | `2026-07-21_canary_v4_238220_a1` | 0.000000 / 4.344167 / 6.410096 | conditional | conditional | UNPROVEN | SELECTIVE |
| 541214 | `2026-07-21_canary_v4_541214_a1` | 0.000000 / 5.661016 / 9.082895 | strong | pass | UNPROVEN | DEPRIORITIZE |
| 541511 | `2026-07-21_canary_v4_541511_a1` | 0.000000 / 6.127854 / 9.877511 | strong | strong | UNPROVEN | EVIDENCE_FIRST |
| 541512 | `2026-07-21_canary_v4_541512_a1` | 4.647784 / 7.482494 / 8.572237 | strong | strong | UNPROVEN | EVIDENCE_FIRST |
| 541930 | `2026-07-21_canary_v4_541930_a1` | 0.000000 / 4.546224 / 7.314575 | conditional | conditional | UNPROVEN | SELECTIVE |

All five sensitivity records crossed a gated verdict tier. All five were
UNPROVEN. As of rejection there were **zero v4.0 review files**, so the written
5/5 independent-publication-review gate was never attempted or satisfied.

These records are therefore:

- not accepted canaries;
- not publication eligible;
- not Phase-4 fleet members;
- not evidence for retaining or changing a threshold; and
- not comparable to v3 or future v4.1 scores.

They remain useful only as disclosed development diagnostics and as inputs to
mechanical regression checks. Their named outcomes may not be used as v4.1
acceptance conditions.

The separate `pipeline/v4/shadow_canary.json` translation is likewise a
formula diagnostic, not research evidence, a review, or an accepted canary.

## 3. Preservation and replacement

The v4.0 methodology, thresholds, scoring code, packets, finalized records,
memos, and shadow diagnostic must remain byte-unchanged. No record is deleted,
relabeled as v4.1, or silently re-finalized.

New research may resume only under a separately versioned v4.1 artifact set
that implements `V4_1_METHODOLOGY.md`, passes its synthetic sentinels, freezes
complete version digests before results, reruns the disclosed five-code set as
development regression data, and passes the untouched deterministic holdout.
