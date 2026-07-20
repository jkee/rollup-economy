# Research one industry for the AI roll-up screen — NAICS {{NAICS}}, {{TITLE}} (US)

**Template version: 3.1.1** — atomic-fact and explicit-method evidence contract. The frozen formulas, gates and verdict thresholds are unchanged. The assigned runtime model ID is `{{MODEL_ID}}`; copy that exact ID into `run_meta.model_id`.

Work context-free. Do not inspect existing scoring, drafts, runs, reviews, golden outcomes, generated site data or deep-dives. If live web access is unavailable, stop. Never research from memory and never fabricate a URL, quote, figure or scope.

## What you author

Write one JSON object conforming exactly to `pipeline/build/schemas/research_draft_v3_1_1.schema.json`. You author reusable atomic `evidence_facts` and selected research/judgment inputs. You do **not** author final provenance, deterministic dataset values, role weights, role contributions, factor scores, `S`, uplift or a verdict. Plain Python owns those fields.

Every selected input has a `method`:

- `OBSERVED` — `value` repeats a value stated by a cited fact exactly. Include the identical `observed_value`. No interpretation, proxy, normalization or judgmental bridge is permitted.
- `CALCULATED` — `value` is fully reproducible arithmetic over named numeric operands, every operand is backed by a cited fact, and the expression uses only numeric constants, parentheses and `+ - * /`. Include every operand's `name`, `value` and `fact_id`. Python recomputes the result. Any judgmental mapping makes this method invalid.
- `ESTIMATE` — required whenever any bridge from facts to the selected value is judgmental, including proxy choice, population mapping, normalization assumptions or an opinion. Its structured `estimate_basis` must enumerate every starting fact ID, every scope mismatch, each ordered proxy/normalization/population step, and the explicit judgmental step reaching the selected value. A cited background fact does not turn an estimate into `OBSERVED` or `CALCULATED`.

Python maps `OBSERVED → DIRECT`, `CALCULATED → DERIVED`, and `ESTIMATE → ESTIMATE`. Never author `provenance_type` in the draft. `evidence_quality` is a separate reliability axis: `HIGH | MED | LOW | NONE`. Empty `fact_ids` requires `NONE`; non-empty `fact_ids` requires non-`NONE` quality.

## Citation discipline — C1 to C4

1. **C1 — Fetch before cite.** Open and inspect the exact page before creating a fact. Search snippets, titles and memory are not evidence.
2. **C2 — Quote what you saw.** Each fact contains one short exact contiguous quote or table figure. Compact (`...`), spaced (`. . .`) and Unicode (`…`) ellipses are forbidden. Never splice separated passages.
3. **C3 — Attribute only what the URL establishes.** Never use a URL as support for a claim it does not establish. If no fetched source supports a background fact, omit the fact and label the selected value honestly as an estimate.
4. **C4 — Reopen and verify.** Before submission, enumerate and reopen every URL and verify its quote, attribution and all structured scope fields against the live page.

`evidence_facts[]` is the only place URLs may appear. Use stable unique IDs `F1`, `F2`, ... and reuse a fact by ID instead of duplicating its URL/quote. Every scope must state `population`, `geography`, `unit`, `period` and `industry_mismatch`. If a source omits any scope element, write exactly `not reported` for that field; never infer it silently.

## Frozen research rules

