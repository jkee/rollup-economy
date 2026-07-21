# AI Value Migration Map — v3: Product Goal & Principles

**Status:** active constitution; v3.1.2 Phase 4 completed 2026-07-21 under the bounded contract (82 published, 1 explicitly excluded; final validated checkpoint `009d088` pushed to origin); the v3.1.1 comparable canary remains a frozen historical mechanics PASS / fleet-readiness FAIL (0/5 accepted)
**Replaces:** the project description in `README.md` and the Methodology tab in `6digit/index.html`. Diff against the current (v2) description is in §8. File:line references are as of commit `1bd26e0`.

---

## 1. Product goal

**A ranked, evidence-backed map of all 1,012 six-digit NAICS US service industries by AI roll-up attractiveness — where every score can be traced to its sources, recomputed from its inputs, and checked by anyone.**

For any industry on the map, a reader must be able to answer four questions without leaving the dashboard:

1. **How attractive is it?** — the score and verdict.
2. **Why exactly?** — a readable research memo explains the thesis; each factor still traces through its formula and compact scorecard inputs to the supporting source registry and any caveats.
3. **How sure are we?** — confidence level, sensitivity ranges on the most uncertain inputs, borderline flags.
4. **How was it produced and checked?** — which prompt, exact model and date; its publication tier and caveats; re-runnable from the stored packet and deterministic finalizer.

The output of the product is a decision about **which industries deserve a deep-dive** — nothing more.

## 2. Scope — what this project is not

- **It does not select companies.** The unit of analysis is the industry (6-digit NAICS). No founder access, no target lists, no company-level underwriting. Anything company-level happens outside this project.
- **It does not validate prior intuition.** v2 listed "validate intuition — sub-sectors we've already deep-dived should match scores here" as a purpose (`README.md:29`). That purpose is removed: it is how target-fitting entered the data (215 records carry an explicit `Target:<bucket>` in their audit notes). v3 has one purpose — rank industries from evidence.
- **It is not an underwriting tool.** Green means "deep-dive next", never "buy".

## 3. Principles

**P1 — Scores are build artifacts.** No score may be set by judgment. Every factor is: recorded inputs → fixed formula → score. Judgment goes into *finding and weighing inputs* and into reviewer notes — never into overriding arithmetic. Consequence: scores cannot be hand-edited at all; to change a score you change an input (with a source), and the build recomputes. Judgment does not disappear in v3 — it is confined and labeled: a short, known list of inputs are declared opinions (within-role automatable fractions, `π_dist`, `π_moat`, `t50`), each bounded, with its own rationale, range and quality flag. Everything downstream of the inputs is arithmetic. Proven: the mechanical version produced identical dentist scores across two independent runs, and surfaced the cost-plus capture mechanism for Engineering Services that judgment scoring missed.

**P2 — Every score input carries its provenance.** The v3.1.2 compact scorecard records each selected `value`, method (`OBSERVED/CALCULATED/ESTIMATE`), evidence reliability (`HIGH/MED/LOW/NONE`), plausible range, confidence, rationale and supporting source IDs. A compact source registry records `id`, URL, title, access date and what the source supports. Exact quotations are optional, and forensic population/geography/unit/period objects and serialized search/bridge logs are no longer required. Material scope or proxy mismatches must instead be disclosed as prose caveats on the affected input. Provenance answers how a value relates to evidence; evidence quality answers how reliable that evidence is. The dashboard keeps the full chain: verdict → score → factors → formulas → inputs → rationale → sources and caveats.

**P3 — Reproducible by construction.** Everything needed to regenerate a result lives in the repo: the versioned prompt, one canonical model-authored v3.1.2 research packet, the deterministic dataset, the finalized run record with model/date/run id, the rendered Markdown memo, and the Python finalizer/build. The packet is the sole model-authored source for both prose and numbers, so they cannot drift. The model cannot author dataset values, role weights, contributions, factor scores, S, uplift or verdict. Plain Python validates the packet, safely recomputes declared calculations, injects deterministic values, computes every downstream field and renders the memo bit-for-bit. Neither a model nor a human may hand-edit a finalized record or rendered memo.

