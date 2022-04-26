from entities.character import Character
from entities.archetype import Archetype

from repositories.archetype_repository import archetype_repository

AVAILABLE_ARCHETYPES = archetype_repository.find_all()


class CharacterService:
    def __init__(self, character: Character = None):
        self._character = character

    def create_character(self, name: str, archetype: Archetype, age: int):
        if name == "":
            raise ValueError("Name cannot be an empty string")
        self._character = Character(name)
        if archetype not in AVAILABLE_ARCHETYPES:
            raise ValueError("Given archetype is not available")
        self._character.set_archetype(AVAILABLE_ARCHETYPES[archetype])
        if not isinstance(age, int):
            raise ValueError("Give the age value as an integer")
        if age < 17:
            raise ValueError("Character age must be over 17")
        self._character.age = age

    def get_character_summary(self):
        if self._character:
            return str(self._character)
        raise ValueError(
            "Character has to be created before it can be summarized")

    def get_character_name(self):
        if self._character:
            return self._character.name
        raise ValueError(
            "Character has to be created before it can have a name")

    def set_character_name(self, name: str):
        if self._character:
            self._character.name = name
        else:
            raise ValueError(
                "Character has to be created before it can be renamed")

    def get_character_archetype_name(self):
        if self._character:
            return self._character.archetype.name
        raise ValueError(
            "Character has to be created before it can have an archetype")

    def set_character_archetype(self, name: str):
        if self._character:
            if name in AVAILABLE_ARCHETYPES:
                self._character.set_archetype(AVAILABLE_ARCHETYPES[name])
            else:
                raise ValueError("Given archetype is not available")
        else:
            raise ValueError(
                "Character has to be created before the archetype can be changed")

    def get_character_age(self):
        if self._character:
            return self._character.age
        raise ValueError(
            "Character has to be created before it can have an age")

    def set_character_age(self, age: int):
        if self._character:
            if isinstance(age, int):
                self._character.age = age
            else:
                raise ValueError("Give the value as an integer")
        else:
            raise ValueError(
                "Character has to be created before the age can be changed")

    def get_character_agegroup(self, age: int = None):
        if self._character:
            if not age:
                age = self._character.age
            return self._character.age_group(age)
        dummy = Character("Dummy")
        if not age or not isinstance(age, int):
            raise ValueError(
                "Character not created, give an age value in integer")
        return dummy.age_group(age)

    def get_archetype_options(self):
        return list(AVAILABLE_ARCHETYPES.keys())

    def get_character_talents(self):
        if len(self._character.talents) == 0:
            return None
        return self._character.talents

    def get_talent_options(self) -> dict:
        if self._character.archetype:
            return self._character.archetype.talents
        raise ValueError("Choose archetype first")

    def give_talent_to_character(self, name: str):
        self._character.give_talent(name)

    def get_character_attributes(self):
        return self._character.attributes

    def get_character_main_attribute(self):
        return self._character.main_attribute

    def get_character_attribute_points_left(self):
        return self._character.attribute_points_left()

    def get_character_attributes_as_list(self):
        attribute_list = []
        for name, value in self._character.attributes.items():
            attribute_info = f"{name:15}{value}"
            if name == self._character.main_attribute:
                attribute_info += " (Main)"
            attribute_list.append(attribute_info)
        return attribute_list

    def change_character_attribute(self, attribute: str, amount: int) -> int:
        if attribute in self._character.attributes:
            try:
                self._character.change_attribute(attribute, amount)
                return self._character.attributes[attribute]
            except ValueError:
                return self._character.attributes[attribute]
        return -1

    def reset_character_attributes(self):
        self._character.reset_attributes()

    def get_character_skills(self):
        return self._character.skills

    def get_character_main_skill(self):
        return self._character.main_skill

    def get_character_skill_points_left(self):
        return self._character.skill_points_left()

    def get_character_skills_as_list(self):
        skill_list = []
        for name, value in self._character.skills.items():
            skill_info = f"{name:15}{value}"
            if name == self._character.main_skill:
                skill_info += " (Main)"
            skill_list.append(skill_info)
        return skill_list

    def get_character_resources(self):
        return self._character.resources

    def change_character_skill(self, skill: str, amount: int) -> int:
        if skill in self._character.skills:
            try:
                self._character.change_skill(skill, amount)
                return self._character.skills[skill]
            except ValueError:
                return self._character.skills[skill]
        return -1

    def reset_character_skills(self):
        self._character.reset_skills()

    def change_character_resources(self, amount: int) -> int:
        try:
            self._character.change_resources(amount)
            return self._character.resources
        except ValueError:
            return self._character.resources

    def reset_character_resources(self):
        self._character.reset_resources()

    def get_equipment_options(self):
        return self._character.archetype.equipment

    def get_character_equipment(self):
        return self._character.equipment

    def set_character_equipment(self, equipment: list) -> list:
        self._character.equipment = equipment
        return self._character.equipment

    def full_character_sheet(self) -> list:
        character_sheet = []
        first_line = f"{self._character.name}, {self._character.age}"
        first_line += f" ({self._character.age_group(self._character.age)})"
        character_sheet.append(first_line)
        character_sheet.append(self._character.archetype.name)
        character_sheet.append("")

        character_sheet.append("Talents:")
        for talent in self._character.talents:
            character_sheet.append(f"{talent.name}: {talent.description}")
        character_sheet.append("")

        character_sheet.append("Attributes:")
        for attribute in self.get_character_attributes_as_list():
            character_sheet.append(attribute)
        character_sheet.append("")

        character_sheet.append("Skills:")
        for skill in self.get_character_skills_as_list():
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

    def save_character_to_file(self, filename: str):
        with open(filename, "w", encoding="UTF-8") as file:
            for row in self.full_character_sheet():
                file.write(row + "\n")


character_service = CharacterService()

# def character_max_attribute_points(self):
#     return self._character.max_attribute_points

# def character_max_skill_points(self):
#     return self._character.max_skill_points

# def remove_character_talents(self):
#     self._character.remove_talents()
