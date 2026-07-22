# 423810 — Construction and Mining (except Oil Well) Machinery and Equipment Merchant Wholesalers

*v5.1 Stage 1 research memo. Run `423810-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 7.11 · L 0.66 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** The installed equipment base produces recurring, uptime-sensitive parts demand protected in many markets by OEM territory and diagnostic rights.
**Weakness:** OEM control, inventory capital, and construction/mining cycles can impair both transferability and near-term economics despite operational improvements.

## Business-model lens
- Included: Independent and owner-controlled merchant wholesalers repeatedly supplying construction, roadbuilding, mining, quarrying, logging, forestry, and related machinery, work tools, and replacement parts to external contractors, producers, governments, and equipment users.
- Excluded: OEM captive branches, oil-well equipment wholesalers, pure rental fleets, repair-only contractors, manufacturers, shells, and non-control financing vehicles; ancillary dealer repair and rental are considered only as context for the transferable distribution relationship, not as the screened service basket.
- Customer and revenue model: High-value new and used equipment and recurring parts transactions supported by OEM territories, stocked inventory, application expertise, field sales, delivery, warranty coordination, financing facilitation, and installed-base support; revenue is transactional and cyclical rather than subscription-based.
- Deviation from default lens: none

## Executive view
Construction and mining equipment wholesalers sit between OEMs and capital-intensive customers, with repeat parts and installed-base relationships cushioning highly cyclical new-equipment sales. AI can improve information workflows, inventory, warranty, and commercial coverage, but equipment expertise, territories, physical logistics, credit, and trusted field relationships remain decisive. Transferability depends as much on OEM approval and inventory quality as on customer demand.

## How AI changes the work
Practical uses include serial-number and parts search, quote drafting, lead scoring, installed-base outreach, inventory forecasting, warranty documentation, credit review support, procurement, collections, AP, and reporting. Field application advice, site assessment, machine configuration, high-value negotiation, delivery, and safety-critical decisions remain human and asset intensive. OEM and dealer systems supply valuable data but also constrain integration rights.

## Value capture
Automation can reduce SG&A growth, accelerate quotes, improve parts availability, shrink inventory aging, and raise sales coverage. Exclusive territories and uptime needs support retention, especially in parts. Competitive bidding, used-equipment transparency, OEM economics, public procurement, and cyclical inventory liquidation can pass benefits to customers or overwhelm them.

## Firm availability
A substantial independent dealer population and an active consolidator channel support potential transfers. Diligence must verify OEM consent, territory durability, floorplan debt, aged and used inventory, warranty exposure, branch economics, customer concentration, technician and salesperson retention, environmental liabilities, and whether reported earnings rely on rental or repair activities outside the screened basket.

## Demand durability
Physical construction, infrastructure, aggregates, mining, and forestry continue to need machinery and parts, and installed fleets create repeat aftermarket demand. The outlook is mixed: public construction and decade-scale construction growth provide support, while recent private construction and dealer markets were soft and mining is cyclical. A broad range around roughly stable real quantity is more credible than a smooth trend.

## Risks and uncertainty
Principal risks are OEM non-consent or termination, territory overlap, interest rates, tariffs, public-budget timing, commodity and construction cycles, aged inventory, floorplan leverage, direct OEM channels, cyber or ERP failures, key-person loss, and misclassification of mixed dealer revenue. Evidence is weakest on six-digit occupation tasks, LMM AI execution, and closed transfer rates.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1096 | — | OBSERVED | — |
| n | — | 793 | — | ESTIMATE | — |
| a | 0.18 | 0.29 | 0.4 | PROXY | S2, S3, S4 |
| rho | 0.36 | 0.52 | 0.67 | PROXY | S3, S4 |
| e | 0.63 | 0.78 | 0.88 | ESTIMATE | S1, S3 |
| s5 | 0.16 | 0.25 | 0.37 | PROXY | S3, S7, S8 |
| q | 0.46 | 0.62 | 0.76 | ESTIMATE | S3 |
| d5 | 0.87 | 1.04 | 1.2 | PROXY | S3, S5, S6 |
| o | 0.84 | 0.93 | 0.98 | PROXY | S3, S4 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.28 | 0.66 | 1.17 | PROXY |
| F | 7.07 | 8.12 | 8.94 | ESTIMATE |
| C | 9.20 | 10.00 | 10.00 | ESTIMATE |
| D | 7.31 | 9.67 | 10.00 | PROXY |

## Caveats
- a: Occupation evidence is for all durable-goods wholesalers, not 423810.
- a: Public OEM and dealer technology may exceed LMM practice.
- a: The estimate excludes physical machine automation and concerns only distributor labor tasks.
- rho: ERP availability is not evidence of AI labor realization.
- rho: OEM-controlled software and territories can limit a buyer's freedom to standardize systems.
- rho: LMM firms may lack clean serial-number, inventory, and customer histories.
- e: The frozen count is margin-bridged and may include firms outside the true EBITDA band.
- e: Reported company activity often spans wholesale, retail, rental, repair, and multiple NAICS codes.
- e: A distributor without transferable OEM rights may not be an eligible operating platform.
- s5: National surveys measure intent or age rather than qualifying transfers.
- s5: Alta acquisitions include adjacent material-handling and other equipment verticals.
- s5: OEM approval can make seller intent irrelevant.
- q: Alta's 2025 equipment gross margin compression shows cycle and inventory can overwhelm operational gains.
- q: Exclusive territories protect some lines but not used equipment or cross-brand competition.
- q: No source directly measures AI benefit retention in LMM dealers.
- d5: Construction spending is nominal and not equipment quantity.
- d5: BLS employment is an imperfect proxy for capital equipment demand and the mining series includes oil and gas excluded from this code.
- d5: Year-five results are highly sensitive to the point in the equipment replacement cycle.
- o: Operator-required quantity differs from human-touch frequency.
- o: OEMs control territories, diagnostic systems, and parts access and could reshape the channel.
- o: Used equipment marketplaces can self-serve more of the transaction while still relying on physical fulfillment.

## Sources
- **S1** — [NAICS Code Description: 423810 Construction and Mining Machinery and Equipment Merchant Wholesalers](https://www.naics.com/naics-code-description/?code=423810) (accessed 2026-07-22): Defines merchant wholesale distribution of specialized construction, mining excluding oil well, logging machinery, equipment, and related parts.
- **S2** — [Merchant Wholesalers, Durable Goods: NAICS 423](https://www.bls.gov/IAG/TGS/iag423.htm) (accessed 2026-07-22): Reports the broader subsector's major 2025 occupations, including 418,260 nontechnical wholesale sales representatives, 219,680 hand material movers, 105,870 technical sales representatives, 88,300 light delivery drivers, and 75,730 shipping/receiving clerks.
- **S3** — [Alta Equipment Group 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/1759824/000119312526076932/altg-20251231.htm) (accessed 2026-07-22): Same-channel evidence on exclusive OEM territories, equipment and parts sales, dealership ERP and service histories, uptime and field sales, 49% five-OEM purchase concentration, 17 acquisitions since 2020, owner approaches, parts margins, and mixed 2025 construction conditions.
- **S4** — [Caterpillar Inc. 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/18230/000001823026000008/cat-20251231.htm) (accessed 2026-07-22): Describes one of the largest independent global dealer networks, construction and resource equipment and parts, parts distribution, dealer administration, automation, software, data analytics, and digital customer/dealer buying solutions.
- **S5** — [BLS Employment Projections 2024-2034](https://www.bls.gov/news.release/archives/ecopro_08282025.pdf) (accessed 2026-07-22): Projects construction employment growth of 4.4% and mining, quarrying, and oil and gas extraction decline of 1.6% from 2024 to 2034.
- **S6** — [U.S. Census Construction Spending: December and Annual 2025](https://www.census.gov/construction/c30/pdf/pr202512.pdf) (accessed 2026-07-22): Reports 2025 private construction of $1,647.5 billion, down 2.9% from 2024, and public construction of $516.8 billion, up 3.6%.
- **S7** — [Five Key Wake-Up Calls for Ambitious Business Owners](https://www.kiplinger.com/business/small-business/key-wake-up-calls-for-ambitious-business-owners) (accessed 2026-07-22): Cites the 2023 National State of Owner Readiness Report: 49% of owners wanted to exit within five years and 42% had a formal written transition plan.
- **S8** — [Starting a small business is hard. Exiting can be even harder, but planning early is the key](https://apnews.com/article/d582a18f1e440846a6ff5bb425ba6daa) (accessed 2026-07-22): Reports Census-based evidence that 51% of small-business owners are over age 55 and distinguishes external sale, internal succession, and wind-down paths.
