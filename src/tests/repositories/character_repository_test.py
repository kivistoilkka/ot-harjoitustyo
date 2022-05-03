import unittest
import os
from repositories.character_repository import CharacterRepository


class TestCharacterRepository(unittest.TestCase):
    def setUp(self):
        self.repository = CharacterRepository()

    def test_repository_opens_character_from_the_file(self):
        character = self.repository.open_character(
            f"{os.path.dirname(__file__)}/test_character.json"
        )
        self.assertEqual(
            str(character),
            "JSON-tester, 55 (Old), Hunter (main attribute Precision, main skill Ranged combat)"
        )
        self.assertEqual(
            str(character.talents[0]),
            "Marksman: Gain +2 to... (available for Hunter)"
        )
        self.assertEqual(len(character.attributes), 4)
        self.assertEqual(character.attribute_points_left(), 0)
        self.assertEqual(len(character.skills), 12)
        self.assertEqual(character.resources, 3)
        self.assertEqual(character.skill_points_left(), 0)
        self.assertEqual(len(character.equipment), 3)
