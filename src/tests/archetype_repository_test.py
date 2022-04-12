import unittest
from pathlib import Path
from repositories.archetype_repository import ArchetypeRepository
from config import ARCHETYPES_FILE_PATH, NONEXISTING_FILE_PATH


class TestArchetypeRepository(unittest.TestCase):
    def setUp(self):
        self.repository = ArchetypeRepository(ARCHETYPES_FILE_PATH)
        if Path(NONEXISTING_FILE_PATH).exists():
            Path(NONEXISTING_FILE_PATH).unlink()

    def test_repository_finds_all_archetypes_from_a_file(self):
        archetypes = self.repository.find_all()
        self.assertEqual(len(archetypes), 3)
        self.assertTrue("Academic" in archetypes.keys())
        self.assertTrue("Doctor" in archetypes.keys())
        self.assertTrue("Hunter" in archetypes.keys())
    
    def test_certain_archetype_information_is_correct(self):
        hunter = self.repository.find_all()["Hunter"]
        self.assertEqual(hunter.name, "Hunter")
        self.assertEqual(hunter.main_attribute, "Precision")
        self.assertEqual(hunter.main_skill, "Ranged combat")
        self.assertEqual(len(hunter.talents), 3)
        self.assertEqual(str(hunter.talents["Bloodhound"]), "Bloodhound: Gain +2 to... (available for Hunter)")
        self.assertEqual(str(hunter.talents["Herbalist"]), "Herbalist: By utilizing... (available for Hunter)")
        self.assertEqual(str(hunter.talents["Marksman"]), "Marksman: Gain +2 to... (available for Hunter)")
        self.assertEqual(hunter.resource_boundaries, (2, 4))
        self.assertEqual(len(hunter.equipment), 3)
        self.assertEqual(hunter.equipment[0], "rifle")
        self.assertEqual(hunter.equipment[1], ("hunting knife", "hunting dog"))
        self.assertEqual(hunter.equipment[2], ("hunting trap", "hunting equipment"))

    def test_deals_with_json_file_that_does_not_exist(self):
        empty_repository = ArchetypeRepository(NONEXISTING_FILE_PATH)
        self.assertEqual(len(empty_repository.find_all()), 0)
