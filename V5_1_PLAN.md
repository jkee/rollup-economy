# v5.1 Plan — scope expansion to the full 1,012-code universe

**Status: DRAFT — not launched.** Launch requires Victor's explicit approval
of this plan as written (scope, budget, contract), and the fleet
additionally requires a passed cross-sector canary gate. These are the only
two unconditional stops, and they are **stage-aware**: `launch_approved`
gates everything including the canary; `canary_approved` gates fleet blocks
only. Each approval is a committed record in
`pipeline/v5_1/campaign_state.json` (created as a prelaunch scaffold, so
approval has a committed place to land) — prose edits to this file
authorize nothing. The launch record also fixes the exact runtime model IDs
(within the frozen classes) and the session/budget ceiling.
**Companion to:** [pipeline/v5/methodology.md](pipeline/v5/methodology.md) (frozen v5.0).
**Proposed under:** [V5_PLAN.md](V5_PLAN.md) "Beyond v5", which permits proposing scope expansion as a new governed version (methodology §7.4: "Expanding beyond the 63 codes is a new version") — it does not itself authorize launch.
**Prior ledger:** [V5_CLOSURE_REPORT.md](V5_CLOSURE_REPORT.md) — v5.0 closed 2026-07-22, 63/63 published, 0 excluded.
**Status legend:** checklists use `[ ]` todo · `[~]` in progress · `[x]` done. Blocks track their lifecycle stage: `todo` · `research` · `review` · `remedy` · `closed` · `descoped`. Canonical campaign state lives in `pipeline/v5_1/campaign_state.json`; this document is its human-readable mirror — update both in the same commit.

## Charter

v5.1 answers the same single question as v5.0 — which six-digit industries
deserve deeper AI-enabled roll-up diligence — over the **full 1,012-code
NAICS 2022 universe**. The **economic content is identical** to frozen v5.0:
same formulas, anchors, tier cuts, evidence rules, and brief substance.
The version identity, fleet scope, paths, and publication mechanics are
v5.1's own: new records identify as methodology 5.1 and live under
`pipeline/v5_1/`.

**v5.1 reruns all 1,012 codes, including the 63 published by v5.0.** This
satisfies the frozen "new version folder and a full rerun" rule literally,
costs only ~6% more sessions, keeps evidence vintage uniform, and turns the
sector-54 block into a free drift measurement against `six_data_v5.json`.
Carrying the 63 forward was considered and **rejected** — it conflicts with
the rerun rule and requires mixed-provenance machinery. It is not a launch
option; only the rerun is operationally defined.

The campaign runs **iteratively in industry blocks** — one block at a time,
each a complete mini-campaign ending with a consistent published dataset and
a committed report section. After the canary gate, no further approvals:
Victor reads block reports at will and can redirect between blocks.

Most frozen rules carry forward verbatim: one independent single-author
research session per code; validator never the author and never a weaker
model class than research; one remediation per reviewed record; never tune
to outcomes; unknown is never zero; commit per validated wave.

**One rule is explicitly amended for compute:** v5.0's "never publish
unreviewed" becomes **sampled validation** under the frozen sampling
contract below. Deterministic gates (`validate` + `finalize` + `check`)
still cover every record; isolated best-class review covers only the
sampled minority; every published record carries
**`independent_review: accepted | not_reviewed`**. The v5.1 output is
therefore labeled a **provisional sampled-validation screen** — not a
completed canonical publication. Reviewing the remainder is the first
Beyond-v5.1 campaign, which publishes its own new immutable output; nothing
is upgraded in place. Everything else — wave sizing, block order, pacing —
is operator judgment (sample selection is not: it follows the frozen
contract).

## Setup

- [x] **Prelaunch scaffold (before approval, breaks the bootstrap circle):**
      commit `pipeline/v5_1/` containing only `campaign_state.json`
      (`launch_approved: null`, `canary_approved: null`, all blocks `todo`).
      Victor's launch approval **is** the commit filling `launch_approved`
      with date, model IDs, and the session/budget ceiling
