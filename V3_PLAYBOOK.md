# v3 Run Playbook

**Status: living document, incomplete** — captures how to re-run the project end-to-end, which model runs what and why, and what it costs. Written after the sector-54 pilot (2026-07-20); the Stage-5 policy is resolved and the Phase-6 API runner remains TBD. Companions: [V3_PRODUCT.md](V3_PRODUCT.md) (what and why), [V3_PLAN.md](V3_PLAN.md) (progress tracker).

---

## 1. The pipeline in one view

```
Stage 0  freeze          templates/thresholds/schemas/golden set   no model
Stage 1  datasets        Census/BLS bulk → derived/<naics>.json    no model      re-run: annually or on new vintage
Stage 2  prompt gen      blocks/<naics>.json → prompts/<naics>.md  Sol           re-run: on template version bump
Stage 3  research runs   prompts → runs/<naics>/<runid>.json       GPT-5.5       re-run: staleness (~12mo) or 'wrong'
Stage 4  build           runs → six_data_v3.json + stats + flags   no model      re-run: on any input change (seconds)
Stage 5  acceptance      records → review/<naics>/<run-id>.json    Sol           full depth on every record
```

Everything is re-runnable from the repo alone: prompts, records, thresholds, and scripts are all committed. A fresh session needs only this file, V3_PLAN.md, and the repo.

## 2. Model-choice logic

The rule (P9): **cheap by default, best model only where quality compounds.**

| Work | Model | Why |
|---|---|---|
| Dataset layer, build, assembly, analysis | none (Python) | Deterministic; models banned by design |
| Per-code prompt blocks (Stage 2) | **Sol** | One-time per code; errors here propagate into every downstream run; needs real industry judgment |
| Golden-set reference runs | **Sol** | 20 codes anchoring the instrument; the quality ceiling everything is benchmarked against |
| Fleet research runs (Stage 3) | **GPT-5.5** | Proven adequate in the 63-record pilot; use Batch/Flex when the workflow supports it |
| Acceptance validator (Stage 5) | **Sol, full depth on every record** | Judgment about judgment; catches plausible-but-wrong; no risk-tiering |
| Re-runs of `wrong` records | GPT-5.5 (escalate to Sol on second failure) | Same as fleet |

Observed GPT-5.5-vs-Sol behavior on the 20 shared benchmark codes: **structure and mechanisms agree** (same moats, same capture traps, same melter mechanisms found independently); divergence concentrates in the declared-uncertain inputs (t50, buy/exit multiples), GPT-5.5 systematically more conservative on adoption timing. Two terminal-class boundary disagreements in 20 (translation, court reporting). Conclusion: GPT-5.5 fleet + Sol anchors is a sound trade; do not downgrade prompt-gen, golden runs or acceptance validation.

## 3. Cost assumptions (observed in the pilot, blended in/out tokens per unit)

| Unit | Model | Observed tokens | Notes |
|---|---|---|---|
| 1 research run (1 code) | GPT-5.5 | ~50–60K | inherited per-unit burn from the pilot; single-author s2 runs, including web research + self-validation |
| 1 golden run (1 code) | Sol | ~50–55K | inherited per-unit burn from the pilot; same shape as fleet run |
| 1 prompt block (1 code) | Sol | ~8–9K | inherited per-unit burn; 13 blocks ≈ 110K per writer agent |
| 1 acceptance review (1 record) | Sol | token split unavailable; **10–12.5 min observed** | two-record canary: 20 URL/path audits, ~8 live-web calls, 20–25 min total |
| Build / datasets / analysis | — | ~0 | Python, seconds |

Current standard API pricing is the same for both selected models: **Sol = GPT-5.5 = $5/M input + $30/M output**. GPT-5.5 Batch/Flex is half the standard rate. Therefore the inherited **best ≈ 5× cheap per-token premise is false**: the relevant price ratio is 1× at standard rates, or about 2× when fleet work uses GPT-5.5 Batch/Flex. Total-token comparisons are still insufficient because input, cached input, output/reasoning tokens and web calls have different cost effects.

