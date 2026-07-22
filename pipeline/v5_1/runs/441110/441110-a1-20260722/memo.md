# 441110 — New Car Dealers

*v5.1 Stage 1 research memo. Run `441110-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 7.45 · L 0.61 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** A large wage-weighted sales, management, and administrative layer sits alongside high-volume repeat service operations where AI can reduce response and processing work.
**Weakness:** Most revenue is still competitive vehicle retail, and physical technician work plus OEM, regulatory, and system-integration constraints limit implementable substitution.

## Business-model lens
- Included: U.S. franchised new-car dealerships in the lower-middle-market EBITDA band that sell vehicles and provide repeat external-customer service, parts, warranty, and related transaction support through an accountable dealership operator.
- Excluded: Standalone used-car dealers, independent repair shops, captive OEM or finance-company units, non-control financing vehicles, shells, and rooftops without a material repeat service relationship with external customers.
- Customer and revenue model: Consumers and small fleets purchase new and used vehicles transactionally; dealerships also earn finance-and-insurance income and repeat fixed-operations revenue from customer-pay repair, warranty work, service contracts, parts, and body work.
- Deviation from default lens: none

## Executive view
New-car dealerships combine a highly competitive, cyclical retail engine with a smaller but repeat and operationally important fixed-operations business. The occupation mix creates real AI opportunity in sales support, customer communications, finance paperwork, scheduling, and administration, while a quarter of employment is installation, maintenance, and repair work that remains largely physical. Deal activity is observable, but the margin-bridged LMM count and the distinction between rooftops, franchises, and firms are important uncertainties.

## How AI changes the work
AI can handle first-response lead qualification, appointment booking, CRM follow-up, marketing drafts, inventory descriptions, document extraction, call summarization, knowledge retrieval, and routine accounting support. Human staff remain central to negotiation, customer trust, compliant F&I decisions, exception handling, diagnosis, repair, and physical vehicle movement. Fragmented dealer systems and customer-data safeguards make workflow integration and review discipline as important as model capability.

## Value capture
Labor savings are not contractually passed through, so an operator can initially retain them. Over time, online price comparison and local competition should share some benefit through vehicle pricing and service offers. Retention should be better in service and parts than in new-vehicle sales, but OEM warranty reimbursement and customer shopping constrain both.

## Firm availability
The industry has an active control market: 2024 produced 438 reported transactions involving 697 franchises. That evidence does not directly reveal the five-year transfer rate of eligible LMM firms, because one firm can own multiple rooftops and one deal can include multiple franchises. Eligibility is also lower than the raw firm count where a rooftop lacks material external service operations or where group and franchise structures frustrate a clean control transfer.

## Demand durability
Vehicle stock and miles traveled remain supportive, and older vehicles plus advanced safety-system calibrations sustain repair needs. New-vehicle purchases are cyclical and affordability-sensitive, while EVs reduce some routine service. Physical delivery, warranty, parts, diagnostics, and repair leave most of the surviving basket dependent on an accountable operator even as discovery and paperwork migrate online.

## Risks and uncertainty
The largest measurement risks are the four-digit occupation proxy, the margin-based LMM firm count, and the mismatch between transaction, franchise, rooftop, and firm counts. Commercial risks include OEM control of franchise economics, direct-sales or agency models, interest-rate and tariff shocks, cybersecurity obligations, technician scarcity, volatile vehicle gross profit, and AI errors in regulated or customer-facing workflows.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.0865 | — | OBSERVED | — |
| n | — | 8868 | — | ESTIMATE | — |
| a | 0.24 | 0.34 | 0.44 | PROXY | S1 |
| rho | 0.35 | 0.52 | 0.68 | ESTIMATE | S3, S4 |
| e | 0.55 | 0.7 | 0.84 | ESTIMATE | S2 |
| s5 | 0.1 | 0.16 | 0.23 | PROXY | S2, S5 |
| q | 0.5 | 0.64 | 0.77 | ESTIMATE | S2, S3 |
| d5 | 0.94 | 1.02 | 1.09 | PROXY | S2, S6, S7 |
| o | 0.8 | 0.9 | 0.96 | ESTIMATE | S1, S2 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.29 | 0.61 | 1.04 | ESTIMATE |
| F | 9.96 | 10.00 | 10.00 | ESTIMATE |
| C | 10.00 | 10.00 | 10.00 | ESTIMATE |
| D | 7.52 | 9.18 | 10.00 | ESTIMATE |

## Caveats
- a: OEWS is a four-digit automobile-dealer proxy and includes used-car dealers.
- a: Task exposure is inferred rather than directly measured, and commission-heavy roles make annual mean wages an imperfect labor-cost weight.
- a: Exposure denotes technically addressable work, not realized implementation or job elimination.
- rho: No representative source directly measures five-year implementation of the exposed opportunity.
- rho: Vendor capability may advance faster than dealership integration, governance, and OEM approval.
- rho: The estimate excludes pricing and demand effects.
- e: The frozen firm count is margin-bridged and may misclassify firms because vehicle retail has high revenue and thin margins.
- e: NADA reports rooftops and averages, whereas the screened unit is an eligible LMM firm and may own multiple rooftops.
- e: Service and parts revenue includes warranty, internal, wholesale, and counter activity, not only repeat customer-pay service.
- s5: A record activity year may not represent the next five years.
- s5: Franchises, rooftops, transactions, and firms are different counting units.
- s5: The public release does not distinguish all qualifying control transfers from portfolio reshuffling or internal reorganizations.
- q: No source directly observes contractual or competitive pass-through of AI savings.
- q: Capture differs sharply between competitively priced vehicle sales and less transparent service work.
- q: The estimate concerns retention of implemented gross benefit and does not include implementation difficulty or demand loss.
- d5: BLS employment is not service quantity and covers technicians across all employing industries.
- d5: EIA's long-horizon VMT growth is not specific to franchised dealers or the next five years.
- d5: Vehicle sales are cyclical, and the current basket mixes transactional sales with recurring service.
- o: The estimate treats an accountable local operator broadly and does not require every current front-office task to remain human.
- o: OEM distribution strategy and state franchise-law changes could shift the operator boundary quickly.
- o: EVs and remote diagnostics reduce some maintenance visits but do not remove collision, tire, warranty, delivery, and complex repair needs.

## Sources
- **S1** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 441100 Automobile Dealers](https://www.bls.gov/oes/2023/may/naics4_441100.htm) (accessed 2026-07-22): Reports 1,264,500 total workers and the detailed occupation mix, including 33.48% sales, 14.56% office and administrative support, 6.77% management, and 25.07% installation, maintenance, and repair employment.
- **S2** — [NADA Data 2025: Annual Financial Profile of America's Franchised New-Car Dealerships](https://www.nada.org/media/4695) (accessed 2026-07-22): Reports 16,990 franchised light-vehicle dealers, 16.2 million light-duty vehicle sales, more than 276 million repair orders, $164.6 billion of service and parts sales, a 13.3% service-and-parts share of sales, and 16,252 repair orders per average dealership.
- **S3** — [2025 NADA Dealership Workforce Study, 2024 Calendar Year Data: Sample Report](https://www.nadaworkforcestudy.com/files/2026-nada-sample-report.pdf) (accessed 2026-07-22): Reports 42% annualized turnover across dealership positions, including 66% for sales consultants and 43% for service advisors, illustrating hiring pressure and implementation/change-management conditions.
- **S4** — [NADA and Authenticom Introduce NADA Vault, Secure Dealership Data Syndication Platform](https://www.nada.org/nada/press-releases/nada-and-authenticom-introduce-nada-vault-secure-dealership-data-syndication) (accessed 2026-07-22): Describes fragmented dealership data-system connections and heightened customer-data controls following the FTC's 2023 Safeguards compliance rule, relevant to AI integration constraints.
- **S5** — [Dealership Buy/Sell Market Hits Record High in 2024 as US Auto Dealer Confidence Rose](https://www.businesswire.com/news/home/20250317569607/en/Dealership-BuySell-Market-Hits-Record-High-in-2024-as-US-Auto-Dealer-Confidence-Rose) (accessed 2026-07-22): Reports Kerrigan Advisors' count of 438 completed dealership transactions in 2024 and 697 franchises sold, with transactions up 10% from 2023.
- **S6** — [Occupational Outlook Handbook: Automotive Service Technicians and Mechanics](https://www.bls.gov/ooh/installation-maintenance-and-repair/automotive-service-technicians-and-mechanics.htm) (accessed 2026-07-22): Projects 4% employment growth from 2024 to 2034 and states that rising vehicle stock, older vehicles, and advanced safety-system repairs support demand while EVs limit some maintenance demand.
- **S7** — [U.S. Energy Information Administration Annual Energy Outlook 2026 Narrative](https://www.eia.gov/outlooks/aeo/narrative/index.php) (accessed 2026-07-22): Projects light-duty vehicle miles traveled to grow 8%-12% by 2050 versus 2025 and discusses the gradual turnover of the on-road vehicle stock.
