# IG Follow Checker

Simple Python scripts to find Instagram accounts you follow that do not follow you back.

## What This Repo Contains

- `ig_not_following_back.py`: works with Instagram export **JSON** files.
- `ig_not_following_back_html.py`: works with Instagram export **HTML** files.
- `followers_1.html` and `following.html`: example input files.

## Requirements

- Python 3.10+ (3.11+ recommended)
- No third-party dependencies

## Quick Start

Run from the project root:

```bash
python3 ig_not_following_back_html.py --followers followers_1.html --following following.html
```

## Usage

### Option 1: HTML Export Files

If you have Instagram export files like `followers_1.html` and `following.html`:

```bash
python3 ig_not_following_back_html.py --followers followers_1.html --following following.html
```

Defaults are:

- `--followers followers_1.html`
- `--following following.html`

So this also works when files use default names:

```bash
python3 ig_not_following_back_html.py
```

### Option 2: JSON Export Folder

If you extracted an Instagram export folder containing:

- `following.json`
- one or more `followers_*.json` files

Run:

```bash
python3 ig_not_following_back.py /path/to/instagram-export
```

Example:

```bash
python3 ig_not_following_back.py ~/Downloads/instagram-data
```

## Output

The scripts print usernames you follow who are not following you back.

The HTML version also prints summary counts first:

- total following
- total followers
- total not following back

## Common Issues

- `Missing followers file` or `Missing following file`:
  Check file names and paths for the HTML script.
- `Missing following.json`:
  The JSON script expects `following.json` in the folder you pass.
- `No followers_*.json found`:
  The JSON script expects one or more follower files matching that pattern.

## Notes

- Usernames are normalized to lowercase before comparison.
- Results are sorted alphabetically.

## License

Add a license file if you plan to share this publicly.
