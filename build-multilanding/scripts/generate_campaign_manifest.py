"""Generate a campaign/URL manifest from active landing variants.

Reads variants.csv, keeps active rows, and emits one manifest row per variant:
the ad mapping (campaign/ad_group/creative), the full landing URL, tagged UTMs
and the indexation policy. This manifest is the bridge you paste into the ad
account and the analytics plan.

Usage:
  python generate_campaign_manifest.py variants.csv --base-url https://example.com \
      [--default-locale fr] [--utm-source google] [--utm-medium cpc] [--out manifest.csv]

No external dependencies.
"""

from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path
from urllib.parse import urlencode

MANIFEST_COLUMNS = [
    "landing_variant_id", "campaign_id", "ad_group_id", "creative_id",
    "intent_id", "locale", "landing_url", "final_url", "indexation_policy",
]


def build_url(base: str, locale: str, slug: str, default_locale: str) -> str:
    base = base.rstrip("/")
    prefix = "" if locale == default_locale else f"/{locale}"
    return f"{base}{prefix}/{slug}"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv_file", type=Path)
    parser.add_argument("--base-url", required=True)
    parser.add_argument("--default-locale", default="fr")
    parser.add_argument("--utm-source", default="google")
    parser.add_argument("--utm-medium", default="cpc")
    parser.add_argument("--out", type=Path, default=None)
    args = parser.parse_args()

    with args.csv_file.open("r", encoding="utf-8-sig", newline="") as handle:
        rows = [r for r in csv.DictReader(handle)
                if (r.get("status") or "").strip() == "active"]

    manifest: list[dict[str, str]] = []
    for row in rows:
        locale = (row.get("locale") or args.default_locale).strip()
        slug = (row.get("slug") or "").strip()
        url = build_url(args.base_url, locale, slug, args.default_locale)
        utm = urlencode({
            "utm_source": args.utm_source,
            "utm_medium": args.utm_medium,
            "utm_campaign": (row.get("campaign_id") or "").strip(),
            "utm_content": (row.get("creative_id") or "").strip(),
        })
        manifest.append({
            "landing_variant_id": (row.get("id") or "").strip(),
            "campaign_id": (row.get("campaign_id") or "").strip(),
            "ad_group_id": (row.get("ad_group_id") or "").strip(),
            "creative_id": (row.get("creative_id") or "").strip(),
            "intent_id": (row.get("intent_id") or "").strip(),
            "locale": locale,
            "landing_url": url,
            "final_url": f"{url}?{utm}",
            "indexation_policy": (row.get("indexation_policy") or "").strip(),
        })

    out = args.out.open("w", encoding="utf-8", newline="") if args.out else sys.stdout
    try:
        writer = csv.DictWriter(out, fieldnames=MANIFEST_COLUMNS)
        writer.writeheader()
        writer.writerows(manifest)
    finally:
        if args.out:
            out.close()

    if args.out:
        print(f"wrote {len(manifest)} rows to {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
