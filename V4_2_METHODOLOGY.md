# AI Roll-Up Map — v4.2 Methodology

> **Historical:** superseded v4.2 candidate. The frozen v5 methodology governs the current product.

**Status:** outcome-blind freeze candidate. v4.2 preserves the sound v4.1
screening architecture while replacing constructs that failed preregistered
operational-consistency review. No v4.0, v4.1, or v4.2 economic output may be
used to choose a formula, anchor, cut, floor, gate, or holdout member in this
document.

v4.2 applies only to new, separately versioned artifacts. It does not mutate,
reinterpret, or validate any earlier packet, record, memo, review, score, or
campaign result. It is not operationally frozen until the manifest and
external timestamp requirements in section 15 are satisfied.

## 1. Decision, horizon, and unit

For one objectively preselected US lower-middle-market target archetype inside
a six-digit NAICS industry, v4.2 is a five-year unlevered screen. It asks:

1. what share of controllable value-added revenue is a gross removable cash
   labor and contractor opportunity;
2. how much of that opportunity is operationally realized over five years
   after explicit implementation and change investment;
3. how much of realized savings is retained commercially over five years;
4. how many sale-available targets a reference buyer can actually access and
   win during five years;
5. whether paid entry valuation and a state-consistent downside exit multiple
   are robust without rewarding multiple expansion; and
6. whether constant-price, operator-controlled value-added service demand
   survives through year five.

The output is a deep-dive priority, not company underwriting, a financing
model, an integration plan, or a realized-return forecast. Economic values and
verdicts never depend on evidence labels. Evidence affects readiness and action
only.

## 2. Archetype selection and denominator boundary

Phase 4 contains exactly one primary record per NAICS. Archetype selection is
completed before researching AI economics, implementation, capture,
buyability, or valuation.

1. Enumerate mutually exclusive target archetypes covering at least 80% of the
   estimated `$1–10M EBITDA` band; retain a named residual.
2. Assign stable IDs and estimate base/low/high band counts before economic
   research.
3. Select the largest base-count archetype. Break an exact tie with the
   lexicographically smallest stable ID. “Most investable” is forbidden.
4. If the top two base counts differ by less than 10%, or their supported
   ranges overlap, retain the largest-base selection as the single primary
   record, set `selection_uncertainty: true`, list every plausible alternative,
   widen coverage and value-basis ranges for reclassification consequences,
   and force readiness to `UNPROVEN`. If consequences cannot be bounded, the
   affected input is `MISSING`.
5. The record describes only its named archetype and is never presented as a
   NAICS-wide economic score.

The common economic denominator is target-archetype **controllable value-added
revenue**. Every recognized-revenue selection carries an evidenced revenue
basis and an exact partition of the packet's pass-through cost IDs:

The accounting basis is not free text. It is a closed object fixing accrual
recognized revenue, a trailing-twelve-month measurement period, and a
`pass_through_presentation` that must exactly equal the reconciliation's
revenue-basis mode.

- `GROSS_OF_ALL`: every pass-through ID is `included_cost_ids`;
- `NET_OF_ALL`: every pass-through ID is `already_netted_cost_ids`; or
- `MIXED`: both disjoint partitions are nonempty and their union is exact.

For an empty pass-through set the canonical basis is `GROSS_OF_ALL` with both
partitions empty. The finalizer computes:

`R_cva = recognized_revenue − Σ(pass_through_i for i in included_cost_ids)`

Amounts in `already_netted_cost_ids` are disclosed and reconciled but are not
subtracted again. Reconciliation evidence is a closed DIRECT, PROXY,
ASSUMPTION, or MISSING construct; nonempty pass-through with an unsupported
reconciliation makes `R_cva` and V `MISSING`.

Third-party pass-through is consideration contractually or economically owed
to an outside provider and not controlled as value added by the operator, such
as documented media, reimbursed filing, carrier, commodity, or subcontracted
service pass-through. A cost removed from `R_cva` may not also appear in V's
cash-cost numerator.

The packet supplies recognized revenue and each pass-through category with
base/low/high, accounting basis, and sources. Undocumented pass-through may not
be deducted. Overlap, omission, an unknown ID, or a revenue-basis/partition
mismatch is invalid. If the record cannot establish a positive, bounded,
internally consistent `R_cva`, the denominator and V are `MISSING`; gross
billed revenue is not a silent substitute.

## 3. Five frozen economic factors

All factors are continuous floats on 0–10. Model-authored packets contain
primitive inputs, evidence, ranges, and scenario rationale, never scores,
gates, actions, or verdicts.

### V — gross removable cash cost on controllable value added

Let:

