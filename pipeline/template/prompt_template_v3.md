# Score one industry for an AI roll-up screen — NAICS {{NAICS}}, {{TITLE}} (US)

**Template version: 3.0** — frozen 2026-07-20. Changes require a version bump and a full re-run (`V3_PRODUCT.md` P4).
**Changelog: 3.0.1** — machine-readability clarification, no rubric change: `owners_60plus_pct` carries a structured `succession_shortage_documented` field (see Step 1) so the build applies the OW +0.1 succession bonus mechanically.

You are scoring a single industry. Work context-free: do NOT look up any existing roll-up scoring of this industry (including anything on lisaivanchikova.github.io or similar maps). If you cannot access the web, stop and say so — do not proceed from memory alone, and never fabricate sources or URLs.

## Core rules

1. **No score may be set by judgment.** Every score is the mechanical output of its formula applied to recorded inputs. Your judgment goes into finding good research inputs and into declaring the judgment inputs (Step 1b) — never into overriding arithmetic. If a formula result contradicts your intuition, report the formula result and describe the disagreement in `reviewer_note`.
2. **PE/M&A deal activity (add-ons, consolidation waves) may only inform B and M.** It is never evidence for V (AI value) or A (AI adoption speed).
3. **EBITDA normalization.** All margins and multiples must be on an EBITDA basis after market-rate owner/partner compensation. If a source reports SDE or pre-owner-comp profit, convert and state the conversion.
4. **No rounding.** Carry full precision through every formula; report at least 3 significant digits. Display rounding happens downstream in the build — never in this record.
5. **Catch-all codes** ("Other …", "All Other …"): identify the top-3 revenue sub-segments, score the DOMINANT sub-segment, set `"heterogeneous": true`, and record the heterogeneity in `reviewer_note`.
6. **Dataset inputs are provided below and are used as given.** Do not re-research them. If your research contradicts a provided value, still use it for the arithmetic and describe the conflict in `reviewer_note`.

## Industry-specific guidance (verify everything; these are hints, not facts)

**Likely role structure (for the V breakdown):**
{{ROLE_HINTS}}

**Suggested sources (start here, prefer primary; mark secondary republication as such):**
{{SOURCE_HINTS}}

**Capture questions to answer with evidence (for C):**
{{CAPTURE_QUESTIONS}}

**Terminal-value question (for cross-check 2):**
{{TERMINAL_VALUE_QUESTION}}

**Known traps for this industry:**
{{SPECIAL_NOTES}}

## Dataset inputs (provided — computed identically for all codes from Census/BLS bulk extracts)

{{DATASET_INPUTS_JSON}}

Fields: `labor_share` (labor cost incl. imputed owner labor / revenue), `role_mix` (OEWS occupation shares of labor cost), `n_total` (firms), `n_band` (firms with $1–10M EBITDA, derivation chain included).

## Step 1 — Collect research inputs

Each with source name, URL, the specific figure quoted, access date, and quality (`HIGH|MED|LOW|ESTIMATE`). Prefer primary sources: trade-association benchmark surveys, industry M&A reports, broker data. Mark any input you could not source as `ESTIMATE` with your basis stated.

- `current_adoption_pct` — share of US firms in this industry already materially using AI in the automatable functions (be explicit what counts as material).
- `historical_analogs` — years this industry took to reach ~50% on comparable prior technology.
- `owners_60plus_pct` — share of owners aged 60+; note whether a succession shortage is documented. Record the succession finding machine-readably inside this input as `"succession_shortage_documented": {"value": true|false, "evidence": "<short quote or citation, or why not documented>"}` — the build reads this flag to apply the OW +0.1 succession bonus; prose alone is not read.
- `active_consolidators` — count of PE-backed platforms actively doing add-ons in this specific industry in the last 24 months.
- `buy_mult` — median EV/EBITDA actually paid for single-location/small firms (normalized per rule 3).
- `exit_mult` — EV/EBITDA for $10M+ EBITDA platforms in recent transactions or credible comps.
- Pricing-structure evidence — how this industry bills (hourly, retainer, fixed fee, cost-plus, % of value, per unit) and what share of revenue sits under each model. Feeds Step 1b and cross-check 4.

## Step 1b — Declare judgment inputs

These are **declared opinions** — the only place judgment enters the record. Each must be bounded, with its own rationale and plausible range.

- `within_role_automatable_fraction` per role (using the provided `role_mix`): share of that role's labor cost in tasks current AI can substantially do. Licensed/judgment/relationship/physical work = not automatable; a small automatable sliver inside professional roles (drafting, research, documentation) is allowed if justified. → `ai_replaceable_share` = Σ(role share × fraction).
- `pi_dist` ∈ [0,1] — client-relationship control: who owns the client — the firm, an upstream gatekeeper, a platform, a procurement department? **Pricing-model deflation must be reflected here with the mechanism stated** (cost-plus/audited/hourly billing hands AI savings to clients).
- `pi_moat` ∈ [0,1] — barrier strength: licensure, switching costs, proprietary data, physical presence, and the realistic threat that clients use generic AI to bypass the firm entirely.
- `t50` — years from today until 50% of firms materially adopt AI in the automatable functions; derive from `current_adoption_pct` + `historical_analogs` and show the derivation. **t50 must appear in `top_uncertain_inputs` with its range and score impact — always.**

