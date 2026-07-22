# Continuation prompt: practical v4 implementation

> **Historical:** preserved handoff prompt; do not use for current work. See `README.md` for the v5 governing documents.

Continue the roll-up attractiveness project from the current repository state.

The authoritative design is `V4_3_METHODOLOGY.md`. Read it together with
`V4_2_REJECTION.md`. Keep the economic methodology; do not redesign or tune it
after seeing results.

## Objective

Implement the smallest practical v4 scoring workflow, validate it on five
industries, and stop for review before rerunning Phase 4.

## Hard scope limits

- Work in normal task mode, not goal mode.
- Reuse the existing v3 data, research, and Phase 4 conventions wherever
  possible.
- Do not build a new campaign-governance framework, cryptographic claim system,
  signed freeze process, holdout program, remediation protocol, or agent fleet.
- Do not create tags, branches, commits, PRs, or deployments unless explicitly
  requested.
- Prefer one implementation path and ordinary tests. Use at most three
  subagents, and only for clearly independent analysis.
- Treat missing evidence as unknown, never as measured zero.
- Do not alter thresholds or anchors in response to canary outcomes. Correct
  implementation errors only; report methodology concerns instead of silently
  tuning them.

## Required workflow

### 1. Minimal implementation

Implement only what is required to calculate and explain v4 results from the
repository's existing data. Keep the code small and inspectable. Add focused
tests for:

- unknown versus measured-low evidence;
- bounded elicited assumptions for C and D;
- empirical-anchor requirements for H and F;
- deterministic factor aggregation and verdict calculation;
- reachable verdict tiers under valid synthetic inputs;
- no NaN, invented zero, or silent fallback behavior.

### 2. Five-industry canary

Run exactly these five industries:

- 238220 — Plumbing, Heating, and Air-Conditioning Contractors
- 541214 — Payroll Services
- 541511 — Custom Computer Programming Services
- 541512 — Computer Systems Design Services
- 541930 — Translation and Interpretation Services

For each industry, report one compact row containing:

- H, C, D, F and overall score/range;
- verdict and any confidence cap;
- evidence state for each factor: empirical, elicited, mixed, or missing;
- the principal positive driver and principal gating weakness.

Also show the v3 result beside v4 when available. Explain surprising differences
from evidence and formulas, not from desired rankings.

### 3. Acceptance review

Assess the canary against these predeclared questions:

- Are upper verdict tiers mathematically reachable?
- Does unknown evidence remain distinct from adverse evidence?
- Do the five industries show meaningful factor dispersion rather than blanket
  compression or blanket inflation?
- Are payroll and the two computer-services industries differentiated for
  economically intelligible reasons?
- Is any verdict driven mainly by unsupported elicitation?
- Are rankings stable under each record's stated low/base/high bounds?

Give an honest recommendation: accept, revise for a named structural defect, or
reject. Do not start the full Phase 4 rerun. Stop and ask the user to approve the
five-industry results.

### 4. After explicit approval only

Rerun the existing Phase 4 universe with v4, preserving the existing membership
and source data. Write v4 outputs separately so v3 remains available for
comparison. Validate completeness, schema consistency, tier distribution,
missing-evidence counts, and the three requested industries. Update the local
`6digit` dashboard only after the data pass those checks.

## Deliverables before the approval pause

- minimal v4 implementation and focused tests;
- five canary result artifacts;
- a concise v3-versus-v4 comparison table;
- a clear acceptance recommendation and any unresolved risks.

Lead with results. Keep operational ceremony proportional to this screening
tool.
