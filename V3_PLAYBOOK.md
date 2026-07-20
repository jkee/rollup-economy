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
| 1 acceptance review (1 record) | Sol | ~25–35K **(estimate)** | not yet measured; source-verification web fetches may dominate |
| Build / datasets / analysis | — | ~0 | Python, seconds |

Current standard API pricing is the same for both selected models: **Sol = GPT-5.5 = $5/M input + $30/M output**. GPT-5.5 Batch/Flex is half the standard rate. Therefore the inherited **best ≈ 5× cheap per-token premise is false**: the relevant price ratio is 1× at standard rates, or about 2× when fleet work uses GPT-5.5 Batch/Flex. Total-token comparisons are still insufficient because input, cached input, output/reasoning tokens and web calls have different cost effects.

**Pilot actuals (83 records):** golden 20 × ~52K Sol + fleet 63 × ~55K GPT-5.5 + prompt-gen 63 codes on Sol + meta/assembler/datasets agents. These are inherited total-token observations, not a reliable OpenAI cost estimate. **Waste line:** the failed first fleet wave (delegation cascades, see §5) burned roughly a full fleet's worth of GPT-5.5-equivalent tokens for zero usable records — prevented in the s2 design, but budget a 10–20% incident margin anyway.

**Phase-6 extrapolation (1,012 codes, order-of-magnitude):**
- Fleet: 1,012 × ~55K ≈ 55M GPT-5.5 total tokens
- Prompt-gen: 1,012 × ~9K ≈ 9M Sol total tokens
- Validator: 1,012 × ~30K ≈ 30M Sol total tokens; full depth is fixed policy, not a cost-tiering option
- The first two-record validator canary must capture input tokens, cached-input tokens, output/reasoning tokens, web-call count and elapsed time per record. Replace the blended estimates and extrapolate Phase 6 from that measured mix before the next wave.

## 4. Runner brief — the canonical contract (Stage 3)

Proven 63/63. Use verbatim, parameterized per pair of codes. Key clauses earned by incident (§5) — do not soften them.

```
You are a research runner for an industry-scoring pipeline. You will score 2 industries,
one at a time, yourself.

HARD RULES:
1. Do NOT spawn, launch, or delegate to any sub-agent, at any level, for any reason.
   Execute all research and writing yourself, sequentially.
2. ISOLATION: within the repo you may read ONLY: your two prompt files, and (for
   validation only) pipeline/build/build.py + pipeline/build/schemas/run_record.schema.json.
   No other repo file — no golden/, no six_data.json, no deep-dives, no other runs.
   Knowledge sources: the prompt file + live web research. Never fabricate sources or
   figures; if a source is unreachable, use another or mark ESTIMATE with basis.
3. Do NOT git commit.

For each code, in order:
a. Read pipeline/prompts/<naics>.md and execute it exactly. The Step 4 JSON structure is
   the mandatory output contract — use its EXACT key names (t50_years not t50,
   breakdown_by_role inside ai_replaceable_share, succession_shortage_documented nested
   inside owners_60plus_pct). Follow any catch-all/heterogeneity and research-gap
   instructions in the prompt.
b. Write the record to pipeline/runs/<naics>/<date>_<model>_<series>.json with run_meta
   exactly: {model_id, run_date, run_id: "<series>-<naics>", template_version, prompt_version}.
c. VALIDATE with the build's own validator and fix every error before moving on
   (repeat until OK):
   python3 -c "
   import importlib.util, json
   spec = importlib.util.spec_from_file_location('build','pipeline/build/build.py')
   b = importlib.util.module_from_spec(spec); spec.loader.exec_module(b)
   schema = json.load(open('pipeline/build/schemas/run_record.schema.json'))
   rec = json.load(open('pipeline/runs/<naics>/<file>.json'))
   errs = b.schema_errors(rec, schema, schema)
   comp, aerrs, _ = b.recompute(rec)
   print('OK' if not errs and not aerrs else ('SCHEMA: '+str(errs[:5])+' ARITH: '+str(aerrs[:3])))"

Report back: per code one line — V/C/A/B/M/S, terminal class, confidence, biggest
uncertainty — plus confirmation the validation printed OK for both.
```

