# 333517 — Machine Tool Manufacturing

*v5.1 Stage 1 research memo. Run `333517-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** CONDITIONAL · A 7.14 · L 2.05 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Engineering-rich workflows and installed-base aftermarket relationships create implementable and retainable opportunities.
**Weakness:** Highly cyclical new-equipment demand and safety-critical physical delivery limit consistency.

## Business-model lens
- Included: US lower-middle-market manufacturers repeatedly supplying metal-cutting and metal-forming machine tools, including lathes, mills, grinders, drilling, punching, shearing, bending, pressing, forging, and die-casting machines, plus associated parts, upgrades, training, and support to external industrial customers.
- Excluded: Captive internal machine-building units, shells, hand tools, welding equipment, rolling-mill machinery, cutting tools and accessories, and stand-alone distributors or service firms classified outside NAICS 333517.
- Customer and revenue model: Capital-equipment sales through direct and distributor channels, often supplemented by recurring replacement parts, control or software upgrades, automation integration, training, applications support, and service.
- Deviation from default lens: none

## Executive view
Machine-tool builders combine substantial engineering, controls, configuration, and aftermarket work with complex physical assembly and commissioning. AI can improve the digital layer, but machinery safety and field variability constrain implementation. Installed bases and switching costs support capture, while new-equipment demand remains sharply cyclical.

## How AI changes the work
AI can assist RFQs, configurations, mechanical and control documentation, schedules, code, inspection, remote diagnostics, service triage, and knowledge retrieval. Machining, welding, assembly, wiring, test execution, installation, and repair remain physical. Safety validation and long-lived legacy controls matter more than generic model capability.

## Value capture
Proprietary controls, installed-base parts, application knowledge, training, and response time create durable customer dependence. New-machine tenders and global competitors pressure price, while warranties and productivity commitments can absorb gains.

## Firm availability
Most estimated in-band builders should qualify as repeat external suppliers, but the count is margin-bridged. Custom engineering may be owner-dependent, and buyers inherit backlog volatility, warranty obligations, service commitments, and product-liability exposure.

## Demand durability
Recent machinery orders show recovery, and automation plus replacement needs support the five-year outlook. Yet machine tools are long-lived capital assets whose orders swing with industrial utilization, financing, tariffs, and confidence; aftermarket parts and upgrades are steadier than new machines.

## Risks and uncertainty
Risks include cyclicality, imported components and competitors, customer capex delays, working-capital swings, backlog cancellation, product safety, controls obsolescence, field-service capacity, and key-person engineering. Direct LMM task, contract, and transaction evidence is limited.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.3023 | — | OBSERVED | — |
| n | — | 272 | — | ESTIMATE | — |
| a | 0.22 | 0.32 | 0.43 | PROXY | S1, S2, S3 |
| rho | 0.34 | 0.53 | 0.7 | PROXY | S3, S4 |
| e | 0.66 | 0.82 | 0.93 | ESTIMATE | S1, S4 |
| s5 | 0.14 | 0.25 | 0.38 | PROXY | S6 |
| q | 0.39 | 0.58 | 0.74 | ESTIMATE | S4 |
| d5 | 0.95 | 1.1 | 1.25 | PROXY | S5, S7 |
| o | 0.91 | 0.97 | 0.995 | ESTIMATE | S1, S4 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.90 | 2.05 | 3.64 | PROXY |
| F | 5.25 | 6.50 | 7.36 | ESTIMATE |
| C | 7.80 | 10.00 | 10.00 | ESTIMATE |
| D | 8.64 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: The occupational mix is for NAICS 333500, not six-digit 333517.
- a: The estimate excludes already-automated CNC control and robotic functions from the unautomated opportunity.
- rho: Hurco is a public multinational rather than an LMM sample.
- rho: Digital features embedded in sold machines do not automatically substitute labor inside the manufacturer.
- e: The provided count is margin-bridged using a sector margin and may misclassify firms into the EBITDA band.
- e: Some custom builders may have repeat customers but highly project-dependent revenue.
- s5: No six-digit qualifying-transfer denominator was found.
- s5: Succession readiness does not measure completed control transactions.
- q: Hurco confirms aftermarket activities but does not measure benefit retention.
- q: Capture can be higher in proprietary installed-base parts and lower in competitively bid new machines.
- d5: USMTO values are nominal and one rebound year does not establish a five-year trend.
- d5: The turning-machine forecast covers one segment and is commercially produced.
- d5: New equipment and aftermarket demand behave differently.
- o: Operator requirement can migrate to foreign or larger builders without disappearing.
- o: Software-defined functionality may reduce some hardware options while increasing control and support work.

## Sources
- **S1** — [Census NAICS definition: 333517 Machine Tool Manufacturing](https://www.census.gov/naics/?details=333517&input=333517&year=2017) (accessed 2026-07-22): Defines metal-cutting and metal-forming machine-tool manufacturing and lists lathes, mills, grinders, drilling, bending, forming, punching, pressing, forging, and die-casting machines.
- **S2** — [BLS May 2023 occupation estimates for Metalworking Machinery Manufacturing](https://www.bls.gov/oes/2023/may/naics4_333500.htm) (accessed 2026-07-22): Reports 97,070 production workers representing 59.81% of broader NAICS 333500 employment and provides occupation-specific employment and wage context.
- **S3** — [The Rise of Artificial Intelligence in U.S. Manufacturing](https://www.nist.gov/mep/rise-artificial-intelligence-ai-us-manufacturing-text-only) (accessed 2026-07-22): Reports 46% manufacturing AI-tool use and more than 80% expecting increased use in two years, with manufacturing use cases and implementation barriers.
- **S4** — [Hurco Companies 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/315374/000110465926002512/hurc-20251031x10k.htm) (accessed 2026-07-22): Describes CNC machine tools, proprietary controls and software, automation integration, components, upgrades, accessories, replacement parts, customer service, training, and applications support.
- **S5** — [AMT: Manufacturing Technology Orders Set Record in December 2025](https://www.amtonline.org/article/manufacturing-technology-orders-set-record-in-december-2025) (accessed 2026-07-22): Reports $5.74 billion of 2025 machinery orders, 22.5% above 2024, following three years of decline after the 2021 rebound.
- **S6** — [Deloitte Private survey: generational disparities in family-business succession planning](https://www2.deloitte.com/us/en/pages/about-deloitte/articles/press-releases/deloitte-private-survey-generational-disparatires-emerge-insuccession-planning-and-priorities-shaping-family-businesses.html) (accessed 2026-07-22): Describes a January 2024 survey of 500 US family-enterprise respondents and reports that 24% of current-generation respondents strongly agreed their succession plan would withstand departure of an important family employee.
- **S7** — [United States Turning Machine and Equipment Market forecast](https://www.mordorintelligence.com/industry-reports/united-states-turning-machine-and-equipment-market) (accessed 2026-07-22): Forecasts the US turning-machine segment from $1.9 billion in 2026 to $2.4 billion in 2031 at 4.8% CAGR; used only as a commercial segment proxy.