- [ ] After approval, complete `pipeline/v5_1/` from frozen v5.0 with these
      enumerated deltas (listed in the freeze commit message):
      - methodology version identity 5.1; fleet scope →
        `pipeline/v5_1/targets.json`: all 1,012 codes with `title` and
        `block` membership — **immutable after the freeze**. Mutable
        campaign state (approvals, block statuses, sample assignments, the
        closure ledger) stays in `campaign_state.json`; the frozen scope
        file never changes
      - the sampled-validation amendments to the copied methodology,
        **enumerated section by section**: §2 (the validator reviews
        sampled attempts, not every attempt), §5 (review coverage follows
        the frozen sampling contract; published records carry
        `independent_review: accepted | not_reviewed`), §7 (fleet process =
        the block loop with sampled reviews), §8 rule 2 ("never publish
        unreviewed" → "never publish outside the fail-closed
        sampled-validation contract": deterministically **unsampled**
        records publish as `not_reviewed` by design; no path publishes a
        **sampled** record without its accepted review or reviewed
        exclusion)
      - `assignment.py` paths → `pipeline/v5_1/`; plus a new
        `assignment.py sample <block>` subcommand that computes the block's
        sample deterministically from finalized scores and the frozen seed
        and writes it to `campaign_state.json` — sampling is **code-owned**;
        no session ever picks records
      - two executable audit subcommands (prose requirements are not
        enforcement): `build.py validate-review <run_dir>` validates a
        landed review against the exact artifact bytes — the block loop
        requires it before any review is accepted or committed; and
        `build.py audit-state` reconciles branch vs origin,
        `contract_sha256` vs the frozen files, `campaign_state.json` vs
        on-disk artifacts (including partial attempts), and recomputes
        every closed block's sample membership — run at every operator
        session start
      - `build.py site` → `6digit/six_data_v5_1.json`, labeled a
        **provisional sampled-validation screen**, publishing **only codes
        in blocks marked closed** in `campaign_state.json`, every record
        carrying `independent_review: accepted | not_reviewed`. Closure
        semantics: every code needs a run passing `check`; every **sampled**
        code must reach a *terminal* review state — `accepted` (publish)
        or, after its single failed remediation, **excluded and listed in
        the output**. A reviewed exclusion closes a block; only a *missing*
        run or review blocks closure. Runs from open blocks (including
        canary runs before their home block closes) are never published;
        the current builder's silent skip of missing run directories must
        become a hard failure for closed blocks. `site` **recomputes each
        closed block's sample membership** from the frozen seed and the
        finalized scores and fails on any drift from `campaign_state.json`.
        v5.0's `--allow-unreviewed` development flag is **removed**:
        unsampled records publish as `not_reviewed` by design, but there is
        **no bypass** for sampled ones
      - freeze identity + drift check: `finalize` records, alongside the
        runtime `methodology_commit` (which is HEAD at run time, **not**
        the freeze identity), a `contract_sha256` over the full frozen v5_1
        contract surface — methodology, briefs, schemas, thresholds,
        scorer, `build.py`, `assignment.py` (sampling seed and selection
        code included), and `targets.json`; `check` and `site` recompute it
        and fail on any drift
- [ ] Dataset check (the V5_PLAN prerequisite — validation, not derivation;
      `pipeline/datasets/derived/` already covers all 1,012): confirm
      `derive.py` reproduces byte-identical output; note per block which
      codes carry gaps (null `labor_share` / null `n_band` / `n_total`
      proxy / the 14 `labor_share > 1` anomalies, of which 13 are outside
      the old fleet plus carried `541618`)
- [ ] Sentinel suite green against `pipeline/v5_1/`; the commit completing
      the contract copy (the step above) is the v5.1 freeze — the scaffold
      commit is not

## Cross-sector canary · gate

v5.0's canary covered four professional-service codes and one construction
code. The expansion is mostly goods, trade, logistics, agriculture, and
government — terrain the frozen lens (a recurring outsourced service
delivered by LMM firms) has never been tested on, and where it may be
incoherent. ~20 sessions to find out before the remaining ~1,200:

