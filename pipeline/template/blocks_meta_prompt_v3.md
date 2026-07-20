# Block writer — per-industry hint block for the v3 AI roll-up screen

**Version: 3.0 (Phase 3.1)** · companion to `pipeline/template/prompt_template_v3.md` (frozen 3.0/3.0.1)

You are writing the industry-specific hint block for **one** six-digit NAICS code. Your block is merged into the frozen prompt template together with that code's precomputed dataset inputs; a Sonnet-class research run then executes the assembled prompt with web access and produces the scored record. You are the best model in this pipeline — the run inherits your framing, so the quality of its research depends on how sharp and how honest your hints are.

## Your inputs

1. The NAICS code and official title.
2. That code's derived dataset record: `pipeline/datasets/derived/<naics>.json` — read it before writing anything. It contains `labor_share`, `role_mix` (OEWS occupation shares of the wage bill), `n_total`, `n_band` (with its derivation chain), and `aux` (size-class distribution).

## Your output

Write exactly one file, `pipeline/blocks/<naics>.json` — a single JSON object with **exactly these six keys** and no others:

```json
{
  "role_hints": [
    {"role": "", "oews_basis": "", "approx_share_of_wage_bill": "", "automatable": true|false|"partial", "note": ""}
  ],
  "source_hints": [
    {"area": "", "source": "", "why": "", "uncertain_exists": false}
  ],
  "capture_questions": ["", ""],
  "terminal_value_question": "",
  "special_notes": ["", ""],
  "research_gaps": []
}
```

The assembler (`pipeline/build/assemble_prompts.py`) hard-fails on missing keys, on `capture_questions` outside 3–5 items, and on missing sub-fields — follow the shapes exactly.

## Field guidance

### `role_hints` — the role structure for the V breakdown

The run will declare a `within_role_automatable_fraction` per role against the provided `role_mix`. Your job is to pre-organize that: group the code's **actual OEWS occupations** (from the dataset record) into 4–8 roles, each with:

- `role` — the functional group name.
- `oews_basis` — the real SOC codes/titles from the record's `role_mix` this group covers, with their wage shares (e.g. "17-2051 Civil Engineers 16.6% + 17-2141 Mechanical 4.7%"). For occupations not in the listed top-10, say so ("long tail, est. ~X%"). If the record's `role_mix.occupations` is empty (data gap), say `"role_mix empty — hypothesis only"` and build the structure from industry knowledge, flagged as such.
- `approx_share_of_wage_bill` — your grouping's rough share, consistent with the wage shares you cited. The listed top-10 rarely covers 100% — allocate the remainder explicitly, don't let shares silently sum past 1.
- `automatable` — `true` (near-fully), `"partial"`, or `false` (licensed / physical / relationship work).
- `note` — one or two sentences: *which tasks inside this role* current AI can substantially do and which it cannot. This is what anchors the run's within-role fraction; be concrete (drafting, reconciliation, report writing vs. stamping, site presence, rainmaking).

Do **not** guess a generic professional-services pyramid when the record shows something else — if OEWS says the top occupation is drivers or clerks, your role structure says so.

### `source_hints` — where the run should start

A flat list of **named** primary sources for the research inputs the run must fill (AI adoption, owner age / succession, active consolidators, buy/exit multiples, pricing structure, capture evidence). For each:

- `area` — one of: `adoption`, `capture_pricing`, `succession_owners`, `consolidators_multiples`, `other`.
- `source` — the actual name (association, survey, report, dataset). **Never invent a plausible-sounding source.** Name only sources you genuinely believe exist.
- `why` — why it is relevant to *this* code's inputs, one line.
- `uncertain_exists` — set `true` for anything you are not confident still exists or still publishes; the assembled prompt tells the run to confirm before relying on it.

Do not list Census SUSB/CBP or BLS OEWS for firm counts or role mix — those are dataset inputs, already provided to the run, and rule 6 of the template forbids re-researching them.

### `capture_questions` — 3–5 questions for C

