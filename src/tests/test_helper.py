from entities.talent import Talent
from entities.archetype import Archetype


class TestHelper:
    def __dict_of_academic_talents():
        bookworm = Talent("Bookworm", "Gain +2 to...")
        erudite = Talent("Erudite", "You can pass a...")
        knowledge_is_reassuring = Talent(
            "Knowledge is Reassuring", "Ignore Conditions when...")
        return {bookworm.name: bookworm, erudite.name: erudite, knowledge_is_reassuring.name: knowledge_is_reassuring}

    def default_character_attributes():
        return {
            "Physique": 2,
            "Precision": 2,
            "Logic": 2,
            "Empathy": 2
        }

    def default_character_skills():
        return {
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

    def dict_of_archetypes(self):
        talent_dict = self.__dict_of_academic_talents()
        equipment_list = [("book collection", "map book"),
                          "writing utensils", ("liquor", "slide rule")]
        academic = Archetype("Academic", "Logic", "Learning",
                             talent_dict, (4, 6), equipment_list)
        return {academic.name: academic}
