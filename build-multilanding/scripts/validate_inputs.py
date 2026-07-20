"""Validate the project marketing context before generating landing variants.

Checks that source-map.yaml resolves to real files and that keyword-intents.csv
has the required shape. Missing sources are reported as context gaps (UNKNOWN)
so the skill stops instead of inventing audiences, offers or keywords.

Usage:  python validate_inputs.py path/to/source-map.yaml [--root PROJECT_ROOT]
Exit 0 = all referenced sources present, exit 1 = context gaps or errors.

No external dependencies: source-map.yaml is read with a minimal flat parser
(top-level `key: value` lines only, which is all this check needs).
"""

from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

# Keys in source-map.yaml that must point to an existing file or directory.
PATH_KEYS = (
    "audiences", "offers", "proof", "messages", "keyword_intents",
    "brand_voice", "restrictions", "tracking", "campaigns", "experiments",
)

KEYWORD_INTENT_COLUMNS = {
    "intent_id", "query_cluster", "keywords", "audience_hypothesis",
    "awareness_stage", "offer_id", "message_id", "status",
}
INTENT_STATUSES = {"confirmed", "derived", "hypothesis", "rejected"}


def read_flat_yaml(path: Path) -> dict[str, str]:
    """Parse top-level `key: value` pairs; ignore lists, nesting and comments."""
    values: dict[str, str] = {}
    for raw in path.read_text(encoding="utf-8").splitlines():
        if not raw or raw[0] in " #-" or ":" not in raw:
            continue
        key, _, value = raw.partition(":")
        value = value.split("#", 1)[0].strip().strip('"').strip("'")
        if value:
            values[key.strip()] = value
    return values


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source_map", type=Path)
    parser.add_argument("--root", type=Path, default=None,
                        help="project root for relative paths (default: cwd)")
    args = parser.parse_args()

    if not args.source_map.is_file():
        print("INVALID")
        print(f"- source-map not found: {args.source_map}")
        return 1

    root = args.root or Path.cwd()
    mapping = read_flat_yaml(args.source_map)

    gaps: list[str] = []
    for key in PATH_KEYS:
        target = mapping.get(key)
        if not target:
            gaps.append(f"UNKNOWN: source-map has no path for '{key}'")
            continue
        resolved = (root / target)
        if not resolved.exists():
            gaps.append(f"UNKNOWN: '{key}' -> {target} does not exist")

    errors: list[str] = []
    ki = mapping.get("keyword_intents")
    if ki and (root / ki).is_file():
        with (root / ki).open("r", encoding="utf-8-sig", newline="") as handle:
            reader = csv.DictReader(handle)
            cols = set(reader.fieldnames or [])
            missing = sorted(KEYWORD_INTENT_COLUMNS - cols)
            if missing:
                errors.append("keyword-intents.csv missing columns: " + ", ".join(missing))
            for line, row in enumerate(reader, start=2):
                status = (row.get("status") or "").strip()
                if status and status not in INTENT_STATUSES:
                    errors.append(f"keyword-intents.csv line {line}: invalid status {status!r}")

    if gaps or errors:
        print("INVALID")
        print("\n".join(f"- {item}" for item in (*gaps, *errors)))
        return 1
    print("VALID inputs: all referenced sources present")
    return 0


if __name__ == "__main__":
    sys.exit(main())
