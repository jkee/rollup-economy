# AI Roll-Up Map — v4.2 target-archetype primitive research packet

Research **{{NAICS}} — {{TITLE}}** as a US lower-middle-market roll-up screen.
Return exactly one JSON packet conforming to
`pipeline/build/schemas/research_packet_v4_2.schema.json`. Python owns every
derived factor, interval, readiness state, cross-check, gate, action, and
verdict. Do not calculate or recommend any of them.

## Runtime identity

- model: `{{MODEL_ID}}`
- date: `{{RUN_DATE}}`
- run id: `{{RUN_ID}}`
- template version: `4.2`
- prompt version: `{{PROMPT_VERSION}}` — exactly `v4.2-target-archetype-1`
- execution kind: `target`
- attempt: supplied by the campaign manifest

Use only the supplied research authorities. Do not seek orchestration metadata,
expected ordering, prior conclusions, or another run's artifacts or review.

## Pinned authorities

- industry specification: `{{SPEC_PATH}}`
- industry specification SHA-256: `{{SPEC_SHA256}}`
- methodology: `{{METHODOLOGY_PATH}}`
- methodology SHA-256: `{{METHODOLOGY_SHA256}}`
- normalized dataset: `{{DATASET_PATH}}`
- normalized dataset SHA-256: `{{DATASET_SHA256}}`

Use only these exact, digest-matched authorities. Stop on any missing file or
digest mismatch. Do not substitute a legacy block, dataset, prompt, or method.

### Frozen industry specification

```json
{{INDUSTRY_SPEC_JSON}}
```

The selected target archetype, its alternatives, residual, count ranges,
coverage, uncertainty flag, value basis, role membership, cash-cost weights,
and allowed pass-through categories are immutable model inputs. Recheck the
objective enumeration arithmetic, but do not select another archetype or
reweight roles based on perceived economics. If selection uncertainty is true,
keep one primary record, make no industry-wide claim, and treat readiness as
`UNPROVEN`.

Obey `value_basis.mode` exactly:

- `target_specific`: preserve the source-backed cash-cost IDs, mutually
  exclusive roles, weights, methods, evidence qualities, and B-source links.
- `assumption`: preserve the pre-frozen source-free cash-cost IDs, role
  taxonomy, and bounded unit-sum weights exactly. These roles are
  `ESTIMATE`/`NONE` with empty source IDs. Do not attach evidence, substitute
  normalized-dataset roles, or imply the basis is measured; all packet
  cash-cost amounts and role removable fractions must be bounded
  `ASSUMPTION`/`NONE` with empty source IDs, and readiness is `UNPROVEN`.
- `missing`: do not invent cash-cost IDs, roles, weights, or a V base.

### Pinned normalized dataset

```json
{{DATASET_INPUTS_JSON}}
```

Do not re-research or change a non-null normalized value. A missing primitive
has no invented base, bounded range, neutral point, or implied economic result.

## Research guidance

### Candidate sources

{{SOURCE_HINTS}}

Hints are leads, not evidence. Reopen each selected HTTP(S) source, register
only sources actually used, and bind each selection to its supporting IDs.

### Controllable value added and V primitives

{{VALUE_ADDED_QUESTIONS}}

Reconcile recognized revenue to controllable value-added revenue by subtracting
only documented third-party pass-through categories approved by the frozen
specification. `inputs.recognized_revenue` must include `accounting_basis` as
the exact closed object with `recognition_standard` equal to
`ACCRUAL_RECOGNIZED_REVENUE`, `measurement_period` equal to
`TRAILING_TWELVE_MONTHS`, and `pass_through_presentation` equal to exactly one
of `GROSS_OF_ALL`, `NET_OF_ALL`, or `MIXED`. That presentation must equal the
`revenue_basis` in the structured `pass_through_reconciliation`. Partition
every authored pass-through `cost_id` exactly once between disjoint
`included_cost_ids` and `already_netted_cost_ids`; and attach construct
evidence. `GROSS_OF_ALL` puts every ID in included, `NET_OF_ALL` puts every ID
in already netted, and `MIXED` requires both nonempty. With no pass-through
items, use `GROSS_OF_ALL` and two empty partitions. Give each pass-through
category its own unique cost ID, accounting basis, amount range, and evidence.
Never count the same cost both as denominator pass-through and in the employee
or controllable-contractor cash-cost numerator. Estimate role removability as
cash cost actually removable or avoidable at full implementation, not task
time. Keep pricing, implementation, commercial response, deal activity, and
survival outside V.

### Operational realization and implementation investment

{{IMPLEMENTATION_QUESTIONS}}

