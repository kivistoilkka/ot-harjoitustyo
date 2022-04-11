from entities.character import Character
from entities.archetype import Archetype
from entities.talent import Talent

bookworm = Talent("Bookworm", "Gain +2 to...")
erudite = Talent("Erudite", "You can pass a...")
knowledge_is_reassuring = Talent(
    "Knowledge is Reassuring", "Ignore Conditions when...")
academic_talent_dict = {bookworm.name: bookworm, erudite.name: erudite,
                        knowledge_is_reassuring.name: knowledge_is_reassuring}
academic_equipment_list = [
    ("book collection", "map book"), "writing utensils", ("liquor", "slide rule")]
academic = Archetype("Academic", "Logic", "Learning",
                     academic_talent_dict, (4, 6), academic_equipment_list)

army_medic = Talent("Army medic", "Gain +2 to...")
chief_physician = Talent("Chief physician", "When you use...")
emergency_medicine = Talent("Emergency medicine", "Ignore...")
doctor_talent_dict = {army_medic.name: army_medic,
                      chief_physician.name: chief_physician, emergency_medicine.name: emergency_medicine}
doctor_equipment_list = ["doctor's bag /w medicinal equipment",
                         ("liquor", "wine"), ("weak horse", "strong poison")]
doctor = Archetype("Doctor", "Logic", "Medicine",
                   doctor_talent_dict, (4, 6), doctor_equipment_list)

AVAILABLE_ARCHETYPES = {academic.name: academic, doctor.name: doctor}
ARCHETYPE_NAMES = list(AVAILABLE_ARCHETYPES.keys())


class CharacterService:
    def __init__(self, character: Character = None):
        self._character = character

    def create_character(self, name: str, archetype: Archetype, age: int):
        if name == "":
            raise ValueError("Name cannot be an empty string")
        self._character = Character(name)
        self._character.set_archetype(archetype)
        self._character.age = age

    def set_character_name(self, name: str):
        if self._character:
            self._character.name = name
        else:
            raise AttributeError(
                "Character has to be created before it can be renamed")

    def set_character_archetype(self, name: str):
        if name in AVAILABLE_ARCHETYPES:
            self._character.set_archetype(AVAILABLE_ARCHETYPES[name])
        else:
            raise ValueError("Given archetype is not available")

    def set_character_age(self, age: int):
        self._character.age = age

    def character_max_attribute_points(self):
        return self._character.max_attribute_points

    def character_max_skill_points(self):
        return self._character.max_skill_points

    def character_talents(self):
        return self._character.talents

    def give_talent_to_character(self, name: str):
        self._character.give_talent(name)

    def remove_character_talents(self):
        self._character.remove_talents()

    def character_attributes_as_list(self):
        return self._character.get_attributes_as_list()

    def character_skills_as_list(self):
        return self._character.get_skills_as_list()

    def character_attribute_points_left(self):
        return self._character.attribute_points_left()

    def character_skill_points_left(self):
        return self._character.skill_points_left()

    def character_resources(self):
        return self._character.resources

    def change_character_resources(self, amount: int):
        self._character.change_resources(amount)

    def reset_character_resources(self):
        self._character.reset_resources()

    def character_attributes(self):
        return self._character.attributes

    def character_main_attribute(self):
        return self._character.main_attribute

    def change_character_attribute(self, attribute: str, amount: int):
        self._character.change_attribute(attribute, amount)

    def reset_character_attributes(self):
        self._character.reset_attributes()

    def character_skills(self):
        return self._character.skills

    def character_main_skill(self):
        return self._character.main_skill

    def change_character_skill(self, skill: str, amount: int):
        self._character.change_skill(skill, amount)

    def reset_character_skills(self):
        self._character.reset_skills()

    def character_equipment(self):
        return self._character.equipment

    def set_character_equipment(self, equipment: list):
        self._character.equipment = equipment

    def save_character_to_file(self, filename: str):
        self._character.save_to_file(filename)

    def full_character_sheet(self) -> list:
        character_sheet = []
        character_sheet.append(
            f"{self._character.name}, {self._character.age} ({self._character.age_group(self._character.age)})")
        character_sheet.append(self._character.archetype.name)
        character_sheet.append("")

        character_sheet.append("Talents:")
        for talent in self._character.talents:
            character_sheet.append(str(talent))
        character_sheet.append("")

        character_sheet.append("Attributes:")
        for attribute in self._character.get_attributes_as_list():
            character_sheet.append(attribute)
        character_sheet.append("")

        character_sheet.append("Skills:")
        for skill in self._character.get_skills_as_list():
            character_sheet.append(skill)
        character_sheet.append("")

        character_sheet.append("Equipment:")
        for item in self._character.equipment:
            character_sheet.append(f"- {item}")
        character_sheet.append("")

        character_sheet.append(
            f"Attribute points left: {self._character.attribute_points_left()}")
        character_sheet.append(
            f"Skill/resource points left: {self._character.skill_points_left()}")
        character_sheet.append("")

        character_sheet.append(f"Resources: {self._character.resources}")

        return character_sheet
