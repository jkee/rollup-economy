# AI Roll-Up Map — v4.0 target-archetype research packet

Research **{{NAICS}} — {{TITLE}}** as a US lower-middle-market roll-up screen.
Return exactly one JSON packet conforming to
`pipeline/build/schemas/research_packet_v4.schema.json`. The packet is the only
model-authored source for the finalized score record and memo. Python owns all
dataset injection, role weights, factor scores, ranges, readiness, gates,
actions, and verdicts.

## Runtime identity

- model: `{{MODEL_ID}}`
- date: `{{RUN_DATE}}`
- run id: `{{RUN_ID}}`
- template version: `4.0`
- prompt version: `{{PROMPT_VERSION}}` — exactly `v4.0-target-archetype-1`
- initial attempt: `1`; remediation alone uses `2` plus `remediates_run_id`

## Decision question

For one clearly defined target archetype within this NAICS code, would buying
a $1–10M EBITDA operator allow an owner to retain AI-created operating savings,
assemble enough targets, and exit without requiring an implausible valuation
outcome while the independent operator remains valuable?

Economic attractiveness and evidence readiness are separate. Never turn
missing private-market evidence into a low economic input. If no defensible
value or bounded numeric range exists, set `evidence_state: "MISSING"`,
`method: "ESTIMATE"`, `evidence_quality: "NONE"`, empty `source_ids`, and null
numeric value/range. Python applies the preregistered neutral point and wide
sensitivity range while marking the conclusion `UNPROVEN`.

## Frozen v4 meanings

- **Target archetype:** name one acquirable business model, with inclusions,
  exclusions, selection basis, and its estimated share of supplied `n_band`.
  Do not count the full NAICS target pool when evidence concerns only a subset.
- **V:** task-level AI replaceability using every supplied SOC exactly once.
  Give numeric base/low/high fractions. Deal activity, adoption, pricing, and
  terminal demand cannot affect role fractions.
- **C:** `retained_savings_share_24m`, the share of gross AI-created operating
  savings retained about 24 months after implementation, after repricing,
  pass-through, vendor charges, and competition. Give numeric 0–1 base/range.
  Do not multiply separate moat and distribution opinions.
- **A:** `t50_years`, time until 50% of the target archetype materially uses AI
  in V's tasks. Tool use is not automatically effective adoption. If current
  effective adoption is at least 50%, t50 is zero.
- **B:** Python combines archetype-adjusted target count, seller supply, and
  active consolidator competition. Unknown owner age is neutral. Use seller
  signal `EXCESS|NORMAL|UNKNOWN|SCARCE`; count only buyers demonstrably active
  or plausibly active for the named archetype.
- **M:** buy and exit EBITDA multiples with numeric base/low/high. Flat
  multiples are neutral because operating value is already represented by V×C.
  Do not invent a spread when no defensible range exists.
- **Operator survival:** `DURABLE|PRESSURED|DISINTERMEDIATED|MELTING` at mature
  AI adoption, evaluated for the acquired operator rather than the continued
  existence of the underlying service. Platform survival is not local-operator
  survival.

Read `V4_METHODOLOGY.md` for exact deterministic formulas, anchors, defaults,
readiness rules, and gates. Do not reinterpret them.

## Supplied deterministic inputs — do not modify

{{DATASET_INPUTS_JSON}}

Use every supplied `role_mix.occupations[].soc` exactly once. Add `RESIDUAL`
exactly when listed wage shares sum below 0.9995. Preserve identities and wage
shares.

## Industry-specific guidance

### Role hints

{{ROLE_HINTS}}

### Source hints

{{SOURCE_HINTS}}

### Capture questions

{{CAPTURE_QUESTIONS}}

### Existing terminal question — reinterpret at operator level

{{TERMINAL_VALUE_QUESTION}}

### Special notes

{{SPECIAL_NOTES}}

## Evidence contract

Maintain one source registry with stable S1, S2, ... IDs, fetched HTTP(S) URL,
title, access date, and what the source supports. Reopen every score-driving
source before returning.

Every selection records:

- provenance method: `OBSERVED|CALCULATED|ESTIMATE`;
- evidence state: `DIRECT|PROXY|ASSUMPTION|MISSING`;
- evidence quality: `HIGH|MED|LOW|NONE`;
- confidence: `HIGH|MED|LOW`;
- source IDs, rationale, and caveats;
- numeric base plus `{low, high}` range where applicable.