- `employee_cash_cost` be target-archetype employee cash compensation and
  associated removable cash burden;
- `controllable_contractor_cash_cost` be contractor cost used to deliver the
  operator's controlled value added, excluding denominator pass-through;
- `role_cash_cost_weight_i` be role i's share of those costs, summing to 1;
  and
- `removable_fraction_i` be the fraction of role i's cash cost actually
  removable, or avoidable through evidenced growth, at full implementation.

`G = (employee_cash_cost + controllable_contractor_cash_cost) ×
     Σ(role_cash_cost_weight_i × removable_fraction_i)`

`g = G / R_cva`

`V = 10 × min(1, g / 0.25)`

Semantic anchors are unchanged:

| Gross removable cash cost / controllable value-added revenue | V |
|---:|---:|
| 0% | 0 |
| 5% | 2 |
| 12.5% | 5 |
| 20% | 8 |
| 25% or more | 10 |

V measures cash removability, not automatable task time. Pricing, market
diffusion, implementation investment, sale activity, valuation, and terminal
demand may not alter V. Target-specific cost weights are required. An invalid
broader-industry bridge makes V `MISSING`.

### I — five-year operational realization after investment

I measures operational realization controlled by the acquirer and explicitly
charges implementation and change investment. It never rewards market-wide
technology diffusion.

The packet supplies `r1` through `r5`, where `rt` is the fraction of G's full
annual gross removable opportunity operationally realized during year t before
commercial capture. Require:

`0 ≤ rt ≤ 1` independently for each `t ∈ {1,2,3,4,5}`

It also supplies nonnegative `k0` through `k5`. `k0` is implementation/change
investment paid at close; `kt` is investment or recurring AI/change cost paid
during year t. Each k is expressed as a fraction of one full year of G:

`k0, k1, k2, k3, k4, k5 ≥ 0`

Negative investment, vendor credits, or subsidies may not inflate I. A
documented subsidy is disclosed separately and is outside this screen.

Let `d = 10%`, `wt = 1/(1+d)^t`, and `D = Σ(t=1..5) wt`.

`i_raw = [Σ(t=1..5)(rt × wt) − k0 − Σ(t=1..5)(kt × wt)] / D`

`I = 10 × clamp(i_raw, 0, 1)`

If G=0, there is no gross AI savings opportunity against which investment can
be normalized: V=0, I=0 by deterministic convention, and the factor floors
produce kill. This convention is not a missing-data imputation; a missing or
unbounded G instead makes both V and I `MISSING`. Exact zero employee plus
contractor cost, or exact zero contribution from every removable-weight term,
identifies G=0 independently of `R_cva`; a missing revenue denominator may not
erase that structural zero.

No ordering is imposed on `r1..r5`. Operational realization may ramp and then
deteriorate; k represents investment and C represents commercial retention, so
neither is a substitute for lost operational realization in a later year.

With all k equal to zero, the exact frozen realization anchors are:

| Realization schedule | I |
|---|---:|
| 100/100/100/100/100% | 10.0 |
| 0/100/100/100/100% | 7.601841083684134 |
| 0/0/100/100/100% | 5.4216966143060725 |
| 0/0/0/100/100% | 3.4397470966896524 |
| 20/40/60/80/100% | 5.620251920525462 |
| 0/0/0/0/0% | 0.0 |

Sentinels compare unrounded values with absolute tolerance `1e-9`; display
rounding occurs only afterward. Sufficient upfront or ongoing investment can
make `i_raw ≤ 0` and I=0.

### C — five-year discounted commercial retention

C is separate from I. It measures only the commercial share of operationally
realized gross savings retained after client repricing, contractual
pass-through, renewal mechanics, and competitive commercial response.

The packet supplies `c1` through `c5`, the commercial retention share in each
year, with `0 ≤ ct ≤ 1`. No monotonic direction is presumed; contracts may
reprice at different times.

`C = 10 × [Σ(t=1..5)(rt × ct × wt)] / [Σ(t=1..5)(rt × wt)]`

C is therefore the discounted retention share of gross savings that are
actually realized operationally, not the retention of a hypothetical level
annual opportunity. If `Σ(rt × wt) = 0`, set `C = 0` by exact deterministic
convention: there are no operationally realized gross savings to retain. This
is an economic zero, not a missing-data imputation. If the denominator cannot
be determined because an `rt` is `MISSING`, base C is also `MISSING`.

For interval support, optimize the ratio jointly over the fixed five-year
feasible realization box
`P={r: rL_t≤r_t≤rH_t}`. Because C is componentwise
nondecreasing in c for fixed r, the minimum uses the complete `c_low` schedule
and the maximum uses `c_high`. For each of those schedules, enumerate every
one of the at most `2^5` distinct per-year lower/upper endpoint schedules and
evaluate the exact ratio above.

