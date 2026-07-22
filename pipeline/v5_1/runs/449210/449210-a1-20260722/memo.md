# 449210 — Electronics and Appliance Retailers

*v5.1 Stage 1 research memo. Run `449210-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** no base (evidence-first) · A — · L — · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness STRESS_TEST_ONLY · action EVIDENCE_FIRST

**Driver:** AI can compress high-volume coordination and diagnostic-support work while unavoidable physical installation and repair preserve accountable local service demand.
**Weakness:** The eligible independent appliance-service subset is not separately counted inside a broad, chain- and e-commerce-exposed retail code.

## Business-model lens
- Included: Lower-middle-market household-appliance retailers that repeatedly provide externally accountable product specification, delivery, installation, repair, warranty coordination, and ongoing support to property managers, builders, hospitality operators, senior-living operators, and repeat households.
- Excluded: Pure product retailers and e-commerce sellers; consumer-electronics, computer, mobile-accessory, software, and recorded-media sellers; manufacturer-owned or captive service locations; standalone repair firms classified outside 449210; big-box chains; and owner-only shops without transferable service operations.
- Customer and revenue model: Product sales and margin combined with fixed-fee delivery, installation, repair, service plans, parts, and warranty reimbursement; recurrence comes from installed-base failures, portfolio replacements, builder turns, and multi-property customer relationships.
- Deviation from default lens: NAICS 449210 combines major appliances, consumer electronics, computers, software, recorded media, product-only retail, and retail bundled with repair/support. These models have sharply different physical work, obsolescence, demand, and service recurrence, so the lens is narrowed to household-appliance dealers with recurring installation and after-sales service.

## Executive view
The coherent lens is the appliance dealer that owns a repeat service relationship, not electronics retail broadly. AI can materially streamline selling, dispatch, warranty administration, parts and manual search, and diagnostic support, while delivery, installation, and repair remain physical and accountable. The core uncertainty is eligibility: the NAICS code is broad, chains and online sellers are prominent, and the LMM service-bearing firm count is missing.

## How AI changes the work
AI changes the information flow around the truck roll: lead qualification, product matching, quote and order creation, scheduling, warranty intake, manual retrieval, symptom triage, parts search, customer updates, and technician documentation. It can reduce avoidable visits and administrative time, but technicians still must verify conditions, move equipment, connect utilities, test systems, replace parts, and handle safety exceptions.

## Value capture
Dealers can initially retain savings through fixed service fees, installation bundles, improved utilization, and fewer administrative errors. Retention is limited by transparent appliance pricing, OEM warranty schedules, builder bidding, service-plan economics, and large omnichannel competitors. Service capability can carry better economics than product resale, but that evidence comes from a large chain rather than the target population.

## Firm availability
Qualifying firms require LMM scale, technicians or controlled service capacity, repeat external accounts, transferable systems, and independence from chains or captive OEM structures. The official code includes many product-only and non-appliance sellers, so only a minority is eligible. General employer-owner succession data supports some five-year transfer flow, but manufacturer authorizations and owner relationships complicate transfers.

## Demand durability
Major appliances are essential installed equipment with continuing replacement, installation, and failure-driven repair. Real service quantity should be approximately stable over five years, with housing and upgrade cycles offset by repair demand during replacement deferral. Physical operator need remains high, though manufacturers, marketplaces, and standalone service networks can take the relationship away from the retailer.

## Risks and uncertainty
The thesis fails if product margin dominates, service is subcontracted without customer ownership, OEM access does not transfer, online platforms acquire the account, or technician shortages prevent scaling. AI diagnosis errors can create repeat visits or safety exposure. Evidence is largely at 4492, occupation, general-owner, or large-chain level rather than direct LMM appliance-dealer cohorts.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1014 | — | ESTIMATE | — |
| n | — | — | — | MISSING | — |
| a | 0.16 | 0.26 | 0.38 | PROXY | S2, S3, S4, S5 |
| rho | 0.3 | 0.52 | 0.71 | ESTIMATE | S3, S5, S6, S11 |
| e | 0.05 | 0.15 | 0.28 | ESTIMATE | S1, S2 |
| s5 | 0.08 | 0.16 | 0.24 | PROXY | S7 |
| q | 0.34 | 0.54 | 0.7 | ESTIMATE | S9, S10 |
| d5 | 0.9 | 1.01 | 1.14 | PROXY | S8, S12 |
| o | 0.66 | 0.81 | 0.91 | PROXY | S3, S10, S11 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.19 | 0.55 | 1.09 | ESTIMATE |
| F | — | — | — | MISSING |
| C | 6.80 | 10.00 | 10.00 | ESTIMATE |
| D | 5.94 | 8.18 | 10.00 | PROXY |

## Caveats
- a: The BLS occupation mix is at 4492 and includes consumer-electronics business models excluded from the lens.
- a: O*NET occupation tasks are not dealer-specific and do not measure current automation penetration.
- a: The provided compensation-to-receipts input is LOW quality at ancestor 44-45 with a 2024-wage/2022-receipts mismatch, so overall labor intensity may differ materially for service-bearing appliance dealers.
- rho: Gallup's frontline adoption statistic is economy-wide rather than appliance-specific.
- rho: Manufacturer restrictions can both impede independent tool integration and make authorized data access more valuable.
- rho: Implementation excludes pricing, sales uplift, and demand effects.
- e: The NAICS definition establishes scope but not the proportion of establishments offering recurring service.
- e: Large chains may account for much activity but are outside the LMM independent-firm lens.
- e: The supplied n input is missing, so this share cannot yield a defensible eligible-firm count.
- s5: The Gallup survey is cross-industry and measures intentions rather than completed deals.
- s5: No appliance-dealer control-transfer series was found.
- s5: A manufacturer authorization may not transfer automatically with ownership.
- q: Best Buy is a large omnichannel chain, not an LMM independent dealer.
- q: No source directly measures automation-savings pass-through in appliance service.
- q: Warranty work, retail projects, and negotiated commercial accounts have different pricing constraints.
- d5: Occupation and industry employment are imperfect demand measures and use a ten-year horizon.
- d5: AHAM identifies authoritative shipment data but the detailed current unit series is paywalled, so it is not used numerically.
- d5: Consumer electronics trends inside 4492 make the broader industry projection a noisy lower bound for appliances.
- o: O*NET establishes physical tasks but not future channel ownership.
- o: FTC evidence emphasizes phones and cars as well as appliances and dates to 2021.
- o: A physical technician may remain necessary while the retail operator itself is displaced.

## Sources
- **S1** — [449210: Electronics and Appliance Retailers](https://data.census.gov/profile/449210_-_Electronics_and_Appliance_Retailers?codeset=naics~449210) (accessed 2026-07-22): The Census definition includes household appliances, consumer electronics, single-line electronics, products combined with repair/support, software, and recorded media, establishing the code's heterogeneity.
- **S2** — [May 2024 OEWS Industry Employment Charts](https://www.bls.gov/oes/2024/may/ind_emp_chart/ind_emp_chart_data.htm) (accessed 2026-07-22): For electronics and appliance retailers, BLS reports 119,960 retail salespersons, 69,240 service sales representatives, 22,890 shipping/receiving clerks, 22,700 computer repairers, 20,000 retail supervisors, 18,750 nonretail sales supervisors, 10,990 general managers, 9,160 appliance repairers, 8,900 audiovisual installers, and 8,450 customer-service representatives.
- **S3** — [O*NET: Home Appliance Repairers](https://www.onetonline.org/link/details/49-9031.00) (accessed 2026-07-22): Core tasks include billing, customer/work-order intake, manuals and schematics, operating observation, circuit tests, cost estimates, disassembly, physical parts replacement, emergency response, repair, and installation.
- **S4** — [O*NET: Retail Salespersons](https://www.onetonline.org/link/details/41-2031.00) (accessed 2026-07-22): Retail-sales tasks include needs discovery, recommendations, pricing, payments, product explanation, demonstrations, inventory, returns, special orders, records, contracts, cost estimates, and service or delivery arrangements.
- **S5** — [Labor market impacts of AI: A new measure and early evidence](https://www.anthropic.com/research/labor-market-impacts) (accessed 2026-07-22): Anthropic's occupation measure combines O*NET tasks, theoretical LLM speedup, observed work usage, automation mode, and task-time weights, while noting adoption and workflow constraints between capability and realized coverage.
- **S6** — [AI Use at Work Has Nearly Doubled in Two Years](https://www.gallup.com/workplace/691643/work-nearly-doubled-two-years.aspx) (accessed 2026-07-22): Gallup reports frequent AI use at 9% for production/frontline workers in 2025 versus 27% for white-collar workers; only 22% of employees said their organization communicated a clear AI plan.
- **S7** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Gallup reports 14% of owners planned to sell, go public, or transfer within five years, 17% among owners 55 or older, and 22% among employer-business owners; 52.3% of U.S. employer businesses were owned by people 55 or older.
- **S8** — [BLS Occupational Projections and Worker Characteristics, 2024-2034](https://www.bls.gov/emp/tables/occupational-projections-and-characteristics.htm) (accessed 2026-07-22): BLS projects home-appliance-repairer employment from 37,300 in 2024 to 38,300 in 2034, a 2.6% increase, with 3,100 average annual openings.
- **S9** — [Best Buy Fiscal 2026 Form 10-K](https://www.sec.gov/Archives/edgar/data/764478/000076447826000009/bby-20260131.htm) (accessed 2026-07-22): Best Buy reported domestic online revenue at 34.4% of segment revenue, appliances at 11% of revenue with comparable sales down 8.9%, services at 6% with sales up 1.0%, and service rate improvement offsetting lower product margin rates.
- **S10** — [Quarterly Retail E-Commerce Sales, First Quarter 2026](https://www.census.gov/retail/eCommerce.html) (accessed 2026-07-22): Census reports e-commerce at 16.9% of total U.S. retail sales in first-quarter 2026, growing 9.8% year over year versus 3.9% for all retail.
- **S11** — [Nixing the Fix: An FTC Report to Congress on Repair Restrictions](https://www.ftc.gov/system/files/documents/reports/nixing-fix-ftc-report-congress-repair-restrictions/nixing_the_fix_report_final_5521_630pm-508_002.pdf) (accessed 2026-07-22): The FTC reports that many consumer products have become harder to fix and that repair can require specialized tools, difficult-to-obtain parts, and proprietary diagnostic software, limiting consumer and independent-repair choices.
- **S12** — [AHAM Top Industry Data and Research](https://www.aham.org/AHAM/What_We_Do/Top_Industry_Data__Research) (accessed 2026-07-22): AHAM identifies major-appliance factory shipment reports and a five-year monthly series covering domestic and imported unit shipments, confirming an obtainable direct demand dataset though the detailed figures require subscription.
