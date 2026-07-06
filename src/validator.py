import re
import sys
from collections import deque

from evAssembler import EvCmd, evAssembler
from ev_argtype import EvArgType
from ev_cmd import EvCmdType
from gdatamanger import GDataManager

def validate_talk_msg(cmd: EvCmd, strList: list, scripts: list, flow_context=None):
    scenarioMsgList = GDataManager.getScenarioMsgList()
    if scenarioMsgList is None:
        return
    msgIdx = cmd.args[0].data
    msg = strList[msgIdx]
    splitMsg = msg.split('%')
    try:
        dataFile = splitMsg[0]
        unlocalized_key = splitMsg[1]
    except IndexError:
        return
        # raise RuntimeError('Invalid msg: {} passed to {} at {}: {}'.format(msg, cmd.cmdType.name, cmd.line, cmd.column))

    if dataFile not in scenarioMsgList:
        raise RuntimeError('Unknown datafile: {} passed to {} at {}:{}'.format(dataFile, cmd.cmdType.name, cmd.line, cmd.column))
    if unlocalized_key not in scenarioMsgList[dataFile]:
        raise RuntimeError('Unknown message: {} passed to {} at {}:{}'.format(msg, cmd.cmdType.name, cmd.line, cmd.column))

def validate_talk_keywait(cmd: EvCmd, strList: list, scripts: list, flow_context=None):
    scenarioMsgList = GDataManager.getScenarioMsgList()
    if scenarioMsgList is None:
        return
    msgIdx = cmd.args[0].data
    msg = strList[msgIdx]
    splitMsg = msg.split('%')
    try:
        dataFile = splitMsg[0]
        unlocalized_key = splitMsg[1]
    except IndexError:
        return
        # raise RuntimeError('Invalid msg: {} passed to {} at {}: {}'.format(msg, cmd.cmdType.name, cmd.line, cmd.column))

    if dataFile not in scenarioMsgList:
        raise RuntimeError('Unknown datafile: {} passed to {} at {}:{}'.format(dataFile, cmd.cmdType.name, cmd.line, cmd.column))
    if unlocalized_key not in scenarioMsgList[dataFile]:
        raise RuntimeError('Unknown message: {} passed to {} at {}:{}'.format(msg, cmd.cmdType.name, cmd.line, cmd.column))

def validate_easy_obj_msg(cmd: EvCmd, strList: list, scripts: list, flow_context=None):
    scenarioMsgList = GDataManager.getScenarioMsgList()
    if scenarioMsgList is None:
        return
    msgIdx = cmd.args[0].data
    msg = strList[msgIdx]
    splitMsg = msg.split('%')
    try:
        dataFile = splitMsg[0]
        unlocalized_key = splitMsg[1]
    except IndexError:
        return
        # raise RuntimeError('Invalid msg: {} passed to {} at {}: {}'.format(msg, cmd.cmdType.name, cmd.line, cmd.column))

    if dataFile not in scenarioMsgList:
        raise RuntimeError('Unknown datafile: {} passed to {} at {}:{}'.format(dataFile, cmd.cmdType.name, cmd.line, cmd.column))
    if unlocalized_key not in scenarioMsgList[dataFile]:
        raise RuntimeError('Unknown message: {} passed to {} at {}:{}'.format(msg, cmd.cmdType.name, cmd.line, cmd.column))

def validate_add_custum_win_label(cmd: EvCmd, strList: list, scripts: list, flow_context=None):
    scenarioMsgList = GDataManager.getScenarioMsgList()
    if scenarioMsgList is None:
        return
    msgIdx = cmd.args[0].data
    msg = strList[msgIdx]
    splitMsg = msg.split('%')
    try:
        dataFile = splitMsg[0]
        unlocalized_key = splitMsg[1]
    except IndexError:
        return
        # raise RuntimeError('Invalid msg: {} passed to {} at {}: {}'.format(msg, cmd.cmdType.name, cmd.line, cmd.column))

    if dataFile not in scenarioMsgList:
        raise RuntimeError('Unknown datafile: {} passed to {} at {}:{}'.format(dataFile, cmd.cmdType.name, cmd.line, cmd.column))
    if unlocalized_key not in scenarioMsgList[dataFile]:
        raise RuntimeError('Unknown message: {} passed to {} at {}:{}'.format(msg, cmd.cmdType.name, cmd.line, cmd.column))

def is_valid_comparator(string):
    return string in ('GE', 'GT', 'LE', 'LT', 'EQ', 'NE')


