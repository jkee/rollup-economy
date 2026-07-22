import json
import re
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "pipeline" / "v5"))
import build as v5_build
import update_docs


def load(path):
    return json.loads((ROOT / path).read_text())


class DashboardContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.site = load("6digit/six_data_v5.json")
        cls.targets = load("pipeline/blocks/targets_phase3.json")["codes"]
        cls.html = (ROOT / "6digit/index.html").read_text()
        cls.js = (ROOT / "6digit/dashboard.js").read_text()

    def test_dashboard_reads_only_canonical_v5_output(self):
        combined = self.html + self.js
        self.assertIn("six_data_v5.json", self.js)
        self.assertNotIn("six_data_v4.json", combined)
        self.assertNotIn("six_data_v3.json", combined)
        self.assertNotIn("fetch('six_data.json')", self.js)
        self.assertNotIn("pnl_data.json", self.js)

    def test_v5_membership_and_counts_reconcile(self):
        summary = self.site["summary"]
        expected = {item["naics"] for item in self.targets}
        actual = {item["naics"] for item in self.site["records"]}
        self.assertEqual(actual, expected)
        self.assertEqual(summary["published"], 63)
        self.assertEqual(summary["excluded"], 0)
        self.assertEqual(len(self.site["records"]), summary["published"])
        self.assertEqual(sum(summary["tiers"].values()), summary["published"])
        self.assertEqual(sum(summary["readiness"].values()), summary["published"])
        self.assertEqual(sum(summary["actions"].values()), summary["published"])
        self.assertEqual(self.site["exclusions"], [])
        self.assertFalse(self.site["allow_unreviewed"])

    def test_orders_are_complete_and_unique(self):
        orders = sorted(record["order"] for record in self.site["records"])
        self.assertEqual(orders, list(range(1, 64)))
        self.assertNotIn("rank", self.site["records"][0])

    def test_committed_site_matches_fresh_fail_closed_build(self):
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "six_data_v5.json"
            v5_build.build_site(False, site_out=output)
            self.assertEqual(output.read_bytes(), (ROOT / "6digit" / "six_data_v5.json").read_bytes())

    def test_every_primitive_and_source_is_traceable(self):
        researched = {"a", "rho", "e", "s5", "q", "d5", "o"}
        for record in self.site["records"]:
            source_ids = {source["id"] for source in record["sources"]}
            for source in record["sources"]:
                self.assertRegex(source["url"], r"^https?://", (record["naics"], source["id"]))
                self.assertTrue(source["supports"].strip(), (record["naics"], source["id"]))
            self.assertEqual(set(record["factors"]), {"H", "F", "C", "D"})
            self.assertEqual(set(record["primitives"]), researched | {"l", "n"})
            cited = set()
            for name in researched:
                primitive = record["primitives"][name]
                cited.update(primitive["source_ids"])
                self.assertTrue(set(primitive["source_ids"]).issubset(source_ids), (record["naics"], name))
                self.assertTrue(primitive["change_evidence"].strip(), (record["naics"], name))
            audited = [item["source_id"] for item in record["review"]["sources_audited"]]
            self.assertEqual(set(audited), cited, record["naics"])
            self.assertEqual(len(audited), len(set(audited)), record["naics"])

    def test_reviews_and_artifact_links_resolve(self):
        accepted = {"publishable", "publishable_with_caveats"}
        for record in self.site["records"]:
            run = ROOT / "pipeline" / "v5" / "runs" / record["naics"] / record["run_id"]
            self.assertIn(record["review"]["outcome"], accepted, record["naics"])
            self.assertEqual(record["review"]["material_findings"], [], record["naics"])
            self.assertEqual(ROOT / record["memo"], run / "memo.md")
            for name in ("packet.json", "score.json", "memo.md", "review.json"):
                self.assertTrue((run / name).is_file(), run / name)
        self.assertTrue((ROOT / "pipeline" / "v5" / "methodology.md").is_file())

    def test_missing_base_records_are_evidence_first(self):
        missing = [record for record in self.site["records"] if record["A"] is None]
        self.assertEqual([record["naics"] for record in missing], ["523940", "541120"])
        for record in missing:
            self.assertIsNone(record["tier"])
            self.assertIsNone(record["L"])
            self.assertIsNone(record["robust_tier"])
            self.assertEqual(record["readiness"], "STRESS_TEST_ONLY")
            self.assertEqual(record["action"], "EVIDENCE_FIRST")

    def test_interface_exposes_v5_decision_context(self):
        combined = (self.html + self.js).lower()
        for expected in (
            "highest priority means", "validate assumptions", "unknown ≠ low",
            "change evidence", "validator review", "commercial retention",
            "operator-required demand", "model-conditioned",
        ):
            self.assertIn(expected, combined)
        for stale in ("matrix-table", "business process matrix", "p&l modal", "v2 thresholds", "threshold ladder"):
            self.assertNotIn(stale, combined)

    def test_lenses_and_null_values_are_renderable(self):
        self.assertIn("record.lens", self.js)
        self.assertIn("value == null", self.js)
        for record in self.site["records"]:
            self.assertEqual(
                set(record["lens"]),
                {"included_activities", "excluded_activities", "customer_and_revenue_model", "heterogeneous", "deviation_from_default"},
            )

    def test_social_preview_and_archived_root_are_project_local(self):
        image_match = re.search(r'<meta property="og:image" content="([^"]+)">', self.html)
        self.assertIsNotNone(image_match)
        preview = ROOT / "6digit" / image_match.group(1)
        self.assertTrue(preview.is_file(), preview)
        self.assertGreater(preview.stat().st_size, 100_000)
        root_html = (ROOT / "index.html").read_text()
        self.assertIn("4-digit prototype is archived", root_html)
        self.assertIn('href="6digit/"', root_html)

    def test_readme_v5_snapshot_is_generated_and_current(self):
        self.assertEqual((ROOT / "README.md").read_text(), update_docs.expected_readme())


if __name__ == "__main__":
    unittest.main()
