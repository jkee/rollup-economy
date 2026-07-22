import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "pipeline" / "build"))
import update_dashboard_docs


def load(path):
    return json.loads((ROOT / path).read_text())


class DashboardContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.site = load("6digit/six_data_v4.json")
        cls.v3 = load("6digit/six_data_v3.json")
        cls.targets = load("pipeline/blocks/targets_phase3.json")["codes"]
        cls.html = (ROOT / "6digit/index.html").read_text()
        cls.js = (ROOT / "6digit/dashboard.js").read_text()

    def test_dashboard_reads_only_canonical_phase4_outputs(self):
        self.assertIn("six_data_v4.json", self.js)
        self.assertIn("six_data_v3.json", self.html)
        self.assertNotIn("fetch('six_data.json')", self.js)
        self.assertNotIn("pnl_data.json", self.js)

    def test_phase4_membership_and_counts_reconcile(self):
        expected = {item["naics"] for item in self.targets}
        actual = {item["naics"] for item in self.site["records"]}
        self.assertEqual(actual, expected)
        self.assertEqual(self.site["summary"]["membership"], 63)
        self.assertEqual(self.site["summary"]["complete_base"] + self.site["summary"]["missing_base"], 63)
        self.assertEqual(sum(self.site["summary"]["tier_counts"].values()), 63)

    def test_v3_is_preserved_as_comparison(self):
        v3_by_code = {item["naics"]: item for item in self.v3["records"]}
        for record in self.site["records"]:
            if record["naics"] in v3_by_code:
                self.assertEqual(record["v3"]["S"], v3_by_code[record["naics"]]["S"])
                self.assertEqual(record["v3"]["verdict"], v3_by_code[record["naics"]]["verdict"])

    def test_every_score_input_has_traceability(self):
        for record in self.site["records"]:
            source_ids = {source["id"] for source in record["sources"]}
            for source in record["sources"]:
                self.assertRegex(source["url"], r"^https?://", (record["naics"], source["id"]))
            self.assertEqual(set(record["factors"]), {"H", "F", "C", "D"})
            for factor, item in record["evidence"].items():
                self.assertIn(item["state"], {"mixed", "elicited", "missing"}, (record["naics"], factor))
                for leaf in item.get("leaves", {}).values():
                    if isinstance(leaf, dict):
                        self.assertTrue(set(leaf.get("source_ids", [])).issubset(source_ids), (record["naics"], factor))

    def test_v4_and_source_artifact_links_resolve(self):
        for record in self.site["records"]:
            v4_path = ROOT / "pipeline" / "v4_3" / "runs" / record["naics"] / "v4_3_minimal.json"
            v3_path = ROOT / "pipeline" / "runs" / record["naics"] / (record["source_run"]["run_id"] + ".json")
            self.assertTrue(v4_path.is_file(), v4_path)
            self.assertTrue(v3_path.is_file(), v3_path)

    def test_unknown_is_not_ranked_as_adverse(self):
        unknown = [record for record in self.site["records"] if record["A"] is None]
        self.assertEqual([record["naics"] for record in unknown], ["541120"])
        self.assertIsNone(unknown[0]["tier"])
        self.assertIsNone(unknown[0]["rank"])
        self.assertEqual(unknown[0]["readiness"], "STRESS_TEST_ONLY")
        self.assertEqual(unknown[0]["action"], "EVIDENCE_FIRST")

    def test_obsolete_interface_concepts_are_absent(self):
        combined = (self.html + self.js).lower()
        for stale in ("matrix-table", "business process matrix", "p&l modal", "v2 thresholds", "threshold ladder"):
            self.assertNotIn(stale, combined)
        self.assertIn("unknown ≠ low", combined)
        self.assertIn("validate assumptions", combined)
        self.assertIn("highest priority means", combined)

    def test_social_preview_is_project_local(self):
        preview = ROOT / "6digit" / "og-phase4.png"
        self.assertTrue(preview.is_file())
        self.assertGreater(preview.stat().st_size, 100_000)
        self.assertIn('content="og-phase4.png"', self.html)

    def test_archived_root_points_to_current_dashboard(self):
        root_html = (ROOT / "index.html").read_text()
        self.assertIn("4-digit prototype is archived", root_html)
        self.assertIn('href="6digit/"', root_html)

    def test_readme_snapshot_is_generated_and_current(self):
        self.assertEqual((ROOT / "README.md").read_text(), update_dashboard_docs.updated_readme())


if __name__ == "__main__":
    unittest.main()
