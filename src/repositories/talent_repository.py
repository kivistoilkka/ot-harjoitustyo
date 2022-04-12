from pathlib import Path
import json

from entities.talent import Talent
from config import TALENTS_FILE_PATH


class TalentRepository:
    def __init__(self, file_path):
        self._file_path = file_path

    def find_all(self):
        return self._read()

    def find_for_archetype(self, archetype: str) -> dict:
        talents = list(
            filter(lambda talent: talent.starting_option_for == archetype, self.find_all()))
        talents_dict = {}
        for talent in talents:
            talents_dict[talent.name] = talent
        return talents_dict

    def _read(self) -> list:
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

    def _ensure_file_exists(self):
        file = Path(self._file_path)
        if not file.exists():
            file.write_text("[]", encoding="UTF-8")


talent_repository = TalentRepository(TALENTS_FILE_PATH)
