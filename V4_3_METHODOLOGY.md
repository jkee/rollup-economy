# AI Roll-Up Map — v4.3 Methodology

> **Historical:** superseded v4.3 adapter methodology. The frozen v5 methodology governs the current product.

**Status:** outcome-blind replacement candidate. v4.3 is additive: it does not
alter, reinterpret, or validate a v4.2 artifact. v4.2 met its preregistered
evidence-infeasibility trigger because target-underwriting constructs could not
be bounded reliably with common industry evidence. That failure changes the
decision stage, not a named industry's score, rank, label, or direction.

v4.3 makes Phase 4 a **Stage 1 Industry Opportunity Screen**. Target and buyer
underwriting move to Stage 2. The screen prioritizes where to perform that
underwriting; it is not an investment recommendation, return forecast, or
claim that a representative company exists.

## 1. Decision, horizon, and unit

The Stage 1 unit is one six-digit US NAICS industry plus one explicit
`business_model_lens`. The lens is a falsifiable inclusion rule stated before
economic research—for example, recurring outsourced service providers—and
contains:

- included and excluded activities;
- the customer, revenue model, and delivery model;
- the lower-middle-market (`LMM`) size boundary used for firm counts; and
- a rule for assigning establishments or firms to the lens.

The record never invents an average, typical, or representative company.
Industry statistics remain industry statistics. A lens estimate is a weighted
subset estimate with disclosed coverage and uncertainty, not target data.

The lens may not be chosen because it is attractive. Before H, transfer-
propensity, C, or D research begins, a separately signed `lens_spec` may use
only classification and class-count evidence to partition the industry's LMM
firms into a frozen,
mutually exclusive and collectively exhaustive business-model taxonomy. The
global LMM boundary is the frozen Phase 4 dataset's estimated $1 million–$10
million normalized-EBITDA band; no industry may redefine it. A class is
eligible only when it supplies an externally acquired service,
has a transferable operating entity or contract/customer base, and is not
principally a shell, captive internal unit, or non-control financing vehicle.
The Stage 1 screening lens is always the canonical
`mixed_full_eligible_naics` union of every eligible class. `e` is their summed
share of the full NAICS firm denominator; no favorable niche may be selected.
In every coherent scenario, class counts are nonnegative, sum exactly to `n`,
and use the same taxonomy. Counts determine only `e` and F. H is recomputed
across the eligible union using compensation and receipts; C uses implemented-
benefit numerators and denominators; D uses constant-price service quantities.
Firm-count weighting is forbidden for those constructs unless it is itself a
supported proxy with explicit bridge error. Each class supplies the native
numerator/denominator leaves required for union aggregation. Unresolved class counts may be
protocol-bound elicitation, but they do not permit analyst choice. The
taxonomy, eligibility decisions, merge/split rules, counts, sources, and exact
reuse of those counts in `n/e/F` are claimed before an economic packet can be
issued. The lens stage may access classification/count evidence only and its
artifact schema forbids H, C, D, tiers, scores, prior results, and outcome
hints.

The common horizon is five years from the campaign's frozen observation date.
Stage 1 asks four questions:

1. how much current industry compensation, as a share of receipts, is exposed
   to implementable AI task substitution or avoidable hiring;
2. how many lens-eligible LMM firms are expected to transfer in five years;
3. how much of an implemented gross benefit can be retained commercially; and
4. how much current operator-required, constant-price demand remains in year
   five.

Every published label is a research-priority label. `HIGHEST_PRIORITY` never
means “buy,” and `STRUCTURAL_OUT` never substitutes for target diligence.

## 2. Evidence contract: support is not treatment

Every primitive selection is a closed object with `value`, `low`, `high`,
`range_kind`, `as_of`, `method`, `evidence_state`, `source_ids`, `bridge`,
`support_present`, `treatment_valid`, `rationale`, and `caveats`.

Allowed evidence states, from most local to least local, are:

| Evidence state | Required meaning |
|---|---|
| `OBSERVED_TARGET` | Measured for the named target; forbidden for Stage 1 score-driving inputs and reserved for Stage 2 |
| `DIRECT_INDUSTRY` | Measures the same quantity for the six-digit industry and frozen lens |
| `BRIDGED_PROXY` | Measures a different population or quantity with an explicit, testable bridge |
| `REFERENCE_CLASS` | A disclosed empirical distribution for a prespecified comparable class |
| `ELICITED_ASSUMPTION` | A candid bounded judgment or prior, not presented as observed evidence |
| `MISSING` | No defensible estimate or bounded judgment is supplied |

`support_present` answers whether the cited material supports the stated
numerator, denominator, population, date, and range. `treatment_valid` answers
whether the methodology permits that state and bridge for the construct. The
two fields are assessed independently. A source can exist while treatment is
invalid; a candid elicited assumption can have no empirical support while its
treatment is valid.

The following rules are mechanical:

- In Stage 1, `DIRECT_INDUSTRY`, `BRIDGED_PROXY`, and `REFERENCE_CLASS`
  require at least one source and `support_present=true`. A target observation
  can enter Stage 1 only through an explicit population bridge and is therefore
  `BRIDGED_PROXY`, never `OBSERVED_TARGET` or `DIRECT_INDUSTRY`.
- A proxy requires named source and destination populations, a quantitative
  transformation, its direction, and bounded bridge error.