**Orchestration parameters (proven):** 2 codes per agent; waves of 7–8 agents; run one **canary agent first** after any brief change or capacity incident; validate every record on landing with the orchestrator's own sweep (never trust an agent's "it passes"); `git commit + push` after each validated wave; new run series suffix (s3, s4…) per re-run campaign so the build's latest-run selection picks the newest.

**Golden runs:** same brief, Sol model, output to `pipeline/golden/<naics>.json`, run_id `golden-<series>-<naics>`, and the isolation clause additionally bans reading `golden_set.json` (it contains expected outcomes — contamination).

## 5. Incident lessons (encoded, do not relearn)

1. **Delegation cascades destroy runs.** GPT-5.5 fleet agents given 3 codes spontaneously fanned out research sub-agents 3–4 levels deep: ~5–10× token burn, and every assembled record failed schema (invented key names, missing per-input fields). Fix: the no-delegation clause + 2-code briefs + the real-validator self-check loop. On the API (Phase 6) this is structurally impossible — one call, one record.
2. **Agents' self-reports lie; artifacts don't.** A resurrected lane claimed "all three records pass" — 2 of 3 failed schema with 45–50 errors. Only the orchestrator's own validation sweep counts.
3. **Session limits kill agents dead.** Agents that hit a usage limit do not resume when credit is added; their in-flight work is lost. Re-launch fresh, canary first. Checkpoint-commit after every validated wave so an outage can only cost one wave.
4. **Platform outages poison sourcing.** A safety-classifier outage blocked web tools mid-wave; helpers offered memory-based figures (banned). Any record produced in an outage window gets extra validator scrutiny for unresolvable sources.
5. **Schema-vs-reality drift bites at the interface.** The run schema demanded a `derivation` key the dataset layer never emitted (`method`/`source`); the hand-adapted fixture masked it; all 20 golden records failed until the 3.0.2 alignment. Rule: interface schemas must be tested against *real* producer output, not hand-made fixtures.

## 6. Validator and remaining TBD work

- **Stage 5 validator policy — resolved 2026-07-20.** Run Sol at full depth on all 83 pilot records, with no risk-tiering: 63 fleet records plus 20 separate golden reference records. Start with a two-record canary (fleet 541330 and fleet 541611), then use batches of five records per validator; keep fleet and golden runs for the same NAICS in different batches. The canonical, parameterized contract is `pipeline/template/validator_brief_v3.md`. Reviews are exact-run artifacts at `pipeline/review/<naics>/<run-id>.json`; fleet and golden versions of the same NAICS therefore remain distinct. The Phase-2 production bootstrap `pipeline/review/541330.json` was removed before the canary; only exact-run Sol reviews can satisfy P10. The formal golden gate requires both `review_campaign.py validate` and `golden_analysis.py` to pass.
- **Template 3.1 clarification candidates** (from pilot divergences — batch them, version-bump, re-run affected codes only after freeze discipline): where payer/regulatory clawback belongs (C input vs terminal class); terminal-class boundary guidance when a statutory human-in-the-loop floor exists (translation, court reporting); explicit rule for 1099-heavy industries (labor_share captures W-2 only — affects V comparability).
- **Phase-6 API batch runner** — TBD. One API call per code (GPT-5.5 + web search tool), schema-validated response, automatic retry with error attached, then build + full-depth Sol validator. Design goals: no delegation possible, resumable, per-sector cost tracking.
- **Dataset refresh cadence** — datasets are vintage-stamped; re-run derive.py on new SUSB/QCEW releases; market inputs (multiples, adoption) stale after ~12 months → refresh runs with a new series suffix.

## 7. Quick commands

```bash
python3 pipeline/datasets/derive.py            # regenerate derived inputs (deterministic)
python3 pipeline/build/assemble_prompts.py     # blocks + datasets + template → prompts (--check to verify)
python3 pipeline/build/build.py                # accepted-only build (P10)
python3 pipeline/build/build.py --allow-unreviewed   # pilot/dev build, everything pending-review
python3 pipeline/build/golden_analysis.py      # golden separation criteria (exit 1 on FAIL)
python3 pipeline/build/review_campaign.py generate  # freeze current 63-fleet + 20-golden review manifest
python3 pipeline/build/review_campaign.py validate  # exact-run/schema/source/flag review sweep
python3 pipeline/build/test_build.py           # regression suite (18 tests)
python3 pipeline/build/test_review_campaign.py # review-campaign tests (9 tests)
```
