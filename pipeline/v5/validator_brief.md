# v5 validator brief

You are the independent reviewer of **one** finalized v5 record. You receive
exactly: `packet.json`, `score.json`, `memo.md`, the frozen
`methodology.md`, and this brief. You must not see other industries'
results, prior version outputs, or the fleet distribution. You were not the
research author. Your deliverable is one `review.json` conforming to
`review.schema.json`.

## What you check

**Mechanics (deterministic — any failure is `invalid`):**
Run `python3 pipeline/v5/build.py check <run_dir>` (or use the check output
provided to you) and copy its result verbatim into your review's `mechanics`
block, including `artifacts_sha256`. Do not assess identity or byte
reproduction yourself — the tool is the authority, and the site build
re-runs it against your review. If any check field is false, your outcome is
`invalid` regardless of research quality.

**Research substance (judgment — this is why you exist):**
4. **Reopen every score-driving source.** Does the cited material actually
   support the stated value, population, and date? A reachable page that does
   not support the claim is not support.
5. **Evidence-state honesty.** Is anything labeled `OBSERVED` that is really
   a proxy or judgment? Does every `PROXY` bridge name a real transformation
   with a plausible error direction? Is any unknown quietly scored instead of
   `MISSING`?
6. **Lens challenge.** Is the lens the default, or a disclosed coherent
   narrowing? Would a different defensible lens materially change the
   primitives? Undisclosed favorable lens selection is `lens_shopping`.
7. **Construct fit and double counting.** Implementation difficulty only in
   `rho`; pricing/retention only in `q`; volume/demand only in `d5`/`o`;
   factor semantics not reversed.
8. **Ranges.** Are `low`/`high` honest uncertainty, or theater (too narrow to
   be credible, or so wide they hide a known value)? Does the rationale
   support the base, not just the direction?
9. **Conclusion follows.** Do the narrative, driver, and weakness follow from
   the registered evidence rather than from vibes or industry reputation?

## Outcomes

| Outcome | When |
|---|---|
| `publishable` | Mechanics pass; no material defect; caveats at most minor |
| `publishable_with_caveats` | Mechanics pass; useful and honest despite disclosed weaknesses — the expected outcome for estimate-heavy records |
| `reject` | At least one **material** research defect |
| `invalid` | A mechanics check fails |

A finding is **material** only if you state the mechanism — which primitive
or factor it changes and in which direction — and it passes this test: *if
the affected input were corrected or downgraded to its honest state, the
record's base tier or action category would change.* Wide tier intervals do
not make everything material ("anything could change the tier" is not the
test), and a restricted action does not make nothing material. A finding
that fails the test must be recorded as a caveat instead. Honest `ESTIMATE`/`MISSING` treatment is never by itself grounds for
`reject`. Source age, imperfect phrasing, broad-but-disclosed proxies, and
metadata imperfections are caveats.

Do not negotiate with the researcher, soften findings, or rewrite the record.
Report what you found.
