# v3 Run Playbook

**Status: living document, v3.1.2 Phase 4 completed 2026-07-21** — captures how to re-run the project end-to-end, which model runs what and why, and what can be reported from observed evidence. The bounded campaign published 82 records with visible caveats and excluded one record after the single permitted remediation wave; final validated checkpoint `009d088` is on origin, and frozen v3.0/v3.1/v3.1.1 artifacts and their historical results remain unchanged. Companions: [V3_PRODUCT.md](V3_PRODUCT.md) (what and why), [V3_PLAN.md](V3_PLAN.md) (progress tracker).

---

## 1. The pipeline in one view

```
Stage 0  freeze          templates/thresholds/schemas/golden set   no model
Stage 1  datasets        Census/BLS bulk → derived/<naics>.json    no model      re-run: annually or on new vintage
Stage 2  prompt design   packet/review contract + cold review      Sol           re-run: on template version bump
         prompt assembly blocks → prompts_v3_1_2/<naics>.md        Python only   deterministic
Stage 3  research packet prose + scorecard + source registry       Terra fleet / isolated Sol golden
Stage 4  finalize/render packet → run JSON + Markdown memo         Python only   deterministic
         publish build   reviewed runs → site/stats/report         Python only   deterministic
Stage 5  tiered review   exact packet/run/memo → review JSON       isolated Sol  full depth on every record
```

Everything is re-runnable from the repo alone: prompts, records, thresholds, and scripts are all committed. A fresh session needs only this file, V3_PLAN.md, and the repo.

## 2. Model-choice logic

The rule (P9): **cheap by default, best model only where quality compounds.**

| Work | Model | Why |
|---|---|---|
| Dataset layer, finalization, memo rendering, build, assembly, analysis | none (plain Python) | Deterministic; models banned by design |
| Prompt design/review (Stage 2) | **Sol (`gpt-5.6-sol`)** | One-time contract work; errors propagate into every downstream run |
| Prompt assembly (Stage 2) | **plain Python only** | Deterministic merge and validation; models prohibited |
| Golden-set reference runs | **Sol (`gpt-5.6-sol`)** | 20 codes anchoring the instrument; the quality ceiling everything is benchmarked against |
| Fleet research runs (Stage 3) | **Terra (`gpt-5.6-terra`)** | Current fleet-research decision; exact runtime ID is recorded in every packet/run |
| Tiered publication validator (Stage 5) | **Sol (`gpt-5.6-sol`), full depth on every record** | Judgment about material support and rubric direction; no risk-tiering |
| One permitted remediation of `reject`/`invalid` | **Same research model class as the original run** | Preserve comparability; do not silently escalate model class |

The earlier GPT-5.5-vs-Sol benchmark remains historical evidence, but it no longer defines the runtime mapping. The v3.1.2 decision is Terra fleet + isolated Sol anchors/validation. Dataset derivation, prompt assembly, packet validation, finalization, memo rendering, build and analysis remain model-free; exact model IDs must be stored in every model-authored artifact. Golden runners and validators are isolated from each other, prior conclusions and golden membership.

## 3. Runtime and usage evidence

| Unit | Model | Observed tokens | Notes |
|---|---|---|---|
| 1 historical research run (1 code) | GPT-5.5 | ~50–60K | inherited pre-v3.1.1 observation; not the current model assignment |
| 1 golden run (1 code) | Sol | ~50–55K | inherited per-unit burn from the pilot; same shape as fleet run |
| 1 prompt block (1 code) | Sol | ~8–9K | inherited per-unit burn; 13 blocks ≈ 110K per writer agent |
| 1 acceptance review (1 record) | Sol | token split unavailable; **10–12.5 min observed** | two-record canary: 20 URL/path audits, ~8 live-web calls, 20–25 min total |
| Build / datasets / analysis | — | ~0 | Python, seconds |

The repository does not currently contain platform-observed billable usage sufficient to price a v3.1.2 campaign. Do not carry forward a price ratio or dollar estimate from the earlier GPT-5.5 or v3.1.1 campaigns. Report exact runtime, input/cached/output/reasoning-token fields and web-call data only when the platform exposes them; otherwise state the limitation.

**Completed v3.1.2 Phase-4 campaign:** 83 initial research attempts (63 Terra fleet, 20 isolated Sol golden), 99 independent Sol reviews of exact attempts, and 16 same-class remediation attempts. The final publication set is 82 `publishable_with_caveats` and one excluded `reject` (541310). The platform did not expose a repository-verifiable billable token split or price ledger, so no dollar total is asserted after the fact.

