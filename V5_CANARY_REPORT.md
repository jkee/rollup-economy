# v5 canary report — five codes, Phase 2 gate

**Recommendation: accept the canary and approve the Phase 3 fleet.**
Judged against the frozen failure conditions (methodology §7): no systemic
construct errors (5/5 isolated reviews returned zero material findings), no
misleading evidence treatment (every validator confirmed honest
PROXY/ESTIMATE labeling and stated bridges), no broken mechanics (all five
records reproduce byte-exactly under `build.py check`), and the results are
useful for prioritization (base tiers span `STRUCTURAL_OUT` to
`HIGHEST_PRIORITY` with economically coherent drivers). Estimates remaining
and tier intervals crossing are, per the methodology, not failure grounds.

All research: fresh single-author claude-sonnet-5 sessions, 2026-07-22.
All reviews: isolated claude-fable-5 sessions, never the author, every
primitive-cited source reopened. Runs finalized under `bcecacb`;
this report written at the Phase 2 gate. No formula, anchor, cut, or
evidence rule was changed after seeing outcomes.

## Canary result

| NAICS | H | F | C | D | A | L | Base tier; interval | Readiness / action | Review |
|---|---:|---:|---:|---:|---:|---:|---|---|---|
| 238220 Plumbing/HVAC | 0.79 | 9.11 | 10.00 | 10.00 | 7.47 | 0.79 | `STRUCTURAL_OUT`; → `LOW_PRIORITY` | `MODEL_CONDITIONED` / `VALIDATE_ASSUMPTIONS` | caveats, 0 material |
| 541214 Payroll | 7.45 | 7.30 | 9.40 | 7.20 | 7.84 | 7.20 | `HIGHEST_PRIORITY`; `CONDITIONAL` → `HIGHEST_PRIORITY` | `MODEL_CONDITIONED` / `VALIDATE_ASSUMPTIONS` | caveats, 0 material |
| 541511 Custom programming | 4.36 | 10.00 | 6.00 | 8.06 | 7.11 | 4.36 | `PRIORITY`; `CONDITIONAL` → `HIGHEST_PRIORITY` | `MODEL_CONDITIONED` / `VALIDATE_ASSUMPTIONS` | caveats, 0 material |
| 541512 Systems design | 5.16 | 10.00 | 6.00 | 6.82 | 6.99 | 5.16 | `PRIORITY`; `CONDITIONAL` → `HIGHEST_PRIORITY` | `MODEL_CONDITIONED` / `VALIDATE_ASSUMPTIONS` | caveats, 0 material |
| 541930 Translation | 4.07 | 3.71 | 6.00 | 6.48 | 5.07 | 3.71 | `CONDITIONAL`; `STRUCTURAL_OUT` → `PRIORITY` | `MODEL_CONDITIONED` / `VALIDATE_ASSUMPTIONS` | caveats, 0 material |

No record has a robust tier. Readiness is uniformly `MODEL_CONDITIONED`
because every `n_band` is a margin-bridged estimate (the known dataset
limitation; better LMM firm-count data differentiates readiness with zero
code changes).

Drivers and weaknesses (condensed from the memos):

- **238220** — driver: intense multi-year PE bid for an aging,
  under-succession-planned owner base. Weakness: ~70% of the wage bill is
  licensed on-site trade work with structurally low AI exposure; the screen
  correctly refuses to follow the M&A heat.
- **541214** — driver: regulation-driven multi-state payroll-tax complexity
  sustains demand for an accountable operator even as processing automates.
  Weakness: thin, competitively-shopped PEPM pricing (see the C-anchor flag
  below).
- **541511** — driver: converting hourly billing to fixed-fee faster than
  clients and AI-native competitors compete the value away. Weakness: T&M
  billing turns efficiency into fewer billable hours by default.
- **541512** — driver: BLS-validated durable demand growth plus a wage bill
  concentrated where AI tooling measurably compresses task time today.
  Weakness: hourly-billed market structure competes gains away at renewal.
- **541930** — driver: statutory language-access mandates plus an active
  buyer pool. Weakness: per-word/per-hour pass-through economics.

## Review layer

Five isolated reviews, five `publishable_with_caveats`, zero material
findings, zero remediations needed. 68 primitive-cited sources audited
across the five records; 2 unsupported-as-cited (both non-score-driving,
demoted to caveats), the rest supported or partially supported. Every
review validates against the exact current artifact bytes
(`validate_review` + `artifacts_sha256`).