Supply coherent low/base/high values for `r1` through `r5`, where each `rt` is
the operationally realized fraction of full removable cash cost in year t.
No ordering is imposed on `r1` through `r5`: realization may ramp and later
deteriorate. Separately supply nonnegative `k0` through `k5`, each expressed as
a fraction of one full year of gross removable cash cost. `k0` includes
up-front implementation and change investment; later values are year-specific
investment. Keep discounting, operational realization, and investment
separate. Do not hide up-front or early losses, vendor cost, change cost, or
execution loss in commercial retention.

### Commercial retention

{{COMMERCIAL_RETENTION_QUESTIONS}}

Supply separate low/base/high `c1` through `c5` schedules for the share of
operationally realized savings commercially retained after repricing,
contractual pass-through, renewal mechanics, and competitive response. No
monotonic direction is assumed. Do not put implementation investment,
operational execution loss, or operator-controlled demand survival in C.

### Buyability: sale availability and buyer access/win

{{SALE_AVAILABILITY_QUESTIONS}}

{{BUYER_ACCESS_WIN_QUESTIONS}}

Estimate five-year sale availability and buyer access/win share as separate
base/low/high primitives with separate causal rationales. Access/win is
conditional on sale availability and assumes prevailing market-clearing price;
it may not embed a price discount. Keep entry price and valuation entirely in
P. Unknown owner age is neutral, not evidence of availability.

Also supply separate `deal_execution_capacity_5y` and
`integration_onboarding_capacity_5y` selections. Their `capacity_type` values
must be `DEAL_EXECUTION` and `INTEGRATION_ONBOARDING`, respectively. Each must
carry the exact `capacity_horizon`: start `ENTRY_DATE`, end `END_OF_YEAR_5`,
and years 5; the exact `capacity_calculation`: measure
`MAXIMUM_TARGET_COUNT`, completion requirement `CLOSED_WITHIN_FIVE_YEARS`,
onboarding requirement `FULLY_ONBOARDED_WITHIN_FIVE_YEARS`, and aggregation
`NON_DUPLICATIVE_TARGET_COUNT`; and the exact closed `capacity_scope`:
reference buyer
`CREDIBLE_US_LMM_NATIONAL_SOURCING_NO_PRIVILEGED_ACCESS`, `horizon_years` 5,
`geography` `UNITED_STATES`, `target_archetype`
`FROZEN_SELECTED_TARGET_ARCHETYPE`, and
`counts_only_completed_and_onboarded_targets` true. Deal capacity covers
diligence, financing, and closing;
integration capacity covers accountable operational onboarding. Do not combine
the capacities or let either create opportunities beyond the sale/access set.

### Entry and downside valuation robustness

{{VALUATION_ROBUSTNESS_QUESTIONS}}

Research all-in entry EV/normalized EBITDA and a downside year-five exit
multiple using one explicit `normalized_y5_operating_state` for low, base, and
high analysis. Its six dimensions—`accounting`, `size`, `service_mix`,
`customer_concentration`, `management_depth`, and `platform_quality`—must each
equal `HOLD_ENTRY_REFERENCE`. Its entry-equivalence object must bind
`ENTRY_TARGET_ARCHETYPE`, `ONE_STATE_LOW_BASE_HIGH`, and
`NO_SPONSOR_TRANSFORMATION`. Supply the canonical state SHA-256 and bind
`downside_exit_multiple.normalized_y5_state_digest` to it exactly.

The downside multiple `anchor.anchor_basis` must use channel
`ENTRY_EQUIVALENT_COMPARABLE_MULTIPLE_LEVEL`, bind its
`normalized_y5_state_digest` to that identical canonical state digest, set
`state_reference` to `ENTRY_TARGET_ARCHETYPE`, and set `scenario_policy` to
`ONE_STATE_LOW_BASE_HIGH`. Its rationale cannot introduce another anchor
channel.

Author downside multiple as an anchor plus at most one nonpositive adjustment
per closed channel:
`EXTERNAL_DISCOUNT_RATE_ENVIRONMENT`,
`ENTRY_EQUIVALENT_COMPARABLE_MULTIPLE_LEVEL`, and
`PRIVATE_TRANSACTION_LIQUIDITY`. Populate the closed exclusion map with every
required channel set to `EXCLUDED`. P measures multiple resilience only;
commercial retention, survival, realization, investment, h, V, B, sponsor
effects, margin, size, mix, concentration, management, platform, and accounting
changes cannot enter the multiple. Do not assume favorable multiple expansion.

### Constant-real-price operator survival

{{SURVIVAL_QUESTIONS}}