- [ ] Research + finalize + check the ten canary codes, fresh single-author
      sessions, one per structural territory. **The list is frozen at
      launch approval; substitutions require re-approval:** `238910` (site
      prep), `311612` (meat processing), `332710` (machine shops), `423840`
      (industrial supplies wholesale), `445110` (grocery), `484110` (local
      freight trucking), `522310` (loan brokers), `621111` (physicians),
      `111998` (misc. crop farming — gap path end-to-end), `921190`
      (general government support — public-sector lens coherence)
- [ ] One isolated review per record (best class, never the author) — the
      canary is reviewed at **100%**; it is purposive, reported separately,
      and never counted toward any random stratum
- [ ] One remediation per `reject`/`invalid` canary record (standard
      single-remediation rule, fresh isolated review); remaining failures
      are excluded and reported at the gate
- [ ] Canary report (`V5_1_CANARY_REPORT.md`) with four specific reads:
      (a) does H stay informative where `l` is structurally small —
      capital-intensive codes screening out *for stated economic reasons*,
      not noise; (b) do `q`/`s5` find real evidence outside services;
      (c) does the frozen lens produce a coherent packet for goods and
      public-sector codes, or a forced construct; (d) does the declared-gap
      path route and render honestly (MISSING → `STRESS_TEST_ONLY /
      EVIDENCE_FIRST`)
- [ ] **GATE — Victor reads the report and approves the fleet**, recorded
      as a committed `canary_approved` entry in `campaign_state.json`. Same
      frozen failure test as v5.0: systemic construct errors, misleading evidence
      treatment, broken mechanics, or results useless for prioritization —
      not estimates remaining or ranges crossing tiers. If the lens proves
      incoherent for a territory, the remedy is **descoping that territory**
      (block status `descoped`, reason stated in the closure report) — never
      a mid-campaign brief edit (that is v5.2 work)

Canary records count toward their home blocks and publish when those blocks
close.

## Sampling contract — frozen at launch

Review coverage follows this contract, fixed in the freeze commit and never
adjusted mid-campaign (adjusting selection after seeing results is tuning):

- **Mandatory stratum:** every record whose **base tier** is
  `HIGHEST_PRIORITY` or `PRIORITY` (as computed by the frozen scorer) is
  reviewed. These drive decisions; their count is unknown until blocks are
  scored (v5.0's services fleet ran ~24% top-tier; goods sectors are
  expected far lower).
- **Random stratum:** per block, `ceil(0.10 × non-mandatory codes)` with a
  minimum of 3, selected deterministically — order the block's non-mandatory
  codes by `sha256(seed + naics)` and take the first k; the seed is a
  constant fixed in the freeze commit. Canary codes are excluded from both
  the selection frame and the denominator.
- **Statistics discipline:** a block's 3–10 random reviews cannot estimate
  a block defect rate. Block reports state observations only (counts,
  outcomes, findings). Inference — a defect-rate estimate with confidence
  bounds for unreviewed records — is computed once, campaign-wide, over the
  pooled random stratum **with design weights** (the minimum-3 rule
  oversamples small blocks, so each record is weighted by its block's
  inclusion probability), in the closure report.
- **Predeclared pause trigger:** any material finding whose stated mechanism
  is systemic (extends beyond the single record), or two or more material
  findings within one block's sample, pauses the campaign for Victor before
  further research spend.

## The block loop

For each block, in whatever order makes sense (the table's order is a
sensible default — services first, goods next, gap-heavy last; reordering
is a committed `campaign_state.json` change with a one-line reason). Every
checkpoint is committed **and pushed**. Backlog is bounded per block, not
per wave — the random stratum is only computable once the block's research
completes, so a per-wave review bound would deadlock large blocks:
mandatory-stratum reviews may start as soon as a run finalizes top-tier,
the random stratum is sampled at block-research completion, and a new
block's research never starts before the previous block reaches `closed`
(at most one block unreviewed at any time):

1. `research` — the block's codes in waves (~10 worked well in v5.0), one
   launcher per code from `assignment.py research`; `validate` + `finalize`
   + `check` each run; commit each validated wave.
2. `review` — `assignment.py sample` computes the block's sample
   (code-owned, deterministic) into `campaign_state.json`; one isolated
   review per sampled attempt (`assignment.py review`); validate each
   landed review against the exact artifact bytes before accepting or
   committing it.
