# v4.3 minimal canary and Phase 4 rerun

> **Historical:** preserved v4.3 adapter result. Fresh v5 research and reviews supersede it.

**Result:** accept the implementation as a Stage 1 research-priority screen;
do not treat its base tiers as underwriting conclusions. The five canaries are
mechanically complete and economically intelligible, but all five tier
intervals cross and all five actions are `VALIDATE_ASSUMPTIONS`.

The adapter contract in
`pipeline/build/thresholds_v4_3_minimal.json` was written before the canary was
run and was not changed after outcomes were viewed.

## Canary result

Factor evidence is shown as `M` (mixed empirical and bounded judgment) or `E`
(elicited/bounded judgment). A is the v4 breadth score; the bracket is the
finite scenario range.

| NAICS | H | F | C | D | Evidence H/F/C/D | A [low, high] | Base tier; interval | v3 score / verdict | Driver; weakness |
|---|---:|---:|---:|---:|---|---:|---|---|---|
| 238220 | 1.69 | 7.75 | 7.19 | 9.00 | M/M/E/E | 6.41 [4.10, 8.11] | `LOW_PRIORITY`; `STRUCTURAL_OUT`–`CONDITIONAL` | 4.08 / `conditional` | durable demand; limited implementable labor share |
| 541214 | 10.00 | 5.40 | 3.15 | 5.85 | M/M/E/E | 6.10 [3.89, 7.58] | `CONDITIONAL`; `LOW_PRIORITY`–`PRIORITY` | 3.36 / `kill` | labor opportunity; commercial retention |
| 541511 | 7.42 | 9.81 | 2.10 | 5.85 | M/M/E/E | 6.30 [3.49, 8.50] | `CONDITIONAL`; `STRUCTURAL_OUT`–`PRIORITY` | 3.38 / `pass` | transferable-firm depth; commercial retention |
| 541512 | 10.00 | 9.18 | 6.50 | 9.00 | M/M/E/E | 8.67 [5.67, 10.00] | `HIGHEST_PRIORITY`; `CONDITIONAL`–`HIGHEST_PRIORITY` | 4.67 / `conditional` | broad strength; commercial retention |
| 541930 | 6.82 | 1.96 | 1.75 | 5.85 | M/M/E/E | 4.10 [1.79, 6.54] | `LOW_PRIORITY`; `STRUCTURAL_OUT`–`CONDITIONAL` | 0.00 / `kill` | labor opportunity; retention and firm depth |

The v3-v4 changes follow the formulas rather than a desired ranking. v4 drops
entry/exit multiple arbitrage, separates implementable labor opportunity from
commercial retention and surviving operator demand, and uses the A/L pair.
That lifts systems design on broad operating economics, distinguishes payroll
from the two computer-service codes, and keeps translation low without using a
missing multiple as economic zero.

## Acceptance checks

- **Unknown is distinct from adverse evidence:** the focused sentinel proves a
  missing factor has no base and maps to `EVIDENCE_FIRST`; measured zero maps
  to `STRUCTURAL_OUT`. In the full universe, the legacy 541120 firm-count gap
  is therefore `STRESS_TEST_ONLY`, not a zero-scored opportunity.
- **Tiers are reachable:** synthetic sentinels reach all five tiers. The canary
  itself reaches `HIGHEST_PRIORITY`, `CONDITIONAL`, and `LOW_PRIORITY` at base.
- **Dispersion is meaningful:** canary bases span H 1.69–10.00, F 1.96–9.81,
  C 1.75–7.19, and D 5.85–9.00. There is neither blanket compression nor
  blanket inflation.
- **Economic differentiation is plausible:** payroll is implementation-heavy
  but capture-constrained; custom programming has deep supply but weak
  retention; systems design combines high labor opportunity, transfer depth,
  retention, and durable operator demand.
- **Elicitation remains decisive:** yes. C and D are bounded elicited adapters,
  and H/F mix empirical anchors with judgment. Readiness therefore remains
  `MODEL_CONDITIONED` and the action remains `VALIDATE_ASSUMPTIONS` even for a
  top base tier.
- **Ranks are not stable under bounds:** none of the five canaries has a robust
  tier. This is disclosed, not repaired by narrowing ranges after seeing the
  outcome.

## Full Phase 4 rerun

The accepted implementation was applied once to the existing 63-code Phase 4
membership. Results are separate from v3:

- 63/63 records generated; 62 have complete bases and one is evidence-first;
- base tiers: 2 `HIGHEST_PRIORITY`, 4 `PRIORITY`, 29 `CONDITIONAL`, 19
  `LOW_PRIORITY`, 8 `STRUCTURAL_OUT`, and 1 unknown;
- readiness/actions: 62 `MODEL_CONDITIONED` / `VALIDATE_ASSUMPTIONS`, 1
  `STRESS_TEST_ONLY` / `EVIDENCE_FIRST`;
- one record has a robust tier; the remaining intervals cross and remain
  visible; and
- the v3 dataset remains unchanged and is embedded only as a comparison.

Canonical outputs are `6digit/six_data_v4.json`,
`pipeline/v4_3/full_report.json`, and the per-code records under
`pipeline/v4_3/runs/`. The dashboard now reads the v4 dataset by default and
shows the v3 score beside every record.
