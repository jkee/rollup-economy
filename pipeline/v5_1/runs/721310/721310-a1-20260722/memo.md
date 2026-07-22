# 721310 — Rooming and Boarding Houses, Dormitories, and Workers' Camps

*v5.1 Stage 1 research memo. Run `721310-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 6.02 · L 0.89 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** A repeatable centralized AI layer can reduce administrative and coordination work across multi-property operators while on-site teams continue the physical service.
**Weakness:** The code mixes transferable commercial operators with captive, membership, passive-property, and asset-sale structures, leaving firm eligibility and qualifying transfer incidence poorly observed.

## Business-model lens
- Included: US operators of rooming and boarding houses, off-campus dormitories, and worker accommodations that repeatedly provide managed lodging and related services to paying residents or external institutional or employer customers, with normalized EBITDA of roughly $1-10 million.
- Excluded: Passive real-estate ownership without operating staff; captive on-campus dormitories and employer-run camps serving only the owner's own organization; fraternity, sorority, religious, or other membership housing that is not commercially transferable; shells; and non-control financing vehicles.
- Customer and revenue model: Residents commonly pay recurring bed or room rent under monthly or academic-year arrangements; student housing may be leased by the bed, while externally operated worker housing may be paid by an employer or project sponsor. Housekeeping, meals, laundry, maintenance, and resident support may be bundled or sold as complementary services.
- Deviation from default lens: The code is heterogeneous across resident-paid rooming houses, student housing, membership housing, and worker camps. To keep the screen coherent, it retains only commercially transferable operators serving external residents or sponsors and excludes captive or nontransferable organization housing; this is a business-model coherence restriction, not an attractiveness selection.

## Executive view
This is a small, heterogeneous operating niche built around essential physical accommodation. The credible AI opportunity is concentrated in reservations, billing, resident communications, scheduling, documentation, procurement, and management support; most labor remains cleaning, food preparation, residential presence, and maintenance. Commercially transferable operators exist, but captive dormitories, membership housing, passive property structures, and asset-only transactions materially shrink the relevant population.

## How AI changes the work
AI can triage resident inquiries, draft and route communications, reconcile charges, support leasing and collections, forecast occupancy, schedule staff, summarize incidents, and surface maintenance priorities. It is less able to replace room cleaning, cooking, repairs, site inspection, de-escalation, emergency response, and the trusted residential-advisor role. The strongest operating design is therefore a centralized digital service layer supporting on-site teams, not an unattended property.

## Value capture
Resident leases and academic-year fixed terms permit savings to remain with the operator until renewal rather than forcing immediate pass-through. Over repeated renewals, market competition and institutional procurement can share the benefit with customers, especially in sponsored worker housing or transparent service contracts. Capture depends on improving labor productivity without degrading responsiveness, safety, cleanliness, or resident experience.

## Firm availability
The classification spans commercially operated rooming and student housing as well as fraternity, sorority, club, and worker-camp structures. Only an estimated portion of the dataset-implied LMM firms are independent, externally serving, staffed platforms whose control can transfer. Transaction evidence specific to this code is absent, and property sales must be separated from acquisition of a continuing operating business.

## Demand durability
Five-year constant-quality demand is likely close to flat with a modest positive base. Postsecondary enrollment projections support the student component, physical housing scarcity supports rooming demand, and project activity can support worker accommodation, but each submarket is local and cyclical. Regardless of volume, occupied accommodation still requires accountable physical operations, so software is more likely to change how the service is delivered than eliminate the service basket.

## Risks and uncertainty
The largest risks are classification heterogeneity, an unknown eligible-firm denominator, asset-heavy economics, local occupancy cycles, regulation, resident safety, privacy, fair-housing compliance, and weak integration across older property systems. A bad outcome would combine low eligibility and sparse control transfers with only small administrative savings, while rent competition or employer contracting shares those savings with customers. The frozen compensation ratio also uses 2024 wages over 2022 receipts and a cross-code harmonization, so it may misstate current operating labor intensity.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1935 | — | OBSERVED | — |
| n | — | 88 | — | ESTIMATE | — |
| a | 0.13 | 0.21 | 0.31 | ESTIMATE | S2, S3, S4 |
| rho | 0.35 | 0.55 | 0.75 | PROXY | S5, S6 |
| e | 0.35 | 0.55 | 0.72 | ESTIMATE | S1, S7 |
| s5 | 0.08 | 0.16 | 0.28 | ESTIMATE | S10 |
| q | 0.45 | 0.67 | 0.85 | ESTIMATE | S7 |
| d5 | 0.92 | 1.02 | 1.1 | PROXY | S8, S9, S11 |
| o | 0.88 | 0.95 | 0.99 | ESTIMATE | S1, S3, S4, S9 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.35 | 0.89 | 1.80 | ESTIMATE |
| F | 2.00 | 3.49 | 4.71 | ESTIMATE |
| C | 9.00 | 10.00 | 10.00 | ESTIMATE |
| D | 8.10 | 9.69 | 10.00 | ESTIMATE |

## Caveats
- a: OEWS covers all employer establishments in NAICS 721300 and excludes self-employed workers; it is not limited to the eligible LMM lens.
- a: The estimate applies judgment to task exposure and does not assume that all clerical work is substitutable.
- a: Occupation shares are employment-weighted in the source; the estimate adjusts qualitatively for wage differences rather than reconstructing microdata-level wage weights.
- rho: BTOS changed its AI-use wording in late 2025 and is economy-wide rather than industry-specific.
- rho: The field study concerns assisted customer support, not rooming-house operations or full task substitution.
- rho: Implementation is sensitive to operator size and the quality of incumbent property-management data.
- e: The Census establishment count is not the dataset firm count and does not reveal ownership, EBITDA, captive status, or transferability.
- e: The SEC example demonstrates a transferable commercial student-housing model but is not representative of every component of NAICS 721310.
- e: Eligibility may be lower if many LMM entities are property-holding vehicles rather than staffed operating companies.
- s5: The cited market covers US small businesses broadly, not this NAICS code or the $1-10 million EBITDA band.
- s5: Real-estate transfers may not constitute a qualifying transfer of an operating business.
- s5: Owner age, succession intention, and actual five-year transaction incidence are not observed for the eligible population.
- q: The filing describes one student-housing property before its sale and does not cover rooming houses or worker-camp contracts.
- q: The estimate separates retention from implementation and demand effects, but competitive responses over five years remain unobserved.
- q: Property rent may reflect location and capital more than service cost, making pass-through weaker than in open-book service contracts.
- d5: NCES projections were prepared in December 2022 and end in 2031; they do not measure housing propensity or the worker-camp and rooming-house components.
- d5: The lodging-manager outlook is occupation-wide and mainly reflects traditional hotels and motels.
- d5: The employment index is not a direct quantity-demand series and can move with productivity or occupational classification.
- o: Accountability and minimum staffing requirements vary by state, property type, resident population, and contract.
- o: The estimate concerns whether an operator remains required, not whether individual administrative tasks are automated.
- o: Some simple rooming houses may shift more administration to software than full-service dormitories or camps.

## Sources
- **S1** — [721310: Rooming and Boarding Houses, Dormitories, and Workers' Camps - Census Bureau Profile](https://data.census.gov/profile/721310_-_Rooming_and_Boarding_Houses%2C_Dormitories%2C_and_Workers%27_Camps?codeset=naics~721310) (accessed 2026-07-22): Defines the included establishment types, principal-residence accommodation, possible housekeeping/meals/laundry services, and reports 1,589 employer establishments in 2023.
- **S2** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 721300](https://www.bls.gov/oes/2023/may/naics4_721300.htm) (accessed 2026-07-22): Industry occupation mix and wages: 9,940 total jobs; food service 21.47%, cleaning/grounds 27.21%, residential advisors 13.19%, office/admin 15.22%, management 9.08%, and maintenance/repair 7.25%.
- **S3** — [O*NET OnLine: Hotel, Motel, and Resort Desk Clerks](https://www.onetonline.org/link/summary/43-4081.00) (accessed 2026-07-22): Lists desk-clerk tasks including reservations, room assignment, account records, charges, payments, inquiries, complaint escalation, bookkeeping, key issuance, housekeeping coordination, and staff scheduling.
- **S4** — [O*NET OnLine: Maids and Housekeeping Cleaners](https://www.onetonline.org/link/details/37-2012.00) (accessed 2026-07-22): Describes the physical cleaning occupation and core tasks such as cleaning rooms and common areas, replenishing supplies, and cleaning carpets and furnishings.
- **S5** — [Large Firms With at Least 20 Employees Biggest AI Users](https://www.census.gov/library/stories/2026/05/ai-use-businesses.html) (accessed 2026-07-22): BTOS evidence that overall business AI use was 17%-20% from December 2025 to May 2026, expected six-month use was 20%-23%, adoption was below 20% for the smallest firms, and use increased with larger size.
- **S6** — [Generative AI at Work](https://www.nber.org/papers/w31161) (accessed 2026-07-22): Field evidence from 5,179 customer-support agents that conversational AI assistance increased issues resolved per hour by 14% on average, with heterogeneous effects by worker experience.
- **S7** — [Strategic Student & Senior Housing Trust, Inc. 2024 Form 10-K](https://www.sec.gov/Archives/edgar/data/1698538/000095017025043115/sssht-20241231.htm) (accessed 2026-07-22): Describes a student-housing property leased by the bed on fixed individual terms aligned with the academic year, billed monthly, with furnished units and shared amenities.
- **S8** — [NCES Table 303.10: Total fall enrollment in degree-granting postsecondary institutions through 2031](https://nces.ed.gov/programs/digest/d22/tables/dt22_303.10.asp) (accessed 2026-07-22): Projects total enrollment of 19,807,880 in 2026 and 20,233,776 in 2031, with projections prepared in December 2022.
- **S9** — [BLS Occupational Outlook Handbook: Lodging Managers](https://www.bls.gov/ooh/management/lodging-managers.htm) (accessed 2026-07-22): Projects lodging-manager employment to grow 3% from 2024 to 2034 and describes duties involving inspection, standards, resident or guest questions, staff management, front-desk coordination, budgets, and round-the-clock accountability.
- **S10** — [BizBuySell Insight Report - Market Trends](https://www.bizbuysell.com/insight-report/) (accessed 2026-07-22): Reports 2,345 US small businesses bought and sold in 2026 Q1 and explains that its market analysis covers roughly 50,000 businesses for sale and recently sold, with closed transactions voluntarily reported by brokers.
- **S11** — [ALFRED: Employment for Accommodation and Food Services: Rooming and Boarding Houses (NAICS 721310)](https://alfred.stlouisfed.org/series?seid=IPUTN721310W010000000) (accessed 2026-07-22): Reports the 2024 employment index at 77.0 with 2017=100 and defines employment to include wage and salary workers, unincorporated self-employed workers, and unpaid family workers.
