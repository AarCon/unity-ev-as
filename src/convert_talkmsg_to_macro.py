#!/usr/bin/env python3
"""
convert_talkmsg_to_macro.py — Batch converts _TALKMSG/_TALK_KEYWAIT
calls in .ev files to explicit macro calls using existing
constants from the codebase rather than a unified _MACRO_MSG format.

This script uses `msbt.MsgEventID` constants for mapping event IDs to
escape sequences and parses Unity YAML `.asset` files under
`Assets/format_msbt/en/english/english_{file}.asset` to extract labels.

Usage:
  python tools/convert_talkmsg_to_macro.py [--dry-run] [--file path.ev]
"""
from __future__ import annotations

import os
import re
import sys
import argparse
import glob
from typing import Dict
from ev_parse import decode_unity_yaml
import yaml
from yamlcore import CoreLoader
import json

ROOT = os.path.dirname(os.path.dirname(__file__))
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
SCRIPTS_DIR = os.path.join(ROOT, 'scripts')
ASSETS_DIR = os.path.join(ROOT, 'Assets', 'format_msbt', 'en', 'english')

from msbt import MsgEventID
from ev_zone_code import get_zone_id

# Commands that can be converted: map the ev command name to a target macro
CONVERTIBLE_COMMANDS = {
    '_TALKMSG': '_MACRO_TALKMSG',
    '_TALK_KEYWAIT': '_MACRO_TALK_KEYWAIT',
    '_EASY_OBJ_MSG': '_MACRO_EASY_OBJ_MSG',
}

# Map msbt.MsgEventID values to escape sequences used in .ev text format
EVENT_ID_MAP = {
    MsgEventID.NewLine.value: '\\n',
    MsgEventID.ScrollPage.value: '\\r',
    MsgEventID.ScrollLine.value: '\\f',
    MsgEventID.End.value: '',
}

un_macroable_labels = []
non_existant_labels = []

def parse_message_asset(filepath: str) -> Dict[str, str]:
    """Parse a Unity YAML message asset into a dict mapping labelName -> text.

    Uses decode_unity_yaml + PyYAML CoreLoader to get a structured dict
    (same approach as loadYamlCoreLabels in ev_as), then builds text
    from tagDataArray/wordDataArray.

    Tag placeholders will be emitted as:
      {tagIndex,groupID,tagID,tagParam,tagPatternID}
    where numeric values are taken from the tag entry (fallbacks applied).
    """
    labels: Dict[str, str] = {}
    if not os.path.exists(filepath):
        return labels

    with open(filepath, 'r', encoding='utf-8') as fh:
        try:
            decoded = decode_unity_yaml(fh)
            bundle = yaml.load(decoded, Loader=CoreLoader)
            tree = bundle.get("MonoBehaviour", {})
        except Exception:
            return labels

    for label_entry in tree.get("labelDataArray", []):
        name = label_entry.get("labelName")
        if not name:
            continue

        # Build tag index list with full info: (tagIndex, groupID, tagID, tagParam, patternID)
        tag_entries = []
        unsupported_group = False
        for tag in label_entry.get("tagDataArray", []):
            if isinstance(tag, dict):
                ti = int(tag.get("tagIndex", 0) or 0)
                gid = int(tag.get("groupID", 1) or 1)
                tid = int(tag.get("tagID", 0) or 0)
                tparam = int(tag.get("tagParam", 0) or 0)
                pat = tag.get("patternID", None)
            else:
                ti = int(getattr(tag, "tagIndex", 0) or 0)
                gid = int(getattr(tag, "groupID", 1) or 1)
                tid = int(getattr(tag, "tagID", 0) or 0)
                tparam = int(getattr(tag, "tagParam", 0) or 0)
                pat = getattr(tag, "patternID", None)

            # If groupID is not supported (1=Name,2=Digit), mark unsupported and stop
            if gid not in (1, 2):
                unsupported_group = True
                break

            tag_entries.append((ti, gid, tid, tparam))

        if unsupported_group:
            # skip this label — contains unsupported groupID entries so don't convert
            un_macroable_labels.append(name)
            continue

        text_parts = []
        for wd in label_entry.get("wordDataArray", []):
            # handle dict or object-like entry
            if isinstance(wd, dict):
                s = wd.get("str")
                tindex = wd.get("tagIndex", -1)
                event_id = wd.get("eventID")
            else:
                s = getattr(wd, "str", None)
                tindex = getattr(wd, "tagIndex", -1)
                event_id = getattr(wd, "eventID", None)

            if s:
                text_parts.append(s)

            # Tag placeholders: emit full tuple if tag index present
            try:
                ti = int(tindex) if tindex is not None else -1
            except Exception:
                ti = -1

            if ti != -1:
                if 0 <= ti < len(tag_entries):
                    te = tag_entries[ti]
                    # Use the tag entry's tagIndex (te[0]) and other numeric fields
                    text_parts.append("{" + ",".join(str(x) for x in te) + "}")
                else:
                    # Unknown reference; still emit what we have
                    text_parts.append("{" + str(ti) + ",1,0,0,0}")

            # Translate message event IDs to escape sequences
            if event_id is not None:
                try:
                    ev = int(event_id)
                except Exception:
                    ev = None
                if ev is not None:
                    esc = EVENT_ID_MAP.get(ev, "")
                    if esc:
                        text_parts.append(esc)

        # Extract controlID from styleInfo if present (handle dict or object-like)
        control_id = 0
        style_info = label_entry.get("styleInfo", {})
        if isinstance(style_info, dict):
            control_id = int(style_info.get("controlID", 0) or 0)
        else:
            control_id = int(getattr(style_info, "controlID", 0) or 0)

        labels[name] = ("".join(text_parts), control_id)

    return labels


