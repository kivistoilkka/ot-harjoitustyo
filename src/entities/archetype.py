class Archetype:
    def __init__(
            self, name: str,
            main_attribute: str,
            main_skill: str,
            talents: dict,
            resource_boundaries: tuple,
            equipment: list
        ):
        self.__name = name
        self.__main_attribute = main_attribute
        self.__main_skill = main_skill
        self.__talents = talents
        self.__resource_boundaries = resource_boundaries
        self.__equipment = equipment

    def __str__(self) -> str:
        description = f"{self.__name}, {self.__main_attribute}, {self.__main_skill}, "
        description += f"{self.__talents}, resources {self.__resource_boundaries[0]}-"
        description += f"{self.__resource_boundaries[1]}, {self.__equipment}"
        return description

    @property
    def name(self):
        return self.__name

    @property
    def main_attribute(self):
        return self.__main_attribute

    @property
    def main_skill(self):
        return self.__main_skill

    @property
    def talents(self):
        return self.__talents

    @property
    def resource_boundaries(self):
        return self.__resource_boundaries

    @property
    def equipment(self):
        return self.__equipment
