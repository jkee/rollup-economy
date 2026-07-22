# 561740 — Carpet and Upholstery Cleaning Services

*v5.1 Stage 1 research memo. Run `561740-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 5.81 · L 1.21 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Fixed-price physical jobs leave a small but implementable back-office efficiency layer that can be retained when systems reduce coordination labor or avoided hiring.
**Weakness:** Most wages fund on-site manual execution that current AI cannot substitute, and the estimated LMM acquisition pool is very small.

## Business-model lens
- Included: US lower-middle-market firms repeatedly providing outsourced cleaning, spotting, dyeing, maintenance, and related care for used carpets, rugs, and upholstery at residential, commercial, institutional, or plant locations.
- Excluded: Captive in-house cleaning departments, self-service equipment rental, janitorial firms without substantive carpet or upholstery work, new-product manufacturing or installation, repair-only operations, one-person practices without a transferable operating organization, shells, and non-control financing vehicles.
- Customer and revenue model: External households and organizations buy on-site or plant-based cleaning through per-room, per-square-foot, hourly, quoted-project, or scheduled maintenance pricing. Residential demand is commonly episodic but repeatable; commercial and institutional accounts can be scheduled under recurring maintenance plans or service agreements.
- Deviation from default lens: none

## Executive view
Carpet and upholstery cleaning is a labor-intensive physical service with only a modest digitally automatable layer. AI can streamline customer intake, quoting support, reminders, routing, marketing, documentation, and routine administration, but technicians must still travel to sites, handle equipment and chemicals, treat variable surfaces, and verify results. Demand is comparatively durable because physical assets repeatedly soil, although household work is deferrable and commercial customers can bundle scopes or rebid aggressively.

## How AI changes the work
The most practical uses are automated call and message handling, lead qualification, appointment reminders, route suggestions, draft estimates from structured inputs, review responses, campaign content, job-note summarization, purchasing alerts, and analysis of customer history. Human review remains important for promises, stain diagnosis, material compatibility, pricing exceptions, and customer disputes. Physical extraction, spotting, setup, furniture movement, equipment maintenance, and final inspection remain field work.

## Value capture
Per-room, per-square-foot, and fixed quoted-job pricing can preserve back-office efficiency inside the job price, while recurring commercial plans can spread dispatch and sales costs over predictable work. Capture is weaker for hourly jobs and at renewal because customers can compare local providers, negotiate recurring discounts, or demand faster service. Savings matter only when a firm actually reduces office labor, avoids hiring, or turns freed capacity into more completed jobs.

## Firm availability
LMM firms should be more transferable than the industry's many owner-operators because scale generally requires crews, equipment, service systems, lead channels, and commercial or repeat accounts. Even so, the supplied population is only 31 estimated firms, and eligibility may shrink when founder field work, concentrated local relationships, nonrepeat restoration revenue, or classification error is examined.

## Demand durability
Carpets, rugs, and upholstered assets repeatedly accumulate soil, stains, allergens, and wear, supporting maintenance and restorative cleaning. Broader cleaning employment is projected to grow slowly rather than contract, but residential customers can defer service, commercial occupancy can shift, and hard-floor substitution can erode the addressable base. Most surviving demand still requires accountable physical execution at the customer's property or a cleaning plant.

## Risks and uncertainty
There is no public six-digit task mix, contract mix, AI deployment study, ownership-transfer series, or constant-price demand series for the screened population. The main operating risks are technician recruiting and retention, vehicle and equipment utilization, chemical or surface damage, inconsistent quality, lead-platform dependence, local competition, customer concentration, and owner dependence. The firm-count anchor is margin-bridged, so a small number of classification or normalization errors can materially change the apparent acquisition pool.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.4017 | — | OBSERVED | — |
| n | — | 31 | — | ESTIMATE | — |
| a | 0.08 | 0.15 | 0.24 | PROXY | S1, S2, S3 |
| rho | 0.3 | 0.5 | 0.68 | PROXY | S3, S4 |
| e | 0.62 | 0.78 | 0.9 | ESTIMATE | S1, S6, S7 |
| s5 | 0.08 | 0.16 | 0.27 | PROXY | S5 |
| q | 0.34 | 0.54 | 0.72 | PROXY | S6, S7 |
| d5 | 0.92 | 1.02 | 1.12 | PROXY | S1, S2, S6, S7 |
| o | 0.84 | 0.93 | 0.98 | PROXY | S1, S2, S6 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.39 | 1.21 | 2.62 | PROXY |
| F | 1.50 | 2.55 | 3.45 | ESTIMATE |
| C | 6.80 | 10.00 | 10.00 | PROXY |
| D | 7.73 | 9.49 | 10.00 | PROXY |

## Caveats
- a: No public source reports a six-digit occupation mix or wage-weighted task distribution for NAICS 561740.
- a: The BLS occupation is broader than carpet and upholstery cleaning and includes duties outside the industry definition.
- a: The supplied compensation ratio has a 2024-wage and 2022-receipts vintage mismatch.
- rho: General SME adoption is not implementation intensity in NAICS 561740.
- rho: Use of AI for marketing or messages does not necessarily reduce payroll or avoid hiring.
- rho: Small operators may lack consistent customer, route, and job-history data needed for deeper automation.
- e: No source measures lens eligibility among firms in the frozen EBITDA band.
- e: Residential customers may repeat only every several years and are not contractually recurring.
- e: The supplied firm count is margin-bridged and small, making eligibility sensitive to classification and normalization error.
- s5: Gallup covers all employer businesses rather than this industry or EBITDA band.
- s5: Owner intentions are not completed transactions and include transfers that may not qualify.
- s5: Local reputation, lead channels, and technician retention may deteriorate when an owner exits.
- q: No source measures the national revenue mix by pricing model for NAICS 561740.
- q: Published pricing guides are advisory and not realized transaction data.
- q: Administrative time savings create value only if owners reduce paid hours, avoid hiring, or redeploy capacity productively.
- d5: Occupational employment is not industry output and includes many non-carpet cleaning activities.
- d5: No source quantifies the installed carpet and upholstery base or cleaning frequency nationally.
- d5: Residential cleaning can be deferred, while commercial demand varies with occupancy and flooring substitution.
- o: No source measures operator-required quantity directly for this industry.
- o: Commercial facilities may bundle carpet work into broader janitorial contracts rather than use a specialist.
- o: Advances in autonomous floor equipment or stain-resistant materials could reduce operator need faster than assumed.

## Sources
- **S1** — [2022 NAICS 561740 Carpet and Upholstery Cleaning Services](https://www.census.gov/naics/?details=56174&input=56174&year=2022) (accessed 2026-07-22): Defines the industry as establishments primarily engaged in cleaning and dyeing used rugs, carpets, and upholstery.
- **S2** — [Janitors and Building Cleaners](https://www.bls.gov/OOH/building-and-grounds-cleaning/janitors-and-building-cleaners.htm) (accessed 2026-07-22): Describes physical cleaning duties and equipment, physical stamina requirements, 2 percent projected employment growth from 2024 to 2034, continued demand for clean and healthy spaces, and employment restraint from high-tech cleaning methods.
- **S3** — [AI for Small Business](https://www.sba.gov/business-guide/manage-your-business/ai-small-business) (accessed 2026-07-22): Identifies practical small-business AI uses in repeat administration, data analysis, content, customer service, phone routing, and review responses, while advising firms to start small and apply human review and data safeguards.
- **S4** — [AI Adoption by Small and Medium-Sized Enterprises](https://www.oecd.org/content/dam/oecd/en/publications/reports/2025/12/ai-adoption-by-small-and-medium-sized-enterprises_9c48eae6/426399c1-en.pdf) (accessed 2026-07-22): Reports lower AI adoption among SMEs, including 11.9 percent of 10-49 employee firms in 2024, below-10-percent core-business adoption in G7 countries, and predominantly peripheral generative-AI use among SMEs.
- **S5** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Reports that 22 percent of US employer-business owners planned to sell, transfer, or go public within five years and 5 percent planned to close.
- **S6** — [Carpet Cleaning Price Guide 2026](https://www.housecallpro.com/resources/carpet-cleaning-prices/) (accessed 2026-07-22): Describes per-room and per-square-foot residential pricing, square-foot or hourly commercial pricing, regularly scheduled commercial jobs, add-ons, tiered service, and recurring-plan discounts.
- **S7** — [Commercial Cleaning Rates per Square Foot](https://www.issa.com/articles/commercial-cleaning-rates-per-square-foot/) (accessed 2026-07-22): Describes square-foot pricing for commercial cleaning, labor and frequency as price drivers, carpet cleaning as a separately priced specialty service, and annual maintenance-plan inclusion.