**Pilot actuals (83 records):** golden 20 × ~52K Sol + fleet 63 × ~55K GPT-5.5 + prompt-gen 63 codes on Sol + meta/assembler/datasets agents. These are inherited total-token observations, not a reliable OpenAI cost estimate. **Waste line:** the failed first fleet wave (delegation cascades, see §5) burned roughly a full fleet's worth of GPT-5.5-equivalent tokens for zero usable records — prevented in the s2 design, but budget a 10–20% incident margin anyway.

**Phase-6 extrapolation (1,012 codes, order-of-magnitude):**
- Fleet: 1,012 × ~55K ≈ 55M GPT-5.5 total tokens
- Prompt-gen: 1,012 × ~9K ≈ 9M Sol total tokens
- Validator token extrapolation remains TBD because the sub-agent interface did not expose input/cached/output/reasoning token splits. Full depth is fixed policy, not a cost-tiering option.
- **First validator canary observed:** two records, 20 URL/path occurrences, approximately 8 live-web calls and 20–25 minutes elapsed (10–12.5 minutes per record). Both records were `wrong`; 18/20 citation occurrences failed claim support. The next API-instrumented canary must capture input, cached-input and output/reasoning token splits before a dollar extrapolation is stated.

## 4. Runner brief — canonical v3.1 contract (Stage 3)

The verbatim runner contract is `pipeline/template/runner_brief_v3_1.md`; do not recreate or soften it in an agent message. Parameterize only its assignment paths and runtime metadata.

The v3.1 flow is deliberately one model stage plus one Python boundary:

1. GPT-5.5 (Sol for golden runs) writes `pipeline/drafts/<naics>/<run-id>.json` against `research_draft_v3_1.schema.json`.
2. C1–C4 require fetch-before-cite, a short exact quote and scope for every citation, no URL for an unsourced estimate, and a complete visible bridge for every proxy/derivation.
3. Before finalization, the same runner lists and reopens every URL in its draft. A citation that cannot be reverified is replaced or removed and the input is honestly reclassified.
4. `pipeline/build/finalize_run_v3_1.py` injects deterministic datasets/role weights and writes all contributions, scores, S and uplift to the final run. The model never authors those fields.
5. The orchestrator independently validates the draft, final record and arithmetic. Agent self-report does not count.

Provenance and reliability are separate:

- `provenance_type`: `DIRECT | DERIVED | ESTIMATE`
- `evidence_quality`: `HIGH | MED | LOW | NONE`

The legacy `quality: ESTIMATE` combination is not used in v3.1. `NONE` means no citation; an ESTIMATE may still cite background facts, in which case the citation quality is stated separately and only the quoted background fact is attributed to it.

**Orchestration parameters:** two codes per single-author runner; no sub-agent delegation; strict repo isolation; one canary after any brief/schema/model/platform change; own sweep on landing; checkpoint commit/push after every validated wave; new series suffix for every campaign. No v3.1 research campaign is authorized until the contract is reviewed and frozen.

**Golden runs:** same v3.1 brief with Sol and the additional ban on reading `pipeline/golden/golden_set.json`. The exact golden storage migration is frozen before its canary; do not overwrite a reference record ad hoc.

## 5. Incident lessons (encoded, do not relearn)