**Historical pilot observations (83 records):** golden 20 × ~52K Sol + fleet 63 × ~55K GPT-5.5 + prompt design for 63 codes on Sol. These are inherited total-token observations, not a Terra/Sol forecast or reliable billable-cost estimate. The failed first fleet wave (delegation cascades, see §5) produced zero usable records; v3.1.2 keeps the strict single-author/no-delegation rule, exact-artifact isolation and checkpointed validated waves rather than inventing a cost margin.

**Phase-6 reporting policy:**
- Fleet model: Terra (`gpt-5.6-terra`); no token or dollar extrapolation until the v3.1.2 canary/campaign exposes comparable runtime data.
- Prompt design/review, golden research and full-depth validation: Sol (`gpt-5.6-sol`). Prompt assembly remains plain Python and is not counted as a model stage.
- Validator token extrapolation remains TBD when the platform does not expose input/cached/output/reasoning splits. Full depth is fixed policy, not a cost-tiering option.
- **First validator canary observed:** two records, 20 URL/path occurrences, approximately 8 live-web calls and 20–25 minutes elapsed (10–12.5 minutes per record). Both records were `wrong`; 18/20 citation occurrences failed claim support. The next API-instrumented canary must capture input, cached-input and output/reasoning token splits before a dollar extrapolation is stated.
- **v31c1 limitation:** the historical five-record canary recorded `gpt-5.6-terra` but exposed neither token splits nor billable web-call counts. It cannot honestly recalibrate costs. Capture what the platform exposes during v3.1.2 and do not fabricate missing billable usage.

## 4. Canonical v3.1.2 text-first contract (Stages 3–5)

The v3.1.1 canary stop remains a valid historical result. The user's 2026-07-21 direction supersedes that stop only for new, versioned v3.1.2 artifacts; it does not authorize mutation or reinterpretation of any earlier packet, draft, run, review, prompt or score.

The verbatim runner contract will live at `pipeline/template/runner_brief_v3_1_2.md`; the validator contract will live at `pipeline/template/validator_brief_v3_1_2.md`. Orchestration messages parameterize only assignment paths and exact runtime metadata. They must not paraphrase, add to or soften either contract.

### Canonical packet and deterministic boundary

Each code has one canonical model-authored packet at `pipeline/packets/<naics>/<run-id>.json`. Both the research memo and score record derive from it, so there is no separate narrative that can drift from the scored inputs. The packet contains:

1. Exact metadata: NAICS code/title, run ID/date, packet/template/prompt version and exact model ID.
2. Seven substantive prose sections: **executive view; how AI changes the work; value capture; adoption timing; consolidation and economics; terminal demand; risks and uncertainty**.
3. A compact machine scorecard. Every selected input records `value`, plausible range, confidence, method (`OBSERVED | CALCULATED | ESTIMATE`), concise rationale, source IDs and any material population/geography/period/proxy caveat. An estimate is valid when its rationale, range and uncertainty are understandable; it does not need a serialized search log or step-by-step bridge form.
4. A compact source registry. Every entry records stable `id`, URL, page title, access date and `supports` text. Every material factual or numeric score-driving claim cites one or more source IDs. Exact quotations are optional. Mandatory per-fact population/geography/unit/period objects from v3.1.1 are not carried forward.

The model authors no deterministic dataset input, SOC identity/weight, contribution, factor score, aggregate S, uplift, gate result or verdict. Plain Python validates the packet, safely recomputes declared calculations, injects the dataset and role objects, computes every downstream field and writes the finalized fleet record to `pipeline/runs/<naics>/<run-id>.json` or the isolated golden record to `pipeline/golden_v3_1_2/<naics>/<run-id>.json`. The same deterministic pass renders `pipeline/memos/<naics>/<run-id>.md`. A fresh finalization must reproduce the record and memo byte-for-byte. Models and humans must never hand-edit either generated artifact.

Fleet research uses exactly Terra (`gpt-5.6-terra`). The 20 golden research runs use exactly Sol (`gpt-5.6-sol`) in isolated contexts that may not read golden membership, earlier golden conclusions, fleet conclusions or another runner's artifact. Every publication review uses exactly Sol (`gpt-5.6-sol`) in a fresh isolated context and binds the exact packet, finalized record and memo identity. Single-author/no-delegation remains mandatory; an orchestration lane may receive at most two codes, but each code is researched and stored independently. Agent self-report never substitutes for the orchestrator's own schema, identity and deterministic-equality checks.

