#!/usr/bin/env python3

import copy
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest


HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location(
    "remediation_comparator_v4_2_tests", HERE / "campaign_v4_2.py")
campaign = importlib.util.module_from_spec(spec)
spec.loader.exec_module(campaign)


class RemediationComparatorV42Tests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.old_packet = {"inputs": {
            "recognized_revenue": {"value": 1}, "employee_cash_cost": {"value": 1},
            "controllable_contractor_cash_cost": {"value": 1},
            "target_archetype_coverage": {"value": 1},
            "five_year_sale_availability": {"value": 1},
            "buyer_access_win_share": {"value": 1}, "buy_multiple": {"value": 1},
            "deal_execution_capacity_5y": {"value": 1},
            "integration_onboarding_capacity_5y": {"value": 1},
            "normalized_y5_operating_state": {"state": 1},
            "downside_exit_multiple": {"value": 1},
            "operator_controlled_value_added_demand_share_y5": {"value": 1},
            "implementation_realization": {"r%d" % i: {"value": 1} for i in range(1, 6)},
            "implementation_investment": {"k%d" % i: {"value": 1} for i in range(0, 6)},
            "commercial_retention": {"c%d" % i: {"value": 1} for i in range(1, 6)},
        }, "sources": [], "reviewer_note": "unchanged"}

    def tearDown(self):
        self.temp.cleanup()

    def entry(self, prefix, packet):
        artifacts = {}
        for key, value in (("packet", packet), ("dataset", {"frozen": True}),
                           ("industry_spec", {"frozen": True}), ("record", {})):
            relative = "%s-%s.json" % (prefix, key)
            (self.root / relative).write_text(json.dumps(value), encoding="utf-8")
            artifacts[key] = {"path": relative}
        return {"artifacts": artifacts, "input_registry": [], "source_registry": []}

    def assert_linked_change(self, path, packet_key, child=None):
        new = copy.deepcopy(self.old_packet)
        target = new["inputs"][packet_key]
        if child is None:
            target["changed"] = True
        else:
            target[child] = {"value": 2}
        first, second = self.entry("old", self.old_packet), self.entry("new", new)
        errors = campaign._v4_2_remediation_semantic_errors(
            first, second, [{"input_paths": [path], "source_ids": []}], str(self.root))
        self.assertEqual(errors, [], path)

    def test_every_v4_2_primitive_mapping_is_exactly_reachable(self):
        for path, location in campaign.V4_2_REMEDIATION_PACKET_PATHS.items():
            self.assert_linked_change(path, location[1])
        for schedule, prefix, indexes in (
                ("implementation_realization", "r", range(1, 6)),
                ("implementation_investment", "k", range(0, 6)),
                ("commercial_retention", "c", range(1, 6))):
            for index in indexes:
                self.assert_linked_change(
                    "inputs.%s.%s%d" % (schedule, prefix, index),
                    schedule, "%s%d" % (prefix, index))

    def test_sibling_and_unlinked_changes_fail(self):
        new = copy.deepcopy(self.old_packet)
        new["inputs"]["implementation_realization"]["r2"] = {"value": 2}
        first, second = self.entry("old", self.old_packet), self.entry("new", new)
        errors = campaign._v4_2_remediation_semantic_errors(
            first, second,
            [{"input_paths": ["inputs.implementation_realization.r1"], "source_ids": []}],
            str(self.root))
        self.assertTrue(any("outside predecessor-linked" in item for item in errors), errors)

    def test_replacement_source_is_allowed_only_for_exact_linked_paths(self):
        old_packet, new_packet = copy.deepcopy(self.old_packet), copy.deepcopy(self.old_packet)
        old_packet["sources"] = [{"id": "S1", "url": "https://old.example"}]
        new_packet["sources"] = [{"id": "S2", "url": "https://new.example"}]
        first, second = self.entry("old", old_packet), self.entry("new", new_packet)
        first["source_registry"] = [{"source_id": "S1", "input_paths": [
            "inputs.recognized_revenue"]}]
        second["source_registry"] = [{"source_id": "S2", "input_paths": [
            "inputs.recognized_revenue"]}]
        findings = [{"input_paths": ["inputs.recognized_revenue"], "source_ids": []}]
        self.assertEqual([], campaign._v4_2_remediation_semantic_errors(
            first, second, findings, str(self.root)))
        second["source_registry"][0]["input_paths"].append("inputs.buy_mult")
        errors = campaign._v4_2_remediation_semantic_errors(
            first, second, findings, str(self.root))
        self.assertTrue(any("outside exact linked inputs" in item for item in errors), errors)


if __name__ == "__main__":
    unittest.main()
