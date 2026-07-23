# Roll-Up Economy

The current product is the closed v5.1 provisional sampled-validation screen served at the site root ([index.html](index.html)). It covers all 1,012 six-digit NAICS 2022 industries and links every result to its memo, factor chain, primitive evidence, sources, caveats, explicit independent-review status, and change-evidence requests. The fully reviewed 63-code v5.0 campaign remains immutable history.

## Which document governs what

| Document | Role |
|---|---|
| [`pipeline/v5_1/methodology.md`](pipeline/v5_1/methodology.md) | Frozen v5.1 governing methodology and sampled-validation contract |
| [`pipeline/v5_1/research_brief.md`](pipeline/v5_1/research_brief.md) | Frozen v5.1 research-author contract |
| [`pipeline/v5_1/validator_brief.md`](pipeline/v5_1/validator_brief.md) | Frozen v5.1 isolated-review contract |
| [`V5_1_PLAN.md`](V5_1_PLAN.md) | Completed v5.1 campaign contract and tracker |
| [`V5_1_CANARY_REPORT.md`](V5_1_CANARY_REPORT.md) | v5.1 canary gate record |
| [`V5_1_FLEET_REPORT.md`](V5_1_FLEET_REPORT.md) | v5.1 block-by-block campaign report |
| [`V5_1_CLOSURE_REPORT.md`](V5_1_CLOSURE_REPORT.md) | Final v5.1 campaign ledger, pooled sample statistics, and maintenance handoff |
| [`V5_CLOSURE_REPORT.md`](V5_CLOSURE_REPORT.md) | Immutable fully reviewed v5.0 campaign ledger |
| `V3_*` and `V4_*` | Preserved historical development records |

## v5.1 snapshot

<!-- DASHBOARD_STATS_START -->
This block is reconciled from `six_data_v5_1.json`, canonical campaign state,
and the validated review artifacts.

- Publication: 1,012/1,012 records across 20 closed blocks; 0 excluded or descoped
- Independent review: 178 accepted; 834 explicitly `not_reviewed`
- Review strata: 64 mandatory, 104 deterministic random, 10 canary
- Review outcomes: 178 `publishable_with_caveats`; 0 `publishable`, `reject`, or `invalid`
- Remediation and material findings: 0
- Reviewed source audits: 1,038 supported, 398 partially supported, 68 unsupported, 1 not score-driving
- Tiers: 19 highest priority, 46 priority, 161 conditional, 228 low priority, 367 structural out, 191 without a base tier
- Readiness/actions: 821 model-conditioned / validate assumptions; 191 stress-test-only / evidence first
- Robust tiers: 167; methodology 5.1; provisional sampled-validation label retained
<!-- DASHBOARD_STATS_END -->

The dashboard reads the deterministic v5.1 publication output directly and
never presents an unsampled record as reviewed. Highest Priority means
research next, never buy; model-conditioned results require assumption
validation, while missing base inputs route to Evidence First.

## Maintenance and refresh cadence

Check the deterministic dataset layer at least annually and rebuild it when a
newer applicable release is available. QCEW, OEWS, and IPS update annually;
SUSB receipts refresh with Economic Census years. The pinned vintages, source
cadence, and deterministic rebuild procedure are documented in
[`pipeline/datasets/README.md`](pipeline/datasets/README.md). Do not overwrite
the artifacts of a published campaign.

Market-sensitive packet evidence—including transaction activity, AI adoption
and capability, pricing and value capture, regulation, and demand—is treated as
stale about 12 months after the 2026-07-22 research date. On staleness or a
dataset refresh, launch a new date-stamped run series in a separate campaign
namespace—never an overwrite of `pipeline/v5_1/runs/`. Repeat deterministic
sampling and isolated review, then rebuild to a new publication output through
the fail-closed gate. Any change to formulas, anchors, tier cuts, or evidence
rules requires a new methodology version.

## Run locally

From the repository root:

```bash
python3 -m http.server 4173 --bind 127.0.0.1
```

Open <http://127.0.0.1:4173/>.

## Validate

```bash
python3 pipeline/v5_1/test_v5_1.py
python3 pipeline/v5_1/build.py audit-state
python3 pipeline/v5_1/build.py site
node --check dashboard.js
git diff --check
```

## Canonical outputs

- [`6digit/six_data_v5_1.json`](6digit/six_data_v5_1.json) — fail-closed provisional sampled-validation dashboard data (path frozen by the v5.1 contract)
- [`pipeline/v5_1/runs/`](pipeline/v5_1/runs/) — packets, scores, memos, and sampled isolated reviews
- [`pipeline/v5_1/`](pipeline/v5_1/) — frozen briefs, schemas, scorer, build, state, and tests
- [`V5_1_CANARY_REPORT.md`](V5_1_CANARY_REPORT.md), [`V5_1_FLEET_REPORT.md`](V5_1_FLEET_REPORT.md), and [`V5_1_CLOSURE_REPORT.md`](V5_1_CLOSURE_REPORT.md) — campaign gate, fleet, and closure records

`pipeline/v5/` remains immutable v5.0 history. Retired artifacts — the v5.0
dataset `six_data_v5.json`, the earlier `six_data*.json` versions, the root
4-digit prototype and its `naics_CA_data.json`, `naics_M_data.json`, and
`pnl_data.json` inputs, and the `deep-dives/` pages — were removed from the
working tree and live in git history (last present at commit `6635e79`).