- A reference class requires an inclusion rule fixed before seeing the focal
  result and reports the focal selection separately from the class statistic.
- `ELICITED_ASSUMPTION` has no source requirement, must be labeled as prior or
  elicitation, and must provide a bounded rationale. It may not claim direct or
  proxy support.
- `MISSING` has null value and no evidentiary range. A scenario stress value may
  be carried separately but is never relabeled as a base estimate.
- An unsupported claim of direct, proxy, or reference-class evidence is a
  publication rejection. Honest `ELICITED_ASSUMPTION` or `MISSING` treatment is
  eligible for `publishable_with_caveats` when mechanics and disclosure pass.

The Stage 1 state/range/null truth table is closed:

| State | Numeric fields | Range kind | Sources | `support_present` | `treatment_valid` when otherwise conforming |
|---|---|---|---|---|---|
| `DIRECT_INDUSTRY` | finite `low <= value <= high` | `PREDICTIVE_80` or `SUPPORTED_BOUND` | nonempty | `true` | `true` |
| `BRIDGED_PROXY` | finite `low <= value <= high` | `PREDICTIVE_80` or `SUPPORTED_BOUND` | nonempty | `true` | bridge-dependent |
| `REFERENCE_CLASS` | finite `low <= value <= high` | `PREDICTIVE_80` or `SUPPORTED_BOUND` | nonempty | `true` | class-dependent |
| `ELICITED_ASSUMPTION` | finite `low <= value <= high` | `ELICITED_BOUND` | empty | `false` | protocol-dependent |
| `MISSING` | `value=low=high=null` | null | empty | `false` | `true` |

For `MISSING`, `bridge=null`; for a nonproxy state, `bridge=null`; and for a
proxy the bridge is a closed object. For every nonmissing selection, `value`
is exactly the base-scenario primitive before dependency transforms. No other
combination is valid.

Citation count, prose confidence, and model self-assessment never promote an
evidence state. Absence of evidence is never scored as adverse economic
evidence.

### 2.1 Frozen elicitation protocol

`ELICITED_ASSUMPTION` is not free-form analyst discretion. Before any focal
economic packet is issued, `pipeline/v4_3/elicitation_protocol.json` freezes a
closed questionnaire and global ordinal lookup tables for task exposure,
implementation complexity, lens eligibility, transfer propensity, contract
benefit intensity/retention, demand durability, and operator requirement. A
table may contain a broad `evidenced_heterogeneous` row only when sources
affirmatively establish a mixed population. Epistemic unknown is `MISSING` and
has no numeric base; it never maps to a pessimistic, neutral, or attractive
category. Lookup rows, endpoints, minimum
widths, and monotonic order are scorer-consumed threshold IDs.

For each elicited leaf or inseparable constrained bundle, three independent
fork-none research sessions receive
only the lens specification, allowed evidence, questionnaire, and lookup table;
they cannot see factors, tiers, prior versions, or other assessors. The base
category is the ordinal median of their three selections. The low endpoint is
the lowest selected category's low endpoint and the high endpoint is the
highest selected category's high endpoint, widened to the table's minimum
width. For simplex or accounting bundles, the table supplies complete
constraint-preserving vectors; medians and hulls operate on bundle IDs, never
independently on leaves, and require weights to retain their exact sums. Each
assessor supplies a reason code, not a numeric value. The packet
binds all three blinded receipts. A source-backed value uses the appropriate
empirical state instead and may not be blended with elicitation unless a global
blend rule was frozen before the campaign.

Canary and holdout acceptance additionally require at least one valid
`DIRECT_INDUSTRY`, `BRIDGED_PROXY`, or `REFERENCE_CLASS` score-driving leaf in
each of H, F, C, and D. No factor may pass on elicitation alone. Elicited inputs
can make a complete model-conditioned screen and rank, but the action remains
`VALIDATE_ASSUMPTIONS`.

## 3. Ranges, domains, and coherent scenarios

Supported nonmissing inputs supply `low <= base <= high`. A range must declare
one of:

- `PREDICTIVE_80`: a calibrated central 80% predictive interval (10th,
  50th, and 90th percentiles, except a disclosed discrete median convention);
- `SUPPORTED_BOUND`: empirically bounded endpoints without a probability
  interpretation; or
- `ELICITED_BOUND`: a bounded judgment or prior.

A predictive interval is not the construct's semantic domain. Semantic domains
are used only for missingness ablation, never as empirical uncertainty:

| Primitive | Semantic domain |
|---|---:|
| receipt ratio `l` | [0, +infinity) |
| shares `a`, `rho`, `e`, `s5`, `q`, `o` | [0, 1] |
| eligible LMM firm count `n` | [0, +infinity) |
| constant-price demand ratio `d5` | [0, +infinity) |

