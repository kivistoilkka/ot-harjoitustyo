import unittest
from entities.character import Character
from entities.archetype import Archetype
from entities.talent import Talent
from services.character_service import CharacterService
from tests.test_helper import TestHelper


class TestCharacterService(unittest.TestCase):
    def setUp(self):
        self.character_service = CharacterService()
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
        self.tester_character = Character("Tester", self.doctor_archetype, 42)

    def test_character_creation(self):
        created_manually = str(self.tester_character)
        self.character_service.create_character("Tester", "Doctor", 42)
        created_by_service = self.character_service.get_character_summary()
        self.assertEqual(created_by_service, str(created_manually))

    def test_character_cannot_be_created_with_nonexisting_archetype(self):
        with self.assertRaises(ValueError) as cm:
            self.character_service.create_character("Tester", "Imaginary", 42)
        self.assertEqual(str(cm.exception), "Given archetype is not available")

    def test_character_cannot_be_created_with_non_integer_age(self):
        with self.assertRaises(ValueError) as cm:
            self.character_service.create_character(
                "Tester", "Doctor", "forty-two")
        self.assertEqual(str(cm.exception), "Give the age value as an integer")

    def test_character_cannot_be_created_with_age_under_17(self):
        with self.assertRaises(ValueError) as cm:
            self.character_service.create_character("Tester", "Doctor", 16)
        self.assertEqual(str(cm.exception), "Character age must be over 17")

    def test_character_summary_works_when_character_is_created(self):
        self.character_service.create_character("Tester", "Doctor", 42)
        summary = self.character_service.get_character_summary()
        self.assertEqual(
            summary, "Tester, 42 (Middle aged), Doctor (main attribute Logic, main skill Medicine)")

    def test_character_cannot_summarized_before_creation(self):
        with self.assertRaises(ValueError) as cm:
            self.character_service.get_character_summary()
        self.assertEqual(
            str(cm.exception), "Character has to be created before it can be summarized")

    def test_name_getter_works(self):
        self.character_service.create_character("Tester", "Doctor", 42)
        name = self.character_service.get_character_name()
        self.assertEqual(name, "Tester")

    def test_name_getter_does_not_work_if_character_is_not_created(self):
        with self.assertRaises(ValueError) as cm:
            self.character_service.get_character_name()
        self.assertEqual(
            str(cm.exception), "Character has to be created before it can have a name")

    def test_character_renaming(self):
        self.tester_character.name = "Supertester"
        self.character_service.create_character("Tester", "Doctor", 42)
        self.character_service.set_character_name("Supertester")
        summary_from_service = self.character_service.get_character_summary()
        self.assertEqual(summary_from_service, str(self.tester_character))

    def test_character_cannot_be_created_with_empty_string_as_a_name(self):
        with self.assertRaises(ValueError) as cm:
            self.character_service.create_character("", "Doctor", 42)
        self.assertEqual(str(cm.exception), "Name cannot be an empty string")

    def test_renaming_does_not_work_with_empty_string(self):
        self.character_service.create_character("Tester", "Doctor", 42)
        with self.assertRaises(ValueError) as cm:
            self.character_service.set_character_name("")
        self.assertEqual(str(cm.exception), "Name cannot be an empty string")

    def test_renaming_does_not_work_without_created_character(self):
        with self.assertRaises(ValueError) as cm:
            self.character_service.set_character_name("Supertester")
        self.assertEqual(
            str(cm.exception), "Character has to be created before it can be renamed")

    def test_list_of_archetype_options_is_correct(self):
        options = self.character_service.get_archetype_options()
        self.assertEqual(len(options), 3)
        self.assertTrue("Academic" in options)
        self.assertTrue("Doctor" in options)
        self.assertTrue("Hunter" in options)

    def test_archetype_name_getter_works(self):
        self.character_service.create_character("Tester", "Doctor", 42)
        archetype_name = self.character_service.get_character_archetype_name()
        self.assertEqual(archetype_name, "Doctor")

    def test_archetype_name_getter_does_not_work_if_character_is_not_created(self):
        with self.assertRaises(ValueError) as cm:
            self.character_service.get_character_archetype_name()
        self.assertEqual(
            str(cm.exception), "Character has to be created before it can have an archetype")

    def test_archetype_changing_works(self):
        self.character_service.create_character("Tester", "Doctor", 42)
        self.character_service.set_character_archetype("Academic")
        archetype_name = self.character_service.get_character_archetype_name()
        self.assertEqual(archetype_name, "Academic")

    def test_archetype_changing_does_not_work_with_invalid_archetype_name(self):
        self.character_service.create_character("Tester", "Doctor", 42)
        with self.assertRaises(ValueError) as cm:
            self.character_service.set_character_archetype("Imaginary")
        self.assertEqual(str(cm.exception), "Given archetype is not available")

    def test_archetype_changing_does_not_work_if_character_is_not_created(self):
        with self.assertRaises(ValueError) as cm:
            self.character_service.set_character_archetype("Academic")
        self.assertEqual(str(
            cm.exception), "Character has to be created before the archetype can be changed")

    def test_age_getter_works(self):
        self.character_service.create_character("Tester", "Doctor", 42)
        age = self.character_service.get_character_age()
        self.assertEqual(age, 42)

    def test_archetype_age_getter_does_not_work_if_character_is_not_created(self):
        with self.assertRaises(ValueError) as cm:
            self.character_service.get_character_age()
        self.assertEqual(
            str(cm.exception), "Character has to be created before it can have an age")

    def test_age_setter_works_with_valid_age(self):
        self.character_service.create_character("Tester", "Doctor", 42)
        self.character_service.set_character_age(17)
        age = self.character_service.get_character_age()
        self.assertEqual(age, 17)

    def test_age_setter_does_not_work_with_age_under_17(self):
        self.character_service.create_character("Tester", "Doctor", 42)
        with self.assertRaises(ValueError) as cm:
            self.character_service.set_character_age(16)
        self.assertEqual(str(cm.exception),
                         "Give the value as an integer, which is 17 or more")

    def test_age_setter_does_not_work_with_wrong_type_of_input(self):
        self.character_service.create_character("Tester", "Doctor", 42)
        with self.assertRaises(ValueError) as cm:
            self.character_service.set_character_age("fourty-two")
        self.assertEqual(str(cm.exception),
                         "Give the value as an integer, which is 17 or more")

    def test_age_setter_does_not_work_if_character_is_not_created(self):
        with self.assertRaises(ValueError) as cm:
            self.character_service.set_character_age(17)
        self.assertEqual(
            str(cm.exception), "Character has to be created before the age can be changed")

    def test_age_group_getter_works_with_correct_inputs(self):
        self.assertEqual(
            self.character_service.get_character_agegroup(99), "Old")
        self.character_service.create_character("Tester", "Doctor", 26)
        self.assertEqual(
            self.character_service.get_character_agegroup(), "Middle aged")
        self.assertEqual(
            self.character_service.get_character_agegroup(17), "Young")
        self.assertEqual(
            self.character_service.get_character_agegroup(25), "Young")
        self.assertEqual(
            self.character_service.get_character_agegroup(50), "Middle aged")
        self.assertEqual(
            self.character_service.get_character_agegroup(51), "Old")
        self.character_service.set_character_age(72)
        self.assertEqual(
            self.character_service.get_character_agegroup(), "Old")

    def test_age_group_getter_does_not_work_if_character_is_not_created_and_if_age_parameter_is_not_given(self):
        with self.assertRaises(ValueError) as cm:
            self.character_service.get_character_agegroup()
        self.assertEqual(str(cm.exception),
                         "Character not created, give an age value in integer")

    def test_list_of_talent_options_is_correct(self):
        self.character_service.create_character("Tester", "Doctor", 26)
        options = self.character_service.get_talent_options()
        self.assertEqual(len(options), 3)
        self.assertTrue("Army medic" in options)
        self.assertTrue("Chief physician" in options)
        self.assertTrue("Emergency medicine" in options)

    def test_list_of_talent_options_cannot_be_given_if_character_is_not_created(self):
        with self.assertRaises(ValueError) as cm:
            self.character_service.get_talent_options()
        self.assertEqual(str(
            cm.exception), "Character has to be created before talent options can be returned")

    def test_talent_giver_and_talent_getter_work_with_available_talent(self):
        self.character_service.create_character("Tester", "Doctor", 26)
        self.character_service.give_talent_to_character("Emergency medicine")
        talent = self.character_service.get_character_talents()
        self.assertEqual(
            str(talent[0]), "Emergency medicine: Ignore... (available for Doctor)")

    def test_talent_getter_returns_none_when_character_is_created_but_no_talents_are_given(self):
        self.character_service.create_character("Tester", "Doctor", 26)
        talent = self.character_service.get_character_talents()
        self.assertEqual(talent, None)

    def test_talent_giver_does_not_work_when_character_is_not_created(self):
        with self.assertRaises(ValueError) as cm:
            self.character_service.give_talent_to_character(
                "Emergency medicine")
        self.assertEqual(
            str(cm.exception), "Character has to be created before talents can be given")

    def test_talent_getter_does_not_work_when_character_is_not_created(self):
        with self.assertRaises(ValueError) as cm:
            self.character_service.get_character_talents()
        self.assertEqual(
            str(cm.exception), "Character has to be created before it can have talents")

    def test_talent_giver_replaces_any_existing_talents(self):
        self.character_service.create_character("Tester", "Doctor", 26)
        self.character_service.give_talent_to_character("Emergency medicine")
        self.character_service.give_talent_to_character("Chief physician")
        talent = self.character_service.get_character_talents()
        self.assertEqual(
            str(talent[0]), "Chief physician: When you use... (available for Doctor)")

    def test_attribute_getter_works(self):
        helper = TestHelper()
        self.character_service.create_character("Tester", "Doctor", 26)
        character_attributes = self.character_service.get_character_attributes()
        self.assertEqual(character_attributes,
                         helper.default_character_attributes())

    def test_attribute_getter_does_not_work_when_character_is_not_created(self):
        with self.assertRaises(ValueError) as cm:
            self.character_service.get_character_attributes()
        self.assertEqual(str(
            cm.exception), "Character has to be created before attributes can be returned")

    def test_main_attribute_getter_works(self):
        self.character_service.create_character("Tester", "Doctor", 26)
        main_attribute = self.character_service.get_character_main_attribute()
        self.assertEqual(main_attribute, "Logic")

    def test_main_attribute_points_left_works(self):
        self.character_service.create_character("First", "Doctor", 17)
        points_left = self.character_service.get_character_attribute_points_left()
        self.assertEqual(points_left, 15-4*2)
        self.character_service.create_character("Second", "Doctor", 26)
        points_left = self.character_service.get_character_attribute_points_left()
        self.assertEqual(points_left, 14-4*2)
        self.character_service.create_character("Third", "Doctor", 51)
        points_left = self.character_service.get_character_attribute_points_left()
        self.assertEqual(points_left, 13-4*2)
