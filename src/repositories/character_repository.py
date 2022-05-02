import json

from entities.character import Character
from repositories.archetype_repository import archetype_repository

AVAILABLE_ARCHETYPES = archetype_repository.find_all()

class CharacterRepository:
    def __init__(self):
        pass

    def _attributes_as_list(self, character: Character) -> list:
        attribute_list = []
        for name, value in character.attributes.items():
            attribute_info = f"{name:15}{value}"
            if name == character.main_attribute:
                attribute_info += " (Main)"
            attribute_list.append(attribute_info)
        return attribute_list

    def _skills_as_list(self, character: Character) -> list:
        skill_list = []
        for name, value in character.skills.items():
            skill_info = f"{name:15}{value}"
            if name == character.main_skill:
                skill_info += " (Main)"
            skill_list.append(skill_info)
        return skill_list

    def _character_sheet_as_list(self, character: Character) -> list:
        character_sheet = []
        first_line = f"{character.name}, {character.age}"
        first_line += f" ({character.age_group(character.age)})"
        character_sheet.append(first_line)
        character_sheet.append(character.archetype.name)
        character_sheet.append("")

        character_sheet.append("Talents:")
        for talent in character.talents:
            character_sheet.append(f"{talent.name}: {talent.description}")
        character_sheet.append("")

        character_sheet.append("Attributes:")
        for attribute in self._attributes_as_list(character):
            character_sheet.append(attribute)
        character_sheet.append("")

        character_sheet.append("Skills:")
        for skill in self._skills_as_list(character):
            character_sheet.append(skill)
        character_sheet.append("")

        character_sheet.append("Equipment:")
        for item in character.equipment:
            character_sheet.append(f"- {item}")
        character_sheet.append("")

        character_sheet.append(
            f"Attribute points left: {character.attribute_points_left()}")
        character_sheet.append(
            f"Skill/resource points left: {character.skill_points_left()}")
        character_sheet.append("")

        character_sheet.append(f"Resources: {character.resources}")

        return character_sheet

    def _check_character_legality(self) -> bool:
        pass

    def export_character_sheet(self, character: Character, filename: str) -> bool:
        try:
            with open(filename, "w", encoding="UTF-8") as file:
                for row in self._character_sheet_as_list(character):
                    file.write(row + "\n")
            return True
        except OSError:
            return False

    def save_character(self, character: Character, filename: str) -> bool:
        character_to_save = {
            "name": character.name,
            "archetype": character.archetype.name,
            "age": character.age,
            "talents": [talent.name for talent in character.talents],
            "attributes": character.attributes,
            "skills": character.skills,
            "equipment": character.equipment,
            "resources": character.resources
        }

        try:
            with open(filename, "w", encoding="UTF-8") as file:
                file.write(json.dumps(character_to_save))
            return True
        except OSError:
            return False

    def open_character(self, filename: str) -> Character:
        try:
            with open(filename, encoding="UTF-8") as file:
                data = file.read()
            character_data = json.loads(data)
            character = Character(
                character_data["name"],
                AVAILABLE_ARCHETYPES[character_data["archetype"]],
                character_data["age"]
            )
            character.talents = character_data["talents"]
            #TODO: Check talent legality
            character.attributes = character_data["attributes"]
            #TODO: Check attribute legality, method for this
            character.skills = character_data["skills"]
            #TODO: Check skill legality, method for this
            character.equipment = character_data["equipment"]
            #TODO: Check equipment legality, method for this
            character.resources = character_data["resources"]
            #TODO: Check resource legality, method for this
            return character
        except OSError:
            return False

character_repository = CharacterRepository()