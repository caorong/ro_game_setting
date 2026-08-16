#!/usr/bin/env python3
from __future__ import annotations

import csv
import json
from collections import defaultdict
from pathlib import Path
from typing import Any, Iterable

import yaml

ROOT = Path(__file__).resolve().parents[1]
VENDOR = ROOT / "vendor/rathena"
GENERATED = ROOT / "generated"
LOCK = yaml.safe_load((ROOT / "data/sources/rathena.lock.yml").read_text(encoding="utf-8"))
COMMIT = str(LOCK["commit"])
REPOSITORY = str(LOCK["repository"])
SOURCE = "db/pre-re/item_db_etc.yml"
START_MARKER = "<!-- generated-cards:start -->"
END_MARKER = "<!-- generated-cards:end -->"


def provenance() -> dict[str, str]:
    return {
        "repository": REPOSITORY,
        "commit": COMMIT,
        "mode": "PRERE",
        "path": SOURCE,
    }


def load_cards() -> list[dict[str, Any]]:
    path = VENDOR / SOURCE
    if not path.is_file():
        raise FileNotFoundError(f"missing {path}; run scripts/sync_rathena.py first")
    value = yaml.safe_load(path.read_text(encoding="utf-8"))
    rows = value.get("Body", []) if isinstance(value, dict) else []
    return [row for row in rows if isinstance(row, dict) and row.get("Type") == "Card"]


def write_jsonl(path: Path, rows: Iterable[dict[str, Any]]) -> int:
    path.parent.mkdir(parents=True, exist_ok=True)
    count = 0
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n")
            count += 1
    return count


def write_csv(path: Path, rows: Iterable[dict[str, Any]], fields: list[str]) -> int:
    path.parent.mkdir(parents=True, exist_ok=True)
    count = 0
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        for row in rows:
            writer.writerow(row)
            count += 1
    return count


def flatten(card: dict[str, Any]) -> dict[str, Any]:
    flags = card.get("Flags", {}) if isinstance(card.get("Flags"), dict) else {}
    trade = card.get("Trade", {}) if isinstance(card.get("Trade"), dict) else {}
    return {
        "id": card.get("Id"),
        "aegis_name": card.get("AegisName"),
        "name": card.get("Name"),
        "buy": card.get("Buy"),
        "sell": card.get("Sell"),
        "weight": card.get("Weight", 0),
        "slots": card.get("Slots", 0),
        "drop_announce": bool(flags.get("DropAnnounce", False)),
        "container": bool(flags.get("Container", False)),
        "no_drop": bool(trade.get("NoDrop", False)),
        "no_trade": bool(trade.get("NoTrade", False)),
        "no_cart": bool(trade.get("NoCart", False)),
        "no_storage": bool(trade.get("NoStorage", False)),
        "script": card.get("Script", ""),
    }


def markdown_escape(value: Any) -> str:
    return str(value).replace("|", "\\|").replace("\n", " ")


def update_marked_section(path: Path, content: str) -> None:
    text = path.read_text(encoding="utf-8") if path.exists() else ""
    block = f"{START_MARKER}\n{content.rstrip()}\n{END_MARKER}"
    if START_MARKER in text and END_MARKER in text:
        before, rest = text.split(START_MARKER, 1)
        _, after = rest.split(END_MARKER, 1)
        text = before.rstrip() + "\n\n" + block + after
    else:
        text = text.rstrip() + "\n\n" + block + "\n"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def build_pages(cards: list[dict[str, Any]]) -> int:
    directory = GENERATED / "reference/items/cards"
    directory.mkdir(parents=True, exist_ok=True)
    pages: dict[int, list[dict[str, Any]]] = defaultdict(list)
    for card in cards:
        card_id = int(card.get("Id", 0) or 0)
        pages[(card_id // 250) * 250].append(card)

    index_lines = [
        "# Pre-Renewal 卡片目录",
        "",
        f"> 来源：`{REPOSITORY}@{COMMIT}` 的 `{SOURCE}`。完整机器数据见 `generated/items/cards.jsonl`。",
        "",
    ]
    for start, page_cards in sorted(pages.items()):
        end = start + 249
        filename = f"{start:05d}-{end:05d}.md"
        index_lines.append(f"- [{start}-{end}]({filename}) — {len(page_cards)} 张卡片")
        lines = [
            f"# 卡片 {start}-{end}",
            "",
            "| ID | 卡片 | 重量 | 买价/卖价 | 脚本 |
|---:|---|---:|---|---|",
        ]
        for card in sorted(page_cards, key=lambda row: int(row.get("Id", 0) or 0)):
            script = str(card.get("Script", "")).strip()
            short_script = script if len(script) <= 100 else script[:97] + "..."
            lines.append(
                f"| {card.get('Id')} | {markdown_escape(card.get('Name', ''))} (`{card.get('AegisName', '')}`) | "
                f"{card.get('Weight', 0)} | {card.get('Buy', '')}/{card.get('Sell', '')} | `{markdown_escape(short_script)}` |"
            )
        lines.extend(["", "## 完整脚本效果", ""])
        for card in sorted(page_cards, key=lambda row: int(row.get("Id", 0) or 0)):
            script = card.get("Script")
            if not script:
                continue
            lines.extend([
                f"### {card.get('Name', card.get('AegisName'))} (`{card.get('Id')}` / `{card.get('AegisName')}`)",
                "",
                "```text",
                str(script).strip(),
                "```",
                "",
            ])
        (directory / filename).write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    (directory / "README.md").write_text("\n".join(index_lines) + "\n", encoding="utf-8")
    return len(pages)


def update_summary(records: int, csv_rows: int, pages: int) -> None:
    path = GENERATED / "summary.json"
    summary = json.loads(path.read_text(encoding="utf-8"))
    summary.setdefault("counts", {})["cards"] = {
        "records": records,
        "csv_rows": csv_rows,
        "pages": pages,
    }
    path.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def update_indexes(records: int, pages: int) -> None:
    item_index = GENERATED / "reference/items/README.md"
    text = item_index.read_text(encoding="utf-8")
    lines = [line for line in text.splitlines() if not line.startswith("- **cards**")]
    insert_at = len(lines)
    for index, line in enumerate(lines):
        if line.startswith("- **"):
            insert_at = index
            break
    lines.insert(insert_at, f"- **cards**：{records} 条（[浏览目录](cards/README.md)）")
    item_index.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")

    generated_readme = GENERATED / "README.md"
    update_marked_section(
        generated_readme,
        "\n".join([
            "## 卡片数据",
            "",
            f"- 卡片记录：**{records}**",
            f"- 浏览分页：**{pages}**",
            "- 机器数据：`items/cards.jsonl` / `items/cards.csv`",
            "- 浏览入口：`reference/items/cards/README.md`",
            "- 每张卡片保留完整 rAthena `Script`，用于还原属性、种族、体型、状态和触发效果。",
        ]),
    )


def main() -> int:
    cards = load_cards()
    if not cards:
        raise RuntimeError("no Pre-Renewal card records found")
    source = provenance()
    records = write_jsonl(
        GENERATED / "items/cards.jsonl",
        ({**card, "_source": source} for card in cards),
    )
    flat = [flatten(card) for card in cards]
    fields = list(flat[0].keys())
    csv_rows = write_csv(GENERATED / "items/cards.csv", flat, fields)
    pages = build_pages(cards)
    update_summary(records, csv_rows, pages)
    update_indexes(records, pages)
    print(json.dumps({"cards": records, "pages": pages}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
