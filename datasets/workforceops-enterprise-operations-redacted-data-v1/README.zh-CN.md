# WorkforceOps Enterprise Operations Redacted Data Package v1

这是 WorkforceOps Benchmark v1 的公开脱敏配套数据包，基于 UGP 2026-07 与 `org.ugp.enterprise_operations` 场景配置。

[English README](./README.md)

它提供 benchmark case 的 grounding 依赖数据：2026 年 5 月企业侧用工管理脱敏表、QA grounding、120 case benchmark 包、manifest 和校验制品。

范围说明：第一版只覆盖企业侧用工管理场景。

源系统元数据可能包含混合用工类型；UGP 一致性范围仅限灵工对象与能力，不代表支持全职 HCM。

## 内容

| 路径 | 用途 |
|---|---|
| [`manifest.json`](./manifest.json) | 包元数据、dataset id、公开表清单和 benchmark entity-alias 映射。 |
| [`tables/`](./tables/) | 2026 年 5 月企业侧用工管理快照的脱敏依赖 CSV 表。 |
| [`qa/workforceops-enterprise-operations-qa-grounding-redacted-v1.json`](./qa/workforceops-enterprise-operations-qa-grounding-redacted-v1.json) | 与 benchmark case 对齐的 120 条 QA grounding。Gold metrics 只保留可由公开脱敏 CSV 表重算的指标。 |
| [`benchmark/cases/workforceops-enterprise-operations-benchmark-v1.json`](./benchmark/cases/workforceops-enterprise-operations-benchmark-v1.json) | 公开 120 case benchmark 包。 |
| [`validation/VALIDATION.md`](./validation/VALIDATION.md) | 人类可读校验报告。 |
| [`validation/public_safety_validation.json`](./validation/public_safety_validation.json) | 机器可读校验报告。 |
| [`redaction_summary.json`](./redaction_summary.json) | 公开脱敏摘要，包含 alias 数量和合成展示实体。 |

## 脱敏策略

- 企业、大区、门店和实体路径展示名均为公开合成名。
- worker id、worker name、enterprise id、store id、department id、task id、job id、bill id、training id 均为稳定别名。
- 公开企业、门店、劳动者和部门别名在包内保持一一稳定展示映射。
- 业务日期、状态字段、数量和金额聚合保留，用于 benchmark 可复验。
- SQL 片段、原始可执行 SQL、私有反向映射、手机号、身份证号、银行卡号、邮箱和密钥均不进入公开仓库。
- 红线隐私 prompt 使用通用示例占位符，不使用真实劳动者身份。

## 脱敏问题模板说明

benchmark metadata 和 QA grounding 中的 `question_redacted` 是脱敏模板，不是最终用户题面。`<门店路径>` 表示构造 case 时会替换为公开合成门店路径。实际 `conversation` 消息使用 `A市星桥火锅店` 这类合成展示名；当前 120 个 case 的对话消息中不包含 `<门店路径>`。

## 与 Benchmark 的配套关系

本包与 [`../workforceops-enterprise-operations-benchmark-v1.json`](../workforceops-enterprise-operations-benchmark-v1.json) 配套。

校验结果：

- 120 个 benchmark case 与 120 个 QA grounding item 通过 `case_id` 和 `qa_id` 一一对齐。
- 所有 benchmark `entity_alias` 都能映射到 `manifest.json` 中的公开 entity-alias map。
- 所有 benchmark case 引用的公开表都能解析到本包内的脱敏 CSV 文件。
- 所有公开 gold metrics 都能从公开脱敏 CSV 表重算。
- 全包 dataset id 统一为 `workforceops_enterprise_operations_redacted_data_v1_20260531`。

## 行数

| 文件 | 行数 |
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

本包随仓库采用 MIT License 发布。
