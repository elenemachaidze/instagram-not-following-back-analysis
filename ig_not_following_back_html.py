#!/usr/bin/env python3
import argparse
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse


def username_from_instagram_url(url: str) -> str | None:
    parsed = urlparse(url)
    host = parsed.netloc.lower()
    if "instagram.com" not in host:
        return None

    parts = [part for part in parsed.path.split("/") if part]
    if not parts:
        return None

    first = parts[0].strip().lower()
    if first == "_u" and len(parts) > 1:
        username = parts[1].strip().lower()
        return username or None

    if first and first not in {"accounts", "explore", "p"}:
        return first
    return None


class InstagramUserHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.users: set[str] = set()

    def handle_starttag(self, tag, attrs):
        if tag.lower() != "a":
            return

        href = None
        for key, value in attrs:
            if key.lower() == "href":
                href = value
                break

        if not href:
            return

        username = username_from_instagram_url(href)
        if username:
            self.users.add(username)


def load_users_from_html(path: Path) -> set[str]:
    parser = InstagramUserHTMLParser()
    parser.feed(path.read_text(encoding="utf-8", errors="ignore"))
    return parser.users


def main():
    argp = argparse.ArgumentParser(
        description="Find Instagram accounts you follow that do not follow you back."
    )
    argp.add_argument(
        "--followers",
        default="followers_1.html",
        help="Path to followers HTML file (default: followers_1.html)",
    )
    argp.add_argument(
        "--following",
        default="following.html",
        help="Path to following HTML file (default: following.html)",
    )
    args = argp.parse_args()

    followers_path = Path(args.followers)
    following_path = Path(args.following)

    if not followers_path.exists():
        raise SystemExit(f"Missing followers file: {followers_path}")
    if not following_path.exists():
        raise SystemExit(f"Missing following file: {following_path}")

    followers = load_users_from_html(followers_path)
    following = load_users_from_html(following_path)

    not_following_back = sorted(following - followers)

    print(f"Following: {len(following)}")
    print(f"Followers: {len(followers)}")
    print(f"Not following back: {len(not_following_back)}")
    print()

    for username in not_following_back:
        print(username)


if __name__ == "__main__":
    main()
