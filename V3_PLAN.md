# v3 Implementation Plan

**Companion to:** [V3_PRODUCT.md](V3_PRODUCT.md) (goal, principles, pipeline spec) · created 2026-07-20
**Status legend:** `[ ]` todo · `[x]` done · `[~]` in progress. This file is the working tracker — update checkboxes as work lands.

Sequencing has two deliberate inversions: the build/check script (Phase 2) is built **before** any runs, so the pilot validates itself from day one; the dataset layer (Phase 1) comes **before** prompt generation, because prompts embed the precomputed dataset inputs.

---

## Phase 0 — Restructure & freeze (Stage 0) · ~1 day + sign-offs

**Blocking item: the five decisions in `V3_PRODUCT.md` §9 must be resolved before the freeze. Everything else in this phase can proceed in parallel.**

- [x] 0.1 Create `pipeline/` skeleton (`template/ datasets/ blocks/ prompts/ runs/ golden/ review/ build/`)
- [x] 0.2 Move prototypes into the repo so they're git-tracked: `../prompt_template_v2.md`, `../prompts_54/` (12 prompts + `blocks_batch1.json`), `../results_54/541330.json` (copied in; originals in `../` can be deleted after commit)
- [x] 0.3 Decide §9 items (owner: Victor):
  - [x] cut values & factor floors — decided 2026-07-20: **Hell-Yes S ≥ 7.0, every factor ≥ 6.0** (stricter option); Strong ≥ 5.5; Conditional ≥ 4.0; Pass ≥ 3.0; KILL below or any factor < 1.0
  - [x] C composition — decided: **folded** (C = 10 × π_dist × π_moat, pricing deflation reflected in π_dist with mechanism stated)
  - [x] golden-set membership — approved 2026-07-20: 20 codes (12 winners, 5 melters, 3 controls) in `pipeline/golden/golden_set.json` v1.0
  - [x] P&L card — decided: **drop for launch**; may return later derived from datasets
  - [x] v1 (4-digit) page — decided: **archive live with a "superseded by v3" banner**
- [x] 0.4 Write `pipeline/template/prompt_template_v3.md` from v2. Changes: floats end-to-end (no `round()` in factor formulas); PD removed from B; output additions — overall confidence, per-source access dates, `heterogeneous` flag, run-metadata block; dataset inputs marked "provided — do not research"; judgment inputs explicitly labeled as declared opinions
- [x] 0.5 JSON Schemas: run record + review record (`pipeline/build/schemas/`)
- [x] 0.6 `pipeline/build/thresholds.json` — single source for cuts, floors, gates, borderline ε; consumed by build and generated docs (P8). Decided values applied
- [x] 0.7 Freeze: tagged `v3.0-freeze` 2026-07-20 — template 3.0, schemas, thresholds (frozen: true), golden set v1.0. After this point rubric changes = new version + full re-run

**Deliverable:** frozen v3 rubric in-repo. **Done when:** tag exists and §9 has no open items.

## Phase 1 — Dataset layer (Stage 1) · ~1–2 days

- [x] 1.1 Download scripts + checksums into `pipeline/datasets/raw/`: Census SUSB (firms by size class per NAICS), CBP, BLS OEWS industry tables, QCEW
- [x] 1.2 Derivation code → `pipeline/datasets/derived/<naics>.json` per code: `labor_share`, OEWS role mix, `n_total`, size-class distribution → $1–10M EBITDA band chain (`n_band`)
- [x] 1.3 Sanity check vs known points: 541330 (reference labor share 0.470 from BLS-via-FRED) + 3–4 hand-checked codes across different sectors — QCEW-method labor_share harmonized to the IPS basis (÷ median ×1.3407 from the 65 dual-method codes); 541330 independent cross-method lands at 0.4924 vs 0.470 reference (see `pipeline/datasets/sanity_check.md`)
- [x] 1.4 Coverage report: which of the 1,012 codes lack a direct series and use a stated fallback (parent-code inheritance, imputation — method recorded per code)

**Deliverable:** deterministic dataset inputs for all 1,012 codes. **Done when:** coverage report shows 100% with method stated; spot checks pass.

