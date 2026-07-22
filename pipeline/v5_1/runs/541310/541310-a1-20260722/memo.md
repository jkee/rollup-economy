# 541310 — Architectural Services

*v5.1 Stage 1 research memo. Run `541310-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** CONDITIONAL · A 7.77 · L 3.40 · interval LOW_PRIORITY → PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** A labor-intensive digital production workflow creates broad assistive-AI use cases across documentation, specifications, research, visualization, and administration.
**Weakness:** Project cyclicality and competitive fee renegotiation can prevent technically achievable labor savings from becoming durable retained cash flow.

## Business-model lens
- Included: US architectural-services firms in the $1-10M normalized EBITDA band that provide building planning, architectural design, documentation, specification, permitting, and construction-phase services to external owners and repeat or recurring clients.
- Excluded: Captive internal design units, shell entities, non-control financing vehicles, design-build contractors classified in construction, landscape architecture, standalone engineering, and firms without transferable operating relationships or accountable architectural-service delivery.
- Customer and revenue model: Project-based outsourced professional services for private and public owners, commonly billed by stipulated sum, professional fee plus reimbursables, hourly rates, or a percentage of construction cost; repeat demand comes from continuing owner relationships and successive projects rather than subscriptions.
- Deviation from default lens: none

## Executive view
Architectural services offer a material but bounded AI labor opportunity. Digital documentation, research, specifications, visualization, proposals, and project administration are exposed, while licensed judgment, client coordination, site context, and responsibility for code-compliant designs limit substitution. The opportunity depends on converting immature experimentation into controlled workflows and retaining savings despite competitive fee pressure.

## How AI changes the work
AI is likely to assist rather than replace architects over the five-year horizon. The strongest use cases are document drafting and review, meeting records, product and code research, specification support, visualization, option generation, takeoffs, and internal operations. Human architects still must validate outputs, reconcile disciplines, interpret client needs, exercise design judgment, and take responsible control of signed work.

## Value capture
Stipulated-sum and pre-agreed professional-fee projects let an operator retain early productivity gains when delivery hours fall. Hourly projects pass savings to clients more directly, and later renewals, competitive procurement, and fee negotiation should share gains across the market. Capacity released by AI can also support more projects, but that is not assumed to eliminate pricing pressure.

## Firm availability
The frozen dataset estimates 1,589 firms in the EBITDA band, but eligibility is lower because some project boutiques and principal-dependent practices lack durable repeat relationships or transferable operations. AIA survey evidence indicates industry expectations for rising M&A activity, yet most individual leaders still view a merger or acquisition as unlikely, and small-firm transition planning has historically been sparse.

## Demand durability
Underlying need for building design, renovation, healthcare, resilience, sustainability, and regulatory navigation should persist, but architecture is cyclical and tied to financing and construction markets. Current nonresidential conditions are weak and sector outcomes are sharply split. AI and BIM improve productivity, yet regulation and architect-of-record accountability make wholesale software substitution unlikely within five years.

## Risks and uncertainty
The principal risks are prolonged construction weakness, fee compression that transfers productivity gains to clients, unreliable or insecure AI outputs, professional-liability exposure, slow adoption at smaller firms, and acquisitions of relationship-dependent practices that do not survive founder exit. The largest empirical gaps are payroll-weighted task exposure, realized workflow savings, and completed control-transfer incidence for LMM architecture firms.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.4625 | — | OBSERVED | — |
| n | — | 1589 | — | ESTIMATE | — |
| a | 0.28 | 0.4 | 0.52 | PROXY | S2, S3 |
| rho | 0.28 | 0.46 | 0.62 | PROXY | S3, S4, S9 |
| e | 0.68 | 0.82 | 0.92 | ESTIMATE | S1, S4 |
| s5 | 0.08 | 0.16 | 0.27 | PROXY | S6, S8 |
| q | 0.36 | 0.56 | 0.72 | PROXY | S5 |
| d5 | 0.88 | 1.01 | 1.13 | PROXY | S2, S7 |
| o | 0.81 | 0.9 | 0.96 | PROXY | S9, S10 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 1.45 | 3.40 | 5.96 | PROXY |
| F | 7.19 | 8.60 | 9.62 | ESTIMATE |
| C | 7.20 | 10.00 | 10.00 | PROXY |
| D | 7.13 | 9.09 | 10.00 | PROXY |

## Caveats
- a: No source directly reports a wage-weighted exposure share for NAICS 541310.
- a: The AIA survey covers architectural professionals and firm leaders rather than a representative payroll-weighted sample of LMM firms.
- a: Exposure is limited to current, not-yet-automated tasks; existing CAD/BIM productivity is excluded conceptually but cannot be measured precisely.
- rho: Adoption status is not equivalent to implemented labor substitution or avoided hiring.
- rho: The AIA studies include firms outside the frozen EBITDA band and may overweight firms active in the association.
- rho: Tool capabilities and professional standards may change substantially during the five-year horizon.
- e: The frozen n estimate already bridges firm size into an EBITDA band; e does not re-estimate that input.
- e: The 84% architect-of-record statistic is billings-weighted, dated 2019, and not a firm eligibility rate.
- e: Repeat-client behavior is not directly quantified in the fetched evidence.
- s5: Surveyed likelihood is not observed transaction incidence and includes firms outside the LMM band.
- s5: The small-firm transition-plan evidence is from 2020 and planning does not imply a control transfer.
- s5: Architecture firms may transition internally over many years, which does not necessarily meet the qualifying-transfer definition.
- q: Billing-method shares are from 2019, before the current generative-AI cycle.
- q: Professional fee plus reimbursables does not reveal whether the professional component is fixed, hourly, or renegotiable.
- q: The estimate does not include demand volume loss, which belongs in d5 and o, or implementation friction, which belongs in rho.
- d5: Employment is an input proxy rather than a direct measure of constant-quality service quantity.
- d5: The AIA forecast covers nonresidential construction only and extends just through 2027.
- d5: Residential work, regional cycles, renovation, interest rates, and construction-cost inflation create substantial dispersion.
- o: Licensing rules vary, and many jurisdictions exempt certain small residential, agricultural, or low-risk projects.
- o: Title and practice regulation do not guarantee that the current firm model captures all required accountability.
- o: The estimate covers year-five quantity after elimination or self-service, not task automation within retained projects.

## Sources
- **S1** — [2022 NAICS Definition: 541310 Architectural Services](https://www.census.gov/naics/?details=541310&input=5413&year=2022) (accessed 2026-07-22): Defines the industry as establishments planning and designing residential, institutional, leisure, commercial, and industrial buildings and structures using knowledge of design, construction, zoning, codes, and materials.
- **S2** — [Occupational Outlook Handbook: Architects](https://www.bls.gov/ooh/architecture-and-engineering/architects.htm) (accessed 2026-07-22): Reports architect duties and work context, 123,600 jobs in 2024, 76% employed in architectural/engineering/related services, 4% projected employment growth for 2024-34, and continued demand alongside BIM, measuring technology, and AI productivity gains.
- **S3** — [Architects are excited about the potential of AI, but concerns abound](https://www.aia.org/aia-architect/article/architects-are-excited-about-potential-ai-concerns-abound) (accessed 2026-07-22): A statistically valid AIA survey reports 8% of firm leaders integrated AI, 20% implementing, 35% considering, 6% of individuals using regularly, 53% experimenting, common low-risk uses, inefficient task areas, and 90-94% concern levels across major risk categories.
- **S4** — [AIA Firm Survey Report 2024](https://www.aia.org/resource-center/aia-firm-survey-report-2024) (accessed 2026-07-22): Reports results from more than 1,200 firms, one-third of firms using AI day to day, and firm metrics spanning billings, practice, technology, and ownership-transition planning; the linked report summary also contextualizes architect-of-record billings.
- **S5** — [Architecture Billings Index March 2024: Architecture firm billings retreat further](https://www.aia.org/resource-center/abi-march-2024-architecture-firm-billings-retreat-further-march) (accessed 2026-07-22): Reports fee-method use and profitability perceptions, including 93% of firms using hourly rates and 92% stipulated sums, plus 46% finding fee negotiation more challenging than four to five years earlier; it also links the 2019 billings mix used in the rationale.
- **S6** — [Architecture Billings Index August 2025: Softness persists at architecture firms](https://www.aia.org/resource-center/abi-august-2025-softness-persists-architecture-firms) (accessed 2026-07-22): Reports 63% of firm leaders expect US architecture M&A to increase over three to five years, while 36% say their own firm is not at all likely and 28% not very likely to merge or be acquired; 5% say very likely.
- **S7** — [AIA Consensus Construction Forecast: July 2026](https://www.aia.org/resource-center/july-2026-consensus-construction-forecast) (accessed 2026-07-22): Reports nonresidential construction spending down 2% in 2025, a forecast 0.3% decline in 2026 and 3.0% growth in 2027, persistent architecture-billings weakness, and large differences across building sectors.
- **S8** — [23% of Firms Have Ownership Transition Plans](https://www.architectmagazine.com/aia-architect/aianow/23-of-firms-have-ownership-transition-plans_o/) (accessed 2026-07-22): Reports from the AIA Firm Survey 2020 that 15% of small firms with two to nine employees, 60% of midsize firms, and 90% of large firms had ownership transition plans; sole practitioners were at 4%.
- **S9** — [AIA AI Firm Toolkit](https://aifirmtoolkit.aia.org/) (accessed 2026-07-22): States that professional responsibility cannot be delegated, architects remain responsible for AI-produced work, and the architect of record remains responsible for code compliance and design integrity regardless of AI involvement.
- **S10** — [NCARB: Contact Your Licensing Board](https://www.ncarb.org/become-architect/earn-license/state-licensing-boards) (accessed 2026-07-22): States that all 55 US jurisdictions have architecture boards responsible for issuing licenses, regulating architectural practice, and protecting public health, safety, and welfare.
