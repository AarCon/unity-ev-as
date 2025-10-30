from copy import copy
import os
import struct
import json
import glob
import yaml
from yamlcore import CoreLoader
from yamlcore import CoreDumper
import sys
from argparse import ArgumentParser
import hashlib
import time

import UnityPy
from gdatamanger import DATA_FILES
import marshmallow

from antlr4 import *
from evAssembler import EvCmd, evAssembler
from evLexer import evLexer
from evParser import evParser

from ev_argtype import EvArgType
from ev_work import EvWork
from ev_sys_flag import EvSysFlag
from ev_flag import EvFlag
from ev_cmd import EvCmdType

from function_definitions import FunctionDefinition
from msbt import (
    MsbtFile,
    LabelData,
    LabelData,
    WordData,
    WordDataPatternID,
    MsgEventID,
    GroupTagID,
    TagPatternID,
    ForceGrmID,
    TagID,
)
from validator import Validator
from ev_parse import decode_unity_yaml
from dataclasses import asdict

CACHE_FILE = "file_hash_cache.json"
LABEL_CACHE_FILE = "label_hash_cache.json"


def jsonDumpUnity(tree, ofpath):
    with open(ofpath, "w") as ofobj:
        json.dump(tree, ofobj, indent=4)


def int_enum_representer(dumper, data):
    # Convert the enum to its integer value and represent as scalar
    return dumper.represent_scalar("tag:yaml.org,2002:int", str(int(data)))


def none_representer(dumper, data):
    return dumper.represent_scalar("tag:yaml.org,2002:null", "")


def dataclass_representer(dumper, data):
    return dumper.represent_dict(data.to_yaml_dict())


def calculate_file_hash(filepath):
    """Calculate the hash of a file to detect changes."""
    hasher = hashlib.md5()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hasher.update(chunk)
    return hasher.hexdigest()


def file_has_changed(filepath, basename, cache):
    """Check if a file has changed by comparing its hash."""
    current_hash = calculate_file_hash(filepath)
    if basename in cache and cache[basename] == current_hash:
        return False
    cache[basename] = current_hash
    return True


def load_file_hash_cache():
    """Load the file hash cache from a JSON file."""
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r") as f:
            return json.load(f)
    return {}


def save_file_hash_cache(cache):
    """Save the file hash cache to a JSON file."""
    with open(CACHE_FILE, "w") as f:
        json.dump(cache, f, indent=4)


def generate_file_hash_cache(ifdir):
    """Generate the file hash cache for all files in the specified directory."""
    file_hash_cache = {}
    for ifpath in glob.glob(os.path.join(ifdir, "**"), recursive=True):
        if os.path.isfile(ifpath):
            basename = os.path.basename(ifpath)
            basename = os.path.splitext(basename)[0]

            file_hash_cache[basename] = calculate_file_hash(ifpath)
    save_file_hash_cache(file_hash_cache)
    print(f"File hash cache generated and saved to {CACHE_FILE}")


def load_label_hash_cache():
    """Load the label hash cache from a JSON file."""
    if os.path.exists(LABEL_CACHE_FILE):
        with open(LABEL_CACHE_FILE, "r") as f:
            return json.load(f)
    return {}


def save_label_hash_cache(cache):
    """Save the label hash cache to a JSON file."""
    with open(LABEL_CACHE_FILE, "w") as f:
        json.dump(cache, f, indent=4)


def calculate_label_hash(labelDatas, data_file):
    """Calculate hash for a specific data file's labels."""
    relevant_labels = {
        key: asdict(value) if not isinstance(value, dict) else value
        for key, value in labelDatas.items()
        if key.split("%")[0] == data_file
    }
    if not relevant_labels:
        return None
    # Convert to string and hash
    try:
        label_str = json.dumps(relevant_labels, sort_keys=True)
        return hashlib.md5(label_str.encode()).hexdigest()
    except TypeError as e:
        print(f"Warning: Failed to hash labels for {data_file}: {e}")
        return None


