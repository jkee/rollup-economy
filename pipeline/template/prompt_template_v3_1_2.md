# AI Value Migration Map — v3.1.2 text-first research packet

Research **{{NAICS}} — {{TITLE}}** as a US lower-middle-market industry. Your
single output is one JSON packet conforming exactly to
`pipeline/build/schemas/research_packet_v3_1_2.schema.json`. The packet is the
canonical source for both the prose memo and score record. Do not author
dataset values, role weights, role contributions, factor scores, S, uplift or
verdict; plain Python owns them.

## Runtime identity (copy exactly)

- model: `{{MODEL_ID}}`
- date: `{{RUN_DATE}}`
- run id: `{{RUN_ID}}`
- template version: `3.1.2`
- prompt version: `{{PROMPT_VERSION}}` (the orchestrator must replace this with
  exact frozen value `v3.1.2-text-first-1`)
- initial attempt: `1` (a remediation brief explicitly changes this to `2`
  and supplies `remediates_run_id`)

## Product question

Would buying a $1–10M EBITDA operator in this industry allow an owner to retain
AI-created operating value while the market still has durable paid demand?
Write a candid investment-research memo, not an audit transcript. Clear prose,
explicit judgment and useful uncertainty matter more than forensic metadata.

## Frozen score meanings — do not reinterpret

- **V:** labor-cost value available from replaceable task share. Judge tasks by
  the supplied SOC roles. Do not use adoption speed, deal evidence, ownership
  age, licensing or terminal demand to inflate task replaceability.
- **C:** fraction of operating savings retained by the operator: `pi_dist`
  (distribution/pass-through) × `pi_moat` (competitive moat). Pricing
  deflation belongs here. Do not count a human/regulatory floor here merely
  because it preserves terminal demand.
- **A:** years until 50% effective adoption. If current adoption is already at
  least 50%, `t50_years` is exactly `0`; otherwise it is positive. Do not use
  consolidation or owner age as adoption evidence.
- **B:** buyability from target count, owners over 60, documented succession
  shortage and active consolidators. Do not recycle these mechanisms into V/A.
- **M:** buy and exit EBITDA multiples. Do not use multiple expansion to
  justify C or terminal value.
- **Terminal demand:** whether paid demand for the operator survives AI. This
  is distinct from capture. Choose `DURABLE`, `PRESSURED` or `MELTING`.

One mechanism may be discussed in multiple sections, but it may not do two
score jobs unless you state the two distinct causal channels. Disclose any
possible double count in the affected input caveats.

## Supplied deterministic inputs — do not re-research or modify

{{DATASET_INPUTS_JSON}}

Use every supplied `role_mix.occupations[].soc` exactly once in
`scorecard.ai_replaceable_share.role_judgments`. Keep SOC identities and wage
shares untouched. Add `RESIDUAL` exactly when the listed wage shares sum to
less than 0.9995; its fraction is a separate bounded judgment.

## Industry-specific research guidance

### Role hints

{{ROLE_HINTS}}

### Source hints

{{SOURCE_HINTS}}

### Capture questions

{{CAPTURE_QUESTIONS}}

### Terminal-value question

{{TERMINAL_VALUE_QUESTION}}

### Special notes

{{SPECIAL_NOTES}}

## Compact evidence contract

Maintain one compact `sources` registry. Each source has a stable `S1`, `S2`,
... ID, fetched HTTP(S) URL, page/report title, access date and a plain-language
statement of what it supports. An exact quote is optional. Cite source IDs on
every score-driving material factual or numeric input.

For each selected input:

- `OBSERVED` means the selected value is directly stated by its source.
- `CALCULATED` means safe arithmetic using only named numeric operands tied to
  source IDs; only `+ - * /`, numeric constants and parentheses are allowed.
- `ESTIMATE` means any judgmental bridge, proxy mapping or bounded opinion.

Every selection carries `evidence_quality` (`HIGH|MED|LOW|NONE`), confidence
(`HIGH|MED|LOW`), source IDs, rationale, plausible range and `caveats[]`.
`NONE` requires empty source IDs; any cited source requires non-`NONE` quality.
An estimate may cite useful background facts. It is valid when the rationale,
range and uncertainty are understandable; do not serialize search logs or a
step-by-step bridge form.

Disclose material population, geography, period, size-band, unit, industry or
proxy mismatches as concise caveats on the affected input. Page-title variants,
quote punctuation and incomplete forensic metadata are not reasons to invent
precision or hide uncertainty.

## Required narrative

Write seven substantive sections, each at least a short paragraph:

1. `executive_view`
2. `how_ai_changes_work`
3. `value_capture`
4. `adoption_timing`
5. `consolidation_economics`
6. `terminal_demand`
7. `risks_and_uncertainty`

Use `[S#]` source references in prose where helpful. The numeric scorecard and
narrative must express the same thesis.

## Output shape

Return JSON only. Use this exact top-level shape and the exact schema names:

