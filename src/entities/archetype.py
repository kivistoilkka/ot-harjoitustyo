class Archetype:
    def __init__(self, name: str, main_attribute: str, main_skill: str, talents: list, resource_boundaries: tuple, equipment: list):
        self.__name = name
        self.__main_attribute = main_attribute
        self.__main_skill = main_skill
        self.__talents = talents
        self.__resource_boundaries = resource_boundaries
        self.__equipment = equipment

    def __str__(self) -> str:
        return f"{self.__name}, {self.__main_attribute}, {self.__main_skill}, {self.__talents}, resources {self.__resource_boundaries[0]}-{self.__resource_boundaries[1]}, {self.__equipment}"

    @property
    def name(self):
        return self.__name

if __name__ == "__main__":
    talent_list = ["Bookworm", "Erudite", "Knowledge is Reassuring"]
    equipment_list = [("book collection", "map book"), "writing utensils", ("liquor", "slide rule")]
    academic = Archetype("Academic", "logic", "learning", talent_list, (4, 6), equipment_list)
    print(academic)