1. PE/M&A activity informs only B and M, never V or A.
2. Multiples are EV/EBITDA after market-rate owner compensation. State unit, target size, source population and every normalization. A normalization or market mapping that requires judgment is `ESTIMATE`.
3. A zero consolidator count is an absence-of-evidence estimate, not an observation. State the searches performed; do not cite a topical page as proving zero.
4. `current_adoption_pct` means the share of US firms in this NAICS materially using AI in automatable functions. Tool use, worker use and broad-sector use are different populations. Any judgmental mapping to the target population is `ESTIMATE`.
5. `t50_years` means years from today until 50% material firm adoption. If current adoption is already at least 50%, set it to `0`; otherwise it must be positive. Forecasting or analog-based bridging is normally `ESTIMATE`, even when supported by observed adoption facts.
6. Payer/regulatory repricing belongs in C when it determines who retains cost savings. Terminal class separately answers whether paid end demand survives mature AI; do not count the same clawback twice.
7. A statutory human-in-the-loop boundary affects terminal class only to the extent it preserves paid demand. It does not make automatable tasks non-automatable.
8. If a W-2 dataset labor share is distorted by 1099-heavy labor, use the injected value unchanged, flag `dataset_mismatch`, lower confidence as appropriate and show sensitivity. Do not silently adjust it.
9. Catch-all codes: identify at least the top three revenue subsegments, score the dominant subsegment, set `heterogeneous=true`, and complete the structured market-boundary disclosure.
10. `succession_shortage_documented` changes B. It is a full boolean selection under the same method/fact contract. `true` requires `OBSERVED`, at least one fact that directly documents a shortage, and exact live verification. A search-based `false` is normally `ESTIMATE` + `NONE`, with the searches and absence judgment fully disclosed in `estimate_basis`.

## Industry-specific guidance — hints, not facts

**Likely role structure:**
{{ROLE_HINTS}}

**Suggested sources:**
{{SOURCE_HINTS}}

**Capture questions:**
{{CAPTURE_QUESTIONS}}

**Terminal-value question:**
{{TERMINAL_VALUE_QUESTION}}

**Known traps:**
{{SPECIAL_NOTES}}

## Deterministic context — read-only

The finalizer injects these exact objects. Use them to form judgments, but do not copy them into the draft.

{{DATASET_INPUTS_JSON}}

For `role_mix.occupations`, author one role judgment for every supplied `soc`, unchanged. The finalizer injects titles and wage shares. If listed wage shares sum below one, add exactly one `soc: "RESIDUAL"` judgment for the remainder. Role fractions are judgments: the finalized role aggregate is always an estimate. Never relabel or reinterpret a supplied SOC.

If `labor_share.value` or `n_band.value` is null, provide only that field in `dataset_fallbacks` under the same method contract. Otherwise the fallback is forbidden.

## Inputs to research and declare

- `current_adoption_pct`
- `historical_analogs`
- `owners_60plus_pct`, including structured succession evidence
- `active_consolidators`
- `buy_mult`
- `exit_mult`
- `pricing_structure`
- `within_role_automatable_fraction` for every supplied SOC and any required residual
- `pi_dist`
- `pi_moat`
- `t50_years`

Every selected input carries a rationale and plausible range. `t50_years` must appear in `top_uncertain_inputs`. Method and evidence reliability must be assessed independently.

## Frozen formulas — Python calculates them

- `V_raw = labor_share × ai_replaceable_share`
- `V = 10 × min(1, V_raw / 0.25)`
- `C = 10 × pi_dist × pi_moat`
- `A = 10` when `t50_years=0`, otherwise `min(10, 10 / t50_years)`
- `TD = clamp(log10(n_band) / 4, 0, 1)`
- `OW = clamp((owners_60plus_pct − 0.10) / 0.35, 0.1, 0.9)`; add 0.1 for documented succession shortage, cap at 1
- `CFD = min(0.9, log10(1 + active_consolidators) / 2)`
- `B = 10 × sqrt(TD × OW) / (1 + 0.3 × CFD)`
- `M = clamp(4 × (exit_mult − buy_mult) / buy_mult, 0, 10)`
- `S = (V × C × A × B × M)^(1/5)`

## Mandatory cross-check narratives

Answer all four candidly:

1. Uplift consistency, while acknowledging Python supplies final `uplift_pp`.
2. Terminal value: `DURABLE`, `PRESSURED` or `MELTING`, separating operator cost reduction from product replacement.
3. No-proxy confirmation that V/A exclude deal evidence.
4. Pricing-model deflation and its explicit mapping into `pi_dist`/`pi_moat`.

## Final self-audit — required before submission

1. Enumerate every `evidence_facts[].url`, reopen each URL and verify the exact contiguous quote, title, attribution and every scope field.
2. Enumerate every fact ID and confirm it is unique and referenced accurately.
3. For every selected input, verify its `fact_ids`, method, evidence quality, rationale and range.
4. For every `OBSERVED` selection, verify the cited fact states the selected value exactly.
5. For every `CALCULATED` selection, verify every operand against its fact, confirm the expression uses all operands, recompute it, and confirm there is no judgmental bridge.
6. For every judgmental bridge, require `ESTIMATE` even when background facts are cited.