This is exhaustive: a linear-fractional objective with positive denominator
attains its extrema at vertices of the bounded box. If the all-zero schedule is feasible, its exact
conventional C score of 0 is also included. Base C remains the exact base-
schedule ratio. Values equal within the frozen numeric tolerance are
canonicalized to the exact base value before support ordering. This tight rule
affects C support only; h continues to use the coherent low/base/high scenario
schedules directly.

For any nonzero realization schedule, frozen constant-retention anchors are:

| Five-year commercial retention schedule | C |
|---|---:|
| 0/0/0/0/0% | 0 |
| 20/20/20/20/20% | 2 |
| 50/50/50/50/50% | 5 |
| 80/80/80/80/80% | 8 |
| 100/100/100/100/100% | 10 |

Employee removability belongs only in V. Workflow realization and timing enter
I and provide C's realized-savings weights; AI/vendor cost and change
investment belong only in I and never enter C's numerator or denominator.
Constant-price demand volume and operator control belong only in survival.

### B — expected executable and winnable five-year targets

B measures expected targets that a frozen reference buyer can both access and
win, not merely firms that exist or come to market.

The reference buyer is a financially credible US lower-middle-market sponsor
or platform able to close `$1–10M EBITDA` acquisitions, with professional
national sourcing but no incumbent relationship, proprietary channel,
regulatory exemption, or industry-specific privileged access unless that
feature is uniformly part of the declared campaign buyer profile.

First compute the opportunity set and the buyer's execution ceiling:

`O5 = n_band × archetype_coverage × five_year_sale_availability_share ×
      buyer_access_win_share`

`K5 = min(deal_execution_capacity_5y, integration_onboarding_capacity_5y)`

`N5 = min(O5, K5)`

Both capacity selections are closed typed objects, not causal prose. Each fixes
its type (`DEAL_EXECUTION` or `INTEGRATION_ONBOARDING`), entry-date through
end-of-year-five horizon, maximum nonduplicative target-count calculation, and
the exact buyer/geography/archetype scope. Both count only acquisitions completed and fully onboarded
within five years by the same frozen reference buyer, in the United States,
for the frozen selected target archetype. The buyer has credible national LMM
sourcing but no privileged access. Deal-execution capacity covers transactions
the buyer can diligence, finance, and close; integration/onboarding capacity
covers targets it can absorb into accountable operation without changing the
buyer or target archetype. Capacity cannot create opportunity beyond `O5`.

`buyer_access_win_share` is the conditional share of sale-available targets
the reference buyer can source, access, diligence, and win at the prevailing
market-clearing price. It may reflect geography, process access, eligibility,
and competition for target count. It may not assume a price discount, penalize
the paid multiple, or reward willingness to overpay. Paid price belongs only
in P. Raw active-consolidator count is not an additional B penalty.

`B = 10 × clamp(log10(1 + N5) / log10(501), 0, 1)`

Frozen anchors remain:

| Expected executable/winnable targets | B |
|---:|---:|
| 0 | 0.00 |
| 10 | 3.86 |
| approximately 21 | approximately 5.00 |
| 100 | 7.42 |
| 500 or more | 10.00 |

Sale availability, access/win share, and both capacities each require separate
base/low/high values and evidence metadata. If either capacity is MISSING, base
B is MISSING; capacity low is 0 and capacity high is the minimum of `O5_high`
and every known capacity high endpoint. Thus one missing capacity never erases
the known ceiling imposed by the other. The same market evidence may support both a win probability and P's paid
price only when the record states the distinct quantity and price channels.

### P — paid-price and state-consistent valuation robustness

P captures actual paid entry valuation and a multiple-only downside. It never
rewards multiple expansion.

`entry_score = clamp(14 − buy_mult, 0, 10)`

Entry anchors remain 4x=10, 6x=8, 8x=6, 10x=4, 12x=2, and 14x=0.

`buy_mult` is entry EV divided by consistently normalized entry EBITDA for the
named target archetype. `downside_exit_mult` is year-five EV divided by
consistently normalized year-five EBITDA, conditional on one entry-equivalent
`normalized_y5_operating_state`. Its accounting, size, service mix, customer
concentration, management depth, and platform quality dimensions each equal
`HOLD_ENTRY_REFERENCE`; its reference is `ENTRY_TARGET_ARCHETYPE`, its scenario
policy is `ONE_STATE_LOW_BASE_HIGH`, and sponsor transformation is forbidden.
The finalizer binds P to the canonical SHA-256 digest of this closed state.

Downside exit multiple is recomputed, never accepted as a free scalar:

`downside_exit_mult = anchor + Σ(allowed_adjustment_j)`

The anchor has its own closed basis: its only channel is
`ENTRY_EQUIVALENT_COMPARABLE_MULTIPLE_LEVEL`, and it binds the identical
normalized-y5 state digest, entry-target reference, and one-state scenario
policy. Free-text rationale cannot introduce an alternate anchor channel.

The only allowed adjustment channels are external discount-rate environment,
entry-equivalent comparable-multiple level, and private-transaction liquidity.
Every adjustment is nonpositive, so the construct cannot reward favorable
multiple expansion. A closed exclusion map explicitly excludes C, survival,
I realization/investment, h, V, B, sponsor transformation/synergy, margin,
size, service mix, concentration, management depth, platform quality, and
accounting changes. Missing state support, a digest mismatch, an unsupported
anchor/adjustment, or an excluded channel makes P's downside input `MISSING`.

The same state digest is used for P's low, base, and high analysis. Changes in
C or constant-price survival may change operating dollars outside P; they may
not cause an additional multiple haircut inside P. Any duplicate or unlisted
channel is a material defect.

`resilience_score =
    clamp(20 × (downside_exit_mult / buy_mult − 0.5), 0, 10)`

Resilience anchors remain 50% multiple retention=0, 75%=5, and flat or
expanding=10. Expansion receives no score above 10.

`P = min(entry_score, resilience_score)`

When state or downside-exit support is missing but buy-multiple support is
known, base P remains MISSING and low P remains 0, but P high is capped by the
maximum feasible entry score from the low buy endpoint. Missing downside
support may not silently restore P high to 10; for example buy low 13x caps
P high at 1.

If buy multiple is MISSING, its domain is positive with no positive lower
bound. Therefore a positive downside-exit high can still permit P high 10, but
an exactly zero downside-exit high makes resilience zero for every feasible
positive buy multiple and collapses P high to 0.

Observed transaction evidence may directly measure a comparable entry
multiple. A future downside exit conclusion is normally PROXY or ASSUMPTION,
not DIRECT.

## 4. Operating-value viability cross-check

I and C remain distinct factors, but implementation investment is not
commercially retained. A deterministic cross-check therefore prevents their
separate scores from masking a negative combined cash opportunity.

In units of one full year of G:

`h = Σ(t=1..5)(rt × ct × wt) − k0 − Σ(t=1..5)(kt × wt)`

If `h ≤ 0`, the scenario is `kill`. Apply this rule independently to low,
base, and high scenarios and before the survival gate. This is an economic
gate, never an evidence-quality gate. `h` is a diagnostic and gate, not a sixth
factor and not a return forecast.

This is the only new threshold-like treatment in v4.2. It is mathematically
required because multiplying separately scored I and C would otherwise apply
commercial retention to implementation investment and could label a negative
cash opportunity investable.

## 5. Aggregate score, cuts, and floors

`S = (V × I × C × B × P)^(1/5)`

The outcome-independent v4.1 aggregate cuts and structural floors are retained
unchanged. Assign tiers in descending order, after applying the h gate:

| Verdict | Aggregate cut | Minimum every factor |
|---|---:|---:|
| `hell_yes` | S ≥ 7.5 | ≥ 6 |
| `strong` | S ≥ 6.0 | ≥ 4 |
| `conditional` | S ≥ 4.5 | ≥ 2 |
| `pass` | S ≥ 3.0 | ≥ 1 |
| `kill` | otherwise | — |

Floors are economic and apply regardless of evidence state. A high factor
cannot compensate for a structurally failed factor. `N5=0` produces B=0 and
kill without a separate provenance-dependent gate.

## 6. Constant-price year-five operator survival

The packet supplies a closed fixed-base service basket for
`operator_controlled_value_added_demand_share_y5`. For each exhaustive baseline
service j it records a stable service ID and unit, constant-quality
specification, baseline quantity `q0_j`, baseline revenue, baseline
pass-through, derived baseline CVA, derived baseline CVA unit price `p0_j`,
base weight `w0_j`, and year-five operator-controlled quantity `q5_j`.

Every fixed-baseline primitive—`q0_j`, baseline recognized revenue, and
baseline pass-through—is point-identified: low=base=high. Derived baseline CVA,
CVA unit price, and weight are therefore points as well. A ranged baseline is
invalid and survival is never computed by silently discarding that range. For
example `q0=[50,100,400]` with `q5=80` is rejected or yields MISSING, never an
invented `[0.8,0.8]` survival support.

The finalizer reconciles each service and the exhaustive basket to the same
pass-through boundary and `R_cva` used by V:

`CVA0_j = baseline_revenue_j − baseline_pass_through_j`

`p0_j = CVA0_j / q0_j`

`w0_j = CVA0_j / R_cva_base`, with `Σ_j w0_j = 1`

The constant-price survival index is the fixed-base Laspeyres quantity index:

`survival_y5 = Σ_j(w0_j × q5_j / q0_j)`

Real baseline CVA unit prices and stated service quality are held constant.
`q5_j` counts only demand still purchasing the accountable service from the
named operator. New services and new demand are excluded, and every quantity
relative is capped at one. A nonexhaustive basket, mismatched CVA/pass-through,
zero or missing positive-weight endpoint, invalid weight, or total other than
the reconciled `R_cva` makes survival `MISSING`.

This construct excludes:

- price/repricing and contractual pass-through, which belong in C;
- implementation and cost realization, which belong in I;
- third-party billed pass-through excluded from `R_cva`; and
- valuation multiples, which belong in P.

Frozen survival treatment remains:

| Constant-price operator-controlled value-added demand share | Treatment |
|---:|---|
| ≥ 0.75 | no cap |
| ≥ 0.50 and < 0.75 | cap at `conditional` |
| ≥ 0.25 and < 0.50 | cap at `pass` |
| < 0.25 | `kill` |

Apply the gate after the h gate and factor-based verdict. Use corresponding
low/base/high fixed-base quantity selections in each scenario. Evidence state
never changes the gate.

## 7. Ranges, scenarios, and partial identification

Every nonmissing primitive input supplies base, low, and high values with
`low ≤ base ≤ high`. Annual I realization paths are unconstrained across years;
implementation investments are nonnegative. C schedules remain bounded 0–1.

For monotone endpoints:

- V uses the supported low/base/high numerator and denominator combinations;
- I low uses low realization/high investment, and I high uses high
  realization/low investment;
- C base uses the corresponding coherent base realization and retention
  schedules, while low/high use the exact box-vertex extrema rule in
  section 3; because changing realization timing can change the
  retention mix, no standalone monotonic direction is presumed for C with
  respect to r;
- B first computes coherent `O5`, `K5`, and `N5`; B low uses low opportunity
  and low capacities, while B high uses their highs;
- P low uses high buy/low downside exit; P high uses low buy/high downside
  exit; and
- h and survival use coherent downside/base/upside combinations.

These marginal factor supports remain the displayed diagnostics, but they are
not combined mechanically to identify verdicts. I, C, and h share one feasible
realization schedule. For each downside/upside endpoint bundle, the scorer
enumerates the exact vertices of the five-year r interval box and
projects them to

`A = Σ(r_y w_y)` and `N = Σ(r_y c_y w_y)`.

Their convex hull is sufficient because I, C, and h depend on r only through
`(A,N)`. On every hull edge the finite decision algorithm evaluates vertices,
stationary candidates of the I×C product, intersections with every I/C floor,
aggregate cut, and h=0, plus one representative inside every resulting edge
interval. The lower decision tier uses worst c/k/other-factor endpoints; the
upper attainable tier uses their best endpoints. This preserves exact marginal
C vertex extrema for display while forbidding a verdict or action based on an
incompatible low-I/low-C or high-I/high-C bundle.

The packet must supply coherent named scenario narratives. The displayed
`[S_low, S_high]` is a partial-identification envelope, not a confidence or
credible interval.

`MISSING` means no defensible base or bounded range exists. No neutral base is
imputed. Full semantic domains are used only for partial identification:

- V, I, C, and P: 0–10 factor domain;
- coverage, sale availability, and access/win share: 0–1;
- survival service quantity relatives: 0–1, with new demand excluded;
- five-year capacity: nonnegative, with missing capacity bounded from 0 to the
  corresponding `O5` opportunity support;
- nonnegative implementation investment: no artificial finite upper bound,
  implying I low=0 and h may be nonpositive.

No base factor, S, h, gate, or verdict is fabricated from a missing primitive.
After applying floors, h, and survival:

- if every feasible scenario has one verdict, that verdict is identified;
- otherwise economic verdict is `INDETERMINATE`;
- a base verdict exists only when every score-driving and gating base input
  exists.

## 8. Evidence contract and reachable readiness states

Each critical selection records method `OBSERVED|CALCULATED|ESTIMATE`, evidence
state `DIRECT|PROXY|ASSUMPTION|MISSING`, quality `HIGH|MED|LOW|NONE`, source
IDs, base/range or schedules, rationale, and caveats.