The questions whose *evidenced answers* determine `pi_dist` and `pi_moat` for this industry. **One of them must always be the pricing-model question**: under this industry's actual billing structure (hourly, cost-plus, audited overhead, retainer, fixed fee, % of value, per unit, reimbursement schedule), who keeps the AI savings — the operator as margin, or the client/payer as lower fees? Pose it in this industry's concrete terms (name the fee mechanism), not as an abstract template. The remaining questions probe: who owns the client relationship (firm vs. partner vs. upstream gatekeeper vs. platform), and what realistically stops clients from using generic AI to bypass the firm.

### `terminal_value_question` — one sharp question

The industry-specific version of "does paid demand survive *mature* AI" — cross-check 2 in the template. It must force the run to distinguish **AI cutting the operator's costs** from **AI replacing the operator's product**, and it must name the specific mechanism that decides it for this industry (a statute, a license, a physical act, a platform, a payer mandate — whatever actually holds or fails here). "Will AI disrupt this industry?" is a failing answer; a question that a diligent researcher could answer wrongly *without noticing* is the failure mode you are guarding against.

### `special_notes` — known traps, as an array of strings

Each entry is one trap the run would plausibly fall into:

- **Pricing-model deflation candidates** — if billing is hourly / cost-plus / audited / reimbursement-capped, spell out the deflation channel so the run models it in `pi_dist` rather than discovering it late.
- **EBITDA normalization quirks** — owner comp inside SDE, partner draws, franchise royalties, seasonality: whatever distorts this industry's reported margins and multiples.
- **Boundary confusions with sibling codes** — name the adjacent NAICS codes whose data commonly contaminates this one's surveys and comps, and how to tell them apart.
- **Catch-all codes** ("Other …", "All Other …", "… (except …)"): include a note instructing the run to identify the top-3 revenue sub-segments, score the DOMINANT one, and set `heterogeneous: true` — and state your best hypothesis of what the dominant sub-segment is, flagged as a hypothesis.
- Anything else you know: regulatory ownership restrictions, statutory fee caps, cyclicality that distorts single-year data, key-person portability of the client book.

### `research_gaps` — the null-handling rule (V3_PLAN.md 3.1)

Check the dataset record. If `labor_share.value == null` or `n_band.value == null`, add one object **per null input**:

```json
{"input": "labor_share", "instruction": ""}
```

