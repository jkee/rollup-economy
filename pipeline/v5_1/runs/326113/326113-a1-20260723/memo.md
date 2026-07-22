# 326113 — Unlaminated Plastics Film and Sheet (except Packaging) Manufacturing

*v5.1 Stage 1 research memo. Run `326113-a1-20260723`, model `claude-sonnet-5`, 2026-07-23, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 6.12 · L 0.75 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Specification-critical physical films serving containment, industrial, construction, and energy uses can support recurring demand and operational data advantages.
**Weakness:** Product-mix opacity and capital-intensive commodity economics make transferable-firm quality and benefit retention highly firm-specific.

## Business-model lens
- Included: US lower-middle-market manufacturers that repeatedly convert plastic resins into nonpackaging unlaminated film or sheet for external industrial, construction, environmental-containment, agricultural, energy, medical, graphics, or downstream fabrication customers.
- Excluded: Captive internal production, pure resin or film distribution, packaging film and sheet, laminated nonpackaging sheet, profile shapes, finished bags and pouches, shells, and non-control financing vehicles.
- Customer and revenue model: Recurring rolls or sheets sold by weight, area, gauge, formulation, performance specification, qualification, or supply agreement; resin-index and commodity pricing coexist with differentiated technical products such as liners, specialty films, and energy-related components.
- Deviation from default lens: none

## Executive view
Nonpackaging plastic film and sheet is a capital-intensive, heterogeneous physical-products industry. AI can improve planning, quality and process analytics, maintenance, specification work, and administration, but does not replace extrusion, calendering, handling, or accountable release. Diverse construction, containment, industrial, and energy uses support demand while making any aggregate forecast uncertain.

## How AI changes the work
The feasible opportunity lies around the line: recipe and specification retrieval, scheduling, anomaly detection, vision inspection, predictive-maintenance support, laboratory-data analysis, quoting, procurement, and customer service. Physical changeovers, material handling, machine tending, maintenance, sampling, and final quality accountability persist.

## Value capture
Engineered performance, certifications, installation risk, and customer qualification can protect savings in specialty films. Commodity sheet is more exposed to resin indices, rebids, imported alternatives, and customers that understand conversion economics.

## Firm availability
Transferable specialty independents likely exist, but the nominal pool requires filtering for captive integration, large-company ownership, utilization, equipment age, environmental obligations, certifications, customer concentration, and maintenance capital. Broad owner-age data provide only weak succession evidence.

## Demand durability
Construction and industrial cycles matter, while containment requirements and solar or other advanced applications provide durable or growing niches. Lightweighting, alternative materials, imports, and policy pressure on plastics can reduce tonnage, though packaging-specific restrictions are less directly relevant here.

## Risks and uncertainty
Major risks include resin and energy volatility, capital intensity, line downtime, thickness and property defects, environmental permits, imported competition, end-market concentration, certifications, and rapidly changing materials. Public sources do not reveal the code's current product weights.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1601 | — | OBSERVED | — |
| n | — | 72 | — | ESTIMATE | — |
| a | 0.12 | 0.22 | 0.34 | PROXY | S2, S3 |
| rho | 0.33 | 0.53 | 0.7 | ESTIMATE | S2, S3 |
| e | 0.36 | 0.56 | 0.73 | ESTIMATE | S1, S5, S6 |
| s5 | 0.12 | 0.23 | 0.35 | PROXY | S4 |
| q | 0.3 | 0.53 | 0.73 | ESTIMATE | S1, S6, S7 |
| d5 | 0.82 | 1.04 | 1.23 | PROXY | S5, S6, S7, S8 |
| o | 0.89 | 0.96 | 0.995 | ESTIMATE | S1, S6, S7 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.25 | 0.75 | 1.52 | ESTIMATE |
| F | 2.27 | 3.75 | 4.77 | ESTIMATE |
| C | 6.00 | 10.00 | 10.00 | ESTIMATE |
| D | 7.30 | 9.98 | 10.00 | ESTIMATE |

## Caveats
- a: The occupation proxy is four-digit and includes many plastics processes outside film and sheet.
- a: Employment counts are not direct task or wage shares.
- rho: The sources describe occupations and automation context rather than observed AI implementation.
- rho: Some gains would improve yield or throughput instead of reducing labor.
- e: The injected firm count is model-derived.
- e: The code combines films and sheets serving unrelated end markets, so plant-level eligibility cannot be inferred from the label.
- s5: ABS contains industries and sizes outside the lens.
- s5: A line or plant asset sale may not transfer a complete recurring operating firm.
- q: No source directly measures five-year retention of AI-derived benefit.
- q: Bargaining power differs substantially across commodity construction sheet and highly specified environmental or energy film.
- d5: Construction spending is nominal and only one end market.
- d5: EPA liner sources demonstrate required applications but not current shipment growth.
- d5: DOE solar evidence does not establish the domestic share supplied under this NAICS code.
- o: This is conditional on year-five physical demand after substitution and material reduction.
- o: An external lens operator can be displaced even when the end use still requires film.

## Sources
- **S1** — [2022 NAICS Definition: Unlaminated Plastics Film and Sheet (except Packaging) Manufacturing](https://www.census.gov/naics/?chart=2022&details=324&input=31) (accessed 2026-07-23): Defines 326113 as converting plastics resins into nonpackaging film and unlaminated sheet and distinguishes adjacent packaging and laminated activities.
- **S2** — [May 2023 OEWS: Plastics Product Manufacturing](https://www.bls.gov/oes/2023/may/naics4_326100.htm) (accessed 2026-07-23): Provides broader plastics-product occupation counts for extrusion, forming, inspection, engineering, maintenance-adjacent, and other roles used as the task-mix proxy.
- **S3** — [Metal and Plastic Machine Workers](https://www.bls.gov/ooh/production/metal-and-plastic-machine-workers.htm) (accessed 2026-07-23): Describes machine setup, test runs, adjustments, inspection, monitoring, minor repairs, and the effect of automation on multi-machine operation.
- **S4** — [ABS Characteristics of Business Owners: 2022 Tables](https://www.census.gov/data/tables/2022/econ/abs/2022-abs-characteristics-of-owners.html) (accessed 2026-07-23): Provides age-of-owner tables used solely as a broad succession proxy.
- **S5** — [Monthly Construction Spending: May 2026](https://www.census.gov/construction/c30/current/index.html) (accessed 2026-07-23): Reports May 2026 US construction spending at a $2,210.2 billion annual rate, 1.5% below a year earlier, as a downstream-demand proxy.
- **S6** — [Materials Management: State of the Practice](https://nepis.epa.gov/Exe/ZyPURL.cgi?Dockey=P10135TF.TXT) (accessed 2026-07-23): Describes plastic geomembrane use in landfill liner systems and regulatory containment requirements, supporting a durable end-use example.
- **S7** — [Solar Manufacturing](https://www.energy.gov/cmei/systems/solar-manufacturing) (accessed 2026-07-23): Identifies encapsulant and backsheets among physical photovoltaic module components and describes current domestic manufacturing context.
- **S8** — [Solar Photovoltaics Supply Chain Deep Dive Assessment](https://www.energy.gov/sites/default/files/2022-02/Solar%20Energy%20Supply%20Chain%20Report%20-%20Final.pdf) (accessed 2026-07-23): Explains that front and back encapsulant films protect photovoltaic cells and identifies EVA and POE as predominant resins.
