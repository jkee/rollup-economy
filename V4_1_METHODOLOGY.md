# AI Roll-Up Map — v4.1 Methodology

> **Historical:** superseded v4.1 specification. The frozen v5 methodology governs the current product.

**Status:** frozen methodology specification, authored 2026-07-21 after the
v4.0 instrument and its five first-attempt outputs had been viewed. The
economic constants in this document may not be changed in place. The
instrument is not operationally authorized until the version manifest and
digests in section 14 have been committed before any v4.1 research run.

v4.1 replaces v4.0 for all new work. It does not mutate or reinterpret any
v3 or v4.0 packet, finalized record, memo, review, or campaign artifact. The
reason v4.0 was rejected is recorded in `V4_0_REJECTION.md`.

## 1. Decision and horizon

For one preselected US lower-middle-market target archetype inside a six-digit
NAICS industry, v4.1 is a five-year, unlevered screening instrument. It asks:

1. how much cash labor and contractor cost AI can remove;
2. how much of that operational opportunity can be realized and how quickly;
3. how much realized savings the operator can retain commercially;
4. whether there is enough five-year acquisition inventory; and
5. whether entry and downside exit valuation are robust without multiple
   expansion.

It separately reports evidence readiness. It is a deep-dive priority, not a
company valuation, financing model, integration plan, or return forecast.

Economic values, gates, and verdicts never depend on evidence labels. Evidence
labels affect readiness and action only.

## 2. Unit of analysis and archetype selection

Phase 4 retains exactly one primary record per NAICS. Archetype selection
occurs before researching AI economics, pricing capture, implementation, or
valuation.

1. Enumerate mutually exclusive target archetypes that together cover at least
   80% of the estimated `$1–10M EBITDA` band; retain the remainder as a named
   residual. Assign each archetype a stable ID before economic research.
2. Estimate each archetype's band count with base, low, and high values.
3. Select the archetype with the largest base band count. Break an exact base-
   count tie by the lexicographically smallest stable ID. “Most investable” is
   forbidden as a selection rule.
4. If the two largest base counts differ by less than 10%, or their supported
   ranges overlap, keep the objectively selected largest-base archetype as the
   single primary record and set `selection_uncertainty: true`. Record every
   alternative archetype, stable ID, base/range count, and reason it remains
   plausible. Force overall readiness to `UNPROVEN`. Widen the selected
   archetype's coverage range and V value-basis ranges to encompass the
   supported reclassification and weighting consequences of every overlapping
   alternative; if those consequences cannot be bounded, the affected input is
   `MISSING`.
5. A record describes its named archetype only. It is never presented as the
   score of the whole NAICS industry.

The record must give inclusion criteria, exclusion criteria, the enumeration,
selection calculation, coverage base/range, and sources.

This fixed one-record rule prevents uncertain archetype boundaries from
dynamically changing campaign membership. The largest-base rule and frozen
tie-break prevent choosing the alternative with the most favorable economic
outcome; the uncertainty flag and widened ranges preserve the cost of the
unresolved selection instead of hiding it.

V uses target-archetype cash-cost weights. A broader NAICS role mix is not a
valid deterministic substitute. It may be used only as a disclosed proxy when
the bridge supports target-specific reweighting. If the bridge is invalid or
cannot support bounded target-specific weights, V is `MISSING`.

## 3. Five economic factors

Every factor is a continuous float on 0–10. Model-authored packets contain
inputs, ranges, scenarios, evidence, and rationale, never factor scores,
aggregate scores, gates, actions, or verdicts.

### V — gross removable cash cost

V measures steady-state cash labor and contractor cost that can actually be
removed, or avoided through documented growth, at full implementation. Task
time that cannot become cash savings is not removable.

Let:

- `labor_contractor_cash_cost_share` be target-archetype employee and
  contractor cash cost divided by revenue;
- `role_cash_cost_weight_i` be role i's share of that cost, with weights summing
  to 1; and
- `removable_fraction_i` be the fraction of role i's cash cost removable at
  full implementation, before AI/vendor/change cost and commercial repricing.

`g = labor_contractor_cash_cost_share ×
     Σ(role_cash_cost_weight_i × removable_fraction_i)`

`V = 10 × min(1, g / 0.25)`

Semantic anchors:

| Gross removable cash cost / revenue | V |
|---:|---:|
| 0% | 0 |
| 5% | 2 |
| 12.5% | 5 |
| 20% | 8 |
| 25% or more | 10 |

Adoption, pricing, market diffusion, deal activity, and terminal demand may not
alter V.

### I — five-year operational realization

I measures acquirer-controlled implementation and timing. It never rewards
fast market-wide diffusion.