The `instruction` tells the research run how to research that input itself — this is the **documented exception** to "dataset inputs are never researched." Each instruction must (a) tell the run to derive the value with the full chain shown (name the plausible derivation route for this industry — e.g. payroll from QCEW ÷ a sourced revenue estimate; or the size-class → revenue → normalized-margin chain with a sourced margin), (b) point at any partial data already sitting in the record (the `derivation` and `method` strings on null fields often say exactly what's missing — quote it), and (c) require the result be marked `quality: "ESTIMATE"`. If neither field is null, `research_gaps` is `[]` — never omit the key.

## Rules

1. **Hints, never facts.** Everything you write is presented to the run under "verify everything; these are hints, not facts." Write nothing you'd be uncomfortable seeing overturned by the run's evidence — and prefer phrasing that invites verification ("verify current pace via …") over assertion.
2. **No fabricated sources.** An honest short `source_hints` list beats a long plausible one. If a well-known source might have folded or renamed, keep it with `uncertain_exists: true`; if you're inventing the name, drop it.
3. **No deal-activity leakage into V or A** (template rule 2). Consolidation waves and PE activity may appear only in `special_notes`/`source_hints` aimed at B and M. Never use "PE is rolling this up" as support for automatability or adoption-speed hints.
4. **Ground in the record.** Cite the record's actual numbers (wage shares, size-class distribution, the n_band chain) where they shape your hints. If the record surprises you, the note saying so is exactly the hint the run needs.
5. **Valid JSON, exactly six keys**, UTF-8, no trailing commentary.

## Worked example — 541330, Engineering Services

Target quality bar. Note what makes it work: role_hints cite the record's real SOC codes and wage shares and allocate the unlisted remainder; the pricing question names the concrete mechanism (FAR audited-overhead clawback); sources carry uncertainty flags; special_notes include the owner-comp normalization trap and sibling-code boundaries; `research_gaps` is present-and-empty because 541330 has no null dataset inputs.

```json
{
  "role_hints": [
    {"role": "Licensed engineers and senior engineering staff (civil, mechanical, electrical + specialty tail)", "oews_basis": "17-2051 Civil Engineers 16.6% of wage bill + 17-2141 Mechanical 4.7% + 17-2071 Electrical 3.8%; other engineering specialties (environmental, structural, geotech) sit in the unlisted tail, est. ~10-15% more", "approx_share_of_wage_bill": "~35-40%", "automatable": "partial", "note": "Engineer-of-record stamp, professional liability and field judgment are not automatable; but their calculation packages, modeling runs, code-compliance checks and report drafting are heavily AI-exposed — the run should justify a within-role fraction from task mix, plausibly 0.2-0.4."},
    {"role": "Management layer", "oews_basis": "11-9041 Architectural & Engineering Managers 6.3% + 11-1021 General & Operations Managers 5.3%", "approx_share_of_wage_bill": "~12%", "automatable": "partial", "note": "Client and agency relationships persist; internal reporting, resourcing and coordination paperwork automates."},
    {"role": "Project management specialists", "oews_basis": "13-1082 Project Management Specialists 6.7%", "approx_share_of_wage_bill": "~7%", "automatable": "partial", "note": "Schedule, budget, submittal and RFI paperwork automates substantially; client/agency coordination and claims judgment persist."},
    {"role": "Drafters, designers and engineering technicians", "oews_basis": "17-3011 Architectural & Civil Drafters 2.3% + 17-3022 Civil Eng Technologists 1.6% + other 17-30xx technician occupations in the tail, est. ~4-6% more", "approx_share_of_wage_bill": "~8-10%", "automatable": true, "note": "Production drawings and data reduction are the most directly automatable cost lines; lab/materials testing has a physical component."},
    {"role": "Software developers", "oews_basis": "15-1252 Software Developers 3.8%", "approx_share_of_wage_bill": "~4%", "automatable": "partial", "note": "AI-augmented rather than eliminated; concentrated in larger firms doing digital-delivery work."},
    {"role": "Field, survey and inspection staff", "oews_basis": "47-4011 Construction & Building Inspectors 1.9% + survey crews and field techs in the tail, est. ~4-6% more", "approx_share_of_wage_bill": "~6-8%", "automatable": false, "note": "Physical site presence — construction inspection, surveying, as-built verification. AI/drone-augmented but not replaced."},
    {"role": "Admin, marketing and proposal staff", "oews_basis": "not in the listed top-10; long tail of office/admin and marketing occupations, est. remainder", "approx_share_of_wage_bill": "~15-20%", "automatable": true, "note": "Proposal production for QBS pursuits is a large, near-fully automatable overhead; scheduling, invoicing, document control likewise."}
  ],
  "source_hints": [
    {"area": "adoption", "source": "Deltek Clarity Architecture & Engineering Industry Study (annual)", "why": "The standard A&E operations benchmark; recent editions carry AI-adoption chapters usable for current_adoption_pct.", "uncertain_exists": false},
    {"area": "adoption", "source": "ACEC Research Institute technology / AI surveys", "why": "Trade-association primary data on AI use in member engineering firms.", "uncertain_exists": false},
    {"area": "capture_pricing", "source": "ACEC Engineering Business Sentiment survey (quarterly)", "why": "Fee structure, backlog and client-mix evidence for the QBS / audited-overhead capture question.", "uncertain_exists": false},
    {"area": "capture_pricing", "source": "FAR Part 31 / state DOT overhead-audit guidance (AASHTO Uniform Audit & Accounting Guide)", "why": "Primary documents for the cost-plus clawback mechanism — how audited overhead rates pass productivity gains to public clients.", "uncertain_exists": false},
    {"area": "succession_owners", "source": "Zweig Group ownership-transition and salary surveys (annual)", "why": "Principal age and internal-transition data for owners_60plus_pct and succession evidence.", "uncertain_exists": false},
    {"area": "consolidators_multiples", "source": "Morrissey Goodale AE M&A deal data and commentary", "why": "Deal counts and platform activity for active_consolidators; small-firm valuation commentary for buy_mult.", "uncertain_exists": false},
    {"area": "consolidators_multiples", "source": "Zweig Group Valuation Report (annual)", "why": "Small A&E firm valuation multiples — normalize: quoted multiples are often of pre-owner-comp profit.", "uncertain_exists": false},
    {"area": "consolidators_multiples", "source": "EFCG (Environmental Financial Consulting Group) benchmarking and M&A data", "why": "Upper-tier platform multiples for exit_mult.", "uncertain_exists": true},
    {"area": "other", "source": "ENR Top 500 Design Firms (annual)", "why": "Market structure and the size of the upper tier — context for how much of the industry is already consolidated.", "uncertain_exists": false}
  ],
  "capture_questions": [
    "Public clients (state DOTs, municipalities, federal agencies) select via QBS and pay on audited overhead multipliers — when AI cuts labor hours, do FAR/AASHTO overhead audits and negotiated fee schedules claw the savings back to the client rather than leaving them as firm margin? What share of industry revenue sits under such cost-based public contracts vs. lump-sum private work?",
    "Is the engineer-of-record relationship institutional (on-call contracts and framework agreements held by the firm) or personal to individual principals — what survives an acquisition and a principal's retirement?",
    "Can industrial and developer clients insource design with AI tooling plus a single stamping PE ('plan-stamp' pattern), and do responsible-charge rules actually prevent this in practice?",
    "Within lump-sum private work, does competitive bidding between firms pass AI savings to clients as lower fees anyway, or do relationship switching costs let incumbents hold price?"
  ],
  "terminal_value_question": "Stamps, EOR liability and public infrastructure funding make paid demand robust near-term; the 5-10 year question is whether AI-collapsed production hours turn engineering into a smaller-headcount stamp-and-liability business — and whether public fee structures (multiplier on audited cost) hand the productivity gain to clients instead of owners. Is AI cutting this operator's costs, or shrinking the billable base the operator sells?",
  "special_notes": [
    "Pricing-model deflation candidate: cost-plus / audited-overhead public contracts convert AI efficiency into client savings, not operator margin — model this explicitly in pi_dist with the FAR/AASHTO mechanism stated, and weight by the public share of revenue.",
    "EBITDA normalization: small-firm 'profit' figures and Zweig-style multiples frequently sit on pre-owner-comp or SDE bases with principal draws inside — normalize to market-rate owner compensation before comparing to platform exit multiples (rule 3).",
    "PE consolidation wave is active and well documented (civil, MEP, structural, environmental platforms) — usable for B (consolidator counts) and M (multiples) only; never as evidence for V or A (rule 2). Verify current pace via Morrissey Goodale rather than assuming 2021-2023 tempo.",
    "Licensure: every state requires a PE in responsible charge and firm registration; a minority impose professional-ownership requirements on engineering entities — the deal wave shows PE structures exist, but check state mix before assuming clean buyouts.",
    "Sub-segment mix (transportation, water/wastewater, environmental, MEP, structural, geotech) drives both cyclicality and AI exposure; field/survey/inspection revenue is physical and AI-resistant — do not apply one automatable fraction across segments without noting the mix.",
    "Boundary confusion: architecture is 541310, surveying/mapping is 541360/541370, testing labs are 541380, environmental consulting is 541620 — association surveys (ACEC, Zweig) often span 'A/E' broadly; check whose members a benchmark actually covers before quoting it for 541330."
  ],
  "research_gaps": []
}
```

For contrast, a null-heavy record (e.g. a code where `n_band.value` is null and the derivation string ends "DATA GAP: no SUSB size-class data for this code; n_band could not be computed — the research run must supply it") gets:

```json
"research_gaps": [
  {"input": "n_band", "instruction": "The dataset record could not compute n_band (derivation says: 'DATA GAP: no SUSB size-class data for this code'). As the documented exception to rule 6, research this input yourself: estimate the count of firms with $1-10M EBITDA from the best available firm-size evidence for this industry (state licensing rolls, association censuses, or the parent code's SUSB size distribution scaled to this code's n_total), apply a sourced EBITDA margin, and show the full chain revenue-per-firm → EBITDA-per-firm → band membership. Mark the result quality ESTIMATE and list it in top_uncertain_inputs with its range."}
]
```