### Review severity and publication treatment

Sol reopens and evaluates every score-driving source, then reviews material support, declared uncertainty, rubric direction, proxy disclosure, capture/terminal separation and double counting. It returns exactly one outcome:

| Outcome | Required finding | Campaign/build treatment |
|---|---|---|
| `publishable` | Mechanics pass; no material research defect | Include |
| `publishable_with_caveats` | Mechanics pass; thesis remains useful despite non-fatal evidence, proxy or uncertainty findings | Include and render every caveat |
| `reject` | A stated material research defect could change a factor, score or thesis | Exclude; eligible for the one remediation attempt |
| `invalid` | Deterministic mechanics or identity contract fails | Exclude; eligible for the one remediation attempt |

`invalid` is narrow and deterministic: wrong identity/model/version, schema failure, mutated deterministic inputs or roles, invalid/non-finite score inputs, unsafe calculation, finalizer mismatch or arithmetic mismatch. These failures can never be downgraded to caveats.

`reject` is also narrow: fabricated or inaccessible score-driving evidence; a material numeric claim unsupported by its cited source; reversed factor semantics; an undisclosed proxy or contradiction likely to change a factor materially; or capture/terminal double counting likely to change the thesis. Every rejection reason must state the affected input/factor or thesis mechanism and why the effect is material. A reason without that materiality statement cannot support `reject`.

Exact punctuation, normalized-quotation differences, page-title variants, conservative `not reported` metadata, incomplete search logs, source age, broad-but-disclosed proxies, non-material scope weakness and incomplete bridge prose are `publishable_with_caveats` findings unless Sol gives the required score-changing materiality explanation. Caveats are data: authored caveats stay on the affected packet inputs and appear in the memo; review caveats stay on the exact review and appear in the generated product and campaign report.

### Bounded Phase-4 execution

1. Implement the versioned packet/run/review schemas, prompt and briefs, finalizer, memo renderer, build routing and campaign tooling. Add synthetic tests for all four outcomes and earlier-artifact/hash preservation. Obtain one cold independent implementation review, close its material findings, run the complete deterministic test suite, assemble exactly 63 prompts using plain Python, prove byte-identical rerendering, checkpoint and push only to `origin`.
2. Run the comparable regression canary `524210 541110 541350 541612 541613`. This is a **mechanics-only execution gate**: 5/5 packets must pass schema and exact identity/model/version checks; fresh finalization must reproduce 5/5 run records and memos; and arithmetic mismatch must be zero. Research findings assign publication tier but a repeated subjective finding does not stop fleet execution.
3. After the mechanics gate passes, count the five valid canary artifacts toward the 63-record Terra fleet and run the remaining 58 once, plus 20 independent Sol golden artifacts. Independently verify packet/run/memo identity and deterministic equality for all 83, then launch one fresh isolated Sol review per exact artifact.
4. Remediate only `reject` or `invalid`. Attach the concrete review findings to the same-model-class runner, write a new packet under a new run ID, re-finalize, rerender and obtain one new isolated Sol review. This is the **only** remediation attempt. Never rerun either publishable tier, silently edit an artifact or start a third attempt.
5. Close the campaign after that one remediation wave. Publish `publishable` and `publishable_with_caveats`; exclude remaining `reject`/`invalid`; list every remaining exclusion and every included caveat in generated output. Golden separation is computed and reported as a diagnostic, never used as an unbounded rerun trigger. There is no 83/83 publication requirement.
6. Report exact attempted/reviewed/remediated/included/excluded counts; counts by publication tier and confidence; source-support and caveat distributions; each unresolved exclusion by code/run/outcome/reason; golden analysis; test/frozen-hash/determinism results; commit IDs; and pushes to `origin`. Report runtime, token splits and web-call counts only when directly exposed by the platform, with missing fields stated rather than estimated.

### 4.1 Historical v3.1.1 contract and stop result

The verbatim historical runner contract is `pipeline/template/runner_brief_v3_1_1.md`; do not recreate or mutate it. The frozen v3.1 brief also remains historical and unchanged.

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

#### v3.1.1 mechanical guarantees (prompt layer frozen 63/63 at `40e9a67`)

Frozen v3.1 records remain valid and are not migrated in place. The v3.1.1 mechanical contract is versioned separately:

