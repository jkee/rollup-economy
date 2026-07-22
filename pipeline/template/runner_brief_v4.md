# v4 isolated research-runner brief

Research one code at a time with no delegation. Fleet packets must identify
`gpt-5.6-terra`; isolated golden packets must identify `gpt-5.6-sol`. Do not
read another runner's packet, prior v4 conclusions, or golden membership.

For each code, read its assembled `pipeline/prompts_v4/<naics>.md`, the exact
v4 methodology and packet schema. Research and write one canonical packet to
`pipeline/v4/packets/<naics>/<run-id>.json`. Then run the v4 finalizer into
`pipeline/v4/runs/...` for fleet or `pipeline/v4/golden/...` for golden, with
the memo under `pipeline/v4/memos/...`.

Reopen every score-driving source. Missing data must remain MISSING; an honest
unproven packet can be publishable. Never write deterministic scores or edit a
generated record/memo. Validate schema, identity, dataset equality, role
membership, numeric ranges, arithmetic, score monotonicity, and byte-identical
fresh finalization before reporting completion.

Attempt 2 is allowed only with exact independent-review findings supplied by
the orchestrator. It uses a new run ID, records `remediates_run_id`, and fixes
only those material/fatal defects. There is no third attempt.
