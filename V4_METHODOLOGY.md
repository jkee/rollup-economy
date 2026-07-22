# AI Roll-Up Map — v4 Methodology

> **Historical:** superseded v4.0 candidate. The frozen v5 methodology governs the current product.

**Status:** v4.0 methodology freeze candidate, authored 2026-07-21 before any
v4 canary result. This document defines the scoring instrument that replaces
the v3.0 score freeze for new v4 artifacts. It does not mutate or reinterpret
any v3 packet, run, review, dashboard result, or campaign report.

## 1. Decision the instrument makes

For a defined US lower-middle-market target archetype inside a six-digit NAICS
industry, v4 answers two separate questions:

1. **Economic attractiveness:** can a buyer acquire enough operators, retain
   AI-created operating savings, and exit without relying on an implausible
   valuation outcome while the independent operator remains valuable?
2. **Evidence readiness:** is that economic conclusion substantiated,
   provisional, or still unproven?

The output remains a deep-dive priority, not company underwriting. A high score
does not establish target quality, financing capacity, integration ability, or
realized investment returns.

The two questions must never be collapsed. Missing private-market evidence is
not evidence of bad economics; it produces an `UNPROVEN` readiness state and a
wide score interval, not an artificially low factor. Conversely, weak observed
economics are not rescued by abundant citations.

## 2. Unit of analysis: a named target archetype

Six-digit NAICS codes often combine materially different business models. Each
v4 record therefore names exactly one **target archetype**:

- inclusion criteria;
- exclusion criteria;
- why it is the dominant or most investable acquirable archetype;
- estimated share of the deterministic $1–10M EBITDA target band, expressed as
  a base value and numeric low/high range;
- evidence state and caveats for that coverage estimate.

The deterministic NAICS count is never relabeled as though every firm belongs
to the chosen archetype. Python computes:

`n_effective = n_band × target_archetype_coverage`

When the industry is sufficiently homogeneous, coverage may be 1.0. When the
coverage is missing, the provisional point value is 0.5, the sensitivity range
is 0–1, and evidence readiness is `UNPROVEN`.

## 3. Five economic factors

All factor scores are continuous floats on 0–10. Rounding occurs only in the
display. Model-authored packets contain inputs and evidence, never factor
scores, aggregate scores, gates, or verdicts.

### V — value available

V measures the share of industry revenue represented by labor tasks that AI
can remove or materially compress.

`V_raw = labor_share × Σ(role_wage_share × automatable_fraction)`

`V = 10 × min(1, V_raw / 0.25)`

The deterministic labor share and role weights remain Python-owned. Each role
judgment has numeric base/low/high fractions. Adoption, pricing, deal activity,
owner age, and terminal demand may not inflate V. Freeing 25% of revenue remains
the semantic 10 anchor.

### C — value retained

C directly measures the share of gross AI-created operating savings retained
by the acquired operator approximately 24 months after implementation, after
client repricing, contract pass-through, vendor charges, and competitive
response.

`C = 10 × retained_savings_share_24m`

The packet supplies a base value and numeric low/high range from 0–1. Evidence
must address the actual target archetype's pricing and renewal structure. Fixed
fee, recurring, outcome-based, and gain-share arrangements generally support
retention; hourly, cost-plus, audited-overhead, headcount-linked, or rapidly
repriced arrangements generally reduce it.

Moat and distribution control are evidence used to estimate retained savings;
they are no longer multiplied as two separate judgment fractions. This avoids
double-penalizing the same commercial weakness. Whether the independent
operator survives is handled by the operator-survival gate, not counted again
inside C.

If no defensible retained-savings range exists, Python uses the neutral point
C=5 only for provisional ordering, uses 0–10 as the sensitivity range, and
sets readiness to `UNPROVEN`.

### A — adoption timing

A measures time until 50% of the target archetype materially uses AI in the
tasks represented in V.

`A = 10 / (1 + t50_years / 3)`

Semantic anchors:

| Years to 50% | A |
|---:|---:|
| 0 | 10.0 |
| 1 | 7.5 |
| 3 | 5.0 |
| 6 | 3.3 |
| 9 | 2.5 |

`t50_years` is zero when effective adoption is already at least 50%, but the
curve is continuous around zero. Tool use alone is not effective adoption. The
packet records numeric base/low/high years and any population or business-model
proxy. Missing timing evidence uses the neutral three-year point, an open
0–12-year sensitivity range, and contributes to `UNPROVEN` readiness.

### B — buyability

B measures whether enough target-archetype firms are plausibly acquirable,
without treating unknown owner age as proof of weak seller supply.

First compute target density:

`TD = 10 × clamp(log10(max(1, n_effective)) / 4, 0, 1)`

Then apply a seller-supply adjustment:

| Signal | Adjustment |
|---|---:|
| documented excess seller/succession supply | +1 |
| normal or unknown | 0 |
| documented unusually scarce seller supply | −1 |

Finally apply a buyer-competition penalty:

`competition_penalty = min(2, log10(1 + active_consolidators))`

`B = clamp(TD + seller_supply_adjustment − competition_penalty, 0, 10)`

The packet records active consolidators as numeric base/low/high values and
states whether they are demonstrably active for the target archetype. Missing
buyer counts use a neutral provisional count of five, range 0–20, and force
`UNPROVEN`. Owner-age statistics may appear as evidence for the seller signal,
but an unsupported owner-age estimate is never required and never depresses B.

### M — entry-to-exit valuation effect

M measures the effect of entry-to-exit EBITDA multiple change. It is not the
whole return model: V×C already represents the operating-value engine. A flat
multiple is therefore neutral, not fatal.

`spread = exit_multiple / buy_multiple − 1`

M is piecewise-linear between these preregistered anchors:

| Relative spread | Example | M |
|---:|---:|---:|
| −50% | 8x → 4x | 0.0 |
| −25% | 8x → 6x | 2.5 |
| 0% | 8x → 8x | 5.0 |
| +25% | 8x → 10x | 7.0 |
| +50% | 8x → 12x | 8.5 |
| +100% | 8x → 16x | 10.0 |

Values outside the table are clamped to 0–10. Buy and exit inputs each carry
numeric base/low/high values and evidence state. The pessimistic M uses the
high buy and low exit; the optimistic M uses the low buy and high exit.

If no defensible multiple range exists, flat multiples are used as the neutral
point (M=5), the sensitivity range is 0–10, and readiness is `UNPROVEN`. This
does not claim that flat multiples are likely; it prevents absence of private
transaction disclosure from masquerading as measured multiple compression.

## 4. Aggregate score and sensitivity

The base economic score remains a geometric mean:

`S = (V × C × A × B × M)^(1/5)`

The geometric mean preserves the weak-link principle without making flat
multiples a zero. Python also computes a monotonic pessimistic and optimistic
score from every numeric input range:

- V: low/high role fractions;
- C: low/high retained-savings share;
- A: high/low t50 respectively;
- B: low/high archetype coverage, adverse/favorable seller signal, and
  high/low consolidator count;
- M: high-buy/low-exit and low-buy/high-exit respectively.

The displayed result is `S_base [S_low, S_high]`. `CROSS_TIER` is set whenever
the interval crosses an economic-verdict cut. This replaces the v3 ±0.15
borderline heuristic with record-specific sensitivity.

## 5. Operator-survival gate

Terminal demand is assessed at the level of the acquired operator, not merely
the continued existence of the underlying service.

| Class | Meaning | Economic treatment |
|---|---|---|
| `DURABLE` | The target remains a paid, accountable operator at mature AI adoption | no cap |
| `PRESSURED` | The operator survives, but price, volume, or repositioning pressure is material | cap at `strong` |
| `DISINTERMEDIATED` | The service persists but value/control migrates to a platform, vendor, or client | cap at `pass` |
| `MELTING` | Paid demand for the operator's core product is substantially replaced | `kill` |

The class has evidence state, rationale, sources, plausible classes, and
caveats. The base class gates the base verdict; the least and most favorable
plausible classes gate the low and high verdicts respectively. Regulatory responsibility counts only when it preserves a paid role
for the target archetype. The same mechanism may inform C and survival only if
the packet states the separate 24-month retention and mature-demand channels.

## 6. Economic verdicts and hard gates

The absolute cuts retain their preregistered v3 scale meanings:

| Verdict | Rule before survival treatment |
|---|---|
| `hell_yes` | S ≥ 7.0 and every factor ≥ 6.0 |
| `strong` | S ≥ 5.5 |
| `conditional` | S ≥ 4.0 |
| `pass` | S ≥ 3.0 |
| `kill` | S < 3.0 |

Hard structural gates:

- `MELTING` ⇒ `kill`.
- B=0 from deterministic target absence ⇒ `kill`.
- Directly measured C below 1.0 ⇒ `kill`; a missing C instead produces `UNPROVEN`.
- Directly measured M below 1.0 ⇒ `kill`; a missing M instead produces `UNPROVEN`.
- Apply the operator-survival caps after the base verdict.

No confidence label changes the economic verdict. Percentile never defines a
verdict.

## 7. Evidence state and readiness

Every model-authored selected input retains provenance method
`OBSERVED|CALCULATED|ESTIMATE` and evidence quality `HIGH|MED|LOW|NONE`, and
adds one evidence state:

| Evidence state | Meaning |
|---|---|
| `DIRECT` | Target-archetype evidence directly measures or states the input |
| `PROXY` | Adjacent population/size/geography evidence supports a disclosed bridge |
| `ASSUMPTION` | A bounded judgment has no specific empirical support |
| `MISSING` | No defensible value or bounded range was found |

Python derives readiness from every score-driving or gating authored input:
AI-replaceable share, target-archetype coverage, retained savings, t50,
seller-supply signal, active consolidators, buy multiple, exit multiple, and
operator survival.

- `UNPROVEN`: any critical input is `MISSING`, or operator survival itself is
  only an unsupported assumption.
- `PROVISIONAL`: no critical input is missing, but any critical input is an
  `ASSUMPTION`, or at least two critical inputs have LOW/NONE evidence quality.
- `SUBSTANTIATED`: neither condition above applies.

Readiness never numerically rewards citation quantity. It describes how much
work remains before relying on the economic result.

## 8. Decision action

The product displays economic verdict and evidence readiness separately, then
derives an action:

| Economic result | Readiness | Action |
|---|---|---|
| hell_yes/strong | substantiated or provisional | `DEEP_DIVE` |
| hell_yes/strong | unproven | `EVIDENCE_FIRST` |
| conditional | any | `SELECTIVE` |
| pass | any | `DEPRIORITIZE` |
| kill | any | `AVOID` |

The dashboard must never present `100th percentile · conditional` as though
the two signals answer the same question. Absolute economics, evidence
readiness, relative rank, score interval, and action are distinct fields.

## 9. Publication review

Publication acceptance remains separate from economic readiness. An isolated
reviewer returns exactly one of:

- `publishable`;
- `publishable_with_caveats`;
- `reject` for a material research defect likely to change an input range,
  readiness state, survival gate, score interval, or thesis;
- `invalid` for deterministic/schema/identity failure.

The reviewer must verify both ends of score-driving ranges, target-archetype
scope, missing-versus-assumption classification, and the separation of
24-month capture from mature operator survival. A low-readiness but honest
record may be publishable. Unsupported precision or disguising missing data as
a measured low value is material.

## 10. Calibration without outcome fitting

The formulas and anchors above are frozen before the v4 canary. They were
chosen from economic meanings, not desired bucket counts:

- 25% of revenue available is V=10;
- retaining half of savings is C=5;
- three years to majority adoption is A=5;
- 100 target-archetype firms before competition is approximately B=5;
- a flat multiple is M=5 and +25% expansion is M=7.

Synthetic tests must prove every verdict tier is reachable and each factor is
monotonic. Fleet distribution is a diagnostic only. If the canary reveals a
method defect, the freeze is not edited: a v4.1 candidate is authored, all five
canaries are rerun from scratch, and the change is documented. No threshold is
tuned to make a named industry green.

## 11. Five-industry canary gate

The preregistered v4 canary is:

- 541512 Computer Systems Design Services;
- 541511 Custom Computer Programming Services;
- 541214 Payroll Services;
- 238220 Plumbing, Heating, and Air-Conditioning Contractors;
- 541930 Translation and Interpretation Services.

It spans recurring IT operations, project labor, platform squeeze, a durable
physical-service control, and an AI substitution case. The gate requires:

1. 5/5 schema-valid packets and deterministic record/memo reproduction;
2. zero arithmetic, dataset, role, identity, or range-ordering mismatch;
3. 5/5 independent reviews in a publishable tier after at most one bounded
   remediation per rejected/invalid record;
4. no repeated material defect in target-archetype scope, evidence-state
   classification, capture/survival separation, or range support;
5. all score intervals and readiness states rendered;
6. economic monotonicity invariants hold: worsening any one input cannot
   improve its factor or S; `MELTING` cannot outrank its kill gate; and missing
   evidence cannot be presented as measured bad economics;
7. a written human economic-sense review before authorizing the remaining
   Phase-4 campaign. Exact canary verdicts are not preregistered acceptance
   conditions.

The five accepted fleet canaries count toward the v4 Phase-4 fleet. After the
gate, rerun the remaining original Phase-4 fleet membership and the isolated
golden set under v4, with one independent review per exact artifact and one
bounded remediation only for `reject` or `invalid`.

## 12. Versioning and preservation

New v4 artifacts use separate versioned templates, schemas, prompts, finalizer,
campaign manifest/report, build output, and dashboard data. Earlier artifacts
remain byte-unchanged. The deterministic dataset layer may be reused only with
its vintage and derivation unchanged and explicitly recorded.

The final v4 implementation must record exact model IDs, run dates, run IDs,
prompt versions, finalizer version, review prompt version, source access dates,
artifact digests, and campaign membership. No model or human may hand-edit a
finalized score, interval, gate, readiness state, memo, or verdict.
