\# Engineering Specification



\## 1. Project Information



\- \*\*Project:\*\* Automated Test \& Self-Diagnostic System (ATSD)

\- \*\*Document:\*\* Engineering Specification

\- \*\*Status:\*\* Draft

\- \*\*Purpose:\*\* Define the reference specifications used by the test simulation.



\## 2. Engineering References



| Part Number | Description | Revision |

|---|---|---|

| ECM-080-050 | Mechanical Assembly Drawing | A |

| ELS-012-001 | Electrical Schematic | A |



\## 3. Scope



This document records the illustrative engineering parameters shown in the project drawings.



The values are intended for simulation and educational purposes only. They are not validated manufacturing specifications.



\## 4. Mechanical Specifications



\*\*Reference Drawing:\*\* ECM-080-050

\*\*Revision:\*\* A

\*\*Units:\*\* Millimetres (mm), unless otherwise specified



\### 4.1 General Assembly



| Parameter | Drawing Value | Notes |

|---|---:|---|

| Plate width | 80 mm | Overall plate dimension |

| Plate depth | 50 mm | Overall plate dimension |

| Assembly height | 24 mm | Overall height shown in side view |

| Plate thickness | 3 mm | Marked as 3 THK |

| General tolerance | ±0.2 mm | Unless otherwise specified |

| Connector mounting opening | Ø20 mm | Illustrative drawing value |

| Mounting holes | 4 × Ø4.5 mm | Four holes |

| Mounting hole spacing | 60 mm | Horizontal spacing shown |

| Mounting hole spacing | 30 mm | Vertical spacing shown |



\### 4.2 Assembly Information



| Parameter | Drawing Value |

|---|---|

| Connector | 4-pin circular, panel mount |

| Mounting screws | 4 × M4 |

| Assembly torque | 0.5 N·m |

| Datum A | Underside of plate |

| Plate material | Aluminium 6061-T6 |

| Connector body material | PA66 |



\### 4.3 Inspection Notes



\- Use the drawing dimensions as the reference, not measurements taken from the image.

\- Apply the general tolerance of ±0.2 mm only where no specific tolerance is provided.

\- Record actual measurements separately from nominal dimensions.

\- Mark a measurement as PASS only when it meets the applicable acceptance limits.

\- The drawing is conceptual and is not validated for manufacturing or production use.



\## 5. Electrical Specifications



\*\*Reference Drawing:\*\* ELS-012-001  

\*\*Revision:\*\* A  

\*\*Circuit Type:\*\* Low-voltage DC concept circuit



\### 5.1 Electrical Parameters



| Parameter | Drawing Value | Notes |

|---|---:|---|

| Nominal input voltage | 12 V DC | Illustrative value |

| Fuse F1 rating | 250 mA / 32 V DC | Fuse specification |

| Switch SW1 rating | 1 A / 24 V DC | SPST switch, shown open |

| Resistor R1 | 2.2 kΩ, ±5%, 0.25 W | LED current-limiting resistor |

| LED D1 forward voltage | Approximately 2 V | Assumed illustrative value |

| LED current | Approximately 4.5 mA | Shown on schematic |

| External load current | 100 mA nominal | External load |

| Total current | Approximately 105 mA | SW1 closed, load 100 mA |

| Wire specification | 22 AWG copper | Red for +V, black for 0 V |



\### 5.2 Connector Pinout



| Connector | Pin | Signal |

|---|---:|---|

| J1 — Input | 1 | +12 V DC |

| J1 — Input | 2 | 0 V / GND |

| J2 — Output | 1 | +12V\_SW |

| J2 — Output | 2 | 0 V / GND |



\### 5.3 Circuit Components



| Reference | Component | Function |

|---|---|---|

| F1 | Fuse | Overcurrent protection |

| SW1 | SPST switch | Controls the switched output |

| R1 | 2.2 kΩ resistor | Limits LED current |

| D1 | Indicator LED | Indicates power when the circuit conditions permit |

| J1 | 2-pin input connector | Receives DC input |

| J2 | 2-pin output connector | Supplies the external load |



\### 5.4 Electrical Verification Notes



\- The circuit is a conceptual, low-voltage DC simulation reference.

\- The expected output is approximately 12 V DC when the input is correct, the fuse is intact, and SW1 is closed.

\- An open fuse or open switch can interrupt the switched output.

\- A failed LED branch does not necessarily mean the external output has failed.

\- Electrical PASS/FAIL limits must be explicitly defined before automated testing.

\- The drawing is illustrative and has not been validated for real hardware or production use.



\## 6. Verification Rules



\- Test results must be evaluated against the defined reference specifications.

\- The system must not change acceptance limits to force a PASS result.

\- Any recovery action must preserve the original specifications.

\- Failed tests must remain recorded, even if a later retest passes.

