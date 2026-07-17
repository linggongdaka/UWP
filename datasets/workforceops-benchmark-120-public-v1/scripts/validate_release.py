#!/usr/bin/env python3
"""Validate the standalone WorkforceOps public benchmark release package."""

from __future__ import annotations

import hashlib
import json
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any, Iterable


REQUIRED_CASE_KEYS = {
    "case_id",
    "track",
    "stage",
    "difficulty",
    "actor_role",
    "conversation",
    "initial_state",
    "expected_state_transitions",
    "expected_artifacts",
    "policy_expectation",
    "mandate_expectation",
    "redlines",
}

FORBIDDEN_KEYS = {
    "source_tables",
    "snapshot_sql_ref",
    "real_data_scope",
    "employee_detail_fixture",
    "mixed_pack_source_pack",
    "mixed_pack_source_case_id",
    "source_report_root",
}

INTERNAL_REFERENCE_PATTERNS = (
    re.compile(r"[^\s\"']+\.sql\b", re.IGNORECASE),
    re.compile(r"[^\s\"']+_internal\.csv\b", re.IGNORECASE),
)

SECRET_PATTERNS = (
    re.compile(r"sk-[A-Za-z0-9]{10,}"),
    re.compile(r"[A-Za-z0-9]{32}\.[A-Za-z0-9]{16}"),
    re.compile(r"AKIA[0-9A-Z]{16}"),
    re.compile(r"AIza[0-9A-Za-z_-]{20,}"),
    re.compile(r"gh[pousr]_[A-Za-z0-9]{20,}"),
)

MOBILE_PATTERN = re.compile(r"(?<!\d)1[3-9]\d{9}(?!\d)")
ID_CARD_PATTERN = re.compile(r"(?<!\d)\d{17}[0-9Xx](?!\d)")
BANK_ACCOUNT_PATTERN = re.compile(r"(?<!\d)\d{16,19}(?!\d)")
EMAIL_PATTERN = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b")


def walk(value: Any, path: str = "$") -> Iterable[tuple[str, Any]]:
    yield path, value
    if isinstance(value, dict):
        for key, item in value.items():
            yield from walk(item, f"{path}.{key}")
    elif isinstance(value, list):
        for index, item in enumerate(value):
            yield from walk(item, f"{path}[{index}]")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as file_handle:
        for chunk in iter(lambda: file_handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def validate_dataset(dataset_path: Path) -> list[str]:
    errors: list[str] = []
    data = json.loads(dataset_path.read_text(encoding="utf-8"))
    cases = data.get("cases")
    if not isinstance(cases, list):
        return ["dataset.cases must be a list"]
    if len(cases) != 120:
        errors.append(f"expected 120 cases, got {len(cases)}")

    case_ids = [case.get("case_id") for case in cases if isinstance(case, dict)]
    if len(set(case_ids)) != len(case_ids):
        errors.append("case_id values must be unique")

    for index, case in enumerate(cases):
        if not isinstance(case, dict):
            errors.append(f"cases[{index}] must be an object")
            continue
        missing = sorted(REQUIRED_CASE_KEYS - set(case))
        if missing:
            errors.append(f"{case.get('case_id', index)} missing keys: {', '.join(missing)}")
        if case.get("difficulty") not in {"easy", "mid", "hard"}:
            errors.append(f"{case.get('case_id', index)} has invalid difficulty")
        conversation = case.get("conversation")
        if not isinstance(conversation, list) or not conversation:
            errors.append(f"{case.get('case_id', index)} conversation must be non-empty")

    expected_summary = data.get("summary", {})
    checks = {
        "by_difficulty": Counter(case.get("difficulty") for case in cases),
        "by_stage": Counter(case.get("stage") for case in cases),
        "by_track": Counter(case.get("track") for case in cases),
        "by_policy": Counter(case.get("policy_expectation", {}).get("decision") for case in cases),
        "by_evaluation_mode": Counter(case.get("evaluation_mode", "single") for case in cases),
    }
    for key, actual in checks.items():
        expected = expected_summary.get(key, {})
        if dict(actual) != expected:
            errors.append(f"summary.{key} mismatch: expected {expected}, actual {dict(actual)}")

    serialized = json.dumps(data, ensure_ascii=False)
    for path, value in walk(data):
        if path.rsplit(".", 1)[-1] in FORBIDDEN_KEYS:
            errors.append(f"forbidden key at {path}")
    for pattern in INTERNAL_REFERENCE_PATTERNS:
        if pattern.search(serialized):
            errors.append(f"possible internal reference matched: {pattern.pattern}")
    for pattern in SECRET_PATTERNS:
        if pattern.search(serialized):
            errors.append(f"possible secret matched: {pattern.pattern}")
    if MOBILE_PATTERN.search(serialized):
        errors.append("possible full mobile number found")
    if ID_CARD_PATTERN.search(serialized):
        errors.append("possible ID card number found")
    if BANK_ACCOUNT_PATTERN.search(serialized):
        errors.append("possible bank account number found")
    if EMAIL_PATTERN.search(serialized):
        errors.append("possible email address found")
    return errors


def validate_checksums(root: Path) -> list[str]:
    checksum_path = root / "SHA256SUMS"
    if not checksum_path.exists():
        return ["SHA256SUMS is missing"]
    errors: list[str] = []
    for line in checksum_path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        expected, relative = line.split("  ", 1)
        path = root / relative
        if not path.exists():
            errors.append(f"checksum target missing: {relative}")
        elif sha256(path) != expected:
            errors.append(f"checksum mismatch: {relative}")
    return errors


def main() -> int:
    root = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]
    dataset_path = root / "data" / "workforceops_benchmark_120_public_v1.json"
    errors = validate_dataset(dataset_path)
    errors.extend(validate_checksums(root))
    if errors:
        print(json.dumps({"ok": False, "errors": errors}, ensure_ascii=False, indent=2))
        return 1
    data = json.loads(dataset_path.read_text(encoding="utf-8"))
    print(
        json.dumps(
            {
                "ok": True,
                "pack_id": data["pack_id"],
                "case_count": len(data["cases"]),
                "by_difficulty": data["summary"]["by_difficulty"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
