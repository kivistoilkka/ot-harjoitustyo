import unittest
from pathlib import Path
from repositories.talent_repository import TalentRepository
from config import NONEXISTING_TALENTS_FILE_PATH, TALENTS_FILE_PATH

class TestTalentRepository(unittest.TestCase):
    def setUp(self):
        self.repository = TalentRepository(TALENTS_FILE_PATH)
        if Path(NONEXISTING_TALENTS_FILE_PATH).exists():
            Path(NONEXISTING_TALENTS_FILE_PATH).unlink()

    def test_repository_finds_all_talents_from_a_file(self):
        self.assertEqual(len(self.repository.find_all()), 9)
 
    def test_find_all_for_certain_archetype(self):
        doctor_talents = self.repository.find_for_archetype("Doctor")
        army_medic = "Army medic: Gain +2 to... (available for Doctor)"
        chief = "Chief physician: When you use... (available for Doctor)"
        emergency = "Emergency medicine: Ignore... (available for Doctor)"

        self.assertEqual(len(doctor_talents), 3)
        self.assertEqual(str(doctor_talents["Army medic"]), army_medic)
        self.assertEqual(str(doctor_talents["Chief physician"]), chief)
        self.assertEqual(str(doctor_talents["Emergency medicine"]), emergency)
    
    def test_deals_with_json_file_that_does_not_exist(self):
        empty_repository = TalentRepository(NONEXISTING_TALENTS_FILE_PATH)
        self.assertEqual(len(empty_repository.find_all()), 0)