The packet supplies `r1` through `r5`, where `rt` is the fraction of V's gross
removable cash savings realized operationally during year t after AI/vendor
cost, change cost, workflow feasibility, and execution loss, but before the
commercial capture represented by C.

`0 ≤ r1 ≤ r2 ≤ r3 ≤ r4 ≤ r5 ≤ 1`

With the frozen unlevered screen discount rate `d = 10%`:

`I = 10 × [Σ(t=1..5) rt / (1+d)^t] / [Σ(t=1..5) 1 / (1+d)^t]`

Semantic anchors:

| Realization schedule | I |
|---|---:|
| 100/100/100/100/100% | 10.0 |
| 0/100/100/100/100% | 7.601841083684134 |
| 0/0/100/100/100% | 5.4216966143060725 |
| 0/0/0/100/100% | 3.4397470966896524 |
| 20/40/60/80/100% | 5.620251920525462 |
| 0/0/0/0/0% | 0.0 |

Sentinel comparisons use absolute tolerance `1e-9` against these frozen
values. Display rounds I to two decimals only after validation.

### C — commercial capture

C measures the share of operationally realized savings retained by the
operator after client repricing, contractual pass-through, renewal mechanics,
and competitive commercial response.

`C = 10 × commercial_retention_share`

Semantic anchors:

| Commercial retention | C |
|---:|---:|
| 0% | 0 |
| 20% | 2 |
| 50% | 5 |
| 80% | 8 |
| 100% | 10 |

AI/vendor cost, change cost, workforce realizability, and implementation
timing belong only in I. Terminal paid-demand volume belongs only in the
survival gate. They may be discussed in C but not scored there.

### B — five-year acquisition runway

B measures the number of target-archetype firms plausibly available for sale
during the five-year screen.

`N5 = n_band × archetype_coverage × five_year_sale_availability_share`

`B = 10 × clamp(log10(1 + N5) / log10(501), 0, 1)`

Semantic anchors:

| Five-year available targets | B |
|---:|---:|
| 0 | 0.00 |
| 10 | 3.86 |
| approximately 21 | approximately 5.00 |
| 100 | 7.42 |
| 500 or more | 10.00 |

Sale availability is a numeric base/low/high share from 0–1. Unknown owner age
does not imply scarce supply. Active consolidators do not enter B: buyer
competition is reflected in the observed entry price used by P.

### P — valuation robustness

P rewards affordable entry and downside resilience without rewarding multiple
expansion.

Let `buy_mult` be entry EV/normalized EBITDA for the named target archetype.

`entry_score = clamp(14 − buy_mult, 0, 10)`

Entry anchors are 4x=10, 6x=8, 8x=6, 10x=4, 12x=2, and 14x=0.

Let `downside_exit_mult` be the year-five downside EV/normalized EBITDA
multiple for the same stated quality and scale definition. It excludes
forecast synergies and does not assume AI-driven or roll-up multiple expansion.

`resilience_score =
    clamp(20 × (downside_exit_mult / buy_mult − 0.5), 0, 10)`

Resilience anchors are 50% multiple retention=0, 75%=5, and flat or
expanding=10. Expansion receives no score above 10.

`P = min(entry_score, resilience_score)`

Current or historical transaction evidence may directly measure a comparable
multiple. A future downside exit conclusion remains a forecast and therefore
cannot be `DIRECT` without a separately valid longitudinal design.

## 4. Aggregate score, tiers, and structural floors

`S = (V × I × C × B × P)^(1/5)`

Verdicts are assigned in descending order:

| Verdict | Aggregate cut | Minimum every factor |
|---|---:|---:|
| `hell_yes` | S ≥ 7.5 | ≥ 6 |
| `strong` | S ≥ 6.0 | ≥ 4 |
| `conditional` | S ≥ 4.5 | ≥ 2 |
| `pass` | S ≥ 3.0 | ≥ 1 |
| `kill` | otherwise | — |

The floors are economic and apply regardless of evidence state. A high factor
cannot compensate for a structurally failed factor. `N5=0` therefore produces
B=0 and `kill` without a separate provenance-dependent gate.

## 5. Year-five operator-survival gate

The packet supplies `operator_controlled_paid_demand_share_y5`, the year-five
share of baseline demand that still purchases an accountable service from the
named operator archetype. It measures paid-demand volume/control only. Price,
margin, implementation, and vendor cost are excluded.

| Year-five share | Treatment |
|---:|---|
| ≥ 0.75 | no cap |
| ≥ 0.50 and < 0.75 | cap at `conditional` |
| ≥ 0.25 and < 0.50 | cap at `pass` |
| < 0.25 | `kill` |

Apply the gate after the factor-based verdict. Apply low, base, and high
survival values to the corresponding low, base, and high scenarios. Evidence
state never changes the gate.

## 6. Ranges, missing values, and partial identification

