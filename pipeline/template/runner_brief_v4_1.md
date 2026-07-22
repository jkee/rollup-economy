# v4.1 isolated research-runner brief

Research exactly one manifest entry with no delegation. Use the research model
specified by that entry; do not infer the route from the industry. Do not read
benchmark membership, class labels, expected outcomes, prior conclusions,
another runner's packet, or any prior review.

Read only the entry's assembled `pipeline/prompts_v4_1/<naics>.md`, pinned
industry specification, dataset snapshot, methodology, and packet schema. The
same class-neutral prompt bytes are used for every research route. Runtime
substitution may fill only model ID, date, run ID, and prompt version.

Write one packet under `pipeline/v4_1/packets/<naics>/<run-id>.json`, then run
`pipeline/build/finalize_run_v4_1.py` into the manifest-declared record and memo
paths. Never author or edit a score, interval, readiness state, gate, action,
verdict, finalized record, or rendered memo.

Honor the frozen archetype enumeration, objective selection, and value-basis
mode. A missing basis or dataset value remains missing; do not manufacture a
base value or bounded range. Missing inputs produce partial identification,
not a neutral point, base factor, aggregate S, or verdict. Reopen every
score-driving source and disclose every proxy bridge.

An `assumption` value basis is a pre-frozen class-neutral bounded structure,
not evidence: preserve its cash-cost range and mutually exclusive role weights,
accept no source claim for it, prohibit substitution with a bad broad-NAICS
proxy, and force readiness `UNPROVEN`.

For `dataset` mode, preserve the machine-readable population, geography,
period, unit, and business-model bridge. If the bridge is absent or null, treat the broad
labor/role basis as an unsupported proxy and force readiness `UNPROVEN`.

If `selection_uncertainty` is true, retain one selected primary record, force
readiness to `UNPROVEN`, widen coverage and value-basis uncertainty, make no
NAICS-wide claim, and do not split the NAICS into additional records.

Validate schema, manifest identity, all pinned digests, exact role membership,
numeric ranges, fresh finalization, and byte-identical memo rendering before
reporting completion. Attempt 2 is permitted only when the manifest binds it
to a prior rejected or invalid exact run. There is no third attempt.