`DIRECT` requires a target-archetype source and `OBSERVED` or safely
`CALCULATED` value. `PROXY` requires cited evidence and a disclosed bridge.
`ASSUMPTION` and `MISSING` require ESTIMATE, NONE quality, and no source IDs.
An assumption still supplies a candid bounded value/range; missing supplies
null numeric value/range. Unsupported precision or misclassifying missing data
as measured low is a material defect.

## Required narrative

Write nine substantive sections matching the schema: executive view, target
archetype, how AI changes work, value capture, adoption timing, buyability,
valuation, operator survival, and risks/uncertainty. Use [S#] references where
helpful. Numeric inputs and prose must express the same thesis.

## Required scorecard shape

Use exactly these scorecard keys:

```json
{
  "ai_replaceable_share": {
    "method": "ESTIMATE", "evidence_state": "PROXY",
    "evidence_quality": "MED", "confidence": "MED",
    "source_ids": ["S1"], "rationale": "...", "caveats": [],
    "role_judgments": [
      {"soc": "...", "within_role_automatable_fraction": 0.0,
       "range": {"low": 0.0, "high": 0.0}, "rationale": "..."}
    ]
  },
  "target_archetype": {
    "name": "...", "inclusion_criteria": ["..."],
    "exclusion_criteria": ["..."], "selection_basis": "...",
    "coverage": {"value": 0.0, "range": {"low": 0.0, "high": 0.0},
      "method": "ESTIMATE", "evidence_state": "PROXY",
      "evidence_quality": "MED", "confidence": "MED",
      "source_ids": ["S1"], "rationale": "...", "caveats": []}
  },
  "retained_savings_share_24m": {"value": 0.0, "range": {"low": 0.0, "high": 0.0}, "method": "ESTIMATE", "evidence_state": "PROXY", "evidence_quality": "MED", "confidence": "MED", "source_ids": ["S1"], "rationale": "...", "caveats": []},
  "t50_years": {"value": 0.0, "range": {"low": 0.0, "high": 0.0}, "method": "ESTIMATE", "evidence_state": "PROXY", "evidence_quality": "MED", "confidence": "MED", "source_ids": ["S1"], "rationale": "...", "caveats": []},
  "current_adoption_pct": {"value": 0.0, "range": {"low": 0.0, "high": 0.0}, "method": "ESTIMATE", "evidence_state": "PROXY", "evidence_quality": "MED", "confidence": "MED", "source_ids": ["S1"], "rationale": "...", "caveats": []},
  "historical_analogs": {"value": "...", "method": "ESTIMATE", "evidence_state": "PROXY", "evidence_quality": "MED", "confidence": "MED", "source_ids": ["S1"], "rationale": "...", "caveats": []},
  "seller_supply_signal": {"value": "NORMAL", "plausible_values": ["NORMAL"], "method": "ESTIMATE", "evidence_state": "PROXY", "evidence_quality": "MED", "confidence": "MED", "source_ids": ["S1"], "rationale": "...", "caveats": []},
  "active_consolidators": {"value": 0, "range": {"low": 0, "high": 0}, "method": "ESTIMATE", "evidence_state": "PROXY", "evidence_quality": "MED", "confidence": "MED", "source_ids": ["S1"], "rationale": "...", "caveats": []},
  "buy_mult": {"value": 1.0, "range": {"low": 1.0, "high": 1.0}, "method": "ESTIMATE", "evidence_state": "PROXY", "evidence_quality": "MED", "confidence": "MED", "source_ids": ["S1"], "rationale": "...", "caveats": []},
  "exit_mult": {"value": 1.0, "range": {"low": 1.0, "high": 1.0}, "method": "ESTIMATE", "evidence_state": "PROXY", "evidence_quality": "MED", "confidence": "MED", "source_ids": ["S1"], "rationale": "...", "caveats": []},
  "pricing_structure": {"value": "...", "method": "ESTIMATE", "evidence_state": "PROXY", "evidence_quality": "MED", "confidence": "MED", "source_ids": ["S1"], "rationale": "...", "caveats": []},
  "operator_survival": {"value": "DURABLE", "plausible_values": ["DURABLE", "PRESSURED"], "method": "ESTIMATE", "evidence_state": "PROXY", "evidence_quality": "MED", "confidence": "MED", "source_ids": ["S1"], "rationale": "...", "caveats": []}
}
```

Return JSON only. Validate against the exact schema; enumerate and recheck all
source IDs; verify role membership, numeric range ordering, t50/adoption
boundary, target-archetype scope, and capture/operator-survival separation.
