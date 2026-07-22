# v5 methodology — AI roll-up industry opportunity screen

**Status:** frozen. The freeze identity is the git commit that introduces
this folder; every artifact records the commit it ran under
(`methodology_commit`). Changing a formula, anchor, cut, evidence rule,
default lens, or fleet scope after this commit requires a new version folder
and a full rerun.
**Supersedes:** the v4.x line for the active workflow. v3.1.2 remains the
published product until a v5 fleet replaces it. All earlier versions are
immutable historical evidence and are never imported as active tooling.

## 1. Product decision

v5 answers one question: **which six-digit industries deserve deeper
AI-enabled roll-up diligence?** It does not select companies, underwrite
transactions, forecast returns, or claim a representative target exists.
`HIGHEST_PRIORITY` means "research next," never "buy."

## 2. Architecture

```
research_brief.md + dataset inputs
        ↓
industry research model  — research + judgment, one industry per assignment
        ↓
canonical packet (packet.json)
        ↓
deterministic code (build.py + score.py)  — validation + arithmetic
        ↓
independent validator model (validator_brief.md)
        ↓
publish / publish with caveats / exclude   (build.py site)
```

The division of labor is absolute:

- **Models** own research, lens judgment, evidence classification, ranges,
  rationale, and review judgment. One industry is one independent single-author
  assignment; no delegation to sub-agents. **Routing:** research packets use a
  cost-optimized capable web-research model (Terra/Sonnet class); validation
  uses the best available model (Sol/Fable class), because review quality
  compounds across every published record. The validator is never the research
  author and runs in a fresh isolated session. Exact runtime model IDs are
  recorded in every packet and review; swapping models within these classes is
  not a methodology change, but validation may never be routed to a weaker
  class than research.
- **Code** owns schema validation, dataset injection, source-reference
  integrity, arithmetic, factor/tier/envelope/readiness/action computation,
  memo rendering, latest-accepted-attempt selection, the deterministic
  integrity check (`build.py check`: identity, byte reproduction, artifact
  digest), and the publication gate (`build.py site` re-runs the check and
  validates every accepted review against the exact current bytes, failing
  closed on any mismatch). Code never judges whether a proxy is
  intellectually appropriate or whether a source truly supports a conclusion
  — that is the validator's job. Conversely, models never self-assess
  mechanics: a review's `mechanics` block is copied from the check tool.
- **Git** owns governance. The freeze is the commit containing this folder;
  every `score.json` records the commit it ran under (`methodology_commit`,
  captured at finalize time — a commit cannot contain its own hash, so
  nothing else stores one). There are no signed tags, freeze manifests,
  salted holdouts, issuance authorities, claim envelopes, or receipts.
- The enforced packet/review contract is `build.py`; the `.schema.json`
  files document the same contract for authors. A divergence between them is
  a bug, never a permitted extension — unknown fields are rejected.

## 3. Economic model

Two dataset inputs are injected per industry from
`pipeline/datasets/derived/<naics>.json` and never researched by a model:
`l` (compensation-to-receipts ratio) and `n` (LMM-band firm count). Their
values are frozen points for cross-industry comparability, but their
evidence state honors the dataset's own provenance: recorded quality
`HIGH`/`MED` maps to `OBSERVED`, anything weaker (including derived
`ESTIMATE` series such as margin-bridged firm counts) maps to `ESTIMATE`
and weighs on readiness like any other estimate. A stored zero whose
provenance says no series exists is treated as `MISSING`, never as economic
zero. Anomalous raw values (e.g. `l > 1`) are kept raw; the factor cap
absorbs them.

Because `l` uses a receipts denominator (not controllable value-added or
target cash cost), H is a *relative screening* measure of labor opportunity.
It may not be quoted as EBITDA uplift, target savings, or a forecast.

Seven researched primitives (defined precisely in `research_brief.md`):
`a`, `rho` (labor opportunity), `e`, `s5` (transferable firms), `q`
(retention), `d5`, `o` (durable demand). Each carries numeric
`low <= base <= high`, an evidence state, sources, rationale, caveats, and
`change_evidence` — what obtainable evidence could materially move it.

Factors (continuous 0–10; anchors in `thresholds.json`):

```
H = 10 · min(1, l·a·rho / 0.25)          labor opportunity; 25% of receipts = 10
F = 10 · clamp(log10(1 + n·e·s5) / log10(501), 0, 1)   500 expected transfers = 10
C = 10 · min(1, q / 0.50)                 50% retention = 10
D = 10 · clamp(d5·o, 0, 1)               surviving operator-required quantity share
```

Aggregate and tier:

```
A = (H + F + C + D) / 4        breadth
L = min(H, F, C, D)            weakest link, disclosed not averaged away
```

| Tier | A ≥ | L ≥ |
|---|---|---|
| `HIGHEST_PRIORITY` | 7.5 | 6 |
| `PRIORITY` | 6.0 | 4 |
| `CONDITIONAL` | 4.5 | 2 |
| `LOW_PRIORITY` | 3.0 | 1 |
| `STRUCTURAL_OUT` | otherwise | — |

Each record also publishes the exact 3⁴ scenario envelope over its factor
low/base/high values: attainable tier interval, and `robust_tier` only when
every scenario lands in one tier. A missing factor spans its semantic domain
[0, 10] in the envelope and produces **no base score** — missing evidence
never becomes zero.