The admissible-joint-state language is finite and closed. Every primitive
belongs to one `uncertainty_bundle`; each bundle enumerates complete endpoint
vectors with stable state IDs. Shared denominators, simplex weights, and
correlated quantities must live in the same vector. The admissible set is the
Cartesian product of bundle states after exact equality/inequality constraints
from the frozen grammar are applied, with at most 256 resulting states.
Arbitrary formulas, correlations, analyst filters, numerical optimization, and
tolerances are forbidden. The numeric engine is Python's frozen `decimal`
implementation using `Context(prec=50, rounding=ROUND_HALF_EVEN)`; `ln` and
`log10` use that context. Primitive decimal values remain exact. Each derived
H/F/C/D value is first computed from primitives and quantized once to `1E-12`
with `ROUND_HALF_EVEN`. A and L are then computed from those quantized factors
and themselves quantized once to `1E-12`. Tier comparison, K ordering,
serialization, and ranking use only those canonical values. Cuts are exact at
the quantized value; no epsilon or platform float is permitted. A sentinel covers
values immediately below, at, and above every cut after quantization.

`base` is the Cartesian product of each bundle's declared base state. Define
the exact outcome key `K=(tier_ordinal,A,L)`, compared lexicographically with
tier first, then the quantized A, then the quantized L. Named `low` and `high` are the
admissible states attaining minimum and maximum K, with canonical state-ID
tie-break. Mechanical scoring recomputes every factor from every complete
state. For H, F, C, D, A, L, and K, publish separate attainable minima/maxima
and witness state IDs; one aggregate witness need not attain every coordinate
extreme.

The published envelope is the exact finite admissible set, not three
analyst-selected points. Additional semantic stress bundles can widen but never
narrow the evidence-supported set. All comparisons use the frozen quantized
values; coarser display rounding happens last.

If an input is `MISSING`, no base factor or base aggregate is fabricated.
Semantic-domain ablation may establish a stable structural conclusion or show
that the output is unbounded. A bounded elicited value can generate a model-
conditioned base and rank, but it cannot generate a target action.

## 4. Frozen Stage 1 inputs

All inputs are specific to the frozen NAICS, lens, geography, horizon, and data
vintage.

The threshold contract freezes one primitive dependency DAG. Evidence objects
attach to score-driving leaves—benefits conversion, occupation weights, task
exposure, implementation category, class counts, transfer propensity, contract
mix, benefit intensity, annual retention, demand, and operator requirement—not
only to the composites `l/a/e/q`. Composite evidence state is mechanically the
weakest valid dependency state, with every proxy bridge retained. One source
may support multiple leaves only when each distinct numerator, denominator,
population, and channel is registered; reuse never upgrades independence.

Normalization preserves source anomalies and separates them from absence.
Values above one, including the frozen 541618 compensation/receipts anomaly,
remain raw and are not silently clamped before H. A stored zero whose provenance
states that no series exists—specifically the legacy 541120 firm-count gap—is
normalized to `MISSING`, not economic zero. Exact-zero economics requires an
affirmative measured-zero source. Sentinels bind both cases.

### 4.1 Implementable labor opportunity

- `l` is the public-data compensation-to-receipts ratio: employee wages plus a
  frozen benefits conversion, divided by industry receipts on the declared
  vintage. It is a broad industry proxy, not target cash cost or controllable
  value-added revenue. Any ancestor-NAICS, vintage, establishment/firm, lens, or
  contractor omission is an explicit bridge and widens the range. Controllable
  contractor cost and third-party pass-through are not estimated in Stage 1.
- `a` is the wage-weighted share of current, not-yet-automated tasks exposed to
  AI substitution or avoidable hiring. Occupation exposure is joined to the
  lens's occupation mix;
  a generic “AI exposure” score is not `a` without a documented calibration to
  removable task share.
- `rho` is the five-year implementation haircut: the share of exposed task
  opportunity expected to become operationally implementable after workflow,
  quality, compliance, adoption, and change constraints. It excludes pricing
  retention, demand loss, valuation, and market-wide diffusion.

The gross technical labor-opportunity proxy is `x = l * a * rho`. Because its
denominator is receipts rather than target CVA, it is used only for Stage 1
relative screening and may not be quoted as EBITDA uplift or target savings.

### 4.2 Five-year transferable-firm opportunity

- `n` is the estimated number of firms, not establishments, inside the frozen
  LMM boundary. Multi-establishment firms are deduplicated. A modeled firm
  conversion from establishment data is disclosed.
- `e` is the share of those firms eligible under the prespecified business-
  model lens.
- `s5` is the probability an eligible firm undergoes a qualifying control
  transfer during the next five years. Deaths without transferable operations,
  internal reorganizations, and non-control financings are excluded.

`n * e * s5` is an expected opportunity count, not a claim about buyer access,
win rate, integration capacity, or a specific target. Those belong in Stage 2.

### 4.3 Five-year commercial retention

`q` is the raw discounted five-year commercial-retention share of an
implemented gross benefit. It is derived from a mutually exclusive and
exhaustive contract table. For contract class `j` and year `t`, let `m_jt` be
its value-added revenue weight, `b_jt` its gross implemented-benefit intensity
per dollar of value-added revenue, and:

`B_t = sum_j(m_jt * b_jt)`

`g_jt = m_jt * b_jt / B_t`

be its share of implemented gross benefit. Require `sum_j(m_jt)=1`,
`sum_j(g_jt)=1` whenever `B_t` is positive, and nonnegative `b_jt`. Let `q_jt`
be the share of that class's implemented benefit retained
after contractual pass-through, renewal repricing, customer sharing, and price
competition, conditional on service quantity. Volume loss, self-service, and
operator displacement belong only in `d5`/`o`. Require `0 <= q_jt <= 1`.

With `w_t = 1/(1.10)^t`:

`retained_t = sum_j(m_jt * b_jt * q_jt)`

`q = sum_(t=1..5)(w_t * retained_t) /
     sum_(t=1..5)(w_t * B_t)`

If the aggregate denominator is exactly zero, set `q=0`; if any required
`m_jt`, `b_jt`, or `q_jt` is missing such that the ratio cannot be constructed,
`q` is missing. A zero-benefit year contributes zero to both numerator and
denominator and therefore does not reduce retention.

Contract migration can be represented only through coherent year-specific
`m_jt`, `b_jt`, and `g_jt` arrays. Revenue weights may proxy benefit weights only
under an explicit equal-benefit-intensity bridge with bounded error. The
undiscounted revenue and benefit weights, annual retention schedule, and raw
`q` are published. Stage 1 `q` is preserved for screen disclosure and
benchmarking only. It may enter Stage 2 solely as an explicitly bridged proxy
and never as a target observation or substitute for `q_target`.
Implementation belongs in `rho` or Stage 2 `I`; demand belongs in `d5`; neither
may be deducted again in `q`.

### 4.4 Year-five operator-required demand

- `d5` is the year-five to current ratio of constant-price, constant-quality
  demand for the current service basket. Price, new services, and acquisition
  growth are excluded.
- `o` is the share of that year-five service quantity still requiring an
  accountable operator of the kind covered by the lens, rather than being
  eliminated, self-served, or supplied entirely by software.

`d5 * o` is capped only when scored. A growing market may have `d5 > 1`.
Pricing effects belong only in `q` and may not also reduce `d5` or `o`.

## 5. Four Stage 1 factors

Let `clamp(z,a,b) = min(b,max(a,z))`. Each factor is a continuous float on
0–10.

### H — implementable labor opportunity

`H = 10 * min(1, l * a * rho / 0.25)`

Thus gross technical compensation opportunity equal to 0%, 5%, 12.5%, 20%,
and at least 25% of industry receipts scores 0, 2, 5, 8, and 10. The 25%
receipts anchor is exceptional technical exposure, not CVA, EBITDA uplift, or
expected net savings.

### F — transferable-firm opportunity

`F = 10 * clamp(log10(1 + n * e * s5) / log10(501), 0, 1)`

Zero expected transfers scores 0 and 500 or more scores 10. The logarithm
acknowledges diminishing screening value from additional candidates. It does
not encode buyer-specific executability.

### C — commercial retention

`C = 10 * min(1, q / 0.50)`

Raw retention of 0%, 10%, 25%, 40%, and at least 50% scores 0, 2, 5, 8, and
10. Fifty percent discounted five-year retention is an exceptional anchor.
The cap never changes raw Stage 1 `q`; Stage 2 independently computes
`q_target`.

### D — durable operator-required demand

`D = 10 * clamp(d5 * o, 0, 1)`

The product is the surviving quantity share of today's accountable service.
Demand growth cannot score above 10.

## 6. Aggregate, tier interval, and rank

For each coherent scenario compute:

`A = (H + F + C + D) / 4`

`L = min(H, F, C, D)`

Assign the first matching tier in descending order:

| Stage 1 research-priority tier | A cut | L cut |
|---|---:|---:|
| `HIGHEST_PRIORITY` | >= 7.5 | >= 6 |
| `PRIORITY` | >= 6.0 | >= 4 |
| `CONDITIONAL` | >= 4.5 | >= 2 |
| `LOW_PRIORITY` | >= 3.0 | >= 1 |
| `STRUCTURAL_OUT` | otherwise | — |

`A` rewards breadth while `L` discloses the weakest dimension. The pair avoids
the geometric-mean-plus-floor double punishment of a thin factor.

Each industry record publishes its finite attainable K set, base K, per-output
bounds, and witnesses. A `robust_tier` exists only when all admissible states
have the same tier; otherwise publish the ordinal
`tier_interval=[lowest_attainable, highest_attainable]`. Missingness ablation
may widen the tier interval but may not create a base tier. Industry records do
not contain fleet rank metadata.

After every industry record has a final accepted isolated review, a separate
signed fleet aggregation computes display rank lexicographically by:

1. robust lower tier, highest first;
2. base `A`, highest first;
3. base `L`, highest first; and
4. six-digit NAICS, ascending, solely as a deterministic tie-break.

For an interval result, “robust lower tier” is the lowest attainable tier.
Records without a base score sort after bounded records in that lower tier and
then by ascending NAICS. For records `i` and `j`, `i` definitely dominates `j`
only when every admissible full key `(tier_ordinal,A,L)` for `i` is
lexicographically greater than every such key for `j`. Otherwise the pair is
incomparable. The best possible rank for `i` is one plus the count of records
that definitely dominate `i`; the worst is fleet size minus the count that `i`
definitely dominates. Optional overlap groups are maximal cliques and may
overlap; they are navigation aids, not equivalence classes. Rank scope binds
the exact accepted-record and campaign-membership digests.

A distinct fleet reviewer is authorized to inspect the complete accepted set
and reproduces display order, dominance edges, rank intervals, membership, and
record references. It cannot change an industry record, readiness, action, or
publication outcome. The isolated per-record reviewer never sees or reproduces
fleet rank. This separation permits byte-identical accepted holdout records to
be referenced later by the 53-code fleet overlay.