1. `evidence_facts[]` is the only place URLs and exact source excerpts may appear. Each fact has a stable ID plus required population, geography, unit, period and industry-mismatch scope fields. Ellipses are rejected because a spliced excerpt is not an exact contiguous quote.
2. A selected input declares a method, not final provenance:
   - `OBSERVED`: the selected value exactly repeats `observed_value` and cites at least one fact.
   - `CALCULATED`: a safe expression using only named, fact-backed numeric operands and `+ - * /`; Python recomputes it exactly. No judgmental mapping is allowed in this branch.
   - `ESTIMATE`: any judgmental bridge; it must state an estimate basis and plausible range.
3. Python maps `OBSERVED → DIRECT`, `CALCULATED → DERIVED`, and `ESTIMATE → ESTIMATE`. The model cannot author that final mapping.
4. `evidence_quality` remains a separate reliability axis (`HIGH | MED | LOW | NONE`). `NONE` means `fact_ids` is empty; any non-empty fact list requires a non-`NONE` quality.
5. `finalize_run_v3_1_1.py`, `build.py` and `review_campaign.py` all fail closed on the v3.1.1 contract. Build rechecks finalized records independently, so changing a method/provenance label after finalization is rejected.

The v3.1.1 prompt layer was cold-reviewed and frozen 63/63 before the comparable canary. The canary failed its predeclared gate, so the v3.1.1 campaign stopped and remains closed. The 2026-07-21 user direction authorizes only the separately versioned v3.1.2 path above; it does not reopen or modify v3.1.1. Thresholds and scoring formulas were not changed.

**Historical orchestration parameters:** at most two codes per single-author runner; no sub-agent delegation; strict repo isolation; one canary after any brief/schema/model/platform change; orchestrator-owned validation sweep on landing; checkpoint commit/push after every validated wave; new series suffix for every campaign. The comparable v3.1.1 canary was `524210 541110 541350 541612 541613`; its gate required at least one acceptance and no repeated/systemic method, calculation, quote, scope, evidence-attribution or validator-contract defect.

**Historical golden rule:** v3.1.1 golden runs used the same brief with Sol (`gpt-5.6-sol`) and the additional ban on reading `pipeline/golden/golden_set.json` or prior golden conclusions. They used new run IDs and never overwrote a reference record ad hoc.

**v3.1.1 canary stop result:** Terra (`gpt-5.6-terra`) produced five mechanically valid records with zero arithmetic mismatches; isolated full-depth Sol (`gpt-5.6-sol`) validation returned 0 accepted / 5 wrong. Atomic support was 36/47 (76.6%), with one record fully supported. Repeated defects included reported geography labeled `not reported`, incomplete historical-analogue/search bridges, and human/ownership/credential mechanisms reused in disallowed or double-counted rubric locations. That failure remains preserved evidence; the user subsequently chose the separately versioned text-first/materiality hypothesis in §4.

## 5. Incident lessons (encoded, do not relearn)

1. **Delegation cascades destroy runs.** GPT-5.5 fleet agents given 3 codes spontaneously fanned out research sub-agents 3–4 levels deep: ~5–10× token burn, and every assembled record failed schema (invented key names, missing per-input fields). Fix: the no-delegation clause + 2-code briefs + the real-validator self-check loop. On the API (Phase 6) this is structurally impossible — one call, one record.
2. **Agents' self-reports lie; artifacts don't.** A resurrected lane claimed "all three records pass" — 2 of 3 failed schema with 45–50 errors. Only the orchestrator's own validation sweep counts.
3. **Session limits kill agents dead.** Agents that hit a usage limit do not resume when credit is added; their in-flight work is lost. Re-launch fresh, canary first. Checkpoint-commit after every validated wave so an outage can only cost one wave.
4. **Platform outages poison sourcing.** A safety-classifier outage blocked web tools mid-wave; helpers offered memory-based figures (banned). Any record produced in an outage window gets extra validator scrutiny for unresolvable sources.
5. **Schema-vs-reality drift bites at the interface.** The run schema demanded a `derivation` key the dataset layer never emitted (`method`/`source`); the hand-adapted fixture masked it; all 20 golden records failed until the 3.0.2 alignment. Rule: interface schemas must be tested against *real* producer output, not hand-made fixtures.
6. **Relevant pages are not evidence for invented precision.** The initial Sol pass found 0/72 accepted; in a random five-record sample, all pages resolved but 34/35 citation occurrences failed exact claim support. A citation-hardened 541420 s3 rerun using the same fleet model class passed 11/11 audits and all five checks, motivating v3.1's stronger attribution mechanics. The later v3.1.1 canary then showed that forensic completeness also created excessive all-record rejection. v3.1.2 keeps material source-support checks while turning non-score-changing metadata/bridge imperfections into visible caveats.

