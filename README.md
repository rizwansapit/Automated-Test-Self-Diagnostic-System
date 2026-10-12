# Automated Test & Self-Diagnostic System (ATSD)

## Overview

A Python-based electromechanical test and self-diagnostic simulation demonstrating automated testing, fault detection, diagnostic reporting, test history, and retesting workflows.

## Project Objective

The project demonstrates a structured engineering test workflow:

1. Engineering specification
2. Automated testing
3. Failure detection
4. Fault diagnosis
5. Recovery and baseline restoration
6. Retesting
7. PASS / Technician Inspection

## Engineering References

- **Mechanical Assembly Drawing:** ECM-080-050
- **Electrical Schematic:** ELS-012-001

## Project Status

**Current Milestone: Step 2 — Electrical Fault Diagnosis and Test Consistency (Completed)**

Step 1 and Step 2 have been implemented, tested through simulation, and pushed to the `main` branch on GitHub.

### Completed Features

- **Mechanical Testing:** Evaluates plate thickness against predefined acceptance limits.
- **Electrical Testing:** Evaluates simulated switched output voltage against an illustrative acceptance range of 11.4–12.6 V DC.
- **Automated Test Results:** Determines PASS or FAIL based on predefined acceptance criteria.
- **Output Simulation:** Simulates output voltage based on input voltage, fuse status, and switch status.
- **Electrical Fault Diagnosis:** Supports `OPEN_FUSE`, `SWITCH_OPEN`, and `INPUT_VOLTAGE_ABNORMAL`.
- **Voltage Limit Diagnosis:** Supports `BELOW_LOWER_LIMIT` and `ABOVE_UPPER_LIMIT`.
- **Normal Operation Diagnosis:** Reports `NORMAL_OPERATION` when the simulated conditions meet the current criteria.
- **Test Reports:** Displays electrical and mechanical test results in Windows Command Prompt.
- **PostgreSQL Integration:** Stores electrical and mechanical test records in the `test_history` table.
- **Test History:** Preserves previous test records when new test runs are executed.
- **Engineering Documentation:** Defines illustrative mechanical dimensions, electrical acceptance criteria, and verification rules.

### Current Implementation

The system runs as a Python command-line simulation connected to PostgreSQL. Electrical and mechanical tests are evaluated separately and stored as individual database records.

Electrical fault simulations have been tested for normal operation, open fuse, open switch, low input voltage, and high input voltage.

### Next Development Phase

**Step 3 — Test History and Retest Management**

Planned improvements:

- Preserve the same test ID across retests.
- Store each test attempt as a separate historical record.
- Compare results before and after corrective action.
- Verify whether a failed test passes after corrective action.

## Disclaimer

This is a conceptual simulation project for educational and portfolio purposes. Its reference dimensions, electrical values, and acceptance limits have not been validated for real production hardware. It must not be represented as a production-validated or safety-critical test system.