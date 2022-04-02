from entities.archetype import Archetype
from entities.character import Character

if __name__ == "__main__":
    albert = Character("Albert Brugge", age=(30, "Middle-aged"))
    print(albert)

    albert.set_age(51)
    print(albert)

    talent_list = ["Bookworm", "Erudite", "Knowledge is Reassuring"]
    equipment_list = [("book collection", "map book"), "writing utensils", ("liquor", "slide rule")]
    academic = Archetype("Academic", "logic", "learning", talent_list, (4, 6), equipment_list)
    albert.set_archetype(academic)
    print(albert)
