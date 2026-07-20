# v3 Run Playbook

**Status: living document, incomplete** — captures how to re-run the project end-to-end, which model runs what and why, and what it costs. Written after the sector-54 pilot (2026-07-20); the Stage-5 policy is resolved and the Phase-6 API runner remains TBD. Companions: [V3_PRODUCT.md](V3_PRODUCT.md) (what and why), [V3_PLAN.md](V3_PLAN.md) (progress tracker).

---

## 1. The pipeline in one view

```
Stage 0  freeze          templates/thresholds/schemas/golden set   no model
Stage 1  datasets        Census/BLS bulk → derived/<naics>.json    no model      re-run: annually or on new vintage
Stage 2  prompt design   blocks + contract review                  Sol           re-run: on template version bump
         prompt assembly blocks/<naics>.json → prompts/<naics>.md  Python only   deterministic
Stage 3  research runs   prompts → runs/<naics>/<runid>.json       Terra fleet / Sol golden
Stage 4  build           runs → six_data_v3.json + stats + flags   no model      re-run: on any input change (seconds)
Stage 5  acceptance      records → review/<naics>/<run-id>.json    Sol           full depth on every record
```

Everything is re-runnable from the repo alone: prompts, records, thresholds, and scripts are all committed. A fresh session needs only this file, V3_PLAN.md, and the repo.

## 2. Model-choice logic

The rule (P9): **cheap by default, best model only where quality compounds.**

| Work | Model | Why |
|---|---|---|
| Dataset layer, build, assembly, analysis | none (Python) | Deterministic; models banned by design |
| Prompt design/review (Stage 2) | **Sol (`gpt-5.6-sol`)** | One-time contract work; errors propagate into every downstream run |
| Prompt assembly (Stage 2) | **plain Python only** | Deterministic merge and validation; models prohibited |
| Golden-set reference runs | **Sol (`gpt-5.6-sol`)** | 20 codes anchoring the instrument; the quality ceiling everything is benchmarked against |
| Fleet research runs (Stage 3) | **Terra (`gpt-5.6-terra`)** | Current fleet-research decision; exact runtime ID is recorded in every draft/run |
| Acceptance validator (Stage 5) | **Sol (`gpt-5.6-sol`), full depth on every record** | Judgment about judgment; no risk-tiering |
| Re-runs of `wrong` records | **Same research model class as the failed run** | Preserve comparability; do not silently escalate model class |

The earlier GPT-5.5-vs-Sol benchmark remains historical evidence, but it no longer defines the runtime mapping. The current decision is Terra fleet + Sol anchors/validation. Dataset derivation, prompt assembly, finalization, build and analysis remain model-free; exact model IDs must be stored in every model-authored artifact.

## 3. Runtime and usage evidence (historical until a v3.1.1 campaign replaces it)

| Unit | Model | Observed tokens | Notes |
|---|---|---|---|
| 1 historical research run (1 code) | GPT-5.5 | ~50–60K | inherited pre-v3.1.1 observation; not the current model assignment |
| 1 golden run (1 code) | Sol | ~50–55K | inherited per-unit burn from the pilot; same shape as fleet run |
| 1 prompt block (1 code) | Sol | ~8–9K | inherited per-unit burn; 13 blocks ≈ 110K per writer agent |
| 1 acceptance review (1 record) | Sol | token split unavailable; **10–12.5 min observed** | two-record canary: 20 URL/path audits, ~8 live-web calls, 20–25 min total |
| Build / datasets / analysis | — | ~0 | Python, seconds |

The repository does not currently contain platform-observed billable usage for Terra/Sol v3.1.1 work. Do not carry forward a price ratio or dollar estimate from the earlier GPT-5.5 campaign. Report exact runtime, input/cached/output/reasoning-token fields and web-call data only when the platform exposes them; otherwise state the limitation.

**Historical pilot observations (83 records):** golden 20 × ~52K Sol + fleet 63 × ~55K GPT-5.5 + prompt design for 63 codes on Sol. These are inherited total-token observations, not a Terra/Sol forecast or reliable billable-cost estimate. The failed first fleet wave (delegation cascades, see §5) produced zero usable records; the v3.1.1 design therefore keeps the strict single-author/no-delegation rule and checkpoints every validated wave rather than inventing a cost margin.

**Phase-6 reporting policy:**
- Fleet model: Terra (`gpt-5.6-terra`); no token or dollar extrapolation until the v3.1.1 canary exposes comparable runtime data.
- Prompt design/review, golden research and full-depth validation: Sol (`gpt-5.6-sol`). Prompt assembly remains plain Python and is not counted as a model stage.
- Validator token extrapolation remains TBD when the platform does not expose input/cached/output/reasoning splits. Full depth is fixed policy, not a cost-tiering option.
- **First validator canary observed:** two records, 20 URL/path occurrences, approximately 8 live-web calls and 20–25 minutes elapsed (10–12.5 minutes per record). Both records were `wrong`; 18/20 citation occurrences failed claim support. The next API-instrumented canary must capture input, cached-input and output/reasoning token splits before a dollar extrapolation is stated.
- **v31c1 limitation:** the five-record canary recorded `gpt-5.6-terra` but exposed neither token splits nor billable web-call counts. It cannot honestly recalibrate costs. Capture what the platform exposes in the v3.1.1 canary and do not fabricate missing billable usage.

