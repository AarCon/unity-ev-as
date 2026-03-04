import json
import os
from typing import Optional

_THIS_DIR = os.path.dirname(__file__)
_JSON_PATH = os.path.join(_THIS_DIR, "zone_codes.json")

class ZoneLookup:
    def __init__(self, json_path: str = _JSON_PATH):
        self._id_to_code = {}
        self._code_to_id = {}
        try:
            with open(json_path, "r", encoding="utf-8") as fh:
                arr = json.load(fh)
        except Exception:
            arr = []

        for zid, zcode in enumerate(arr):
            if zcode is None:
                continue
            self._id_to_code[zid] = str(zcode)
            self._code_to_id[str(zcode)] = zid

    def id_to_code(self, zone_id) -> Optional[str]:
        try:
            zid = int(zone_id)
        except Exception:
            return None
        return self._id_to_code.get(zid).lower()

    def code_to_id(self, zone_code) -> Optional[int]:
        if zone_code is None:
            return None
        return self._code_to_id.get(str(zone_code).strip())

    def lookup(self, key):
        try:
            return self.id_to_code(int(key))
        except Exception:
            return self.code_to_id(key)

zone_lookup = ZoneLookup()

def get_zone_code(zone_id):
    return zone_lookup.id_to_code(zone_id)

def get_zone_id(zone_code):
    return zone_lookup.code_to_id(zone_code.upper())