def convertToUnity(ifpath, scripts, strList, linkerLabels):
    # FunctionDefinition.load("ev_scripts.json")
    tree = {}
    treeScripts = []

    validator = Validator()

    for label, script in scripts.items():
        scriptCommands = []
        for cmd in script:
            evCmdType = cmd.cmdType
            # funcDef = FunctionDefinition.getFunctionDefinition(evCmdType)
            scriptArgs = [{"argType": EvArgType.CmdType, "data": evCmdType.value}]

            validator.validate_command(cmd, strList, linkerLabels)

            # reqArgs = funcDef.noReqArgs()
            # if len(cmd.args) < reqArgs:
            #     print("[Warning] {}:{} Too few arguments passed in. At least {} required. {} provided.".format(cmd.line, cmd.column, reqArgs, len(cmd.args)))
            # noMaxArgs = funcDef.maxArgs()
            # if len(cmd.args) > noMaxArgs:
            #     print("[Warning] {}:{}  Too many arguments passed in. At most {} allowed. {} provided.".format(cmd.line, cmd.column, noMaxArgs, len(cmd.args)))

            for i, arg in enumerate(cmd.args):
                # argDef = funcDef.validArgs[i]
                # if arg.argType not in argDef.validArgTypes:
                #    print("[Warning] {} {}:{} invalid argument".format(ifpath, arg.line, arg.column))

                scriptArgs.append({"argType": arg.argType, "data": arg.data})

            scriptCommands.append({"Arg": scriptArgs})

        treeScripts.append({"Label": label, "Commands": scriptCommands})
    tree["Scripts"] = treeScripts
    # print(strList)
    tree["StrList"] = strList
    return tree


def repackUnity(ofpath, script, unityTree):
    with open(ofpath, "rb") as ifobj:
        bundle = UnityPy.load(ofpath)

        for obj in bundle.objects:
            if obj.type.name == "MonoBehaviour":
                data = obj.read()
                if obj.serialized_type.nodes:
                    tree = obj.read_typetree()
                    if data.name == script:
                        tree.update(unityTree)
                        obj.save_typetree(tree)

    with open(ofpath, "wb") as ofobj:
        # Thanks Aldo796
        ofobj.write(bundle.file.save(packer=(64, 2)))


def updateLabelDatas(path, lang, labelDatas, debug=False):
    print("Updating message files using Macro information.")
    msbt_files = {}
    file_times = []
    for data_file in DATA_FILES:
        ifpath = os.path.join(path, "{}_{}.json".format(lang, data_file))
        t0 = time.time()
        with open(ifpath, "r", encoding="utf-8") as ifobj:
            try:
                msbt_file = MsbtFile.Schema().loads(ifobj.read())
            except marshmallow.exceptions.ValidationError as exc:
                print(
                    "Failed to load: {}. Unable to update message files".format(ifpath)
                )
                print(exc)
                return
            msbt_files[data_file] = msbt_file
        t1 = time.time()
        file_times.append(t1 - t0)
        if debug:
            print(f"[Timing] updateLabelDatas load {ifpath}: {t1-t0:.3f}s")
    label_times = []
    for scriptMessage, labelData in labelDatas.items():
        t0 = time.time()
        splitMsg = scriptMessage.split("%")
        dataFile = splitMsg[0]
        unlocalized_key = splitMsg[1]
        msbt_file: MsbtFile = msbt_files[dataFile]
        found_entry = False
        for i, iLabelData in enumerate(msbt_file.labelDataArray):
            if iLabelData.labelName == labelData.labelName:
                labelData.labelIndex = iLabelData.labelIndex
                labelData.arrayIndex = iLabelData.arrayIndex
                msbt_file.labelDataArray[i] = labelData
                found_entry = True
                break
        if found_entry:
            t1 = time.time()
            label_times.append(t1 - t0)
            continue
        arrayIndex = msbt_file.labelDataArray[-1].arrayIndex + 1
        labelData.labelIndex = arrayIndex
        labelData.arrayIndex = arrayIndex
        msbt_file.labelDataArray.append(labelData)
        t1 = time.time()
        label_times.append(t1 - t0)
    if label_times and debug:
        avg_label_time = sum(label_times) / len(label_times)
        print(f"[Timing] updateLabelDatas average per labelData: {avg_label_time:.3f}s")
    for data_file in DATA_FILES:
        ifpath = os.path.join(path, "{}_{}.json".format(lang, data_file))
        t0 = time.time()
        with open(ifpath, "w", encoding="utf-8") as ofobj:
            msbt_file = msbt_files[data_file]
            json.dump(
                MsbtFile.Schema().dump(msbt_file), ofobj, indent=4, ensure_ascii=False
            )
        t1 = time.time()
        file_times.append(t1 - t0)
        if debug:
            print(f"[Timing] updateLabelDatas write {ifpath}: {t1-t0:.3f}s")
    if file_times and debug:
        avg_time = sum(file_times) / len(file_times)
        print(f"[Timing] updateLabelDatas average per file: {avg_time:.3f}s")