**P4 — Frozen rubric (pre-registration).** Formulas, anchors, gates and verdict cuts are frozen *before* the scoring run and never tuned after seeing which industries land where. (v2 chose its ×1.8 threshold explicitly to preserve the previous verdict-bucket proportions — that is back-fitting; it is banned.) Rubric changes are allowed only as a new version followed by a full re-run.

**P5 — Continuous everywhere.** Factors and scores are floats end-to-end; rounding happens only at display time (one decimal). No integer snapping inside formulas — v2's `round()` at each factor, amplified by multiplication, produced verdict flips from ±1 accidents.

**P6 — Weak links gate; they are not averaged away.** The economic logic of "any near-zero factor kills the thesis" stays. But a top verdict must *actually* mean "no weak factor": per-factor minimum gates, a terminal-value gate, and a confidence gate are enforced explicitly, not implied by a product threshold (v2's Hell-Yes admitted M=4: 9×8×8×10×4 clears the bar).

**P7 — Uncertainty is part of the result.** Overall confidence (`HIGH/MED/LOW`) is a first-class output metric of every run — shown on the card next to the score, and gating: `LOW` caps the verdict at Conditional. Each run names its most uncertain inputs with plausible ranges and the score impact. Verdicts near a cut are flagged `borderline`, not silently binned.

**P8 — One source of truth.** Thresholds, formulas and distribution stats are defined once (in the build), and every displayed or documented number — README verdict counts, methodology tables, dashboard stats — is generated from the data. No hand-maintained copies. (v2: README says 83 Hell-Yes and a 4-factor formula; the shipped data computes 22 Hell-Yes with 5 factors; the methodology page carries three contradictory threshold ladders.)

**P9 — Cheap by default, expensive where it matters.** The current fleet-research model is Terra (`gpt-5.6-terra`). Sol (`gpt-5.6-sol`) is used where quality compounds: prompt design/review, golden reference runs and full-depth tiered publication validation. Dataset derivation, prompt assembly, finalization, memo rendering, build and analysis are plain Python only; models are prohibited in those deterministic stages. Every model-authored artifact records the exact runtime model ID, and pricing/token burn are reported only from platform-observed campaign data.

**P10 — Nothing ships unreviewed; review is materiality-based and bounded.** Sol (`gpt-5.6-sol`), prompted as a critic, reviews every exact packet/run/memo artifact and every score-driving source. It assigns `publishable`, `publishable_with_caveats`, `reject` or `invalid` with reasons and explicit materiality. Both publishable tiers enter the product, with caveats visible. Only a defect likely to change the score or thesis may cause `reject`; deterministic contract failures cause `invalid`. Rejected or invalid records receive at most one record-specific remediation attempt. Remaining failures are excluded and reported instead of keeping the campaign open.

## 4. The factors — corrected semantics

One score per industry. The 13-cell APQC workflow matrix is removed (see §8, "Unit of analysis"). Workflow detail survives where it carries evidence: inside V's role-by-role automatability breakdown.

| Factor | Measures | Computed from |
|---|---|---|
| **V** — Value freed | Share of industry revenue AI can free up | `labor_share × ai_replaceable_share`, where replaceable share is itemized by occupation (BLS OEWS role mix × within-role automatable fraction). Anchor: freeing ≥25% of revenue = 10. |
| **C** — Value kept | Share of freed value the *operator* keeps | Two questions, answered with evidence: (a) **pricing/contract structure** — does the billing model let the operator keep savings (fixed fee/retainer) or hand them to clients (cost-plus, audited overhead, pure hourly)? (b) **bypass/squeeze resistance** — client-relationship control (`π_dist`) and moat vs generic-AI bypass (`π_moat`). |
| **A** — Adoption speed | Years until 50% of firms materially adopt AI in the automatable functions | `A = 10 / t50`; `t50` derived from measured current adoption (industry surveys) + historical technology analogs, derivation shown. Historically the widest error bar — its plausible range and score impact are mandatory in every record. |
| **B** — Buyability | Are there enough acquirable targets | Firms in the **$1–10M EBITDA band** derived from Census SUSB size distributions (not raw firm counts), owner age / succession pressure, minus a competition penalty for active PE consolidators. **The price-spread subfactor (PD) is removed from B — pricing signal lives only in M.** v2 double-counted the buy/exit spread in both B and M. |
| **M** — Multiple arbitrage | Buy-to-exit multiple spread | `(exit_mult − buy_mult) / buy_mult`, from sourced transaction data, EBITDA normalized after market-rate owner compensation. |

**Where each input comes from — three declared classes:**

- **Dataset inputs** — deterministic; computed identically for all 1,012 codes from bulk extracts in `pipeline/datasets/` (Census SUSB/CBP, BLS OEWS/QCEW): `labor_share`, the role mix behind V's breakdown, `n_total`, the size-class distribution behind the `n_band` chain. No model touches these values.
- **Research inputs** — collected in the compact scorecard, each with selected value, method, rationale, plausible range, confidence, source IDs and any material scope/proxy caveat: current AI adoption, historical analogs, owner age / succession, active consolidators, buy/exit multiples, pricing-structure and capture evidence.
- **Judgment inputs** — declared opinions, bounded and itemized, each with rationale and range: within-role automatable fractions, `π_dist`, `π_moat`, `t50`. Stated plainly: opinions still exist in v3 — but only here, in small visible pieces challengeable one by one, never at the score level.

Two gates sit outside the score:

- **T — Terminal value** (`DURABLE / PRESSURED / MELTING`): does demand for the service survive *mature* AI — is AI cutting the operator's costs, or replacing the operator's product? v2's top list is full of melting businesses (court reporting, telemarketing, translation). `MELTING` caps the verdict at Pass; `PRESSURED` caps at Strong.
- **Confidence** (`HIGH / MED / LOW`): `LOW` caps the verdict at Conditional. In v2 confidence was a visual badge with zero effect on ranking.

Standing rules (carried from the proven v2 template): PE deal activity may inform only B and M, never V or A; all margins/multiples EBITDA-normalized after owner comp; catch-all codes score their dominant sub-segment and carry a visible `heterogeneous` flag on the card.

Exact functional forms, gates and cuts remain the v3.0 freeze. Evidence-contract versions may tighten authoring and validation mechanics, including the already-at-50% t50 boundary, but do not tune thresholds after seeing outcomes.

## 5. The score and verdicts

**S = (V × C × A × B × M)^(1/5)** — the geometric mean, a float on the 0–10 scale.

Multiplicative logic is kept deliberately — a sum would let strong V compensate C≈0 (the mortgage-processor trap). What v3 removes is each specific bias layered on top of it in v2:

| Bias in v2 | Fix in v3 |
|---|---|
| Integer rounding at each factor, round-half-up, amplified by the product | Floats end-to-end (P5) |
| Error amplification: five slightly-optimistic factors compound to ~×1.6 on S | Sensitivity ranges reported per record (P7). The geometric mean also reads on the familiar 0–10 scale — its ordering is identical to the product's, so the ranking de-bias comes from floats, corrected semantics and gates, not from the mean itself |
| Compensation at the top: product threshold ≠ "no weak factor" | Explicit per-factor gates + T gate + confidence gate (P6) |
| Double-counting: buy/exit spread inside both B (PD) and M | Spread lives only in M (§4) |
| Knife-edge verdicts: ±1 on one factor flips the bucket (6 of 22 current Hell-Yes die on a single −1) | Continuous S, a `borderline` zone around every cut (P7) |
| Thresholds back-fitted to preserve v1 bucket proportions (×1.8) | Absolute cuts frozen before the run, defined on scale semantics ("all factors good"), never on outcomes or bucket shares (P4) |

**Verdicts** keep the familiar names, but are defined as *gates + frozen absolute cuts* on the 0–10 S scale — never percentiles. Percentile-based verdicts would guarantee a fixed share of green regardless of absolute quality, and re-running one code could flip another code's verdict; in v3 a code's verdict depends only on its own record. Percentile appears on the card as context ("top 4% of the economy"), never as the definition. Decided cuts (2026-07-20), frozen at Stage 0:

- **Hell-Yes** — S ≥ 7.0 and every factor ≥ 6.0, T = DURABLE, confidence ≥ MED.
- **Strong** — S ≥ 5.5 · **Conditional** — S ≥ 4.0 · **Pass** — S ≥ 3.0 — each subject to the caps from T and confidence.
- **KILL** — S < 3.0, or any factor below its floor (e.g. B = 0: not acquirable; C near 0: value flows elsewhere), or MELTING + weak economics.
- Any record within ±0.15 of a cut is additionally flagged **`borderline`** and shows its sensitivity range.

## 6. The pipeline

Six stages; v3.1.2 adds versioned artifacts and does not mutate the frozen v3.0, v3.1 or v3.1.1 layers:

```
pipeline/
  template/prompt_template_v3_1_2.md    # text-first packet contract; frozen formulas retained
  template/runner_brief_v3_1_2.md       # canonical packet authoring brief
  template/validator_brief_v3_1_2.md    # tiered, materiality-based review brief
  datasets/                             # stage 1 — bulk Census SUSB/CBP + BLS OEWS/QCEW extracts
                                        #   + derivation code → per-code dataset inputs
  blocks/<sector>.json                  # per-industry hint blocks (stage 2 output)
  prompts_v3_1_2/<naics>.md             # one plain-Python-assembled prompt per fleet code
  packets/<naics>/<run-id>.json         # canonical model-authored prose + scorecard + sources
  runs/<naics>/<run-id>.json            # Python-finalized fleet inputs + scores
  golden_v3_1_2/<naics>/<run-id>.json   # isolated Python-finalized Sol reference runs
  memos/<naics>/<run-id>.md             # Python-rendered human-facing research memo
  review/<naics>/<run-id>.json          # stage 5 — four-tier exact-artifact review
  build/                                # stage 4 — deterministic build + checks
6digit/six_data_v3.json                 # GENERATED — the site's v3 view; never hand-edited
```

- **Stage 0 — Freeze.** Template v3 finalized: formulas, anchors, gates, verdict cuts, output schema, golden-set membership, validator rubric. Frozen before any scoring.
- **Stage 1 — Dataset layer (no model).** Bulk-download Census SUSB/CBP and BLS OEWS/QCEW once into `pipeline/datasets/`; derive the dataset inputs (labor share, role mix, firm counts, size distribution → $1–10M band chain) for all 1,012 codes with one shared method. These values are injected into prompts and never re-researched by a model — one methodology across all codes is what makes the ranking comparable.
- **Stage 2 — Prompt design and assembly.** Sol (`gpt-5.6-sol`) designs and independently reviews the versioned prompt, packet and validator contract. Plain Python deterministically merges blocks and dataset context into exactly 63 Phase-4 prompts under `prompts_v3_1_2/`; models are prohibited from assembly. The prompt layer must rerender byte-identically before it is frozen.
- **Stage 3 — Canonical research packet (Terra fleet; isolated Sol golden).** A single-author model with live web access writes `packets/<naics>/<run-id>.json`. Its prose sections are: executive view; how AI changes the work; value capture; adoption timing; consolidation and economics; terminal demand; and risks and uncertainty. The same packet contains the compact scorecard and source registry. Every score input carries a selected value, plausible range, confidence, method, rationale, source IDs and any scope/proxy caveat. Material factual and numeric claims require source IDs; exact quotations are optional. Fleet packets must identify `gpt-5.6-terra`; golden packets must identify `gpt-5.6-sol` and remain isolated from golden membership and prior conclusions.
- **Stage 4a — Finalize and render (plain Python, no model).** The v3.1.2 finalizer validates packet schema/identity/model/version, safe calculations and scorecard bounds; injects immutable dataset objects and locked SOC role weights; computes contributions, V/C/A/B/M/S, uplift, gates and verdict; then renders `memos/<naics>/<run-id>.md` from the same packet and finalized run. A fresh rerun must reproduce both the record and memo exactly. Hand edits are prohibited.
- **Stage 4b — Build (plain Python, no model).** Validates the versioned final schema, independently recomputes every score, applies the frozen gates/cuts and publishable-tier filter, and regenerates site/stats/flags/reconciliation and completion-report outputs. It includes `publishable` and `publishable_with_caveats`, exposes their caveats, and excludes remaining `reject`/`invalid` artifacts by exact run ID.
- **Stage 5 — Tiered review (isolated Sol, every record).** Sol (`gpt-5.6-sol`) reviews every exact packet/run/memo identity, each score-driving source, rubric direction and possible double counting. Its outcome is `publishable`, `publishable_with_caveats`, `reject` or `invalid`. A rejection reason must explain why the defect could materially change a factor, score or thesis; otherwise the issue is a caveat. Each record is independently reviewed once, with at most one new-run remediation and re-review for `reject`/`invalid` only.

**Phase-4 execution and golden set.** First run the same five regression-canary codes (`524210 541110 541350 541612 541613`). This gate tests mechanics only: all five must yield schema-valid packets and freshly reproducible final records and memos with zero arithmetic mismatch. Subjective research findings set publication tier but do not stop the fleet. Once mechanics pass, the five valid canary artifacts count toward the 63-record Terra fleet; run the remaining 58 once, plus 20 isolated Sol golden records, then obtain one exact-artifact Sol review per record. Golden separation remains a reported diagnostic, not a trigger for an open-ended rerun loop. The frozen golden membership, datasets, formulas, factors, thresholds and gates do not change.

**Bounded remediation and close.** Only `reject` or `invalid` records may receive remediation. Attach the concrete review findings, author a new packet with a new run ID using the same research model class, rerun deterministic finalization/memo rendering, and obtain a new isolated Sol review. There is exactly one remediation attempt per record and no third attempt. After that wave, include both publishable tiers, exclude remaining failures, list every exclusion and caveat in generated output, and close Phase 4 even if publication is below 83/83.

**Run metadata** on every packet, finalized record, memo and review binds the NAICS code, artifact/run ID, exact model ID where applicable, run date, template/prompt/review version and review date. Two runs of the same code sit side by side; remediation never overwrites an earlier artifact. Source-registry entries carry access dates. Market evidence older than about 12 months is reported as a caveat/refresh signal unless Sol explains why it materially changes the result.

**Dashboard requirements** (traceability is a product feature, not an internal artifact): the generated memo is the primary readable explanation; every factor chip expands to formula + compact scorecard inputs; every input shows rationale, method, range, confidence, supporting sources and caveats. Cards show run metadata, publication tier, overall confidence, `borderline` and `heterogeneous` flags, sensitivity ranges, and percentile as context next to the absolute verdict. `publishable_with_caveats` must be visibly distinct, exclusions must appear in the completion report, and strings that are not URLs are never rendered as links.

## 7. How results are checked

1. **Arithmetic regression (CI).** The build recomputes all scores from inputs on every change; any mismatch between stored and recomputed values fails the build. Hand-edits to scores are structurally impossible (P1).
2. **Packet cross-checks.** Every packet must address uplift consistency (V_raw → expected EBITDA pp vs A), terminal value, V/A evidence independent of deal activity, and pricing-model deflation. A disclosed non-material weakness becomes a caveat; only a score-changing contradiction becomes `reject`.
3. **Sensitivity.** Top uncertain inputs carry plausible ranges + score impact; ranges that cross a verdict cut ⇒ `borderline`.
4. **Reconciliation.** Generated report comparing screen verdicts against deep-dives; divergence is surfaced, not discovered by accident.
5. **Tiered publication review.** Every record receives an isolated full-depth Sol review (P10, Stage 5). Fatal mechanics are narrowly deterministic: wrong identity/model/version, schema failure, mutated datasets/roles, invalid or non-finite inputs, unsafe calculation, finalizer mismatch or arithmetic mismatch. These always yield `invalid`. Material research defects are fabricated/inaccessible score-driving evidence, unsupported material numeric claims, reversed factor semantics, undisclosed score-changing proxies/contradictions, or thesis-changing terminal/capture double counting. These yield `reject` only with a materiality explanation.
6. **Caveat policy and golden diagnostic.** Punctuation or normalized-quotation differences, page-title variants, conservative `not reported` metadata, incomplete search logs, source age, broad-but-disclosed proxies, non-material scope weakness and incomplete bridge prose are caveats unless the validator explains their score-changing effect. Golden separation is reported as an external diagnostic; it does not create an unbounded repair loop or authorize hand-fixing records.
7. **Doc consistency.** README counts, methodology tables and thresholds are generated from the same build (P8) — they cannot drift from the data.

## 8. Diff against the current (v2) description

**Purpose.**
v2: dual purpose — "discover blind spots" *and* "validate intuition: deep-dived sub-sectors should match scores here" (`README.md:26-29`).
v3: single purpose — rank industries from evidence. Validation-of-intuition is removed as a goal because it institutionalized outcome leakage: 225 records carry audit notes, 215 of them with an explicit `Target:<bucket>` alongside manual factor edits.

**Unit of analysis.**
v2: 13 cells per industry (NAICS × APQC category); verdict from "≥2 green cells" plus ΣS thresholds (`6digit/index.html:374,387`). All 13 cells derive from one V/A via universal workflow modifiers, so the "two green cells" rule is one signal counted twice — all 22 current Hell-Yes verticals get their green pair from the near-identical Customer Service and Finance modifiers.
v3: **one record per industry**; the matrix is deleted. Workflow granularity survives as evidence inside V's role-by-role breakdown, where it is actually sourced (OEWS role mix) instead of a universal coefficient.

**Where scores come from.**
v2: five integers assigned per code by agent judgment, one rationale paragraph, a flat source list attached to nothing; documented formulas (`π_dist`, `t_50`, `TD/OW/PD/CFD`) exist only as prose — none of their inputs are stored, so nothing is recomputable. Same facts produced three different dentist scores across edits.
v3: 13 inputs per code (dataset inputs computed identically for all codes from bulk Census/BLS extracts; research inputs sourced by the run; judgment inputs declared and bounded) → frozen formulas → float scores; the score is derivable from the record (P1–P3), and every shipped record has a publishable-tier Sol review (P10).

**Factor semantics.**
v2: C described as distribution×moat but scored as opinion — pricing/contract structure ignored (hourly and cost-plus industries scored as if the operator keeps AI savings). B described as "$1–10M EBITDA band" (`6digit/index.html:429-431`) but scored from raw firm counts — 20 of 22 Hell-Yes codes have median firms far below the band; the competition penalty effectively never applied; PD inside B duplicated M's spread. No terminal-value concept — melting industries (court reporting, telemarketing, translation) ranked at the top.
v3: C explicitly models *who keeps the savings* (pricing structure first); B counts band-eligible firms from SUSB size distributions and drops PD; T gate catches melting businesses; deal activity banned as evidence for V/A (§4).

**Score & verdicts.**
v2: integer product 0–100,000; three mutually inconsistent threshold ladders on one page (card-level `:387`, cell-level `:478`, legacy 4-factor derivation `:490-508`); ×1.8 recalibration chosen to preserve old bucket shares; Hell-Yes claims "all five blocks ≥7" but admits weak links; ±1 flips verdicts.
v3: float geometric mean + explicit gates + frozen absolute cuts (percentile shown only as context) + borderline zone (§5). The "no weak factor" claim becomes enforced instead of asserted.

**Traceability.**
v2: sources are unlinked report names (70 of 1,012 records contain any URL; the current #1 has five sources, none with a URL); UI renders non-URLs as links; P&L card math is broken (comment promises 70/20/10 split, code applies 70/30/20 and double-adds revenue uplift, `6digit/index.html:1000,1012` — 951 of 1,012 post-AI P&Ls off by >0.1pp).
v3: per-input provenance, source IDs, rationale, ranges, confidence and visible caveats (P2); exact quotes are optional. The P&L display is either derived from stored inputs as a true accounting identity or dropped — no separately-guessed numbers.

**Reproducibility.**
v2: "96 specialist agents, ~3–5 min each" (`README.md:16`) — no prompts, no model/version, no run records stored; independent reproduction impossible.
v3: template + dataset extracts + per-code prompts + run records with model/date/run-id + validator verdicts + deterministic build, all in-repo (P3, §6). Re-running a code is one command away.

**Consistency.**
v2: README says 4 factors and 83 Hell-Yes (`README.md:18,22`); code multiplies 5 factors (`6digit/index.html:647`); the shipped data recomputes to 22 Hell-Yes / 69 Strong / 180 Conditional / 328 Pass / 413 KILL.
v3: all documented numbers generated from the build (P8).

**Confidence & uncertainty.**
v2: confidence is a badge (`6digit/index.html:1067`); LOW and HIGH enter the product identically; a LOW-confidence code sits in the top-10.
v3: confidence is a first-class output metric that gates verdicts; sensitivity ranges displayed; borderline flagged (P6–P7).

**Scope.**
v2: caveats gesture at company-level next steps (founder access, per-vertical P&L sheets before underwriting, `README.md:56-59`).
v3: company selection is explicitly out of scope (§2). The deliverable ends at "which industries deserve a deep-dive".

**Cost model.**
v2: one undocumented expensive pass over 96 agents.
v3: Sol (`gpt-5.6-sol`) for prompt design/review, golden-set reference runs and full-depth tiered publication review; Terra (`gpt-5.6-terra`) for fleet research; plain Python only for deterministic stages (P9–P10). Unsupported price estimates are not inferred when the platform does not expose billable usage.

## 9. Open decisions (need sign-off before Stage 0 freeze)

Resolved 2026-07-20:

1. **Cut values & factor floors** — decided: Hell-Yes S ≥ 7.0 with every factor ≥ 6.0 (stricter than initially proposed); Strong ≥ 5.5, Conditional ≥ 4.0, Pass ≥ 3.0, KILL below or any factor < 1.0. In `pipeline/build/thresholds.json`.
2. **C composition** — decided: folded. C = 10 × π_dist × π_moat, with pricing-model deflation mandatorily reflected in π_dist and the mechanism stated.
3. **P&L card** — decided: dropped for the v3 launch (broken v2 math, inputs not in the v3 schema; EBITDA-uplift economics survive as cross-check 1). May return later derived from datasets.
4. **v1 (4-digit) page** — decided: archived live with a "superseded by v3" banner.

5. **Golden set membership** — decided: the 20-code list (12 winners, 5 melters, 3 controls) in `pipeline/golden/golden_set.json`, approved as v1.0.
6. **v3.1 evidence contract** — decided after the 0/72 initial acceptance signal and the citation-hardened 541420 s3 acceptance: keep the validator strict; separate provenance type from evidence reliability; retain C1-C4 live-source self-audit; inject deterministic inputs and calculate scores in Python; prohibit role relabeling; clarify `t50=0` when adoption is already at least 50%. No threshold was changed.
7. **v3.1.1 mechanical boundary** — decided after the v3.1 canary produced 0/5 accepted despite materially better citation attribution: preserve atomic evidence facts; replace model-authored final provenance with explicit `OBSERVED/CALCULATED/ESTIMATE` methods and a Python mapping; restrict calculated values to safe reproducible arithmetic over fact-backed operands; require structured scope; mechanically reject ellipsis quotes; keep C1–C4 for the later runner brief. No threshold or scoring formula changed.
8. **v3.1.2 text-first bounded contract** — authorized 2026-07-21 after the v3.1.1 five-record canary passed mechanics but produced 0/5 accepted under the forensic all-or-nothing review. Replace the primary audit form with one canonical prose-plus-scorecard packet, retain Python-owned arithmetic and exact model/artifact identity, use four publication tiers, and permit exactly one remediation attempt for `reject`/`invalid`. Metadata and non-material evidence imperfections are visible caveats; they are not fatal by default. The campaign closes with explicit exclusions rather than requiring 83/83 publication. No frozen dataset, formula, factor, threshold, gate or golden-set member changes.

The v3.0 score freeze remains tagged (`v3.0-freeze`). Frozen v3.1 and v3.1.1 artifacts remain byte-unchanged. v3.1.2 passed synthetic tests, cold independent implementation review, deterministic 63-prompt assembly and the mechanics-only five-record canary before the complete Phase-4 campaign was launched.

---

*Next execution step: Phase 5 dashboard traceability; the bounded v3.1.2 Phase-4 campaign is complete.*
