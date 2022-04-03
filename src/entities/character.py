from functools import reduce

from archetype import Archetype
from talent import Talent

class Character:
    def __init__(self, name: str, archetype: Archetype = None, age: int = None):
        self._name = name

        self._archetype = archetype
        self.__main_attribute = None if not self._archetype else self._archetype.main_attribute
        self.__main_skill = None if not self._archetype else self._archetype.main_skill
        self._resources = None if not self._archetype else self._archetype.resource_boundaries[0]

        self._age = age
        self.__max_attribute_points = None
        self.__max_skill_points = None
        if self._age:
            self.__set_age_related_modifiers(age)

        self._talents = []
        self._attributes = {
            "Physique": 2,
            "Precision": 2,
            "Logic": 2,
            "Empathy": 2
        }
        self._skills = {
            "Agility": 0,
            "Close combat": 0,
            "Force": 0,
            "Medicine": 0,
            "Ranged combat": 0,
            "Stealth": 0,
            "Investigation": 0,
            "Learning": 0,
            "Vigilance": 0,
            "Inspiration": 0,
            "Manipulation": 0,
            "Observation": 0
        }
    
    def __str__(self) -> str:
        description = f"{self._name}"
        if self._age != (None, None):
            description += f", {self._age} ({self.age_group(self._age)})"
        if self._archetype:
            description += f", {self._archetype.name}"
            description += f" (main attribute {self.__main_attribute}"
            description += f", main skill {self.__main_skill})"
        return description
    
    def full_character_sheet(self) -> list:
        character_sheet = []
        character_sheet.append(f"{self._name}, {self._age} ({self.age_group(self._age)})")
        character_sheet.append(self._archetype.name)
        character_sheet.append("")
        
        character_sheet.append("Talents:")
        for talent in self._talents:
            character_sheet.append(talent)
        character_sheet.append("")
        
        character_sheet.append("Attributes:")
        for attribute in self.get_attributes_as_list():
            character_sheet.append(attribute)
        character_sheet.append("")

        character_sheet.append("Skills:")
        for skill in self.get_skills_as_list():
            character_sheet.append(skill)
        character_sheet.append("")
        
        character_sheet.append(f"Attribute points left: {self.attribute_points_left()}")
        character_sheet.append(f"Skill/resource points left: {self.skill_points_left()}")
        character_sheet.append("")

        character_sheet.append(f"Resources: {self._resources}")

        return character_sheet
    
    def set_name(self, name: str):
        self._name = name
    
    def set_archetype(self, archetype: Archetype):
        self._archetype = archetype
        self.__main_attribute = archetype.main_attribute
        self.__main_skill = archetype.main_skill
        self._resources = archetype.resource_boundaries[0]
        self.reset_attributes()
        self.reset_skills()
        self.reset_resources()
    
    def set_age(self, age: int):
        if age < 17:
            raise ValueError("Age must be 17 or higher")
        self._age = age
        self.__set_age_related_modifiers(age)
        self.reset_attributes()
        self.reset_skills()
        self.reset_resources()
    
    def age_group(self, age: int):
        if age < 17:
            raise ValueError("Age must be 17 or higher")
        if age < 26:
            return "Young"
        if age < 51:
            return "Middle aged"
        else:
            return "Old"
    
    def __set_age_related_modifiers(self, age: int):
        if age < 17:
            raise ValueError("Age must be 17 or higher")
        if age < 26:
            self.__max_attribute_points = 15
            self.__max_skill_points = 10
        if age < 51:
            self.__max_attribute_points = 14
            self.__max_skill_points = 12
        else:
            self.__max_attribute_points = 13
            self.__max_skill_points = 14
    
    def get_talents(self):
        return self._talents
    
    def give_talent(self, name: str):
        if not self._archetype:
            raise AttributeError("Choose archetype before giving talent")
        if name not in self._archetype.talents:
            raise ValueError("Talent not available for the current archetype")
        self.remove_talents()
        self._talents.append(self._archetype.talents[name])
    
    def remove_talents(self):
        self._talents = []
    
    def get_attributes_as_list(self):
        attribute_list = []
        for name, value in self._attributes.items():
            attribute_info = f"{name:15}{value}"
            if name == self.__main_attribute:
                attribute_info += " (Main)"
            attribute_list.append(attribute_info)
        return attribute_list
    
    def get_skills_as_list(self):
        skill_list = []
        for name, value in self._skills.items():
            skill_info = f"{name:15}{value}"
            if name == self.__main_skill:
                skill_info += " (Main)"
            skill_list.append(skill_info)
        return skill_list
    
    def attribute_points_left(self):
        used_points = reduce(lambda total, attribute: total + attribute, self._attributes.values(), 0)
        return self.__max_attribute_points - used_points

    def skill_points_left(self):
        points_used_to_resources = self._resources - self._archetype.resource_boundaries[0]
        points_used_to_skills = reduce(lambda total, skill: total + skill, self._skills.values(), 0)
        return self.__max_skill_points - points_used_to_skills - points_used_to_resources
    
    def get_resources(self):
        return self._resources
    
    def change_resources(self, amount: int):
        if not self._archetype:
            raise AttributeError("Choose archetype before changing resources")
        if not self._age:
            raise AttributeError("Set age before changing resources")
        if amount > self.skill_points_left():
            raise ValueError("Not enough skill points left")
        new_resources = self._resources + amount
        boundaries = self._archetype.resource_boundaries
        if new_resources < boundaries[0] or new_resources > boundaries[1] :
            error_message = f"Chosen archetype allows starting resources between "
            error_message += f"{boundaries[0]} - {boundaries[1]}"
            raise ValueError(error_message)
        self._resources = new_resources
    
    def reset_resources(self):
        self._resources = None if not self._archetype else self._archetype.resource_boundaries[0]
    
    def change_attribute(self, attribute: str, amount: int):
        if not self._age:
            raise AttributeError("Set age before changing attributes")
        if not self._archetype:
            raise AttributeError("Choose archetype before changing attributes")
        if amount > self.attribute_points_left():
            raise ValueError("Not enough attribute points left")
        if attribute not in self._attributes:
            raise ValueError("Given attribute does not exist")
        
        new_value = self._attributes[attribute] + amount
        if 2 <= new_value <= 4 or (new_value == 5 and attribute == self.__main_attribute):
            self._attributes[attribute] = new_value
        else:
            raise ValueError("Given value is not allowed")
    
    def reset_attributes(self):
        for name in self._attributes:
            self._attributes[name] = 2
    
    def change_skill(self, skill: str, amount: int):
        if not self._age:
            raise AttributeError("Set age before changing skills")
        if not self._archetype:
            raise AttributeError("Choose archetype before changing skills")
        if amount > self.skill_points_left():
            raise ValueError("Not enough skill points left")
        if skill not in self._skills:
            raise ValueError("Given skill does not exist")
        
        new_value = self._skills[skill] + amount
        if 0 <= new_value <= 2 or (new_value == 3 and skill == self.__main_skill):
            self._skills[skill] = new_value
        else:
            raise ValueError("Given value is not allowed")
    
    def reset_skills(self):
        for name in self._skills:
            self._skills[name] = 0


