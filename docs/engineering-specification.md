\# Engineering Specification



\## 1. Project Information



\- \*\*Project:\*\* Automated Test \& Self-Diagnostic System (ATSD)

\- \*\*Document:\*\* Engineering Specification

\- \*\*Status:\*\* Draft

\- \*\*Purpose:\*\* Define the reference specifications and acceptance criteria used by the test simulation.



\## 2. Engineering References



| Part Number | Description | Revision |

|---|---|---|

| ECM-080-050 | Mechanical Assembly Drawing | A |

| ELS-012-001 | Electrical Schematic | A |



\## 3. Scope



This document defines the illustrative mechanical and electrical parameters used by the ATSD simulation.



The values are intended for educational and simulation purposes only. They are not validated manufacturing specifications and must not be used as acceptance criteria for real production hardware without appropriate engineering review and approval.



The simulation will evaluate test results against predefined reference values and acceptance limits. It must not modify those limits automatically to obtain a PASS result.



\## 4. Mechanical Specifications



\*\*Reference Drawing:\*\* ECM-080-050  

\*\*Revision:\*\* A  

\*\*Units:\*\* Millimetres (mm), unless otherwise specified.



\### 4.1 General Assembly



| Parameter | Drawing Value | Notes |

|---|---:|---|

| Plate width | 80 mm | Overall plate dimension |

| Plate depth | 50 mm | Overall plate dimension |

| Assembly height | 24 mm | Overall height shown in side view |

| Plate thickness | 3 mm | Marked as 3 THK |

| General tolerance | ±0.2 mm | Illustrative tolerance where no specific tolerance is provided |

| Connector mounting opening | Ø20 mm | Illustrative drawing value |

| Mounting holes | 4 × Ø4.5 mm | Four mounting holes |

| Mounting hole spacing — horizontal | 60 mm | Illustrative horizontal spacing |

| Mounting hole spacing — vertical | 30 mm | Illustrative vertical spacing |



\*\*Reference:\*\* ECM-080-050, Revision A.



\*\*Note:\*\* The dimensions and tolerances above are reference values for the simulation. They must be verified against the approved drawing before being used for actual manufacturing or inspection.



\### 4.2 Assembly Information



| Parameter | Drawing Value |

|---|---|

| Connector | 4-pin circular, panel mount |

| Mounting screws | 4 × M4 |

| Assembly torque | 0.5 N·m |

| Datum A | Underside of plate |

| Plate material | Aluminium 6061-T6 |

| Connector body material | PA66 |



\*\*Reference:\*\* ECM-080-050, Revision A.



\*\*Note:\*\* Material, torque and component details are illustrative reference values and have not been validated for production use.



\### 4.3 Inspection Notes



\- Use the drawing dimensions as the reference, not measurements taken from the drawing image.

\- Apply the general tolerance of ±0.2 mm only where no specific tolerance is provided and where the illustrative drawing specifies that general tolerance.

\- Record actual measurements separately from nominal dimensions.

\- Evaluate measurements against the applicable acceptance limits.

\- Record a result as PASS only when it satisfies the defined acceptance rule.

\- Record a result as FAIL when it falls outside the defined acceptance limits.

\- Use REVIEW only when a separate review rule has been defined.

\- Do not change nominal values, tolerances or acceptance limits automatically to obtain a PASS result.

\- The drawing is conceptual and has not been validated for manufacturing or production use.



\### 4.4 Initial Test Parameter — Plate Width



| Parameter | Value |

|---|---:|

| Nominal value | 80.0 mm |

| Tolerance | ±0.2 mm |

| Lower acceptance limit | 79.8 mm |

| Upper acceptance limit | 80.2 mm |

| Unit | mm |



\*\*Acceptance rule:\*\* PASS when the measured plate width is between 79.8 mm and 80.2 mm, inclusive. Otherwise, FAIL.



\*\*Review rule:\*\* Measurements near either acceptance limit may be flagged for review once a separate review threshold has been defined. The acceptance limits must not be changed automatically.



\*\*Reference:\*\* ECM-080-050, Revision A.



\*\*Note:\*\* This is an illustrative simulation parameter, not a validated manufacturing acceptance criterion.



\### 4.5 Initial Test Parameter — Plate Depth



| Parameter | Value |

|---|---:|

| Nominal value | 50.0 mm |

| Tolerance | ±0.2 mm |

| Lower acceptance limit | 49.8 mm |

| Upper acceptance limit | 50.2 mm |

| Unit | mm |



\*\*Acceptance rule:\*\* PASS when the measured plate depth is between 49.8 mm and 50.2 mm, inclusive. Otherwise, FAIL.



\*\*Review rule:\*\* Measurements near either acceptance limit may be flagged for review once a separate review threshold has been defined. The acceptance limits must not be changed automatically.



\*\*Reference:\*\* ECM-080-050, Revision A.



\*\*Note:\*\* This is an illustrative simulation parameter, not a validated manufacturing acceptance criterion.



\### 4.6 Initial Test Parameter — Assembly Height



| Parameter | Value |

|---|---:|

| Nominal value | 24.0 mm |

| Tolerance | ±0.2 mm |

| Lower acceptance limit | 23.8 mm |

| Upper acceptance limit | 24.2 mm |

| Unit | mm |



\*\*Acceptance rule:\*\* PASS when the measured assembly height is between 23.8 mm and 24.2 mm, inclusive. Otherwise, FAIL.



