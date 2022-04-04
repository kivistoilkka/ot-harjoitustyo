import unittest
from .test_helper import TestHelper
from entities.character import Character

class TestCharacter(unittest.TestCase):
    def setUp(self):
        self.character = Character("Louis Brugge")

    def test_constructor_and_getter_methods_work(self):
        default_attributes = TestHelper.default_character_attributes()
        default_skills = TestHelper.default_character_skills()
        character = Character("Louis Brugge")
        self.assertEqual(character.name, "Louis Brugge")
        self.assertEqual(character.archetype, None)
        self.assertEqual(character.age, None)
        self.assertEqual(character.resources, None)
        self.assertEqual(len(character.talents), 0)
        self.assertEqual(character.attributes, default_attributes)
        self.assertEqual(character.skills, default_skills)
        self.assertEqual(character.main_attribute, None)
        self.assertEqual(character.main_skill, None)
        self.assertEqual(character.max_attribute_points, None)
        self.assertEqual(character.max_skill_points, None)
    
    def test_setting_correct_new_name(self):
        self.character.name = "Praskoviya Gregorius"
        self.assertEqual(self.character.name, "Praskoviya Gregorius")

    def test_new_name_cannot_be_an_empty_string(self):
        original_name = self.character.name
        with self.assertRaises(ValueError) as cm:
            self.character.name = ""
        self.assertEqual(str(cm.exception), "Name cannot be an empty string")
        self.assertEqual(self.character.name, original_name)

    def test_setting_correct_age(self):
        self.character.age = 17
        self.assertEqual(self.character.age, 17)
    
    def test_setting_incorrect_age(self):
        with self.assertRaises(ValueError) as cm:
            self.character.age = 16
        self.assertEqual(str(cm.exception), "Age must be 17 or higher")
        self.assertEqual(self.character.age, None)
    
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