1. **Delegation cascades destroy runs.** GPT-5.5 fleet agents given 3 codes spontaneously fanned out research sub-agents 3–4 levels deep: ~5–10× token burn, and every assembled record failed schema (invented key names, missing per-input fields). Fix: the no-delegation clause + 2-code briefs + the real-validator self-check loop. On the API (Phase 6) this is structurally impossible — one call, one record.
2. **Agents' self-reports lie; artifacts don't.** A resurrected lane claimed "all three records pass" — 2 of 3 failed schema with 45–50 errors. Only the orchestrator's own validation sweep counts.
3. **Session limits kill agents dead.** Agents that hit a usage limit do not resume when credit is added; their in-flight work is lost. Re-launch fresh, canary first. Checkpoint-commit after every validated wave so an outage can only cost one wave.
4. **Platform outages poison sourcing.** A safety-classifier outage blocked web tools mid-wave; helpers offered memory-based figures (banned). Any record produced in an outage window gets extra validator scrutiny for unresolvable sources.
5. **Schema-vs-reality drift bites at the interface.** The run schema demanded a `derivation` key the dataset layer never emitted (`method`/`source`); the hand-adapted fixture masked it; all 20 golden records failed until the 3.0.2 alignment. Rule: interface schemas must be tested against *real* producer output, not hand-made fixtures.
6. **Relevant pages are not evidence for invented precision.** The initial Sol pass found 0/72 accepted; in a random five-record sample, all pages resolved but 34/35 citation occurrences failed exact claim support. A citation-hardened 541420 s3 rerun using the same fleet model class passed 11/11 audits and all five checks. Root cause: runner attribution behavior and an ambiguous evidence schema, not a need to weaken validation. v3.1 encodes the successful fetch/quote/scope/derive behavior.

## 6. Validator and remaining TBD work

- **Stage 5 validator policy — v3.1 pending canary.** The halted v3.0 campaign remains historical evidence. New records use `pipeline/template/validator_brief_v3_1.md`: Sol verifies each atomic cited source fact, then separately checks derivation/proxy reasonableness and estimate honesty. A source need not state a DERIVED selected value; it must state the quoted starting fact. Full depth and exact-run review paths remain unchanged. The build and campaign validator fail closed on unknown template versions, and a v3.1 record can be accepted only by a review whose `review_meta.prompt_version` is exactly `validator-3.1`.
- **Template 3.1 clarifications — resolved in the new template.** Payer/regulatory clawback belongs in C when it governs retention of savings; terminal class separately governs survival of paid demand. A statutory human-in-loop floor affects terminal value only insofar as it preserves paid demand. W-2/1099 distortions are disclosed as `DATASET_MISMATCH` with sensitivity; deterministic labor share is never silently changed.
- **Phase-6 API batch runner** — TBD. One API call per code (GPT-5.5 + web search tool), schema-validated response, automatic retry with error attached, then build + full-depth Sol validator. Design goals: no delegation possible, resumable, per-sector cost tracking.
- **Dataset refresh cadence** — datasets are vintage-stamped; re-run derive.py on new SUSB/QCEW releases; market inputs (multiples, adoption) stale after ~12 months → refresh runs with a new series suffix.

## 7. Quick commands

```bash
python3 pipeline/datasets/derive.py            # regenerate derived inputs (deterministic)
python3 pipeline/build/assemble_prompts.py --check  # verify frozen v3.0 prompts
python3 pipeline/build/assemble_prompts.py --template-version 3.1  # assemble v3.1 prompts only after authorization
python3 pipeline/build/finalize_run_v3_1.py --draft <draft> --dataset <dataset> --output <run>
python3 pipeline/build/build.py                # accepted-only build (P10)
python3 pipeline/build/build.py --allow-unreviewed   # pilot/dev build, everything pending-review
python3 pipeline/build/golden_analysis.py      # golden separation criteria (exit 1 on FAIL)
python3 pipeline/build/review_campaign.py generate  # freeze current 63-fleet + 20-golden review manifest
python3 pipeline/build/review_campaign.py validate  # exact-run/schema/source/flag review sweep
python3 pipeline/build/test_v3_1.py            # synthetic v3.1 draft/finalizer tests (no research runs)
python3 pipeline/build/test_build.py           # v3.0/v3.1 build regression suite
python3 pipeline/build/test_review_campaign.py # review-campaign tests (9 tests)
```