Supply `operator_controlled_value_added_demand_share_y5` as a closed fixed-base
service basket, not a scalar estimate. Use the exact assertions
`FIXED_BASE_LASPEYRES_CVA`, `BASELINE_CVA_PER_UNIT_HELD_CONSTANT`,
`CONSTANT_QUALITY`, `EXHAUSTIVE_BASELINE_SERVICES_ONLY`,
`PURCHASED_FROM_NAMED_OPERATOR`, `EXCLUDED_AND_CAPPED_AT_ONE`, and
`MATCHES_R_CVA_RECONCILIATION`. For each exhaustive baseline service provide a
stable ID and unit, constant-quality specification, baseline quantity,
baseline revenue, baseline pass-through, derived baseline CVA, derived baseline
CVA unit price, base weight, and year-five operator-controlled quantity. The
three fixed-baseline primitives `baseline_quantity`, `baseline_revenue`, and
`baseline_pass_through` must each be point-identified, with low = base = high;
in schema fields, `range.low = value = range.high`. Do not collapse a ranged
baseline to a point. The year-five quantity may remain ranged. The basket must
reconcile to the same R_cva and pass-through boundary, weights must sum to one,
new demand is excluded, and every quantity relative is capped at one. If that
closed reconciliation cannot be supported, return basket status `MISSING` with
no services. Exclude implementation, valuation, repricing, and contractual
commercial retention.

### Additional outcome-neutral notes

{{SPECIAL_NOTES}}

## Evidence and separation contract

Every critical primitive records method, evidence state, evidence quality,
confidence, source IDs, rationale, caveats, and low/base/high where applicable.

- `DIRECT` requires target-archetype evidence and an observed or safely
  calculated value.
- `PROXY` requires cited evidence and an explicit population, geography,
  period, unit, and business-model bridge.
- `ASSUMPTION` requires method `ESTIMATE`, quality `NONE`, no source claim, and
  a candid bounded judgment; it always makes readiness `UNPROVEN`.
- `MISSING` supplies no invented base or range and always makes readiness
  `UNPROVEN`.

When claiming independent or longitudinal validation, set
`validation_support.independence_basis` exactly to
`validation_source_ids_disjoint_from_primary_support`. Every validation source
ID must be distinct from the endpoint or primary-support source IDs for that
selection. Reusing a primary source as cited context is permitted, but it does
not qualify as independent or longitudinal validation.

Author only the primitive packet. The deterministic finalizer computes V, I,
C, B, P, the aggregate, evidence readiness, and the operating-value viability
cross-check `h`. Still provide the primitive separation attestations needed to
reproduce `h = sum(r_t * c_t * w_t) - k0 - sum(k_t * w_t)` independently for
low, base, and high scenarios. A nonpositive h is a deterministic economic
gate, never an evidence-quality judgment.

For explanation only, the finalizer does not mechanically combine marginal I,
C, and h supports: all three share one feasible realization schedule. For each
downside or upside endpoint bundle, it enumerates at most 32 distinct box vertices
of the five-year r interval box and projects them to
`A = sum(r_y * w_y)` and `N = sum(r_y * c_y * w_y)`. Their convex hull is
sufficient because I, C, and h depend on r only through `(A,N)`. On every hull
edge, it evaluates vertices, stationary candidates of the I*C product,
intersections with every I/C floor, aggregate cut, and h=0, plus one
representative in each resulting edge interval. The lower decision tier uses
worst c/k/other-factor endpoints and the upper attainable tier uses their best
endpoints. Exact marginal C vertex extrema remain display diagnostics, but no
verdict or action may use incompatible low-I/low-C or high-I/high-C bundles.
Do not reproduce this scoring, calculate any endpoint, or author a verdict or
action; supply only the required primitives and attestations.

## Final self-check

Before returning JSON, verify exact schema and runtime identity; all
pinned digests; fixed archetype and value basis; source-ID closure; distinct
employee and contractor cost IDs; unit role-weight sum; documented
pass-through removed exactly once; recognized-revenue accounting basis;
independent-validation source disjointness and exact independence basis;
ordered per-year ranges; unconstrained-across-years r paths;
nonnegative k values; separate c schedules; separate sale-availability,
access/win, deal-capacity, integration-capacity, and price channels; exact
typed capacity derivations and scopes; one canonical entry-equivalent
six-dimension y5 state and digest; a digest-bound closed anchor basis; only
closed nonpositive P adjustments and exclusions; an exhaustive fixed-base
Laspeyres CVA basket with point-identified baseline primitives; no
P/C/survival double count; h
reproducibility; and honest ASSUMPTION/MISSING readiness mapping. Return JSON
only.