## 7. Readiness, ablation, and action

Readiness reports whether the Stage 1 result can support its next action. It
does not change factor values or tiers.

First compute a **global weak-evidence ablation**. Simultaneously replace every
non-`DIRECT_INDUSTRY` Stage 1 primitive and every inseparable
shared-denominator bundle with its semantic domain. The frozen leaf-to-factor
map projects each affected factor to a conservative closed interval. H, F, and
D use their exact monotone analytic endpoints where available; C and any
nonmonotone/shared ratio default to `[0,10]` unless a certified closed algebraic
bound is registered. The projection uses exact factor cap values 0 and 10; it
never serializes an infinite primitive or solves for a nonterminating decimal.
Dependencies may narrow an interval but are conservatively ignored when their
exact projection is unavailable. The four factor intervals form one
symbolic box. Evaluate its lower and upper factor corners with the canonical
quantized scorer; monotonicity makes them the K extrema. The conservative
attainable tier set is every ordinal tier between those corner tiers, and the
action-category set is their mapped union. This symbolic representation has
constant size, no vertex cap, optimizer, or tolerance, and can only widen—not
falsely stabilize—the result.

Then run one-at-a-time and inseparable-bundle projections only to attribute
which inputs drive the global box. A primitive is `decision_relevant` when its
semantic projection can change the conservative K envelope or screening action
category. This joint global test prevents two individually harmless weak inputs
from appearing harmless when varied together. Ablation is an epistemic stress
envelope, not empirical support and not the finite evidence-supported scenario
set in §3.

Before readiness, map tiers to evidence-neutral action categories:
`HIGHEST_PRIORITY/PRIORITY -> advance`, `CONDITIONAL -> validate`, and
`LOW_PRIORITY/STRUCTURAL_OUT -> deprioritize`. A crossing tier interval carries
the union of its attainable categories.

Readiness is an exhaustive first-match state computed before the final action:

| Readiness | Mechanical meaning |
|---|---|
| `UNBOUNDED` | No complete valid base exists and the global semantic-domain state set itself cannot be constructed or validated |
| `STRESS_TEST_ONLY` | No complete base exists, but the global semantic-domain set yields a valid finite K/action envelope |
| `MODEL_CONDITIONED` | A complete bounded base exists and at least one decision-relevant input is `ELICITED_ASSUMPTION` |
| `PROVISIONAL` | A complete bounded base exists, no decision-relevant input is missing or elicited, and at least one is `BRIDGED_PROXY` or `REFERENCE_CLASS` |
| `SUBSTANTIATED` | A complete bounded base exists and every decision-relevant Stage 1 input is `DIRECT_INDUSTRY`, with valid support and treatment |

Nonrelevant weaker evidence remains disclosed. A complete all-direct result
whose scenarios cross tiers is still `SUBSTANTIATED`; its separate stability
field is `CROSSING`, never silently upgraded to a robust conclusion. A
mechanics error or unsupported claim of empirical support is a publication
defect, not a low-readiness shortcut.

The final action is a total function:

| Readiness | Tier/action condition | Action |
|---|---|---|
| `UNBOUNDED` or `STRESS_TEST_ONLY` | any | `EVIDENCE_FIRST` |
| `MODEL_CONDITIONED` | any | `VALIDATE_ASSUMPTIONS` |
| `PROVISIONAL` or `SUBSTANTIATED` | attainable tiers are a nonempty subset of `{HIGHEST_PRIORITY, PRIORITY}` | `ADVANCE_TO_STAGE2` |
| `PROVISIONAL` or `SUBSTANTIATED` | attainable set contains `CONDITIONAL` or spans multiple action categories | `SELECTIVE_VALIDATE` |
| `SUBSTANTIATED` | attainable tiers are a subset of `{LOW_PRIORITY, STRUCTURAL_OUT}` | `DEPRIORITIZE` |
| `PROVISIONAL` | attainable tiers are a subset of `{LOW_PRIORITY, STRUCTURAL_OUT}` | `SELECTIVE_VALIDATE` |

The rows are mutually exclusive in order and cover every valid record. Exact
sentinels prove that precisely one readiness and one action are produced.

No Stage 1 action authorizes a transaction, valuation, financing, or target
contact.

## 8. Stage 2 target and buyer diligence

Stage 2 is opened only for a named target archetype or company and a frozen
reference buyer. It retains v4.2's target-specific controllable-value-added
boundary, `V`, `I`, executable-and-winnable `B`, operating viability `h`, and
constant-price operator-survival gate. The sole import authority is signed tag
`v4.2-freeze-2026-07-21-8`, freeze root
`1f1fedba7760aad8f4589d40d0f984c7d73359557f3839efa4c2104dc0a475a2`.
The v4.3 freeze validator requires these exact tagged blobs:

| Imported v4.2 artifact | SHA-256 |
|---|---|
| `V4_2_RUNTIME_METHODOLOGY.md` | `7ff396fd9a73b821df8fadabb2abdc235864154cc7257e304a295bcffdac4427` |
| `pipeline/build/thresholds_v4_2.json` | `a6b006ffcd48fc799c905599e427d42a16366f052c474eb22a2a69e1286707d9` |
| `pipeline/build/v4_2_scoring.py` | `a782f8f88d455e14027b13457a7f2cf202424b1c08af17d4ef6952fa39c4f7b7` |
| `pipeline/build/finalize_run_v4_2.py` | `c2f1c71b652196821f24bb4aa23c056b58b03a08943148b3e7fa4c2d24491707` |
| `pipeline/build/schemas/research_packet_v4_2.schema.json` | `7e5683805074d4e545788a9a54d9fcf4da1df2ca97faee77b9c105a0579a3bb5` |
| `pipeline/build/schemas/run_record_v4_2.schema.json` | `6e3d89e9dbdd7657218a3d059618218615a172ae76980a45fe718f098113d39a` |

Only the v4.2 definitions for `R_cva`, `G`, `V`, `I`, `B`, `h`, the fixed-base
survival basket, and their accounting/no-double-count rules are retained.
v4.3 replaces v4.2 `C`, `P`, geometric `S`, factor floors, verdict aggregation,
evidence states, and action mapping with the definitions below. A compatibility
test enumerates every retained and overridden field; unlisted inheritance is
forbidden. Stage 2 must collect target/buyer evidence; Stage 1 industry
estimates do not become target observations.

Stage 2 uses the same evidence states, with this additional valid row:

| State | Numeric fields | Range kind | Sources | `support_present` | `treatment_valid` |
|---|---|---|---|---|---|
| `OBSERVED_TARGET` | finite `low <= value <= high` | `PREDICTIVE_80` or `SUPPORTED_BOUND` | nonempty target sources | `true` | `true` |

The remaining Stage 1 truth-table rows remain available at their stated
readiness. The exact imported v4.2 semantic domains and joint partial-
identification mechanics govern `R_cva`, G inputs, `r1..r5`, `k0..k5`,
`c1..c5`, B inputs, and survival quantities. v4.3 adds positive domains
`buy_mult,exit_mult in (0,+infinity)` and computes C/M/h/survival for every
admissible state. A missing decisive primitive produces no base diligence
verdict. `h<=0` kills only the states where it is established; missing h never
becomes zero. The published diligence verdict is identified only when every
admissible state has the same post-h/post-survival verdict; otherwise it is
`INDETERMINATE` with the full attainable verdict set and
`EVIDENCE_FIRST`. A Stage 1 value may enter Stage 2 only through an explicit
new `BRIDGED_PROXY` or `REFERENCE_CLASS` selection that preserves its industry
population, bridge error, and low readiness; it is never silently copied,
reclassified as `OBSERVED_TARGET`, or used as target fact.

Stage 2 uses five scored factors: `V`, `I`, reanchored `C`, `B`, and `M`.
For target-specific annual operational realization `r_t`, annual commercial
retention `c_t`, implementation investment `k0`, recurring investment `k_t`,
and `w_t=1/(1.10)^t`:

`q_target = sum_(t=1..5)(r_t * c_t * w_t) /
            sum_(t=1..5)(r_t * w_t)`

If the denominator is exactly zero, set `C=0`; if it is missing, `C` is
missing. Otherwise:

`C = 10 * min(1, q_target / 0.50)`

The raw `q_target` is used in economics. The operating-value cross-check
remains:

`h = sum_(t=1..5)(r_t * c_t * w_t) - k0 -
     sum_(t=1..5)(k_t * w_t)`

`h <= 0` is a kill before survival treatment. `h` is in units of one full year
of target gross removable opportunity and is not a sixth factor.

### Stage 2 multiple/price factor

Only Stage 2 may score acquisition price and multiple resilience. With entry
`buy_mult` and downside `exit_mult`, both positive and consistently normalized:

`E = clamp(14 - buy_mult, 0, 10)`

`spread = (exit_mult - buy_mult) / buy_mult`

`R = clamp(3 + 8 * spread, 0, 10)`

`M = min(E, R)`

A flat multiple therefore gives `R=3`. `exit_mult` may exceed `buy_mult` only
for a source-supported, same-vintage structural size or recurring-quality
differential between the acquired add-on state and the frozen exit state. The
uplift must be reproduced from consistently normalized comparables and a
complete exclusion map. Pure market expansion is capped at the flat-multiple
case. Entry and exit evidence must use consistent EBITDA normalization,
service mix, customer concentration, management depth, and accounting policy.
Sponsor reputation, AI benefits, margin expansion, revenue growth, synergies,
and future favorable market forecasts may change operating dollars once, but
may not increase `exit_mult` or be counted again in `M`.

### Stage 2 decision pair and gates

`A2 = (V + I + C + B + M) / 5`

`L2 = min(V, I, C, B, M)`

| Stage 2 diligence verdict | A2 cut | L2 cut |
|---|---:|---:|
| `HELL_YES` | >= 7.5 | >= 6 |
| `STRONG` | >= 6.0 | >= 4 |
| `CONDITIONAL` | >= 4.5 | >= 2 |
| `PASS` | >= 3.0 | >= 1 |
| `KILL` | otherwise | — |

Apply `h<=0` kill first, then the factor decision pair, then the retained v4.2
constant-price survival treatment: at least 0.75 has no cap; [0.50,0.75) caps
at `CONDITIONAL`; [0.25,0.50) caps at `PASS`; below 0.25 kills. Low/base/high
states are coherent, and an identified verdict exists only when all admissible
states agree. This is target/buyer diligence, still not final underwriting.

## 9. Publication review

