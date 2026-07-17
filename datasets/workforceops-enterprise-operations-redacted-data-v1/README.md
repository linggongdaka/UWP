# WorkforceOps Enterprise Operations Redacted Data Package v1

This package is the public redacted companion dataset for WorkforceOps Benchmark v1, built on UGP 2026-07 and the `org.ugp.enterprise_operations` profile.

[中文说明](./README.zh-CN.md)

It contains the dependent data needed to inspect how the benchmark cases are grounded: redacted May 2026 enterprise-side workforce operations tables, QA grounding, the 120-case benchmark pack, a manifest, and validation artifacts.

Scope note: this first version only covers enterprise-side workforce management scenarios.

Source-system metadata may include mixed employment types. UGP conformance remains limited to gig-work objects and capabilities and does not claim full-time HCM support.

## Contents

| Path | Purpose |
|---|---|
| [`manifest.json`](./manifest.json) | Package metadata, dataset id, public table inventory, and benchmark entity-alias mapping. |
| [`tables/`](./tables/) | Redacted dependent CSV tables for the May 2026 enterprise workforce operations snapshot. |
| [`qa/workforceops-enterprise-operations-qa-grounding-redacted-v1.json`](./qa/workforceops-enterprise-operations-qa-grounding-redacted-v1.json) | 120 QA grounding items aligned to benchmark cases. Gold metrics are restricted to values that can be recomputed from the public redacted CSV tables. |
| [`benchmark/cases/workforceops-enterprise-operations-benchmark-v1.json`](./benchmark/cases/workforceops-enterprise-operations-benchmark-v1.json) | Public 120-case benchmark pack. |
| [`validation/VALIDATION.md`](./validation/VALIDATION.md) | Human-readable validation report. |
| [`validation/public_safety_validation.json`](./validation/public_safety_validation.json) | Machine-readable validation report. |
| [`redaction_summary.json`](./redaction_summary.json) | Public redaction summary with alias counts and synthetic display entities. |

## Redaction Policy

- Enterprise, region, store, and entity-path display names are synthetic public names.
- Worker ids, worker names, enterprise ids, store ids, department ids, task ids, job ids, bill ids, and training ids are stable aliases.
- Public enterprise, store, worker, and department aliases keep stable one-to-one display mappings inside this package.
- Business dates, status fields, counts, and monetary aggregates are preserved for benchmark reproducibility.
- SQL snippets, raw executable SQL, private reverse mappings, phone numbers, ID-card numbers, bank-card numbers, email addresses, and secrets are excluded from the public repository.
- Redline privacy prompts use generic sample placeholders rather than real worker identities.

## Redacted Question Templates

The `question_redacted` fields in benchmark metadata and QA grounding are redaction templates, not user-facing benchmark prompts. Placeholders such as `<门店路径>` mark where synthetic public store paths are substituted during case construction. The actual `conversation` messages use synthetic display entities such as `A市星桥火锅店`; no conversation message in the 120-case pack contains `<门店路径>`.

## Pairing With Benchmark

The package is paired with [`../workforceops-enterprise-operations-benchmark-v1.json`](../workforceops-enterprise-operations-benchmark-v1.json).

Validation results:

- 120 benchmark cases align one-to-one with 120 QA grounding items by `case_id` and `qa_id`.
- All benchmark `entity_alias` values map to the public entity-alias map in `manifest.json`.
- All public table references used by benchmark cases resolve to redacted CSV files in this package.
- All public gold metrics can be recomputed from the public redacted CSV tables.
- All package-level dataset ids are unified as `workforceops_enterprise_operations_redacted_data_v1_20260531`.

## Row Counts

| File | Rows |
|---|---:|
| `anchor_stores.csv` | 30 |
| `bills_may.csv` | 136 |
| `comments_may.csv` | 7395 |
| `demand_schedule_may.csv` | 3050 |
| `insurance_claims_may.csv` | 9369 |
| `salary_records_may.csv` | 5817 |
| `schedule_attendance_may.csv` | 11347 |
| `store_roster_may.csv` | 955 |
| `training_may.csv` | 1070 |

## License

This package is released under the repository MIT License.
