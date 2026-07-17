# UGP：通用灵工协议

UGP（Universal Gig Protocol，通用灵工协议）是面向 AI Agent 时代的开放业务协议。

它让企业 Agent、劳动者 Agent 和平台 Agent 能够使用同一套语言完成能力发现、人力状态表达、工作机会匹配、工作承诺协商、履约事实确认、争议处理、结算信用沉淀和跨系统审计。

UGP 不是招聘协议，不是岗位发布协议，也不是内部 API 的自然语言包装。UGP 把“灵工关系”作为 Agent 可以理解、授权、执行、审计和持续优化的一等协议对象。

[English README](./README.md)

## 为什么是 UGP

灵工市场的第一性原理是流动性：合适的人、合适的工作、合适的时间、合适的地点和合适的约束，需要被快速、可靠、负责任地匹配起来。

传统软件把这个过程拆在需求、排班、报名、入职、考勤、工时、培训、证件、薪资、账单、开票、争议、评价和信用等多个系统里。到了 Agent 时代，如果没有共同协议，AI 只会把碎片化软件变成碎片化对话。

UGP 是 Agent 原生灵工网络的协议层：

- 企业可以表达需要什么人、什么时间、什么地点、什么规则、什么预算和什么履约要求。
- 劳动者可以表达可工作状态、能力、偏好、证件、承诺和收入预期。
- 平台可以完成匹配、调度、验真、结算、审计和跨周期信用沉淀。

## 仓库内容

| 路径 | 作用 |
|---|---|
| [protocol/](./protocol/) | UGP 协议目录，包含中英文规格、协议图、示例和 starter schemas。 |
| [protocol/en/](./protocol/en/) | 英文协议入口与完整英文协议正文。 |
| [protocol/zh/](./protocol/zh/) | 中文协议入口与完整中文协议正文。 |
| [protocol/examples/](./protocol/examples/) | 发现、能力响应、策略决策和企业侧用工管理流程的机器可读示例。 |
| [protocol/schemas/](./protocol/schemas/) | UGP 场景配置发现与消息信封的 starter JSON Schemas。 |
| [datasets/](./datasets/) | WorkforceOps 评测 v1 与脱敏数据配套包。 |

## 协议表面

UGP 从六类一等对象开始：

| 对象 | 含义 |
|---|---|
| `labor_state` | 劳动者的可工作状态、能力、偏好、证件、位置、限制条件和信用状态。 |
| `workforce_demand` | 企业或平台的人力需求，包括岗位、班次、规则、技能、预算和履约要求。 |
| `work_opportunity` | 劳动者 Agent 可以发现、比较、申请、接受或拒绝的具体工作机会。 |
| `work_contract` | 关于时间、地点、薪酬、规则、取消条件、责任主体和确认动作的标准承诺对象。 |
| `fulfillment_record` | 到岗、打卡、工时、任务完成、验真、异常、证据和争议事实。 |
| `settlement_credit` | 薪资、账单、支付、赔付、扣罚、开票状态、评价和履约信用。 |

UGP 还定义：

- 通过 `/.well-known/ugp` 或等价注册表进行场景配置发现；
- `org.ugp.*` 命名空间下的标准能力；
- `ALLOW`、`MASK_AND_ALLOW`、`ASK_CONFIRMATION`、`ESCALATE`、`DENY` 五类策略决策；
- 高风险动作的授权确认与审计语义；
- 从 `prepared` 到 `settled` 的 WorkContract 生命周期，以及争议、取消、阻断路径；
- 场景配置与扩展的 schema 组合；
- REST、MCP、A2A、Event 和内部 RPC 的传输绑定。

## 初始场景配置

| 场景配置 | 范围 |
|---|---|
| `org.ugp.core` | 发现、信封、对象引用、策略决策、授权确认、审计事件和通用生命周期语义。 |
| `org.ugp.enterprise_operations` | 企业侧与平台用工管理：花名册、需求排班、考勤工时、薪资费用、账单开票、争议合规、评价奖惩。 |
| `org.ugp.worker_opportunity` | 劳动者侧工作机会旅程：找活、推荐、接单、到岗、收入核对、争议发起和信用解释。 |
| `org.ugp.flex_work` | 兼职、临时、按需、班次制和项目制灵工关系。 |
| `org.ugp.settlement` | 薪资、支付、账单、开票、赔付、扣罚、信用更新和对账。 |
| `org.ugp.dispute` | 证据包、申诉、争议流转、责任主体升级和处理结果。 |

全职 HCM 与通用员工全生命周期管理不属于 UGP 核心范围。灵工链路与这些系统交叉时，实现方可以通过厂商扩展完成集成。

## WorkforceOps 评测 v1

本仓库中的数据集是基于 UGP 的第一版 WorkforceOps 评测。

重要范围说明：v1 只覆盖企业侧用工管理场景，聚焦企业侧和平台侧的人员花名册、需求排班、考勤工时、薪资费用、培训证件、争议合规、账单开票、评价奖惩等运营链路。它还不覆盖完整劳动者侧工作机会旅程，也不覆盖所有平台结算与信用场景配置。

数据集概览：

- 120 个案例。
- 43 个简单案例、48 个中等案例、29 个困难案例。
- 86 个多轮案例、34 个单轮案例；其中 110 个采用一次性输入评测，10 个采用逐轮输入评测。
- 覆盖 9 类用工管理场景和 30 组模拟门店授权范围。
- 包含 106 个业务操作案例和 14 个红线安全案例。
- 策略期望包含 `ALLOW`、`MASK_AND_ALLOW`、`ASK_CONFIRMATION`、`ESCALATE`、`DENY`。
- 数据集基于脱敏业务数据映射生成，并经过公开发布适配：劳动者身份不进入改写案例，实体路径使用合成别名，标准答案值仅保留门店/月度聚合指标，私有脱敏映射不提交到本仓库。

配套数据包 [WorkforceOps Enterprise Operations Redacted Data Package v1](./datasets/workforceops-enterprise-operations-redacted-data-v1/) 提供可公开使用的脱敏依赖表和 QA grounding。包内包含机器可读 manifest 和校验制品，确认评测 cases、QA grounding 与公开 CSV 指标已对齐。

仓库同时提供 [120 道业务题校准公开版](./datasets/workforceops-benchmark-120-public-v1/)，包含 43 道简单题、48 道中等题和 29 道困难题，并附数据集分析、四模型对比结果、图表、Schema、校验和与独立校验脚本。

这个评测不是单纯问答集。它评估的是 Agent 在企业用工运营语境下，是否理解授权边界、隐私策略、红线要求、预期产物和工具调用意图。

## 许可证

本仓库采用 MIT 许可证。详见 [LICENSE](./LICENSE)。