An isolated reviewer returns `publishable`, `publishable_with_caveats`,
`reject`, or `invalid`. Publication status is independent of tier and
readiness. The reviewer must reproduce primitives, factors, scenario outputs,
tiers, record-local ablations, readiness, action, and every Stage 2 gate when
applicable.

`publishable_with_caveats` is the honest expected treatment for a mechanically
valid record whose elicited or missing evidence is conspicuous and whose action
is properly restricted. Review must reject unsupported claimed direct/proxy
support, an unstated bridge, invented company data, incoherent scenarios,
absence-as-zero, double counting, or a result-derived methodology exception.
`invalid` is reserved for corrupted authority, binding, schema, execution, or
review independence.

Research and review packets bind exact methodology, thresholds, schemas,
prompts, toolchain, source snapshots, model identifiers, run identifiers, and
artifact digests. The reviewer must not inspect other campaign results.
Research and review use distinct issued principals and fork-none sessions.
Reviewer execution inherits no research conversation, cannot be the research
author, cannot communicate with research during review, and receives only one
exact manifest-bound artifact set. Guarded claims and execution receipts make
those separations mechanically auditable.

## 10. Preregistered five-industry canary

The disclosed development canary is exactly these five six-digit codes, in
ascending canonical order:

`238220`, `541214`, `541511`, `541512`, `541930`.

They are development data. Their named score, tier, order, distribution,
color, movement from v4.2, or apparent economic appeal is never an acceptance
condition and may not change an anchor, cut, formula, evidence rule, or gate.

The canary passes only when all of the following hold:

1. every frozen directional sentinel passes;
2. mechanics and isolated reproduction pass for 100% of selected records;
3. all five selected records receive `publishable` or
   `publishable_with_caveats` after at most one bounded remediation per record;
4. no record is `invalid`, and no material construct defect repeats after its
   permitted remediation;
5. every Stage 1 record has a complete bounded base and finite admissible state
   set, with no `MISSING` score-driving leaf; and
6. exact campaign, review, remediation, and operator signatures validate.

Each record also names at most three decision-relevant evidence packages for the
next diligence pass. A package identifies one primitive or inseparable
shared-denominator bundle, its required population/date/quantity, acceptable
evidence states, search endpoints, numeric decision breakpoint, and a
success/failure rule. It may not promise a desired tier. The package list is a
usefulness output, not an escape from the complete bounded-screen requirement.

## 11. Untouched v4.3 holdout and Phase 4 rerun

v4.3 requires a new frozen public salt string. The v4.2 holdout and every code whose v4.2 or
pre-freeze v4.3 economic output was generated or viewed are burned and excluded.
No v4.2 salt, membership, or ranking may be reused.

The cohort derivation is closed. Start with the exact 63-code target universe
in `pipeline/blocks/targets_phase3.json`; remove the five development codes in
§10 and the burned v4.2 holdout codes `541199`, `541340`, `541370`, `541420`,
and `541890`. The remaining exact 53 codes are both the v4.3 holdout-eligible
universe and the final Phase 4 publication cohort, materialized in
`pipeline/v4_3/full_membership.json` with source digests. A code is burned when
any v4.2/v4.3 lens spec, assembled prompt, packet, manual Stage 1 primitive
calculation, factor/tier calculation, record, memo, or review was generated or
viewed outside the authorized sequence. The signed exposure ledger records the
code, artifact kind, first timestamp, task, and digest. Prior v3 publication is
legacy discovery material and cannot train thresholds or priors, but by itself
does not remove a code from this v4.3 universe.

Before selection, freeze the eligible six-digit universe, every exclusion,
the deterministic stratification values, a five-bin rule, the selection
algorithm, and the literal salt `rollup-v4.3-holdout-2026-07-22|` in the signed
manifest. The stratification field is the preexisting raw
`labor_share.value` from `pipeline/datasets/derived/<naics>.json`, ordered
ascending with NAICS tie-break; it is used only for selection. This field is
complete for the cohort and retains 541618 at `1.3991`. The membership artifact
materializes and validates every `(naics,value,sort_key)` before hashing. Split the 53 eligible
codes into five contiguous bins, assigning remainder rows to the earliest
bins, and select from each bin the smallest lexicographic value of:

`SHA256("rollup-v4.3-holdout-2026-07-22|" + naics)`

The five selected codes may be known, but no economic output for them may be
generated or viewed before the authorized holdout run. The manifest
materializes membership and proof before any such output. If five eligible
untouched codes do not exist, v4.3 cannot claim holdout validation.

The holdout uses the same sentinels, mechanics, reproduction, publication,
remediation, evidence-package, and signed operator gates as the canary. It has
no named score, tier, order, or distribution expectation. Any viewed holdout
is burned for later versions.

Only a passing canary and holdout authorize the complete 53-code Phase 4 rerun.
The final publication reuses the five exact accepted holdout records and runs
the remaining 48 codes under the identical frozen toolchain and rules. Any
rejected, invalid, or missing selected record blocks the fleet rank and final
publication; an incomplete 53-code set may be disclosed only as a failed
campaign status report, never as a partial ranking.

## 12. Bounded remediation

