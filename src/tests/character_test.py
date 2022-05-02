import unittest
from entities.character import Character
from entities.talent import Talent
from entities.archetype import Archetype
from .test_helper import TestHelper


class TestCharacter(unittest.TestCase):
    def setUp(self):
        self.talent_army_medic = Talent(
            "Army medic", "Gain +2 to...", "Doctor")
        self.talent_chief = Talent(
            "Chief physician", "When you use...", "Doctor")
        self.talent_emergency = Talent(
            "Emergency medicine", "Ignore...", "Doctor")
        self.doctor_archetype = Archetype(
            "Doctor",
            "Logic",
            "Medicine",
            {
                self.talent_army_medic.name: self.talent_army_medic,
                self.talent_chief.name: self.talent_chief,
                self.talent_emergency.name: self.talent_emergency
            },
            (4, 6),
            [
                "doctor's bag /w medicinal equipment",
                ("liquor", "wine"),
                ("weak horse", "strong poison")
            ]
        )
        self.character = Character("Louis Brugge", self.doctor_archetype, 40)

    def test_constructor_and_getter_methods_work(self):
        helper = TestHelper()
        default_attributes = helper.default_character_attributes()
        default_skills = helper.default_character_skills()
        character = Character("Louis Brugge", self.doctor_archetype, 42)
        self.assertEqual(character.name, "Louis Brugge")
        self.assertEqual(character.archetype.name, "Doctor")
        self.assertEqual(character.age, 42)
        self.assertEqual(character.resources, 4)
        self.assertEqual(len(character.talents), 0)
        self.assertEqual(character.attributes, default_attributes)
        self.assertEqual(character.skills, default_skills)
        self.assertEqual(character.main_attribute, "Logic")
        self.assertEqual(character.main_skill, "Medicine")
        self.assertEqual(character.max_attribute_points, 14)
        self.assertEqual(character.max_skill_points, 12)

    def test_setting_correct_new_name(self):
        self.assertEqual(self.character.name, "Louis Brugge")
        self.character.name = "Praskoviya Gregorius"
        self.assertEqual(self.character.name, "Praskoviya Gregorius")

    def test_new_name_cannot_be_an_empty_string(self):
        original_name = self.character.name
        with self.assertRaises(ValueError) as cm:
            self.character.name = ""
        self.assertEqual(str(cm.exception), "Name cannot be an empty string")
        self.assertEqual(self.character.name, original_name)

    def test_setting_correct_age(self):
        self.assertEqual(self.character.age, 40)
        self.character.age = 17
        self.assertEqual(self.character.age, 17)

    def test_setting_incorrect_age(self):
        with self.assertRaises(ValueError) as cm:
            self.character.age = 16
        self.assertEqual(str(cm.exception), "Age must be 17 or higher")
        self.assertEqual(self.character.age, 40)

    def test_age_related_modifiers_are_set_when_age_is_set(self):
        self.character.age = 50
        self.assertEqual(self.character.max_attribute_points, 14)
        self.assertEqual(self.character.max_skill_points, 12)

    def test_age_related_modifiers_change_when_age_is_changed(self):
        self.character.age = 50
        self.character.age = 51
        self.assertEqual(self.character.max_attribute_points, 13)
        self.assertEqual(self.character.max_skill_points, 14)

    def test_age_cannot_be_changed_with_incorrect_value(self):
        self.character.age = 50
        with self.assertRaises(ValueError) as cm:
            self.character.age = -1
        self.assertEqual(str(cm.exception), "Age must be 17 or higher")
        self.assertEqual(self.character.age, 50)
        self.assertEqual(self.character.max_attribute_points, 14)
        self.assertEqual(self.character.max_skill_points, 12)
