# UGP Schemas

This directory contains starter schemas for the public Universal Gig Protocol package.

The current schema files are intentionally small. They define the minimum validation surface needed to demonstrate how UGP profile discovery and message envelopes can be checked before an implementation expands into complete object, capability, and profile schemas.

| File | Purpose |
|---|---|
| [ugp-profile.schema.json](./ugp-profile.schema.json) | Starter schema for a `/.well-known/ugp` profile document. |
| [ugp-envelope.schema.json](./ugp-envelope.schema.json) | Starter schema for a UGP message envelope. |

Future schema sets can add base object schemas, profile-specific constraints, capability input/output schemas, and extension composition tests.
