from functools import reduce

from entities.archetype import Archetype


class Character:
    """Object for saving the information of the character.


    Attributes:
        _name (str): Name of the character, cannot be an empty string
        _archetype (Archetype): Archetype of the character
        __main_attribute (str): Main character attribute of the character as determined
                                by the archetype
        __main_skill (str): Main skill of the character as determined by the archetype
        _resources (int): Character resources, minimum value and available range is
                                determined by the archetype, skill points can be used
                                to increase the value
        __age (int): Age of the character
        __max_attribute_points (int): Maximum amount of attribute points as determined by the age
        __max_skill_points (int): Maximum amount of skill points as determined by the age
        _talents (list): List of Talent objects, currently character can only have one talent
        _attributes (dict): Dictionary of character attributes, names and default values can be
                                found in class variable default_attributes
        _skills (dict): Dictionary of character skills, names and default values can be
                                found in class variable default_skills
        _equipment (list): List of equipment names as strings
        _description (str): Description of the character
    """

    default_attributes = {
        "Physique": 2,
        "Precision": 2,
        "Logic": 2,
        "Empathy": 2
    }
    default_skills = {
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

    def __init__(self, name: str, archetype: Archetype, age: int):
        self._name = name

        self._archetype = archetype
        self.__main_attribute = self._archetype.main_attribute
        self.__main_skill = self._archetype.main_skill
        self._resources = self._archetype.resource_boundaries[0]

        self.__age = age
        self.__max_attribute_points = None
        self.__max_skill_points = None
        if self.__age:
            self.__set_age_related_modifiers(age)

        self._talents = []
        self._attributes = Character.default_attributes.copy()
        self._skills = Character.default_skills.copy()
        self._equipment = []
        self._description = ""

    def __str__(self) -> str:
        description = f"{self._name}"
        if self.__age is not None:
            description += f", {self.__age} ({self.age_group(self.__age)})"
        if self._archetype:
            description += f", {self._archetype.name}"
            description += f" (main attribute {self.__main_attribute}"
            description += f", main skill {self.__main_skill})"
        return description

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        if name != "":
            self._name = name
        else:
            raise ValueError("Name cannot be an empty string")

    @property
    def archetype(self):
        return self._archetype

    @archetype.setter
    def archetype(self, archetype: Archetype):
        self._archetype = archetype
        self.__main_attribute = archetype.main_attribute
        self.__main_skill = archetype.main_skill
        self._resources = archetype.resource_boundaries[0]
        self._attributes = Character.default_attributes.copy()
        self._skills = Character.default_skills.copy()
        self._resources = self._archetype.resource_boundaries[0]
        self._talents = []
        self._equipment = []

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age: int):
        if age < 17:
            raise ValueError("Age must be 17 or higher")
        self.__age = age
        self.__set_age_related_modifiers(age)
        self._attributes = Character.default_attributes.copy()
        self._skills = Character.default_skills.copy()
        self._resources = self._archetype.resource_boundaries[0]

    @property
    def max_attribute_points(self):
        return self.__max_attribute_points

    @property
    def max_skill_points(self):
        return self.__max_skill_points

    def age_group(self, age: int) -> str:
        if age < 17:
            raise ValueError("Age must be 17 or higher")
        if age < 26:
            return "Young"
        if age < 51:
            return "Middle aged"
        return "Old"

    def __set_age_related_modifiers(self, age: int):
        if age < 17:
            raise ValueError("Age must be 17 or higher")
        if age < 26:
            self.__max_attribute_points = 15
            self.__max_skill_points = 10
        elif age < 51:
            self.__max_attribute_points = 14
            self.__max_skill_points = 12
        else:
            self.__max_attribute_points = 13
            self.__max_skill_points = 14

    @property
    def talents(self) -> list:
        return self._talents

    @talents.setter
    def talents(self, new_talents: list):
        self._talents = new_talents

    def attribute_points_left(self) -> int:
        used_points = reduce(lambda total, attribute: total +
                             attribute, self._attributes.values(), 0)
        return self.__max_attribute_points - used_points

    def skill_points_left(self) -> int:
        points_used_to_resources = self._resources - \
            self._archetype.resource_boundaries[0]
        points_used_to_skills = reduce(
            lambda total, skill: total + skill, self._skills.values(), 0)
        return self.__max_skill_points - points_used_to_skills - points_used_to_resources

    @property
    def resources(self):
        return self._resources

    @resources.setter
    def resources(self, new_resources: int):
        self._resources = new_resources

    def change_resources(self, amount: int):
        if not self._archetype:
            raise ValueError("Choose archetype before changing resources")
        if not self.__age:
            raise ValueError("Set age before changing resources")
        if amount > self.skill_points_left():
            raise ValueError("Not enough skill points left")
        new_resources = self._resources + amount
        boundaries = self._archetype.resource_boundaries
        if new_resources < boundaries[0] or new_resources > boundaries[1]:
            error_message = "Chosen archetype allows starting resources between "
            error_message += f"{boundaries[0]} - {boundaries[1]}"
            raise ValueError(error_message)
        self._resources = new_resources

    @property
    def attributes(self):
        return self._attributes

    @attributes.setter
    def attributes(self, new_attributes: dict):
        self._attributes = new_attributes

    @property
    def main_attribute(self):
        return self.__main_attribute

    def change_attribute(self, attribute: str, amount: int):
        if not self.__age:
            raise ValueError("Set age before changing attributes")
        if not self._archetype:
            raise ValueError("Choose archetype before changing attributes")
        if amount > self.attribute_points_left():
            raise ValueError("Not enough attribute points left")
        if attribute not in self._attributes:
            raise ValueError("Given attribute does not exist")

        new_value = self._attributes[attribute] + amount
        if 2 <= new_value <= 4 or (new_value == 5 and attribute == self.__main_attribute):
            self._attributes[attribute] = new_value
        else:
            raise ValueError("Given value is not allowed")

    @property
    def skills(self):
        return self._skills

    @skills.setter
    def skills(self, new_skills: dict):
        self._skills = new_skills

    @property
    def main_skill(self):
        return self.__main_skill

    def change_skill(self, skill: str, amount: int):
        if not self.__age:
            raise ValueError("Set age before changing skills")
        if not self._archetype:
            raise ValueError("Choose archetype before changing skills")
        if amount > self.skill_points_left():
            raise ValueError("Not enough skill points left")
        if skill not in self._skills:
            raise ValueError("Given skill does not exist")

        new_value = self._skills[skill] + amount
        if 0 <= new_value <= 2 or (new_value == 3 and skill == self.__main_skill):
            self._skills[skill] = new_value
        else:
            raise ValueError("Given value is not allowed")

    @property
    def equipment(self):
        return self._equipment

    @equipment.setter
    def equipment(self, equipment: list):
        self._equipment = equipment

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, text: str):
        self._description = text
