# v4 isolated Sol publication-review brief

Run exactly as `gpt-5.6-sol` under prompt version `validator-4.0`. Review one
exact packet, finalized record, and memo without reading prior reviews or
golden conclusions. Do not edit research artifacts.

First verify schema, identity/model route, deterministic dataset/roles, fresh
finalization and memo equality, arithmetic, range monotonicity, readiness,
gates, and artifact digests. A failure is `invalid`.

Then reopen every registered score-driving source and evaluate both ends of
each material input range. Confirm:

- the named target archetype matches the cited evidence and adjusted target
  coverage rather than silently using the whole NAICS pool;
- DIRECT/PROXY/ASSUMPTION/MISSING is honest;
- missing private data is not disguised as a measured low value;
- 24-month retained savings is distinct from mature operator survival;
- deal evidence does not inflate V or A;
- buy/exit ranges support M without assuming platform-quality exits for
  undifferentiated targets;
- the narrative, ranges, survival class, score, readiness, and action cohere.

Return `publishable`, `publishable_with_caveats`, `reject`, or `invalid`.
Reject only when a material defect could change an input range, readiness,
survival gate, score interval, action, or thesis, and state that causal effect.
An honestly `UNPROVEN` result is not a rejection. Bind the review to exact
packet/run/memo SHA-256 digests and validate against
`review_record_v4.schema.json`.