Critical selections include archetype enumeration/coverage; recognized revenue,
the revenue-basis reconciliation, and every pass-through item; V cost basis,
weights, and removability; every r and k; every c; sale availability;
access/win share; deal-execution and integration/onboarding capacities; buy
multiple; the normalized-y5 state digest; downside anchor and every allowed
adjustment; and every fixed-base survival service endpoint.

State/quality combinations are constrained:

- DIRECT requires target-archetype evidence, OBSERVED or safely CALCULATED
  method, at least one source, and MED/HIGH quality.
- PROXY requires at least one source and an explicit bridge. It may be
  HIGH/MED/LOW.
- ASSUMPTION requires ESTIMATE, NONE quality, no source, and a candid bounded
  base/range.
- MISSING requires ESTIMATE, NONE quality, no source, and null base/range.

Readiness is evaluated in this order, making every state reachable and the
ASSUMPTION treatment internally consistent.

### UNPROVEN

Any of:

- a critical input is MISSING or ASSUMPTION;
- a critical input has LOW or NONE quality;
- `selection_uncertainty` is true;
- the controllable-value-added denominator or its gross/net/mixed
  reconciliation is unsupported;
- target-specific V weights cannot be validly constructed;
- either five-year capacity selection is unsupported;
- h or survival lacks a supported endpoint; or
- a base/range/schedule endpoint lacks its stated evidence bridge.

Because ASSUMPTION necessarily has NONE quality, it always maps to UNPROVEN;
there is no unreachable PROVISIONAL-assumption branch.

### SUBSTANTIATED

All of:

- no UNPROVEN condition;
- archetype count, `R_cva` reconciliation, target cash-cost structure, and
  entry multiple are DIRECT or safely CALCULATED with MED/HIGH evidence;
- every forward PROXY has MED/HIGH quality, a target-applicable bridge with
  supported endpoints, and independent corroboration or a documented
  longitudinal validation;
- C, survival, and P rationales pass the no-double-count checks;
- verdict and ordinary action are invariant across supported scenarios; and
- an isolated reviewer reproduces every factor, h, floor, and gate.

### PROVISIONAL

No UNPROVEN condition, but one or more SUBSTANTIATED requirements is not met.
Examples include a MED/HIGH forward proxy with a disclosed but not independently
validated bridge, a supported tier-crossing interval whose ordinary action is
stable, or insufficient corroboration for a range endpoint.

This ordered definition makes PROVISIONAL reachable without mislabeling an
unsupported assumption and makes SUBSTANTIATED reachable with validated
forward proxies rather than requiring impossible direct future evidence.
For a derived composite, validation is complete when every proxy component
individually qualifies by either permitted route. A mixture of independently
corroborated and longitudinally validated components is complete; all
components need not use the same validation kind.

Citation count and model-authored confidence labels never improve readiness.

## 9. Actions

Map a stable economic verdict to its ordinary action:

| Verdict | Ordinary action |
|---|---|
| hell_yes or strong | `DEEP_DIVE` |
| conditional | `SELECTIVE` |
| pass | `DEPRIORITIZE` |
| kill | `AVOID` |

Final action is:

1. `EVIDENCE_FIRST` if economic verdict is INDETERMINATE;
2. `EVIDENCE_FIRST` if supported scenarios imply different ordinary actions;
3. `EVIDENCE_FIRST` when readiness is UNPROVEN, except an identified
   structural kill whose high scenario cannot reach pass is `AVOID`;
4. otherwise the stable ordinary action.

Missing or assumed evidence cannot create a decisive positive or negative
action. Evidence never changes the economic verdict itself.

## 10. Publication review

An isolated reviewer returns `publishable`, `publishable_with_caveats`,
`reject`, or `invalid`. Publication acceptance remains distinct from economic
readiness.

The reviewer must verify:

- objective archetype selection and one-record membership;
- the evidenced gross/net/mixed `R_cva` partition, including proof that each
  pass-through ID is removed exactly once;
- target-specific V weights and cash removability;
- every I realization and explicit nonnegative investment input;
- C's five-year commercial schedule and its separation from I/survival;
- the h cross-check;
- B's `O5`, scoped deal/integration capacities, `K5`, and `N5`, without a
  paid-price penalty;
- P's canonical normalized-y5 state digest, closed anchor/adjustment channels,
  and exact exclusion map;
- fixed-base Laspeyres service-basket reconciliation and constant-price,
  value-added operator survival;
- every range endpoint, readiness state, action, and missing-value treatment;
  and
- schema, identity, deterministic reproduction, and exact artifact digests.

A fabricated denominator, negative investment, missing base imputation,
NAICS-wide claim, duplicate deterioration channel, or evidence-dependent
economic gate is material.

## 11. Frozen synthetic sentinels

All sentinels must pass before any real v4.2 artifact is accepted.

