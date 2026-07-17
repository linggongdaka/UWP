# Protocol

This directory contains the public Universal Gig Protocol package.

UGP is organized as a protocol directory, not a single document. The directory includes the English and Chinese protocol texts, shared diagrams, machine-readable examples, and schema notes that make the protocol easier to implement and review.

## Directory Layout

| Path | Purpose |
|---|---|
| [en/](./en/) | English protocol overview and full protocol text. |
| [zh/](./zh/) | 中文协议入口与完整中文协议正文。 |
| [examples/](./examples/) | Machine-readable example payloads for discovery, negotiation, policy, and workforce operations flows. |
| [schemas/](./schemas/) | Schema guidance and starter JSON Schemas for UGP profile and envelope validation. |
| [assets/](./assets/) | Shared protocol diagrams rendered by GitHub Markdown. |

## Protocol Texts

| Language | Overview | Full Protocol |
|---|---|---|
| English | [protocol/en/README.md](./en/) | [protocol/en/universal-gig-protocol.md](./en/universal-gig-protocol.md) |
| 中文 | [protocol/zh/README.md](./zh/) | [protocol/zh/universal-gig-protocol.md](./zh/universal-gig-protocol.md) |

## Implementation Surface

UGP implementations should start from these protocol surfaces:

- discovery through `/.well-known/ugp` or an equivalent internal registry;
- profiles such as `org.ugp.core` and `org.ugp.enterprise_operations`;
- capabilities in the `org.ugp.*` namespace;
- standard objects such as `labor_state`, `workforce_demand`, `work_opportunity`, `work_contract`, `fulfillment_record`, and `settlement_credit`;
- policy decisions: `ALLOW`, `MASK_AND_ALLOW`, `ASK_CONFIRMATION`, `ESCALATE`, and `DENY`;
- mandates and audit events for high-risk actions;
- schema composition for base objects, profiles, and vendor extensions;
- transport bindings for REST, MCP, A2A, event streams, and internal RPC.

## Diagrams

- Protocol layering: [PNG](./assets/ugp-diagram-1-protocol-layers.png), [SVG](./assets/ugp-diagram-1-protocol-layers.svg)
- Three agent applications: [PNG](./assets/ugp-diagram-2-three-agent-applications.png), [SVG](./assets/ugp-diagram-2-three-agent-applications.svg)
- Architecture overview: [PNG](./assets/ugp-rfc-architecture-overview.png), [SVG](./assets/ugp-rfc-architecture-overview.svg)
- Object lifecycle: [PNG](./assets/ugp-rfc-object-lifecycle.png), [SVG](./assets/ugp-rfc-object-lifecycle.svg)
- Policy gate: [PNG](./assets/ugp-rfc-policy-gate.png), [SVG](./assets/ugp-rfc-policy-gate.svg)

## Benchmark Link

The repository's first benchmark release covers the enterprise-side workforce management profile, `org.ugp.enterprise_operations`. It is not yet a full test of every UGP profile.
