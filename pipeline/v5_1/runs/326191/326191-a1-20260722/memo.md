# 326191 — Plastics Plumbing Fixture Manufacturing

*v5.1 Stage 1 research memo. Run `326191-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 6.05 · L 0.80 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Recurring replacement and construction channels plus improvable planning, quality, and production-support workflows.
**Weakness:** Cyclical demand and powerful channels can absorb operational gains while plant integration remains capital-intensive.

## Business-model lens
- Included: US lower-middle-market manufacturers of plastic bathtubs, shower stalls, sinks, lavatories, toilet fixtures, and related plastic plumbing fixtures supplied repeatedly to distributors, builders, remodelers, hospitality customers, and OEM or private-label accounts.
- Excluded: Captive internal plants, installers without fixture manufacturing, metal or vitreous-china fixture makers, distributors without manufacturing, shells, and non-control financing vehicles.
- Customer and revenue model: Repeat B2B product sales through distributor, wholesale, builder, OEM, and project channels, generally priced per unit or product line with periodic negotiated adjustments and meaningful freight and resin exposure.
- Deviation from default lens: none

## Executive view
Plastics plumbing fixtures combine repeat physical-product channels with useful but bounded digital and automation opportunities. Improvement is most plausible in planning, quoting, quality, inspection, maintenance, and administration; tooling, molding, finishing, and customer acceptance remain operator-intensive.

## How AI changes the work
AI can improve demand planning, production scheduling, CAD and document retrieval, quoting, quality analytics, vision-assisted inspection, maintenance triage, and customer support. Manual trim, finishing, handling, setup, and process troubleshooting are harder to substitute within five years.

## Value capture
Mold ownership, finish quality, design differentiation, certification, and delivery reliability can protect some savings. Distributor, retailer, builder, and OEM bargaining power plus line reviews and competitive imports should erode a meaningful portion over time.

## Firm availability
The activity is coherent but the true pool of independent, recurring-supply, LMM firms is uncertain. Succession pressure is plausible; verified ownership, EBITDA, asset quality, channels, and closed transfer data are absent.

## Demand durability
Construction and remodeling cycles cause volatility, while replacement and efficiency-led product refresh support recurring demand. Physical fixtures still require an accountable manufacturer even as software and factory automation advance.

## Risks and uncertainty
Key risks include housing cyclicality, import competition, resin and freight volatility, large-customer concentration, obsolete tooling, warranty and product-liability exposure, and high manual finishing content. The evidence is weakest on six-digit occupation mix, firm eligibility, transfer incidence, and contract-level capture.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1585 | — | OBSERVED | — |
| n | — | 96 | — | ESTIMATE | — |
| a | 0.15 | 0.23 | 0.32 | PROXY | S1 |
| rho | 0.4 | 0.55 | 0.69 | PROXY | S2 |
| e | 0.34 | 0.5 | 0.66 | ESTIMATE | S3 |
| s5 | 0.12 | 0.2 | 0.3 | PROXY | S5 |
| q | 0.32 | 0.48 | 0.64 | ESTIMATE | — |
| d5 | 0.93 | 1.02 | 1.12 | ESTIMATE | S4 |
| o | 0.94 | 0.98 | 0.995 | ESTIMATE | S3, S4 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.38 | 0.80 | 1.40 | PROXY |
| F | 2.56 | 3.80 | 4.82 | ESTIMATE |
| C | 6.40 | 9.60 | 10.00 | ESTIMATE |
| D | 8.74 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: Four-digit occupational data are not specific to 326191.
- a: Exposure is inferred from occupational structure rather than directly observed tasks.
- rho: The machine-worker source includes processes unlike thermoforming, injection molding, and composite fixture finishing.
- rho: Product variety and manual finishing materially affect implementability.
- e: NAICS scope confirms activity but not ownership or transferability.
- e: The frozen firm count is a margin-based estimate, not observed eligible firms.
- s5: Intentions are not transactions and the source is cross-industry.
- s5: No six-digit succession or completed-control dataset was found.
- q: No public contract set quantifies benefit pass-through.
- q: Private-label commodity fixtures likely retain less than differentiated branded or engineered products.
- d5: WaterSense documents product efficiency and replacement logic, not a five-year industry volume forecast.
- d5: Demand varies by new-build, remodel, institutional, and manufactured-housing exposure.
- o: Operator requirement is inferred from the physical and performance-tested product.
- o: Material substitution is mainly captured in d5 to avoid double counting.

## Sources
- **S1** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 326100 Plastics Product Manufacturing](https://www.bls.gov/oes/2023/may/naics4_326100.htm) (accessed 2026-07-22): States that the estimates cover NAICS 326100 employers and reports 357,010 production workers, 58.94 percent of industry employment, grounding the occupation-mix proxy for AI exposure.
- **S2** — [Metal and Plastic Machine Workers, Occupational Outlook Handbook](https://www.bls.gov/ooh/production/metal-and-plastic-machine-workers.htm) (accessed 2026-07-22): Reports a 7 percent projected employment decline for 2024-2034 and describes ongoing expansion of CNC, robots, and other labor-saving machinery alongside continuing operator skill requirements.
- **S3** — [Plastics Plumbing Fixture Manufacturing: 2002 Economic Census](https://www2.census.gov/library/publications/economic-census/2002/manufacturing-reports/industry-series/ec0231i326191.pdf) (accessed 2026-07-22): Identifies NAICS 326191 as Plastics Plumbing Fixture Manufacturing and provides the industry-series scope used to anchor the physical manufacturing lens.
- **S4** — [About WaterSense](https://www.epa.gov/watersense/about-watersense) (accessed 2026-07-22): Explains that WaterSense-labeled plumbing products meet EPA efficiency and performance criteria and provides examples of fixture replacement savings, supporting efficiency-led product replacement and testing requirements.
- **S5** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Reports a fall 2024 employer-business-owner survey about five-year plans and that 74 percent of those planning around retirement intend to sell or transfer ownership, used only as a cross-industry transfer proxy.
