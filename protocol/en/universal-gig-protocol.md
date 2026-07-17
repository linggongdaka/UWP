# UGP: Universal Gig Protocol

## Universal Gig Protocol for Agent-Native Gig Work Relationships

## Abstract

UGP, the Universal Gig Protocol, is an open business protocol for the age of AI agents. It gives enterprise agents, worker agents, and platform agents a shared way to discover workforce capabilities, express workforce demand, represent worker intent, match opportunities, form commitments, verify fulfillment, settle work, resolve disputes, and preserve workforce credit across systems.

UGP does not try to make agents "chat about work." It defines the objects, capabilities, authorization semantics, lifecycle states, evidence references, policy decisions, and audit events that let agents operate inside real gig-work workflows.

UGP covers part-time, temporary, on-demand, shift-based, outsourced-service, staffing, and project-based gig work arrangements. Full-time HCM and general employee-lifecycle management are outside the core protocol scope. UGP does not replace legal classification. Employment status, labor dispatch status, outsourcing responsibility, tax treatment, insurance responsibility, social security responsibility, worker protection rules, and local compliance obligations must be resolved by the applicable jurisdiction, contracts, business rules, and responsible entities.

## Table of Contents

1. [Conventions](#1-conventions)
2. [Motivation](#2-motivation)
3. [Scope](#3-scope)
4. [Architecture](#4-architecture)
5. [Roles](#5-roles)
6. [Discovery, Governance, and Negotiation](#6-discovery-governance-and-negotiation)
7. [Profiles and Conformance Levels](#7-profiles-and-conformance-levels)
8. [Core Object Model](#8-core-object-model)
9. [Capability Model](#9-capability-model)
10. [Policy, Mandates, and Audit](#10-policy-mandates-and-audit)
11. [Message Envelope and Response Contract](#11-message-envelope-and-response-contract)
12. [Work Contract Lifecycle](#12-work-contract-lifecycle)
13. [Schema Composition and Extensibility](#13-schema-composition-and-extensibility)
14. [Transport Bindings](#14-transport-bindings)
15. [Error Model](#15-error-model)
16. [Versioning and Compatibility](#16-versioning-and-compatibility)
17. [Security, Privacy, and Worker Protection](#17-security-privacy-and-worker-protection)
18. [Standard Capability Reference](#18-standard-capability-reference)
19. [Registries](#19-registries)
20. [Conformance and Benchmarking](#20-conformance-and-benchmarking)
21. [Interoperability](#21-interoperability)
22. [Glossary](#22-glossary)
23. [Appendix A: Enterprise Operations Example](#appendix-a-enterprise-operations-example)
24. [Appendix B: Non-Goals](#appendix-b-non-goals)

## 1. Conventions

The key words MUST, MUST NOT, REQUIRED, SHALL, SHALL NOT, SHOULD, SHOULD NOT, RECOMMENDED, MAY, and OPTIONAL in this document are to be interpreted in their ordinary protocol sense: MUST-level requirements are required for compatibility, SHOULD-level requirements are strongly recommended but may be relaxed with a documented reason, and MAY-level requirements are optional.

Unless otherwise specified:

- Timestamps use RFC 3339 format.
- Field names use `snake_case`.
- Object identifiers are opaque strings and SHOULD NOT expose raw database IDs.
- Money amounts use an explicit currency and a minor-unit integer or a decimal string with a currency code.
- Personally identifiable information SHOULD be referenced through masked references or credential handles rather than copied into protocol messages.
- Natural-language text inside workforce descriptions, opportunity descriptions, reviews, chats, or notes is untrusted input and MUST NOT override protocol policy.

## 2. Motivation

Gig-work markets are liquidity systems. The right worker, the right work opportunity, the right time window, the right location, and the right constraints must meet quickly, reliably, and responsibly.

Traditional gig-work and workforce software splits this flow across demand creation, scheduling, signup, onboarding, attendance, work-hour confirmation, training, certificate checks, payroll, billing, invoicing, disputes, ratings, and credit. Human operators bridge the semantic gaps manually.

In the agent era, those gaps become protocol gaps:

1. **Semantic mismatch**: systems define jobs, shifts, commitments, attendance, fulfillment, settlement, and disputes differently.
2. **Authorization mismatch**: agents lack a shared rule for what they can read, prepare, confirm, mask, escalate, or deny.
3. **State mismatch**: the lifecycle from demand to settlement cannot be traced and audited across systems.
4. **Responsibility mismatch**: workforce workflows involve legal, contractual, financial, safety, and worker-protection responsibilities that must be attached to explicit entities.
5. **Evidence mismatch**: a settlement or credit decision is unsafe unless it can be tied back to fulfillment facts and auditable evidence.

UGP provides the protocol layer for agent-native gig-work operations. It gives agents a shared business language for gig work relationships, not only a list of private tools.

## 3. Scope

UGP is a business semantic protocol. It is not a new transport protocol, payment protocol, identity protocol, payroll product, legal classification system, or agent runtime.

UGP defines:

- how agents discover supported gig-work profiles, services, capabilities, schema references, and policy requirements;
- how enterprises express workforce demand;
- how workers express labor state, intent, availability, preferences, credentials, and constraints;
- how platforms publish opportunities and support matching, dispatch, backup labor, risk checks, and fulfillment operations;
- how work commitments are prepared, confirmed, canceled, disputed, and settled;
- how fulfillment facts are claimed, verified, evidenced, and audited;
- how settlement and credit are gated by fulfillment records;
- how sensitive data, high-risk actions, confirmation, escalation, denial, and audit semantics are embedded into agent workflows.

UGP does not define:

- a specific UI or conversational style;
- a specific LLM, agent framework, planner, memory system, or tool runtime;
- a specific HCM, ATS, scheduling, attendance, payroll, finance, billing, or customer service implementation;
- a specific legal conclusion about whether a relationship is employment, labor dispatch, outsourcing, contractor work, or platform service;
- a requirement that implementations expose production data publicly.

## 4. Architecture

![UGP architecture overview](../assets/ugp-rfc-architecture-overview.png)

SVG source: [ugp-rfc-architecture-overview.svg](../assets/ugp-rfc-architecture-overview.svg)

UGP is organized into six layers.

| Layer | Purpose |
|---|---|
| Profile layer | Declares supported protocol versions, scenario profiles, services, capabilities, policy requirements, schema references, endpoints, keys, and conformance claims. |
| Object layer | Defines `labor_state`, `workforce_demand`, `work_opportunity`, `work_contract`, `fulfillment_record`, `settlement_credit`, and supporting objects. |
| Capability layer | Defines discoverable business capabilities for discovery, demand, opportunity, contract, fulfillment, settlement, dispute, credit, and audit operations. |
| Policy layer | Defines authorization, data classification, confirmation, masking, escalation, denial, mandate, and audit semantics. |
| Lifecycle layer | Defines work-contract state transitions and fulfillment-to-settlement gates. |
| Transport layer | Binds the same semantics to REST, MCP, A2A, event streams, internal RPC, or other transports. |

UGP intentionally separates protocol semantics from transport shape. A REST endpoint, MCP tool, A2A task, or event message can all be UGP-compatible if they preserve the same object, capability, policy, lifecycle, and audit semantics.

## 5. Roles

| Role | Responsibility |
|---|---|
| Enterprise Agent | Express workforce demand, inspect candidate or supply state, confirm workers, verify fulfillment, handle exceptions, and request settlement or dispute actions. |
| Worker Agent | Express work intent, discover opportunities, compare terms, confirm commitments, fulfill work, check income, raise disputes, and maintain credit. |
| Platform Agent | Match supply and demand, dispatch workers, coordinate backup labor, assess risk, advance fulfillment state, validate settlement, route disputes, and preserve trust. |
| Workforce Platform | Provide system facts and capabilities such as jobs, schedules, attendance, work hours, payroll, billing, disputes, reviews, and credit. |
| Responsible Entity | Carry legal, contractual, tax, insurance, work injury, service delivery, financial, or compliance responsibility for a specific action or contract. |
| Human Controller | Confirm, approve, reject, or assume responsibility for high-risk actions. |
| Auditor or Regulator | Inspect evidence, audit events, policy decisions, mandates, and state transitions where legally or contractually allowed. |

One real organization can play multiple roles. A platform may act as both workforce platform and responsible entity. An enterprise system may publish demand and also verify fulfillment. Each session MUST declare the active role and responsibility anchor for high-risk actions.

## 6. Discovery, Governance, and Negotiation

UGP uses profile discovery and capability negotiation so that agents can interoperate without prior private integration.

### 6.1 Well-Known Profile

A UGP server SHOULD publish a profile document at:

```text
GET /.well-known/ugp
```

The profile document is JSON. It declares supported protocol versions, services, capabilities, profiles, schema references, endpoints, public keys, policy requirements, and conformance claims.

Example:

```json
{
  "ugp_version": "2026-07",
  "publisher": {
    "role": "workforce_platform",
    "entity_ref": "org_example_platform"
  },
  "supported_versions": {
    "2026-07": "https://platform.example.com/.well-known/ugp"
  },
  "profiles": [
    "org.ugp.core",
    "org.ugp.enterprise_operations"
  ],
  "services": {
    "org.ugp.workforce": [
      {
        "version": "2026-07-17",
        "transport": "rest",
        "spec": "https://platform.example.com/specs/ugp/workforce",
        "schema": "https://platform.example.com/schemas/ugp/workforce.openapi.json",
        "endpoint": "https://platform.example.com/api/ugp"
      }
    ]
  },
  "capabilities": {
    "org.ugp.demand.create": [
      {
        "version": "2026-07-17",
        "profile": "org.ugp.enterprise_operations",
        "spec": "https://platform.example.com/specs/ugp/capabilities/demand.create",
        "schema": "https://platform.example.com/schemas/ugp/demand.create.schema.json",
        "side_effect": "data_write_prepare",
        "risk_level": "R3",
        "requires_mandate": "demand_mandate"
      }
    ]
  },
  "policy": {
    "data_classification": ["public", "internal", "confidential", "sensitive", "restricted"],
    "decisions": ["ALLOW", "MASK_AND_ALLOW", "ASK_CONFIRMATION", "ESCALATE", "DENY"]
  },
  "keys": [
    {
      "kid": "ugp-key-2026-07",
      "jwk_url": "https://platform.example.com/.well-known/jwks.json"
    }
  ],
  "conformance": ["org.ugp.core.server", "org.ugp.enterprise_operations.server"]
}
```

Private or internal deployments MAY use a registry, signed configuration bundle, MCP resource, or A2A Agent Card instead of a public well-known URL. The same profile fields SHOULD be preserved.

### 6.2 Namespace Governance

UGP capability and service names SHOULD use reverse-domain naming:

```text
{reverse-domain}.{service-or-domain}.{capability}
```

Examples:

| Name | Authority | Meaning |
|---|---|---|
| `org.ugp.demand.create` | UGP | Prepare or create workforce demand. |
| `org.ugp.contract.worker_accept.confirm` | UGP | Confirm worker acceptance. |
| `org.ugp.settlement.prepare` | UGP | Prepare settlement or adjustment. |
| `com.example.staffing.fast_backup_dispatch` | example.com | Vendor-specific backup dispatch extension. |

The `org.ugp.*` namespace is reserved for standard UGP capabilities. Vendors, platforms, enterprises, and research groups SHOULD use namespaces under their own controlled domains.

Capability declarations SHOULD include `spec` and `schema` URLs. The origin of those URLs SHOULD match the namespace authority unless the declaration is part of a signed internal registry.

### 6.3 Services

A service defines an API surface for a workforce domain. Services may expose operations, tools, events, or agent tasks.

| Field | Required | Meaning |
|---|---|---|
| `version` | yes | Service definition version. |
| `transport` | yes | `rest`, `mcp`, `a2a`, `event`, `rpc`, or another declared binding. |
| `spec` | yes | Human-readable service specification. |
| `schema` | recommended | OpenAPI, OpenRPC, JSON Schema, Agent Card, AsyncAPI, or equivalent schema. |
| `endpoint` | transport-dependent | Endpoint or discovery URL for this binding. |
| `config` | optional | Service-specific configuration. |

Transport definitions SHOULD be thin. They should reference UGP base schemas and active extension schemas rather than redefine business objects inline.

### 6.4 Capability Negotiation

UGP uses a server-selects negotiation model:

1. The client discovers the server profile.
2. The client sends requested protocol version, profiles, capabilities, and optional extensions.
3. The server computes the intersection between the client's request and its supported capabilities.
4. The server selects active capabilities, applies policy, and returns the active set in the response.
5. If a required profile or capability cannot be satisfied, the server returns a structured error and MUST NOT silently ignore the unsupported requirement.

Request example:

```json
{
  "ugp_version": "2026-07",
  "required_profiles": ["org.ugp.core", "org.ugp.enterprise_operations"],
  "requested_capabilities": [
    "org.ugp.demand.create",
    "org.ugp.matching.run",
    "org.ugp.contract.prepare_confirm"
  ],
  "requested_extensions": [
    "com.example.staffing.fast_backup_dispatch"
  ]
}
```

Response capability declaration:

```json
{
  "ugp": {
    "version": "2026-07",
    "active_profiles": ["org.ugp.core", "org.ugp.enterprise_operations"],
    "active_capabilities": [
      "org.ugp.demand.create",
      "org.ugp.matching.run",
      "org.ugp.contract.prepare_confirm"
    ],
    "inactive_capabilities": [
      {
        "name": "com.example.staffing.fast_backup_dispatch",
        "reason": "capability_not_available"
      }
    ]
  }
}
```

## 7. Profiles and Conformance Levels

A profile is a scenario-specific bundle of objects, capabilities, policies, lifecycle rules, and schema constraints.

Initial UGP profiles:

| Profile | Scope |
|---|---|
| `org.ugp.core` | Discovery, envelope, object references, policy decisions, mandates, audit events, and common lifecycle semantics. |
| `org.ugp.enterprise_operations` | Enterprise-side and platform workforce management: roster, demand, scheduling, attendance, work hours, payroll, billing, disputes, compliance, invoicing, and reward or penalty handling. |
| `org.ugp.worker_opportunity` | worker-side opportunity journey: intent, search, recommendation, acceptance, reminders, attendance claims, income reconciliation, dispute initiation, and credit explanation. |
| `org.ugp.flex_work` | Part-time, temporary, on-demand, shift-based, and project-based work relationships. |
| `org.ugp.settlement` | Payroll, payment, billing, invoicing, compensation, penalties, credit update, and reconciliation. |
| `org.ugp.dispute` | Evidence packaging, claim routing, dispute lifecycle, responsible entity escalation, and resolution records. |

The first benchmark dataset in this repository covers only `org.ugp.enterprise_operations`, the enterprise-side workforce management profile. It does not yet cover the full worker opportunity journey or all settlement and dispute profiles.

Full-time HCM and general employee-lifecycle management are not standard UGP profiles. Implementations may integrate those systems through vendor extensions when a gig-work flow crosses them.

Conformance claims are declared as strings:

| Claim | Meaning |
|---|---|
| `org.ugp.core.client` | Can read profiles, send UGP envelopes, negotiate capabilities, and process policy-aware responses. |
| `org.ugp.core.server` | Publishes a profile, validates envelopes, returns active capabilities, emits policy decisions, and records audit events. |
| `org.ugp.enterprise_operations.client` | Can create or inspect enterprise-side workforce operations requests and interpret enterprise operations responses. |
| `org.ugp.enterprise_operations.server` | Supports the required enterprise-side workforce operations object and capability subset. |
| `org.ugp.worker_opportunity.client` | Can express worker intent, inspect work opportunities, and prepare worker confirmations. |
| `org.ugp.settlement.server` | Gates settlement by fulfillment evidence, mandate state, policy decision, and responsible entity. |

An implementation MUST NOT claim a profile if it cannot enforce the corresponding policy and lifecycle rules.

## 8. Core Object Model

![UGP object lifecycle](../assets/ugp-rfc-object-lifecycle.png)

SVG source: [ugp-rfc-object-lifecycle.svg](../assets/ugp-rfc-object-lifecycle.svg)

UGP starts from six first-class protocol objects and several supporting objects.

### 8.1 Common Fields

All first-class objects SHOULD include:

| Field | Meaning |
|---|---|
| `object_type` | One of the registered UGP object types. |
| `id` | Opaque protocol object identifier. |
| `version` | Object version or event version. |
| `created_at` | RFC 3339 timestamp. |
| `updated_at` | RFC 3339 timestamp when applicable. |
| `source_system` | System that produced the object. |
| `profile` | Profile under which the object is interpreted. |
| `responsible_entity` | Entity responsible for this object or action when applicable. |
| `policy_tags` | Data classification, risk, jurisdiction, and handling tags. |
| `evidence_refs` | Evidence references that support this object. |
| `audit_refs` | Audit events related to this object. |

### 8.2 `labor_state`

The worker's work-ready state at a point in time or within a time window. It can include identity references, capability, credentials, availability, preferences, location constraints, work restrictions, historical fulfillment summary, and credit signals.

Minimum useful fields:

- `worker_ref`
- `availability`
- `skills`
- `credentials`
- `preferences`
- `constraints`
- `location_scope`
- `credit_summary`
- `consent`

Implementations SHOULD use credential handles and verification results instead of raw credential images or full personal identifiers.

### 8.3 `workforce_demand`

The enterprise or platform demand for labor. It includes time, place, headcount, role, skills, credentials, compensation, budget, rules, and service-level expectations.

Minimum useful fields:

- `demand_ref`
- `enterprise_ref`
- `site_ref`
- `role`
- `headcount`
- `time_window`
- `skills`
- `credential_requirements`
- `compensation`
- `budget`
- `rules`
- `service_level`
- `risk_constraints`

### 8.4 `work_opportunity`

A concrete work opportunity that a worker agent can discover, compare, apply for, accept, reject, or negotiate.

Minimum useful fields:

- `opportunity_ref`
- `demand_ref`
- `site_ref`
- `role`
- `time_window`
- `compensation`
- `requirements`
- `cancellation_terms`
- `fit_explanation`
- `application_or_acceptance_path`
- `expires_at`

### 8.5 `work_contract`

The standard commitment object for a work relationship. It records the confirmed parties, time, place, role, compensation, rules, cancellation terms, responsibility anchor, and linked legal or platform documents when needed.

Minimum useful fields:

- `contract_ref`
- `status`
- `parties`
- `responsible_entity`
- `role`
- `time_window`
- `site_ref`
- `compensation`
- `rules`
- `mandates`
- `cancellation_terms`
- `linked_documents`
- `audit_refs`

### 8.6 `fulfillment_record`

The factual record of work fulfillment. It distinguishes worker-side claims, enterprise-side verification, platform-side evidence, exceptions, disputes, and final confirmation.

Minimum useful fields:

- `fulfillment_ref`
- `contract_ref`
- `worker_claim`
- `business_verification`
- `platform_evidence`
- `work_hours`
- `quality_or_task_result`
- `exceptions`
- `dispute_ref`
- `verification_status`

### 8.7 `settlement_credit`

The settlement and credit record derived from fulfillment. It covers payroll, payment, billing, invoices, compensation, penalties, dispute outcomes, ratings, and workforce credit.

Minimum useful fields:

- `settlement_ref`
- `contract_ref`
- `fulfillment_ref`
- `settlement_status`
- `payroll_items`
- `billing_items`
- `adjustments`
- `invoice_refs`
- `payment_refs`
- `credit_updates`
- `policy_decision`
- `mandate_refs`

### 8.8 Supporting Objects

| Object | Meaning |
|---|---|
| `evidence_ref` | Pointer to attendance, geofence, image, signature, check-in, certificate, log, document, message, or other evidence. |
| `artifact` | Human-readable or machine-readable output produced by an agent, such as a confirmation card, evidence packet, settlement explanation, or dispute summary. |
| `audit_event` | Immutable or append-only event recording who did what, under which policy decision, with which mandate, at what time. |
| `mandate` | Auditable confirmation or authorization record tied to a principal, action, object, scope, expiration, and responsible entity. |
| `policy_decision` | Protocol decision that allows, masks, asks for confirmation, escalates, or denies an action. |

## 9. Capability Model

Capabilities are discoverable, authorizable, auditable business operations. A capability is not the same as an internal raw API.

Capability declaration fields:

| Field | Required | Meaning |
|---|---|---|
| `name` | yes | Stable capability name. |
| `version` | yes | Capability definition version. |
| `profile` | yes | Profile under which the capability is valid. |
| `spec` | yes | Human-readable capability specification. |
| `schema` | yes | Input and output schema reference. |
| `description` | recommended | Short capability description. |
| `side_effect` | yes | `data_read`, `data_write_prepare`, `data_write_commit`, or `external_call`. |
| `risk_level` | yes | `R0` through `R5`. |
| `required_scope` | recommended | Required authorization scopes. |
| `requires_mandate` | conditional | Required mandate type for high-risk actions. |
| `extends` | optional | Parent capability or capabilities for extensions. |
| `audit` | recommended | Audit event requirements. |

Side-effect levels:

| Side Effect | Meaning |
|---|---|
| `data_read` | Read-only query that does not alter business state. |
| `data_write_prepare` | Generates a proposal, confirmation item, evidence packet, or pending task. |
| `data_write_commit` | Commits a business state change. |
| `external_call` | Triggers external notification, payment, invoicing, legal, contract, or fund movement. |

Risk levels:

| Risk | Meaning |
|---|---|
| `R0` | Static discovery or profile metadata. |
| `R1` | Low-risk explanatory content. |
| `R2` | Routine business query. |
| `R3` | Sensitive query or preparation step. |
| `R4` | High-risk confirmation, wage, work-hour, personal data, negative credit, or write action. |
| `R5` | Dispute, compensation, liability, legal, funds, or external irreversible action. |

R4 and R5 capabilities MUST produce audit events. Commit actions at R4 or R5 MUST bind to a mandate or human controller.

## 10. Policy, Mandates, and Audit

![UGP capability invocation with policy gate](../assets/ugp-rfc-policy-gate.png)

SVG source: [ugp-rfc-policy-gate.svg](../assets/ugp-rfc-policy-gate.svg)

UGP embeds policy into the protocol path. Agents MUST NOT jump from natural language directly to irreversible business changes.

Policy decisions:

| Decision | Meaning |
|---|---|
| `ALLOW` | The action may proceed. |
| `MASK_AND_ALLOW` | The action may proceed after sensitive fields are masked or omitted. |
| `ASK_CONFIRMATION` | A human, principal, or authorized controller must confirm before commit. |
| `ESCALATE` | The action must be escalated to a responsible human or control function. |
| `DENY` | The action must not proceed. |

Data classification:

| Class | Examples | Default Handling |
|---|---|---|
| `public` | Public opportunity information. | Can be returned. |
| `internal` | Store rules, roster summaries, schedule overview. | Can be returned within scope. |
| `confidential` | Roster details, work hours, billing, payroll status. | Requires role and scope checks. |
| `sensitive` | Phone, ID number, bank card, personal wage details. | Mask by default or deny. |
| `restricted` | Legal liability, compensation, dispute decisions, cross-tenant data. | Escalate or deny by default. |

Mandate types:

| Mandate | Confirming Principal | Use |
|---|---|---|
| `demand_mandate` | Enterprise user or authorized manager. | Authorize demand creation, publishing, scheduling, or backup dispatch. |
| `worker_intent_mandate` | Worker or worker agent under consent. | Express work intent, availability, and preferences. |
| `worker_acceptance` | Worker. | Confirm work acceptance, onboarding, shift acceptance, or terms. |
| `business_confirmation` | Enterprise or site controller. | Confirm hiring, attendance, work hours, fulfillment, or exception outcome. |
| `settlement_mandate` | Authorized finance, platform, or responsible entity. | Confirm payment, adjustment, deduction, compensation, or credit update. |
| `dispute_mandate` | Compliance, arbitration, responsible person, or dispute handler. | Confirm dispute path, evidence package, or resolution boundary. |

A mandate MUST include principal, action, object, scope, timestamp, expiration or revocation semantics, policy decision, and audit reference.

## 11. Message Envelope and Response Contract

All UGP messages SHOULD use a common envelope when crossing system boundaries.

```json
{
  "ugp_version": "2026-07",
  "msg_id": "msg_01HXEXAMPLE",
  "msg_type": "workforce_demand",
  "ts": "2026-07-17T10:00:00+08:00",
  "from": {
    "role": "enterprise_agent",
    "agent_id": "agent_ent_001"
  },
  "to": {
    "role": "platform_agent",
    "agent_id": "agent_platform_001"
  },
  "profile": "org.ugp.enterprise_operations",
  "capabilities": {
    "requested": ["org.ugp.demand.create"],
    "required": ["org.ugp.policy.evaluate"]
  },
  "body": {},
  "sig": "optional-detached-signature"
}
```

Responses SHOULD include:

- `ugp.version`
- `ugp.active_profiles`
- `ugp.active_capabilities`
- `policy_decision`
- `result` or `artifact`
- `audit_event` or `audit_ref` when audit is required
- `mandate_request` when confirmation is required
- `error` when the request cannot be safely fulfilled

Agent final responses MUST remain consistent with tool results, policy decisions, active capabilities, and object state. An agent MUST NOT claim that a high-risk action has been completed if the protocol response only prepared a mandate or pending confirmation.

## 12. Work Contract Lifecycle

A compatible `work_contract` lifecycle includes the following state machine or a compatible subset.

```text
prepared
  -> proposed
  -> accepted
  -> confirmed
  -> scheduled
  -> in_progress
  -> worker_claimed
  -> verified
  -> settlement_pending
  -> settled
```

Exceptional states include `needs_info`, `confirmation_required`, `disputed`, `canceled`, `voided`, and `blocked`.

Required gates:

- A contract MUST NOT enter `confirmed` without worker acceptance or an equivalent mandate when worker acceptance is required.
- A contract MUST NOT enter `settlement_pending` without a responsible entity.
- A contract MUST NOT enter `settled` without fulfillment evidence and settlement policy approval.
- A disputed contract MUST NOT produce negative worker credit without a dispute path, evidence, and responsible confirmation.
- A canceled or voided contract MUST preserve audit history.

## 13. Schema Composition and Extensibility

UGP schemas SHOULD be JSON Schema compatible. Transport definitions such as OpenAPI, OpenRPC, MCP tool schemas, and A2A task schemas SHOULD reference UGP base schemas rather than redefine all business fields inline.

### 13.1 Base and Extension Schemas

Each standard object has a base schema. A profile can constrain or extend the base schema. A capability can reference the relevant input and output schema. A vendor extension can add fields or constraints when it declares its parent capability or object.

Extension schema pattern:

```json
{
  "$id": "https://example.com/schemas/ugp/extensions/fast-backup-dispatch.schema.json",
  "$defs": {
    "org.ugp.demand.create": {
      "title": "Demand Create with Fast Backup Dispatch",
      "allOf": [
        { "$ref": "https://ugp.example.org/schemas/demand.create.schema.json" },
        {
          "type": "object",
          "properties": {
            "backup_dispatch_window_minutes": {
              "type": "integer",
              "minimum": 5
            }
          }
        }
      ]
    }
  }
}
```

Requirements:

- An extension that declares `extends` SHOULD provide a `$defs` entry for each parent.
- The `$defs` key SHOULD match the parent object or capability name.
- Clients SHOULD compose base schemas and active extension schemas before validating tool inputs and results.
- Servers MUST validate incoming payloads against the selected protocol version, active profile, and active capabilities.

### 13.2 Extension Rules

Extensions MAY add fields, add constraints, define new evidence types, introduce new capabilities, or refine policy requirements.

Extensions MUST NOT:

- remove required base fields;
- silently change the meaning of standard fields;
- bypass policy, mandate, or audit requirements;
- weaken worker protection requirements;
- claim an `org.ugp.*` name unless accepted as a standard UGP capability.

## 14. Transport Bindings

UGP can be carried over multiple transports.

### 14.1 REST

REST bindings SHOULD use HTTPS. Requests SHOULD include:

```text
UGP-Version: 2026-07
UGP-Profile: org.ugp.enterprise_operations
UGP-Request-Id: req_01HXEXAMPLE
UGP-Capabilities: org.ugp.demand.create,org.ugp.policy.evaluate
```

REST responses SHOULD include active capabilities, policy decisions, and audit references in the JSON body. HTTP status codes indicate transport-level success or failure; the UGP error object indicates protocol-level failure.

### 14.2 MCP

MCP bindings expose UGP capabilities as tools. Tool names SHOULD preserve the capability name or a reversible mapping.

Example mapping:

| UGP Capability | MCP Tool |
|---|---|
| `org.ugp.discovery.profile` | `ugp.discovery.profile` |
| `org.ugp.demand.create` | `ugp.demand.create` |
| `org.ugp.policy.evaluate` | `ugp.policy.evaluate` |
| `org.ugp.mandate.confirm` | `ugp.mandate.confirm` |

MCP tool results MUST include policy outcomes for sensitive and high-risk actions.

### 14.3 A2A

A2A bindings MAY advertise UGP profiles and capabilities in Agent Cards. A2A tasks can carry UGP envelopes as task inputs and outputs. Long-running workforce flows SHOULD expose task status and audit references.

### 14.4 Event Streams

Event streams MAY publish UGP lifecycle events such as `work_contract.confirmed`, `fulfillment_record.verified`, `settlement_credit.prepared`, or `dispute_case.opened`. Events MUST carry object references, timestamps, policy tags, and audit references.

### 14.5 Internal RPC

Internal RPC or message buses MAY be used inside a trusted environment. The implementation remains UGP-compatible only if it preserves protocol objects, policy decisions, mandates, audit events, and lifecycle gates.

## 15. Error Model

UGP errors are structured objects.

```json
{
  "error": {
    "code": "ugp.mandate_required",
    "message": "Settlement adjustment requires a settlement mandate.",
    "details": {
      "required_mandate": "settlement_mandate",
      "risk_level": "R4"
    },
    "continue_url": "https://platform.example.com/confirm/mandate_123"
  }
}
```

Initial error codes:

| Code | Meaning |
|---|---|
| `ugp.unsupported_version` | Requested protocol version is not supported. |
| `ugp.unsupported_profile` | Required profile is not supported. |
| `ugp.capability_not_available` | Requested capability is unavailable or inactive. |
| `ugp.schema_validation_failed` | Payload does not match selected schema. |
| `ugp.policy_denied` | Policy returned `DENY`. |
| `ugp.masking_applied` | Sensitive fields were masked before returning the result. |
| `ugp.mandate_required` | A mandate is required before commit. |
| `ugp.confirmation_required` | Human or principal confirmation is required. |
| `ugp.responsibility_unresolved` | Responsible entity is missing or invalid. |
| `ugp.fulfillment_evidence_missing` | Fulfillment evidence is required before settlement or credit action. |
| `ugp.dispute_active` | Active dispute blocks settlement or negative credit. |
| `ugp.scope_violation` | Request exceeds role, tenant, worker, site, or data scope. |

When the response includes a `continue_url`, clients MAY use it to route confirmation, escalation, dispute handling, or missing-information collection. Clients MUST NOT treat `continue_url` as proof that the requested action has already been committed.

## 16. Versioning and Compatibility

UGP uses independent versioning for the protocol, profiles, services, capabilities, schemas, and extensions.

| Entity | Example | Meaning |
|---|---|---|
| Protocol version | `2026-07` | Top-level UGP semantic version. |
| Profile version | `org.ugp.enterprise_operations@2026-07-17` | Scenario profile version. |
| Capability version | `org.ugp.demand.create@2026-07-17` | Capability definition version. |
| Schema version | Schema `$id` or date | Schema version for validation. |
| Extension version | `com.example.staffing.fast_backup_dispatch@2026-07-17` | Vendor extension version. |

Backwards-compatible changes MAY:

- add optional fields;
- add new capabilities;
- add new policy reason codes;
- add new data classes with conservative default handling;
- add new error details while preserving the base error code.

Breaking changes include:

- removing required fields;
- changing the meaning of a standard field;
- weakening mandate or audit requirements;
- allowing settlement without fulfillment evidence;
- changing state transition semantics in a way that invalidates existing clients;
- treating sensitive data as less protected by default.

Servers SHOULD advertise supported versions in the well-known profile. Clients SHOULD request the highest mutually supported version.

## 17. Security, Privacy, and Worker Protection

UGP treats security and worker protection as protocol concerns.

| Threat | Description | Mitigation |
|---|---|---|
| Prompt injection | Workforce descriptions or chat text instruct an agent to ignore policy or expose private data. | Treat business text as untrusted, use capability allowlists, enforce policy gates. |
| Data leakage | Worker, enterprise, wage, billing, or dispute data crosses scope. | Data classification, tenant and role checks, masking, audit. |
| Identity impersonation | The accepting worker and the arriving worker are not the same person. | Identity binding, credential checks, attendance evidence, subject-bound claims. |
| Ghost labor | Fake attendance or fake work hours are used to trigger settlement. | Dual confirmation, geofence, site verification, anomaly detection, evidence refs. |
| Wage harm | Settlement is delayed, denied, or reduced without evidence or dispute path. | Fulfillment evidence, settlement gates, mandate, dispute SLA, audit. |
| Discrimination | Matching uses prohibited attributes or proxy features. | Policy constraints, prohibited filters, feature audit, explanations. |
| Reputation manipulation | Collusive reviews or malicious negative credit updates. | Evidence-bound credit events, anomaly detection, dispute mechanisms. |
| Stale state | Agents act on outdated schedules, credentials, wage rules, or dispute state. | Object versions, event watermarks, expiration, revalidation. |
| Unauthorized write | Agents directly submit deductions, compensation, payments, or liability decisions. | R4/R5 mandate, human controller, audit event, least privilege. |

Implementations MUST NOT expose full personal identifiers unless the requester has explicit authority and a legitimate purpose. Selective disclosure SHOULD be used for credentials whenever possible. For example, return "health certificate valid = true" instead of returning the certificate image.

Negative worker outcomes such as deductions, negative credit, settlement denial, or dispute liability MUST be supported by evidence, policy decision, responsible entity, and a review or dispute path.

## 18. Standard Capability Reference

### 18.1 Core Capabilities

| Capability | Purpose | Side Effect | Risk |
|---|---|---|---|
| `org.ugp.discovery.profile` | Discover protocol versions, profiles, services, capabilities, and policy requirements. | `data_read` | `R0` |
| `org.ugp.policy.evaluate` | Evaluate authorization, risk, masking, confirmation, escalation, or denial. | `data_read` | `R1` |
| `org.ugp.audit.record` | Record an audit event. | `data_write_commit` | `R3` |
| `org.ugp.artifact.create` | Create a confirmation card, evidence packet, settlement explanation, or other artifact. | `data_write_prepare` | `R3` |
| `org.ugp.mandate.prepare` | Prepare confirmation or authorization. | `data_write_prepare` | `R3` |
| `org.ugp.mandate.confirm` | Commit confirmation or authorization. | `data_write_commit` | `R4` |

### 18.2 Enterprise Operations Capabilities

| Capability | Purpose |
|---|---|
| `org.ugp.demand.create` | Prepare or create workforce demand. |
| `org.ugp.demand.publish` | Publish workforce demand. |
| `org.ugp.candidate.query` | Query candidate or supply state. |
| `org.ugp.fit_assessment.review` | Review fit assessment. |
| `org.ugp.contract.prepare_confirm` | Prepare enterprise confirmation. |
| `org.ugp.schedule.assign` | Prepare or commit scheduling assignment. |
| `org.ugp.fulfillment.business_verification.prepare` | Prepare fulfillment verification. |
| `org.ugp.workhour.confirm.prepare` | Prepare work-hour confirmation. |
| `org.ugp.dispute.evidence_packet.create` | Create a dispute evidence packet. |

### 18.3 Worker Opportunity Capabilities

| Capability | Purpose |
|---|---|
| `org.ugp.labor_state.claim` | Let a worker declare availability, preferences, capability, or constraints. |
| `org.ugp.opportunity.search` | Search work opportunities. |
| `org.ugp.opportunity.explain_fit` | Explain whether an opportunity fits the worker's state and preferences. |
| `org.ugp.contract.worker_accept.prepare` | Prepare worker acceptance. |
| `org.ugp.contract.worker_accept.confirm` | Confirm worker acceptance. |
| `org.ugp.attendance.claim` | Claim attendance, check-in, supplemental check-in, or exception explanation. |
| `org.ugp.income.reconcile` | Reconcile work hours and income. |
| `org.ugp.credit.explain` | Explain workforce credit changes. |

### 18.4 Platform, Settlement, and Dispute Capabilities

| Capability | Purpose |
|---|---|
| `org.ugp.matching.run` | Match workforce demand with labor state and opportunity constraints. |
| `org.ugp.risk.assess` | Assess workforce, demand, fulfillment, or settlement risk. |
| `org.ugp.backup.dispatch` | Dispatch backup labor. |
| `org.ugp.fulfillment.status.query` | Query fulfillment status. |
| `org.ugp.exception.route` | Route exceptions to the right handler. |
| `org.ugp.settlement.diagnose` | Diagnose payroll, billing, settlement, or credit blockers. |
| `org.ugp.settlement.prepare` | Prepare settlement, adjustment, compensation, or deduction. |
| `org.ugp.credit.update.prepare` | Prepare credit update. |
| `org.ugp.dispute.open` | Open a dispute case. |
| `org.ugp.dispute.resolve.prepare` | Prepare dispute resolution. |

## 19. Registries

UGP defines the following initial registries.

| Registry | Initial Values |
|---|---|
| Object Type | `labor_state`, `workforce_demand`, `work_opportunity`, `work_contract`, `fulfillment_record`, `settlement_credit`, `evidence_ref`, `artifact`, `mandate`, `audit_event`, `policy_decision` |
| Profile | `org.ugp.core`, `org.ugp.enterprise_operations`, `org.ugp.worker_opportunity`, `org.ugp.flex_work`, `org.ugp.settlement`, `org.ugp.dispute` |
| Capability Namespace | `org.ugp.discovery`, `org.ugp.policy`, `org.ugp.audit`, `org.ugp.mandate`, `org.ugp.demand`, `org.ugp.opportunity`, `org.ugp.contract`, `org.ugp.fulfillment`, `org.ugp.settlement`, `org.ugp.dispute`, `org.ugp.credit` |
| WorkContract State | `prepared`, `proposed`, `accepted`, `confirmed`, `scheduled`, `in_progress`, `worker_claimed`, `verified`, `settlement_pending`, `settled`, `needs_info`, `confirmation_required`, `disputed`, `canceled`, `voided`, `blocked` |
| Policy Decision | `ALLOW`, `MASK_AND_ALLOW`, `ASK_CONFIRMATION`, `ESCALATE`, `DENY` |
| Data Classification | `public`, `internal`, `confidential`, `sensitive`, `restricted` |
| Mandate Type | `demand_mandate`, `worker_intent_mandate`, `worker_acceptance`, `business_confirmation`, `settlement_mandate`, `dispute_mandate` |
| Responsible Entity Model | `direct_employment`, `labor_dispatch`, `outsourcing`, `platform_service`, `contractor`, `employer_of_record`, `unknown` |

## 20. Conformance and Benchmarking

A UGP implementation SHOULD be testable. Conformance tests SHOULD verify:

- profile discovery works;
- unsupported versions and profiles fail safely;
- capability negotiation returns active capabilities;
- schema validation blocks invalid payloads;
- policy decisions are enforced before tool commit;
- sensitive data is masked or denied by default;
- R4 and R5 actions require mandate or human controller;
- work-contract state transitions reject invalid jumps;
- settlement is gated by fulfillment evidence;
- audit events are produced for required actions;
- agent final responses do not claim committed actions when only a prepared artifact exists.

The WorkforceOps Benchmark v1 in this repository is the first benchmark dataset built on UGP. It is grounded in redacted enterprise-side workforce management data and validates whether an agent can handle realistic enterprise operations questions while respecting policy, privacy, mandate, and tool-call boundaries.

Important scope note: Benchmark v1 covers only enterprise-side workforce management. It is not a full coverage test for all UGP profiles.

## 21. Interoperability

UGP may reuse:

- A2A for agent discovery, task negotiation, and long-running agent workflows;
- MCP for tool invocation and LLM-facing capability exposure;
- REST and OpenAPI for enterprise and platform integration;
- event protocols and AsyncAPI for lifecycle events;
- AP2 or local payment protocols for payment, escrow, payout, and reconciliation;
- DID and W3C Verifiable Credentials for identity, credentials, certificates, training, and selective disclosure;
- UCP where a work-related flow includes ordinary commerce;
- existing workforce systems such as HCM, ATS, scheduling, attendance, payroll, finance, billing, and customer service.

The protocol's center of gravity remains the gig work relationship: demand, labor state, opportunity, commitment, fulfillment, settlement, dispute, and credit.

## 22. Glossary

| Term | Meaning |
|---|---|
| Agent | Software actor that represents an enterprise, worker, platform, or responsible entity. |
| Capability | Discoverable, authorizable, auditable business operation. |
| Profile | Scenario-specific bundle of UGP objects, capabilities, policy rules, schemas, and lifecycle constraints. |
| Mandate | Confirmation or authorization record tied to a principal, action, scope, object, expiration, and audit trail. |
| Responsible Entity | Entity that carries legal, contractual, financial, safety, tax, insurance, or service responsibility. |
| Fulfillment | The fact that work was performed, verified, disputed, or blocked. |
| Settlement | Payroll, payment, billing, compensation, deduction, invoicing, or reconciliation action derived from fulfillment. |
| Workforce Credit | Reputation, trust, or risk signal derived from fulfillment, dispute, and settlement history. |

## Appendix A: Enterprise Operations Example

Enterprise manager:

```text
Tomorrow from 2 PM to 6 PM, we need three tea shop workers with valid health certificates at Store A. The hourly rate is 25 CNY and the gap must be filled before 10 PM tonight.
```

Enterprise Agent creates `workforce_demand`:

```json
{
  "object_type": "workforce_demand",
  "profile": "org.ugp.enterprise_operations",
  "enterprise_ref": "enterprise_masked_01",
  "site_ref": "store_alias_a",
  "role": "tea_shop_worker",
  "headcount": 3,
  "time_window": {
    "start": "2026-07-18T14:00:00+08:00",
    "end": "2026-07-18T18:00:00+08:00"
  },
  "credential_requirements": [
    {
      "type": "health_certificate",
      "verification": "valid"
    }
  ],
  "compensation": {
    "rate": "25 CNY/hour"
  },
  "service_level": {
    "fill_before": "2026-07-17T22:00:00+08:00"
  }
}
```

Platform Agent runs matching, creates opportunities, prepares enterprise confirmation, requests worker acceptance, verifies attendance, and prepares settlement. Each commit step is represented by UGP objects, policy decisions, mandates, and audit events.

## Appendix B: Non-Goals

UGP is not:

- a recruiting-only protocol;
- a job-posting-only protocol;
- an enterprise-side operations-only protocol;
- a natural-language wrapper around private APIs;
- a payment protocol;
- an identity protocol;
- a payroll system;
- a general-purpose full-time HCM or employee-lifecycle protocol;
- a legal classification framework;
- a replacement for local labor law, tax law, social insurance rules, safety rules, or contractual obligations.