```json
{
  "naics": "{{NAICS}}",
  "title": "{{TITLE}}",
  "run_meta": {
    "model_id": "{{MODEL_ID}}",
    "run_date": "{{RUN_DATE}}",
    "run_id": "{{RUN_ID}}",
    "template_version": "3.1.2",
    "prompt_version": "{{PROMPT_VERSION}}",
    "attempt": 1
  },
  "narrative": {
    "executive_view": "...",
    "how_ai_changes_work": "...",
    "value_capture": "...",
    "adoption_timing": "...",
    "consolidation_economics": "...",
    "terminal_demand": "...",
    "risks_and_uncertainty": "..."
  },
  "sources": [
    {
      "id": "S1",
      "url": "https://...",
      "title": "...",
      "access_date": "{{RUN_DATE}}",
      "what_it_supports": "...",
      "exact_quote": "optional"
    }
  ],
  "dataset_fallbacks": {},
  "scorecard": {
    "ai_replaceable_share": {
      "method": "ESTIMATE",
      "evidence_quality": "MED",
      "confidence": "MED",
      "source_ids": ["S1"],
      "rationale": "...",
      "plausible_range": "...",
      "caveats": [],
      "role_judgments": [
        {
          "soc": "copy supplied SOC or RESIDUAL",
          "within_role_automatable_fraction": 0.0,
          "rationale": "...",
          "plausible_range": "..."
        }
      ]
    },
    "pi_dist": {
      "value": 0.0,
      "method": "ESTIMATE",
      "evidence_quality": "MED",
      "confidence": "MED",
      "source_ids": ["S1"],
      "rationale": "...",
      "plausible_range": "...",
      "caveats": []
    },
    "pi_moat": {"value": 0.0, "method": "ESTIMATE", "evidence_quality": "MED", "confidence": "MED", "source_ids": ["S1"], "rationale": "...", "plausible_range": "...", "caveats": []},
    "t50_years": {"value": 1.0, "method": "ESTIMATE", "evidence_quality": "MED", "confidence": "MED", "source_ids": ["S1"], "rationale": "...", "plausible_range": "...", "caveats": []},
    "current_adoption_pct": {"value": 0.0, "method": "ESTIMATE", "evidence_quality": "MED", "confidence": "MED", "source_ids": ["S1"], "rationale": "...", "plausible_range": "...", "caveats": []},
    "historical_analogs": {"value": "...", "method": "ESTIMATE", "evidence_quality": "MED", "confidence": "MED", "source_ids": ["S1"], "rationale": "...", "plausible_range": "...", "caveats": []},
    "owners_60plus_pct": {
      "selection": {"value": 0.0, "method": "ESTIMATE", "evidence_quality": "MED", "confidence": "MED", "source_ids": ["S1"], "rationale": "...", "plausible_range": "...", "caveats": []},
      "succession_shortage_documented": {"value": false, "method": "ESTIMATE", "evidence_quality": "MED", "confidence": "MED", "source_ids": ["S1"], "rationale": "...", "plausible_range": "true/false", "caveats": []}
    },
    "active_consolidators": {"value": 0, "method": "ESTIMATE", "evidence_quality": "MED", "confidence": "MED", "source_ids": ["S1"], "rationale": "...", "plausible_range": "...", "caveats": []},
    "buy_mult": {"value": 1.0, "method": "ESTIMATE", "evidence_quality": "MED", "confidence": "MED", "source_ids": ["S1"], "rationale": "...", "plausible_range": "...", "caveats": []},
    "exit_mult": {"value": 1.0, "method": "ESTIMATE", "evidence_quality": "MED", "confidence": "MED", "source_ids": ["S1"], "rationale": "...", "plausible_range": "...", "caveats": []},
    "pricing_structure": {"value": "...", "method": "ESTIMATE", "evidence_quality": "MED", "confidence": "MED", "source_ids": ["S1"], "rationale": "...", "plausible_range": "...", "caveats": []}
  },
  "cross_checks": {
    "uplift_vs_A_consistent": "...",
    "terminal_value": {"class": "DURABLE", "justification": "..."},
    "no_proxy_confirmed": "...",
    "pricing_model_deflation": "..."
  },
  "disclosures": {
    "dataset_mismatch": {"applies": false, "description": "", "sensitivity": []},
    "market_boundary": {"applies": false, "subsegments": [], "dominant_subsegment": "", "selection_basis": ""}
  },
  "confidence_overall": "MED",
  "heterogeneous": false,
  "top_uncertain_inputs": [
    {"input": "t50_years", "plausible_range": "...", "score_impact": "..."}
  ],
  "reviewer_note": ""
}
```

Before returning, enumerate every source ID and scorecard reference; reopen each
score-driving URL; remove inaccessible or unsupported material claims; validate
the JSON against the exact v3.1.2 packet schema; verify role membership and t50
boundary; and make every proxy, scope mismatch and possible double count candid.
