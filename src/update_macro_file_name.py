#!/usr/bin/env python3
"""
update_macro_file_name.py — Update existing _MACRO_TALKMSG / _MACRO_TALK_KEYWAIT
calls in .ev files so their first (file_name) argument matches the containing
.ev filename (basename) when that basename is a known zone code.

Only updates macros for allowed message files and skips excluded labels
(same rules as convert_talkmsg_to_macro.py).
"""
from __future__ import annotations

import argparse
import glob
import os
import re
from typing import Tuple

from ev_zone_code import get_zone_id

FILE_DIR = os.path.dirname(__file__)

MACROS = ("_MACRO_TALKMSG", "_MACRO_TALK_KEYWAIT")
MACRO_RE = re.compile(r"^(\s*)(" + "|".join(re.escape(m) for m in MACROS) + r")\s*\(\s*(['\"])([^'\"]+?)\3(.*)\)\s*$")

# Same allowed files as convert_talkmsg_to_macro.py
ALLOWED_FILES = {
    "dp_scenario1",
    "dp_scenario2",
    "dp_scenario3",
    "dlp_underground"
}

# load excluded labels (if present)
def _load_excluded_labels():
    path = os.path.join(FILE_DIR, "ui_scenario_strings.json")
    try:
        import json
        with open(path, "r", encoding="utf-8") as fh:
            data = json.load(fh)
            if isinstance(data, list):
                return set(data)
    except Exception:
        pass
    return set()

EXCLUDED_LABELS = _load_excluded_labels()

def process_file(path: str, dry_run: bool = False) -> Tuple[int,int]:
    """Return (matches_seen, replaced_count)."""
    with open(path, "r", encoding="utf-8") as fh:
        lines = fh.readlines()

    ev_basename = os.path.splitext(os.path.basename(path))[0]
    if get_zone_id(ev_basename) is None:
        return 0, 0  # only operate when file basename is a known zone code


    new_lines = []
    matches = 0
    replaced = 0
    for ln in lines:
        m = MACRO_RE.match(ln.rstrip("\n"))
        if not m:
            new_lines.append(ln)
            continue
        matches += 1
        indent, macro, quote, file_name, rest = m.group(1), m.group(2), m.group(3), m.group(4), m.group(5)

        # extract the label (expected to be the immediate next argument)
        label_match = re.match(r"\s*,\s*(['\"])([^'\"]+?)\1", rest)
        if not label_match:
            # if we can't parse the label, skip modifying this line
            new_lines.append(ln)
            continue
        label_name = label_match.group(2)

        # only update if the current message file is in the allowed set
        if file_name not in ALLOWED_FILES:
            new_lines.append(ln)
            continue

        # skip excluded labels
        if label_name in EXCLUDED_LABELS:
            new_lines.append(ln)
            continue

        if file_name == ev_basename:
            new_lines.append(ln)
            continue

        dialogue_file_name = f"dialogue_{ev_basename}"

        # build replacement: keep same quote char
        new_line = f"{indent}{macro}({quote}{dialogue_file_name}{quote}{rest})\n"
        replaced += 1
        new_lines.append(new_line)

    if replaced and not dry_run:
        with open(path, "w", encoding="utf-8") as fh:
            fh.writelines(new_lines)

    return matches, replaced

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--dry-run", action="store_true")
    p.add_argument("--file", type=str, help=".ev file to process")
    p.add_argument("--dir", type=str, default=None, help="directory to scan for .ev files (defaults to scripts/)")
    args = p.parse_args()

    root_dir = args.dir if args.dir else os.path.join(os.path.dirname(os.path.dirname(__file__)), "scripts")
    files = [args.file] if args.file else sorted(glob.glob(os.path.join(root_dir, "*.ev")))
    if not files:
        print("No .ev files found")
        return

    total_matches = 0
    total_replaced = 0
    for f in files:
        matches, replaced = process_file(f, dry_run=args.dry_run)
        if matches:
            print(f"{os.path.basename(f)}: {replaced}/{matches} replaced")
        total_matches += matches
        total_replaced += replaced

    print(f"Total replaced: {total_replaced}/{total_matches}")
    if args.dry_run:
        print("(dry run — no files written)")

if __name__ == "__main__":
    main()