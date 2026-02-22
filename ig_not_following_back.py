#!/usr/bin/env python3
import json
from pathlib import Path

def load_following(path: Path):
    data = json.loads(path.read_text(encoding="utf-8"))
    # Structure varies by export:
    # {"relationships_following": [{"title": "username", "string_list_data": [...]}, ...]}
    # Some exports include username in string_list_data[].value instead of title.
    following = set()
    for item in data.get("relationships_following", []):
        title = item.get("title")
        if title:
            following.add(title.lower())
            continue
        for sld in item.get("string_list_data", []):
            val = sld.get("value")
            if val:
                following.add(val.lower())
    return following


def load_followers(paths):
    followers = set()
    for path in paths:
        data = json.loads(path.read_text(encoding="utf-8"))
        # Structure: [{"string_list_data": [{"value": "username", ...}], ...}, ...]
        # Some exports wrap it as {"relationships_followers": [...]}
        items = data.get("relationships_followers", []) if isinstance(data, dict) else data
        for item in items:
            for sld in item.get("string_list_data", []):
                val = sld.get("value")
                if val:
                    followers.add(val.lower())
    return followers


def main(export_root: Path):
    base = export_root
    following_path = base / "following.json"
    if not following_path.exists():
        raise SystemExit(f"Missing {following_path}")

    followers_paths = sorted(base.glob("followers_*.json"))
    if not followers_paths:
        raise SystemExit(f"No followers_*.json found in {base}")

    following = load_following(following_path)
    followers = load_followers(followers_paths)

    not_following_back = sorted(following - followers)
    for u in not_following_back:
        print(u)


if __name__ == "__main__":
    # Pass the root folder you extracted from Instagram export
    # Example: python3 ig_not_following_back.py ~/Downloads/instagram-data
    import sys
    if len(sys.argv) != 2:
        print("Usage: python3 ig_not_following_back.py /path/to/instagram-export")
        raise SystemExit(2)
    main(Path(sys.argv[1]))