The envelope's scope is disclosed, not implied: it is **research-input
sensitivity with the dataset anchors (`l`, `n`) held fixed**. Fixing the
public-data anchors is what makes the screen comparable across industries,
but it means the tier interval does not include uncertainty in
compensation/receipts measurement, ancestor-code substitutions, vintage
mismatches, or margin-bridged firm counts. Each record's envelope carries
this statement (`interval_scope`), and dataset weaknesses still reach the
reader through the dataset leaves' evidence states and readiness.

## 4. Evidence and readiness

Evidence states: `OBSERVED`, `PROXY` (requires a stated bridge), `ESTIMATE`
(bounded honest judgment), `MISSING` (null values, no base). Citation count
and prose confidence never promote a state.

Readiness is reported beside the economics, never blended into them:

| Readiness | Meaning | Action |
|---|---|---|
| `STRESS_TEST_ONLY` | no complete base exists | `EVIDENCE_FIRST` |
| `MODEL_CONDITIONED` | material estimates remain | `VALIDATE_ASSUMPTIONS` |
| `PROVISIONAL` | material proxies remain | tier-dependent |
| `SUBSTANTIATED` | decision-relevant inputs observed | tier-dependent |

For `PROVISIONAL`/`SUBSTANTIATED`, the action follows the attainable tier
set: only top tiers → `ADVANCE_TO_STAGE2`; mixed or conditional →
`SELECTIVE_VALIDATE`; only bottom tiers and substantiated → `DEPRIORITIZE`.
A model-conditioned record can hold a high tier; its action stays
`VALIDATE_ASSUMPTIONS`.

## 5. Review and publication

An isolated validator model reviews every attempt under `validator_brief.md`
and returns `publishable`, `publishable_with_caveats`, `reject`, or
`invalid`. `reject` requires a material finding with a stated mechanism
(which primitive/factor changes, direction, why it could change the tier or
thesis); findings without that statement are caveats.
`publishable_with_caveats` is the expected honest outcome for
estimate-heavy records. `invalid` is reserved for mechanical failures.

Each rejected or invalid record receives **at most one** remediation attempt
(new run ID, findings attached to the same-class researcher, fresh
finalization and fresh isolated review). Remaining failures are excluded and
listed in the generated output. There is no retry-until-accepted loop and no
required 100% publication rate.

## 6. Traceability

Every displayed result exposes the full chain: tier and interval → A/L →
H/F/C/D → primitives and ranges → rationale → sources and caveats →
validator findings → what evidence would change the result. The memo is
rendered deterministically from the packet, so prose and numbers cannot
drift. Base ordering is provided for navigation; v5 does not claim a precise
stable rank where tier intervals materially overlap.

## 7. Canary and release process

1. **Freeze**: commit methodology, briefs, schemas, thresholds, and code.
   That commit is the freeze; artifacts record it at run time.
2. **Interface test**: the first real canary packet is also the test of the
   brief→packet contract against real model output (hand-made fixtures have
   burned this project before — Playbook lesson 5). Expect to adjust the
   contract after seeing one real packet, before the remaining canaries; any
   such adjustment is re-committed before proceeding.
3. **Canary**: research the five development codes (`238220`, `541214`,
   `541511`, `541512`, `541930`) fresh under v5; score; one isolated
   validator per record; then **stop for human approval**. The canary fails
   for systemic construct errors, misleading evidence treatment, broken
   mechanics, or results useless for prioritization — not because estimates
   remain or ranges cross tiers. (Optional, cheap: diff the fresh canary
   packets against the archived v4.3 adapter projections in
   `V4_3_CANARY_RESULTS.md` to learn where the adapter constants vs the v3
   evidence were weak.)
4. **Fleet** (after approval only): the fleet scope is the existing 63-code
   Phase 4 universe in `pipeline/blocks/targets_phase3.json`; the five
   canary codes count toward it. One run per industry, one review per
   attempt, one remediation wave, publish both publishable tiers, exclude
   and report the rest, close. Expanding beyond the 63 codes is a new
   version.

## 8. Standing rules

1. Never hand-edit a finalized `score.json`, `memo.md`, or the site dataset.
2. Never publish an unreviewed record (the `--allow-unreviewed` build is a
   development preview only and is labeled as such in its output).
3. Unknown is never zero and never a neutral default.
4. Changing a formula, anchor, cut, evidence rule, or the default lens after
   the freeze = a new version folder and a full rerun. Never tune to
   outcomes.
5. At most one remediation per record; campaigns close with exclusions
   listed.

## 9. Non-goals

v5 deliberately does not include: cryptographic claim/receipt systems; signed
operator principals; salted holdouts or burned-code ledgers; multi-model
voting per estimate; remediation authorizers or independent retrievers;
dominance graphs; target-specific valuation or entry/exit multiple scoring
(Stage 2 concerns, out of scope here); attempts to encode validator judgment
in schemas; or precise-rank claims unsupported by the published uncertainty.
If a future problem seems to demand one of these, the answer is a better
brief or a better validator, not more machinery.

## 10. Layout

```
pipeline/v5/
  methodology.md                this file
  research_brief.md             verbatim researcher contract
  validator_brief.md            verbatim validator contract
  research_packet.schema.json   formal packet reference (enforced by build.py)
  review.schema.json            formal review reference
  thresholds.json               anchors + tier cuts, one source of truth
  score.py                      pure arithmetic (ported from verified v4.3 scorer)
  build.py                      validate / finalize / site
  test_v5.py                    sentinels and contract tests
  runs/<naics>/<run_id>/        packet.json, score.json, memo.md, review.json
6digit/six_data_v5.json         generated site dataset — never hand-edited
```