## 4. Runner brief — canonical v3.1.1 contract (Stage 3)

The verbatim current runner contract is `pipeline/template/runner_brief_v3_1_1.md`; do not recreate or soften it in an agent message. Parameterize only its assignment paths and exact runtime metadata. The frozen v3.1 brief remains historical and unchanged.

The v3.1.1 flow is deliberately one model stage plus one Python boundary:

1. Terra (`gpt-5.6-terra`) for fleet or Sol (`gpt-5.6-sol`) for golden writes `pipeline/drafts/<naics>/<run-id>.json` against `research_draft_v3_1_1.schema.json`.
2. C1–C4 require fetch-before-cite, a short exact contiguous quote and structured scope for every atomic fact, no URL outside the fact table, and honest `OBSERVED | CALCULATED | ESTIMATE` selection methods.
3. Before finalization, the same runner enumerates and reopens every URL, verifies every fact ID/method/scope, and rechecks every calculation operand. A fact that cannot be reverified is replaced or removed and the input is honestly reclassified.
4. `pipeline/build/finalize_run_v3_1_1.py` assigns final provenance, safely recomputes calculations, injects deterministic datasets/role weights and writes all contributions, scores, S and uplift. The model never authors those fields.
5. The orchestrator independently validates the draft, final record and arithmetic. Agent self-report does not count.

Final provenance and reliability are separate:

- runner method: `OBSERVED | CALCULATED | ESTIMATE`; Python maps it to final `DIRECT | DERIVED | ESTIMATE`
- `evidence_quality`: `HIGH | MED | LOW | NONE`

`NONE` means no referenced evidence facts; an ESTIMATE may still cite background facts, in which case their reliability is stated separately and only the atomic quoted facts are attributed to them.

### v3.1.1 mechanical guarantees (prompt layer cold-reviewed; 63 prompts assembled; freeze checkpoint pending)

Frozen v3.1 records remain valid and are not migrated in place. The v3.1.1 mechanical contract is versioned separately:

1. `evidence_facts[]` is the only place URLs and exact source excerpts may appear. Each fact has a stable ID plus required population, geography, unit, period and industry-mismatch scope fields. Ellipses are rejected because a spliced excerpt is not an exact contiguous quote.
2. A selected input declares a method, not final provenance:
   - `OBSERVED`: the selected value exactly repeats `observed_value` and cites at least one fact.
   - `CALCULATED`: a safe expression using only named, fact-backed numeric operands and `+ - * /`; Python recomputes it exactly. No judgmental mapping is allowed in this branch.
   - `ESTIMATE`: any judgmental bridge; it must state an estimate basis and plausible range.
3. Python maps `OBSERVED → DIRECT`, `CALCULATED → DERIVED`, and `ESTIMATE → ESTIMATE`. The model cannot author that final mapping.
4. `evidence_quality` remains a separate reliability axis (`HIGH | MED | LOW | NONE`). `NONE` means `fact_ids` is empty; any non-empty fact list requires a non-`NONE` quality.
5. `finalize_run_v3_1_1.py`, `build.py` and `review_campaign.py` all fail closed on the v3.1.1 contract. Build rechecks finalized records independently, so changing a method/provenance label after finalization is rejected.

No v3.1.1 research run is authorized until the new prompt/runner/validator layer is cold-reviewed, tested, committed and pushed, and all prompts are deterministically assembled and frozen in a separate wave. The unchanged C1–C4 reopen-every-URL self-audit remains mandatory. The contract does not change thresholds or scoring formulas.

**Orchestration parameters:** at most two codes per single-author runner; no sub-agent delegation; strict repo isolation; one canary after any brief/schema/model/platform change; orchestrator-owned validation sweep on landing; checkpoint commit/push after every validated wave; new series suffix for every campaign. The comparable v3.1.1 canary is `524210 541110 541350 541612 541613`. Proceed only with at least one acceptance and no repeated/systemic method, calculation, quote, scope, evidence-attribution or validator-contract defect.

**Golden runs:** use the same current v3.1.1 brief with Sol (`gpt-5.6-sol`) and the additional ban on reading `pipeline/golden/golden_set.json` or prior golden conclusions. Use new run IDs and never overwrite a reference record ad hoc.

## 5. Incident lessons (encoded, do not relearn)

