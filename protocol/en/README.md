# UGP: Universal Gig Protocol

Universal Gig Protocol is an open business protocol for agent-native gig work relationships. It connects enterprise workforce demand, worker intent, and platform fulfillment capability through shared objects, capabilities, policy decisions, mandates, lifecycle states, evidence references, and audit events.

UGP is not a recruiting protocol, not a job posting protocol, and not a private API wrapper. It treats the gig work relationship itself as a first-class protocol object that agents can discover, negotiate, authorize, commit, fulfill, settle, dispute, and improve across systems.

[中文协议入口](../zh/)

## What UGP Standardizes

| Area | UGP Defines |
|---|---|
| Discovery | How agents discover protocol versions, profiles, services, capabilities, schemas, policy requirements, and keys. |
| Objects | How labor state, workforce demand, work opportunities, work contracts, fulfillment records, and settlement credit are represented. |
| Capabilities | How business operations are named, versioned, authorized, audited, and exposed across transports. |
| Policy | How sensitive data, high-risk actions, masking, confirmation, escalation, denial, mandate, and audit semantics work. |
| Lifecycle | How work commitments move from preparation to confirmation, fulfillment, verification, settlement, dispute, or cancellation. |
| Extensibility | How profiles, schemas, and vendor capabilities extend the base protocol without weakening worker protection. |
| Transports | How the same semantics can be bound to REST, MCP, A2A, event streams, or internal RPC. |

## Protocol Layering

![UGP protocol layering](../assets/ugp-diagram-1-protocol-layers.png)

SVG source: [ugp-diagram-1-protocol-layers.svg](../assets/ugp-diagram-1-protocol-layers.svg)

UGP has six layers:

| Layer | Purpose |
|---|---|
| Profile | Declares protocol version, profiles, services, capabilities, schemas, policy, keys, and conformance claims. |
| Object | Defines workforce business objects and supporting evidence, artifacts, mandates, and audit events. |
| Capability | Defines discoverable, authorizable, auditable business operations. |
| Policy | Defines authorization, data classification, masking, confirmation, escalation, denial, and mandate semantics. |
| Lifecycle | Defines work-contract state transitions and fulfillment-to-settlement gates. |
| Transport | Binds the same semantics to REST, MCP, A2A, events, or internal RPC. |

## Core Objects

| Object | Meaning |
|---|---|
| `labor_state` | Worker availability, capability, preference, credential, location, constraint, and credit state. |
| `workforce_demand` | Enterprise or platform demand for roles, shifts, rules, skills, budget, and service-level expectations. |
| `work_opportunity` | A concrete opportunity that a worker agent can discover, compare, apply for, accept, or reject. |
| `work_contract` | A standard commitment object for time, place, compensation, rules, cancellation terms, responsibility, and confirmation. |
| `fulfillment_record` | Attendance, check-in, work hours, task completion, verification, exception, evidence, and dispute facts. |
| `settlement_credit` | Payroll, billing, payment, compensation, penalties, invoice state, reputation, and workforce credit. |

![UGP object lifecycle](../assets/ugp-rfc-object-lifecycle.png)

SVG source: [ugp-rfc-object-lifecycle.svg](../assets/ugp-rfc-object-lifecycle.svg)

## Initial Profiles

| Profile | Scope |
|---|---|
| `org.ugp.core` | Discovery, envelope, object references, policy decisions, mandates, audit events, and common lifecycle semantics. |
| `org.ugp.enterprise_operations` | Enterprise-side and platform workforce management: roster, demand, scheduling, attendance, work hours, payroll, billing, disputes, compliance, invoicing, and rewards or penalties. |
| `org.ugp.worker_opportunity` | worker-side opportunity journey: intent, search, recommendation, acceptance, reminders, attendance claims, income reconciliation, dispute initiation, and credit explanation. |
| `org.ugp.flex_work` | Part-time, temporary, on-demand, shift-based, and project-based work relationships. |
| `org.ugp.settlement` | Payroll, payment, billing, invoicing, compensation, penalties, credit update, and reconciliation. |
| `org.ugp.dispute` | Evidence packaging, claim routing, dispute lifecycle, responsible entity escalation, and resolution records. |

The first benchmark dataset in this repository covers only `org.ugp.enterprise_operations`, the enterprise-side workforce management profile.

Full-time HCM and general employee-lifecycle management are outside UGP's core scope. Implementations may integrate those systems through vendor extensions when a gig-work flow crosses them.

## Discovery and Policy

UGP implementations should publish a profile document at `/.well-known/ugp` or through an equivalent internal registry. The profile declares supported versions, profiles, services, capabilities, schemas, policy decisions, keys, and conformance claims.

Standard capabilities use the `org.ugp.*` namespace. Vendor or platform extensions should use a namespace controlled by the extension owner, such as `com.example.staffing.fast_backup_dispatch`.

High-risk actions must pass through a policy gate before commit. UGP policy returns one of `ALLOW`, `MASK_AND_ALLOW`, `ASK_CONFIRMATION`, `ESCALATE`, or `DENY`.

![UGP capability invocation with policy gate](../assets/ugp-rfc-policy-gate.png)

SVG source: [ugp-rfc-policy-gate.svg](../assets/ugp-rfc-policy-gate.svg)

## UCP Comparison

UCP lets agents complete commerce. UGP lets agents complete gig work relationships.

| Dimension | UCP | UGP |
|---|---|---|
| Relationship | Commerce transaction | Gig work relationship |
| Core objects | Product, merchant, customer, order, payment | Labor state, demand, opportunity, contract, fulfillment, settlement credit |
| Core process | Discover, buy, pay, fulfill order | Demand, match, confirm, arrive, fulfill, settle, preserve credit |
| Risk center | Payment authorization and merchant fulfillment | Identity, credentials, shifts, work hours, wages, compensation, disputes, compliance |

UGP can interoperate with A2A, MCP, REST, AP2, DID/W3C Verifiable Credentials, and UCP. Its center remains gig-work demand, labor state, opportunity, commitment, fulfillment, settlement, dispute, and credit.

## Documents

- [Detailed protocol](./universal-gig-protocol.md)
- [Examples](../examples/)
- [Schemas](../schemas/)
- [Diagrams](../assets/)
- [中文协议](../zh/)

## Benchmark Scope

WorkforceOps Benchmark v1 is the first public benchmark built on UGP. It is grounded in redacted enterprise-side workforce management data and evaluates whether agents can respect authorization, privacy, policy redlines, expected artifacts, and tool-call intent in realistic enterprise operations.

It does not yet cover the full worker opportunity journey, all settlement and credit workflows, or all dispute-handling profiles.
