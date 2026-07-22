# 491110 — Postal Service

*v5.1 Stage 1 research memo. Run `491110-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** no base (evidence-first) · A — · L — · interval STRUCTURAL_OUT → PRIORITY · readiness STRESS_TEST_ONLY · action EVIDENCE_FIRST

**Driver:** The principal positive driver is that surviving physical mail and package flows continue to require operational acceptance, processing, routing, and delivery, leaving a narrow but durable role for accountable operators and modest AI-enabled workflow savings.
**Weakness:** The principal weakness is firm availability: the federal operator is non-acquirable, while no defensible current evidence establishes how many private, appropriately sized, stand-alone, transferable postal contractors exist or are likely to sell.

## Business-model lens
- Included: U.S. private lower-middle-market contractors actually classified in NAICS 491110 that operate contract postal units or perform recurring outsourced mail acceptance, sorting, routing, or delivery within the Postal Service's universal-service system.
- Excluded: The U.S. Postal Service itself is excluded because it is a federal establishment rather than an acquirable private company. Also excluded are bulk mail transportation, private courier and express delivery, presort/consolidation/barcoding services, mailbox stores, ancillary postal counters that are not transferable standalone operations, shells, and non-control investments.
- Customer and revenue model: The Postal Service is the dominant contracting customer and postal patrons are the end users. Contract postal units charge Postal Service prices and receive contract compensation that may be performance-based or fixed; other included contractors earn recurring fees under Postal Service procurement arrangements.
- Deviation from default lens: The lens is narrowed to private contract operators because the overwhelmingly visible industry operator is a non-acquirable federal establishment. This is necessary to define a coherent control-investment universe, not to select for attractiveness.

## Executive view
This is not a conventional postal-industry roll-up: the central operator is a federal establishment and therefore outside the acquisition universe. A coherent thesis can only target private contract postal operators, but the size and transferability of that universe are not defensibly observed. Within that narrow lens, AI offers modest operating leverage rather than a category-changing thesis because core work remains physical and much sorting is already mechanized.

## How AI changes the work
The best near-term uses are customer-inquiry assistance, address and exception triage, scheduling, dispatch and route support, document handling, and back-office administration. Mail carrying and physical acceptance, sorting, handling, and delivery limit labor displacement; national investments in parcel sorting also indicate that part of the readily automatable work is already addressed by conventional equipment.

## Value capture
A contractor can retain some productivity benefit during a fixed or performance-based compensation period, particularly from low-cost workflow tools. Capture is nevertheless structurally constrained by Postal Service-set prices, competitive procurement, renewals, audits, contract repricing, insourcing risk, and dependence on one public contracting system.

## Firm availability
Private contract postal units and other subcontractors demonstrably exist, but public sources do not supply a current, deduplicated list linked to size, ownership, stand-alone status, NAICS classification, contract assignability, or sale behavior. Consequently both acquisition eligibility and five-year availability are left missing, and the declared firm-population gap is preserved without substitution.

## Demand durability
Physical mail demand is structurally pressured by electronic diversion. The OIG baseline implies material decline in the dominant First-Class and Marketing Mail categories, while packages and other products provide partial diversification. Postal price increases may protect nominal system revenue, but they do not erase the decline in constant-quality workload relevant to contractor operations.

## Risks and uncertainty
The largest risks are an unenumerated target universe, uncertain contract transferability, extreme customer concentration, procurement and political constraints, network redesign or insourcing, cybersecurity and systems-access limits, continued mail-volume decline, and lens heterogeneity across retail counters, processors, and delivery operators. Historical contract-unit evidence is too stale to repair the current population gap.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 1.4092 | — | OBSERVED | — |
| n | — | — | — | MISSING | — |
| a | 0.05 | 0.11 | 0.18 | PROXY | S1, S2, S3 |
| rho | 0.15 | 0.35 | 0.55 | PROXY | S3, S4 |
| e | — | — | — | MISSING | — |
| s5 | — | — | — | MISSING | — |
| q | 0.2 | 0.4 | 0.65 | ESTIMATE | S4, S5 |
| d5 | 0.76 | 0.86 | 0.94 | PROXY | S6, S7 |
| o | 0.9 | 0.97 | 0.995 | ESTIMATE | S1, S3, S6 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.42 | 2.17 | 5.58 | PROXY |
| F | — | — | — | MISSING |
| C | 4.00 | 8.00 | 10.00 | ESTIMATE |
| D | 6.84 | 8.34 | 9.35 | ESTIMATE |

## Caveats
- a: Federal Postal Service staffing may differ substantially from contract postal units and outsourced route operators.
- a: Occupational employment shares are not direct task-level AI exposure measures.
- a: Sorting machinery and generative AI are distinct technologies, so mechanization evidence is used only to avoid crediting already-automated work twice.
- rho: National Postal Service capital programs are not direct observations of private-contractor adoption.
- rho: Implementation varies between retail contract units, sorting subcontractors, and route operators.
- rho: Cybersecurity, labor rules, and Postal Service approval could slow deployment beyond a normal small-business software cycle.
- e: The historical contract postal unit count is stale and includes outlets that may be ancillary operations rather than stand-alone acquisition candidates.
- e: No observed evidence supports converting the known existence of contractors into an eligibility percentage.
- e: The declared firm-population dataset gap is preserved rather than replaced with an inferred count.
- s5: Contract duration does not establish that an operating company or its Postal Service contract can be sold.
- s5: Historical outlet closures or count declines are not equivalent to control transactions.
- s5: Any numeric sale-rate range would be unsupported while the eligible population and transfer rules remain unobserved.
- q: The GAO economics are historical and do not measure current AI-related retention.
- q: Capture may differ sharply between fixed-compensation units and volume- or performance-based arrangements.
- q: A single dominant contracting system creates greater pass-through risk than a fragmented commercial customer base.
- d5: The source forecast covers the national Postal Service, not demand specifically outsourced to private contractors.
- d5: A constant compound conversion is a simplifying assumption; volume decline may be front- or back-loaded.
- d5: Postal price increases can support nominal revenue even while constant-quality physical demand falls.
- d5: Package activity faces competitive and network-strategy dynamics not captured by the mail forecast.
- o: This estimate avoids counting electronic mail diversion again because that effect is already reflected in the demand factor.
- o: Operator necessity may be lower for retail counter functions than for last-mile delivery.
- o: A network redesign could shift work back to the Postal Service without eliminating the underlying operator function.

## Sources
- **S1** — [2022 NAICS Manual — Subsector 491 Postal Service and Industry 491110 Postal Service](https://www.census.gov/naics/reference_files_tools/2022_NAICS_Manual.pdf) (accessed 2026-07-22): Defines the industry as the Postal Service and subcontractors operating under a universal-service obligation; lists acceptance, collection, processing, routing, sorting, and delivery; and distinguishes excluded bulk transportation, presort/barcoding, and non-universal-service courier activities.
- **S2** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: Postal Service (Federal Government)](https://www.bls.gov/oes/2023/may/naics4_491100.htm) (accessed 2026-07-22): Reports 632,810 jobs and a task mix dominated by 331,600 mail carriers, 116,520 mail sorters/processors/machine operators, and 78,130 postal clerks, with management a small share; used as a federal-operator proxy for labor-task exposure.
- **S3** — [Delivering for America — Plan Details](https://about.usps.com/what/strategic-plans/delivering-for-america/details.htm) (accessed 2026-07-22): Documents investment in information technology, mobile devices, and parcel sorting, including 348 new package sorting machines and higher daily capacity, while describing the continuing six-day mail and seven-day package service mandate.
- **S4** — [Becoming a Contract Postal Unit Supplier](https://about.usps.com/what/business-services/suppliers/becoming/contract-postal-unit.htm) (accessed 2026-07-22): Shows that supplier-operated contract postal units exist; they use supplier employees, charge Postal Service prices without surcharges, are competitively contracted, and may receive performance-based compensation.
- **S5** — [U.S. Postal Service: Retail Facilities — Information on Cost and Accessibility](https://www.gao.gov/products/gao-13-41) (accessed 2026-07-22): Provides historical evidence that contract postal units were independent businesses compensated by the Postal Service, while showing varied fixed-compensation economics and a decline from 5,290 units in FY2002 to 3,619 in FY2011.
- **S6** — [U.S. Postal Service Reports Fiscal Year 2025 Results](https://about.usps.com/newsroom/national-releases/2025/1114-usps-reports-fiscal-year-2025-results.htm) (accessed 2026-07-22): Reports FY2025 volumes by product, including 42.049 billion First-Class Mail, 56.756 billion Marketing Mail, 6.837 billion shipping and package pieces, and 108.695 billion total pieces; also identifies the Postal Service as an independent federal establishment.
- **S7** — [Projecting Mail Volume: Future Trends and Implications for the Postal Service](https://www.uspsoig.gov/reports/white-papers/projecting-mail-volume-future-trends-and-implications-postal-service) (accessed 2026-07-22): Projects combined First-Class and Marketing Mail volume from 2025 to 2035, with a 29% baseline decline and a 14% to 41% range, and identifies electronic diversion as the primary cause.