def updateYamlLabels(path, lang, labelDatas, debug=False):
    print("Updating message files using Macro information.")

    # Load label hash cache
    label_hash_cache = load_label_hash_cache()
    current_cache_key = f"{path}_{lang}"
    if current_cache_key not in label_hash_cache:
        label_hash_cache[current_cache_key] = {}

    # Only process files referenced in labelDatas, preserving DATA_FILES order
    referenced_files = set()
    for scriptMessage in labelDatas.keys():
        splitMsg = scriptMessage.split("%")
        dataFile = splitMsg[0]
        referenced_files.add(dataFile)
    used_data_files = [df for df in DATA_FILES if df in referenced_files]

    # Calculate new hashes and check for changes
    changed_files = []
    for data_file in used_data_files:
        new_hash = calculate_label_hash(labelDatas, data_file)
        old_hash = label_hash_cache[current_cache_key].get(data_file)

        if new_hash != old_hash:
            changed_files.append(data_file)
            label_hash_cache[current_cache_key][data_file] = new_hash

    if not changed_files or len(changed_files) == 0:
        if debug:
            print(
                f"[Timing] updateYamlLabels: No changes detected in any files for {lang}"
            )
        return

    # Save updated cache
    save_label_hash_cache(label_hash_cache)

    msbt_files = {}
    msbt_headers = {}
    unchanged_msbt_bundles = {}
    original_label_arrays = {}
    load_times = []
    # Only load the files that have changes. List needs to be reversed or the last file will be overwritten by the previous one
    for data_file in reversed(changed_files):
        ifpath = os.path.join(path, f"{lang}_{data_file}.asset")
        t0 = time.time()
        with open(ifpath, "r", encoding="utf-8") as ifobj:
            try:
                yaml_header = ifobj.readlines()[:3]
                yaml_header_string = "".join(yaml_header)
                ifobj.seek(0)
                decoded_yaml = decode_unity_yaml(ifobj)
                bundle = yaml.load(decoded_yaml, Loader=CoreLoader)
                tree = bundle["MonoBehaviour"]
            except marshmallow.exceptions.ValidationError as exc:
                print(
                    "Failed to load: {}. Unable to update message files".format(ifpath)
                )
                print(exc)
                return
            msbt_files[data_file] = tree
            msbt_headers[data_file] = yaml_header_string
            unchanged_msbt_bundles[data_file] = bundle
            # Store a copy of the original labelDataArray for change detection. Use asdict to make sure all entries are dicts for comparison
            original_label_arrays[data_file] = [
                asdict(ld) if not isinstance(ld, dict) else ld
                for ld in tree["labelDataArray"]
            ]
        t1 = time.time()
        load_times.append(t1 - t0)
        if debug:
            print(f"[Timing] updateYamlLabels load {tree['m_Name']}: {t1-t0:.3f}s")

    # Update only the changed files
    for scriptMessage, labelData in labelDatas.items():
        splitMsg = scriptMessage.split("%")
        dataFile = splitMsg[0]
        if dataFile not in changed_files:
            continue
        unlocalized_key = splitMsg[1]
        msbt_file: MsbtFile = msbt_files[dataFile]
        found_entry = False
        for i, iLabelData in enumerate(msbt_file["labelDataArray"]):
            ## PyYaml cannot unpack dataclasses or classes at all (at least not easily)
            ## In order to get around this we need to convert everything to a dict
            ## So this checks if it's a macro label (not a dict) and changes it into a dict
            if not isinstance(iLabelData, dict):
                iLabelData = asdict(iLabelData)
            if not isinstance(labelData, dict):
                labelData = asdict(labelData)
            if iLabelData["labelName"] == labelData["labelName"]:
                labelData["labelIndex"] = iLabelData["labelIndex"]
                labelData["arrayIndex"] = iLabelData["arrayIndex"]
                msbt_file["labelDataArray"][i] = labelData
                found_entry = True
                break
        if found_entry:
            continue
        arrayIndex = msbt_file["labelDataArray"][-1]["arrayIndex"] + 1
        labelData["labelIndex"] = arrayIndex
        labelData["arrayIndex"] = arrayIndex
        msbt_file["labelDataArray"].append(labelData)

    write_times = []
    # Only write the changed files
    for data_file in changed_files:
        msbt_file = msbt_files[data_file]
        # Convert all entries to dict for comparison
        current_label_array = [
            asdict(ld) if not isinstance(ld, dict) else ld
            for ld in msbt_file["labelDataArray"]
        ]
        if current_label_array == original_label_arrays[data_file]:
            if debug:
                print(
                    f"[Timing] updateYamlLabels skip {msbt_file['m_Name']}: no changes detected"
                )
            continue
        ifpath = os.path.join(path, f"{lang}_{data_file}.asset")
        t0 = time.time()
        with open(ifpath, "w", encoding="utf-8") as ofobj:
            msbt_header = msbt_headers[data_file]
            bundle = unchanged_msbt_bundles[data_file]
            bundle["MonoBehaviour"]["m_Name"] = msbt_file["m_Name"]
            bundle["MonoBehaviour"]["hash"] = msbt_file["hash"]
            bundle["MonoBehaviour"]["labelDataArray"] = msbt_file["labelDataArray"]
            new_bundle = yaml.dump(
                bundle,
                Dumper=CoreDumper,
                explicit_start=True,
                sort_keys=False,
                allow_unicode=True,
                default_flow_style=False,
            )
            final_bundle = msbt_header + new_bundle[4:]
            ofobj.writelines(final_bundle)
        t1 = time.time()
        write_times.append(t1 - t0)
        if debug:
            print(
                f"[Timing] updateYamlLabels write {msbt_file['m_Name']}: {t1-t0:.3f}s"
            )
    if load_times and debug:
        avg_load_time = sum(load_times) / len(load_times)
        print(f"[Timing] updateYamlLabels average per file load: {avg_load_time:.3f}s")
    if write_times and debug:
        avg_write_time = sum(write_times) / len(write_times)
        print(
            f"[Timing] updateYamlLabels average per file write: {avg_write_time:.3f}s"
        )


