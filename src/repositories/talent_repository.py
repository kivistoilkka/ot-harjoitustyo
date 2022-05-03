from pathlib import Path
import json

from entities.talent import Talent
from config import TALENTS_FILE_PATH


class TalentRepository:
    """Class responsible for loading Talent objects from JSON-file

    Attributes:
        _file_path (str): File path to the location of talents json-file
    """

    def __init__(self, file_path):
        self._file_path = file_path

    def find_all(self) -> list:
        """Returns talents from the file containing all available talents

        Returns:
            list: List of Talent objects
        """

        self._ensure_file_exists()
        with open(self._file_path, encoding="UTF-8") as file:
            data = file.read()
        talents_list = json.loads(data)
        talents = []
        for talent in talents_list:
            talent_object = Talent(
                talent["name"], talent["description"], talent["startingOptionFor"])
            talents.append(talent_object)
        return talents

    def find_for_archetype(self, archetype: str) -> dict:
        """Returns a dictionary of available talents for certain archetype

        Args:
            archetype (str): Name of the archetype

        Returns:
            dict: Dictionary with talent names as keys and Talent objects as values
        """
        talents = list(
            filter(lambda talent: talent.starting_option_for == archetype, self.find_all()))
        talents_dict = {}
        for talent in talents:
            talents_dict[talent.name] = talent
        return talents_dict

    def _ensure_file_exists(self):
        file = Path(self._file_path)
        if not file.exists():
            file.write_text("[]", encoding="UTF-8")


talent_repository = TalentRepository(TALENTS_FILE_PATH)
