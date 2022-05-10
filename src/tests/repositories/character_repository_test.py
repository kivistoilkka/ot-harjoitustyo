import unittest
import os
from pathlib import Path

from tests.test_helper import TestHelper

from repositories.character_repository import CharacterRepository


class TestCharacterRepository(unittest.TestCase):
    def setUp(self):
        self.repository = CharacterRepository()

    def test_repository_opens_character_from_the_file(self):
        character = self.repository.open_character(
            f"{os.path.dirname(__file__)}/../test_characters/test_character.json"
        )
        self.assertEqual(
            str(character),
            "Stanley, 42 (Middle aged), Hunter (main attribute Precision, main skill Ranged combat)"
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

    def test_character_exporting_works(self):
        if Path(f"{os.path.dirname(__file__)}/stanley.txt").exists():
            Path(f"{os.path.dirname(__file__)}/stanley.txt").unlink()
        helper = TestHelper()
        stanley = helper.create_character()
        self.repository.export_character_sheet(stanley, f"{os.path.dirname(__file__)}/stanley.txt")
        expected = [
            "Stanley, 42 (Middle aged)\n",
            "Academic\n",
            "\n",
            "Talents:\n",
            "Knowledge is Reassuring: Ignore Conditions when...\n",
            "\n",
            "Attributes:\n",
            "Physique       2\n",
            "Precision      5\n",
            "Logic          4 (Main)\n",
            "Empathy        3\n",
            "\n",
            "Skills:\n",
            "Agility        1\n",
            "Close combat   0\n",
            "Force          0\n",
            "Medicine       0\n",
            "Ranged combat  2\n",
            "Stealth        2\n",
            "Investigation  1\n",
            "Learning       3 (Main)\n",
            "Vigilance      1\n",
            "Inspiration    0\n",
            "Manipulation   0\n",
            "Observation    1\n",
            "\n",
            "Equipment:\n",
            "- map book\n",
            "- writing utensils\n",
            "- slide rule\n",
            "\n",
            "Attribute points left: 0\n",
            "Skill/resource points left: 0\n",
            "\n",
            "Resources: 5\n",
            "\n",
            "Character description:\n",
            "This is a story of a man named Stanley.\n"
        ]

        with open(f"{os.path.dirname(__file__)}/stanley.txt") as file:
            row_number = 0
            for row in file:
                self.assertEqual(row, expected[row_number])
                row_number += 1

    def test_character_with_missing_fields_cannot_be_opened(self):
        missing_field_filenames = [
            "missing_name.json",
            "missing_age.json",
            "missing_archetype.json",
            "missing_talents.json",
            "missing_attributes.json",
            "missing_skills.json",
            "missing_equipment.json",
            "missing_resources.json",
            "missing_description.json",

        ]
        for file in missing_field_filenames:
            with self.assertRaises(ValueError):
                self.repository.open_character(
                    f"{os.path.dirname(__file__)}/../test_characters/{file}"
                )

    def test_character_with_wrong_basic_information_cannot_be_opened(self):
        basic_information_filenames = [
            "name_empty_string.json",
            "archetype_does_not_exist.json",
            "age_too_low.json",
        ]
        for file in basic_information_filenames:
            with self.assertRaises(ValueError):
                self.repository.open_character(
                    f"{os.path.dirname(__file__)}/../test_characters/{file}"
                )

    def test_character_with_wrong_talent_cannot_be_opened(self):
        with self.assertRaises(ValueError):
            self.repository.open_character(
                f"{os.path.dirname(__file__)}/../test_characters/talent_does_not_exist.json"
            )

    def test_character_with_wrong_attributes_cannot_be_opened(self):
        #TODO: test too many points in main attribute
        attributes_filenames = [
            "attributes_missing_attribute.json",
            "attributes_too_many_points_used.json",
            "attributes_too_many_points_in_non_main_attribute.json",
            "attributes_too_low_value.json"
        ]
        for file in attributes_filenames:
            with self.assertRaises(ValueError):
                self.repository.open_character(
                    f"{os.path.dirname(__file__)}/../test_characters/{file}"
                )

    def test_character_with_wrong_skills_cannot_be_opened(self):
        skills_filenames = [
            "skills_missing_skill.json",
            "skills_too_many_points_used.json",
            "skills_too_many_points_in_non_main_skill.json",
            "skills_too_many_points_in_main_skill.json",
            "skills_too_low_value.json"
        ]
        for file in skills_filenames:
            with self.assertRaises(ValueError):
                self.repository.open_character(
                    f"{os.path.dirname(__file__)}/../test_characters/{file}"
                )

    def test_character_with_wrong_equipment_cannot_be_opened(self):
        equipment_filenames = [
            "equipment_too_few_items.json",
            "equipment_too_many_items.json",
            "equipment_items_not_available_for_archetype.json",
            "equipment_two_items_from_one_choice.json"
        ]
        for file in equipment_filenames:
            with self.assertRaises(ValueError):
                self.repository.open_character(
                    f"{os.path.dirname(__file__)}/../test_characters/{file}"
                )

    def test_character_with_wrong_resources_cannot_be_opened(self):
        resource_filenames = [
            "resources_too_much_resources_for_archetype.json",
            "resources_too_few_resources_for_archetype.json"
        ]
        for file in resource_filenames:
            with self.assertRaises(ValueError):
                self.repository.open_character(
                    f"{os.path.dirname(__file__)}/../test_characters/{file}"
                )
