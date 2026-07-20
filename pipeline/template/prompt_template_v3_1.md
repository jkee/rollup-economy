# Research one industry for the AI roll-up screen — NAICS {{NAICS}}, {{TITLE}} (US)

**Template version: 3.1** — evidence-contract revision. Formulas and verdict thresholds remain frozen; the only score-boundary clarification is `t50_years=0` when material adoption is already at least 50%.

Work context-free. Do not inspect existing scoring, runs, reviews, golden outcomes, site data or deep-dives. If live web access is unavailable, stop. Never research from memory and never fabricate a URL, quotation or figure.

## What you author

You author evidence and judgment inputs in a `research_draft_v3_1` JSON object. You do **not** author deterministic dataset objects, role wage shares, contributions, factor scores, `S`, `uplift_pp` or a verdict. Plain Python injects and calculates those fields.

Every evidence-bearing input separates:

- `value` — selected value used by the formulas;
- `provenance_type` — `DIRECT`, `DERIVED` or `ESTIMATE`;
- `evidence_quality` — `HIGH`, `MED`, `LOW` or `NONE`;
- `source_fact` — only what fetched citations actually establish;
- `derivation` — the complete bridge from source fact to selected value;
- `plausible_range`;
- `citations[]` — atomic fetched citations with URL, title, exact short quote, access date and scope.

`provenance_type` and `evidence_quality` are independent. An unsourced estimate must use `ESTIMATE` + `NONE` + `citations: []`. A proxy with a strong source is usually `DERIVED` plus an evidence quality reflecting the source and scope fit.

## Frozen research rules

1. PE/M&A activity informs only B and M, never V or A.
2. Multiples are EV/EBITDA after market-rate owner compensation. State unit, target size, source population and every normalization.
3. A zero consolidator count is an absence-of-evidence estimate, not a directly sourced fact. State the searches performed; do not cite a page as proving zero.
4. `current_adoption_pct` means the share of US firms in this NAICS materially using AI in automatable functions. Individual tool use and broad-sector use are different populations and require a visible derivation.
5. `t50_years` means years from today until 50% material firm adoption. If current adoption is already at least 50%, set `t50_years.value` to `0`; otherwise it must be positive.
6. Payer/regulatory repricing belongs in C when it determines who retains cost savings. Terminal class separately answers whether paid end demand survives mature AI; do not count the same clawback twice.
7. A statutory human-in-the-loop boundary affects terminal class only to the extent it preserves paid demand. It does not make automatable tasks non-automatable.
8. If a W-2 dataset labor share is distorted by 1099-heavy labor, use the injected value unchanged, flag `DATASET_MISMATCH`, lower confidence as appropriate and show sensitivity. Do not silently adjust it.
9. Catch-all codes: identify the top three revenue subsegments, score the dominant subsegment, set `heterogeneous=true`, and disclose the boundary.

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

For `role_mix.occupations`, author one role judgment for every supplied `soc`, using the SOC unchanged. The finalizer injects its title and wage share. If listed wage shares sum below one, author one additional `soc: "RESIDUAL"` judgment for the remainder. Never relabel a supplied SOC.

If `labor_share.value` or `n_band.value` is null, provide only that field in `dataset_fallbacks` using the same v3.1 evidence envelope. Otherwise `dataset_fallbacks` must not contain it.

## Inputs to research and declare

- `current_adoption_pct`
- `historical_analogs`
- `owners_60plus_pct`, including structured succession evidence
- `active_consolidators`
- `buy_mult`
- `exit_mult`
- `pricing_structure`
- `within_role_automatable_fraction` for every supplied SOC and the residual
- `pi_dist`
- `pi_moat`
- `t50_years`

All judgment values are bounded and carry a rationale and plausible range. `t50_years` must appear in `top_uncertain_inputs`.

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

Answer:

1. Uplift consistency, while acknowledging Python supplies the final `uplift_pp`.
2. Terminal value: `DURABLE`, `PRESSURED` or `MELTING`, separating operator cost reduction from product replacement.
3. No-proxy confirmation that V/A exclude deal evidence.
4. Pricing-model deflation and its explicit mapping into `pi_dist`/`pi_moat`.

## Output

Write one JSON object conforming exactly to `pipeline/build/schemas/research_draft_v3_1.schema.json` with:

```json
{
  "naics": "{{NAICS}}",
  "title": "{{TITLE}}",
  "run_meta": {
    "model_id": "{{MODEL_ID}}",
    "run_date": "{{RUN_DATE}}",
    "run_id": "{{RUN_ID}}",
    "template_version": "3.1",
    "prompt_version": "{{PROMPT_VERSION}}"
  },
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
      "provenance_type": "ESTIMATE",
      "evidence_quality": "NONE",
      "source_fact": "",
      "derivation": "",
      "citations": []
    },
    "pi_dist": {
      "value": 0.0,
      "rationale": "",
      "provenance_type": "ESTIMATE",
      "evidence_quality": "NONE",
      "source_fact": "",
      "derivation": "",
      "plausible_range": "",
      "citations": []
    },
    "pi_moat": {},
    "t50_years": {},
    "current_adoption_pct": {},
    "historical_analogs": {},
    "owners_60plus_pct": {
      "succession_shortage_documented": {
        "value": false,
        "evidence": ""
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
  "confidence_overall": "LOW",
  "heterogeneous": false,
  "top_uncertain_inputs": [
    {"input": "t50_years", "plausible_range": "", "score_impact": ""}
  ],
  "reviewer_note": ""
}
```

The abbreviated `{}` entries must be filled with their complete schema-defined fields. URLs are allowed only in `citations[].url`.
