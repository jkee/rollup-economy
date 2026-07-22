# 331318 — Other Aluminum Rolling, Drawing, and Extruding

*v5.1 Stage 1 research memo. Run `331318-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.69 · L 0.87 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Customer-specific dies and repeat programs create switching friction while AI-enabled inspection and uptime improvements expand profitable press throughput.
**Weakness:** A large standard-profile and construction-exposed segment remains cyclical, price-sensitive, and vulnerable to imported finished products.

## Business-model lens
- Included: Independent lower-middle-market manufacturers that extrude, draw, or roll non-flat aluminum shapes, rod, bar, wire, or tube, emphasizing custom profiles, customer-specific dies, repeat production programs, and associated fabrication or finishing tied to the extruded product.
- Excluded: Primary smelting; flat sheet, plate, and foil mills; secondary alloy smelting without extrusion or drawing; distributors and fabricators that do not perform substantive extrusion, drawing, or shape rolling; captive divisions of large integrated groups; and commodity-only sellers lacking repeat customer programs.
- Customer and revenue model: Customers are construction-system suppliers, industrial OEMs, electrical and renewable-energy equipment makers, transportation suppliers, durable-goods makers, and service centers. Revenue usually combines purchased metal passed through in product price with a conversion margin; proprietary dies, qualification, engineering support, blanket orders, and scheduled releases create recurring custom-program economics.
- Deviation from default lens: none

## Executive view
Custom aluminum extrusion is more compatible with the recurring-service lens than commodity aluminum rolling. Proprietary profiles, dies, qualification, scheduled releases, and fabrication create repeat programs, while AI vision, scheduling, and maintenance can raise yield and press availability. The thesis is strongest in diversified niche extruders and weakest in standard construction profiles exposed to commodity pricing and imports.

## How AI changes the work
Computer vision has already been used to detect speed and hot tears across varied profiles, and industry offerings extend to full-surface inspection, inline metrology, press optimization, die management, predictive maintenance, and automated handling. Human work remains essential for setup, die changes, handling, testing, repairs, finishing, and complex quality decisions.

## Value capture
Metal is commonly purchased under market-linked arrangements, so customers can separate metal from conversion economics. Custom dies, engineering support, qualification, and integrated fabrication increase switching cost, allowing an efficient extruder to retain more value from yield, uptime, defect prevention, and delivery reliability than from simple material-price savings.

## Firm availability
The estimated LMM pool of 64 firms is useful but heterogeneous. Regional owner-managed extruders may face succession, yet acquisition diligence must test customer concentration, die ownership, backlog quality, press and furnace condition, environmental exposure, power and gas availability, labor, fabrication mix, and vulnerability to imported finished goods.

## Demand durability
The application base is diverse, but current demand is not uniformly strong: North American extrusion demand fell in 2025, construction remains cyclical, and tariff changes have not reliably shifted orders to domestic producers. Electrical, renewable energy, transportation, automation, and specialized industrial profiles provide plausible growth offsets.

## Risks and uncertainty
The largest uncertainties are the true share of custom recurring programs, durability of conversion margins, construction cyclicality, tariff inversion, imported fabricated products, extrusion-capacity utilization, customer concentration, legacy equipment, and whether small operators can realize vendor-promoted AI benefits with limited data and engineering resources.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1236 | — | OBSERVED | — |
| n | — | 64 | — | ESTIMATE | — |
| a | 0.22 | 0.35 | 0.48 | PROXY | S1, S2, S3, S4 |
| rho | 0.3 | 0.5 | 0.68 | ESTIMATE | S3, S4 |
| e | 0.24 | 0.42 | 0.6 | PROXY | S5, S6, S7 |
| s5 | 0.09 | 0.16 | 0.25 | PROXY | S8 |
| q | 0.3 | 0.46 | 0.62 | PROXY | S5, S6, S9 |
| d5 | 0.95 | 1.08 | 1.23 | PROXY | S5, S9, S10 |
| o | 0.95 | 0.99 | 1 | ESTIMATE | S1, S2, S3, S6 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.33 | 0.87 | 1.61 | ESTIMATE |
| F | 1.40 | 2.68 | 3.80 | ESTIMATE |
| C | 6.00 | 9.20 | 10.00 | PROXY |
| D | 9.03 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: O*NET covers metal and plastic extrusion and drawing.
- a: Vendor and conference evidence may emphasize successful deployments.
- a: The NAICS category also includes drawing and shape rolling, not only extrusion.
- rho: No industry-wide AI adoption study was found.
- rho: Inspection software is easier to retrofit than closed-loop press or handling automation.
- rho: Benefits depend on stable data and disciplined process control.
- e: Company websites do not disclose revenue shares or margins.
- e: Recurring product programs are less service-like than customer-owned-metal tolling.
- e: Some advertised fabrication activity may be classified outside this NAICS.
- s5: Cross-industry intentions are not observed extrusion transactions.
- s5: Stated plans may not lead to marketable companies.
- s5: Strategic buyers may absorb the best assets before broad marketing.
- q: Capture varies strongly between custom OEM and standard construction profiles.
- q: Customer-owned dies can facilitate switching after qualification.
- q: Temporary tariff protection or shortages can inflate apparent pricing power.
- d5: Broad product demand does not equal recurring-program demand.
- d5: Construction concentration makes outcomes sensitive to rates and commercial building activity.
- d5: Tariff inversions may shift demand to imported finished goods rather than domestic extrusions.
- o: The factor addresses AI-related obsolescence rather than ordinary share loss.
- o: Individual legacy presses can become uneconomic even when extrusion remains necessary.
- o: Imported finished products can bypass domestic extrusion without changing the underlying technology.

## Sources
- **S1** — [NAICS 331318 - Other Aluminum Rolling, Drawing, and Extruding](https://www.naics.com/%20naics-code-description/?code=331318&v=2022) (accessed 2026-07-22): Industry boundary covering non-flat aluminum shapes made by rolling, drawing, or extruding purchased aluminum or integrated scrap recovery.
- **S2** — [Extruding and Drawing Machine Setters, Operators, and Tenders, Metal and Plastic](https://www.onetonline.org/link/summary/51-4021.00) (accessed 2026-07-22): Core tasks: setup, die changes, controls, inspection, testing, troubleshooting, material handling, cutting, and inventory.
- **S3** — [Automated Speed Tear Detection in Aluminum Extrusion](https://www.matroid.com/case-studies/computer-vision-speed-tear-detection/) (accessed 2026-07-22): Aluminum-specific deployment of AI vision for defect detection, real-time alerts, reduced manual inspection, waste prevention, and operator redeployment.
- **S4** — [Aluminum Extruders Council Extrusion Equipment and Technology](https://aec.org/extrusion-equipment) (accessed 2026-07-22): Industry evidence for AI surface inspection, inline dimensional measurement, automated handling, press optimization, and retrofit pathways.
- **S5** — [Custom Aluminum Extrusions](https://www.industrialmetalsupply.com/services/custom-extrusions) (accessed 2026-07-22): Custom and library dies, engineering guidance, repeat-order metal contracts, price stabilization, inventory storage, and scheduled deliveries.
- **S6** — [Bristol Aluminum Custom Extrusions](https://bristolaluminum.com/) (accessed 2026-07-22): Regional independent extruder example with custom design, standard dies, fabrication, finishing, close specifications, and repeatable precision machining.
- **S7** — [Alexandria Industries Extrusion Die Tooling](https://www.alexandriaindustries.com/capabilities/services/tooling/) (accessed 2026-07-22): Customer-specific die correction, maintenance, measurement, capability studies, and close-tolerance extrusion support.
- **S8** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Cross-industry evidence on aging owners and five-year intentions to sell, transfer, close, or retain small businesses.
- **S9** — [Tredegar Corporation 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/850429/000162828026016665/tg-20251231.htm) (accessed 2026-07-22): Extrusion end-market mix, order levels, purchased-metal inputs, volume, cyclicality, imports, tariff effects, yield, productivity, maintenance, die, utility, and environmental risks.
- **S10** — [North American Aluminum Demand Steady in 2025](https://www.aluminum.org/news/north-american-aluminum-demand-steady-2025) (accessed 2026-07-22): Current North American aluminum demand totals and the 3.1% decline in extruded-product demand during 2025.
