# AI Roll-Up Map — v4.1 class-neutral five-year research packet

Research **{{NAICS}} — {{TITLE}}** as a US lower-middle-market roll-up screen.
Return exactly one JSON packet conforming to
`pipeline/build/schemas/research_packet_v4_1.schema.json`. Python owns all
frozen inputs, role weights, factor scores, score intervals, readiness, gates,
actions, and verdicts.

## Runtime identity

- model: `{{MODEL_ID}}`
- date: `{{RUN_DATE}}`
- run id: `{{RUN_ID}}`
- template version: `4.1`
- prompt version: `{{PROMPT_VERSION}}` — exactly `v4.1-target-archetype-1`
- attempt: supplied by the campaign manifest

This prompt is class-neutral. Do not seek or infer benchmark membership,
expected ordering, prior conclusions, or another run's artifacts.

## Frozen target archetype

The campaign enumerates mutually exclusive alternatives covering at least 80%
of the estimated band and fixes the largest-count archetype before researching
economics. Do not substitute a
different archetype or select on perceived attractiveness. Recheck the
enumeration, count ranges, residual, objective selection calculation, and
uncertainty without using factor outcomes.

Select the largest base band count; if largest base counts tie, use the
lexicographically smallest alternative ID.

If `selection_uncertainty` is true, keep one selected primary record, force
readiness to `UNPROVEN`, widen coverage and value-basis uncertainty to reflect
the unresolved archetype mix, and make no NAICS-wide claim. Do not split the
NAICS into additional records.

```json
{{TARGET_ARCHETYPE_JSON}}
```

## Frozen value basis

```json
{{VALUE_BASIS_JSON}}
```

Obey `mode` exactly:

- `dataset`: use the pinned labor and role fields only through the disclosed,
  frozen bridge to target-archetype employee and contractor cash cost. Preserve
  every supplied identity and weight exactly. A non-null `bridge` must contain
  population, geography, period, unit, and business-model mappings. If it is
  absent or null, treat the broad dataset basis as an unsupported proxy and force
  readiness `UNPROVEN`.
- `target_specific`: use only the approved employee-and-contractor cash-cost
  share and role cash-cost weights above. Do not add, rename, merge,
  substitute, or reweight them.
- `assumption`: use the pre-frozen bounded employee-and-contractor cash-cost
  share and mutually exclusive role weights exactly as supplied. They are
  explicitly `ASSUMPTION`/`NONE`, make no source claim, mark the value basis
  uncertain, and force readiness to `UNPROVEN`. Estimate removable fractions
  for the fixed roles; do not silently replace them with a broad NAICS proxy.
- `missing`: do not invent cash-cost composition. Return the schema's missing
  value-basis state. Python reports the full possible V domain without a base
  V, base aggregate score, or fabricated base verdict.

Removable fractions remain research judgments with base/low/high values and
must represent cash cost actually removed or avoided at full implementation.
V is gross removable employee-and-contractor cash cost. Task time that cannot
become cash savings is not removable. Implementation,
commercial response, deal activity, and year-five paid demand may not alter V.

## Pinned deterministic dataset

Dataset path: `{{DATASET_PATH}}`  
SHA-256: `{{DATASET_SHA256}}`

```json
{{DATASET_INPUTS_JSON}}
```

Do not modify or re-research non-null normalized dataset values. The normalized
provenance binds the legacy source manifest; do not read the legacy derived file
directly. For a deterministic field whose normalized `value` is null, either
provide a source-backed fallback allowed by the packet schema or return it as
missing. Missing evidence is not measured bad economics.

## Research guidance

### Candidate sources

{{SOURCE_HINTS}}

Hints are leads, not evidence. Confirm existence, reopen every selected URL,
and register only sources actually used.

### Five-year implementation and operational realization

{{IMPLEMENTATION_QUESTIONS}}

Research coherent low/base/high `r1` through `r5` schedules. Each value is the
share of V's gross removable savings realized operationally in that year after
AI/vendor cost, change cost, workflow feasibility, and execution loss, but
before commercial retention. Each schedule must be nondecreasing.

### Commercial retention

{{COMMERCIAL_RETENTION_QUESTIONS}}

Estimate only the share of operationally realized savings retained after
repricing, pass-through, renewal mechanics, and competitive response. Do not
include implementation cost, execution loss, or paid-demand volume.

### Five-year sale availability

{{SALE_AVAILABILITY_QUESTIONS}}

Estimate the numeric share of target-archetype band firms plausibly available
for sale during five years. Unknown owner age is neutral. Buyer crowding does
not reduce target count; there is no consolidator penalty in B. Competition is
reflected in observed all-in entry price.

### Entry and downside valuation robustness

{{VALUATION_ROBUSTNESS_QUESTIONS}}

Research all-in entry EV/normalized EBITDA and a year-five downside exit
multiple on the same quality, scale, and earnings definition. Exclude forecast
synergies and do not assume AI-driven or consolidation-driven expansion.

### Year-five operator-controlled paid demand

{{SURVIVAL_QUESTIONS}}

Estimate numeric low/base/high shares of baseline demand that still purchase
an accountable service from the named operator in year five. Exclude price,
margin, implementation, and vendor cost from this input.

### Additional class-neutral notes

{{SPECIAL_NOTES}}

## Evidence contract

Maintain a stable S1, S2, ... source registry with fetched HTTP(S) URL, title,
access date, and supported claim. Every score-driving selection records method,
evidence state, evidence quality, confidence, source IDs, rationale, caveats,
and a numeric range where applicable.

- `DIRECT` requires target-archetype evidence and an observed or safely
  calculated value.
- `PROXY` requires cited evidence plus an explicit population, geography,
  period, unit, and business-model bridge.
- `ASSUMPTION` supplies a candid bounded judgment with no source claim.
- `MISSING` supplies no invented base or bounded range. It receives no neutral
  point and no base factor, aggregate S, or verdict; Python reports only the
  full possible domain and partial-identification result.

Keep gross removable cost, five-year operational realization, commercial
retention, sale availability, entry/downside pricing, and year-five
operator-controlled paid demand in their separate constructs. Deal evidence
may support sale availability or pricing, never removable cash cost or
implementation.

## Final self-check

Before returning JSON, verify schema, runtime identity, fixed archetype,
value-basis mode and uncertainty, dataset digest, role membership and cash-cost weights,
source-ID closure, ordered ranges, monotone realization schedules, comparable
entry/downside definitions, partial-identification behavior, construct
separation, and narrative/input consistency. Return JSON only.
