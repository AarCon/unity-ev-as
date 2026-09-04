import os
import sys
import unittest

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))

from evAssembler import EvArg, EvCmd
from ev_argtype import EvArgType
from ev_cmd import EvCmdType
from validator import Validator


class ValidatorFlowTests(unittest.TestCase):
    def make_cmd(self, cmd_type, target_label="branch"):
        label_index = {"branch": 0, "tail": 1}.get(target_label, 0)
        return EvCmd(
            cmd_type,
            [EvArg(EvArgType.String, label_index, 0, 0)],
            0,
            0,
            "test.ev",
        )

    def test_build_script_flow_map_lists_possible_paths(self):
        validator = Validator()
        script_map = {
            "entry": [self.make_cmd(EvCmdType._JUMP, "branch")],
            "branch": [self.make_cmd(EvCmdType._CALL, "tail")],
            "tail": [],
        }
        str_list = ["branch", "tail"]

        flow_map = validator.build_script_flow_map(
            script_map,
            str_list,
            known_scripts=["entry", "branch", "tail"],
        )

        self.assertEqual(flow_map["graph"]["entry"], ["branch"])
        self.assertEqual(flow_map["paths"]["entry"], [["entry", "branch", "tail"]])

    def test_build_script_flow_map_uses_local_labels_before_external_labels(self):
        validator = Validator()
        script_map = {
            "entry": [self.make_cmd(EvCmdType._JUMP, "branch")],
            "branch": [],
        }
        str_list = ["branch"]

        flow_map = validator.build_script_flow_map(
            script_map,
            str_list,
            known_scripts=["external"],
        )

        self.assertEqual(flow_map["graph"]["entry"], ["branch"])
        self.assertEqual(flow_map["paths"]["entry"], [["entry", "branch"]])

    def test_build_mermaid_markdown_renders_flow_chart(self):
        validator = Validator()
        flow_map = {
            "graph": {"entry": ["branch"], "branch": ["tail"], "tail": []},
            "paths": {"entry": [["entry", "branch", "tail"]]},
        }

        markdown = validator.build_mermaid_markdown(flow_map, title="Test Flow")

        self.assertIn("```mermaid", markdown)
        self.assertIn("flowchart TD", markdown)
        self.assertIn('entry["entry"]', markdown)
        self.assertIn("entry --> branch", markdown)

    def test_build_script_flow_map_records_edge_kinds_for_calls_and_jumps(self):
        validator = Validator()
        script_map = {
            "entry": [self.make_cmd(EvCmdType._JUMP, "branch")],
            "branch": [self.make_cmd(EvCmdType._CALL, "tail")],
            "tail": [],
        }
        str_list = ["branch", "tail"]

        flow_map = validator.build_script_flow_map(
            script_map,
            str_list,
            known_scripts=["entry", "branch", "tail"],
        )

        self.assertEqual(flow_map["edge_types"]["entry"]["branch"], ["JUMP"])
        self.assertEqual(flow_map["edge_types"]["branch"]["tail"], ["CALL"])

    def test_build_mermaid_markdown_labels_calls_and_jumps(self):
        validator = Validator()
        flow_map = {
            "graph": {"entry": ["branch"], "branch": ["tail"], "tail": []},
            "paths": {"entry": [["entry", "branch", "tail"]]},
            "edge_types": {
                "entry": {"branch": ["JUMP"]},
                "branch": {"tail": ["CALL"]},
            },
        }

        markdown = validator.build_mermaid_markdown(flow_map, title="Test Flow")

        self.assertIn("entry -->|JUMP| branch", markdown)
        self.assertIn("branch -->|CALL| tail", markdown)

    def test_build_mermaid_markdown_closes_mermaid_block_before_possible_paths(self):
        validator = Validator()
        flow_map = {
            "graph": {"entry": ["branch"]},
            "paths": {"entry": [["entry", "branch"]]},
        }

        markdown = validator.build_mermaid_markdown(flow_map, title="Test Flow")

        self.assertIn("```\n\n## Possible paths", markdown)

    def test_build_mermaid_markdown_groups_each_root_graph_together(self):
        validator = Validator()
        flow_map = {
            "graph": {"entry": ["branch"], "branch": ["tail"], "tail": []},
            "paths": {"entry": [["entry", "branch", "tail"]]},
        }

        markdown = validator.build_mermaid_markdown(flow_map, title="Test Flow")

        self.assertIn("## entry", markdown)
        self.assertNotIn("## branch", markdown)
        self.assertNotIn("## tail", markdown)
        self.assertEqual(markdown.count("```mermaid"), 1)
        self.assertIn("entry --> branch", markdown)
        self.assertIn("branch --> tail", markdown)

    def test_build_script_flow_map_prunes_graph_to_reachable_labels(self):
        validator = Validator()
        script_map = {
            "entry": [self.make_cmd(EvCmdType._JUMP, "branch")],
            "branch": [self.make_cmd(EvCmdType._CALL, "tail")],
            "tail": [],
        }
        str_list = ["branch", "tail"]

        flow_map = validator.build_script_flow_map(
            script_map,
            str_list,
            known_scripts=["entry", "branch", "tail", "unused"],
            start_labels=["entry"],
        )

        self.assertEqual(set(flow_map["graph"].keys()), {"entry", "branch", "tail"})
        self.assertNotIn("unused", flow_map["graph"])


if __name__ == "__main__":
    unittest.main()
