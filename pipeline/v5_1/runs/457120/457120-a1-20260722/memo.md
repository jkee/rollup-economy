# 457120 — Other Gasoline Stations

*v5.1 Stage 1 research memo. Run `457120-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** no base (evidence-first) · A — · L — · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness STRESS_TEST_ONLY · action EVIDENCE_FIRST

**Driver:** Regulated physical infrastructure makes surviving service quantity strongly operator-required despite opportunities to automate back-office and payment workflows.
**Weakness:** Only a small, unmeasured subset of a primarily commodity-retail industry appears to satisfy the recurring outsourced-service lens.

## Business-model lens
- Included: Lower-middle-market operators of gasoline stations without convenience stores, truck stops, and marine service stations whose operating model includes a recurring external-customer service component such as repair and maintenance or managed fleet fueling accounts.
- Excluded: Fuel-only and incidental merchandise retail, stations with convenience stores, captive corporate fueling, shells, internal fleet depots, non-control financing vehicles, and operations without a repeat outsourced-service relationship.
- Customer and revenue model: Retail fuel and ancillary products are sold per transaction at posted prices; the eligible subset also earns repeat repair labor and parts revenue or contract/account-based fleet-fueling revenue from external customers.
- Deviation from default lens: Narrowed to operators with recurring repair/maintenance or managed fleet-account services because NAICS 457120 combines primarily transactional fuel retail with stations that also provide repair or other services, and pure commodity retail does not satisfy the fixed outsourced-service lens.

## Executive view
Other gasoline stations are primarily physical commodity retailers, so only a small repair- or fleet-service subset fits the recurring outsourced-service lens. AI can streamline administration and exceptions, but the work is already substantially self-served and the remaining core involves physical assets, safety, and environmental compliance.

## How AI changes the work
The clearest uses are customer and fleet-account support, reconciliation, invoice and document handling, scheduling, demand and pricing analysis, fraud review, and maintenance triage. Cashier roles face structural automation pressure, but pay-at-pump has already captured much of the obvious checkout opportunity, while repair, inspection, stocking, spill response, and equipment work remain physical.

## Value capture
Fuel prices are visible and locally competitive, with thin gross economics after card and operating costs. Some savings can fund margin or capacity, particularly in differentiated repair and fleet relationships, but competitive repricing, negotiated discounts, platform fees, and supply arrangements should pass through much of the benefit over five years.

## Firm availability
Succession pressure is plausible among independent operators, yet broad owner-transition intent is a weak proxy for completed sales. Internal family transfers, closures, real-estate sales, environmental liabilities, franchise or supply restrictions, and the very small service-lens-eligible subset all reduce qualifying control-transfer availability.

## Demand durability
Fuel volume should erode gradually rather than collapse over five years as vehicle efficiency and electrification offset travel. Truck, marine, fleet-account, and repair demand can be more durable, while the requirement for trained UST operators and ongoing inspections keeps an accountable operator attached to most surviving quantity.

## Risks and uncertainty
The largest evidence gap is the absence of firm-level data identifying which 457120 operators actually have material recurring service revenue and LMM economics. Exact occupation mix, automation baselines, transaction incidence, environmental liabilities, fuel-format migration, and retention of labor savings are also unobserved for the narrowed population.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1014 | — | ESTIMATE | — |
| n | — | — | — | MISSING | — |
| a | 0.1 | 0.2 | 0.32 | PROXY | S2, S3, S4 |
| rho | 0.3 | 0.5 | 0.7 | ESTIMATE | S4, S9, S10 |
| e | 0.005 | 0.03 | 0.08 | ESTIMATE | S1 |
| s5 | 0.1 | 0.18 | 0.28 | PROXY | S6 |
| q | 0.15 | 0.3 | 0.5 | ESTIMATE | S4, S5 |
| d5 | 0.88 | 0.94 | 0.99 | PROXY | S7, S8 |
| o | 0.85 | 0.93 | 0.98 | ESTIMATE | S4, S9, S10 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.12 | 0.41 | 0.91 | ESTIMATE |
| F | — | — | — | MISSING |
| C | 3.00 | 6.00 | 10.00 | ESTIMATE |
| D | 7.48 | 8.74 | 9.70 | ESTIMATE |

## Caveats
- a: BLS reports NAICS 447 gasoline stations, which includes convenience-store stations and therefore is not the exact 457120 population.
- a: WEF is a global, cross-industry employer survey and measures expected role change rather than wage-weighted task substitution.
- a: The provided labor ratio is measured at ancestor 44-45 and may not reflect the narrowed service subset.
- rho: No source directly measures five-year AI implementation for 457120.
- rho: Automated monitoring can surface work rather than eliminate the trained operator and inspection duties required at UST facilities.
- rho: Implementation capacity likely varies sharply between multi-site truck-stop operators and small independent service stations.
- e: There is no published share of 457120 firms with qualifying recurring service revenue.
- e: Establishment classification is based on primary activity, while eligibility is a firm-level and revenue-model concept.
- e: The supplied LMM firm-count input is missing, so this share cannot be translated into a defensible eligible-firm count.
- s5: EPI respondents are self-selected and cross-industry rather than NAICS-specific.
- s5: Transition desire is not a completed control transfer, and the report indicates substantial preference for internal exits among family firms.
- s5: The estimate excludes closures, deaths without transferable operations, and real-estate-only transactions.
- q: NACS statistics primarily represent convenience fuel retail and are not specific to 457120 or the narrowed service subset.
- q: FTC evidence establishes the importance of local competition and vertical contracts but does not measure retention of AI savings.
- q: Retention differs between posted-price fuel, negotiated fleet accounts, and repair labor.
- d5: The five-year ratio extrapolates beyond EIA's two-year detailed short-term consumption discussion.
- d5: National fuel volume is not the same as demand captured by stations without convenience stores.
- d5: Constant-quality aggregation across fuel, repair, and managed accounts requires judgment.
- o: An accountable operator need not be continuously on site and may oversee multiple locations remotely.
- o: State rules can exceed federal UST requirements.
- o: The estimate concerns continued need for an operating entity, not the number of employees per site.

## Sources
- **S1** — [2022 NAICS Definition: 457120 Other Gasoline Stations](https://www.census.gov/naics/?chart=2022&details=457120&input=457120) (accessed 2026-07-22): Defines the industry as gasoline stations without convenience stores or truck stops primarily retailing automotive fuels, sometimes combined with repair, parts, accessories, or food service.
- **S2** — [Gasoline Stations: NAICS 447](https://www.bls.gov/iag/tgs/iag447.htm) (accessed 2026-07-22): Reports roughly 1.06 million industry employees in 2026 and 2025 occupational employment including 589,470 cashiers, 101,810 retail supervisors, 42,690 combined food workers, 19,090 food preparation workers, 18,880 service-station attendants, and 7,050 automotive technicians.
- **S3** — [Future of Jobs Report 2025: Jobs Outlook](https://www.weforum.org/publications/the-future-of-jobs-report-2025/in-full/2-jobs-outlook/) (accessed 2026-07-22): Finds cashiers and ticket clerks among the fastest-declining roles and identifies digital access, AI and information processing, and autonomous systems as primary drivers; employers expect human-only task share to fall by 2030.
- **S4** — [NACS Key Facts About Fueling](https://www.convenience.org/topics/fuels-and-energy/the-us-petroleum-industry-statistics-definitions) (accessed 2026-07-22): Reports that 81% of pump transactions are by card, 2025 gasoline gross margin was 39.7 cents per gallon or 12.7% of average price, and card fees and other expenses consume material fuel economics.
- **S5** — [The Impact of Vertical Contracting on Firm Behavior: Evidence from Gasoline Stations](https://www.ftc.gov/reports/impact-vertical-contracting-firm-behavior-evidence-gasoline-stations) (accessed 2026-07-22): Shows that gasoline-station organizational form, vertical separation, monitoring costs, local pricing, and wholesale-retail relationships affect station prices and behavior.
- **S6** — [2023 National State of Owner Readiness Report](https://exit-planning-institute.org/hubfs/Member%20Center%20Resources/2023%20National%20State%20of%20Owner%20Readiness%20Report.pdf) (accessed 2026-07-22): Surveyed 1,162 U.S. owners across more than 25 industries; reports about 73% of privately held companies would like to transition within ten years and documents strong preference for internal exits among family-business owners.
- **S7** — [Increasing fuel efficiency leads to decreasing gasoline consumption](https://www.eia.gov/TODAYINENERGY/detail.php?id=67426) (accessed 2026-07-22): Reports U.S. gasoline consumption averaged 8.9 million barrels per day in 2025, down 1% from 2024, and forecasts further 2026-2027 declines as roughly 1% annual fleet-efficiency gains outpace travel growth.
- **S8** — [EIA releases the Annual Energy Outlook 2026](https://www.eia.gov/pressroom/releases/press587.php) (accessed 2026-07-22): States that technology-driven efficiency keeps U.S. energy consumption flat or slightly declining through 2050 in most AEO2026 cases despite economic growth.
- **S9** — [Class A and Class B UST Operator Training and Exams](https://www.epa.gov/ust/class-a-and-class-b-ust-operator) (accessed 2026-07-22): States that operator training is required by federal UST regulations and that typical UST facilities include gas stations; owners and operators must retain operator and training records.
- **S10** — [Frequent Questions About Underground Storage Tanks](https://www.epa.gov/ust/frequent-questions-about-underground-storage-tanks) (accessed 2026-07-22): Lists owner and operator duties including registration, leak detection, spill/overfill/corrosion protection, financial responsibility, trained operators, periodic testing, inspections, records, and corrective action.
