# v5 Plan — to completion

**Companion to:** [pipeline/v5/methodology.md](pipeline/v5/methodology.md) (frozen at `9c8d5ad`, gate hardened at `0bfcde8`, branch `codex/v5`).
**Replaces:** [V3_PLAN.md](V3_PLAN.md) as the working tracker; V3_PLAN, V3_PRODUCT, and V3_PLAYBOOK remain historical records of the shipped v3.1.2 product.
**Status legend:** `[ ]` todo · `[x]` done · `[~]` in progress. Update checkboxes as work lands.

Standing rules for every phase: simplicity first; models own research and
review judgment; code owns arithmetic and fail-closed gates; git is the only
governance; one remediation per record; never publish unreviewed; stop only
at the gates listed here.

---

## Phase 0 — Freeze and scaffold · done

- [x] 0.1 v5 methodology, briefs, schemas, scorer, build, publication gate (`pipeline/v5/`, 37/37 tests)
- [x] 0.2 Frozen decisions recorded: v4.3 anchors/tier cuts as-is; fleet = 63-code Phase 4 universe; validation on best model class (Sol/Fable), research on cost-optimized class (Terra/Sonnet)
- [x] 0.3 v4.2 audit evidence and v4.3 adapter run committed as preserved history
- [x] 0.4 Branch `codex/v5` pushed to origin

## Phase 1 — Interface canary (one code) · done

The first real packet is the test of the brief→packet contract against real
model output (Playbook lesson 5: hand-made fixtures lie).

- [x] 1.1 Research **238220** fresh under `research_brief.md`: single author, web research, cost-optimized model class, dataset `l`/`n` injected into the prompt (run `238220-a1-20260722`, claude-sonnet-5, 18 sources)
- [x] 1.2 `build.py validate` + `finalize` + `check` on the real packet — all pass, no manual repair
- [x] 1.3 One adjustment: memo header printed raw 12-decimal A/L; display-only rounding in `render_memo` (`bcecacb`), 37/37 tests. Brief/schema needed no change; the author's friction notes (PROXY-vs-ESTIMATE boundary on blended constructs, lens-narrowing tension, single evidence_state on two-layer `a`) are judgment tensions the validator brief already covers — flagged for Victor at the Phase 2 gate, not patched with rules
- [x] 1.4 Memo read: economically useful, not schema-compliant garbage. The weakest-link design bites as intended — F 9.11 (intense PE bid for aging owner base) but H 0.79 base (~70% of wage bill is low-AI-exposure field trade labor), so base tier STRUCTURAL_OUT, interval → LOW_PRIORITY, MODEL_CONDITIONED / VALIDATE_ASSUMPTIONS

**Done when:** one real packet passes `check` without manual repair and the memo reads as a defensible screen.

## Phase 2 — Full canary (five codes) + reviews · ~1–2 days

- [ ] 2.1 Research the remaining four: **541214, 541511, 541512, 541930** (fresh sessions, one code each)
- [ ] 2.2 Five isolated validator reviews (best model class, fresh sessions, never the author); mechanics blocks copied from `build.py check`; every primitive-cited source audited
- [ ] 2.3 At most one remediation per `reject`/`invalid`, findings attached, fresh review
- [ ] 2.4 Calibration diff: fresh canary results vs the archived v4.3 adapter projections (`V4_3_CANARY_RESULTS.md`) — where they disagree, note whether the v3 evidence or the adapter constants were weak; no tuning
- [ ] 2.5 Compact report: five rows (H/F/C/D, A/L, tier + interval, readiness/action, driver/weakness, review outcome) + acceptance recommendation

**GATE — stop for Victor's approval.** Per the frozen methodology, the canary
fails only for systemic construct errors, misleading evidence treatment,
broken mechanics, or results useless for prioritization — not because
estimates remain or ranges cross tiers.

## Phase 3 — Fleet (63 codes) · the bulk of the work

- [ ] 3.1 Run the remaining 58 codes in waves (~10 per wave), one independent research session per code
- [ ] 3.2 After each wave: `check` every run, commit the validated wave (v3 lesson: an outage may only cost one wave)
- [ ] 3.3 One isolated review per attempt, wave by wave
- [ ] 3.4 Single remediation wave at the end for all `reject`/`invalid`; remaining failures are excluded, not retried
- [ ] 3.5 `build.py site` → `6digit/six_data_v5.json` (fail-closed gate); record counts by tier, readiness, action, outcome, and every exclusion with its findings

**Done when:** all 63 attempted and reviewed, remediation wave closed, site builds clean with zero integrity errors.

## Phase 4 — Dashboard, docs, and repo hygiene · ~1–2 days

- [ ] 4.1 Point the `6digit` dashboard at `six_data_v5.json`: tier + interval + readiness/action badges, factor chain → primitives → rationale → sources → caveats → validator findings → `change_evidence`; memo as the primary readable explanation
- [ ] 4.2 Replace the v4 adapter view (archived in history); keep v3 available as a comparison column or archive it — decide at the time
- [ ] 4.3 Regenerate README stats from v5 outputs; one "which document governs what" index at the top; mark V3_* and V4_* docs historical
- [ ] 4.4 Merge `codex/v5` → `main` via PR; retire `codex/v4-2-phase4`; remove or mark the root-level v2 duplicate JSONs

**Done when:** every displayed number clicks through to its evidence or its honest evidence state; README is generated, not hand-written; `main` is current.

## Phase 5 — Close and maintain · ~half a day

- [ ] 5.1 Campaign closure note: attempted/reviewed/remediated/published/excluded counts, tier and readiness distributions, the calibration-diff verdict from 2.4
- [ ] 5.2 Refresh cadence stated in README: dataset vintages on new SUSB/QCEW releases (annual); market-sensitive evidence stale after ~12 months → new run series, same methodology
- [ ] 5.3 Final push; v5 campaign closed

**Done when:** the closure note is committed and the repo needs no session context to understand.

---

## Beyond v5 — out of frozen scope, each requires a new version

These are noted so they aren't re-litigated mid-campaign. None of them may
alter v5 while it runs.

- **Scope expansion (v5.1+):** beyond the 63 codes toward the 1,012-industry
  product goal. Needs derived datasets validated for the new codes first;
  otherwise identical methodology.
- **Stage 2 — target/buyer diligence:** for codes the screen marks
  `ADVANCE_TO_STAGE2` (or top-tier `VALIDATE_ASSUMPTIONS` codes after their
  assumptions are validated). Target-level evidence, separate methodology;
  the screen's `change_evidence` fields are its shopping list.
- **Dataset upgrade:** observed-quality LMM firm counts (today every `n_band`
  is a margin-bridged estimate, so readiness is uniformly
  `MODEL_CONDITIONED`). Better data differentiates readiness with zero code
  changes.

## Cost and calendar (rough)

| Phase | Model burn | Calendar |
|---|---|---|
| 1 — interface canary | 1 research run | one session |
| 2 — canary + reviews | 4 research + 5 review runs | 1–2 days |
| 3 — fleet | ~58 research + ~63 review runs + remediations | ~1 week part-time, mostly model wait |
| 4 — dashboard/docs | ~0 (code work) | 1–2 days |
| 5 — close | ~0 | half a day |

No dollar figures are asserted; report platform-observed usage if exposed,
state the limitation otherwise (v3 reporting policy carries forward).

**Critical path:** 1 → 2 → gate → 3 → 4 → 5. Phase 4 dashboard work can
begin against canary data during Phase 3.