## Phase 2 — Build & check script (Stage 4) · ~1 day

- [x] 2.1 Build script: schema validation → arithmetic recompute from inputs (**hard fail on any mismatch**) → S, gates, verdicts, borderline flags, percentile context → generate `6digit/six_data_v3.json` (v2 `six_data.json` stays archived) + `pipeline/build/stats.json` for README/methodology numbers. `pipeline/build/build.py`, stdlib-only, accepted-review filter with `--allow-unreviewed` for the pilot. Note: schemas + template bumped 3.0.1 (machine-readable `succession_shortage_documented` inside `owners_60plus_pct` — clarification only, no rubric change; needs human sign-off)
- [x] 2.2 Deep-dive reconciliation report: `pipeline/build/reconciliation.md` generated from `pipeline/build/deep_dive_expectations.json` (stances + quotes extracted from `deep-dives/*.html`, human-curated-pending-review)
- [x] 2.3 Per-record flag list for the validator → `pipeline/build/flags.json` (LOW confidence, borderline, gate_blocked, uplift-vs-A tension, ESTIMATE-heavy, within-tolerance arithmetic deltas)
- [x] 2.4 Regression fixture: 541330 adapted to the v3 schema (`pipeline/runs/541330/2026-07-20_sonnet_tv3_fixture.json`, scores recomputed with v3 float formulas: V 7.12 / C 3.03 / A 3.33 / B 8.01 / M 4.0 → S 4.70, conditional) + a temporary bootstrap acceptance in `pipeline/review/541330.json` to exercise the filter; the production bootstrap was removed before the Phase-4 validator canary. Permanent tests in `pipeline/build/test_build.py` cover fixture success, corruption failure, threshold coupling and determinism.

**Deliverable:** one-command deterministic build. **Done when:** fixture passes; intentionally corrupted arithmetic fails the build.

## Phase 3 — Prompt generation (Stage 2) · ~½ day for sector 54

- [x] 3.1 Meta-prompt for Sol producing per-code blocks — `pipeline/template/blocks_meta_prompt_v3.md` + deterministic `pipeline/build/assemble_prompts.py` (validates shape, placeholders, byte-determinism) + `pipeline/blocks/targets_phase3.json` (63 codes: 49× sector 54 + 14 non-54 golden). **Null-handling rule (from the phase 1–2 review):** when a dataset input is `null` (84 labor_share, 181 n_band data gaps), the generated prompt must instruct the run to research that input itself, show the chain, and mark it ESTIMATE — a documented exception to "dataset inputs are never researched"
- [x] 3.2 63 blocks written by 5 parallel Sol agents (golden codes with extra rigor; dataset oddities encoded in special_notes; unverified sources flagged `uncertain_exists`) → assembled + validated: 63/63 prompts in `pipeline/prompts/`, `--check` green, runtime placeholders intact

**Deliverable:** v3 prompts for sector 54. **Done when:** each prompt validates against the template (all placeholders filled, dataset inputs present).

## Phase 4 — Pilot: sector 54 + golden set (Stages 3 + 5) · ~1–2 days incl. iteration

