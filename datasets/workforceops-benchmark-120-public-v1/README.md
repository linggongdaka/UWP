# WorkforceOps Benchmark 120

面向灵活用工业务 Agent 的120道公开评测题，覆盖证据查询、授权范围、隐私保护、人工确认、升级流转和可追溯输出。

## 内容

- `data/workforceops_benchmark_120_public_v1.json`：完整公开版题包。
- `reports/dataset_analysis_zh.md`：数据分布、难度、权限、红线和业务能力分析。
- `reports/model_results_zh.md`：四模型对比结果；Qwen 困难题采用三次稳定交集口径。
- `docs/DATASET_CARD.zh-CN.md`：数据集用途、边界与限制。
- `docs/DATA_DICTIONARY.zh-CN.md`：核心字段说明。
- `docs/PRIVACY.md`：隐私与脱敏策略。
- `schemas/`：JSON Schema。
- `scripts/validate_release.py`：独立校验脚本。

## 校验

```bash
python3 scripts/validate_release.py
```

## 使用边界

数据集中的门店、人员和候选人标识均为模拟别名。业务题中的行业常见说法用于测试模型对真实请求的理解，不用于定义任何实际劳动或服务关系。公开包不包含生产原始数据、客户标识、个人敏感信息、内部表名、SQL或数据落地路径。

## License

本发布包随 UGP 仓库采用 [MIT License](../../LICENSE)。
