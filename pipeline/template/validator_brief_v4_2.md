# v4.2 isolated publication-review brief

Review exactly one manifest-bound packet, finalized record, and memo using the
required reviewer model and prompt version. Require the neutral execution kind
`target`. Do not seek orchestration metadata, expected outcomes, prior reviews,
or another research artifact. Do not edit research or generated artifacts.

First verify schemas; exact model, run, prompt, specification, methodology, and
dataset identity; all pinned paths, byte lengths, and digests; fresh
finalization and memo equality; deterministic arithmetic; intervals; readiness;
h; gates; action; and verdict. Any deterministic failure is `invalid`.

Then reopen every registered score-driving source and review the base plus both
ends of every critical range. Return exactly one input review for every required
critical path. Confirm:

- the selected archetype follows objective enumeration and count arithmetic;
- archetype uncertainty preserves one primary record, makes no industry-wide
  claim, widens relevant uncertainty, and maps readiness to `UNPROVEN`;
- controllable value-added reconciles recognized revenue and only documented
  pass-through, recognized revenue uses the closed
  `ACCRUAL_RECOGNIZED_REVENUE` / `TRAILING_TWELVE_MONTHS` accounting-basis
  object, its `pass_through_presentation` equals the reconciliation basis, and
  no cost is also used in V's numerator;
- the pass-through reconciliation declares the revenue basis, exactly and
  disjointly partitions every pass-through cost ID as included or already
  netted, and carries construct evidence;
- cash-cost IDs are distinct, target-specific roles are source-backed and
  unchanged, and role weights sum to one;
- an assumption value basis is pre-frozen, source-free, unchanged, uses only
  ESTIMATE/NONE roles and bounded ASSUMPTION/NONE packet cash costs and
  removable fractions, never substitutes dataset roles, and forces UNPROVEN;
- r1..r5 realization is separate from nonnegative k0..k5 investment, including
  up-front losses, and both are separate from discounted c1..c5 retention;
- sale availability, buyer access/win, deal execution capacity, integration
  onboarding capacity, and paid price remain distinct; the capacities use
  their exact `DEAL_EXECUTION` and `INTEGRATION_ONBOARDING` types, closed
  horizon and `MAXIMUM_TARGET_COUNT` / `NON_DUPLICATIVE_TARGET_COUNT`
  calculation, and exact buyer/horizon/geography/archetype/onboarding scope;
- P binds one canonical digest for an entry-equivalent six-dimension state,
  binds the `ENTRY_EQUIVALENT_COMPARABLE_MULTIPLE_LEVEL` anchor basis to that
  identical digest, uses only the three closed nonpositive adjustment channels
  and complete exclusion map, and does not duplicate C or survival;
- survival is an exhaustive fixed-base Laspeyres CVA service basket reconciled
  to R_cva and pass-through; every baseline quantity, revenue, and pass-through
  is point-identified with low = base = high; it holds baseline CVA unit price
  and quality constant, excludes new demand, and excludes implementation,
  commercial repricing, and valuation;
- h is independently reproduced for low, base, and high from r, c, k, and the
  frozen discount weights before the survival gate;
- joint decision endpoints use one shared feasible r schedule and the exact
  at-most-32-vertex five-year interval-box `(A,N)` convex-hull algorithm, never
  incompatible marginal I/C bundles;
- evidence states, proxy bridges, ranges, and source closure are honest;
- validation source IDs are disjoint from endpoint/primary support IDs whenever
  independence or longitudinal validation is claimed, and `independence_basis`
  is exactly `validation_source_ids_disjoint_from_primary_support`; reused
  primary sources may supply context but do not qualify as independent;
- every ASSUMPTION or MISSING critical input maps readiness to `UNPROVEN`, while
  missing evidence is not presented as measured economic weakness; and
- narrative, primitive attestations, derived outputs, and publication state
  cohere.

Write the completed review to a private temporary repository path, validate it
there, then invoke `pipeline/build/guarded_write_v4_2.py` for artifact kind
`review` with the exact reviewer task path; feed the claim token supplied in
this fork-none task message to the writer through an anonymous FIFO or
Unix-socket FD. Regular files and directories are forbidden credential
endpoints. Never place
the token in a repository file,
envelope, artifact, command argument, log, or response. Direct writes to the
planned review path are forbidden; only the guarded writer may create it.
After an interrupted guarded claim, invoke the same writer with `--recover`
and the same private capability FD. The deterministic recovery protocol accepts
only exact lock-only or identity-valid output-plus-lock state and otherwise
fails without mutation.

Return `publishable`, `publishable_with_caveats`, `reject`, or `invalid`.
Unsupported critical evidence, a false critical-input check, or a material
scope, separation, range, identity, or evidence-state defect cannot receive a
publishable disposition. An honest low-readiness result may be publishable.
Bind the review to the exact artifact and campaign digests and validate it
against `pipeline/build/schemas/review_record_v4_2.schema.json`.
Only a schema-valid `reject` with material findings tied to exact remediable
primitive paths can authorize attempt 2. `invalid` and fatal-mechanics outcomes
terminate the entry and cannot be remediated.
