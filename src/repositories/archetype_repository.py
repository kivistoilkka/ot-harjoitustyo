from pathlib import Path
import json

from entities.archetype import Archetype
from config import ARCHETYPES_FILE_PATH
from repositories.talent_repository import talent_repository


class ArchetypeRepository:
    def __init__(self, file_path):
        self._file_path = file_path

    def find_all(self):
        archetypes = self._read()
        archetypes_dict = {}
        for archetype in archetypes:
            archetypes_dict[archetype.name] = archetype
        return archetypes_dict

    def _read(self) -> list:
        self._ensure_file_exists()
        with open(self._file_path, encoding="UTF-8") as file:
            data = file.read()
        archetype_list = json.loads(data)
        archetypes = []
        for archetype in archetype_list:
            name = archetype["name"]
            main_attribute = archetype["mainAttribute"]
            main_skill = archetype["mainSkill"]
            talents = talent_repository.find_for_archetype(name)
            equipment = []
            for item in archetype["equipment"]:
                if isinstance(item, list):
                    equipment.append((item[0], item[1]))
                else:
                    equipment.append(item)
            resource_boundaries = (
                archetype["resourcesLowerBoundary"],
                archetype["resourcesUpperBoundary"])
            archetype_object = Archetype(
                name, main_attribute, main_skill, talents, resource_boundaries, equipment)
            archetypes.append(archetype_object)
        return archetypes

    def _ensure_file_exists(self):
        file = Path(self._file_path)
        if not file.exists():
            file.write_text("[]", encoding="UTF-8")


archetype_repository = ArchetypeRepository(ARCHETYPES_FILE_PATH)
