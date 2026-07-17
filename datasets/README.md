# Datasets

This directory contains the public dataset releases for UGP.

[中文说明](./README.zh-CN.md)

## Releases

- [WorkforceOps Benchmark v1](./workforceops-enterprise-operations-benchmark-v1.json)
  The first benchmark dataset built on UGP 2026-07. WorkforceOps remains the benchmark name; version 1 covers enterprise-side workforce management scenarios only.

- [WorkforceOps Enterprise Operations Redacted Data Package v1](./workforceops-enterprise-operations-redacted-data-v1/)
  The public companion package for the benchmark. It contains redacted dependent tables, QA grounding, the 120-case benchmark pack, a manifest, and validation artifacts.

- [WorkforceOps Benchmark 120 Calibrated Public Release](./workforceops-benchmark-120-public-v1/)
  A calibrated 120-task release with 43 easy, 48 medium, and 29 hard tasks. It includes the complete public JSON pack, schemas, a dataset card, privacy notes, distribution analysis, four-model main-run results, charts, checksums, and a standalone validator.

## Scope

The first release is deliberately narrow. It covers enterprise-side and platform workforce management: roster, demand and scheduling, attendance and work hours, salary and fees, training and certificates, dispute and compliance, bill and invoice, and reward or penalty scenarios.

The source-system context may report support for mixed employment types, including full-time workers. UGP conformance in this dataset is limited to gig-work objects and capabilities; it does not claim full-time HCM support.

It does not yet cover the full worker-side opportunity journey.
