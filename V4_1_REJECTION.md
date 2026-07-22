# v4.1 Methodology Rejection Record

> **Historical:** preserved v4 development record; v5 supersedes this line of work.

**Decision date:** 2026-07-21

**Decision:** reject v4.1 before any research run as a publication or campaign
instrument; preserve the frozen v4.1 methodology, thresholds, scoring code,
schemas, prompts, specifications, tests, manifests, and other development
artifacts as immutable diagnostics.

This was an outcome-blind, pre-run decision. At the audit and rejection point,
no v4.1 research packets, finalized runs, memos, or reviews existed, and none
had been viewed. No named industry's score, rank, verdict, color, movement from
v4.0, or expected result motivated the change. The decision rests only on the
preregistered outcome-independent change triggers in section 13 of
`V4_1_METHODOLOGY.md`.

## 1. Validated change triggers

### Construct contradictions

1. **V is not invariant to economically irrelevant gross-versus-net revenue
   presentation.** V divides removable employee and contractor cash cost by
   revenue without a frozen normalization for product resale, reimbursable
   expenses, or other pass-through billings. Two operators with the same
   service gross profit, labor opportunity, and EBITDA can therefore receive
   different V values solely because one reports a product or third-party cost
   gross and the other reports it net. This is a systematic downward distortion
   for project-led systems integrators with material hardware or software
   resale relative to cleaner service-revenue models such as custom programming
   or payroll. The prompt's discussion of pass-through does not repair V's
   denominator.

2. **I excludes valid negative implementation states that its own definition
   includes.** Each `rt` is defined after AI/vendor cost, change cost, workflow
   feasibility, and execution loss, but every annual value must be between zero
   and one and the schedule must be nondecreasing. A migration or transformation
   can have year-one net cost greater than that year's gross removable savings.
   For example, gross removable savings of 10 per year, year-one implementation
   cost of 30, and no later implementation cost imply the normalized schedule
   `[-2, 1, 1, 1, 1]`. At the frozen 10% discount rate its normalized I score is
   approximately 2.8055. v4.1 cannot represent it and floors the schedule to
   `[0, 1, 1, 1, 1]`, scoring approximately 7.6018. The distortion is generous
   precisely where payroll migrations, systems integration, or custom-delivery
   tooling require large upfront change expenditure. The monotone constraint
   also excludes supported later operating deterioration.

3. **B measures offered supply while claiming executable acquisition runway.**
   `N5` counts target-archetype firms plausibly available for sale and expressly
   excludes buyer competition on the premise that competition is reflected in
   entry price. Entry price is conditional on winning a transaction; it does not
   measure the probability of winning, seller preference, auction rationing,
   search capacity, or the number of acquisitions one sponsor can execute.
   Consequently, a crowded sale market can retain a high B even when an entrant
   can acquire few targets. The result is structurally generous to crowded
   sectors, including a plausible full-service payroll roll-up, rather than a
   measure of executable five-year runway.

4. **The terminal-multiple construct lacks a required separation from C and
   survival.** C properly assigns price retention and the survival gate assigns
   operator-controlled paid-demand volume. P, however, does not require the
   year-five downside multiple to be conditioned on the same year-five operating
   state or to attribute multiple compression only to residual post-year-five or
   otherwise unscored risk. The research prompts invite deterioration in growth,
   recurring mix, competitive intensity, vendor dependence, and customer
   concentration as downside-multiple rationales. The same platform or AI
   mechanism can therefore reduce C, reduce survival, and reduce P without a
   reconciliation. Those can be three real financial channels, but v4.1 has no
   control requiring them to be distinct rather than repeated descriptions of
   one impairment.

These defects satisfy the preregistered `construct_contradiction` trigger.

### Frozen review or evidence-contract failures

5. **C has no frozen temporal estimator.** C is one scalar share of realized
   savings, but neither the methodology nor the common prompt defines whether
   it is a year-one, year-five, contract-cycle, arithmetic-average, or
   present-value-weighted five-year measure. It therefore cannot be applied
   comparably beside discounted five-year I. The ambiguity is material across
   time-and-materials and rebid custom programming, project-led systems design,
   and recurring payroll contracts with renewal and annual repricing cycles.

6. **The survival gate has no frozen demand unit.** “Share of baseline demand”
   does not specify whether the numerator and denominator use client logos,
   projects, labor hours, service transactions, employees or pay runs processed,
   or a constant-price quantity index. These measures can move differently even
   when price and margin are excluded as required. The ambiguity is material
   because survival is a cliff gate rather than a continuously weighted factor.

7. **The publication review cannot reliably prevent terminal double counting.**
   It requires separation of I, C, and survival and a consistent P downside
   definition, but it does not require a joint five-year scenario or an
   attribution bridge reconciling C, survival, year-five EBITDA, and the
   downside exit multiple. The construct overlap in item 4 therefore cannot be
   resolved reproducibly by the frozen review contract.

These defects satisfy the preregistered
`frozen_review_or_evidence_contract_failure` trigger.

### Schema, scoring, or reproduction mismatch

