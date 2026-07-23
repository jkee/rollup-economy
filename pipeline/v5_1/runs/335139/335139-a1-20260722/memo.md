# 335139 — Electric Lamp Bulb and Other Lighting Equipment Manufacturing

*v5.1 Stage 1 research memo. Run `335139-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** no base (evidence-first) · A — · L — · interval STRUCTURAL_OUT → CONDITIONAL · readiness STRESS_TEST_ONLY · action EVIDENCE_FIRST

**Driver:** Digital engineering, quality, and connected-product workflows provide AI opportunities around a high labor-share manufacturing process.
**Weakness:** The eligible firm population is unknown and likely small, while LED longevity erodes replacement volume.

## Business-model lens
- Included: US lower-middle-market manufacturers of electric lamp bulbs and parts other than LED semiconductor devices, street and outdoor lighting equipment, flashlights, and other lighting equipment that repeatedly supply external OEM, municipal, distributor, private-label, and contract-manufacturing customers.
- Excluded: LED semiconductor manufacturers, residential and commercial fixture manufacturers classified separately, distributors, captive internal plants, firms outside the EBITDA band, shells, and non-control financing vehicles.
- Customer and revenue model: Predominantly per-unit or project product sales through distributors, OEMs, government buyers, and retailers; qualifying outsourced-service revenue is limited to recurring private-label, contract manufacturing, configuration, and lifecycle support.
- Deviation from default lens: none

## Executive view
Lighting equipment combines AI-addressable design, planning, quality, and service work with assembly-heavy physical production. The larger issue is fit: most firms sell products rather than an outsourced service, the LMM firm count is missing, and LED longevity can reduce replacement demand even as connected-lighting adoption grows.

## How AI changes the work
AI can assist optical and thermal design, component substitution, quoting, forecasting, planning, inspection, test analysis, documentation, and customer support. Humans and equipment remain responsible for assembly, soldering, testing, packaging, certification, and release.

## Value capture
Commodity lamps and portable products face imports, transparent pricing, tenders, and channel bargaining. Specialty, certified, municipal, and connected products can retain more through performance, reliability, service, and switching costs.

## Firm availability
Only private-label, contract-manufacturing, or service-rich specialty suppliers clearly fit the lens. The frozen dataset has no defensible n, so even a bounded eligibility share cannot support a target count without a separate census.

## Demand durability
LED conversion and connected lighting support upgrades, but longer product life and high eventual penetration reduce replacement frequency. Code boundaries also shift value toward semiconductors, controls, and fixture categories outside this industry.

## Risks and uncertainty
Key risks are missing firm count, service-lens ineligibility, imports, technology obsolescence, falling replacement frequency, channel inventory, certification and warranty claims, component shortages, cybersecurity, and code-boundary leakage.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.3176 | — | OBSERVED | — |
| n | — | — | — | MISSING | — |
| a | 0.17 | 0.28 | 0.41 | PROXY | S1, S2 |
| rho | 0.38 | 0.58 | 0.74 | ESTIMATE | S1, S3 |
| e | 0.04 | 0.13 | 0.29 | ESTIMATE | S2 |
| s5 | 0.08 | 0.16 | 0.27 | PROXY | S4 |
| q | 0.18 | 0.34 | 0.53 | ESTIMATE | S3 |
| d5 | 0.72 | 0.91 | 1.08 | PROXY | S3, S5 |
| o | 0.86 | 0.94 | 0.98 | ESTIMATE | S1, S3 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.82 | 2.06 | 3.85 | ESTIMATE |
| F | — | — | — | MISSING |
| C | 3.60 | 6.80 | 10.00 | ESTIMATE |
| D | 6.19 | 8.55 | 10.00 | ESTIMATE |

## Caveats
- a: No six-digit occupation-by-task dataset was located.
- a: The code mixes legacy bulbs, portable lights, street lighting, and other equipment with very different labor and technology profiles.
- rho: DOE evidence describes technology adoption and connected-lighting potential, not factory AI realization.
- rho: Low-volume specialty firms may lack sufficient labeled quality and warranty data.
- e: The frozen dataset declares n missing; no firm count was researched or substituted.
- e: Eligibility is sensitive to whether repeat configured product supply is treated as outsourced service.
- s5: Gallup is not industry- or size-specific and measures plans rather than completed transfers.
- s5: The missing firm-count denominator prevents a stable observed industry transfer rate.
- q: No representative contract or pass-through dataset was located.
- q: Retention differs sharply between commodity replacement lamps and specified outdoor or connected systems.
- d5: DOE's forecast is market-wide and long-dated, not a six-digit output forecast.
- d5: The code boundary excludes important LED and fixture value pools, and classification may shift as products integrate.
- o: Accountable manufacturing can consolidate into large global suppliers outside the lens.
- o: Connected lighting can move value from hardware operators to software platforms without eliminating physical products.

## Sources
- **S1** — [Electrical Equipment, Appliance, and Component Manufacturing: NAICS 335](https://www.bls.gov/iag/tgs/iag335.htm) (accessed 2026-07-22): Reports 2025 broader-subsector employment including 65,350 electrical and electronic assemblers, 57,660 team assemblers, and 14,050 inspectors, and identifies electric lighting equipment as a NAICS 335 group.
- **S2** — [NAICS Classification for Electric Lighting Equipment Manufacturing](https://www.census.gov/naics/?details=335131&input=335131&year=2022) (accessed 2026-07-22): Places electric bulbs and tubes other than LED devices, street lights, flashlights, and nonelectric lighting equipment in NAICS 335139 while classifying LED devices in semiconductor manufacturing.
- **S3** — [Energy Savings Forecast of Solid-State Lighting](https://www.energy.gov/cmei/ssl/ssl-forecast-report) (accessed 2026-07-22): Projects LED lamps and luminaires at 84% of lighting applications by 2035 and 569 TWh of annual energy savings if DOE research goals are achieved; identifies connected lighting as part of projected savings.
- **S4** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Fall 2024 US survey found 22% of employer-business owners planned to sell or transfer ownership within five years, while 5% planned closure and 5% had no plan.
- **S5** — [About the Solid-State Lighting Program](https://www.energy.gov/cmei/ssl/about-solid-state-lighting-program) (accessed 2026-07-22): States LED technology still has significant efficiency potential and projects 6.9 trillion kWh of cumulative electricity savings through 2035 if DOE targets for efficiency, controls, and connected lighting are met.