- [x] 4.1 Fleet runs done via in-session agents (not API batch — deferred to Phase 6): 63/63 codes validated (schema + arithmetic recompute), verdicts 7 conditional / 27 pass / 29 kill / 0 green, 20 borderline. **Incident log:** first wave (3-codes-per-agent briefs) collapsed into delegation cascades + a platform outage → 0 usable records; fixed with single-author 2-code briefs + mandatory real-validator self-check loop → 63/63 clean ("s2" runs). Lesson encoded for Phase 6: one API call per code, validator-in-the-loop
- [x] 4.2 Golden-set runs (20, Sol) in `pipeline/golden/` — separation PASS (`golden_analysis.py`); all 20 codes also have GPT-5.5 fleet runs as the benchmark. Observed: tight cross-model agreement on structure/mechanisms; divergence concentrated in t50 and multiples; 2 terminal-class boundary disagreements (541930 translation, 561492 court reporting) + payer-clawback C-vs-T ambiguity (healthcare codes) — template clarification candidates
- [~] 4.3 **RESOLVED 2026-07-20, in progress** — full-depth Sol validator pass over all 83 records, with no risk-tiering: 63 fleet records plus 20 separate golden reference records. Every URL anywhere in each record and every quoted figure is audited; judgment inputs, rubric consistency, dataset agreement and cross-check honesty are reviewed; every Stage-4 flag is addressed. Reviews are run-scoped at `pipeline/review/<naics>/<run-id>.json`. The Phase-2 production bootstrap was removed before the validator canary.
- [ ] 4.4 `wrong` records re-run with critique attached (blocked on 4.3)
- [ ] 4.5 Judge pilot vs frozen pass criteria (partially done: golden separation PASS, zero arithmetic mismatches across all 83 records; acceptance-rate criterion blocked on 4.3):
  - golden gate passes both `python3 pipeline/build/review_campaign.py validate` (all exact-run reviews and campaign invariants) and `python3 pipeline/build/golden_analysis.py` (known winners above known melters; melters caught by the T gate)
  - zero arithmetic mismatches in the build
  - all 83 current records accepted after remediation, with zero unresolved citation/check failures
  - initial acceptance rate and source-quality distribution reported as diagnostics; no post-hoc percentage target is invented after seeing the records
- [ ] 4.6 If the **instrument** fails: fix template → bump to v3.1 → re-freeze → re-run pilot. Never hand-fix records.

**Deliverable:** accepted run records for sector 54 + golden set. **Done when:** 4.5 criteria all pass.

## Phase 5 — Dashboard traceability · ~1–2 days (can overlap Phase 4)

- [ ] 5.1 Remove: 13-cell matrix UI, the three threshold ladders, fake-link rendering of non-URL sources
- [ ] 5.2 Add evidence panel: verdict → S → factors → formulas → inputs → source / URL / quoted figure / quality flag
- [ ] 5.3 Card badges: overall confidence, acceptance status, `borderline`, `heterogeneous`; percentile shown as context next to the absolute verdict; run metadata (model, date, run id, template version, validator verdict)
- [ ] 5.4 Apply the P&L decision from 0.3
- [ ] 5.5 README + methodology page numbers generated by the build (P8); hand-written claims removed

**Deliverable:** site renders v3 records with the full why-chain. **Done when:** every displayed number is clickable down to a source or marked ESTIMATE.

## Phase 6 — Full run (1,012 codes) · ~2–3 days elapsed, mostly batch waiting

- [ ] 6.1 Prompt generation for all codes, batched by sector
- [ ] 6.2 GPT-5.5 run fleet via API batch; per-sector cost + acceptance-rate tracking
- [ ] 6.3 Validator pass over every record; `wrong` → re-run loop until the queue drains
- [ ] 6.4 Final build, publish; deep-dive reconciliation reviewed
- [ ] 6.5 Archive/remove v1 & v2 per decision 0.3; stale-input refresh cadence noted in README (market inputs ~12 months)

**Deliverable:** the v3 map live. **Done when:** all 1,012 published records are validator-accepted and the build is green.

---

## Cost & timeline (rough)

| Item | Estimate |
|---|---|
| GPT-5.5 run fleet, 1,012 codes × observed token mix | Recalculate after the validator canary; standard API is $5/M input + $30/M output, with GPT-5.5 Batch/Flex at half the standard rate |
| Sol: prompt gen + full-depth validator × 1,012 + ~20 golden runs | Recalculate from measured input, cached-input, output/reasoning tokens and web calls; Sol standard pricing matches GPT-5.5 standard pricing, so the old ~5× premise is false |
| Calendar | ~2–3 weeks part-time; Phases 0–2 week 1, 3–4 week 2, 5–6 week 3 |

**Critical path:** 0.3 decisions → 0.7 freeze → 1.x datasets → 3.x prompts → 4.x pilot → 6.x full run. Phases 2 and 5 hang off the critical path and can run in parallel with their neighbors.

**First move:** draft the golden-set list + confirm proposed cut values (0.3), restructure the repo (0.1–0.2) in the same pass.
