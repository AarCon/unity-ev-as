import json
import os

DATA_FILES =  [
    'dp_scenario1',
    'dp_scenario2',
    'dp_scenario3',
    'dp_options',
    'ss_report' ,
    'dlp_underground' ,
    'dp_tvshow',
    'dlp_net_union_room',
    'dp_trainer_msg_sub',
    'dp_poffin_main',
    'ss_fld_shop',
    'dlp_gmstation',
    'dlp_rotom_message',
    'ss_fld_dressup',
    'dp_net_communication',
    'dp_contest',
    'ss_net_net_btl',
    'ss_btl_tower_main',
    'ss_btl_tower_menu_ui_text',
]

NEW_DATA_FILES = [
    "battle_room",
    "bg_attr",
    "common_scr",
    "connect",
    "con_reception",
    "debug_scr",
    "door",
    "dummy",
    "dummy_scr",
    "fld_item",
    "game_clear",
    "global_defines",
    "group",
    "haitatu",
    "hide_item",
    "hiden",
    "hyouka_scr",
    "init_scr",
    "kinomi",
    "pair_scr",
    "pc_ug",
    "perap",
    "pokesearcher",
    "poruto_scr",
    "safari",
    "saisen",
    "scr_seq_def",
    "sodateya",
    "support",
    "trainer",
    "tutor",
    "tv",
    "tv_interview",
]

# append new data files to DATA_FILES
for new_file in NEW_DATA_FILES:
    DATA_FILES.append(f"dialogue_{new_file}")

_THIS_DIR = os.path.dirname(__file__)
_ZONE_JSON = os.path.join(_THIS_DIR, "zone_codes.json")
try:
    with open(_ZONE_JSON, "r", encoding="utf-8") as fh:
        _zone_list = json.load(fh)
except Exception:
    _zone_list = []

# append zone codes (lowercased) to DATA_FILES, avoid duplicates and empty entries
for z in _zone_list:
    if not z:
        continue
    zname = str(z).strip().lower()
    if zname and zname not in DATA_FILES:
        DATA_FILES.append(f"dialogue_{zname}")

class GDataManager:
    SCENARIO_MSGS = None
    DISABLED_MSGS = False

    @classmethod
    def getMoveById(cls, moveId):
        move_list = cls.getMoveList()
        return move_list[moveId]

    @classmethod
    def getScenarioMsgList(cls):
        if cls.DISABLED_MSGS:
            return None
        if not cls.SCENARIO_MSGS:
            scenario_msgs = {}

            try:
                for dateFile in DATA_FILES:
                    ifpath = "AssetFolder/english_Export/english_{}.json".format(dateFile)
                    array = []
                    with open(ifpath, "r", encoding='utf-8') as ifobj:
                        data = json.load(ifobj)
                        for entry in data["labelDataArray"]:
                            labelName = entry["labelName"]
                            array.append(labelName)
                    scenario_msgs[dateFile] = array
            except FileNotFoundError as exc:
                cls.DISABLED_MSGS = True
                print("Warning: english files not found. Message validation will not be enabled: {}".format(exc))
                return None
            cls.SCENARIO_MSGS = scenario_msgs
        return cls.SCENARIO_MSGS    