_message_cache: Dict[str, Dict[str, str]] = {}


def get_message(file_name: str, label_name: str) -> str | None:
    if file_name not in _message_cache:
        print("Adding file to cache:", file_name)
        asset_path = os.path.join(ASSETS_DIR, f'english_{file_name}.asset')
        _message_cache[file_name] = parse_message_asset(asset_path)
    message = _message_cache[file_name].get(label_name)
    if message is None:
        if label_name not in un_macroable_labels:
            non_existant_labels.append(label_name)
    return message


def escape_for_macro(text: str) -> str:
    # Replace ASCII apostrophes with right single quotation mark
    return text.replace("'", "\u2019")


def convert_line(line: str, script_base: str | None = None) -> tuple[str, bool]:
    # Pattern: optional indent, command, ( 'file%label' [ , ... ] )
    cmd_group = '|'.join(re.escape(c) for c in CONVERTIBLE_COMMANDS.keys())
    pattern = re.compile(rf"^(\s*)({cmd_group})\s*\(\s*(['\"])([^'\"]+?)\3\s*((?:\s*,\s*[^)]*)?)\s*\)")
    m = pattern.match(line)
    if not m:
        print("Could not match")
        return line, False

    indent, command, _, ref = m.group(1), m.group(2), m.group(3), m.group(4)
    trailing = m.group(5) or ""

    if '%' not in ref:
        print("Did not convert")
        return line, False

    file_name, label_name = ref.split('%', 1)

    # If the script's basename is a known zone code, override the message file name
    # if script_base:
    #     try:
    #         if get_zone_id(script_base) is not None:
    #             file_name = script_base
    #     except Exception:
    #         pass

    ALLOWED_FILES = {
        "dp_scenario1",
        "dp_scenario2",
        "dp_scenario3",
        "dlp_underground"
    }
    if file_name not in ALLOWED_FILES:
        return line, False

    with open(os.path.join(FILE_DIR, 'ui_scenario_strings.json'), 'r', encoding='utf-8') as excluded_label_file:
        excluded_labels = json.load(excluded_label_file)

    if label_name in excluded_labels:
        print("Did not convert: ", label_name)
        return line, False

    msg = get_message(file_name, label_name)
    if msg is None:
        return line, False

    text, control_id = msg
    safe_text = escape_for_macro(text)
    macro_name = CONVERTIBLE_COMMANDS.get(command, command)

    args = [f"'{file_name}'", f"'{label_name}'", f"'{safe_text}'"]
    trailing_str = trailing.strip()
    if trailing_str.startswith(','):
        trailing_str = trailing_str[1:].strip()
    if trailing_str:
        args.append(trailing_str)

    # Ensure 4th arg placeholder so controlID is always 5th if present
    if len(args) == 4:
        args.append('0')

    if control_id != 0:
        args.append(str(control_id))

    new_line = f"{indent}{macro_name}(" + ", ".join(args) + ")"

    return new_line, True


def process_file(path: str, dry_run: bool = False, use_ev_basename: bool = False) -> tuple[int, int]:
    with open(path, 'r', encoding='utf-8') as fh:
        lines = fh.readlines()

    ev_basename = os.path.splitext(os.path.basename(path))[0] if use_ev_basename else None

    new_lines = []
    total = 0
    converted = 0
    for ln in lines:
        stripped = ln.strip()
        has_cmd = any(stripped.startswith(cmd + '(') or stripped.startswith(cmd + ' (') for cmd in CONVERTIBLE_COMMANDS)
        if has_cmd and '%' in ln:
            total += 1
            new, ok = convert_line(ln.rstrip('\n'), script_base=ev_basename)
            if ok:
                converted += 1
                new_lines.append(new + '\n')
                continue
        new_lines.append(ln)

    if converted and not dry_run:
        with open(path, 'w', encoding='utf-8') as fh:
            fh.writelines(new_lines)

    return total, converted


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dry-run', action='store_true')
    parser.add_argument('--file', type=str)
    parser.add_argument('--use-ev-basename', action='store_true',
                        help='When set, if the .ev filename (basename) is a known zone code, use it as the message file_name override.')
    args = parser.parse_args()

    files = [args.file] if args.file else sorted(glob.glob(os.path.join(SCRIPTS_DIR, '*.ev')))
    if not files:
        print('No .ev files found')
        return

    total_files_modified = 0
    total_conv = 0
    total_matches = 0
    for p in files:
        matches, conv = process_file(p, dry_run=args.dry_run, use_ev_basename=args.use_ev_basename)
        if matches:
            print(f"{os.path.basename(p)}: {conv}/{matches} converted")
        total_matches += matches
        total_conv += conv
        if conv:
            total_files_modified += 1

    print("Un-macroable labels:")
    for label in un_macroable_labels:
        print(f"- {label}")
    print("Non-existant labels:")
    for label in non_existant_labels:
        print(f"- {label}")
    print(f"Total: {total_conv}/{total_matches} across {total_files_modified} files")
    if args.dry_run:
        print('(dry run — no files written)')


if __name__ == '__main__':
    main()