Each selected record permits at most one remediation attempt. The reviewer
must identify the original artifact by exact run ID, content digest, JSON
pointer, source ID, and finding ID. The remediation authorization lists the
only permitted leaf paths and binds the correction algorithm, source endpoint,
source population, extraction rule, and deterministic selection rule. An
independent score-blind remediation authorizer maps the review's frozen defect
rule ID to a pre-frozen correction registry and selects the exact source and
algorithm without access to factors, tiers, or score effects. If the registry
has no applicable rule, remediation is unavailable. A separate independent
retriever executes the authorization without seeing scores. Replacing a leaf
with any merely “defensible” value is not authorized.

Attempt 2 is rebuilt from frozen inputs and may differ from attempt 1 only at:

- authorized defective leaves;
- mechanically dependent derived leaves enumerated by the finalizer; and
- hashes, timestamps, and signatures that necessarily bind the new artifact.

A canonical leaf-diff report must prove that no other value changed. Shared
sources may be corrected only for the cited quantity. A correction may not
expand a source's authority to a new population, denominator, date, construct,
or record. Changing a formula, anchor, cut, evidence mapping, scenario policy,
or business-model lens requires a new methodology version. A repeated material
defect, unauthorized diff, or second remediation fails the record.

Remediation is record-local only. Any finding caused by a shared frozen prompt,
schema, scorer, finalizer, lookup table, source-authority rule, lens protocol,
shared source snapshot, shared extraction rule, normalizer, or campaign
component invalidates the campaign and requires a new version; it cannot be
repaired separately in five records. A local source remediation may address
only a distinct registered quantity without mutating a shared snapshot or
affecting another record. Source IDs never expand the
authorized input-path set. Exact references use `path`, `byte_length`, and
SHA-256; correct bytes at an alternate path are rejected.

## 13. Frozen tests and directional sentinels

The freeze manifest enumerates the exact test IDs and SHA-256 digest of every
test file, fixture, expected-output object, and runner. Authorization compares
the exact ID set and digests. It never accepts a hardcoded test count, a
substring match, or “at least N tests.” Unknown, duplicate, omitted, skipped,
or changed IDs fail authorization.

At minimum the exact sentinel set covers:

- every H, F, C, and D zero, midpoint, cap, and monotonic direction;
- F at zero and 500 expected transfers and invariance to buyer-specific inputs;
- C at raw q of 0, 0.25, and 0.50, plus proof that the raw q survives scoring;
- D with market contraction, growth above one, and declining operator share;
- every A/L tier cut and floor immediately below, exactly at, and immediately
  above the boundary;
- coherent low/base/high recomputation and a crossing tier interval;
- missingness without zero imputation, semantic-domain ablation, stable direct
  structural negative, and each reachable readiness/action state;
- support-present versus treatment-valid truth tables, including honest
  elicitation acceptance and unsupported claimed proxy rejection;
- post-review lexicographic fleet ranking, full-K strict dominance, rank
  intervals, byte-identical holdout reuse, and deterministic NAICS ordering;
- Stage 2 flat multiple `R=3`, nonpositive spread, entry-score anchors,
  same-vintage/state enforcement, `h=0`, and every survival cap;
- no change in factors or tiers when numeric values, ranges, and scenarios are
  fixed while one valid nonmissing evidence state and all metadata required by
  its truth-table row change coherently; readiness, action, and publication
  status may change. Separate sentinels
  prove that changing a primitive to `MISSING` removes its base rather than
  preserving the score; and
- exact-reference remediation, permitted dependent-leaf changes, forbidden
  unrelated changes, and forbidden shared-source authority expansion.

Synthetic profiles are mathematical contracts, not desired industry outcomes.

## 14. Freeze and outcome-independent change control

Before any v4.3 economic research, a canonical freeze manifest records this
methodology; the v4.2 evidence-infeasibility decision; thresholds and categorical
mappings; schemas; scorer; finalizer; renderer; campaign and guarded writers;
research and review prompts; exact tests and fixtures; deterministic datasets
and vintages; canary membership; v4.3 holdout eligibility, exclusions,
stratification and salt commitment; exact model IDs; and change-control rules.

For each file record repository-relative path, byte length, and SHA-256. The
root digest is SHA-256 of UTF-8 lines
`path + NUL + byte_length + NUL + file_sha256 + LF`, sorted bytewise by path.
Canonical JSON uses sorted keys and no insignificant whitespace.

Commit the complete set, record the commit ID, create a signed annotated tag
containing the root digest, and publish an externally timestamped CI or release
artifact before any v4.3 result exists. Every numeric constant and categorical
mapping is owned by one closed contract namespace. The scoring contract
contains only scorer-consumed formulas, anchors, domains, tier cuts, and lookup
tables; the scorer rejects unknown or unused IDs within that namespace.
Campaign, governance, test, membership, salt/date, and hashing constants have
separate closed schemas and validators that likewise reject unknown or unused
IDs within their own namespaces. NAICS codes, dates, campaign counts, byte/hash
conventions, and examples are never forced into the scorer. A self-declared
`frozen` field is not authorization.

After freeze, a change is permitted only for a documented mathematical or
directional error, construct contradiction or double count, schema/scoring
mismatch, publication/evidence-contract failure, or preregistered evidence
infeasibility. Named scores, ranks, tiers, colors, distributions, movements,
or desired business conclusions are never valid reasons to change v4.3. Every
attempt and rejection is preserved. A replacement requires a new version, new
salt, and new untouched holdout.