Every nonmissing primitive input supplies base, low, and high values with
`low ≤ base ≤ high`. I supplies coherent low/base/high monotone five-year
schedules. P's low case uses high buy/low downside exit; its high case uses low
buy/high downside exit. B uses the corresponding coverage and availability
bounds. V and C are monotone in their inputs.

The displayed `[S_low, S_high]` is a partial-identification envelope, not a
confidence or credible interval. Coordinatewise extremes must be supplemented
by coherent downside/base/upside scenario narratives; unsupported combinations
are a publication defect.

`MISSING` means no defensible base or bounded range exists:

- no neutral point is imputed;
- no base factor, base S, or base verdict is fabricated;
- the full semantic domain is used only to determine possible low/high
  economics; and
- readiness is `UNPROVEN`.

For missing V, I, C, or P, the factor domain is 0–10. Missing coverage or sale
availability uses its 0–1 domain when calculating B. Missing survival uses
0–1. A missing deterministic `n_band` makes B missing unless a separately
validated deterministic fallback exists.

After applying factor floors and the survival gate:

- if low and high imply the same verdict, that verdict is identified;
- if they imply different verdicts, economic verdict is `INDETERMINATE`;
- a base verdict is reported only when every score-driving and gating base
  input exists.

## 7. Evidence states and readiness

Each critical selection retains method `OBSERVED|CALCULATED|ESTIMATE`, evidence
state `DIRECT|PROXY|ASSUMPTION|MISSING`, and quality
`HIGH|MED|LOW|NONE`. Critical selections are the archetype enumeration and
coverage, V cost shares/weights/fractions, every I schedule value, C, sale
availability, buy multiple, downside exit multiple, and year-five survival.

- `DIRECT`: target-archetype evidence directly measures the contemporaneous
  input.
- `PROXY`: adjacent evidence supports an explicit population, time, size, or
  business-model bridge.
- `ASSUMPTION`: a bounded judgment has no input-specific empirical support.
- `MISSING`: no defensible value or bounded range exists.

Readiness is derived as follows.

### UNPROVEN

Any of:

- a critical input is `MISSING`, `LOW`, or `NONE`;
- the archetype boundary or largest-count selection is unsupported;
- target-specific V weights cannot be validly constructed;
- operator survival is unsupported; or
- a base or range endpoint lacks an evidence bridge.

### PROVISIONAL

No UNPROVEN condition, but any of:

- a critical input is an `ASSUMPTION`;
- a proxy does not satisfy the substantiation conditions below;
- the verdict interval crosses a tier; or
- the action is not invariant across supported scenarios.

### SUBSTANTIATED

All of:

- no critical `MISSING`, `ASSUMPTION`, `LOW`, or `NONE` input;
- archetype count, target cash-cost structure, and entry multiple are
  `DIRECT` or safely `CALCULATED` with MED/HIGH evidence;
- forward C, I, downside-exit, sale-availability, and survival inputs have
  MED/HIGH evidence with explicit temporal and population bridges;
- every range endpoint is supported; and
- verdict and action are invariant across supported scenarios.

Citation count and model-authored confidence labels never improve readiness.

## 8. Actions

First map every supported low/base/high verdict to its ordinary action:

| Verdict | Ordinary action |
|---|---|
| hell_yes or strong | `DEEP_DIVE` |
| conditional | `SELECTIVE` |
| pass | `DEPRIORITIZE` |
| kill | `AVOID` |

The final action is:

1. `EVIDENCE_FIRST` if the verdict is `INDETERMINATE`;
2. `EVIDENCE_FIRST` if supported scenarios imply different ordinary actions;
3. `EVIDENCE_FIRST` when readiness is `UNPROVEN`, except an identified
   structural `kill` whose high scenario cannot reach `pass` is `AVOID`;
4. otherwise the stable ordinary action.

Thus missing evidence cannot create a decisive positive or negative action.

## 9. Publication review

An isolated reviewer returns `publishable`, `publishable_with_caveats`,
`reject`, or `invalid`. Publication acceptance remains separate from economic
readiness.

The reviewer must verify archetype preselection, target-specific V weights,
cash removability rather than task automation, separation of I/C/survival,
five-year sale availability, absence of a consolidator double count, P's
consistent downside definition, both ends of every range, evidence-state
honesty, partial-identification behavior, action stability, deterministic
reproduction, and exact artifact digests.

An honestly low-readiness record may be publishable. A fabricated base for a
missing input, a NAICS-wide claim from a selected archetype, or evidence-driven
economic gate is material.

## 10. Frozen synthetic sentinels

All sentinels must pass exactly before any real v4.1 artifact is accepted.

