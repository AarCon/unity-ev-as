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
    TagID
)
from validator import Validator
from ev_parse import decode_unity_yaml
from dataclasses import asdict

def jsonDumpUnity(tree, ofpath):
    with open(ofpath, "w") as ofobj:
        json.dump(tree, ofobj, indent=4)

def int_enum_representer(dumper, data):
    # Convert the enum to its integer value and represent as scalar
    return dumper.represent_scalar('tag:yaml.org,2002:int', str(int(data)))

def none_representer(dumper, data):
    return dumper.represent_scalar('tag:yaml.org,2002:null', '')

def dataclass_representer(dumper, data):
    return dumper.represent_dict(data.to_yaml_dict())

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
            scriptArgs = [
                {
                    "argType" : EvArgType.CmdType,
                    "data" : evCmdType.value
                }
            ]

            validator.validate_command(cmd, strList, linkerLabels)

            # reqArgs = funcDef.noReqArgs()
            # if len(cmd.args) < reqArgs:
            #     print("[Warning] {}:{} Too few arguments passed in. At least {} required. {} provided.".format(cmd.line, cmd.column, reqArgs, len(cmd.args)))
            # noMaxArgs = funcDef.maxArgs()
            # if len(cmd.args) > noMaxArgs:
            #     print("[Warning] {}:{}  Too many arguments passed in. At most {} allowed. {} provided.".format(cmd.line, cmd.column, noMaxArgs, len(cmd.args)))
            
            for i, arg in enumerate(cmd.args):
                # argDef = funcDef.validArgs[i]
                #if arg.argType not in argDef.validArgTypes:
                #    print("[Warning] {} {}:{} invalid argument".format(ifpath, arg.line, arg.column))
                

                scriptArgs.append({
                    "argType" : arg.argType,
                    "data" : arg.data
                })
            
            scriptCommands.append({
                "Arg" : scriptArgs
            })

        treeScripts.append({
            "Label" : label,
            "Commands" : scriptCommands
        })
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
        ofobj.write(bundle.file.save(packer=(64,2)))

def updateLabelDatas(path, lang, labelDatas):
    print("Updating message files using Macro information.")
    msbt_files = {}
    for data_file in DATA_FILES:
        ifpath = os.path.join(path, "{}_{}.json".format(lang, data_file))
        with open(ifpath, "r", encoding='utf-8') as ifobj:
            try:
                msbt_file = MsbtFile.Schema().loads(ifobj.read())
            except marshmallow.exceptions.ValidationError as exc:
                print("Failed to load: {}. Unable to update message files".format(ifpath))
                print(exc)
                return
            msbt_files[data_file] = msbt_file
    for scriptMessage, labelData in labelDatas.items():
        splitMsg = scriptMessage.split('%')
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
            continue
        arrayIndex = msbt_file.labelDataArray[-1].arrayIndex + 1
        labelData.labelIndex = arrayIndex
        labelData.arrayIndex = arrayIndex
        msbt_file.labelDataArray.append(labelData)
    
    for data_file in DATA_FILES:
        ifpath = os.path.join(path, "{}_{}.json".format(lang, data_file))
        with open(ifpath, "w", encoding='utf-8') as ofobj:
            msbt_file = msbt_files[data_file]
            json.dump(MsbtFile.Schema().dump(msbt_file), ofobj, indent=4, ensure_ascii=False)

def updateYamlLabels(path, lang, labelDatas):
    print("Updating message files using Macro information.")
    msbt_files = {}
    for data_file in DATA_FILES:
        ifpath = os.path.join(path, f"{lang}_{data_file}.asset")
        with open(ifpath, "r", encoding='utf-8') as ifobj:
            try:
                decoded_yaml = decode_unity_yaml(ifobj)
                bundle = yaml.load(decoded_yaml, Loader=CoreLoader)
                tree = bundle["MonoBehaviour"]
            except marshmallow.exceptions.ValidationError as exc:
                print("Failed to load: {}. Unable to update message files".format(ifpath))
                print(exc)
                return
            msbt_files[data_file] = tree
    for scriptMessage, labelData in labelDatas.items():
        splitMsg = scriptMessage.split('%')
        dataFile = splitMsg[0]
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

    for data_file in DATA_FILES:
        ifpath = os.path.join(path, f"{lang}_{data_file}.asset")
        with open(ifpath, "r", encoding='utf-8') as ifobj:
            try:
                yaml_header = ifobj.readlines()[:3]
                yaml_header_string = "".join(yaml_header)
                ifobj.seek(0)
                decoded_yaml = decode_unity_yaml(ifobj)
                bundle = yaml.load(decoded_yaml, Loader=CoreLoader)
            except TypeError as e:
                print("Something wrong", ifpath, bundle.keys())
                sys.exit()
        with open(ifpath, "w", encoding='utf-8') as ofobj:
            msbt_file = msbt_files[data_file]['labelDataArray']

            bundle['MonoBehaviour']['labelDataArray'] = msbt_file
            new_bundle = yaml.dump(
                bundle,
                Dumper=CoreDumper,
                explicit_start=True,
                sort_keys=False,
                allow_unicode=True,
                default_flow_style=False
            )
            final_bundle = yaml_header_string + new_bundle[4:]
            ofobj.writelines(final_bundle)

def assemble(ifpath, ofpath, script):
    input_stream = FileStream(ifpath)
    lexer = evLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = evParser(stream)
    tree = parser.prog()

    assembler = evAssembler()
    walker = ParseTreeWalker()
    walker.walk(assembler, tree)
    unityTree = convertToUnity(assembler.scripts, assembler.strTbl, assembler.scripts.keys())
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
        ofobj.write(bundle.file.save(packer=(64,2)))

