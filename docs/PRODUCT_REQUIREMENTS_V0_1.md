# Product Requirements — EnginesGoneBananas

## Evidence classification
- VERIFIED: Repository exists and is standalone.
- REPORTED: Automotive business/platform umbrella; Master Mechanic AI is a separate product.
- INFERRED: This repository should own customer/business workflows and shared automotive platform surfaces, not diagnostic AI internals.
- UNKNOWN: Exact MVP surfaces, user roles, payments, scheduling, CRM, inventory/service workflows, branding, and deployment stack.
- BLOCKED: Broad implementation until product scope is narrowed enough to avoid inventing features.

## Initial architecture boundary
EnginesGoneBananas may consume Master Mechanic AI through explicit interfaces, but must not absorb or duplicate that implementation.

## Phase 1 deliverables
1. Customer/business workflow map.
2. MVP scope and non-goals.
3. Interface contract with Master Mechanic AI.
4. Security/privacy requirements.
5. Acceptance criteria and test plan.
6. Technology-stack decision record.
7. Minimal runnable foundation only after items 1–6 are resolved.

## Completion rule
No claim of engineering completion until runnable functionality, tests, docs, and release-readiness evidence exist.