def assemble(ifpath, ofpath, script):
    input_stream = FileStream(ifpath)
    lexer = evLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = evParser(stream)
    tree = parser.prog()

    assembler = evAssembler()
    walker = ParseTreeWalker()
    walker.walk(assembler, tree)
    unityTree = convertToUnity(
        assembler.scripts, assembler.strTbl, assembler.scripts.keys()
    )
    repackUnity(ofpath, script, unityTree)


def repackUnityAll(ifpath, ofpath, scripts):
    os.makedirs("bin", exist_ok=True)

    with open(ifpath, "rb") as ifobj:
        bundle = UnityPy.load(ifpath)

        for obj in bundle.objects:
            if obj.type.name == "MonoBehaviour":
                data = obj.read()
                if obj.serialized_type.nodes:
                    tree = obj.read_typetree()
                    if data.name in scripts:
                        unityTree = scripts[data.name]
                        tree.update(unityTree)
                        obj.save_typetree(tree)

    with open(ofpath, "wb") as ofobj:
        # Thanks Aldo796
        ofobj.write(bundle.file.save(packer=(64, 2)))


def load_definitions():
    ifpath = "scripts/global_defines.ev"
    input_stream = FileStream(ifpath, encoding="utf-8")
    lexer = evLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = evParser(stream)
    tree = parser.prog()

    assembler = evAssembler(ifpath)
    walker = ParseTreeWalker()
    walker.walk(assembler, tree)

    return assembler


