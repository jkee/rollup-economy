# 561621 — Security Systems Services (except Locksmiths)

*v5.1 Stage 1 research memo. Run `561621-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** CONDITIONAL · A 7.48 · L 3.67 · interval LOW_PRIORITY → HIGHEST_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Recurring monitoring and maintenance relationships create a channel to retain value from automating high-volume event handling and coordination work.
**Weakness:** Nearly half of employment is in installation, maintenance, and repair, while DIY and self-monitoring can displace the operator from the easiest customer segments.

## Business-model lens
- Included: Lower-middle-market firms that design, install, inspect, test, repair, maintain, or monitor electronic security, intrusion, video-surveillance, access-control, and fire-alarm systems for external customers on recurring contracts or through repeat service relationships.
- Excluded: Locksmiths; guard services; captive security departments; pure equipment retail or manufacturing; software-only or hardware-only vendors without an accountable service operation; shells; and non-control financing vehicles.
- Customer and revenue model: Residential and commercial customers pay installation and equipment charges, time-and-material service fees, and contractual recurring monitoring or maintenance fees. Monitoring can be bundled with installation, maintenance, repair, response notification, and equipment rental.
- Deviation from default lens: none

## Executive view
Electronic security combines recurring monitoring and maintenance revenue with a substantial on-site installation and service workforce. The opportunity is concentrated in reducing digital coordination, event handling, sales-support, and administrative labor while preserving the licensed, physical, and accountable service layer.

## How AI changes the work
AI can improve alarm verification, reduce false alarms, triage video and sensor events, draft proposals and system documentation, assist design and troubleshooting, automate customer interactions, and streamline scheduling, dispatch, billing, and sales administration. Physical installation, testing, repair, and code compliance remain hard to substitute.

## Value capture
Contractual monthly revenue and bundled service relationships allow some productivity gains to remain with the operator. Capture is limited by renewal repricing, aggressive professional-service competition, expanding DIY options, and customers' ability to self-monitor simpler systems.

## Firm availability
The supplied universe is large but estimated through a margin bridge. Broad owner-age evidence suggests succession pressure, and disclosed acquisition activity confirms that monitored-security operations transact, but there is no industry-specific transfer denominator and founder dependence can impair transferability.

## Demand durability
Security and life-safety needs, installed systems requiring service, and new sensing use cases support modest real demand growth. Operator-required demand is less secure because self-installation, self-monitoring, and platform-based offerings can remove the service firm from simpler residential work.

## Risks and uncertainty
The largest uncertainties are the exact task-level wage exposure, compatibility of legacy installed bases, realized adoption by smaller firms, customer sharing of savings, and the pace of DIY displacement. False alarms, privacy, cybersecurity, permitting, code compliance, and life-safety liability can slow automation. Cyclical installation demand and technology-driven price competition can also offset operating gains.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.4057 | — | OBSERVED | — |
| n | — | 716 | — | ESTIMATE | — |
| a | 0.25 | 0.39 | 0.53 | PROXY | S1, S2, S3 |
| rho | 0.38 | 0.58 | 0.75 | PROXY | S3, S5 |
| e | 0.7 | 0.83 | 0.92 | ESTIMATE | S1, S3, S8 |
| s5 | 0.15 | 0.27 | 0.42 | PROXY | S6, S7, S8 |
| q | 0.4 | 0.59 | 0.74 | PROXY | S3 |
| d5 | 0.96 | 1.06 | 1.17 | PROXY | S3, S4 |
| o | 0.61 | 0.76 | 0.88 | ESTIMATE | S1, S3, S8 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 1.54 | 3.67 | 6.45 | PROXY |
| F | 6.97 | 8.18 | 9.05 | ESTIMATE |
| C | 8.00 | 10.00 | 10.00 | PROXY |
| D | 5.86 | 8.06 | 10.00 | ESTIMATE |

## Caveats
- a: The BLS occupation table is May 2023 and covers five-digit NAICS 561620 rather than the exact six-digit population.
- a: Occupation shares are employment-weighted; the primitive is wage-weighted and therefore requires wage and task mapping.
- a: ADT is a large public operator whose technology and central-monitoring model may overstate the digital task share of LMM firms.
- rho: The Census figures are economy-wide and do not isolate security-system services.
- rho: The ADT filing describes intended benefits and risks, not independently measured implementation rates.
- rho: Cybersecurity, privacy, dispatch regulation, and false-negative risk can slow deployment beyond ordinary office automation.
- e: No source measures the eligible share of the supplied LMM firm population.
- e: The supplied count uses a margin bridge rather than observed normalized EBITDA.
- e: Dealer, subcontractor, monitoring-only, and installation-heavy models may be classified inconsistently in business databases.
- s5: Owner age is from data year 2018 and is not industry-specific.
- s5: The 57 disclosed acquisitions include adjacent fire-protection businesses and come from the acquirer.
- s5: A single strategic buyer's activity does not establish an industry-wide probability or reveal failed transactions.
- q: Observed revenue pricing is not a direct measure of retained AI benefit.
- q: ADT's residential scale, brand, financing, and contract portfolio differ from independent LMM operators.
- q: The range excludes demand loss and operator displacement, which are handled separately.
- d5: The BLS series includes locksmiths and measures employment rather than real service quantity.
- d5: The projection horizon extends beyond the primitive's five-year horizon.
- d5: Product upgrades, bundling, and quality changes make real demand hard to separate from nominal revenue.
- o: No source directly measures the year-five operator-required share.
- o: Residential DIY evidence may overstate displacement for commercial, institutional, and regulated systems.
- o: Definitions of accountable operation differ when software vendors, third-party central stations, dealers, and installers share responsibility.

## Sources
- **S1** — [NAPCS Product List for NAICS 5616: Investigation and Security Services](https://www2.census.gov/library/reference/napcs/product-list/web-5616-final-reformatted-edited-us052009.pdf) (accessed 2026-07-22): Defines security-system monitoring, response notification, physical response, installation, maintenance, repair, remote video monitoring, and equipment rental bundled with monitoring.
- **S2** — [Security Systems Services: May 2023 OEWS Industry-Specific Occupational Employment and Wage Estimates](https://www.bls.gov/oes/2023/may/naics5_561620.htm) (accessed 2026-07-22): Reports 158,450 total employment and detailed occupation shares, including installation and repair, office support, sales, customer service, dispatch, management, business, and computer work.
- **S3** — [ADT Inc. 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/1703056/000170305626000022/adt-20251231.htm) (accessed 2026-07-22): Documents recurring monitoring revenue, pricing, professional and DIY offerings, self-monitoring competition, AI-enabled verification and false-alarm reduction, legacy-system incompatibility, integration risk, monitoring centers, and skilled installation and service.
- **S4** — [BLS Industry Employment and Output Projections](https://www.bls.gov/emp/tables/industry-employment-and-output.htm) (accessed 2026-07-22): Projects security systems services employment of 157.2 thousand in 2024 and 176.0 thousand in 2034, an increase of 11.9%.
- **S5** — [The Rapid Adoption of Generative AI](https://www.census.gov/library/working-papers/2026/adrm/CES-WP-26-25.html) (accessed 2026-07-22): Reports AI use by 18% of firms and 32% on an employment-weighted basis; 66% of users reported augmentation only and 2% reported employment decreases.
- **S6** — [Business Owners by Age](https://www.census.gov/content/dam/Census/library/visualizations/2020/comm/business-owners-ages.pdf) (accessed 2026-07-22): Reports that 51% of responding employer-business owners were at least age 55 in the 2018 data year.
- **S7** — [Pye-Barker Fire & Safety Accelerates Growth Strategy with 57 Acquisitions in 2025](https://www.prnewswire.com/news-releases/pye-barker-fire--safety-accelerates-growth-strategy-with-57-acquisitions-in-2025-302716032.html) (accessed 2026-07-22): Company announcement reports 57 acquisitions across fire alarm, sprinkler, suppression, and security companies in 2025 and expansion to 9,000 employees across 47 states.
- **S8** — [Pye-Barker Fire & Safety Acquires S.E.M. Security Systems](https://pyebarkerfs.com/news/pye-barker-fire-safety-acquires-s-e-m-security-systems-reinforces-impact-in-new-jersey-and-new-york/) (accessed 2026-07-22): Discloses acquisition of a security-system and fire-alarm provider offering intrusion detection, video surveillance, 24-hour monitoring, installation, inspection, testing, maintenance, and code-compliance service.