8. **The documented PROVISIONAL assumption state is unreachable through the
   executable evidence contract.** The methodology says a critical
   `ASSUMPTION` produces PROVISIONAL readiness when no UNPROVEN condition is
   present. The finalizer requires an `ASSUMPTION` to use `NONE` evidence
   quality, while the methodology and scorer make any critical `NONE` input
   UNPROVEN. The thresholds retain `assumption_status: PROVISIONAL`, but a valid
   finalized assumption cannot reach it. Economic values remain separate from
   labels, yet the readiness ladder and consequent action/publication semantics
   do not reproduce the written contract.

This defect satisfies the preregistered
`schema_scoring_or_reproduction_mismatch` trigger.

No named outcome was used to assert a mathematical or monotonicity failure,
and the preregistered evidence-infeasibility condition was not tested or
invoked because no v4.1 research run occurred.

## 2. Components retained as sound diagnostics

The rejection is not a claim that every v4.1 component failed. The following
features remain useful design inputs for v4.2:

- evidence state does not change economic inputs, factor values, gates, or
  verdicts;
- V distinguishes removable cash cost from automatable task time;
- the I discounting formula is deterministic for schedules inside its stated
  domain;
- C excludes implementation cost and paid-demand volume;
- P uses the weaker of absolute entry affordability and downside multiple
  retention and gives no credit for expansion;
- the geometric mean and explicit weak-link floors prevent a very high factor
  from fully compensating for a structural failure elsewhere;
- the survival gate is economically separate from factor provenance, and its
  published boundary behavior is deterministic;
- missing pivotal inputs receive no neutral base, while endpoint economics can
  still identify an invariant verdict;
- the sensitivity range is correctly described as a partial-identification
  envelope rather than a statistical interval;
- economic verdict, evidence readiness, publication review, and final action
  are conceptually separate;
- largest-base archetype selection, stable tie-breaking, uncertainty flags,
  and widened ranges prevent outcome-selective archetype choice; and
- the one-record rule correctly limits the estimand to the named modal
  archetype rather than the entire NAICS industry.

The last point is also a scope limitation: a modal custom-application developer
or project-led systems integrator is not necessarily the best roll-up archetype
inside its NAICS. That is not a v4.1 failure under the stated estimand, provided
the record is never presented as a whole-industry or best-opportunity score.
Likewise, B's unweighted target count ignores the tenfold EBITDA span inside
the target band; that is a disclosed limitation secondary to the more basic
offered-supply versus executable-runway contradiction above.

The frozen strong-factor floors remain interpretable diagnostics. They require
at least 10% gross removable cash cost as a share of the chosen revenue
denominator, 40% discounted operational realization, 40% commercial retention,
approximately 11 five-year available targets, and P conditions equivalent to
entry at no more than 10x with at least 70% downside multiple retention. These
are demanding rather than generically generous thresholds, but sound threshold
anchors cannot cure an invalid input construct.

## 3. Required v4.2 remediation

A separately versioned v4.2 instrument must, before any research outcome is
viewed:

1. define a cross-industry V denominator that excludes or normalizes product
   resale, reimbursable expenses, and pass-through billings, with a reproducible
   gross-versus-net accounting bridge;
2. represent implementation cash costs and timing without truncating valid
   negative annual net realization, either by allowing negative annual values
   or by modeling implementation cash flows separately and clamping only the
   final factor score;
3. define C on the same five-year temporal basis as I, preferably as an
   explicit annual retention schedule or a frozen present-value-weighted
   estimator;
4. redefine B as expected executable acquisition runway, distinguishing target
   supply from acquirer win/access probability and execution capacity while
   avoiding a second price penalty;
5. prescribe an archetype-specific, price-free demand quantity unit or a
   general constant-price quantity-index rule for survival;
6. require one coherent joint scenario that reconciles C, survival, year-five
   normalized EBITDA, and P, with explicit attribution of any terminal multiple
   compression to mechanisms not already scored or to distinct post-year-five
   risk;
7. make assumption evidence-state, evidence-quality, readiness, and action
   rules mutually reachable and identical across the methodology, thresholds,
   schemas, finalizer, scorer, reviewer, and tests;
8. retain the sound v4.1 sentinels and add synthetic cases for gross/net
   pass-through invariance, negative implementation cash flow, renewal timing,
   crowded-buyer acquisition access, survival-unit consistency, terminal
   attribution, and reachable readiness states; and
9. create and freeze the complete v4.2 artifact set and a newly salted
   deterministic holdout before issuing any prompt.

Thresholds must not be tuned to obtain a desired named result. Any new
threshold remains subject to outcome-independent economic justification and
the new frozen sentinels.

## 4. Preservation and replacement

No v4.1 artifact is deleted, rewritten, relabeled as v4.2, or silently
re-finalized. The frozen methodology, thresholds, scoring code, schemas,
prompts, specifications, tests, manifests, and authorization artifacts remain
preserved with their original identities and digests. If any v4.1 output is
later materialized for mechanical diagnosis, it is development-only and may
not be used for publication, campaign acceptance, threshold calibration, or a
claim that v4.1 was valid.

v4.2 must be a new instrument. This rejection does not reinterpret v3, v4.0,
or v4.1 artifacts, and it does not authorize any change in place to
`V4_1_METHODOLOGY.md`, v4.1 code, or v4.1 data.