if __name__ == "__main__":
    albert = Character("Albert Brugge", age=30)
    albert.set_age(51)

    bookworm = Talent("Bookworm", "Gain +2 to...")
    erudite = Talent("Erudite", "You can pass a...")
    knowledge_is_reassuring = Talent("Knowledge is Reassuring", "Ignore Conditions when...")
    talent_dict = {bookworm.name: bookworm, erudite.name: erudite, knowledge_is_reassuring.name: knowledge_is_reassuring}
    equipment_list = [("book collection", "map book"), "writing utensils", ("liquor", "slide rule")]
    academic = Archetype("Academic", "Logic", "Learning", talent_dict, (4, 6), equipment_list)

    albert.set_archetype(academic)
    albert.give_talent("Bookworm")
    albert.give_talent("Erudite")
    
    print(albert)
    print()

    albert.change_resources(2)
    albert.change_resources(-2)
    albert.change_resources(1)
    #albert.reset_resources()

    albert.change_attribute("Logic", 2)
    albert.change_attribute("Logic", -2)
    albert.change_attribute("Logic", 3)
    albert.change_attribute("Physique", 1)
    albert.change_attribute("Empathy", 1)
    albert.change_attribute("Physique", -1)
    albert.change_attribute("Precision", 1)
    #albert.reset_attributes()

    albert.change_skill("Learning", 3)
    albert.change_skill("Learning", -3)
    albert.change_skill("Learning", 3)
    albert.change_skill("Vigilance", 2)
    albert.change_skill("Medicine", 2)
    albert.change_skill("Ranged combat", 1)
    albert.change_skill("Stealth", 1)
    albert.change_skill("Investigation", 2)
    albert.change_skill("Inspiration", 1)
    #albert.change_skill("Manipulation", 1)
    albert.change_skill("Observation", 1)
    #albert.reset_skills()

    for line in albert.full_character_sheet():
        print(line)