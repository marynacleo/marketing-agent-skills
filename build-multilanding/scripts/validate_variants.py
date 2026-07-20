"""Validate a multilanding variants CSV (intent-first schema) with no external deps.

Usage:  python validate_variants.py variants.csv
Exit 0 = VALID, exit 1 = INVALID (errors printed).
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

# Intent-first data contract. Identity flows:
#   audience_id -> intent_id -> awareness_stage -> offer_id -> message_id
#   -> campaign_id/ad_group_id/creative_id -> id(landing_variant) -> conversion_action
REQUIRED = {
    "id", "slug", "status", "locale",
    "audience_id", "intent_id", "awareness_stage",
    "offer_id", "message_id",
    "campaign_id", "ad_group_id", "creative_id",
    "headline", "subheadline", "problem", "solution", "proof",
    "objection", "cta_label", "form_id", "conversion_action",
    "indexation_policy", "canonical_url", "evidence_status",
}

SLUG = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
STATUSES = {"draft", "active", "paused"}
STAGES = {"problem", "solution", "product", "most-aware"}
INDEXATION = {"noindex-paid", "canonical-to", "indexable-self", "test"}
EVIDENCE = {"confirmed", "derived", "hypothesis"}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv_file", type=Path)
    args = parser.parse_args()

    errors: list[str] = []
    with args.csv_file.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        fields = set(reader.fieldnames or [])
        missing = sorted(REQUIRED - fields)
        if missing:
            errors.append("missing columns: " + ", ".join(missing))
        rows = list(reader)

    seen_ids: dict[str, int] = {}
    seen_slugs: dict[str, int] = {}
    for line, row in enumerate(rows, start=2):
        status = (row.get("status") or "").strip()
        indexation = (row.get("indexation_policy") or "").strip()

        # Empty required fields. canonical_url is checked conditionally below,
        # because a noindex-paid or indexable-self page may legitimately omit it.
        for field in sorted((REQUIRED - {"canonical_url"}) & set(row)):
            if not (row.get(field) or "").strip():
                errors.append(f"line {line}: empty {field}")

        for field, seen in (("id", seen_ids), ("slug", seen_slugs)):
            value = (row.get(field) or "").strip()
            if value in seen:
                errors.append(f"line {line}: duplicate {field} {value!r} (first line {seen[value]})")
            elif value:
                seen[value] = line

        slug = (row.get("slug") or "").strip()
        if slug and not SLUG.fullmatch(slug):
            errors.append(f"line {line}: invalid slug {slug!r}")
        if status and status not in STATUSES:
            errors.append(f"line {line}: invalid status {status!r}")

        stage = (row.get("awareness_stage") or "").strip()
        if stage and stage not in STAGES:
            errors.append(f"line {line}: invalid awareness_stage {stage!r}")
        if indexation and indexation not in INDEXATION:
            errors.append(f"line {line}: invalid indexation_policy {indexation!r}")
        evidence = (row.get("evidence_status") or "").strip()
        if evidence and evidence not in EVIDENCE:
            errors.append(f"line {line}: invalid evidence_status {evidence!r}")

        canonical = (row.get("canonical_url") or "").strip()
        if indexation == "canonical-to" and not canonical:
            errors.append(f"line {line}: indexation_policy 'canonical-to' requires canonical_url")
        if canonical:
            parsed = urlparse(canonical)
            if parsed.scheme not in {"http", "https"} or not parsed.netloc:
                errors.append(f"line {line}: invalid canonical_url {canonical!r}")

    if errors:
        print("INVALID")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    active = sum((row.get("status") or "").strip() == "active" for row in rows)
    print(f"VALID rows={len(rows)} active={active}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