def get_edge_kind(cmd: EvCmd):
    if cmd.cmdType in (
        EvCmdType._CALL,
        EvCmdType._IF_FLAGOFF_CALL,
        EvCmdType._IF_FLAGON_CALL,
        EvCmdType._IFVAL_CALL,
    ):
        return "CALL"
    if cmd.cmdType in (
        EvCmdType._JUMP,
        EvCmdType._IF_FLAGOFF_JUMP,
        EvCmdType._IF_FLAGON_JUMP,
        EvCmdType._IFVAL_JUMP,
    ):
        return "JUMP"
    return None


def validate_label(cmd, argIdx, strList, scripts, flow_context=None):
    if cmd.args[argIdx].argType != EvArgType.String:
        raise RuntimeError('Unknown label: {} passed to {} at {} at Line {}, Col {}'.format(cmd.args[argIdx].data, cmd.cmdType.name, cmd.filename, cmd.line, cmd.column))
    msgIdx = cmd.args[argIdx].data
    msg = strList[msgIdx]
    if msg not in scripts:
        raise RuntimeError('Unknown label: {} passed to {} at {} at Line {}, Col {}'.format(msg, cmd.cmdType.name, cmd.filename, cmd.line, cmd.column))

    if flow_context is not None:
        flow_context.setdefault("edges", []).append((cmd.filename, cmd.line, msg))
        flow_context.setdefault("targets", set()).add(msg)

        edge_kind = get_edge_kind(cmd)
        if edge_kind is not None:
            edge_types = flow_context.setdefault("edge_types", {})
            edge_type_list = edge_types.setdefault(msg, [])
            if edge_kind not in edge_type_list:
                edge_type_list.append(edge_kind)

def validate_jump(cmd: EvCmd, strList: list, scripts: list, flow_context=None):
    # Destination label should always be arg0
    validate_label(cmd, 0, strList, scripts, flow_context=flow_context)

def validate_obj_anime(cmd: EvCmd, strList: list, scripts: list, flow_context=None):
    # TODO: Validate object from placedatas

    # Destination label should always be arg1
    validate_label(cmd, 1, strList, scripts, flow_context=flow_context)

def validate_ifflag(cmd: EvCmd, strList: list, scripts: list, flow_context=None):
    # Destination label should always be arg1
    validate_label(cmd, 1, strList, scripts, flow_context=flow_context)

def validate_ifval(cmd: EvCmd, strList: list, scripts: list, flow_context=None):
    # Comparator should always be arg1
    msgIdx = cmd.args[1].data
    msg = strList[msgIdx]

    if not is_valid_comparator(msg):
        raise RuntimeError('Bad comparator: {} passed to {} in {} at Line {}, Col {}'.format(msg, cmd.cmdType.name, cmd.filename, cmd.line, cmd.column))

    # Destination label should always be arg3
    validate_label(cmd, 3, strList, scripts, flow_context=flow_context)

VALIDATE_MESSAGES = {
    EvCmdType._TALKMSG : validate_talk_msg,
    EvCmdType._TALK_KEYWAIT : validate_talk_keywait,
    EvCmdType._EASY_OBJ_MSG : validate_easy_obj_msg,
    EvCmdType._ADD_CUSTUM_WIN_LABEL : validate_add_custum_win_label
}

VALIDATE_TABLE = {
    EvCmdType._IF_FLAGOFF_CALL : validate_ifflag,
    EvCmdType._IF_FLAGOFF_JUMP : validate_ifflag,
    EvCmdType._IF_FLAGON_CALL : validate_ifflag,
    EvCmdType._IF_FLAGON_JUMP : validate_ifflag,
    EvCmdType._IFVAL_CALL : validate_ifval,
    EvCmdType._IFVAL_JUMP : validate_ifval,
    EvCmdType._JUMP : validate_jump,
    EvCmdType._CALL : validate_jump,
    EvCmdType._OBJ_ANIME : validate_obj_anime
}