def loadCoreLabels(ifpath, ignoreNames):
    linkerLabels = []
    with open(ifpath, "rb") as ifobj:
        bundle = UnityPy.load(ifpath)

        for obj in bundle.objects:
            if obj.type.name != "MonoBehaviour":
                continue
            data = obj.read()
            if data.name in ignoreNames:
                # If the file has already been packed together by the previous process
                # then the data from that will be preferred over parsing it from the ev_script
                continue
            if obj.serialized_type.nodes:
                tree = obj.read_typetree()
                if "Scripts" not in tree:
                    continue
                scripts = tree["Scripts"]
                for script in scripts:
                    label = script["Label"]
                    linkerLabels.append(label)

    return linkerLabels


def loadYamlCoreLabels(ifpath, ignoreNames, debug=False):
    linkerLabels = []
    file_times = []
    for filename in os.listdir(ifpath):
        file_path = os.path.join(ifpath, filename)
        if filename.split(".")[0] not in ignoreNames:
            continue
        if not file_path.endswith(".asset"):
            # NO meta here
            continue
        t0 = time.time()
        with open(file_path, "r") as ifobj:
            try:
                decoded_yaml = decode_unity_yaml(ifobj)
                bundle = yaml.load(decoded_yaml, Loader=CoreLoader)
                tree = bundle["MonoBehaviour"]
            except Exception as exc:
                print(exc)
                print("Failed to unpack: {}".format(file_path))
            if "Scripts" not in tree:
                continue
            scripts = tree["Scripts"]
            for script in scripts:
                label = script["Label"]
                linkerLabels.append(label)
        t1 = time.time()
        file_times.append(t1 - t0)
        if debug:
            print(f"[Timing] loadYamlCoreLabels {file_path}: {t1-t0:.3f}s")
    if len(file_times) > 0 and debug:
        avg_time = sum(file_times) / len(file_times)
        print(f"[Timing] loadYamlCoreLabels average per file: {avg_time:.3f}s")
    elif debug:
        print("[Timing] loadYamlCoreLabels: No .asset files processed.")
    return linkerLabels


