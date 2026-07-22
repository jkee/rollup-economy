# 531210 — Offices of Real Estate Agents and Brokers

*v5 Stage 1 research memo. Run `531210-a1-20260722`, model `gpt-5.6-terra`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 6.30 · L 1.02 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** AI is already entering agent workflows while substantial administrative, marketing, and coordination work remains adjacent to the licensed relationship role.
**Weakness:** Brokerage value can be embedded in individual agents and is vulnerable to transaction cycles, fee negotiation, and self-service alternatives.

## Business-model lens
- Included: Independent and franchised brokerage firms providing residential, commercial, or rental representation, listing, marketing, transaction coordination, and negotiation to external customers.
- Excluded: Captive in-house sales units of developers or owners, listing platforms and lead-generation businesses that do not provide brokerage representation, property managers, title and settlement businesses, and passive referral shells.
- Customer and revenue model: Repeat or episodic outsourced representation for buyers, sellers, landlords, and tenants, normally paid through negotiated transaction, lease, or referral commissions rather than cost-plus billing.
- Deviation from default lens: none

## Executive view
This is a fragmented, owner-led brokerage population with repeat external-client work and visible AI adoption, but its core economics are exposed to cyclic transaction demand, agent-centric delivery, and transparent negotiated fees.

## How AI changes the work
AI can compress listing content, lead response, property research, document handling, CRM, and marketing operations. It is less able to replace showings, relationship formation, negotiation, local judgment, and licensed responsibility; implementation also requires controls for quality, privacy, and fair-housing obligations.

## Value capture
Transaction commissions are not cost-plus, so a well-run firm can retain part of operational savings. However, broker fees are negotiable, buyer agreements now state compensation explicitly, agents often capture economics through splits, and both franchises and small offices compete for clients and agents.

## Firm availability
NAR's firm profile depicts mostly independent, single-office, broker-owner firms with long operating histories. That creates a plausible succession pool, but the available evidence does not measure qualifying LMM control transfers and many retirements may end in closure, referral-only status, or agent departure rather than a sale.

## Demand durability
Customers still widely use agents for high-stakes home transactions, and BLS expects modest long-run occupation growth. Demand remains highly sensitive to rates and the economic cycle, while search, content, and routine coordination are vulnerable to self-service and software substitution.

## Risks and uncertainty
The labor input may miss self-employed agent compensation, and the cited surveys cover REALTOR members or residential consumers rather than the exact LMM NAICS population. There is no direct evidence for task-level savings, qualifying transfer frequency, retained AI benefit, or constant-quality service demand; those require operator diligence and transaction data.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1826 | — | OBSERVED | — |
| n | — | 259 | — | ESTIMATE | — |
| a | 0.2 | 0.35 | 0.5 | PROXY | S1, S2 |
| rho | 0.25 | 0.4 | 0.58 | PROXY | S2, S3 |
| e | 0.7 | 0.85 | 0.95 | PROXY | S3 |
| s5 | 0.08 | 0.14 | 0.22 | ESTIMATE | S3 |
| q | 0.35 | 0.5 | 0.65 | ESTIMATE | S3, S5 |
| d5 | 0.92 | 1.015 | 1.08 | PROXY | S1 |
| o | 0.75 | 0.85 | 0.93 | PROXY | S1, S4 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.37 | 1.02 | 2.12 | PROXY |
| F | 4.41 | 5.57 | 6.45 | ESTIMATE |
| C | 7.00 | 10.00 | 10.00 | ESTIMATE |
| D | 6.90 | 8.63 | 10.00 | PROXY |

## Caveats
- a: REALTOR membership is not identical to all NAICS 531210 firms.
- a: The provided wage-based labor input does not directly observe owner-agent commissions or self-employed labor.
- rho: The technology survey is self-reported and membership-based.
- rho: Firm software provision does not establish that agents use the tools consistently or that a workflow is compliant.
- e: Office count and commission volume are not EBITDA.
- e: The NAR firm survey may not represent nonmember brokerages or all NAICS establishments.
- s5: Firm age is not owner age or sale intent.
- s5: No source located measures five-year control-transfer probability for LMM brokerages, and closures are excluded from the construct.
- q: The sources establish negotiability and market structure, not the retained share of AI benefit.
- q: Commission arrangements vary materially by local market, franchise contract, residential versus commercial work, and agent split.
- d5: Occupation projections span work outside NAICS 531210 and do not equal service quantity.
- d5: Constant-quality demand is especially difficult to separate from home-price movements and commission-rate changes.
- o: The consumer survey is residential and recent-transaction based, whereas this NAICS includes commercial and rental brokerage.
- o: Use of an agent today can reflect norms and financing practices as well as irreplaceable operator need.

## Sources
- **S1** — [Real Estate Brokers and Sales Agents: Occupational Outlook Handbook](https://www.bls.gov/ooh/sales/real-estate-brokers-and-sales-agents.htm?Tag=ALS) (accessed 2026-07-22): Documents duties, self-employment share, customer-facing work, and the 2024–2034 employment projection for brokers and sales agents.
- **S2** — [REALTORS Embrace AI, Digital Tools to Enhance Client Service, NAR Survey Finds](https://www.nar.realtor/press-releases/realtors-embrace-ai-digital-tools-to-enhance-client-service-nar-survey-finds) (accessed 2026-07-22): Reports REALTOR AI-use frequency, AI-generated-content use, perceived business impact, client response, and brokerage technology support.
- **S3** — [2025 Profile of Real Estate Firms](https://cms.nar.realtor/sites/default/files/2025-11/2025-profile-of-real-estate-firms-11-19-2025.pdf) (accessed 2026-07-22): Reports firm independence, office count, broker-owner status, years in business, competition, revenue sources, and software provision among real estate firms.
- **S4** — [Top 10 Takeaways from NAR's 2025 Profile of Home Buyers and Sellers](https://www.nar.realtor/news/economists-outlook/top-10-takeaways-from-nars-2025-profile-of-home-buyers-and-sellers) (accessed 2026-07-22): Reports recent buyer and seller use of agents or brokers and the services buyers and sellers value.
- **S5** — [What the NAR Settlement Means for Home Buyers and Sellers](https://www.nar.realtor/the-facts/what-the-nar-settlement-means-for-home-buyers-and-sellers) (accessed 2026-07-22): Documents the post-settlement written buyer agreement requirements, compensation disclosure, prohibition on MLS compensation offers, and negotiability of agent compensation.
