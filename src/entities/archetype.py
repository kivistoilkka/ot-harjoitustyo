from talent import Talent

class Archetype:
    def __init__(self, name: str, main_attribute: str, main_skill: str, talents: dict, resource_boundaries: tuple, equipment: list):
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

if __name__ == "__main__":
    bookworm = Talent("Bookworm", "Gain +2 to...")
    erudite = Talent("Erudite", "You can pass a...")
    knowledge_is_reassuring = Talent("Knowledge is Reassuring", "Ignore Conditions when...")
    talent_dict = {bookworm.name: bookworm, erudite.name: erudite, knowledge_is_reassuring.name: knowledge_is_reassuring}
    equipment_list = [("book collection", "map book"), "writing utensils", ("liquor", "slide rule")]
    academic = Archetype("Academic", "logic", "learning", talent_dict, (4, 6), equipment_list)
    print(academic)