def load_definitions():
    ifpath = "scripts/global_defines.ev"
    input_stream = FileStream(ifpath, encoding='utf-8')
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

def loadYamlCoreLabels(ifpath, ignoreNames):
    linkerLabels = []
    for filename in os.listdir(ifpath):
        file_path = os.path.join(ifpath, filename)
        if not file_path.endswith(".asset"):
            # NO meta here
            continue
        with open(file_path, "r") as ifobj:
            try:
                decoded_yaml = decode_unity_yaml(ifobj)
                bundle = yaml.load(decoded_yaml, Loader=CoreLoader)
                tree = bundle["MonoBehaviour"]
            except Exception as exc:
                print(exc)
                print("Failed to unpack: {}".format(file_path))

            if tree["m_Name"] in ignoreNames:
                continue
            if "Scripts" not in tree:
                continue
            scripts = tree["Scripts"]
            for script in scripts:
                label = script["Label"]
                linkerLabels.append(label)

    return linkerLabels

def assemble_all(ifdir, mode):
    scripts = {}
    labelDatas = {}
    flags = {}
    works = {}
    sysflags = {}
    if os.path.exists("scripts/global_defines.ev"):
        assembler = load_definitions()
        flags = assembler.flags
        works = assembler.works
        sysflags = assembler.sysflags
    
    commands = {}
    if os.path.exists("commands.json"):
        print("Loading external commands reference from commands.json")
        with open("commands.json", "r") as ofobj:
            data = json.load(ofobj)
            for entry in data:
                try:
                    commands[entry["Name"]] = entry["Id"]
                except KeyError:
                    print("Unable to load commands.json, missing either Id or Name key. Defaulting to known commands")

    linkerLabels = []
    toConvertList = []
    ignoreList = []
    for ifpath in glob.glob("scripts/*.ev"):
        # Special file with special behaviour
        basename = os.path.basename(ifpath)
        basename = os.path.splitext(basename)[0]
        if basename == "global_defines.ev":
            continue
        input_stream = FileStream(ifpath, encoding='utf-8')
        lexer = evLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = evParser(stream)
        tree = parser.prog()

        assembler = evAssembler(ifpath, commands=copy(commands), flags=copy(flags), works=copy(works), sysflags=copy(sysflags))
        walker = ParseTreeWalker()
        walker.walk(assembler, tree)
        toConvertList.append((ifpath, assembler.scripts, assembler.strTbl, basename))
        linkerLabels.extend(assembler.scripts.keys())
        labelDatas.update(assembler.macroAssembler.labelDatas)
        ignoreList.append(basename)
    if mode == "bundle":
        linkerLabels.extend(loadCoreLabels("Dpr/ev_script", ignoreList))
        for toConvert in toConvertList:
            unityTree = convertToUnity(toConvert[0], toConvert[1], toConvert[2], linkerLabels)
            scripts[toConvert[3]] = unityTree
        repackUnityAll("Dpr/ev_script", "bin/ev_script", scripts)
        updateLabelDatas("AssetFolder/english_Export", "english", labelDatas)
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
        CoreDumper.add_multi_representer(LabelData, dataclass_representer)

        print("Running in YAML mode")
        linkerLabels.extend(loadYamlCoreLabels(ifdir, ignoreList))
        for toConvert in toConvertList:
            unityTree = convertToUnity(toConvert[0], toConvert[1], toConvert[2], linkerLabels)
            scripts[toConvert[3]] = unityTree
        for filename in os.listdir(ifdir):
            file_path = os.path.join(ifdir, filename)
            if not file_path.endswith(".asset"):
                # NO meta here
                continue
            with open(file_path, 'r') as ifobj:
                yaml_header = ifobj.readlines()[:3]
                yaml_header_string = "".join(yaml_header)
                ifobj.seek(0)
                decoded_yaml = decode_unity_yaml(ifobj)
                bundle = yaml.load(decoded_yaml, Loader=CoreLoader)

            with open(file_path, 'w') as outputobj:
                script_name = bundle['MonoBehaviour']['m_Name']
                new_scripts = scripts[script_name]
                ## You have to write these individually or else the file headers will get overwritten which causes problems
                bundle['MonoBehaviour']['Scripts'] = new_scripts["Scripts"]
                bundle['MonoBehaviour']['StrList'] = new_scripts['StrList']
                new_bundle = yaml.dump(
                    bundle,
                    Dumper=CoreDumper,
                    explicit_start=True,
                    sort_keys=False,
                    allow_unicode=True,
                    default_flow_style=False
                )
                final_bundle = yaml_header_string + new_bundle[4:]
                outputobj.writelines(final_bundle)
        updateYamlLabels("Assets/format_msbt/en/english", "english", labelDatas)
    else:
        raise ValueError(f"'{mode}' is an Invalid mode. Must be 'yaml' or 'bundle'.")

def main():
    parser = ArgumentParser()
    parser.add_argument("-i", "--input", dest='ifpath', action='store', default="Dpr/ev_script")
    parser.add_argument("-m", "--mode", dest='mode', action='store', default="bundle") # yaml is the other option
    # parser.add_argument("-s", "--script", dest='script', action='store', required=True)

    vargs = parser.parse_args()
    # assemble(vargs.ifpath, vargs.ofpath, vargs.script)
    assemble_all(vargs.ifpath, vargs.mode)
    print("Assembly finished")

if __name__ == "__main__":
    main()