class Validator:
    def __init__(self, validateMessages=False):
        self.validate_table = VALIDATE_TABLE
        if validateMessages:
            self.validate_table.update(VALIDATE_MESSAGES)

    def validate_command(self, cmd, strList, scripts, flow_context=None):
        evCmdType = cmd.cmdType
        if evCmdType in self.validate_table:
            valid_func = self.validate_table[evCmdType]
            try:
                valid_func(cmd, strList, scripts, flow_context=flow_context)
            except RuntimeError as exc:
                print(exc)
            except IndexError as exc:
                print(exc, cmd)
                sys.exit()

    def build_script_flow_map(self, script_map, str_list, known_scripts=None, start_labels=None):
        if known_scripts is None:
            known_scripts = list(script_map.keys())
        else:
            known_scripts = list(known_scripts)

        if start_labels is None:
            start_labels = list(script_map.keys())
        else:
            start_labels = list(start_labels)

        graph = {label: [] for label in known_scripts}
        paths = {}
        edge_types = {}
        reachable_labels = set()

        for start_label in start_labels:
            print("Building flow map for script: {}".format(start_label))
            queue = deque([(start_label, [start_label])])
            seen_paths = set()
            visited_labels = set()
            paths[start_label] = []

            while queue:
                current_label, path = queue.popleft()
                if current_label in visited_labels:
                    continue
                visited_labels.add(current_label)

                if current_label not in script_map:
                    continue

                local_labels = list(script_map.keys())
                script_scope = local_labels + [
                    label for label in known_scripts if label not in local_labels
                ]

                flow_context = {"edges": [], "targets": set(), "edge_types": {}}
                for cmd in script_map[current_label]:
                    evCmdType = cmd.cmdType
                    if evCmdType in self.validate_table and evCmdType is not EvCmdType._OBJ_ANIME:
                        valid_func = self.validate_table[evCmdType]
                        try:
                            self.validate_command(
                                cmd,
                                str_list,
                                script_scope,
                                flow_context=flow_context,
                            )
                        except RuntimeError:
                            continue
                        except IndexError:
                            continue

                next_labels = sorted(flow_context["targets"])
                reachable_labels.add(current_label)
                reachable_labels.update(next_labels)
                graph[current_label] = next_labels
                if flow_context.get("edge_types"):
                    edge_types[current_label] = {
                        target: list(kinds) for target, kinds in flow_context["edge_types"].items()
                    }

                if not next_labels:
                    path_key = tuple(path)
                    if path_key not in seen_paths:
                        seen_paths.add(path_key)
                        paths[start_label].append(path)
                    continue

                for next_label in next_labels:
                    new_path = path + [next_label]
                    if next_label not in visited_labels:
                        queue.append((next_label, new_path))

        pruned_graph = {
            label: sorted(graph.get(label, []))
            for label in sorted(reachable_labels)
            if label in graph
        }
        return {"graph": pruned_graph, "paths": paths, "edge_types": edge_types}

    def build_mermaid_markdown(self, flow_map, title="EV Script Flow"):
        graph = flow_map.get("graph", {})
        paths = flow_map.get("paths", {})
        edge_types = flow_map.get("edge_types", {})
        lines = [f"# {title}", ""]

        labels = sorted(graph.keys())
        indegree = {label: 0 for label in labels}
        for source, targets in graph.items():
            for target in targets:
                if target in indegree:
                    indegree[target] += 1

        roots = [label for label in labels if indegree[label] == 0]
        if not roots:
            roots = labels

        visited = set()
        for root in roots:
            if root in visited:
                continue

            stack = [root]
            component_nodes = set()
            while stack:
                current = stack.pop()
                if current in component_nodes:
                    continue
                component_nodes.add(current)
                for target in graph.get(current, []):
                    if target in graph and target not in component_nodes:
                        stack.append(target)

            if not component_nodes:
                continue

            visited.update(component_nodes)
            lines.extend([f"## {root}", "", "```mermaid", "flowchart TD"])

            for node in sorted(component_nodes):
                safe_node = self._escape_mermaid_id(node)
                lines.append(f'    {safe_node}["{node}"]')

            for source in sorted(component_nodes):
                for target in sorted(graph.get(source, [])):
                    if target in component_nodes:
                        source_id = self._escape_mermaid_id(source)
                        target_id = self._escape_mermaid_id(target)
                        kinds = edge_types.get(source, {}).get(target, [])
                        if kinds:
                            lines.append(f"    {source_id} -->|{'/'.join(kinds)}| {target_id}")
                        else:
                            lines.append(f"    {source_id} --> {target_id}")

            lines.extend(["```", ""])

        if paths:
            lines.extend(["## Possible paths"])
            for start_label, path_list in sorted(paths.items()):
                lines.append(f"- {start_label}:")
                for path in path_list:
                    lines.append(f"  - {' -> '.join(path)}")

        return "\n".join(lines).rstrip() + "\n"

    def _escape_mermaid_id(self, label):
        safe = re.sub(r"[^A-Za-z0-9_]", "_", label)
        return safe or "node"
