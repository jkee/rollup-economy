# 334412 — Bare Printed Circuit Board Manufacturing

*v5.1 Stage 1 research memo. Run `334412-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** PRIORITY · A 7.22 · L 4.02 · interval CONDITIONAL → PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Complex, urgent, qualified PCB programs reward faster engineering and higher yield, making AI-enabled CAM and inspection directly valuable within sticky customer workflows.
**Weakness:** Commodity price competition and continuous technology reinvestment can overwhelm labor savings at undifferentiated or obsolete board shops.

## Business-model lens
- Included: Independent lower-middle-market manufacturers of rigid, flex, rigid-flex, high-density interconnect, RF/microwave, and other bare printed circuit boards, emphasizing quick-turn prototypes, high-mix low-volume production, domestic or trusted manufacturing, engineering and CAM support, qualification, and repeat customer part numbers.
- Excluded: PCB assembly without bare-board fabrication; semiconductor substrates classified elsewhere; pure design bureaus and brokers; commodity offshore-volume platforms without recurring engineering relationships; captive board plants; and large integrated manufacturers outside the LMM band.
- Customer and revenue model: Customers include aerospace and defense contractors, data-center and networking OEMs, medical and industrial equipment makers, automotive suppliers, electronics manufacturing services providers, and hardware developers. Revenue is earned per custom board or production lot, with engineering review, nonrecurring setup, expedited turnaround, qualification, repeat releases, and time-to-market support creating service-like program economics.
- Deviation from default lens: none

## Executive view
Bare PCB fabrication combines unusually high labor leverage with a substantial domestic LMM universe and strong structural demand. The attractive target is a qualified high-mix, quick-turn shop embedded in customer engineering and repeat programs, not a commodity board producer competing with Asian scale. AI can materially compress CAM, quoting, inspection, test, and process-control work.

## How AI changes the work
Near-term uses include automated DFM and design-rule review, CAM preparation, quoting, panelization, defect classification, optical and electrical-test analysis, chemistry and process monitoring, predictive maintenance, scheduling, quality records, and customer communication. Wet chemistry, drilling, lamination, plating, handling, maintenance, and complex disposition decisions remain physical or expert-controlled.

## Value capture
Global commodity pricing limits retention of generic savings. Faster turns, complex-board yield, fewer escapes, secure domestic production, qualification, and co-development create greater capture because a late or failed board can delay an entire product program. Expedite premiums and customer retention should be tested directly.

## Firm availability
The frozen estimate of 149 LMM firms is attractive in quantity but not necessarily quality. Aging equipment, environmental compliance, export controls, certifications, technology gaps, customer concentration, and high reinvestment needs may remove many candidates. Skilled CAM and process teams and current HDI, flex, RF, or regulated capabilities are key.

## Demand durability
AI infrastructure, networking, aerospace and defense, medical devices, vehicles, and industrial automation support demand, while secure domestic supply adds resilience for regulated programs. Asian price competition, inventory cycles, rapid technology migration, and concentration of leading-edge demand in large plants remain important offsets.

## Risks and uncertainty
The main uncertainties are the true number of domestic fabricators in the EBITDA band, technology and certification mix, capex backlog, environmental liabilities, qualification portability, customer concentration, offshore price pressure, and whether advertised quick-turn providers actually fabricate boards in-house.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.4851 | — | OBSERVED | — |
| n | — | 149 | — | ESTIMATE | — |
| a | 0.38 | 0.52 | 0.66 | PROXY | S1, S2, S3, S4 |
| rho | 0.4 | 0.58 | 0.74 | ESTIMATE | S3, S4 |
| e | 0.28 | 0.47 | 0.65 | PROXY | S5, S6, S7 |
| s5 | 0.09 | 0.16 | 0.24 | PROXY | S8 |
| q | 0.28 | 0.45 | 0.62 | PROXY | S5, S6, S7 |
| d5 | 1.03 | 1.22 | 1.4 | PROXY | S5, S6 |
| o | 0.94 | 0.99 | 1 | ESTIMATE | S1, S5 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 2.95 | 5.85 | 9.48 | ESTIMATE |
| F | 2.51 | 4.02 | 5.13 | ESTIMATE |
| C | 5.60 | 9.00 | 10.00 | PROXY |
| D | 9.68 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: Semiconductor technicians are a process analogue, not PCB-specific labor evidence.
- a: AI inspection evidence often concerns assembled boards as well as bare boards.
- a: Rigid, flex, HDI, RF, prototype, and production facilities have different task mixes.
- rho: No representative AI-adoption study for bare-board shops was found.
- rho: Front-end engineering is easier to automate than closed-loop wet processing.
- rho: Qualified defense and medical work requires auditable human control.
- e: Repeat part orders are not contractual recurring revenue.
- e: Some advertised full-service providers outsource bare-board fabrication.
- e: Large advanced-board programs may not resemble LMM quick-turn economics.
- s5: Cross-industry intentions are not observed PCB transactions.
- s5: Stated plans may not produce a marketable plant.
- s5: Distressed capacity may be available but require disproportionate reinvestment.
- q: Capture is much lower in standard two-layer boards than HDI, flex, RF, or regulated work.
- q: Large customers can dual-source after qualification.
- q: Customers may directly claim benefits from faster automated quoting and DFM.
- d5: Large-company growth may not reach LMM shops.
- d5: Monthly book-to-bill data are volatile and not a five-year forecast.
- d5: Demand can grow while obsolete facilities lose share.
- o: The factor isolates AI-related obsolescence from ordinary offshore competition.
- o: Legacy board technologies can become obsolete even while the industry grows.
- o: Advanced substrate integration can shift value outside this NAICS.

## Sources
- **S1** — [NAICS 334412 - Bare Printed Circuit Board Manufacturing](https://www.naics.com/naics-code-description/?code=334412&v=2022) (accessed 2026-07-22): Industry boundary for manufacturers of rigid and flexible bare printed circuit boards.
- **S2** — [Semiconductor Processing Technicians](https://www.onetonline.org/link/summary/51-9141.00) (accessed 2026-07-22): Process proxy covering computerized cycles, inspection, photolithography, etching, chemical baths, cleaning, loading, maintenance, measurement, and records.
- **S3** — [AI in Automated Optical Inspection for Electronics Manufacturing](https://www.electronics.org/news-release/new-ipc-white-paper-focuses-use-artificial-intelligence-automated-optical-inspection) (accessed 2026-07-22): Industry evidence on AI improving inspection accuracy, manual intervention, production efficiency, reliability, and time to market, with deployment challenges.
- **S4** — [DVQI: AI Visual Inspection in Electronics Manufacturing](https://arxiv.org/abs/2312.09232) (accessed 2026-07-22): Deployed AI inspection evidence for PCB assemblies, used as a technical proxy for adaptable board inspection and defect classification.
- **S5** — [TTM Technologies 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/1116942/000119312526051976/ttmi-20251229.htm) (accessed 2026-07-22): PCB customization, one-stop design and engineering, advanced interconnects, customer and end-market breadth, time-to-market value, and 2025 data-center, networking, aerospace and defense growth.
- **S6** — [North American PCB Industry Results for March 2025](https://www.ipc.org/news-release/north-american-pcb-industry-shipments-down-31-percent-march) (accessed 2026-07-22): Representative North American PCB shipments, bookings, year-to-date trends, and book-to-bill evidence, with interpretation guidance.
- **S7** — [Custom PCB Engineering and Repeat Orders](https://blindburiedcircuits.com/faq/) (accessed 2026-07-22): Provider evidence for PCB layout and engineering, turnkey manufacturing, bare-board orders, and repeat ordering by prior part number.
- **S8** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Cross-industry owner-age and five-year sale, transfer, closure, and succession-intention evidence.
