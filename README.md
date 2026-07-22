# Roll-Up Economy

The current product is the reviewed v5.0 research-priority screen at [`/6digit/`](6digit/). It covers the frozen 63-code fleet and links every published result to its memo, factor chain, primitive evidence, sources, caveats, validator review, and change-evidence requests.

## Which document governs what

| Document | Role |
|---|---|
| [`pipeline/v5/methodology.md`](pipeline/v5/methodology.md) | Frozen governing methodology and scoring contract |
| [`pipeline/v5/research_brief.md`](pipeline/v5/research_brief.md) | Frozen research-author contract for reproducible v5 run series |
| [`pipeline/v5/validator_brief.md`](pipeline/v5/validator_brief.md) | Frozen isolated-review contract for reproducible v5 run series |
| [`V5_PLAN.md`](V5_PLAN.md) | Completed v5 implementation tracker |
| [`V5_CANARY_REPORT.md`](V5_CANARY_REPORT.md) | Phase 2 canary gate record |
| [`V5_PHASE3_REPORT.md`](V5_PHASE3_REPORT.md) | Completed fleet campaign report |
| [`V5_CLOSURE_REPORT.md`](V5_CLOSURE_REPORT.md) | Final v5 campaign ledger and maintenance handoff |
| `V3_*` and `V4_*` | Preserved historical development records |

## v5 snapshot

<!-- DASHBOARD_STATS_START -->
This block is generated from `six_data_v5.json` and the validated review artifacts by `pipeline/v5/update_docs.py`.

- Publication: 63 records published; 0 excluded
- Reviewed attempts: 65 total — 0 `publishable`, 63 `publishable_with_caveats`, 0 `reject`, 2 `invalid`
- Remediation: 2 bounded attempt-2 records; 2 accepted
- Material findings: 0 across all review attempts
- Published source audits: 252 supported, 156 partially supported, 7 unsupported, 3 not score-driving
- Tiers: 3 highest priority, 12 priority, 30 conditional, 11 low priority, 5 structural out, 2 unscored dataset gaps
- Readiness: 61 model-conditioned, 2 stress-test-only
- Actions: 61 validate assumptions, 2 evidence first
- Robust tiers: 2; methodology 5.0; unreviewed publication disabled
<!-- DASHBOARD_STATS_END -->

The dashboard reads the deterministic publication output directly. Highest Priority means research next, never buy; model-conditioned results require assumption validation, while missing base inputs route to Evidence First.

## Maintenance and refresh cadence

Check the deterministic dataset layer at least annually and rebuild it when a
newer applicable release is available. QCEW, OEWS, and IPS update annually;
SUSB receipts refresh with Economic Census years. The pinned vintages, source
cadence, and deterministic rebuild procedure are documented in
[`pipeline/datasets/README.md`](pipeline/datasets/README.md). Do not overwrite
the artifacts of a published campaign.

Market-sensitive packet evidence—including transaction activity, AI adoption
and capability, pricing and value capture, regulation, and demand—is treated as
stale about 12 months after the research date. On staleness or a dataset
refresh, launch a new date-stamped run series under the same frozen v5
methodology in a separate campaign namespace—never as an attempt 3 or an
overwrite of `pipeline/v5/runs/`. Repeat isolated review and rebuild to a new
publication output through the fail-closed gate. Any change to formulas,
anchors, tier cuts, or evidence rules requires a new methodology version.

## Run locally

From the repository root:

```bash
python3 -m http.server 4173 --bind 127.0.0.1
```

Open <http://127.0.0.1:4173/6digit/>.

## Validate

```bash
python3 pipeline/v5/test_v5.py
python3 pipeline/v5/build.py site
python3 pipeline/v5/update_docs.py --check
node --check 6digit/dashboard.js
git diff --check
```

## Canonical outputs

- [`6digit/six_data_v5.json`](6digit/six_data_v5.json) — fail-closed published dashboard data
- [`pipeline/v5/runs/`](pipeline/v5/runs/) — packets, scores, memos, and isolated reviews
- [`pipeline/v5/`](pipeline/v5/) — frozen briefs, schemas, scorer, build, and tests
- [`V5_CANARY_REPORT.md`](V5_CANARY_REPORT.md), [`V5_PHASE3_REPORT.md`](V5_PHASE3_REPORT.md), and [`V5_CLOSURE_REPORT.md`](V5_CLOSURE_REPORT.md) — campaign gate, fleet, and closure records

`six_data_v3.json`, `six_data_v4.json`, and the v3/v4 root documents remain available only as archived comparisons and development history. The root 4-digit prototype and its duplicate `naics_CA_data.json`, `naics_M_data.json`, and `pnl_data.json` inputs are likewise archived; the current product is `/6digit/`.
