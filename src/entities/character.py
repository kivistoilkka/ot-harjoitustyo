from functools import reduce

from archetype import Archetype
from talent import Talent

class Character:
    def __init__(self, name: str, archetype: Archetype = None, age: int = None):
        self._name = name

        self._archetype = archetype
        self.__main_attribute = None if not self._archetype else self._archetype.main_attribute
        self.__main_skill = None if not self._archetype else self._archetype.main_skill

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
        self._resources = None
    
    def __str__(self) -> str:
        description = f"{self._name}"
        if self._age != (None, None):
            description += f", {self._age} ({self.age_group(self._age)})"
        if self._archetype:
            description += f", {self._archetype.name}"
            description += f" (main attribute {self.__main_attribute}"
            description += f", main skill {self.__main_skill})"
        return description
    
    def set_name(self, name: str):
        self._name = name
    
    def set_archetype(self, archetype: Archetype):
        self._archetype = archetype
        self.__main_attribute = archetype.main_attribute
        self.__main_skill = archetype.main_skill
    
    def set_age(self, age: int):
        if age < 17:
            raise ValueError("Age must be 17 or higher")
        self._age = age
        self.__set_age_related_modifiers(age)
    
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
            raise AttributeError("Choose archetype before setting talents")
        if len(self._talents) == 0:
            for option in self._archetype.talents:
                if option.name == name:
                    self._talents.append(option)
                    return True
        return False
    
    def remove_talents(self):
        self._talents = []
    
    def get_attributes(self):
        attribute_list = []
        for name, value in self._attributes.items():
            attribute_info = f"{name:10}{value}"
            if name == self.__main_attribute:
                attribute_info += " (Main)"
            attribute_list.append(attribute_info)
        return attribute_list
    
    def get_skills(self):
        skill_list = []
        for name, value in self._skills.items():
            skill_info = f"{name:15}{value}"
            if name == self.__main_skill:
                skill_info += " (Main)"
            skill_list.append(skill_info)
        return skill_list
    
    def attribute_points_left(self):
        return self.__max_attribute_points - reduce(lambda total, attribute: total + attribute, self._attributes.values(), 0)

    def skill_points_left(self):
        return self.__max_skill_points - reduce(lambda total, skill: total + skill, self._skills.values(), 0)

if __name__ == "__main__":
    albert = Character("Albert Brugge", age=30)
    albert.set_age(51)
    bookworm = Talent("Bookworm", "Gain +2 to...")
    erudite = Talent("Erudite", "You can pass a...")
    knowledge_is_reassuring = Talent("Knowledge is Reassuring", "Ignore Conditions when...")
    talent_list = [bookworm, erudite, knowledge_is_reassuring]
    equipment_list = [("book collection", "map book"), "writing utensils", ("liquor", "slide rule")]
    academic = Archetype("Academic", "Logic", "Learning", talent_list, (4, 6), equipment_list)
    albert.set_archetype(academic)
    print()
    
    print(albert)
    print()

    albert.give_talent("Bookworm")
    print("Talents:")
    for talent in albert.get_talents():
        print(talent)
    print()
    
    print("Attributes:")
    for attribute in albert.get_attributes():
        print(attribute)
    print()

    print("Skills:")
    for skill in albert.get_skills():
        print(skill)
    print()
    
    print("Attribute points left: ", end="")
    print(albert.attribute_points_left())

    print("Skill/resource points left: ", end="")
    print(albert.skill_points_left())