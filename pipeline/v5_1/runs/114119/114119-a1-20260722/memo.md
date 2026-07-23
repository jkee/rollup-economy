# 114119 — Other Marine Fishing

*v5.1 Stage 1 research memo. Run `114119-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** no base (evidence-first) · A — · L — · interval STRUCTURAL_OUT → CONDITIONAL · readiness STRESS_TEST_ONLY · action EVIDENCE_FIRST

**Driver:** Electronic reporting, monitoring, trip planning, navigation, compliance, and maintenance create bounded AI opportunity around labor-intensive vessel operations.
**Weakness:** The frozen LMM count is zero and residual-species demand is too heterogeneous and data-poor to establish transferable-firm opportunity.

## Business-model lens
- Included: US lower-middle-market commercial operators catching or taking marine animals other than finfish and shellfish from natural habitat for recurring external sale to dealers, processors, wholesalers, foodservice, research, bait, or specialty-product buyers, including vessels, crews, permits, catch handling, and reporting.
- Excluded: Finfish and shellfish fishing, aquaculture, recreational charters, seafood processing without harvest, dealers and wholesalers without vessels, captive internal harvest, subsistence activity, passive permit or vessel shells, and non-control financing vehicles.
- Customer and revenue model: Trip- and season-based repeat revenue from landed catch sold by weight, grade, species, auction, dealer settlement, processor contract, or specialty order, constrained by permits, seasons, areas, quotas, protected-species rules, weather, stock availability, and vessel economics.
- Deviation from default lens: none

## Executive view
Other marine fishing is a tiny residual category for wild marine animals other than finfish and shellfish. AI can improve navigation, trip planning, electronic reporting, monitoring, species review, maintenance, and sales, but deck work remains physical and the frozen estimate of zero LMM firms leaves transferable-firm opportunity undefined.

## How AI changes the work
AI can combine weather, location, historical catch, and vessel data, assist electronic logbooks and compliance, automate video review and species measurements, and support maintenance and buyer administration. Crews still operate vessels and gear, take and handle catch, make repairs, work safely in hazardous conditions, and exercise species and legal judgment.

## Value capture
Fuel, search, reporting, and downtime improvements can accrue to vessel owners, but quotas cap catch and dealers, processors, auctions, crew shares, and competitive adoption redistribute savings. Capture depends on species, permit and quota ownership, and buyer concentration.

## Firm availability
The frozen dataset estimates no firms in the LMM band, and public data do not reveal an alternative eligible pool. Any diligence must begin with species, vessel, permit, owner, revenue, and control mapping rather than assume a roll-up population exists.

## Demand durability
US commercial fisheries remain economically important and several relevant stock complexes received favorable determinations, but those broad facts are weak proxies for this residual basket. Quotas, protected status, climate, habitat, trade, and specialty-market volatility can change harvest sharply.

## Risks and uncertainty
Vessel safety, weather, stock abundance, quotas, protected species, permit transfer, fuel, gear loss, crew availability, insurance, buyer concentration, imports, climate-driven range shifts, and classification error are material. The central weakness is the absence of a demonstrated eligible firm population.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.4162 | — | OBSERVED | — |
| n | — | 0 | — | ESTIMATE | — |
| a | 0.13 | 0.22 | 0.33 | PROXY | S1, S2, S3 |
| rho | 0.38 | 0.53 | 0.67 | ESTIMATE | S3, S4 |
| e | — | — | — | MISSING | — |
| s5 | — | — | — | MISSING | — |
| q | 0.33 | 0.49 | 0.66 | ESTIMATE | S2, S5 |
| d5 | 0.78 | 0.96 | 1.15 | PROXY | S5, S6 |
| o | 0.97 | 0.992 | 1 | ESTIMATE | S1, S2, S3 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.82 | 1.94 | 3.68 | ESTIMATE |
| F | — | — | — | MISSING |
| C | 6.60 | 9.80 | 10.00 | ESTIMATE |
| D | 7.57 | 9.52 | 10.00 | ESTIMATE |

## Caveats
- a: The occupation source spans much larger finfish and shellfish industries and is not six-digit wage-weighted.
- a: The frozen compensation-to-receipts estimate is based on a small residual population and mismatched vintages, so it may be unstable.
- rho: NOAA electronic-monitoring programs largely cover finfish and shellfish fisheries, not the residual code.
- rho: AI may reduce regulator or service-provider review costs without reducing vessel labor.
- e: Zero is a margin-bridged dataset estimate rather than proof that no potentially eligible operator exists.
- e: Rare-species operations may be classified inconsistently under finfish, shellfish, hunting, aquaculture, or other marine fishing.
- s5: Permit and vessel transfers may exclude crews, customer relationships, and operating companies.
- s5: The frozen zero firm count prevents a meaningful conditional transfer rate without new population evidence.
- q: No public contract sample isolates pass-through for the residual species basket.
- q: Value capture differs by species, quota ownership, buyer concentration, crew-share method, and whether savings improve cost or allowed catch.
- d5: National commercial-fishing landings are dominated by finfish and shellfish outside the code.
- d5: The residual category can be moved by a few species or regulatory decisions and lacks a direct five-year forecast.
- o: Operator responsibility may consolidate across vessels or shift to vertically integrated buyers.
- o: Aquaculture and import substitution affect demand in d5 rather than operator requirement and are not double-counted here.

## Sources
- **S1** — [NAICS 114119 Other Marine Fishing](https://www.census.gov/naics/resources/archives/sect11.html) (accessed 2026-07-22): Defines the industry as commercial catching or taking of marine animals other than finfish and shellfish and distinguishes aquaculture and the adjacent fishing industries.
- **S2** — [Fishing and Hunting Workers](https://www.bls.gov/ooh/farming-fishing-and-forestry/fishers-and-related-fishing-workers.htm) (accessed 2026-07-22): Lists fish-finding, navigation, repairs, catch sorting and storage, legal-size checks, and manual gear handling; describes hazardous physical work and projects fishing and hunting employment down 5 percent from 2024 to 2034.
- **S3** — [Electronic Technologies](https://www.fisheries.noaa.gov/national/fisheries-observers/electronic-technologies) (accessed 2026-07-22): Describes electronic monitoring with cameras, GPS, transmitters and gear sensors; electronic reporting; vessel monitoring; and AI for automated video processing and prediction of fishing activity.
- **S4** — [Electronic Monitoring](https://www.fisheries.noaa.gov/national/fisheries-observers/electronic-monitoring) (accessed 2026-07-22): Reports fourteen implemented US electronic-monitoring programs and describes computer-vision development for species identification, weight and length estimation, gear enumeration, and detection of fishing activity, while noting video review, transmission, and storage costs.
- **S5** — [Status of Stocks 2024](https://www.fisheries.noaa.gov/national/sustainable-fisheries/status-stocks-2024) (accessed 2026-07-22): Reports 23 stocks subject to overfishing, 42 overfished stocks, and favorable 2024 determinations for Caribbean coral, sea-urchin, and sea-cucumber complexes, illustrating stock-specific regulation and uncertainty.
- **S6** — [Fisheries of the United States Reports](https://www.fisheries.noaa.gov/resource/document/fisheries-united-states-reports) (accessed 2026-07-22): Reports total US commercial landings of 8.4 billion pounds valued at $5.1 billion in 2023, used only as broad commercial-fishing context because residual-code landings are not isolated.