## Step 2 — Compute scores (show full arithmetic; no rounding anywhere)

- `V_raw = labor_share × ai_replaceable_share`; `V = 10 × min(1, V_raw / 0.25)` — anchor: freeing ≥25% of revenue = 10.
- `C = 10 × pi_dist × pi_moat`
- `A = min(10, 10 / t50)`
- B subfactors (all continuous):
  `TD = clamp(log10(n_band) / 4, 0, 1)` — 10,000+ targets → 1.0
  `OW = clamp((owners_60plus_pct − 0.10) / 0.35, 0.1, 0.9)`; +0.1 if documented succession shortage, cap 1.0
  `CFD = min(0.9, log10(1 + active_consolidators) / 2)`
  `B = 10 × sqrt(TD × OW) / (1 + 0.3 × CFD)`
  (No price term in B — pricing signal lives only in M.)
- `M = clamp(4 × (exit_mult − buy_mult) / buy_mult, 0, 10)`
- `S = (V × C × A × B × M)^(1/5)`

## Step 3 — Mandatory cross-checks (answer each explicitly)

1. **Uplift consistency.** Convert V_raw into expected EBITDA uplift (pp). If uplift < 3pp while A ≥ 5, explain or revisit t50.
2. **Terminal value.** Answer the industry-specific terminal-value question. Distinguish: AI cutting the operator's costs vs AI replacing the operator's product. Classify: `DURABLE` (demand survives mature AI), `PRESSURED` (demand shrinks but persists), `MELTING` (the product itself is being replaced).
3. **No-proxy audit.** Confirm in writing that V and A were justified without reference to deal activity or consolidation trends.
4. **Pricing-model deflation.** State the billing mix and whether AI efficiency flows to clients as lower fees rather than to the operator as margin; confirm how this is reflected in `pi_dist`/`pi_moat`.

## Step 4 — Output

Return a single JSON object validating against `run_record.schema.json`:

```json
{
  "naics": "{{NAICS}}",
  "title": "{{TITLE}}",
  "run_meta": {
    "model_id": "{{MODEL_ID}}", "run_date": "{{RUN_DATE}}", "run_id": "{{RUN_ID}}",
    "template_version": "3.0", "prompt_version": "{{PROMPT_VERSION}}"
  },
  "dataset_inputs": { "...copy the provided dataset inputs verbatim..." },
  "inputs": {
    "ai_replaceable_share": {"value": 0.0, "breakdown_by_role": [
      {"role": "", "labor_share_of_total": 0.0, "within_role_automatable_fraction": 0.0,
       "contribution": 0.0, "rationale": "", "plausible_range": ""}
    ], "quality": ""},
    "pi_dist": {"value": 0.0, "rationale": "", "plausible_range": "", "sources": [], "quality": ""},
    "pi_moat": {"value": 0.0, "rationale": "", "plausible_range": "", "sources": [], "quality": ""},
    "t50_years": {"value": 0.0, "derivation": "", "plausible_range": "", "quality": ""},
    "current_adoption_pct": {"value": 0.0, "source": "", "url": "", "figure_quoted": "", "access_date": "", "quality": ""},
    "historical_analogs": {"value": "", "source": "", "url": "", "figure_quoted": "", "access_date": "", "quality": ""},
    "owners_60plus_pct": {"value": 0.0, "source": "", "url": "", "figure_quoted": "", "access_date": "", "quality": "", "succession_shortage_documented": {"value": false, "evidence": ""}},
    "active_consolidators": {"value": 0, "source": "", "url": "", "figure_quoted": "", "access_date": "", "quality": ""},
    "buy_mult": {"value": 0.0, "source": "", "url": "", "figure_quoted": "", "access_date": "", "quality": ""},
    "exit_mult": {"value": 0.0, "source": "", "url": "", "figure_quoted": "", "access_date": "", "quality": ""},
    "pricing_structure": {"value": "", "source": "", "url": "", "figure_quoted": "", "access_date": "", "quality": ""}
  },
  "scores": {
    "V": {"arithmetic": "", "score": 0.0},
    "C": {"arithmetic": "", "score": 0.0},
    "A": {"arithmetic": "", "score": 0.0},
    "B": {"arithmetic": "", "score": 0.0},
    "M": {"arithmetic": "", "score": 0.0}
  },
  "S": 0.0,
  "cross_checks": {
    "uplift_pp": 0.0,
    "uplift_vs_A_consistent": "",
    "terminal_value": {"class": "DURABLE|PRESSURED|MELTING", "justification": ""},
    "no_proxy_confirmed": "",
    "pricing_model_deflation": ""
  },
  "confidence_overall": "HIGH|MED|LOW",
  "heterogeneous": false,
  "top_uncertain_inputs": [{"input": "t50_years", "plausible_range": "", "score_impact": ""}],
  "reviewer_note": ""
}
```

Copy `run_meta` values as provided — do not invent them. Do not report a verdict or bucket — verdicts are computed by the build from `thresholds.json`.