def assemble_all(ifdir, mode, debug=False, override=False):
    start_time = time.time()
    scripts = {}
    labelDatas = {}
    flags = {}
    works = {}
    sysflags = {}
    file_hash_cache = load_file_hash_cache()
    t0 = time.time()

    if os.path.exists("scripts/global_defines.ev"):
        assembler = load_definitions()
        flags = assembler.flags
        works = assembler.works
        sysflags = assembler.sysflags
    t1 = time.time()
    if debug:
        print(f"[Timing] load_definitions: {t1-t0:.3f}s")

    commands = {}
    if os.path.exists("commands.json"):
        print("Loading external commands reference from commands.json")
        with open("commands.json", "r") as ofobj:
            data = json.load(ofobj)
            for entry in data:
                try:
                    commands[entry["Name"]] = entry["Id"]
                except KeyError:
                    print(
                        "Unable to load commands.json, missing either Id or Name key. Defaulting to known commands"
                    )
    t2 = time.time()
    if debug:
        print(f"[Timing] load commands.json: {t2-t1:.3f}s")

    linkerLabels = []
    toConvertList = []
    ignoreList = []
    file_times = []
    for ifpath in glob.glob("scripts/*.ev"):
        file_start = time.time()
        # Special file with special behaviour
        basename = os.path.basename(ifpath)
        basename = os.path.splitext(basename)[0]
        if basename == "global_defines.ev":
            continue

        # Causes the parser to not have every file to read from
        # and causes minor warnings to pop up in the console.
        # Not the recommended way of running ev_as
        override_hash_change = False
        if override:
            if not file_has_changed(ifpath, basename, file_hash_cache):
                continue
            override_hash_change = True

        input_stream = FileStream(ifpath, encoding="utf-8")
        lexer = evLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = evParser(stream)
        tree = parser.prog()

        assembler = evAssembler(
            ifpath,
            commands=copy(commands),
            flags=copy(flags),
            works=copy(works),
            sysflags=copy(sysflags),
        )
        walker = ParseTreeWalker()
        walker.walk(assembler, tree)
        # Skip processing if the file hasn't changed
        if file_has_changed(ifpath, basename, file_hash_cache):
            toConvertList.append((ifpath, assembler.scripts, assembler.strTbl, basename))
            ignoreList.append(basename)
        if override_hash_change:
            # Only worry about this if override_safety is enabled
            toConvertList.append((ifpath, assembler.scripts, assembler.strTbl, basename))
            ignoreList.append(basename)
        linkerLabels.extend(assembler.scripts.keys())
        labelDatas.update(assembler.macroAssembler.labelDatas)
        file_end = time.time()
        file_times.append(file_end - file_start)
        if debug:
            print(f"[Timing] {ifpath}: {file_end-file_start:.3f}s")
    if len(ignoreList) == 0:
        ## I'm just going to use this to say if a file has any changes
        ## I know it's not what the variable name means, fight me.
        return
    if debug:
        print(ignoreList)
    t3 = time.time()
    if debug:
        print(f"[Timing] parse .ev files: {t3-t2:.3f}s")
        if file_times:
            avg_time = sum(file_times) / len(file_times)
            print(f"[Timing] Average per .ev file: {avg_time:.3f}s")
        else:
            print("[Timing] No .ev files processed.")

    if mode == "bundle":
        linkerLabels.extend(loadCoreLabels("Dpr/ev_script", ignoreList))
        t4 = time.time()
        if debug:
            print(f"[Timing] loadCoreLabels: {t4-t3:.3f}s")
        for toConvert in toConvertList:
            unityTree = convertToUnity(
                toConvert[0], toConvert[1], toConvert[2], linkerLabels
            )
            scripts[toConvert[3]] = unityTree
        t5 = time.time()
        if debug:
            print(f"[Timing] convertToUnity: {t5-t4:.3f}s")
        repackUnityAll("Dpr/ev_script", "bin/ev_script", scripts)
        t6 = time.time()
        if debug:
            print(f"[Timing] repackUnityAll: {t6-t5:.3f}s")
        updateLabelDatas("AssetFolder/english_Export", "english", labelDatas)
        t7 = time.time()
        if debug:
            print(f"[Timing] updateLabelDatas: {t7-t6:.3f}s")
    elif mode == "yaml":
        # Do the yaml thing
        CoreDumper.add_multi_representer(EvArgType, int_enum_representer)
        CoreDumper.add_multi_representer(EvWork, int_enum_representer)
        CoreDumper.add_multi_representer(EvSysFlag, int_enum_representer)
        CoreDumper.add_multi_representer(EvFlag, int_enum_representer)
        CoreDumper.add_multi_representer(EvCmdType, int_enum_representer)
        CoreDumper.add_multi_representer(WordDataPatternID, int_enum_representer)
        CoreDumper.add_multi_representer(MsgEventID, int_enum_representer)
        CoreDumper.add_multi_representer(GroupTagID, int_enum_representer)
        CoreDumper.add_multi_representer(TagPatternID, int_enum_representer)
        CoreDumper.add_multi_representer(ForceGrmID, int_enum_representer)
        CoreDumper.add_multi_representer(TagID, int_enum_representer)
        CoreDumper.add_representer(type(None), none_representer)
        CoreDumper.add_multi_representer(LabelData, dataclass_representer)
        CoreDumper.add_multi_representer(MsbtFile, dataclass_representer)
        CoreDumper.add_multi_representer(WordData, dataclass_representer)

        print("Running in YAML mode")
        linkerLabels.extend(loadYamlCoreLabels(ifdir, ignoreList, debug=debug))
        t4 = time.time()
        if debug:
            print(f"[Timing] loadYamlCoreLabels: {t4-t3:.3f}s")
        for toConvert in toConvertList:
            unityTree = convertToUnity(
                toConvert[0], toConvert[1], toConvert[2], linkerLabels
            )
            scripts[toConvert[3]] = unityTree
        t5 = time.time()
        if debug:
            print(f"[Timing] convertToUnity: {t5-t4:.3f}s")
        for filename in os.listdir(ifdir):
            file_path = os.path.join(ifdir, filename)
            if filename.split(".")[0] not in ignoreList:
                continue
            if not file_path.endswith(".asset"):
                # NO meta here
                continue
            basename = os.path.basename(file_path)
            basename = os.path.splitext(basename)[0]
            if basename == "global_defines.ev":
                continue
            if not file_has_changed(file_path, basename, file_hash_cache):
                continue
            file_write_start = time.time()
            with open(file_path, "r") as ifobj:
                yaml_header = ifobj.readlines()[:3]
                yaml_header_string = "".join(yaml_header)
                ifobj.seek(0)
                decoded_yaml = decode_unity_yaml(ifobj)
                bundle = yaml.load(decoded_yaml, Loader=CoreLoader)
            with open(file_path, "w") as outputobj:
                script_name = bundle["MonoBehaviour"]["m_Name"]
                new_scripts = scripts[script_name]
                ## You have to write these individually or else the file headers will get overwritten which causes problems
                bundle["MonoBehaviour"]["Scripts"] = new_scripts["Scripts"]
                bundle["MonoBehaviour"]["StrList"] = new_scripts["StrList"]
                new_bundle = yaml.dump(
                    bundle,
                    Dumper=CoreDumper,
                    explicit_start=True,
                    sort_keys=False,
                    allow_unicode=True,
                    default_flow_style=False,
                )
                final_bundle = yaml_header_string + new_bundle[4:]
                outputobj.writelines(final_bundle)
            file_write_end = time.time()
            if debug:
                print(
                    f"[Timing] yaml file writing {file_path}: {file_write_end-file_write_start:.3f}s"
                )
        t6 = time.time()
        if debug:
            print(f"[Timing] yaml file writing total: {t6-t5:.3f}s")
        updateYamlLabels(
            "Assets/format_msbt/en/english", "english", labelDatas, debug=debug
        )
        t7 = time.time()
        if debug:
            print(f"[Timing] updateYamlLabels: {t7-t6:.3f}s")
    else:
        raise ValueError(f"'{mode}' is an Invalid mode. Must be 'yaml' or 'bundle'.")

    generate_file_hash_cache(".\\scripts")
    end_time = time.time()
    if debug:
        print(f"[Timing] Total assemble_all: {end_time-start_time:.3f}s")


def main():
    parser = ArgumentParser()
    parser.add_argument(
        "-i", "--input", dest="ifpath", action="store", default="Dpr/ev_script"
    )
    parser.add_argument(
        "-m",
        "--mode",
        dest="mode",
        action="store",
        default="bundle",
        help="Mode of operation: 'bundle', 'yaml', or 'generate-cache'",
    )
    parser.add_argument(
        "--debug", dest="debug", action="store_true", help="Enable timing debug output"
    )
    parser.add_argument(# This literally just shows some warnings that don't amount to anything
        "--override_safety",
        dest="override_safety",
        action="store_true",
        help="WARNING: Will increase the speed of operation at the expense of all safety measures. Use with Extreme Caution"
    )
    # parser.add_argument("-s", "--script", dest='script', action='store', required=True)

    vargs = parser.parse_args()

    if vargs.mode == "generate-cache":
        generate_file_hash_cache(vargs.ifpath)
    else:
        assemble_all(vargs.ifpath, vargs.mode, debug=vargs.debug, override=vargs.override_safety)
        print("Assembly finished")


if __name__ == "__main__":
    main()