3. `remedy` — one remediation wave for any reviewed `reject`/`invalid`;
   a failed remediation makes the record a reviewed exclusion, which does
   not block closure.
4. `closed` — flip the block's status in `campaign_state.json` and run
   `build.py site` (fail-closed, cumulative) in the same commit as its
   report section in `V5_1_FLEET_REPORT.md`: counts by tier/readiness/
   action/outcome, **review statistics as observations only** (sampled n,
   stratum composition, outcomes, material findings — no block-level
   defect rates; inference happens once at closure), exclusions with
   findings, and a few sentences on whether the screen stayed economically
   informative in this terrain. Update the status and reviewed columns
   below.

Gap-dominated codes run like any others: the frozen finalizer injects
MISSING and they publish as `STRESS_TEST_ONLY / EVIDENCE_FIRST` — lower
evidence quality is a *result* the reports disclose, not a reason to skip.
If a whole block comes back economically uninformative, say so in its report
and move on.

## Block schedule / tracker — 1,012 codes

| Status | # | Block | NAICS | Codes | Reviewed | Notes |
|---|---|---|---|---:|---:|---|
| todo | S1 | Professional, scientific, technical | 54 | 49 | – | v5.0 rerun territory — doubles as drift check vs `six_data_v5.json` |
| todo | S2 | Administrative & support, waste | 56 | 44 | – | |
| todo | S3 | Health care & social assistance | 62 | 39 | – | |
| todo | S4 | Finance & insurance | 52 | 35 | – | 5251x labor_share gaps |
| todo | S5 | Real estate + mgmt of companies | 53, 55 | 27 | – | `551114` anomaly |
| todo | S6 | Other services | 81 | 44 | – | `814110` gap |
| todo | S7 | Information | 51 | 29 | – | n_total proxies |
| todo | S8 | Education + arts/entertainment | 61, 71 | 42 | – | |
| todo | S9 | Accommodation & food | 72 | 15 | – | |
| todo | G1 | Construction | 23 | 31 | – | |
| todo | G2 | Transportation & warehousing | 48–49 | 57 | – | `482112`/`491110` gaps |
| todo | G3 | Wholesale trade | 42 | 69 | – | |
| todo | G4 | Retail trade | 44–45 | 57 | – | n_total proxies |
| todo | G5 | Mfg: food, beverage, textiles | 311–316 | 69 | – | |
| todo | G6 | Mfg: wood through minerals | 321–327 | 96 | – | largest block |
| todo | G7 | Mfg: metals & machinery | 331–333 | 89 | – | machine-shop roll-up territory |
| todo | G8 | Mfg: electronics through misc | 334–339 | 92 | – | `334111`/`334118` anomalies |
| todo | G9 | Mining + utilities | 21, 22 | 35 | – | |
| todo | Z1 | Agriculture, forestry, fishing | 11 | 64 | – | 49/64 gap-routed → unscored, expected |
| todo | Z2 | Public administration | 92 | 29 | – | 29/29 gap-routed → unscored, expected |

The **Reviewed** column is filled at block close as `reviewed/total` (e.g.
`12/49`). Per-record `independent_review: accepted | not_reviewed` lives in
the published output; this column is the block-level rollup.

## Close

- [ ] Dashboard may read `6digit/six_data_v5_1.json` once the first block
      closes, but until the campaign closes it must **visibly state
      coverage**: closed / pending / descoped blocks, codes published of
      1,012, the independently-reviewed share, and the provisional
      sampled-validation label — a partial checkpoint must never present as
      the complete product, and a `not_reviewed` record must never present
      as a reviewed one. `six_data_v5.json` stays as the immutable v5.0
      output
- [ ] Regenerate README stats and extend the "which document governs what"
      index as blocks land
- [ ] `V5_1_CLOSURE_REPORT.md`: attempted/reviewed/remediated/published/
      excluded/descoped counts overall and per block, **campaign-wide
      review statistics** (reviewed share by stratum, outcomes, and the
      pooled random-stratum defect-rate estimate with confidence bounds —
      the only place defect inference happens), tier and readiness
      distributions, the S1 drift comparison vs v5.0, cross-sector
      calibration observations, maintenance handoff (12-month evidence
      staleness per block research date; annual dataset-layer check per
      `pipeline/datasets/README.md`)
