# v5 campaign closure report

**Status:** closed on 2026-07-22. Methodology 5.0 is frozen and the reviewed
63-code publication set is complete.

This note is the final campaign ledger. The Phase 2 canary gate was approved
before fleet work began, every frozen-scope code was attempted and independently
reviewed, the bounded remediation wave is closed, and the fail-closed site build
publishes the complete fleet.

## Final disposition

| Measure | Result |
|---|---:|
| Frozen fleet codes | 63 |
| Unique codes attempted | 63 |
| Research attempts | 65 |
| Unique codes independently reviewed | 63 |
| Review attempts | 65 |
| Codes remediated once | 2 |
| Published | 63 |
| Excluded | 0 |

The two extra attempts were the single permitted remediations for **541410**
and **541420**. Their attempt-1 reviews were `invalid` because the packet
`run_id` values carried an erroneous `run` prefix; both fresh attempt-2 runs
were accepted. Across all 65 review attempts, outcomes were 63
`publishable_with_caveats`, 2 `invalid`, 0 `publishable`, and 0 `reject`.
There were zero material findings. Every final published record is
`publishable_with_caveats`.

## Published distributions

| Dimension | Count |
|---|---:|
| Tier — `HIGHEST_PRIORITY` | 3 |
| Tier — `PRIORITY` | 12 |
| Tier — `CONDITIONAL` | 30 |
| Tier — `LOW_PRIORITY` | 11 |
| Tier — `STRUCTURAL_OUT` | 5 |
| Tier — unscored dataset gap | 2 |
| Readiness — `MODEL_CONDITIONED` | 61 |
| Readiness — `STRESS_TEST_ONLY` | 2 |
| Action — `VALIDATE_ASSUMPTIONS` | 61 |
| Action — `EVIDENCE_FIRST` | 2 |
| Robust tier present | 2 |

The two unscored records, 523940 and 541120, have frozen dataset gaps and
therefore route to `STRESS_TEST_ONLY / EVIDENCE_FIRST`. The two robust records,
541713 and 541922, remain `STRUCTURAL_OUT` across their tier intervals.

## Calibration verdict

The five-code v4.3-to-v5 canary comparison found the archived v4.3 adapter's
H constants systematically generous and its elicited C constants harsh. Fresh
evidence compressed H, lifted C, and flipped the canary leader from 541512 to
541214. This is an interpretation result, not a tuning instruction: no formula,
anchor, tier cut, evidence rule, frozen brief, or methodology contract changed
before or during the fleet campaign.

## Integrity and publication state

- The frozen fleet in
  [`pipeline/blocks/targets_phase3.json`](pipeline/blocks/targets_phase3.json)
  exactly matches the 63 code directories in `pipeline/v5/runs/`.
- All 65 attempts contain a packet, deterministic score, memo, and isolated
  review; final packets pass `validate`, `finalize`, and `check`.
- All accepted reviews bind to the exact artifact bytes and reproduce the
  mechanics block required by `build.py check`.
- The sentinel suite passes 37/37.
- `python3 pipeline/v5/build.py site` publishes 63 records and excludes zero;
  unreviewed or stale artifacts still fail closed.
- [`6digit/six_data_v5.json`](6digit/six_data_v5.json) is the canonical
  dashboard publication output.

## Maintenance handoff

Published campaign artifacts are immutable history. Check the deterministic
dataset layer at least annually and rebuild it when newer applicable releases
arrive. QCEW, OEWS, and IPS are annual; SUSB receipts refresh with Economic
Census years. The pinned vintages and exact source cadence are maintained in
[`pipeline/datasets/README.md`](pipeline/datasets/README.md).

Market-sensitive packet evidence is treated as stale about 12 months after its
research date. For this 2026-07-22 campaign, review that evidence by roughly
2027-07-22. A data refresh or stale market evidence starts a new date-stamped
run series under the same frozen methodology in a separate campaign namespace,
with fresh isolated reviews and a new publication output. It is never an
attempt 3 or an overwrite of `pipeline/v5/runs/`. Any change to a formula,
anchor, tier cut, or evidence rule requires a new methodology version.

Scope expansion and target/buyer diligence remain outside v5.0 and begin only
as separately governed work described in [`V5_PLAN.md`](V5_PLAN.md).

## Usage disclosure

The repository does not contain a campaign-wide platform export of model usage
or cost, so no aggregate token or dollar total is asserted or extrapolated.
[`V5_CANARY_REPORT.md`](V5_CANARY_REPORT.md) preserves the platform-observed
canary ranges that were available at the Phase 2 gate.
