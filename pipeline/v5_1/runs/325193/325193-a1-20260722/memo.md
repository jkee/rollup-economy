# 325193 — Ethyl Alcohol Manufacturing

*v5.1 Stage 1 research memo. Run `325193-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 4.69 · L 0.08 · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Recurring physical processing and compliance work can support durable customer relationships where a genuine tolling model exists.
**Weakness:** Very few firms appear eligible, and the low labor intensity leaves AI improvements secondary to commodity spreads, utilization, and policy.

## Business-model lens
- Included: Independent lower-middle-market plants that repeatedly provide contract fermentation, distillation, purification, denaturing, recovery, or byproduct-processing capacity to external customers under customer specifications.
- Excluded: Plants producing and marketing only their own commodity fuel or industrial alcohol, farmer or corporate captive facilities, shell entities, non-control financing vehicles, and firms outside the normalized EBITDA band.
- Customer and revenue model: Customers purchase contracted processing campaigns or recurring volumes, with revenue based on throughput, finished gallons, conversion fees, or product prices that may include feedstock and energy adjustments.
- Deviation from default lens: Ethyl alcohol manufacturing is dominated by plants selling commodity output, while only a small subset plausibly provides recurring outsourced processing. The lens retains contract-processing operations so transferability and commercial retention describe a coherent service model.

## Executive view
The service lens captures at most a small fringe of ethyl alcohol manufacturing because the industry primarily sells commodity fuel or industrial alcohol. Eligible contract processors can have recurring throughput and specification work, but the provided firm population is already small and plant economics are dominated by feedstock, energy, policy, and utilization rather than labor.

## How AI changes the work
AI can improve production planning, yield and energy analysis, maintenance triage, laboratory review, compliance documentation, purchasing, and customer coordination. Physical operations and existing process controls limit direct substitution, and any new control recommendation must meet safety and quality requirements.

## Value capture
Contract duration and fee design determine capture. Yield, reliability, and faster release can support durable value, while transparent headcount or administrative savings are vulnerable to open-book review, rebidding, and commodity competition.

## Firm availability
Only a few independent plants are likely to earn material recurring conversion-fee revenue for third parties. Control transfers are further constrained by cooperatives, institutional ownership, permits, environmental obligations, capital intensity, and volatile commodity margins.

## Demand durability
Federal renewable-fuel standards support near-term volumes and ethanol remains widely blended into gasoline. Counterweights are the domestic blend wall, electric-vehicle adoption, gasoline demand, export reliance, excess capacity, and the ability of large commodity plants to absorb outsourced volume.

## Risks and uncertainty
A transaction can fail the lens if diligence reveals proprietary commodity sales rather than a true outsourced service. Other material risks are policy changes, RIN economics, corn and energy spreads, customer concentration, environmental liabilities, cyber risk, old plant controls, and limited commercial retention of visible savings.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.0246 | — | OBSERVED | — |
| n | — | 14 | — | ESTIMATE | — |
| a | 0.11 | 0.19 | 0.28 | PROXY | S1, S2 |
| rho | 0.28 | 0.43 | 0.6 | ESTIMATE | S5 |
| e | 0.02 | 0.07 | 0.15 | ESTIMATE | S4 |
| s5 | 0.06 | 0.13 | 0.23 | PROXY | S3 |
| q | 0.28 | 0.45 | 0.64 | ESTIMATE | S4 |
| d5 | 0.8 | 0.99 | 1.12 | PROXY | S4, S5, S6 |
| o | 0.89 | 0.96 | 0.99 | ESTIMATE | S2, S4 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.03 | 0.08 | 0.17 | ESTIMATE |
| F | 0.03 | 0.19 | 0.63 | ESTIMATE |
| C | 5.60 | 9.00 | 10.00 | ESTIMATE |
| D | 7.12 | 9.50 | 10.00 | ESTIMATE |

## Caveats
- a: The occupation mix is for NAICS 325, not 325193 or the eligible contract-processing subset.
- a: ILO exposure describes technical potential rather than observed substitution.
- a: The industry's low provided compensation-to-receipts ratio means small task-share errors should not be interpreted as large operating-value changes.
- rho: No source measures AI implementation rates for lower-middle-market ethanol contract processors.
- rho: Legacy controls and sparse labeled failure data may make predictive tools slower to validate.
- e: The dataset firm count is a margin-bridged estimate and may include cooperatives, integrated plants, or entities without transferable contract-service operations.
- e: Public sources rarely disclose whether third-party processing is material revenue rather than incidental spare-capacity use.
- s5: The Census owner-age data are cross-industry, based on 2018, and represent responding owners rather than firms.
- s5: Cooperatives and institutionally owned plants do not follow the same owner-retirement pathway.
- q: No public contract sample establishes the commercial sharing of AI benefits for the eligible population.
- q: Excess capacity and low-price competition can cause savings to pass rapidly to customers.
- d5: Renewable-fuel requirements are measured in RINs and are not a direct mandate for output from NAICS 325193 contract processors.
- d5: The result is highly sensitive to policy, gasoline consumption, exports, and the customer's ability to switch plants.
- o: The estimate does not protect current demand from electrification, alternative fuels, or policy changes, which belong in d5.
- o: Operator requirement may persist while the work shifts to a different, larger supplier.

## Sources
- **S1** — [Chemical Manufacturing: NAICS 325](https://www.bls.gov/iag/tgs/iag325.htm) (accessed 2026-07-22): BLS reports 2025 chemical-manufacturing employment of 124,330 chemical equipment operators, 17,600 chemical technicians, 27,530 chemists, 25,810 mixing and blending operators, and 57,400 packaging and filling operators.
- **S2** — [Generative AI and Jobs: Policies to Manage the Transition](https://www.ilo.org/sites/default/files/2024-08/GenAI%20and%20Jobs_Policy%20Brief_ILO.pdf) (accessed 2026-07-22): ILO reports 24% of clerical tasks at high automation exposure and 58% at medium exposure, while other occupational groups have 1% to 4% highly exposed and no more than 25% medium-exposed tasks.
- **S3** — [Business Owners' Ages](https://www.census.gov/content/dam/Census/library/visualizations/2020/comm/business-owners-ages.pdf) (accessed 2026-07-22): Census reports that 51% of responding owners of employer businesses were age 55 or older, based on the 2019 Annual Business Survey for data year 2018.
- **S4** — [Ethanol Explained: Supply of Ethanol](https://www.eia.gov/energyexplained/biofuels/ethanol-supply.php) (accessed 2026-07-22): EIA reports 17.7 billion gallons of U.S. fuel-ethanol capacity at the end of 2022, 15.4 billion gallons of 2022 production, production exceeding domestic blending consumption by 1.3 billion gallons, and exports of about 1.3 billion gallons.
- **S5** — [Final Renewable Fuel Standards for 2026 and 2027](https://www.epa.gov/renewable-fuel-standard/final-renewable-fuel-standards-2026-and-2027) (accessed 2026-07-22): EPA states that the March 27, 2026 final rule sets renewable-fuel requirements for 2026 and 2027; the page lists total applicable renewable-fuel volumes of 26.81 and 27.02 billion RINs, respectively.
- **S6** — [Ethanol Explained: Use of Ethanol](https://www.eia.gov/energyexplained/biofuels/ethanol-use.php) (accessed 2026-07-22): EIA explains that ethanol's gasoline share has exceeded 10% since 2017 and describes the blend wall, E15 vehicle eligibility, and the restriction of higher blends such as E85 to flexible-fuel vehicles.