1. Factors `[8,8,8,8,8]`, survival 0.80 ⇒ `hell_yes`.
2. Factors `[7,7,7,7,7]`, survival 0.80 ⇒ `strong`.
3. Factors `[5,5,5,5,5]`, survival 0.80 ⇒ `conditional`.
4. Factors `[10,1.5,10,10,10]`, survival 0.80 ⇒ `pass`, never `strong`.
5. Factors `[10,0.9,10,10,10]`, survival 0.80 ⇒ `kill`.
6. B=0 ⇒ `kill`.
7. Otherwise excellent factors and survival 0.40 ⇒ cap at `pass`.
8. Identical economics labeled DIRECT and PROXY ⇒ identical factors, S,
   gate, and verdict; readiness may differ.
9. One pivotal MISSING input whose domain crosses tiers ⇒ `INDETERMINATE` and
   `EVIDENCE_FIRST`.
10. Every primitive input is monotone in its stated direction, including
    epsilon tests immediately below, at, and above every factor floor, verdict
    cut, P anchor, B anchor, and survival boundary.
11. I reproduces every schedule anchor in section 3 within `1e-9` before
    display rounding.

## 11. Disclosed five-code regression canary

The following v4.0 codes and outputs have already been viewed and are
development data, not holdout evidence:

- 541512 Computer Systems Design Services;
- 541511 Custom Computer Programming Services;
- 541214 Payroll Services;
- 238220 Plumbing, Heating, and Air-Conditioning Contractors; and
- 541930 Translation and Interpretation Services.

They must be rerun from scratch under exact v4.1 artifacts. The regression gate
requires five schema-valid reproductions, zero arithmetic/identity/range
errors, five independent publishable-tier reviews after at most one bounded
remediation each, no repeated material construct defect, all sentinels passing,
and a written human economic-sense review.

Their score distribution, ordering, colors, and named verdicts are never
acceptance conditions and may not motivate a threshold change. If at least two
of five cannot bound a critical factor using the permitted evidence process,
v4.1 is declared evidence-infeasible; the response is a new version and new
holdout, not threshold tuning.

## 12. Untouched v4.1 holdout

Because the five v4.0 outputs were viewed, campaign authorization additionally
requires a five-code untouched holdout selected without economic outcomes.

1. Eligibility is the original Phase-4 fleet membership, excluding the five
   regression codes, golden-set codes, and any code with a pre-freeze v4.1
   packet, run, memo, review, or manually produced v4.1 result.
2. Sort eligible codes by the preexisting deterministic `labor_share` field
   from the frozen dataset vintage, breaking ties by NAICS. This field is used
   only to stratify holdout selection; it is not a substitute for the
   target-specific cash-cost input required by V.
3. Split the ordered list into five contiguous bins whose sizes differ by at
   most one.
4. Within each bin select the code with the lexicographically smallest
   lowercase SHA-256 of
   `"rollup-v4.1-holdout-2026-07-21|" + naics`.
5. Materialize the resulting membership and its inputs in the freeze manifest
   before any selected prompt is run.

The holdout uses the same mechanics, publication, sentinel, and human-review
gate as the regression canary. It has no preregistered named verdicts. Once any
holdout output is viewed, all five codes are burned for later methodology
versions.

## 13. Outcome-independent change control

A v4.1 failure may trigger v4.2 only for a documented:

- mathematical or monotonicity failure;
- construct contradiction;
- schema/scoring/reproduction mismatch;
- failure of the frozen review or evidence contract; or
- preregistered evidence-infeasibility condition.

A named industry's score, rank, verdict, color, or movement from v4.0 is not a
valid change trigger. Every superseded candidate and every result remains
preserved. A revised methodology requires a newly salted deterministic
holdout; viewed codes cannot return to holdout status.

## 14. Freeze manifest, digests, and authorization

Before any v4.1 research run, create a canonical manifest covering at least:

- `V4_1_METHODOLOGY.md` and `V4_0_REJECTION.md`;
- the complete threshold contract;
- scoring, schema, finalizer, renderer, campaign, and review code;
- research and review prompts;
- synthetic sentinel fixtures;
- deterministic dataset files and vintage;
- regression and holdout membership;
- exact research/reviewer model IDs; and
- the change-control rubric.

For every file record repository-relative path, byte length, and SHA-256.
Compute the root digest as SHA-256 of UTF-8 lines
`path + NUL + byte_length + NUL + file_sha256 + LF`, sorted bytewise by path.
The manifest itself is canonical JSON with sorted keys and no insignificant
whitespace.

Commit the files and manifest, record the commit ID, create a signed annotated
tag containing the root digest, and publish an externally timestamped CI or
release artifact before any v4.1 result exists. The threshold contract must
contain every numeric constant and categorical mapping in this document;
scoring must fail on unknown or unused threshold keys. A self-declared
`frozen: true` field is insufficient.

No v4.1 campaign is authorized until these steps are complete.
