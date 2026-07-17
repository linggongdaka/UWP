# UGP: Universal Gig Protocol

UGP, the Universal Gig Protocol, is an open business protocol for agent-native gig work relationships.

It gives enterprise agents, worker agents, and platform agents a shared language for discovering workforce capabilities, expressing labor state, matching work opportunities, negotiating commitments, verifying fulfillment, settling work, resolving disputes, and preserving workforce credit across systems.

UGP is not a recruiting protocol, not a job posting protocol, and not a private API wrapper. It treats the gig work relationship itself as a first-class protocol surface that agents can understand, authorize, execute, audit, and improve.

[中文说明](./README.zh-CN.md)

## Why UGP

Gig-work markets are liquidity systems. The right worker, the right work, the right time, the right place, and the right constraints must meet quickly, reliably, and responsibly.

Software has historically split that flow across demand creation, scheduling, signup, onboarding, attendance, work-hour confirmation, training, credentials, payroll, billing, invoicing, disputes, ratings, and credit. In the age of AI agents, without a common protocol, fragmented software becomes fragmented conversation.

UGP is the protocol layer for an agent-native gig-work network:

- Enterprises can express what kind of workforce they need, where, when, under what rules, and with what budget or service-level constraints.
- Workers can express availability, capability, preferences, credentials, commitments, and income expectations.
- Platforms can match, dispatch, verify, settle, audit, and preserve trust across the full work lifecycle.

## What Is In This Repository

| Path | Purpose |
|---|---|
| [protocol/](./protocol/) | The Universal Gig Protocol directory, including English and Chinese specifications, diagrams, examples, and starter schemas. |
| [protocol/en/](./protocol/en/) | English protocol overview and full protocol text. |
| [protocol/zh/](./protocol/zh/) | 中文协议入口与完整中文协议正文。 |
| [protocol/examples/](./protocol/examples/) | Machine-readable examples for discovery, capability responses, policy decisions, and enterprise workforce operations flows. |
| [protocol/schemas/](./protocol/schemas/) | Starter JSON Schemas for UGP profile discovery and message envelopes. |
| [datasets/](./datasets/) | WorkforceOps Benchmark v1 and the redacted data companion package. |

## Protocol Surface

UGP starts from six first-class objects:

| Object | Meaning |
|---|---|
| `labor_state` | Worker availability, capability, preference, credential, location, constraint, and credit state. |
| `workforce_demand` | Enterprise or platform demand for roles, shifts, rules, skills, budget, and service-level expectations. |
| `work_opportunity` | A concrete opportunity that a worker agent can discover, compare, apply for, accept, or reject. |
| `work_contract` | A standard commitment object for time, place, compensation, rules, cancellation terms, responsibility, and confirmation. |
| `fulfillment_record` | Attendance, check-in, work hours, task completion, verification, exception, evidence, and dispute facts. |
| `settlement_credit` | Payroll, billing, payment, compensation, penalties, invoice state, reputation, and workforce credit. |

UGP also defines:

- profile discovery through `/.well-known/ugp` or an equivalent registry;
- capabilities in the `org.ugp.*` namespace;
- policy decisions: `ALLOW`, `MASK_AND_ALLOW`, `ASK_CONFIRMATION`, `ESCALATE`, and `DENY`;
- mandate and audit semantics for high-risk actions;
- work-contract lifecycle states from `prepared` through `settled`, with dispute and cancellation paths;
- schema composition for profiles and extensions;
- transport bindings for REST, MCP, A2A, event streams, and internal RPC.

## Initial Profiles

| Profile | Scope |
|---|---|
| `org.ugp.core` | Discovery, envelopes, policy, mandates, audit, and common lifecycle semantics. |
| `org.ugp.enterprise_operations` | Enterprise-side and platform workforce management: roster, demand, scheduling, attendance, work hours, payroll, billing, disputes, compliance, invoicing, and rewards or penalties. |
| `org.ugp.worker_opportunity` | worker-side opportunity journey: intent, search, recommendation, acceptance, reminders, attendance claims, income reconciliation, dispute initiation, and credit explanation. |
| `org.ugp.flex_work` | Part-time, temporary, on-demand, shift-based, and project-based work relationships. |
| `org.ugp.settlement` | Payroll, payment, billing, invoicing, compensation, penalties, credit update, and reconciliation. |
| `org.ugp.dispute` | Evidence packaging, claim routing, dispute lifecycle, responsible entity escalation, and resolution records. |

Full-time HCM and general employee-lifecycle management are outside UGP's core scope. Implementations may integrate those systems through vendor extensions when a gig-work flow crosses them.

## WorkforceOps Benchmark v1

The dataset in this repository is the first WorkforceOps Benchmark release built on UGP.

Important scope note: v1 covers enterprise-side workforce management only. It focuses on enterprise and platform operations such as roster management, demand and scheduling, attendance and work hours, payroll and fees, training and certificates, disputes and compliance, billing and invoicing, and reward or penalty handling. It does not yet cover the full worker-side opportunity journey or all platform settlement and credit profiles.

Dataset summary:

- 120 cases.
- 80 easy cases and 40 hard cases.
- 78 multi-turn cases and 42 single-turn cases.
- 8 workforce management stages.
- Policy expectations include `ALLOW`, `MASK_AND_ALLOW`, `ASK_CONFIRMATION`, `ESCALATE`, and `DENY`.
- The pack is grounded in a redacted business operations snapshot: worker identity is not carried into adapted cases, entity paths are replaced by synthetic aliases, gold values are limited to store-month aggregate metrics, and the private redaction map is not committed to this repository.

The companion package [WorkforceOps Enterprise Operations Redacted Data Package v1](./datasets/workforceops-enterprise-operations-redacted-data-v1/) contains the public redacted tables and QA grounding needed to reproduce the benchmark context. The package includes a machine-readable manifest and validation artifacts showing that benchmark cases, QA grounding, and public CSV metrics are aligned.

The repository also includes a [calibrated 120-task public release](./datasets/workforceops-benchmark-120-public-v1/) with 43 easy, 48 medium, and 29 hard tasks, together with dataset analysis, four-model comparison results, charts, schemas, checksums, and a standalone validator.

This benchmark is not just a question-answer set. It evaluates whether an agent can respect mandate boundaries, privacy policy, redlines, expected artifacts, and tool-call intent in realistic workforce operations.

## License

This repository is released under the MIT License. See [LICENSE](./LICENSE).