1. V uses `R_cva`, and adding documented pass-through equally to billed revenue
   and pass-through leaves V unchanged.
2. A cost excluded as pass-through cannot also appear in V's numerator.
3. With all k=0, I reproduces all six exact anchors in section 3 within
   absolute tolerance `1e-9`.
4. With all r=1 and `k0=D`, I=0; with larger investment I remains 0.
5. Changing only k changes I and h, never C.
6. Changing only a c schedule changes C and h, never I.
7. With all r=1, all c=0.20, all later k=0, and `k0=0.25D`, h<0 and verdict is
   kill even though I and C are positive.
8. Holding all else fixed, reducing sale availability or access/win share
   cannot improve B.
9. Changing only buy price changes P, never B; changing only access/win share
   changes B, never P.
10. Holding P inputs and normalized y5 state fixed, changing only C or survival
    leaves P exactly unchanged.
11. Factors `[8,8,8,8,8]`, h>0, survival 0.80 ⇒ `hell_yes`.
12. Factors `[7,7,7,7,7]`, h>0, survival 0.80 ⇒ `strong`.
13. Factors `[5,5,5,5,5]`, h>0, survival 0.80 ⇒ `conditional`.
14. Factors `[10,1.5,10,10,10]`, h>0, survival 0.80 ⇒ `pass`.
15. Factors `[10,0.9,10,10,10]` ⇒ `kill`.
16. Otherwise excellent factors and constant-price survival 0.40 ⇒ pass cap.
17. Identical primitive economics labeled DIRECT and PROXY produce identical
    factors, h, gates, and verdict; readiness may differ.
18. One ASSUMPTION critical input ⇒ UNPROVEN, never PROVISIONAL.
19. A MED supported proxy lacking independent bridge validation, with no
    UNPROVEN condition ⇒ PROVISIONAL.
20. A fully qualifying stable synthetic evidence packet ⇒ SUBSTANTIATED.
21. One pivotal MISSING input whose domain crosses actions ⇒ INDETERMINATE and
    EVIDENCE_FIRST.
22. Every primitive input passes directionality and epsilon tests immediately
    below, at, and above every anchor, floor, cut, h=0, and survival boundary.
23. With `r=[0,0,0,0,1]`, `c=[1,1,1,1,0.001]`, and all k=0, C is exactly
    `0.01`, not the approximately `8.36` produced by weighting retention in
    years with no realized savings. Here h is positive but C's structural
    floor still produces `kill`; positive h alone cannot create an attractive
    verdict.
24. Gross-of-all revenue 100 with pass-through 20 gives `R_cva=80`; the same
    amount declared net-of-all gives `R_cva=100`; a valid mixed partition
    subtracts only its included IDs.
25. Overlap, omission, unknown pass-through IDs, or subtracting an
    already-netted amount fails closed; unsupported reconciliation makes V
    MISSING.
26. With `O5=100`, deal capacity 100, and integration capacity 80, `K5=80` and
    `N5=80`; raising either capacity alone above the other cannot improve B.
27. Missing capacity makes base B MISSING and sets low capacity to 0; high
    capacity is `min(O5_high, every known capacity high)`. With `O5_high=100`
    and the other known capacity high 40, high `K5=N5=40`.
28. A one-service basket with `R_cva=80`, `q0=100`, baseline CVA unit price
    0.8, weight 1, and `q5=70` recomputes survival exactly to 0.70; a basket
    mismatch fails closed.
29. A downside anchor of 5.0 plus a private-liquidity adjustment of −1.0 gives
    4.0. A positive adjustment, excluded channel, state mutation without a new
    digest, or digest mismatch fails closed.
30. `q0=[50,100,400]` and `q5=80` is a ranged fixed baseline and therefore
    MISSING or invalid, never collapsed to survival 0.8.
31. With buy low 13x and missing state or exit support, P high is at most 1.
32. A composite whose proxy components are respectively independently
    corroborated and longitudinally validated is validation-complete and may
    reach SUBSTANTIATED when every other condition qualifies.
33. Recognized-revenue presentation must equal the gross/net/mixed partition;
    swapped capacity types and any non-comparable-multiple anchor channel fail
    schema validation.
34. With `x=0.043293960941`, `r1..r4∈[x,1]`, `r5=1`,
    `c=[.05,.05,.05,.05,1]`, all k=0, V=B=P=6.5, and survival=.8, both exact
    joint decision endpoints are `conditional`; action is `SELECTIVE`, not an
    indeterminate pass–strong envelope built from incompatible marginals.
35. Missing buy multiple with downside-exit high exactly 0 gives P high 0;
    missing buy with a positive exit high retains feasible P high 10.