1. **Delegation cascades destroy runs.** GPT-5.5 fleet agents given 3 codes spontaneously fanned out research sub-agents 3–4 levels deep: ~5–10× token burn, and every assembled record failed schema (invented key names, missing per-input fields). Fix: the no-delegation clause + 2-code briefs + the real-validator self-check loop. On the API (Phase 6) this is structurally impossible — one call, one record.
2. **Agents' self-reports lie; artifacts don't.** A resurrected lane claimed "all three records pass" — 2 of 3 failed schema with 45–50 errors. Only the orchestrator's own validation sweep counts.
3. **Session limits kill agents dead.** Agents that hit a usage limit do not resume when credit is added; their in-flight work is lost. Re-launch fresh, canary first. Checkpoint-commit after every validated wave so an outage can only cost one wave.
4. **Platform outages poison sourcing.** A safety-classifier outage blocked web tools mid-wave; helpers offered memory-based figures (banned). Any record produced in an outage window gets extra validator scrutiny for unresolvable sources.
5. **Schema-vs-reality drift bites at the interface.** The run schema demanded a `derivation` key the dataset layer never emitted (`method`/`source`); the hand-adapted fixture masked it; all 20 golden records failed until the 3.0.2 alignment. Rule: interface schemas must be tested against *real* producer output, not hand-made fixtures.
6. **Relevant pages are not evidence for invented precision.** The initial Sol pass found 0/72 accepted; in a random five-record sample, all pages resolved but 34/35 citation occurrences failed exact claim support. A citation-hardened 541420 s3 rerun using the same fleet model class passed 11/11 audits and all five checks. Root cause: runner attribution behavior and an ambiguous evidence schema, not a need to weaken validation. v3.1 encodes the successful fetch/quote/scope/derive behavior.

## 6. Validator and remaining TBD work

- **Stage 5 validator policy — v3.1 canary completed; validator instrument passed.** The halted v3.0 campaign remains historical evidence. New records use `pipeline/template/validator_brief_v3_1.md`: Sol verifies each atomic cited source fact, then separately checks derivation/proxy reasonableness and estimate honesty. A source need not state a DERIVED selected value; it must state the quoted starting fact. Full depth and exact-run review paths remain unchanged. The build and campaign validator fail closed on unknown template versions, and a v3.1 record can be accepted only by a review whose `review_meta.prompt_version` is exactly `validator-3.1`. In the five-record `v31c1` canary, every review passed the orchestrator's identity/schema/URL/flag checks; Sol supported 18/24 atomic citation occurrences (all citations in four records) while rejecting all five records for separate provenance/derivation defects. This confirms that the validator now distinguishes a supported starting fact from an unsupported selected value.
- **Runner canary result — v3.1 is not fleet-ready.** The five-record `v31c1` canary produced 0 accepted / 5 wrong. The recurring defect was using `DIRECT` or `DERIVED` where the final bridge was judgmental and should have been `ESTIMATE`; one record also used ellipses to splice non-contiguous text while calling it verbatim and omitted geography from citation scope. Before another canary, v3.1.1 must define DERIVED as a fully reproducible non-judgmental transformation, mechanically reject ellipses in quotes, and make population/geography/unit/date/mismatch explicit scope fields. Thresholds and score rules remain frozen.
- **Template 3.1 clarifications — resolved in the new template.** Payer/regulatory clawback belongs in C when it governs retention of savings; terminal class separately governs survival of paid demand. A statutory human-in-loop floor affects terminal value only insofar as it preserves paid demand. W-2/1099 distortions are disclosed as `DATASET_MISMATCH` with sensitivity; deterministic labor share is never silently changed.
- **Phase-6 API batch runner** — TBD. One Terra (`gpt-5.6-terra`) API call per fleet code with web research, schema-validated response and automatic retry with the concrete review reasons attached; Sol (`gpt-5.6-sol`) for golden runs and full-depth validation. Design goals: no delegation possible, resumable, per-sector observed usage tracking.
- **Dataset refresh cadence** — datasets are vintage-stamped; re-run derive.py on new SUSB/QCEW releases; market inputs (multiples, adoption) stale after ~12 months → refresh runs with a new series suffix.

## 7. Quick commands

```bash
python3 pipeline/datasets/derive.py            # regenerate derived inputs (deterministic)
python3 pipeline/build/assemble_prompts.py --check  # verify frozen v3.0 prompts
python3 pipeline/build/assemble_prompts.py --template-version 3.1  # assemble v3.1 prompts only after authorization
python3 pipeline/build/assemble_prompts.py --template-version 3.1.1  # assemble current prompts after prompt-layer checkpoint
python3 pipeline/build/finalize_run_v3_1.py --draft <draft> --dataset <dataset> --output <run>
python3 pipeline/build/finalize_run_v3_1_1.py --draft <draft> --dataset <dataset> --output <run>  # after v3.1.1 prompt authorization
python3 pipeline/build/build.py                # accepted-only build (P10)
python3 pipeline/build/build.py --allow-unreviewed   # pilot/dev build, everything pending-review
python3 pipeline/build/golden_analysis.py      # golden separation criteria (exit 1 on FAIL)
python3 pipeline/build/review_campaign.py generate  # freeze current 63-fleet + 20-golden review manifest
python3 pipeline/build/review_campaign.py validate  # exact-run/schema/source/flag review sweep
python3 pipeline/build/test_v3_1.py            # synthetic v3.1 draft/finalizer tests (no research runs)
python3 pipeline/build/test_v3_1_1.py          # synthetic v3.1.1 mechanics tests (no research runs)
python3 pipeline/build/test_build.py           # v3.0/v3.1 build regression suite
python3 pipeline/build/test_review_campaign.py # review-campaign tests (10 tests)
```
