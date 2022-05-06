from entities.character import Character
from entities.archetype import Archetype

from repositories.archetype_repository import archetype_repository
from repositories.character_repository import character_repository

AVAILABLE_ARCHETYPES = archetype_repository.find_all()


class CharacterService:
    """Class responsible for creation and modification of the character

    Attributes:
        _repository (CharacterRepository): Repository for character files
        _character (Character): Character object
    """

    def __init__(
            self,
            repository,
            character: Character = None):
        """Constructor which can take an existing Character object as a parameter.

        Args:
            repository (CharacterRepository): Repository for character files
            character (Character, optional): Character to be modified. Defaults to None.
        """

        self._repository = repository
        self._character = character

    def create_character(self, name: str, archetype: Archetype, age: int):
        """Creates new character to be modified.

        Args:
            name (str): Name of the character
            archetype (Archetype): Archetype of the character as a Archetype object
            age (int): Age of the character (>= 17)
        """

        if name == "":
            raise ValueError("Name cannot be an empty string")
        if archetype not in AVAILABLE_ARCHETYPES:
            raise ValueError("Given archetype is not available")
        if not isinstance(age, int):
            raise ValueError("Give the age value as an integer")
        if age < 17:
            raise ValueError("Character age must be over 17")
        self._character = Character(name, AVAILABLE_ARCHETYPES[archetype], age)

    def get_character_summary(self) -> str:
        """Returns summary of the character

        Returns:
            str: String with character name, age, age group and archetype
        """

        if self._character:
            return str(self._character)
        raise ValueError(
            "Character has to be created before it can be summarized")

    def get_character_name(self) -> str:
        """Returns the name of the character

        Returns:
            str: Name of the character
        """

        if self._character:
            return self._character.name
        raise ValueError(
            "Character has to be created before it can have a name")

    def set_character_name(self, name: str):
        """Sets new name for the character

        Args:
            name (str): New name as a string (empty string is not allowed)
        """

        if self._character:
            if name != "":
                self._character.name = name
            else:
                raise ValueError("Name cannot be an empty string")
        else:
            raise ValueError(
                "Character has to be created before it can be renamed")

    def get_character_archetype_name(self) -> str:
        """Returns the name of the archetype of the character

        Returns:
            str: Name of the archetype
        """

        if self._character:
            return self._character.archetype.name
        raise ValueError(
            "Character has to be created before it can have an archetype")

    def set_character_archetype(self, name: str):
        """Sets an archetype for the character from the options available (list available with
        method .get_archetype_options()).

        Args:
            name (str): Name of the new archetype
        """

        if self._character:
            if name in AVAILABLE_ARCHETYPES:
                self._character.archetype = AVAILABLE_ARCHETYPES[name]
            else:
                raise ValueError("Given archetype is not available")
        else:
            raise ValueError(
                "Character has to be created before the archetype can be changed")

    def get_character_age(self) -> int:
        """Returns the age of the character

        Returns:
            int: Age of the character
        """
        if self._character:
            return self._character.age
        raise ValueError(
            "Character has to be created before it can have an age")

    def set_character_age(self, age: int):
        """Sets new age for the character

        Args:
            age (int): New age (>= 17)
        """

        if self._character:
            if isinstance(age, int) and age >= 17:
                self._character.age = age
            else:
                raise ValueError(
                    "Give the value as an integer, which is 17 or more")
        else:
            raise ValueError(
                "Character has to be created before the age can be changed")

    def get_character_agegroup(self, age: int = None) -> str:
        """Returns the age group of the character if no age parameter is provided, otherwise
        returns the age group of the age provided as a parameter.

        Args:
            age (int, optional): Age of which the age group will be returned. Defaults to None.

        Returns:
            str: Age group of the character if no age parameter is given, otherwise the age group
            to which the provided age belongs to.
        """

        if self._character:
            if not age:
                age = self._character.age
            return self._character.age_group(age)
        dummy = Character("Dummy", Archetype(
            "Tester", "Logic", "Testing", {}, (0, 1), []), 100)
        if not age or not isinstance(age, int):
            raise ValueError(
                "Character not created, give an age value in integer")
        return dummy.age_group(age)

    def get_archetype_options(self) -> list:
        """Returns list of available archetype options for character creation.

        Returns:
            list: List of archetype names as strings
        """

        return list(AVAILABLE_ARCHETYPES.keys())

    def get_character_talents(self) -> list:
        """Returns list of character talents.

        Returns:
            list: List of Talent objects, None if character has no talents
        """

        if self._character:
            if len(self._character.talents) == 0:
                return None
            return self._character.talents
        raise ValueError(
            "Character has to be created before it can have talents")

    def get_talent_options(self) -> dict:
        """Returns dictionary of available talent options for the archetype the character has.

        Returns:
            dict: Dictionary with talent names as keys and Talent objects as values.
        """

        if self._character:
            return self._character.archetype.talents
        raise ValueError(
            "Character has to be created before talent options can be returned")

    def give_talent_to_character(self, name: str):
        """Gives the character a new talent. Current version removes previous talents from the
        character before giving it a new one.

        Args:
            name (str): Name of the talent from the list of names available for the archetype
            of the character (available with method .get_talent_options())
        """

        if self._character:
            if name in self._character.archetype.talents:
                self._character.talents = [
                    self._character.archetype.talents[name]]
                return
            raise ValueError("Talent not available for the current archetype")
        raise ValueError(
            "Character has to be created before talents can be given")

    def get_character_attributes(self) -> dict:
        """Returns character attributes (Physique, Precision, Logic and Empathy).

        Returns:
            dict: Dictionary with character attribute names as keys and attribute values as
            values (2-5 for the main attribute, 2-4 for the rest)
        """

        if self._character:
            return self._character.attributes
        raise ValueError(
            "Character has to be created before attributes can be returned")

    def get_character_main_attribute(self) -> str:
        """Returns main attribute of the character as determined by the character archetype

        Returns:
            str: Name of the main character attribute of the character
        """

        return self._character.main_attribute

    def get_character_attribute_points_left(self) -> int:
        """Returns amount of unused attribute points of the character

        Returns:
            int: Remaining unused attribute points
        """

        return self._character.attribute_points_left()

    def change_character_attribute(self, attribute: str, amount: int) -> int:
        """Changes the value of a character attribute by the amount provided and returns the new
        value. The range of attribute values are 2-5 for the main attribute, 2-4 for the rest.

        Args:
            attribute (str): Name of the attribute (Physique, Precision, Logic or Empathy)
            amount (int): Amount to be changed as a positive or negative integer.

        Returns:
            int: The new value of the modified attribute
        """

        if attribute in self._character.attributes:
            try:
                self._character.change_attribute(attribute, amount)
                return self._character.attributes[attribute]
            except ValueError:
                return self._character.attributes[attribute]
        else:
            raise ValueError("The name of the attribute is incorrect")

    def reset_character_attributes(self):
        """Resets the character attributes to default values (2 in each)
        """

        self._character.attributes = Character.default_attributes.copy()

    def get_character_skills(self) -> dict:
        """Returns character skills.

        Returns:
            dict: Dictionary with character skill names as keys and skill values as
            values (0-3 for main skill, 0-2 for the rest)
        """

        return self._character.skills

    def get_character_main_skill(self) -> str:
        """Returns main skill of the character as determined by the character archetype.

        Returns:
            str: Name of the main skill of the character
        """
        return self._character.main_skill

    def get_character_skill_points_left(self) -> int:
        """Returns amount of unused skill points of the character.

        Returns:
            int: Remaining unused skill points
        """

        return self._character.skill_points_left()

    def change_character_skill(self, skill: str, amount: int) -> int:
        """Changes the value of a skill by the amount provided and returns the new value.
        The range of skill values are 0-3 for the main skill, 0-2 for the rest.

        Args:
            skill (str): Name of the skill
            amount (int): Amount to be changed as a positive or negative integer.

        Returns:
            int: The new value of the modified skill
        """

        if skill in self._character.skills:
            try:
                self._character.change_skill(skill, amount)
                return self._character.skills[skill]
            except ValueError:
                return self._character.skills[skill]
        else:
            raise ValueError("The name of the skill is incorrect")

    def reset_character_skills(self):
        """Resets the character skills to default values (0 in each)
        """

        self._character.skills = Character.default_skills.copy()

    def get_character_resources(self) -> int:
        """Returns the resource value assigned to character. Minimum value is determined by the
        character archetype and skill points can be used to increase it up to the maximum value
        determined by the archetype.

        Returns:
            int: Resource value of the character
        """

        return self._character.resources

    def change_character_resources(self, amount: int) -> int:
        """Changes the value of character resources by the amount provided and returns the
        new value. The minimum and maximum values are determined by the archetype of the
        character.

        Args:
            amount (int): Amount to be changed as a positive or negative integer.

        Returns:
            int: The new value of the resources
        """

        try:
            self._character.change_resources(amount)
            return self._character.resources
        except ValueError:
            return self._character.resources

    def reset_character_resources(self):
        """Resets the character resources to minimum value determined by the character archetype.
        """

        self._character.resources = self._character.archetype.resource_boundaries[0]

    def get_equipment_options(self) -> list:
        """Returns list of available equipment options for the archetype of the character.

        Returns:
            list: List of strings (name of mandatory equipment) and tuples of strings (names of
            two mutually exclusive equipment options)
        """

        return self._character.archetype.equipment

    def get_character_equipment(self) -> list:
        """Returns list equipment chosen for the character.

        Returns:
            list: Name of chosen equipments as a string
        """

        return self._character.equipment

    def set_character_equipment(self, equipment: list) -> list:
        """Sets the equipment list of the character and returns it.

        Args:
            equipment (list): List of equipment names

        Returns:
            list: List of equipment names
        """

        self._character.equipment = equipment
        return self._character.equipment

    def get_character_description(self) -> str:
        """Returns freeform description of the character

        Returns:
            str: Saved character description
        """
        return self._character.description

    def change_character_description(self, text: str) -> str:
        """Changes freeform description of the character

        Args:
            text (str): New character description

        Returns:
            str: Saved character description
        """
        self._character.description = text
        return self._character.description

    def export_character_to_file(self, filename: str):
        """Calls CharacterRepository object to export current character as a character sheet
        to a text file.

        Args:
            filename (str): Name of the file to which the character sheet will be saved.
        """

        self._repository.export_character_sheet(self._character, filename)

    def save_character_to_file(self, filename: str):
        """Calls CharacterRepository object to save current character to a JSON file.

        Args:
            filename (str): Name of the file to which the character will be saved.
        """

        self._repository.save_character(self._character, filename)

    def load_character_from_file(self, filename: str):
        """Calls CharacterRepository object to load a character from a JSON file and sets it
        as a character to be modified.

        Args:
            filename (str): Name of the file from which the character will be loaded.
        """

        self._character = self._repository.open_character(filename)


character_service = CharacterService(character_repository)
