#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path
from typing import Iterable

import yaml

ROOT = Path(__file__).resolve().parents[1]
LOCK_PATH = ROOT / "data/sources/rathena.lock.yml"
FILES_PATH = ROOT / "data/sources/rathena_files.yml"
VENDOR = ROOT / "vendor/rathena"


def load_yaml(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def request(url: str, token: str | None = None, retries: int = 3) -> bytes:
    headers = {"User-Agent": "ro-game-setting-sync/1.0", "Accept": "application/vnd.github+json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    last_error: Exception | None = None
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=60) as response:
                return response.read()
        except (urllib.error.URLError, TimeoutError) as exc:
            last_error = exc
            if attempt + 1 < retries:
                time.sleep(2 ** attempt)
    raise RuntimeError(f"failed to download {url}: {last_error}")


def github_tree(repository: str, commit: str, token: str | None) -> list[dict]:
    api = f"https://api.github.com/repos/{repository}/git/trees/{commit}?recursive=1"
    payload = json.loads(request(api, token).decode("utf-8"))
    if payload.get("truncated"):
        raise RuntimeError("GitHub recursive tree response was truncated; use a token or narrower source lock")
    return payload.get("tree", [])


def depth_from(prefix: str, path: str) -> int:
    suffix = path[len(prefix):].strip("/")
    return 0 if not suffix else suffix.count("/") + 1


def selected_paths(tree: list[dict], config: dict, include_skill_source: bool) -> list[str]:
    available = {entry["path"]: entry for entry in tree if entry.get("type") == "blob"}
    selected = set(config.get("always_include", []))
    excluded = tuple(config.get("excluded_prefixes", []))

    for rule in config.get("tree_filters", []):
        if rule.get("optional_flag") == "--include-skill-source" and not include_skill_source:
            continue
        prefix = rule["prefix"]
        max_depth = rule.get("depth")
        extensions = tuple(rule.get("extensions", []))
        for path in available:
            if not path.startswith(prefix) or path.startswith(excluded):
                continue
            if max_depth is not None and depth_from(prefix, path) > max_depth:
                continue
            if extensions and not path.endswith(extensions):
                continue
            selected.add(path)

    missing = sorted(path for path in selected if path not in available)
    if missing:
        raise RuntimeError("locked paths missing upstream: " + ", ".join(missing))
    return sorted(selected)


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description="Sync pinned rAthena Pre-Renewal sources")
    parser.add_argument("--include-skill-source", action="store_true", help="download every src/map/skills .cpp/.hpp")
    parser.add_argument("--verify-only", action="store_true", help="verify existing files against sync-manifest.json")
    parser.add_argument("--clean", action="store_true", help="remove vendor directory before download")
    args = parser.parse_args()

    lock = load_yaml(LOCK_PATH)
    config = load_yaml(FILES_PATH)
    repository = lock["repository"]
    commit = lock["commit"]
    token = os.environ.get("GITHUB_TOKEN")
    manifest_path = VENDOR / "sync-manifest.json"

    if lock.get("mode") != "PRERE":
        raise RuntimeError("source lock is not PRERE")

    if args.verify_only:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        failures = []
        for item in manifest["files"]:
            path = VENDOR / item["path"]
            if not path.exists() or sha256(path.read_bytes()) != item["sha256"]:
                failures.append(item["path"])
        if failures:
            print("verification failed:", *failures, sep="\n- ", file=sys.stderr)
            return 1
        print(f"verified {len(manifest['files'])} files at {commit}")
        return 0

    if args.clean and VENDOR.exists():
        import shutil
        shutil.rmtree(VENDOR)
    VENDOR.mkdir(parents=True, exist_ok=True)

    tree = github_tree(repository, commit, token)
    paths = selected_paths(tree, config, args.include_skill_source)
    raw_base = lock["raw_base_url"].rstrip("/")
    records = []

    for index, path in enumerate(paths, 1):
        data = request(f"{raw_base}/{path}", token)
        destination = VENDOR / path
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes(data)
        records.append({"path": path, "size": len(data), "sha256": sha256(data)})
        print(f"[{index}/{len(paths)}] {path}")

    manifest = {
        "repository": repository,
        "commit": commit,
        "mode": "PRERE",
        "include_skill_source": args.include_skill_source,
        "files": records,
    }
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"synced {len(records)} files to {VENDOR}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
