# v5.1 campaign incident — researcher session reuse

**Detected:** 2026-07-22
**Status:** resolved by Victor's direct waiver on 2026-07-22
**Affected checkpoint:** S1 publication at `d99208f`

## Incident

S1 research wave 1 used ten fresh, one-code researcher sessions. For
orchestration efficiency, those same agent threads were then given new codes
through follow-up turns for waves 2–5. Each packet still had one author and
passed `validate`, `finalize`, and `check`, but the thread reuse violates the
binding requirement that every code be researched in an independent,
single-purpose session.

The affected surface is 39 of S1's 49 records: all records committed in
research-wave commits `fbb4dc7`, `ceff54b`, `62d4d7c`, and `415025d`.
Wave-1 commit `8c703b8` used fresh sessions. All 29 sampled reviews used fresh,
one-record validator sessions and passed `validate-review`; that does not cure
the research-provenance breach.

No S2 research session was launched. S2 was only moved to `research` in
canonical state at `40faf7f` before the incident was recognized.

## Why executable audits remained green

`build.py audit-state` verifies Git reconciliation, contract hashes, campaign
state, on-disk attempt integrity, and deterministic sample membership. Research
session identity is not represented in packet artifacts or campaign state, so
the audit cannot distinguish one fresh session per code from repeated turns in
one agent thread. Its clean result is therefore not evidence that this process
rule was satisfied.

## Frozen-contract recovery constraints

An in-place retry is not defined:

- finalized artifacts may not be hand-edited;
- duplicate attempt-1 runs are rejected;
- attempt 2 is permitted only after a valid attempt-1 `reject` or `invalid`
  review, which these records do not have;
- the S1 sample is immutable and may not be replaced; and
- S1 has already been published through the fail-closed site builder.

Deleting or replacing the affected records, changing the recorded sample, or
inventing a new retry state would bypass the frozen governance rather than
repair it. No further research spend was authorized while the campaign was
paused.

## Resolution

Victor directly instructed the operator on 2026-07-22 to ignore the
single-purpose-session contract. This is recorded as a narrow governance
exception: the 39 S1 records are accepted, and researcher workstreams may be
reused for later codes. The waiver does not alter artifact bytes, deterministic
gates, sampling, review isolation from authors, remediation limits, publication
rules, pause triggers, or launch-fixed ceilings. The campaign resumes at S2,
whose state had already been committed as `research` before the pause.