- [ ] Final push; v5.1 campaign closed

## Risks, stated upfront

- **Most records publish without independent review** (the exact share
  depends on the mandatory stratum's size; plausibly ~75–80% unreviewed).
  Deterministic gates catch mechanics, not judgment — evidence
  misclassification or unsupported citations in unreviewed records survive
  until the full-validation campaign. Mitigations: every decision-driving
  top-tier record is reviewed; the pooled random stratum yields one honest
  campaign-wide defect-rate estimate with stated bounds; every record is
  labeled, and the output itself is labeled provisional. Residual hole: a
  wrongly-scored record that lands mid-tier can escape review entirely —
  only the full-validation campaign closes it.
- **`q`/`s5` are the judgment-heaviest primitives** (retention and transfer
  probability are weakly observed). Exact base ranks are non-claims where
  intervals overlap; validators scrutinize retention/transfer evidence
  hardest; the S1 rerun quantifies researcher-to-researcher drift against
  v5.0. No brief or anchor changes — that would be tuning.
- **Lens coherence outside services.** `l` uses a revenue-scale denominator
  (receipts for most codes, IPS sectoral output for ~100), so capital- and
  COGS-heavy codes get structurally small H and should concentrate in
  `STRUCTURAL_OUT`/`LOW_PRIORITY` — acceptable if the *reasons* are
  economically right (canary read a), a descoping trigger if the construct
  is incoherent (canary read c).
- **Gap volume.** 181 codes have null `n_band` and 84 null `labor_share`
  (universe-wide; 49 of 64 sector-11 codes and all 29 sector-92 codes are
  gap-routed) — roughly a fifth of the universe publishes without a base
  score. Disclosed per block; a dataset upgrade later differentiates them
  with zero code changes.
- **Evidence aging.** Market-sensitive evidence is stale ~12 months after
  research; each block stamps its dates; refresh is a new date-stamped run
  series per v5.0 closure policy, never an overwrite.

## Beyond v5.1 — separate work, separate governance

- **Full-validation campaign:** isolated best-class reviews for every
  record left `not_reviewed` (the unreviewed majority). Reviews bind to the
  existing artifact bytes — no re-research; the standard one-remediation
  rule applies. It closes by publishing a **new immutable output** that
  supersedes the provisional screen (which remains archived history) —
  never an in-place upgrade. Priority order can follow the campaign's
  pooled defect statistics and per-block observations — review the worst
  terrain first.
- **Stage 2 target/buyer diligence** for `ADVANCE_TO_STAGE2` and validated
  top-tier codes; the screen's `change_evidence` fields are its shopping
  list.
- **Dataset upgrade** (observed LMM firm counts; USDA ERS for sector 11):
  upgrades readiness everywhere with zero code changes.
- **Annual refresh** of the dataset layer and re-screen of stale-evidence
  records as new date-stamped campaigns.

## Cost, budget, calendar (rough)

~1,012 research (cost-optimized class) sessions plus reviews per the
sampling contract: the random stratum is ~90–100 reviews; the mandatory
top-tier stratum is unknown until scoring (plausibly ~100–150 campaign-wide
if services run near v5.0's ~24% top-tier rate and goods run low) — call it
**~200–250 reviews** at the planning midpoint, including the ten
100%-reviewed canary records, plus a few percent remediations. Roughly 1–2
part-time days per block, ~5–8 weeks back-to-back, pausable at any block
boundary.

**Planning budget — an inference for authorization, not asserted actuals:**
extrapolating the prior v5-scale per-session estimate, ~1,220–1,270 sessions
imply roughly **$5.5k–8k before remediations**, with sensitivity of roughly
**+$0.5–1k per additional 100 reviews** if the mandatory stratum runs larger
than planned. The fully-reviewed variant (~2,024 sessions, ~$10k–12.5k)
remains the reference ceiling; the deferred ~750–800 reviews move to the
Beyond-v5.1 full-validation campaign, runnable in any increments later.
Platform-observed usage is reported if exposed; otherwise the limitation is
stated (v3/v5 policy carries forward).
