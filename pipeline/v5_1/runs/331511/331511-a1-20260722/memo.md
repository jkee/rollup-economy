# 331511 — Iron Foundries

*v5.1 Stage 1 research memo. Run `331511-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 6.04 · L 0.63 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Qualified recurring casting programs create durable switching costs and information workflows that AI can improve.
**Weakness:** Two-thirds of employment is production work, while aggregate foundry output is projected to decline and weak plants may close rather than transfer.

## Business-model lens
- Included: Independent US iron foundries that repeatedly engineer and pour ductile, gray, malleable, compacted-graphite, or semisteel castings to external customer specifications and have transferable operations in the target band.
- Excluded: Captive OEM foundries, iron and steel mills, fabricators that do not pour castings, consumer-product businesses without repeat external casting relationships, project shells, and non-control interests.
- Customer and revenue model: Revenue is earned per casting, pound, tooling program, lot, or machining/finishing step under recurring OEM, distributor, infrastructure, and industrial purchase orders, often with metal and energy surcharges.
- Deviation from default lens: The code includes both repeat contract foundries and captive or product-led operations. The lens retains independent external casting programs because the other models are not coherent recurring outsourced services.

## Executive view
Independent iron foundries often have exactly the repeat, qualification-heavy outsourced manufacturing relationships the lens seeks, but AI applies to engineering and support workflows rather than the labor-intensive foundry floor. Demand is durable yet modestly declining in aggregate, with large variation by end market and awarded program.

## How AI changes the work
AI can assist RFQs, cost estimates, routings, work instructions, production schedules, defect analysis, maintenance knowledge, quality records, certificates, purchasing, and customer service. Melting, molding, pouring, shakeout, grinding, inspection, and material movement remain physical.

## Value capture
Tooling, qualification, metallurgy, and switching costs support retention, particularly in complex or low-volume work. OEM annual productivity demands and program rebids share benefits in high-volume segments.

## Firm availability
Many jobbing and program foundries fit the external repeat-production lens, but captive plants, customer concentration, capital needs, permits, liabilities, and owner dependence narrow the transferable pool. Closure can be more rational than sale for weak assets.

## Demand durability
Infrastructure, pipe, machinery, motors, vehicles, agriculture, and industrial equipment preserve a broad physical need. Aggregate foundry output is projected to decline, reflecting lightweighting, imports, alternate processes, and productivity.

## Risks and uncertainty
Major risks are customer-program concentration, cyclical end markets, energy and scrap costs, air emissions, silica and worker safety, capital backlog, obsolete tooling, imports, closure economics, and the lack of six-digit occupation data.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.2497 | — | OBSERVED | — |
| n | — | 123 | — | ESTIMATE | — |
| a | 0.07 | 0.14 | 0.22 | PROXY | S1, S2 |
| rho | 0.25 | 0.45 | 0.64 | ESTIMATE | S2, S3 |
| e | 0.25 | 0.46 | 0.66 | ESTIMATE | S2 |
| s5 | 0.11 | 0.21 | 0.33 | PROXY | S4 |
| q | 0.28 | 0.5 | 0.71 | ESTIMATE | S2, S5 |
| d5 | 0.79 | 0.95 | 1.12 | PROXY | S5, S6 |
| o | 0.95 | 0.99 | 1 | ESTIMATE | S2, S3 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.17 | 0.63 | 1.41 | ESTIMATE |
| F | 2.38 | 4.11 | 5.35 | ESTIMATE |
| C | 5.60 | 10.00 | 10.00 | ESTIMATE |
| D | 7.50 | 9.40 | 10.00 | ESTIMATE |

## Caveats
- a: Four-digit occupation data include steel, investment, and nonferrous foundries.
- a: Existing casting simulation and machine automation are not separated from not-yet-automated tasks.
- rho: No US iron-foundry five-year AI implementation study was located.
- rho: Jobbing foundries may have more document complexity but less clean data than high-volume automotive foundries.
- e: Public industry counts do not separate captive and independent foundries.
- e: The machinery margin proxy may not fit energy-intensive casting businesses.
- s5: Cross-industry owner intentions are not completed transaction probabilities.
- s5: Strategic plant purchases and family transfers may not leave a standalone eligible firm.
- q: No public source directly measures AI-benefit pass-through.
- q: Scrap, alloy, energy, freight, and yield changes can mask retention.
- d5: The BLS series combines all foundry metals and methods.
- d5: A foundry's demand depends heavily on a small number of awarded programs and tooling life cycles.
- o: This measures operator necessity rather than labor intensity.
- o: Part redesign and import substitution affect d5 more than operator requirement.

## Sources
- **S1** — [Foundries - May 2023 OEWS Industry-Specific Occupational Employment and Wage Estimates](https://www.bls.gov/oes/2023/may/naics4_331500.htm) (accessed 2026-07-22): Foundry occupation mix: 66.92% production, 7.33% installation/maintenance/repair, and 5.25% office support.
- **S2** — [2022 NAICS Definition: Iron Foundries](https://www.census.gov/naics/?details=331511&input=331511&year=2022) (accessed 2026-07-22): Official six-digit scope and examples: purchased iron is poured into molds for ductile, gray, malleable, pipe, fittings, wheels, cookware, and other castings.
- **S3** — [Emission Estimation Protocol for Iron and Steel Foundries](https://nepis.epa.gov/Exe/ZyPURL.cgi?Dockey=P101H8DZ.txt) (accessed 2026-07-22): Foundry process sequence and accountability: scrap/material handling, melting, mold/core making, pouring, cooling, shakeout, sand recovery, cutting, grinding, finishing, and emissions reporting.
- **S4** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Cross-industry succession proxy: 52.3% of employer businesses have owners age 55 or older and 22% planned a five-year sale or transfer.
- **S5** — [Employment and output by industry](https://www.bls.gov/emp/tables/industry-employment-and-output.htm) (accessed 2026-07-22): BLS projects foundry real output from 26.9 to 24.8 billion chained 2017 dollars and employment down 14.7% over 2024-34.
- **S6** — [Locating and Estimating Air Emissions from Sources of Lead and Lead Compounds](https://www.epa.gov/sites/default/files/2020-11/documents/lead.pdf) (accessed 2026-07-22): Iron-casting end uses include motor vehicles, farm and construction machinery, petroleum equipment, electric motors, and iron and steel industry equipment.
