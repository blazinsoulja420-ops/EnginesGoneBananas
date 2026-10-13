# Creator Pilot Readiness Gate — v0.1

Date: 2026-10-13  
Owner: EnginesGoneBananas product repository  
Status: **REQUIREMENTS / RECOVERY GATE — NOT APPROVAL TO IMPLEMENT OR PUBLISH**  
Starting source revision: `152a06a159d73e06283d14aa57541b63a450a2ae`

## 1. Decision and boundary

The Creator Operating System concept covers research, original media creation, editing, scheduling, brand collaboration, affiliates, digital products, analytics, and governed automation. This repository owns **only an EnginesGoneBananas-specific, non-production pilot definition**. A reusable multi-brand Creator Operating System requires an independent product/ownership decision and explicit versioned interface; it is **not** silently incorporated into this automotive service application.

Preserve the existing service-request/referral workflow and the external Master Mechanic AI dependency. Do not copy diagnostics, ResearchOS, Universal AI or Poindexter internals into this repository. Consumer integrations may later use explicit adapters and approved provider contracts.

This document creates no social account, paid subscription, storefront, posting authorization, secret, executable publisher, or production deployment.

## 2. Evidence register

| Class | Statement |
| --- | --- |
| VERIFIED | At the starting revision, this repo has Phase 1 documents, an isolated Python service/referral module, pytest tests, and CI workflow. |
| VERIFIED | The existing README marks the product as BOOTSTRAP / REQUIREMENTS RECOVERY; it does not claim production readiness. |
| REPORTED | EnginesGoneBananas is the proposed pilot brand; creator research, social content and monetization are requested business goals. |
| INFERRED | An original automotive education/UGC pilot can validate customer demand before implementing generalized automation. This is a hypothesis, not market validation. |
| UNKNOWN | Brand Constitution, current Style Guide, authorized gorilla mascot assets/rights, audience segments, platform accounts, owner/operator identities, marketing consent rules, publishing cadence, editorial authority, and product/UGC commercial offerings. |
| UNKNOWN | Provider API eligibility, current prices and tiers, platform permissions, affiliate acceptance, real revenue potential, creator-store tax/payment requirements and commercial licenses. |
| BLOCKED | Implementing cross-platform publication, automatic paid services, marketing claims and multi-brand tenancy until requirements and authority are verified. |

Historical brand artifacts must be **recovered and reviewed**, not reconstructed by guesswork. If missing, record the absence and prepare a separately approved replacement proposal.

## 3. Narrow candidate pilot

A manual, zero-new-subscription pilot may be scoped after the brand/rights gate:

1. Research automotive how-to questions with publicly accessible trend tools.
2. Maintain a content idea register with date, source, audience, hypothesis, and use rights.
3. Produce original footage, scripts, captions, and thumbnails.
4. Review accuracy, vehicle/repair safety, originality, commercial media rights, privacy, claims, and disclosure obligations.
5. Have an authorized human publish on a selected owned channel.
6. Record each post's native ID and measurement window.
7. Test **one** revenue path (UGC portfolio, disclosed affiliate link, or owned digital item) after legal/platform eligibility is checked.
8. Calculate net profit after actual fees, production costs, and refunds.

Suggested tools from the research inventory (not approved vendor dependencies): Google Trends and TikTok Creative Center for discovery; CapCut/DaVinci Resolve/Canva for creation; Buffer/Metricool for optional scheduling; Make/n8n for later automation; JoinBrands/Collabstr for optional UGC; Payhip/Fourthwall for optional products. Verify all pricing, Terms of Service, account eligibility, privacy, rights and geographic support at onboarding. Free-tier presence does **not** imply a commercial license.

## 4. Required recovery / readiness gate

Before implementing a creator feature or automating a publishing action, collect and review:

- [ ] Existing EnginesGoneBananas Master Prompt / Brand Constitution and decision authority; document provenance and version.
- [ ] Existing Brand Style Guide, logos and mascot assets; identify rights holders and authorized uses.
- [ ] Specific audience, content pillars, claims standard, editorial reviewer, publish approver and channel ownership.
- [ ] Written opt-in/permission for images, testimonials and identifiable persons, where applicable.
- [ ] Candidate platform accounts, official API capabilities, rate limits, revocation flow and current provider agreements.
- [ ] Publishing policy: sponsorship/affiliate disclosures, music/voice/image licenses, technical safety review and incident response.
- [ ] Maximum **additional recurring budget of $0** for pilot by default; any spend requires a separately recorded approval.
- [ ] Single revenue experiment with eligibility, payment/refund policies and a basic accounting plan.
- [ ] Data retention, export, backup, deletion and secrets-handling decisions appropriate to the selected providers.
- [ ] Baseline metric definitions and a manual runbook for the full research-to-measurement path.
- [ ] Architectural decision about whether/when reusable multi-brand software belongs in its own repository/service.

Until these boxes have evidence, the implementation/publishing gates remain CLOSED. A document or green CI cannot open them automatically.

## 5. Candidate content state machine (design only)

`IDEA -> DRAFT -> IN_REVIEW -> APPROVED -> SCHEDULED -> PUBLISHED -> MEASURED`

Allowed alternate outcomes: `REJECTED`, `CANCELED`, `PUBLISH_FAILED`. No transition to `APPROVED` without an identified human reviewer; no transition to `SCHEDULED` or `PUBLISHED` without channel-level publishing authority. Revisions after approval invalidate that approval. Invalid state transitions must fail closed.

Future adapter requirements:

- Do not store tokens, secrets, personal data, or payment credentials in repository files, logs or prompts.
- Provider adapters must be separated from domain rules and individually revocable; support per-account credential isolation and least privilege.
- Guard against duplicate publication with provider IDs/idempotency keys, retries with backoff, and explicit reconciliation.
- Record immutable-enough audit references: idea ID, asset hashes/rights, review decision, approver, scheduled time, provider response, post URL/ID and failure reason.
- Never bypass CAPTCHA, rate limits, service restrictions, paywalls or platform permissions.
- No unattended AI-controlled spending, financial commitments, unapproved publication, deceptive engagement, or claims of guaranteed earnings.

## 6. Acceptance and verification plan

**Gate A — Baseline preservation (current PR):**

- Only this prospective document is added; existing domain code, tests, architecture and workflow are unchanged.
- A review confirms accurate VERIFIED/UNKNOWN/BLOCKED classification and project isolation.
- GitHub Actions tests succeed for the exact PR head and merged main; absence of runs or permissions is recorded honestly.
- Merge records commit SHA and run links; no marketing feature is described as implemented.

**Gate B — Requirements recovery (future separately authorized work):**

- Every recovery checklist item is resolved with an evidence link, an explicit non-applicability reason, or remains visibly BLOCKED.
- A single pilot audience, channel, permission model, content/revenue format, success criteria, and stop conditions are decided.
- Provider costs/licenses are current, and the user separately authorizes any new spend, account access or publication.

**Gate C — Offline prototype (future):**

- Build an isolated, provider-neutral content-idea/approval registry with deterministic state transitions and unit tests.
- Prove rejection of unauthorized publication and duplicate job submission in local tests.
- Keep all external publishing and financial APIs mocked until a further release gate.

**Gate D — Live pilot (future):**

- Approved and permissioned publishing adapter with revocable credentials, observability and rollback/manual disable.
- A supervised end-to-end post, timestamped analytics evidence, and accurate cost/revenue ledger.
- Separate production authorization, never inherited from this docs PR.

## 7. Next safe action

Recover or locate authoritative brand materials and approvals, then open a new bounded requirements PR to populate the pilot decisions. Do **not** turn on an automatic posting service or claim a completed creator application on the strength of this gate document.