## Output shape

Fill every abbreviated selection with the exact fields required by the schema. The example shows method-specific shapes; do not include fields belonging to another method branch.

```json
{
  "naics": "{{NAICS}}",
  "title": "{{TITLE}}",
  "run_meta": {
    "model_id": "{{MODEL_ID}}",
    "run_date": "{{RUN_DATE}}",
    "run_id": "{{RUN_ID}}",
    "template_version": "3.1.1",
    "prompt_version": "{{PROMPT_VERSION}}"
  },
  "evidence_facts": [
    {
      "id": "F1",
      "url": "https://example.org/source",
      "title": "Exact source title",
      "quote": "One short exact contiguous excerpt or table figure",
      "access_date": "{{RUN_DATE}}",
      "scope": {
        "population": "not reported",
        "geography": "not reported",
        "unit": "not reported",
        "period": "not reported",
        "industry_mismatch": "not reported"
      }
    }
  ],
  "dataset_fallbacks": {},
  "inputs": {
    "ai_replaceable_share": {
      "role_judgments": [
        {
          "soc": "00-0000",
          "within_role_automatable_fraction": 0.0,
          "rationale": "",
          "plausible_range": ""
        }
      ],
      "evidence_quality": "NONE",
      "fact_ids": [],
      "estimate_basis": {
        "starting_fact_ids": [],
        "scope_mismatches": ["none; no source fact is used"],
        "bridge_steps": ["State the factual/search starting point and each bridge step."],
        "judgment_step": "State the explicit judgment used to select the value."
      }
    },
    "pi_dist": {
      "value": 0.0,
      "method": "ESTIMATE",
      "evidence_quality": "NONE",
      "fact_ids": [],
      "rationale": "",
      "plausible_range": "",
      "estimate_basis": {
        "starting_fact_ids": [],
        "scope_mismatches": ["none; no source fact is used"],
        "bridge_steps": ["State the factual/search starting point and each bridge step."],
        "judgment_step": "State the explicit judgment used to select the value."
      }
    },
    "pi_moat": {},
    "t50_years": {},
    "current_adoption_pct": {
      "value": 0.0,
      "method": "OBSERVED",
      "evidence_quality": "HIGH",
      "fact_ids": ["F1"],
      "rationale": "",
      "plausible_range": "",
      "observed_value": 0.0
    },
    "historical_analogs": {},
    "owners_60plus_pct": {
      "selection": {},
      "succession_shortage_documented": {
        "value": false,
        "method": "ESTIMATE",
        "evidence_quality": "NONE",
        "fact_ids": [],
        "rationale": "",
        "plausible_range": "false unless directly documented otherwise",
        "estimate_basis": {
          "starting_fact_ids": [],
          "scope_mismatches": ["none; no source fact is used"],
          "bridge_steps": ["List the searches performed and what they did not establish."],
          "judgment_step": "Treat the absence of located documentation as an estimate, not proof of absence."
        }
      }
    },
    "active_consolidators": {},
    "buy_mult": {},
    "exit_mult": {},
    "pricing_structure": {}
  },
  "cross_checks": {
    "uplift_vs_A_consistent": "",
    "terminal_value": {"class": "DURABLE", "justification": ""},
    "no_proxy_confirmed": "",
    "pricing_model_deflation": ""
  },
  "disclosures": {
    "dataset_mismatch": {"applies": false, "description": "", "sensitivity": []},
    "market_boundary": {
      "applies": false,
      "subsegments": [],
      "dominant_subsegment": "",
      "selection_basis": ""
    }
  },
  "confidence_overall": "LOW",
  "heterogeneous": false,
  "top_uncertain_inputs": [
    {"input": "t50_years", "plausible_range": "", "score_impact": ""}
  ],
  "reviewer_note": ""
}
```

URLs are permitted only in `evidence_facts[].url`. Output only the completed JSON object.
