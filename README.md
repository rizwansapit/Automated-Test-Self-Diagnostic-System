\# Automated Test \& Self-Diagnostic System (ATSD)



\## Overview



A Python-based electromechanical test and self-diagnostic simulation demonstrating automated testing, fault detection, controlled recovery, baseline restoration, and retesting.



\## Project Objective



Demonstrates a structured engineering test workflow:



1\. Engineering specification

2\. Automated testing

3\. Failure detection

4\. Diagnosis

5\. Recovery

6\. Retesting

7\. PASS / Technician Inspection



\## Engineering References



\- \*\*Mechanical Assembly Drawing:\*\* ECM-080-050

\- \*\*Electrical Schematic:\*\* ELS-012-001



\## Project Status



\*\*Current Milestone: Step 1 — Mechanical and Electrical Test Simulation (Completed)\*\*



Step 1 has been completed, tested, and pushed to the `main` branch on GitHub.



\### Completed Features



\- \*\*Mechanical Testing:\*\* Evaluates plate thickness against predefined acceptance limits.

\- \*\*Electrical Testing:\*\* Evaluates simulated switched output voltage against an illustrative acceptance range of 11.4–12.6 V DC.

\- \*\*Automated Test Results:\*\* Determines PASS or FAIL based on predefined acceptance criteria.

\- \*\*Basic Diagnostics:\*\* Supports `NORMAL\_OPERATION`, `OPEN\_FUSE`, `SWITCH\_OPEN`, `INPUT\_VOLTAGE\_ABNORMAL`, `BELOW\_LOWER\_LIMIT`, and `ABOVE\_UPPER\_LIMIT`.

\- \*\*Test Reports:\*\* Displays selected mechanical and electrical test results in the Windows Command Prompt.

\- \*\*PostgreSQL Integration:\*\* Stores mechanical and electrical test records in the `test\_history` table.

\- \*\*Test History:\*\* Preserves previous test records when new test runs are executed.

\- \*\*Engineering Documentation:\*\* Defines illustrative mechanical dimensions, electrical acceptance criteria, and verification rules.



\### Current Implementation



The system runs as a Python command-line simulation connected to PostgreSQL. Mechanical and electrical tests are evaluated separately, and their results are stored as individual database records.



\### Next Development Phase



Improve diagnostic consistency, validate fault-simulation scenarios, and strengthen the separation between measurement results and fault diagnosis.



\## Disclaimer



This is a conceptual simulation project for educational and portfolio purposes. Its reference dimensions, electrical values, and acceptance limits have not been validated for real production hardware. It must not be represented as a production-validated or safety-critical test system.

