import sys
import unittest
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "prototype"))

from asri_reflection import reflect  # noqa: E402


class PrototypeScenarioTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.scenarios = yaml.safe_load((ROOT / "tests/scenarios.yaml").read_text())["scenarios"]

    def test_scenarios(self):
        for scenario in self.scenarios:
            with self.subTest(scenario=scenario["id"]):
                result = reflect(scenario["event"])
                selected = {item["id"] for item in result["selected_objects"]}
                self.assertLessEqual(len(selected), 3)
                self.assertEqual(result["safety"]["flagged"], scenario["safety"])
                self.assertTrue(set(scenario.get("expect_all", [])) <= selected)
                if scenario.get("expect_any"):
                    self.assertTrue(set(scenario["expect_any"]) & selected)
                self.assertFalse(set(scenario.get("expect_none", [])) & selected)
                self.assertIn("döntést te végzed", result["human_authorship"])

    def test_no_match_is_explicit(self):
        result = reflect("A kék bögre az asztalon van.")
        self.assertTrue(result["no_match"])
        self.assertEqual(result["selected_objects"], [])


if __name__ == "__main__":
    unittest.main()