\*\*Review rule:\*\* Measurements near either acceptance limit may be flagged for review once a separate review threshold has been defined. The acceptance limits must not be changed automatically.



\*\*Reference:\*\* ECM-080-050, Revision A.



\*\*Note:\*\* This is an illustrative simulation parameter, not a validated manufacturing acceptance criterion.



\### 4.7 Initial Test Parameter — Plate Thickness



| Parameter | Value |

|---|---:|

| Nominal value | 3.0 mm |

| Tolerance | ±0.2 mm |

| Lower acceptance limit | 2.8 mm |

| Upper acceptance limit | 3.2 mm |

| Unit | mm |



\*\*Acceptance rule:\*\* PASS when the measured plate thickness is between 2.8 mm and 3.2 mm, inclusive. Otherwise, FAIL.



\*\*Review rule:\*\* Measurements near either acceptance limit may be flagged for review once a separate review threshold has been defined. The acceptance limits must not be changed automatically.



\*\*Reference:\*\* ECM-080-050, Revision A.



\*\*Note:\*\* This is an illustrative simulation parameter, not a validated manufacturing acceptance criterion.



\## 5. Electrical Specifications



\*\*Reference Drawing:\*\* ELS-012-001  

\*\*Revision:\*\* A  

\*\*Circuit Type:\*\* Low-voltage DC concept circuit.



\### 5.1 Electrical Parameters



| Parameter | Reference Value | Notes |

|---|---:|---|

| Nominal input voltage | 12 V DC | Illustrative supply voltage |

| Fuse F1 rating | 250 mA / 32 V DC | Illustrative fuse specification |

| Switch SW1 rating | 1 A / 24 V DC | SPST switch, shown open |

| Resistor R1 | 2.2 kΩ, ±5%, 0.25 W | LED current-limiting resistor |

| LED D1 forward voltage | Approximately 2 V | Assumed illustrative value |

| LED current | Approximately 4.5 mA | Estimated from the assumed supply and LED values |

| External load current | 100 mA nominal | Assumed external load current |

| Total current | Approximately 105 mA | Estimated when the switch is closed and the load draws 100 mA, assuming the LED branch shares the supply current |

| Wire specification | 22 AWG copper | Red for +V and black for 0 V |



\*\*Reference:\*\* ELS-012-001, Revision A.



\*\*Note:\*\* Electrical values are illustrative. Actual current depends on the circuit topology, component characteristics, supply voltage and connected load.



\### 5.2 Connector Pinout



| Connector | Pin | Signal |

|---|---:|---|

| J1 — Input | 1 | +12 V DC |

| J1 — Input | 2 | 0 V / GND |

| J2 — Output | 1 | +12V\_SW |

| J2 — Output | 2 | 0 V / GND |



\*\*Reference:\*\* ELS-012-001, Revision A.



\*\*Note:\*\* The connector pinout must be checked against the schematic before it is treated as a verified electrical interface specification.



\### 5.3 Circuit Components



| Reference | Component | Function |

|---|---|---|

| F1 | Fuse | Provides overcurrent protection |

| SW1 | SPST switch | Controls the switched output |

| R1 | 2.2 kΩ resistor | Limits current through the LED branch |

| D1 | Indicator LED | Indicates the relevant power or circuit condition |

| J1 | 2-pin input connector | Receives the DC input |

| J2 | 2-pin output connector | Supplies the external load |



\*\*Reference:\*\* ELS-012-001, Revision A.



\### 5.4 Electrical Verification Notes



\- The circuit is a conceptual, low-voltage DC simulation reference.

\- The expected switched output is approximately 12 V DC when the input is correct, the fuse is intact, SW1 is closed and the circuit connections are correct.

\- An open fuse or an open switch can interrupt the switched output.

\- A failed LED branch does not necessarily mean the external output has failed.

\- LED status and external output status must be evaluated separately where the circuit design allows them to be tested independently.

\- Electrical PASS/FAIL limits must be explicitly defined before automated electrical testing is implemented.

\- Test conditions must identify the expected switch state, input voltage and load condition.

\- The drawing is illustrative and has not been validated for real hardware or production use.



\## 6. Verification Rules



\- All test results must be evaluated against predefined reference specifications and acceptance limits.

\- The system must not modify nominal values, tolerances or acceptance limits automatically to obtain a PASS result.

\- Every test result must record the test parameter, reference value, measured or simulated value, applicable limits and final status.

\- A test result must be marked PASS only when the applicable acceptance rule is satisfied.

\- A test result outside the acceptance limits must remain recorded as FAIL.

\- REVIEW may be assigned only when a separate review rule and threshold have been defined.

\- Any recovery action must preserve the original engineering specifications and acceptance limits.

\- Failed tests must remain in the test history, even if a subsequent retest passes.

\- Initial failures, diagnostic findings, recovery actions and retest results should be recorded separately.

\- These verification rules apply to the ATSD simulation and do not replace approved engineering or quality procedures for real production hardware.



\## 7. Document Limitations



\- This document is a draft for an educational engineering simulation.

\- The reference drawings and parameters are conceptual and are not validated production documents.

\- The listed values must be verified against approved engineering documentation before use in real hardware testing or manufacturing.

\- The simulation must not be represented as a validated test system for Lam Research equipment or any other commercial production equipment.



