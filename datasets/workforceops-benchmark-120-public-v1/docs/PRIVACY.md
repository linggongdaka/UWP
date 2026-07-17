# Privacy and Redaction

This release is a privacy-safe evaluation package, not a production-data dump.

## Removed

- Real names, full mobile numbers, ID cards, bank accounts and certificate images.
- Real location, store, school and brand names, plus health-certificate details.
- Customer identifiers, private contract terms and private redaction maps.
- Internal worker identifiers and candidate media or original interview answers.
- Internal table names, SQL references, source paths and replay file names.

## Retained

- Synthetic store, worker and candidate aliases.
- Aggregate business metrics and deterministic mock-safe detail metrics.
- Authorization boundaries, redline definitions and scoring expectations required to reproduce the evaluation semantics.

Some business-task inputs intentionally contain common industry wording in order to test robust request understanding. These simulated inputs do not define any real employment or service relationship.

Public display names use explicit numbered aliases such as `模拟门店01` and `灵工001`. Generic words such as school, entry document or chain restaurant describe task semantics and do not identify a real entity.
