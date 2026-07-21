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
        cls.site = load("6digit/six_data_v3.json")
        cls.campaign = load("pipeline/build/campaign_report_v3_1_2.json")
        cls.golden = load("pipeline/build/golden_analysis_v3_1_2.json")
        cls.html = (ROOT / "6digit/index.html").read_text()
        cls.js = (ROOT / "6digit/dashboard.js").read_text()

    def test_dashboard_reads_only_canonical_phase4_outputs(self):
        self.assertIn("six_data_v3.json", self.js)
        self.assertIn("campaign_report_v3_1_2.json", self.js)
        self.assertIn("golden_analysis_v3_1_2.json", self.js)
        self.assertNotIn("fetch('six_data.json')", self.js)
        self.assertNotIn("pnl_data.json", self.js)

    def test_closed_campaign_counts_reconcile(self):
        campaign = self.campaign
        self.assertTrue(campaign["campaign_closed"])
        self.assertTrue(campaign["phase4_complete"])
        self.assertEqual(campaign["published"] + campaign["excluded"], campaign["planned"]["total"])
        self.assertEqual(len(campaign["attempts"]), campaign["attempt_counts"]["total"])
        self.assertEqual(len(self.site["records"]), campaign["build_stats"]["published"])
        self.assertEqual(len(self.golden["records"]), campaign["planned"]["golden"])

    def test_exclusions_never_enter_fleet_rankings(self):
        excluded = {item["naics"] for item in self.campaign["exclusions"]}
        published_fleet = {item["naics"] for item in self.site["records"]}
        self.assertTrue(excluded)
        self.assertTrue(excluded.isdisjoint(published_fleet))

    def test_every_score_input_has_traceability(self):
        for record in self.site["records"]:
            source_ids = {source["id"] for source in record["sources"]}
            for source in record["sources"]:
                self.assertRegex(source["url"], r"^https?://", (record["naics"], source["id"]))
            for name, item in record["evidence"]["inputs"].items():
                self.assertIn(item["method"], {"OBSERVED", "CALCULATED", "ESTIMATE"}, (record["naics"], name))
                self.assertIn("rationale", item, (record["naics"], name))
                self.assertIn("plausible_range", item, (record["naics"], name))
                self.assertTrue(set(item.get("source_ids", [])).issubset(source_ids), (record["naics"], name))
            roles = record["evidence"]["inputs"]["ai_replaceable_share"]["breakdown_by_role"]
            self.assertAlmostEqual(sum(role["contribution"] for role in roles), record["evidence"]["inputs"]["ai_replaceable_share"]["value"], places=9)

    def test_current_campaign_artifact_links_resolve(self):
        for item in self.campaign["records"]:
            naics, run_id, kind = item["naics"], item["run_id"], item["kind"]
            record_root = "golden_v3_1_2" if kind == "golden" else "runs"
            paths = [
                f"pipeline/packets/{naics}/{run_id}.json",
                f"pipeline/{record_root}/{naics}/{run_id}.json",
                f"pipeline/memos/{naics}/{run_id}.md",
                f"pipeline/review/{naics}/{run_id}.json",
            ]
            for path in paths:
                self.assertTrue((ROOT / path).is_file(), path)

    def test_obsolete_interface_concepts_are_absent(self):
        combined = (self.html + self.js).lower()
        for stale in ("matrix-table", "business process matrix", "p&l modal", "v2 thresholds", "threshold ladder"):
            self.assertNotIn(stale, combined)
        self.assertIn("golden-set diagnostics", combined)
        self.assertIn("exclusions ledger", combined)

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
