# 336320 — Motor Vehicle Electrical and Electronic Equipment Manufacturing

*v5.1 Stage 1 research memo. Run `336320-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 6.53 · L 0.84 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Rising electrical and electronic content per vehicle.
**Weakness:** OEM bargaining and safety-validation constraints limit realized and retained savings.

## Business-model lens
- Included: Independent LMM manufacturers of vehicle electrical, electronic, power-control, lighting, sensing, wiring, and related equipment for repeat external OEM and aftermarket customers.
- Excluded: Captive OEM plants, software-only firms, distributors without manufacturing, shell brands, and financing vehicles.
- Customer and revenue model: Repeat per-unit supply under OEM programs, qualified contracts, distributor replenishment, and aftermarket orders.
- Deviation from default lens: none

## Executive view
Electronic content growth supports demand, while AI improves technical and commercial workflows more than factory work.

## How AI changes the work
Requirements, documentation, test analysis, planning, quoting, and support are exposed; physical production and safety validation remain accountable.

## Value capture
Qualification helps, but OEM procurement and redesign reclaim meaningful savings.

## Firm availability
Repeat programs fit the lens; the 157-firm count and transfer probability remain estimates.

## Demand durability
EVs and ADAS add power electronics, sensors, wiring, and computing, though integration and imports create risk.

## Risks and uncertainty
Cybersecurity, recalls, semiconductor cycles, platform losses, warranty claims, and OEM concentration dominate.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1688 | — | OBSERVED | — |
| n | — | 157 | — | ESTIMATE | — |
| a | 0.15 | 0.25 | 0.36 | PROXY | S1, S2 |
| rho | 0.32 | 0.5 | 0.65 | ESTIMATE | S3 |
| e | 0.52 | 0.7 | 0.83 | ESTIMATE | — |
| s5 | 0.12 | 0.23 | 0.35 | ESTIMATE | — |
| q | 0.34 | 0.51 | 0.68 | ESTIMATE | — |
| d5 | 1 | 1.14 | 1.32 | PROXY | S2, S3, S4 |
| o | 0.9 | 0.97 | 0.99 | ESTIMATE | S2, S3 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.32 | 0.84 | 1.58 | ESTIMATE |
| F | 3.83 | 5.26 | 6.18 | ESTIMATE |
| C | 6.80 | 10.00 | 10.00 | ESTIMATE |
| D | 9.00 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: No six-digit task mix was found.
- rho: Implementation varies by hardware, software content, and safety criticality.
- e: The assigned 157-firm count is margin-bridged.
- s5: Technology or product-line acquisitions are not necessarily control transfers.
- q: Aftermarket and proprietary products retain more than build-to-print programs.
- d5: Technology adoption is not a direct six-digit shipment forecast.
- o: Integration can reduce discrete units without eliminating hardware manufacturing.

## Sources
- **S1** — [BLS May 2023 OEWS: Motor Vehicle Parts Manufacturing](https://www.bls.gov/oes/2023/may/naics4_336300.htm) (accessed 2026-07-22): Reports 557,020 jobs and substantial assembly and metalworking employment across automotive parts.
- **S2** — [DOE Power Electronics Research and Development](https://www.energy.gov/cmei/vehicles/power-electronics-research-and-development) (accessed 2026-07-22): Identifies inverters, converters, and chargers as core hybrid and EV components that control and distribute electrical power.
- **S3** — [NHTSA Vehicle Cybersecurity](https://www.nhtsa.gov/research/vehicle-cybersecurity) (accessed 2026-07-22): States ADAS depends on electronics, sensors, and computer systems and emphasizes cybersecurity risk.
- **S4** — [EIA Annual Energy Outlook: IRA Issues in Focus](https://www.eia.gov/outlooks/aeo/IIF_IRA/) (accessed 2026-07-22): Projects EVs at 15% of 2030 light-duty sales in the reference case, with alternative cases from 12% to nearly 17%.
