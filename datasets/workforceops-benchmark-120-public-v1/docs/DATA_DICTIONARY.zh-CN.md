# 数据字典

| 字段 | 含义 |
| --- | --- |
| `case_id` | 业务题稳定标识，例如 `WOB-1.0-083`。 |
| `track` | `b_operation` 为业务操作题，`redline` 为红线安全题。 |
| `stage` | 业务类型技术标识。 |
| `difficulty` | `easy`、`mid`、`hard`。 |
| `turn_type` | 对话内容是单轮还是多轮。 |
| `evaluation_mode` | `single` 一次性输入完整上下文；`incremental` 逐轮输入。 |
| `actor_role` | 当前请求人的业务角色。 |
| `auth_context` | 授权范围、可见门店、允许字段、脱敏字段和禁止字段。 |
| `runtime_context` | 业务日期、相对时间解析和报告月份。 |
| `conversation` | 模型需要处理的用户请求。 |
| `initial_state` | 任务开始时的业务状态。 |
| `expected_capabilities` | 期望调用的业务能力。 |
| `expected_tool_args` | 业务能力调用参数的验收要求。 |
| `expected_state_transitions` | 允许或要求出现的状态变化。 |
| `expected_artifacts` | 期望生成的报告、确认草稿或证据包。 |
| `policy_expectation` | 允许、脱敏、确认、升级或拒绝的权限处置要求。 |
| `mandate_expectation` | 是否需要明确授权或人工确认。 |
| `redlines` | 敏感信息、越权和高风险动作的硬边界。 |
| `metadata.real_data_grounding.gold_metrics` | 最终回答应引用的安全业务指标。 |
| `metadata.scoring_expectation` | 必需证据与动作等补充验收条件。 |

## 权限处置值

- `ALLOW`：允许查询并回答。
- `MASK_AND_ALLOW`：脱敏后回答。
- `ASK_CONFIRMATION`：准备确认草稿，等待人工确认。
- `ESCALATE`：整理证据并升级人工复核。
- `DENY`：拒绝越权或不合规请求，并给出安全替代方案。
