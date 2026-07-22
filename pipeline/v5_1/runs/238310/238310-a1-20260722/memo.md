# 238310 — Drywall and Insulation Contractors

*v5.1 Stage 1 research memo. Run `238310-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 6.51 · L 0.91 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Durable, operator-required physical demand paired with meaningful estimator, project-control, and administrative labor that AI can compress.
**Weakness:** Most labor is hands-on field work, while transferable-firm supply and five-year control-transfer probability lack NAICS-specific observed denominators.

## Business-model lens
- Included: US lower-middle-market contractors installing, replacing, and finishing drywall, ceiling tile, plaster, building insulation, mechanical insulation, and closely related firestopping for external general contractors, property owners, and facility customers on recurring or repeat outsourced engagements.
- Excluded: Shells, captive internal construction units, non-control financing vehicles, materials-only distributors or manufacturers, firms outside the roughly $1-10M normalized EBITDA band, and operations whose customer relationships, licenses, workforce, or systems cannot transfer independently of the owner.
- Customer and revenue model: Primarily project-based subcontract revenue from competitively bid or negotiated scopes, commonly fixed-price with change orders and occasional price-sharing or escalation clauses; repeat revenue comes from recurring general-contractor and owner relationships rather than subscription contracts.
- Deviation from default lens: none

## Executive view
Drywall and insulation contracting offers a real but bounded AI labor opportunity concentrated in estimating, project administration, field coordination, and back-office workflows. The physical installation core remains operator- and crew-dependent, which supports service durability but caps substitutable wage share. The main underwriting uncertainty is not whether the service persists; it is whether enough owner-dependent firms transfer cleanly and whether productivity gains remain with the contractor after repeated bidding cycles.

## How AI changes the work
AI can assist plan and specification review, quantity takeoff, scope-gap detection, estimate drafting, bid comparison, crew and delivery scheduling, RFI and submittal preparation, daily reports, safety paperwork, time capture, invoicing, and collections. It is far less able to replace the dexterous, variable-site work of measuring, cutting, lifting, fastening, taping, smoothing, spraying, firestopping, and correcting defects. Five-year implementation therefore looks like fewer administrative hours and avoided estimator or coordinator hiring, with selective field augmentation rather than autonomous installation.

## Value capture
Savings on already-awarded fixed-price work may initially accrue to the contractor, and faster, more accurate estimating can protect margin or increase bid capacity. Over time, hard bidding, GC purchasing power, customer negotiation, and competitor adoption should share much of the benefit through lower prices or more service for the same price. Differentiated execution, lower rework, better change-order recovery, and reliable scheduling are likelier to retain value than a generic reduction in clerical effort.

## Firm availability
The trade is populated by external contractors with crews and repeat GC or owner relationships, so many LMM firms should be structurally transferable. Yet licensing, customer ties, estimating knowledge, and production supervision often sit with the founder. Broad owner surveys and construction marketplace activity indicate a supply of potential transfers, but neither gives a drywall-specific five-year rate or a clean denominator for eligible LMM firms.

## Demand durability
Drywall follows new construction, tenant improvements, renovation, and repair; insulation adds retrofit, energy-efficiency, mechanical-system, and fire-protection demand. BLS projects 4% decade growth for both relevant occupational groups, consistent with roughly stable to modestly growing five-year quantity. The work remains physical, local, code- and quality-sensitive, leaving an accountable contractor necessary even as software changes planning and administration.

## Risks and uncertainty
Construction cyclicality, interest rates, tariffs, immigration enforcement, project postponements, customer concentration, safety incidents, defect claims, and thin hard-bid margins can overwhelm modest AI savings. The dataset compensation ratio is low quality and measured at ancestor NAICS 23831 with a 2024-wage/2022-receipts vintage mismatch; the provided LMM firm count is an estimate. Research evidence is also broader than this six-digit industry, especially for transfers, pricing, and technology adoption.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.3171 | — | ESTIMATE | — |
| n | — | 337 | — | ESTIMATE | — |
| a | 0.09 | 0.15 | 0.23 | ESTIMATE | S1, S2, S3, S4 |
| rho | 0.3 | 0.48 | 0.68 | ESTIMATE | S4, S5 |
| e | 0.6 | 0.78 | 0.9 | ESTIMATE | S7, S10 |
| s5 | 0.1 | 0.17 | 0.27 | PROXY | S6, S7 |
| q | 0.28 | 0.45 | 0.62 | ESTIMATE | S5, S7 |
| d5 | 0.94 | 1.02 | 1.1 | PROXY | S8, S9 |
| o | 0.94 | 0.98 | 1 | ESTIMATE | S2, S4, S8, S9 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.34 | 0.91 | 1.98 | ESTIMATE |
| F | 4.91 | 6.15 | 7.11 | ESTIMATE |
| C | 5.60 | 9.00 | 10.00 | ESTIMATE |
| D | 8.84 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: OEWS excludes self-employed workers and covers employers of all sizes, not only the lower-middle-market lens.
- a: The occupation-to-task allocation and wage weighting are researcher judgments because no source measures not-yet-automated AI-exposed wage share for NAICS 238310.
- a: Anthropic usage data describe observed Claude use and may understate future multimodal, vision, and integrated-workflow capability while overstating adoption among digitally advanced users.
- rho: AGC respondents span construction segments and sizes; 43% reported revenue above $50 million, making the survey more digitally capable than the target lens may be.
- rho: Survey expectations about AI are not observed implementation or realized labor substitution.
- rho: Implementation may augment scarce estimators and supervisors without reducing payroll, although avoided hiring remains in scope.
- e: No source reports the eligible share specifically for NAICS 238310 firms in the specified EBITDA band.
- e: BizBuySell's transacted construction businesses are selected for marketability and are generally smaller than the target EBITDA band.
- e: Licensing and qualifier requirements vary by state and can make owner separation difficult.
- s5: The 64.5% intention statistic is broad, dated, and does not specify timing or whether a sale ultimately closes.
- s5: BizBuySell covers reported platform transactions, broad construction categories, and mostly Main Street firms rather than the target EBITDA band.
- s5: No denominator exists for converting the reported construction sales count into an observed annual transfer rate.
- q: The tariff pricing responses are an analogy for contractual pass-through, not direct evidence on sharing AI savings.
- q: Contract mix varies by residential versus commercial work, negotiated versus hard-bid procurement, union status, and local competition.
- q: BizBuySell financials are self- or broker-reported for sold broad-construction firms and do not isolate gross-benefit retention.
- d5: Occupational employment is not service quantity and incorporates productivity, labor supply, and occupation shares.
- d5: BLS projections cover ten years and broader occupational employment, not the five-year NAICS lens.
- d5: The frozen lens combines cyclical new-construction drywall with retrofit-oriented and energy-efficiency insulation demand.
- o: The estimate concerns continued need for an accountable contractor, not the number of labor hours inside that contractor.
- o: Advances in robotics and prefabrication could reduce field labor faster than current usage evidence suggests while still leaving operator accountability intact.
- o: Self-service is more plausible for small residential repairs than for code-, safety-, fire-, acoustic-, or warranty-sensitive commercial scopes.

## Sources
- **S1** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 238310](https://www.bls.gov/oes/2023/may/naics5_238310.htm) (accessed 2026-07-22): Industry occupation mix and wages: 245,810 total jobs; 81.69% construction and extraction, 7.74% first-line construction supervisors, 5.73% office support, 4.51% business and financial operations, 4.48% management, 2.26% cost estimators, and 1.28% project management specialists.
- **S2** — [O*NET OnLine: Drywall and Ceiling Tile Installers](https://www.onetonline.org/link/summary/47-2081.00) (accessed 2026-07-22): Core tasks include reading blueprints, measuring and marking surfaces, fitting and fastening drywall, cutting openings and framing, verifying alignment, coordinating project activities, and applying fill material.
- **S3** — [O*NET OnLine: Cost Estimators](https://www.onetonline.org/link/summary/13-1051.00) (accessed 2026-07-22): Cost estimators analyze blueprints and documentation to prepare labor, materials, time, and cost estimates and confer with project parties on changes—digitally tractable tasks present in the industry mix.
- **S4** — [Which Economic Tasks are Performed with AI? Evidence from Millions of Claude Conversations](https://assets.anthropic.com/m/2e23255f1e84ca97/original/Economic_Tasks_AI_Paper.p/) (accessed 2026-07-22): Observed Claude usage was highest in software, writing, and analytical work but minimal for occupations involving physical manipulation such as construction; physical installation and equipment-maintenance skills also had minimal presence.
- **S5** — [2025 Workforce Survey Analysis](https://www.agc.org/sites/default/files/users/user21902/2025%20Workforce%20Survey%20Analysis%20%283%29.pdf) (accessed 2026-07-22): Among 1,342 broad construction respondents, 83% of firms employing craft workers had openings; estimating personnel and project managers/supervisors were hard to fill for 77% and 76% of firms seeking them; 45% expected AI/robotics to automate error-prone tasks and 44% expected safer or more productive jobs. Also, 41% raised bid prices and 23% added price-sharing or other contract terms in response to tariffs.
- **S6** — [Small Business Facts: Paths to Business Ownership](https://advocacy.sba.gov/wp-content/uploads/2021/03/Paths-to-Business-Ownership-fact-sheet.pdf) (accessed 2026-07-22): SBA summarizes Census data showing 64.5% of current owners planned to sell, while 12% of construction owners had purchased their business; these are broad, non-timed transfer proxies.
- **S7** — [Construction Business Valuation Multiples and Financial Benchmarks](https://www.bizbuysell.com/learning-center/valuation-benchmarks/building-construction/) (accessed 2026-07-22): BizBuySell reports 3,142 broad building and construction businesses sold over 2021-2025, a $1.51 million median revenue, $323,174 median owner earnings, 207 median days on market, and notes that low owner involvement and consistent performance support higher transfer values.
- **S8** — [Occupational Outlook Handbook: Drywall Installers, Ceiling Tile Installers, and Tapers](https://www.bls.gov/ooh/construction-and-extraction/drywall-and-ceiling-tile-installers-and-tapers.htm) (accessed 2026-07-22): BLS projects 4% employment growth from 2024 to 2034 and describes physical installation, finishing, repair, lifting, bending, and reaching requirements.
- **S9** — [Occupational Outlook Handbook: Insulation Workers](https://www.bls.gov/ooh/construction-and-extraction/insulation-workers.htm) (accessed 2026-07-22): BLS projects 4% overall insulation-worker growth from 2024 to 2034, with energy efficiency supporting mechanical-insulation demand and new home building and retrofits linked to floor, ceiling, and wall insulation employment.
- **S10** — [North American Industry Classification System: 238310 Drywall and Insulation Contractors](https://www.census.gov/naics/?details=238310&input=238310&year=2012) (accessed 2026-07-22): Defines the industry as establishments primarily engaged in drywall, plaster work, and building insulation work.
