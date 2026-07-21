# Roll-Up Economy

The current product is the Phase-4 v3.1.2 evidence map at [`/6digit/`](6digit/). The root page is the archived 4-digit prototype and is clearly marked as superseded.

## Phase-4 snapshot

<!-- DASHBOARD_STATS_START -->
This block is derived from `pipeline/build/stats.json`, `campaign_report_v3_1_2.json`, and `golden_analysis_v3_1_2.json` by `pipeline/build/update_dashboard_docs.py`.

- Campaign: closed and complete; 83 planned records independently reviewed
- Attempts: 99 total, including 16 bounded remediations
- Publication: 82 records published with caveats; 1 fleet record excluded
- Fleet dashboard: 62 published records — 3 conditional, 6 pass, 53 kill
- Fleet confidence: 15 MED, 47 LOW; 9 borderline records
- Source review: 318 supported, 228 partially supported, 30 not score-driving
- Golden diagnostic: separation PASS; 20/20 mechanics-clean and published with caveats
- Frozen scoring model: thresholds version 3.0
<!-- DASHBOARD_STATS_END -->

The dashboard reads the generated outputs directly. It keeps fleet rankings, golden diagnostics, and exclusions separate, and links every result to its packet, finalized record, memo, review, sources, and caveats.

## Run locally

From the repository root:

```bash
python3 -m http.server 4173 --bind 127.0.0.1
```

Open <http://127.0.0.1:4173/6digit/>.

## Validate

```bash
python3 -m unittest discover -s pipeline/build -p 'test_*.py'
python3 pipeline/build/assemble_prompts.py --check
python3 pipeline/build/assemble_prompts.py --template-version 3.1 --check
python3 pipeline/build/assemble_prompts.py --template-version 3.1.1 --check
python3 pipeline/build/assemble_prompts.py --template-version 3.1.2 --check
python3 pipeline/build/golden_analysis_v3_1_2.py
python3 pipeline/build/review_campaign_v3_1_2.py validate
python3 pipeline/build/update_dashboard_docs.py --check
node --check 6digit/dashboard.js
git diff --check
```

## Canonical outputs

- `6digit/six_data_v3.json` — published fleet dashboard records
- `pipeline/build/campaign_report_v3_1_2.json` — closed-campaign counts, attempts, caveats, and exclusions
- `pipeline/build/golden_analysis_v3_1_2.json` — isolated golden diagnostic
- `pipeline/packets/`, `pipeline/runs/`, `pipeline/golden_v3_1_2/`, `pipeline/memos/`, and `pipeline/review/` — underlying traceability artifacts

The scoring model, Phase-4 artifacts, earlier contract versions, and excluded records are preserved. Phase 6 has not started.
