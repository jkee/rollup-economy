# 213113 — Support Activities for Coal Mining

*v5.1 Stage 1 research memo. Run `213113-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 5.14 · L 1.41 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Essential physical field work and compliance preserve operator demand within the surviving coal-production and reclamation base.
**Weakness:** A small target universe is exposed to structural coal decline and concentrated customers with strong repricing leverage.

## Business-model lens
- Included: Independent U.S. contractors providing repeat coal-mine development, drilling, blasting, excavation, dewatering, equipment operation, maintenance, ventilation, reclamation support, and other on-site technical or operating services to external mine owners.
- Excluded: Captive mine-owner crews; coal extraction for the firm's own account; equipment-only dealers; commodity traders; one-off consultants without recurring field delivery; shells; and businesses dominated by oil, gas, or noncoal mining support.
- Customer and revenue model: Recurring or repeat project, unit-rate, time-and-materials, and contracted field services sold to coal mine operators, limited to transferable external-customer firms plausibly generating $1-10 million of normalized EBITDA.
- Deviation from default lens: none

## Executive view
Coal-support contracting is labor-heavy and operator-required, but the addressable firm universe is small and underlying production demand is structurally declining. AI can improve coordination and compliance work without replacing most field delivery.

## How AI changes the work
Practical uses include bid and scope analysis, dispatch, shift reporting, safety-document drafting, maintenance prediction, parts planning, sensor anomaly triage, production reconciliation, and regulatory record search. Drilling, blasting, excavation, equipment operation, underground work, repair, and safety accountability remain physical.

## Value capture
Specialized equipment, basin familiarity, safety records, and urgent availability can protect margin. Large mine customers, competitive rebids, shrinking local demand, and transparent unit rates can pass savings through quickly.

## Firm availability
The frozen estimate indicates only a limited lower-middle-market population. Eligibility must exclude captive affiliates and diversified firms whose coal work is minor, while transferability depends on equipment condition, permits, bonding, labor, and customer concentration.

## Demand durability
Near-term EIA forecasts already show falling U.S. coal output, and long-run retirement pressure is severe. Metallurgical and export coal, outsourcing, mine maintenance, closure, and reclamation soften but do not erase the likely five-year contraction.

## Risks and uncertainty
Principal risks are mine and customer concentration, policy and commodity volatility, fatalities and safety liabilities, bonding, environmental obligations, equipment capex, labor availability, and liquidation rather than sale during contraction.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.3772 | — | OBSERVED | — |
| n | — | 17 | — | ESTIMATE | — |
| a | 0.1 | 0.18 | 0.27 | PROXY | S1, S2 |
| rho | 0.36 | 0.52 | 0.66 | ESTIMATE | S1, S2 |
| e | 0.5 | 0.66 | 0.8 | ESTIMATE | S4 |
| s5 | 0.1 | 0.22 | 0.35 | ESTIMATE | — |
| q | 0.36 | 0.52 | 0.68 | ESTIMATE | S3 |
| d5 | 0.62 | 0.76 | 0.91 | PROXY | S3, S4 |
| o | 0.86 | 0.94 | 0.99 | ESTIMATE | S1, S2 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.54 | 1.41 | 2.69 | ESTIMATE |
| F | 0.99 | 2.00 | 2.82 | ESTIMATE |
| C | 7.20 | 10.00 | 10.00 | ESTIMATE |
| D | 5.33 | 7.14 | 9.01 | ESTIMATE |

## Caveats
- a: Neither source directly reports the six-digit contractor task mix.
- a: Occupation shares are not wage-weighted AI exposure and include already automated work.
- rho: Remote or highly standardized surface operations may implement faster than underground and specialty crews.
- e: The frozen firm count is margin-bridged from an oilfield-services margin and is especially uncertain for coal contractors.
- s5: No observed six-digit control-transfer rate was found.
- q: Emergency and specialized work may retain more than competitively bid routine services.
- d5: Coal outcomes are highly policy-, weather-, export-, and natural-gas-price-sensitive.
- d5: The service basket spans production-linked and closure-linked activities with opposite trends.
- o: Demand lost from lower coal output is captured in d5 rather than repeated here.

## Sources
- **S1** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: Coal Mining](https://www.bls.gov/oes/2023/may/naics4_212100.htm) (accessed 2026-07-22): Coal mining employed 41,940 workers; construction and extraction occupations were 55.43%, including construction equipment operators at 12.05%, demonstrating the physical mine-site task mix.
- **S2** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: Support Activities for Mining](https://www.bls.gov/oes/2023/may/naics4_213100.htm) (accessed 2026-07-22): Broader mining support shows extraction workers at 34.37% and installation, maintenance, and repair workers at 5.77%, grounding the contractor task proxy.
- **S3** — [STEO Current/Previous Forecast Comparisons: U.S. Coal and Carbon Dioxide Emissions](https://www.eia.gov/outlooks/steo/pdf/compare.pdf) (accessed 2026-07-22): EIA's April 2026 outlook projects U.S. coal production of 533 million short tons in 2025, 517 in 2026, and 494 in 2027, declines of 3.1% and 4.3%.
- **S4** — [EIA Releases the Annual Energy Outlook 2026](https://www.eia.gov/pressroom/releases/press587.php) (accessed 2026-07-22): EIA states coal-plant retirements drive U.S. coal demand lower and projects coal generation could mostly disappear if 2024 power-sector emissions regulations are enforced.