36. Missing `R_cva` plus exact zero employee and contractor cost forces
    G=V=I=0 and stable factor-floor kill. The h diagnostic remains derived
    independently from r, c, and k and is not forced to zero.
37. Missing `R_cva` plus exact zero contribution from every removable-weight
    term produces the same structural G=V=I zero; h remains schedule-derived,
    while positive or unresolved G retains ordinary missing-denominator V
    support.
38. `r=[.2,.8,.9,.4,.1]` is valid. Against otherwise identical
    `[.2,.8,.9,.9,.9]`, later operational decay lowers I, C, and h when
    retention is concentrated in years four and five.

Synthetic profiles are mathematical contracts, not desired real-industry
outcomes.

## 12. Development regression campaign

Every code with a viewed or generated v4.0 or v4.1 economic artifact is
development data. Such codes may be rerun from scratch to test schema,
construct separation, reproducibility, evidence feasibility, and reviewer
behavior, but their score, rank, color, movement, or verdict is never an
acceptance condition and may not trigger a threshold change.

The fixed five-record evidence-feasibility regression set is the already
disclosed v4.0 development set: 541512, 541511, 541214, 238220, and 541930.
Other viewed codes remain development data but do not change this denominator.

The development gate requires all synthetic sentinels, deterministic
reproduction, exact model/prompt routing, one bounded remediation at most,
publishable-tier isolated review for every accepted artifact, no repeated
material construct defect, and a written outcome-blind root/operator economic-
sense review bound to the exact gate artifacts by the frozen operator's SSH
signature. The signature authenticates the operator principal and payload; it
does not claim that a human personally performed the review.

If at least two of five preregistered development records cannot bound a
critical construct under the evidence contract, v4.2 is evidence-infeasible.
The response is a new version and a new untouched holdout, never tuning a
threshold to make a named record usable.

## 13. New untouched salted v4.2 holdout

Campaign authorization requires a new five-code holdout. No prior v4.1 salt or
membership may be reused.

1. Eligibility is the original Phase-4 fleet membership, excluding golden-set
   codes, every disclosed development code, every code with any generated
   v4.0/v4.1 economic artifact, and every code with a pre-freeze v4.2 packet,
   score, memo, review, or manually calculated result.
2. Sort eligible codes by the preexisting deterministic `labor_share` field in
   the frozen dataset vintage, breaking ties by NAICS. This field is used only
   for holdout stratification, never as V's denominator or target cost basis.
3. Split the ordered list into five contiguous bins whose sizes differ by at
   most one.
4. In each bin select the lexicographically smallest lowercase SHA-256 of
   `"rollup-v4.2-holdout-2026-07-21|" + naics`.
5. Materialize eligibility, exclusions, bins, hashes, selected membership, and
   dataset digests in the freeze manifest before any selected prompt is run.

The holdout uses the same sentinel, mechanical, evidence, publication, and
root/operator-review gates as development, without named verdict or distribution
expectations. Once any holdout output is generated or viewed, all selected
codes are burned for future methodology versions.

## 14. Outcome-independent change control

A v4.2 failure may trigger v4.3 only for a documented:

- mathematical, directionality, or sentinel failure;
- construct contradiction or double count;
- schema/scoring/reproduction mismatch;
- review/evidence-contract failure; or
- preregistered evidence-infeasibility condition.

A named score, rank, color, verdict, distribution, or movement from an earlier
version is not a valid trigger. Every candidate and result remains preserved.
A replacement version requires a new salt and untouched holdout.

## 15. Freeze manifest, digests, and authorization

Before any v4.2 research run, create a canonical manifest covering:

- this methodology and the v4.2 change/rejection record;
- complete thresholds and categorical mappings;
- scoring, h cross-check, schema, finalizer, renderer, campaign, and review
  code;
- research and review prompts;
- synthetic sentinel fixtures;
- deterministic dataset files and vintage;
- development and holdout membership;
- exact research/reviewer model IDs; and
- the change-control rubric.

For each file record repository-relative path, byte length, and SHA-256.
Compute the root digest as SHA-256 of UTF-8 lines
`path + NUL + byte_length + NUL + file_sha256 + LF`, sorted bytewise by path.
The manifest is canonical JSON with sorted keys and no insignificant
whitespace.

Commit the complete artifact set and manifest, record the commit ID, create a
signed annotated tag containing the root digest, and publish an externally
timestamped CI or release artifact before any v4.2 result exists. Every numeric
constant and categorical mapping in this document must exist in the threshold
contract; scoring fails on unknown or unused threshold keys. A self-declared
`frozen: true` field is insufficient.

No v4.2 campaign is authorized until these steps are complete.