The consistent citation-hygiene pattern: authors' score-driving anchors
(OEWS occupation tables, deal counts, adoption telemetry) verified exactly,
while decorative secondary statistics were repeatedly over-attributed to
pages that don't contain them. Two authors independently caught WebSearch
inventing statistics not present on the underlying page and excluded them.
The validator layer caught the rest. None passed the materiality test.

## Calibration diff vs the archived v4.3 adapter projections (§2.4)

| NAICS | v4.3 H/F/C/D → v5 | v4.3 base → v5 base | Where the weakness was |
|---|---|---|---|
| 238220 | 1.69/7.75/7.19/9.00 → 0.79/9.11/10/10 | `LOW_PRIORITY` → `STRUCTURAL_OUT` | Same diagnosis (H weakest link). Fresh wage-weighted occupation research cut H below the L≥1 cut; v3 evidence lacked the occupational split, adapter was directionally right |
| 541214 | 10.0/5.40/3.15/5.85 → 7.45/7.30/9.40/7.20 | `CONDITIONAL` → `HIGHEST_PRIORITY` | Largest swing, both directions: adapter mapped l=0.86 straight to H=10 (generous); its elicited C=3.15 ignored flat PEPM billing that researched q=0.47 credits (harsh). Adapter constants weak on both; note the fresh q is itself ESTIMATE-grade |
| 541511 | 7.42/9.81/2.10/5.85 → 4.36/10/6.0/8.06 | `CONDITIONAL` → `PRIORITY` | Adapter C=2.10 too harsh vs researched q=0.30; fresh a·rho tempers H. Adapter constants weak |
| 541512 | 10.0/9.18/6.50/9.00 → 5.16/10/6.0/6.82 | `HIGHEST_PRIORITY` → `PRIORITY` | Adapter mapped high l to H=10 with generic implementability; fresh occupation-mix a·rho halves it. Adapter constants weak |
| 541930 | 6.82/1.96/1.75/5.85 → 4.07/3.71/6.0/6.48 | `LOW_PRIORITY` → `CONDITIONAL` | Fresh evidence lifts F and C moderately; still bottom of the five. Split verdict: adapter C harsh again; v3-era evidence understated buyer activity |

Systematic pattern, consistent across all five: **the v4.3 adapter's H
constants were generous** (high `l` flowed through generic a·rho into
near-cap H) **and its elicited C constants were harsh** (1.75–3.15 vs
researched 6.0–9.4). Fresh research compresses H and lifts C. The top of
the ranking flips accordingly (541512 → 541214). No tuning performed or
proposed; recorded for interpretation only.

## Flags for Victor (frozen items — none block acceptance)

1. **C-anchor compression at the top.** q=0.47 (541214) and q=0.58 (238220)
   both land C ≥ 9.4 against the frozen 50%-retention anchor, so C stops
   differentiating precisely where retention narratives are most cautious —
   541214's own weakness statement says gains get competed away while C is
   its strongest factor. An anchor artifact, disclosed by its validator; a
   change is a v6 decision.
2. **PROXY-vs-ESTIMATE boundary on blended constructs.** Multiple authors
   noted that a source-grounded quantity with judgment layered on top
   (`d5` deflation, `a` exposure-weighting) fits neither state cleanly.
   Validators consistently judged the chosen labels honest; left to
   validator judgment per the simplicity principle.
3. **Lens-narrowing tension.** For 238220 the coherent narrowing (recurring
   service vs new-construction subcontracting) coincides with the segment
   PE prefers. Disclosed and validated as non-favorable (the record screens
   out anyway); expect the same tension in fleet codes where it will not be
   self-neutralizing.
4. **`l` basis understates 1099-heavy industries.** 541930's compensation
   ratio misses freelance linguist pay (QCEW is W-2 only) — disclosed, and
   outside the envelope's declared `interval_scope`. Other fleet codes with
   heavy contractor delivery will share this.
5. **Uniform `MODEL_CONDITIONED`** readiness, as predicted at freeze time —
   the dataset-upgrade item in V5_PLAN "Beyond v5" is what would move it.

## Cost note

Per the v3 reporting policy carried forward: no dollar figures are
asserted. Platform-observed usage for the canary: five research runs
(claude-sonnet-5) at roughly 115k–136k subagent tokens each and five
reviews (claude-fable-5) at roughly 85k–128k each, ~10 minutes per research
run wall-clock with research and reviews overlapped.
