# Public Safety and Pairing Validation

Status: **PASS**

Package: `workforceops-enterprise-operations-redacted-data-v1`
Dataset ID: `workforceops_enterprise_operations_redacted_data_v1_20260531`

## Checks

| Check | Result | Details |
|---|---:|---|
| `case_count` | PASS | `{"benchmark_120":120,"qa_items":120}` |
| `case_id_alignment` | PASS | `{"missing_in_qa":[],"missing_in_benchmark":[]}` |
| `dataset_id_alignment` | PASS | `{"dataset_ids":["workforceops_enterprise_operations_redacted_data_v1_20260531"]}` |
| `public_table_alignment` | PASS | `{"public_table_count":9,"missing_public_tables":[]}` |
| `internal_source_names_absent` | PASS | `{"internal_table_name_count":0,"warehouse_product_name_count":0}` |
| `stable_public_id_mapping` | PASS | `{"enterprise_id_name_conflicts":0,"store_id_name_conflicts":0,"worker_id_name_conflicts":0,"department_id_name_conflicts":0}` |
| `entity_alias_alignment` | PASS | `{"case_alias_count":30,"manifest_alias_count":30,"missing":[]}` |
| `display_entity_alignment` | PASS | `{"mismatches":[]}` |
| `qa_metric_replay_from_public_csv` | PASS | `{"metrics_checked":797,"domain_counts":{"薪资与费用":{"qa_items":16,"metrics_checked":80},"人员与花名册":{"qa_items":20,"metrics_checked":160},"需求与排班":{"qa_items":15,"metrics_checked":105},"考勤与工时":{"qa_items":17,"metrics_checked":136},"评价与奖惩":{"qa_items":9,"metrics_checked":45},"争议与合规":{"qa_items":14,"metrics_checked":98},"培训与...` |
| `benchmark_gold_metrics_equal_referenced_qa` | PASS | `{"gold_blocks_checked":284,"bad_blocks":[]}` |
| `public_executable_queries_absent` | PASS | `{"query_field_count":0,"executable_query_metadata_present":false}` |
| `public_safety_regex_scan` | PASS | `{"email":[],"cn_mobile":[],"cn_id_18":[],"bank_card_like":[],"source_enterprise_id":[],"source_store_id":[]}` |
| `forbidden_public_text_scan` | PASS | `{}` |
| `id_alias_format` | PASS | `{"bad_values":[]}` |
| `csv_row_counts` | PASS | `{"anchor_stores.csv":30,"bills_may.csv":136,"comments_may.csv":7395,"demand_schedule_may.csv":3050,"insurance_claims_may.csv":9369,"salary_records_may.csv":5817,"schedule_attendance_may.csv":11347,"store_roster_may.csv":955,"training_may.csv":1070}` |
| `json_parse` | PASS | `{"json_file_count":5,"errors":[]}` |
| `markdown_local_links` | PASS | `{"bad_links":[]}` |

## Notes

- The 120 benchmark cases align one-to-one with the 120 QA grounding items by `case_id` and `qa_id`.
- All public benchmark gold metrics are replayed from redacted CSV files under `tables/`.
- Public replay uses redacted CSV tables and gold metrics; SQL snippets, raw executable SQL, and private reverse mappings are excluded.
- Public enterprise, store, worker, and department aliases have stable one-to-one display mappings.
- Redline privacy prompts use generic sample placeholders rather than real worker identities.
- The package only covers enterprise-side workforce management scenarios in this first version.
