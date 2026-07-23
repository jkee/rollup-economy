# 115210 — Support Activities for Animal Production

*v5.1 Stage 1 research memo. Run `115210-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** CONDITIONAL · A 5.51 · L 2.15 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** A recurring outsourced-service model, measurable office and management labor, and expanding livestock data create implementable AI opportunities alongside durable physical service demand.
**Weakness:** The small firm pool is margin-estimated, and business-model heterogeneity makes both transferability and technology-driven self-service highly candidate-specific.

## Business-model lens
- Included: US lower-middle-market firms repeatedly providing outsourced animal-production support to external livestock, equine, and companion-animal customers, including breeding and semen services, pedigree records, dairy herd improvement, horse boarding and training outside racing, farrier work, poultry catching and house cleaning, livestock spraying, sheep dipping and shearing, and related classified support work.
- Excluded: Captive internal farm units; animal raising for sale; veterinary practices; pet boarding and grooming classified outside this industry; racehorse training; shells; passive real-estate or financing vehicles; and firms outside the specified earnings band.
- Customer and revenue model: Customers are livestock farms, dairies, poultry operations, horse owners and farms, breeders, breed associations, and related animal operators. Revenue recurs through per-animal, per-visit, per-day, per-head, hourly, route, subscription, testing, record, or seasonal service charges; some contracts bundle labor, equipment, consumables, facilities, data, and scheduled availability.
- Deviation from default lens: none

## Executive view
Unlike the three production industries in this batch, support activities for animal production fits the recurring outsourced-service lens directly. The dataset indicates meaningful compensation intensity and a small estimated LMM pool. AI can address office, records, scheduling, customer, breeding-data, and monitoring work, but BLS confirms that most employment remains hands-on farming and animal-care labor. Recurring local demand and differentiated service quality support some value retention, while heterogeneous business models and the margin-bridged firm count require careful candidate-level diligence.

## How AI changes the work
Near-term applications include scheduling and dispatch, billing and collections, customer communications, pedigree and herd records, compliance documentation, workforce coordination, breeding and production analytics, computer-vision triage, and sensor-based animal monitoring. Precision dairy and livestock research shows growing use and economic value of sensors, analytics, automation, and computer vision. Hands-on animal care, farrier work, shearing, catching, cleaning, boarding, and many procedures remain physical, and welfare or liability concerns keep humans accountable.

## Value capture
Fixed, route, per-animal, boarding, and subscription-like pricing can preserve savings between repricing events, especially where local coverage, trust, animal-handling quality, specialist skill, and historical records differentiate the provider. Farm customers are cost-sensitive and can demand savings at renewal or bring work in-house; equipment and software vendors can also capture part of the benefit. Retention should be strongest in differentiated, recurring relationships and weakest in bid, hourly, or commodity labor services.

## Firm availability
The dataset supplies 34 estimated firms in the earnings band, but that count depends on applying a farming and agriculture margin proxy to heterogeneous service-company receipts. Most classified activities meet the external-service lens, yet owner-dependent farriers, trainers, and breeders; captive units; real-estate-heavy boarding; customer concentration; and weak second-layer management reduce transferability. Direct diligence of the candidate list is more important than the headline count.

## Demand durability
Breeding, animal handling and care, hoof work, shearing, boarding, cleaning, performance records, and herd improvement persist as long as animal production and ownership continue. Broader agricultural support output is projected to grow modestly. Farm consolidation can increase use of scaled providers, while sensors, robotic milking, and farm software can either generate new support needs or move monitoring, records, and routine work to self-service, producing a mixed but generally durable outlook.

## Risks and uncertainty
The main risks are the heterogeneous mix of data services, skilled practitioners, route labor, and facility-based equine operations; self-employed labor omitted from OEWS; the wage and receipts vintage mismatch in compensation; the margin proxy behind the 34-firm estimate; owner and reputation dependence; animal welfare and liability; farm customer concentration; livestock and equine cycles; rural labor shortages; and technology enabling customer self-service rather than provider efficiency.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.3256 | — | OBSERVED | — |
| n | — | 34 | — | ESTIMATE | — |
| a | 0.19 | 0.3 | 0.42 | PROXY | S2, S3, S4 |
| rho | 0.34 | 0.55 | 0.72 | ESTIMATE | S3, S4 |
| e | 0.38 | 0.62 | 0.8 | ESTIMATE | S1, S2 |
| s5 | 0.14 | 0.27 | 0.41 | PROXY | S6 |
| q | 0.2 | 0.37 | 0.56 | ESTIMATE | S1, S3 |
| d5 | 0.93 | 1.07 | 1.2 | PROXY | S3, S5 |
| o | 0.75 | 0.88 | 0.96 | ESTIMATE | S1, S3, S4 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.84 | 2.15 | 3.94 | ESTIMATE |
| F | 1.66 | 3.06 | 4.02 | ESTIMATE |
| C | 4.00 | 7.40 | 10.00 | ESTIMATE |
| D | 6.97 | 9.42 | 10.00 | ESTIMATE |

## Caveats
- a: Occupation groups do not reveal task shares, so the exposure mapping is judgment rather than a measured AI quantity.
- a: The code mixes data-heavy herd services, route services, and highly physical animal-care businesses.
- a: OEWS excludes self-employed workers, which can be material in farrier, breeder, trainer, and shearing services.
- a: The assigned compensation ratio has a 2024-wage versus 2022-receipts vintage mismatch and a cross-code harmonization adjustment.
- rho: The estimate applies only to the exposed opportunity in a.
- rho: USDA evidence primarily measures technology on animal-production farms rather than implementation inside outsourced support firms.
- rho: Animal welfare and liability considerations can require human verification even when analytics are reliable.
- e: The dataset supplies 34 firms using an estimated margin bridge rather than observed firm EBITDA.
- e: The farming and agriculture margin proxy used for n may misclassify service firms because margins differ across boarding, breeding, records, poultry, and mobile field services.
- e: OEWS includes employers of all sizes and does not identify which belong in the target earnings band.
- e: Some horse boarding economics may be driven more by real estate than a separable service operation.
- s5: The proxy is cross-industry and measures intentions rather than completed transfers.
- s5: Owner dependence varies sharply among records platforms, route services, skilled practitioners, and facility-based boarding.
- s5: An asset sale or family handoff without a transferable operating company is not a qualifying event.
- q: No source directly measures the retained share of implemented AI benefits.
- q: Value capture differs materially between subscription-like record services, fixed-price routes, skilled practitioner work, and cost-sensitive farm labor services.
- q: Precision technology can benefit the customer directly, increasing pressure to share savings.
- d5: The BLS output projection combines crop, animal, and forestry support activities.
- d5: No public series provides constant-quality demand for the heterogeneous services inside NAICS 115210.
- d5: Dairy technology evidence does not represent poultry, equine, sheep, or companion-animal service demand.
- o: The service mix ranges from almost entirely physical work to data and record services that are much more self-serviceable.
- o: Technology adoption by farms can complement outsourced providers or displace them, and available evidence does not resolve the net effect.
- o: A retained operator may use a materially different staffing model.

## Sources
- **S1** — [2017 NAICS Definition: 115210 Support Activities for Animal Production](https://www.census.gov/naics/2017NAICS/2017_Definition_File.pdf) (accessed 2026-07-22): Industry boundary and included service examples: animal breeding, pedigree records, horse boarding, dairy herd improvement, livestock spraying, and sheep dipping and shearing.
- **S2** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: Support Activities for Animal Production](https://www.bls.gov/oes/2023/may/naics4_115200.htm) (accessed 2026-07-22): Industry occupation and wage mix, including 40.09 percent farming occupations, 26.75 percent personal care and service, 7.99 percent office support, and 6.34 percent management; self-employed workers are excluded.
- **S3** — [Precision Dairy Farming, Robotic Milking, and Profitability in the United States](https://ers.usda.gov/publications/113704) (accessed 2026-07-22): Steadily increasing US adoption of precision dairy technologies involving sensors, data analytics, automation, breeding, and data systems, and evidence of higher farm net returns among adopters.
- **S4** — [Automated estimation of cattle body weight and hip height using 2D sensors](https://www.ars.usda.gov/research/publications/publication/?seqNo115=430474) (accessed 2026-07-22): Recent USDA research on computer-vision measurement of animal growth for feeding, breeding, management decisions, and farm-income prediction, illustrating relevant but not yet representative automation capability.
- **S5** — [Industry employment and output projections to 2034](https://www.bls.gov/emp/tables/industry-employment-and-output.htm) (accessed 2026-07-22): Real output for broader support activities for agriculture and forestry is projected to grow from 23.6 billion chained 2017 dollars in 2024 to 27.6 billion in 2034, a 1.6 percent annual rate.
- **S6** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Cross-industry US employer-business owner age and five-year sale-or-transfer intentions used only as a succession proxy.