## 6. Validator state and remaining work

- **Stage 5 validator policy — v3.1.2 implemented.** `pipeline/template/validator_brief_v3_1_2.md` and the matching versioned review schema enforce the four outcomes and materiality rules in §4. Sol reviews every record and score-driving source at full depth. Campaign/build tooling fails closed on unknown versions, exact-artifact identity mismatch, current-attempt/build drift and publication-set drift; it includes both publishable tiers, surfaces caveats and excludes the other two tiers.
- **v3.1/v3.1.1 validator history.** The halted v3.0 campaign, successful citation-hardened 541420 rerun, `v31c1` attribution failure and `v311c1` all-wrong canary remain historical evidence. Their frozen briefs, schemas, verdicts and artifacts are not migrated to the new severity contract.
- **Template 3.1 clarifications — resolved in the new template.** Payer/regulatory clawback belongs in C when it governs retention of savings; terminal class separately governs survival of paid demand. A statutory human-in-loop floor affects terminal value only insofar as it preserves paid demand. W-2/1099 distortions are disclosed as `DATASET_MISMATCH` with sensitivity; deterministic labor share is never silently changed.
- **Phase-6 API batch runner** — TBD. One Terra (`gpt-5.6-terra`) API call per fleet code with web research and a schema-validated packet; Sol (`gpt-5.6-sol`) for isolated golden runs and full-depth tiered validation. Only `reject`/`invalid` may trigger one retry with the concrete review reasons attached; remaining failures are reported and excluded. Design goals: no delegation possible, resumable, exact-artifact isolation and per-sector observed usage tracking.
- **Dataset refresh cadence** — datasets are vintage-stamped; re-run derive.py on new SUSB/QCEW releases; market inputs (multiples, adoption) stale after ~12 months → refresh runs with a new series suffix.

## 7. Quick commands

```bash
python3 pipeline/datasets/derive.py            # regenerate derived inputs (deterministic)
python3 pipeline/build/assemble_prompts.py --check  # verify frozen v3.0 prompts
python3 pipeline/build/assemble_prompts.py --template-version 3.1  # assemble v3.1 prompts only after authorization
python3 pipeline/build/assemble_prompts.py --template-version 3.1.1  # verify frozen historical prompts
python3 pipeline/build/assemble_prompts.py --template-version 3.1.2  # assemble canonical text-first prompts
python3 pipeline/build/finalize_run_v3_1.py --draft <draft> --dataset <dataset> --output <run>
python3 pipeline/build/finalize_run_v3_1_1.py --draft <draft> --dataset <dataset> --output <run>  # frozen historical path
python3 pipeline/build/finalize_run_v3_1_2.py --packet <packet> --dataset <dataset> --kind fleet|golden --output <run> --memo <memo>
python3 pipeline/build/build.py                # publishable-only build (both publishable tiers; P10)
python3 pipeline/build/build.py --allow-unreviewed   # pilot/dev build, everything pending-review
python3 pipeline/build/golden_analysis_v3_1_2.py  # current golden diagnostic; no open-ended reruns
python3 pipeline/build/review_campaign_v3_1_2.py generate  # freeze current exact artifact bytes
python3 pipeline/build/review_campaign_v3_1_2.py validate  # validate all attempts/reviews
python3 pipeline/build/review_campaign_v3_1_2.py close     # close bounded wave; build + golden + tests
python3 pipeline/build/review_campaign_v3_1_2.py close --finalize  # only after a clean checkpoint is pushed and HEAD == origin/main
python3 pipeline/build/test_v3_1.py            # synthetic v3.1 draft/finalizer tests (no research runs)
python3 pipeline/build/test_v3_1_1.py          # synthetic v3.1.1 mechanics tests (no research runs)
python3 pipeline/build/test_v3_1_2.py          # packet/finalizer/memo/tier regressions (no research runs)
python3 pipeline/build/test_build.py           # v3.0/v3.1 build regression suite
python3 pipeline/build/test_review_campaign.py # review-campaign tests (10 tests)
```
