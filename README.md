# Automated Test & Self-Diagnostic System (ATSD)

## Overview

A Python-based electromechanical test and self-diagnostic simulation demonstrating automated testing, fault detection, diagnostic reporting, simulated recovery, technician escalation, test history, and retesting workflows.

## Project Objective

The project demonstrates a structured engineering test workflow:

1. Engineering specification
2. Automated testing
3. Failure detection
4. Fault diagnosis
5. Simulated recovery and technician escalation
6. Retesting and test history
7. Final PASS / Technician Inspection

## Engineering References

- **Mechanical Assembly Drawing:** ECM-080-050 Rev A
- **Electrical Schematic:** ELS-012-001 Rev A

## Project Status

**Current Milestone: Step 3 — Automated Recovery, Technician Escalation and Retest History (Implemented and Tested in Simulation)**

Step 1 and Step 2 have been implemented, tested through simulation, and pushed to the `main` branch on GitHub. Step 3 introduces simulated automated recovery, technician escalation, and separate database records for initial and final electrical test results.

### Completed Features

- **Mechanical Testing:** Evaluates plate thickness against predefined acceptance limits.
- **Electrical Testing:** Evaluates simulated switched output voltage against an illustrative acceptance range of 11.4–12.6 V DC.
- **Automated Test Results:** Determines PASS or FAIL based on predefined acceptance criteria.
- **Output Simulation:** Simulates output voltage based on input voltage, fuse status, and switch status.
- **Electrical Fault Diagnosis:** Supports `OPEN_FUSE`, `SWITCH_OPEN`, and `INPUT_VOLTAGE_ABNORMAL`.
- **Voltage Limit Diagnosis:** Supports `BELOW_LOWER_LIMIT` and `ABOVE_UPPER_LIMIT`.
- **Normal Operation Diagnosis:** Reports `NORMAL_OPERATION` when the simulated conditions meet the current criteria.
- **Failure Decision Logic:** Routes failed tests to simulated automated recovery or technician mode according to fuse and switch status.
- **Automated Recovery Simulation:** Applies simulated 1.0 V adjustments, with a maximum of five attempts, when recovery is eligible.
- **Technician Escalation:** Routes open-fuse and open-switch failures to `TECHNICIAN_MODE` without attempting automated recovery.
- **Initial and Final Test Records:** Stores the initial electrical result and the post-recovery result as separate records in PostgreSQL.
- **Test ID Consistency:** Preserves the same `test_id` across the initial and final electrical records while PostgreSQL generates a distinct `record_id` for each record.
- **Test Reports:** Displays electrical and mechanical test results in Windows Command Prompt.
- **PostgreSQL Integration:** Stores electrical and mechanical test records in the `test_history` table.
- **Test History:** Preserves previous records when new test runs are executed.
- **Engineering Documentation:** Defines illustrative mechanical dimensions, electrical acceptance criteria, and verification rules.

### Current Implementation

The system runs as a Python command-line simulation connected to PostgreSQL. Electrical and mechanical tests are evaluated separately and stored in the `test_history` table.

The following scenarios have been tested:

- Normal electrical operation.
- Low input voltage with simulated automated recovery.
- Open fuse resulting in `TECHNICIAN_MODE`.
- Open switch resulting in `TECHNICIAN_MODE`.
- Separate database records for the initial failed electrical test and the post-recovery passing result.

A database verification confirmed that the initial result (`FAIL`, 10.000 V DC) and post-recovery result (`PASS`, 12.000 V DC) were stored separately under the same test ID, `ELEC-0001`, with different record IDs.

### Limitations

Automated voltage adjustment is a software simulation. The electrical schematic ELS-012-001 Rev A does not establish that the physical circuit can automatically adjust its output voltage. Actual hardware recovery, sensor-based retesting, and production validation have not been demonstrated.

The current implementation records initial and final electrical results. A more complete retest-management workflow may later add explicit attempt numbering, recovery metadata, and stronger linkage between test attempts.

### Next Development Phase

**Step 4 — Further Test History and Retest Management Improvements**

Potential improvements:

- Add explicit attempt numbers or retest sequence identifiers.
- Record recovery actions and the reason for technician escalation.
- Improve linkage between initial failures, recovery attempts, and final outcomes.
- Add automated database queries or reports for test history and recovery success rates.

## Disclaimer

This is a conceptual simulation project for educational and portfolio purposes. Its reference dimensions, electrical values, and acceptance limits have not been validated for real production hardware. It must not be represented as a production-validated or safety-critical test system.