from entities.archetype import Archetype
from entities.character import Character
from entities.talent import Talent

bookworm = Talent("Bookworm", "Gain +2 to...")
erudite = Talent("Erudite", "You can pass a...")
knowledge_is_reassuring = Talent("Knowledge is Reassuring", "Ignore Conditions when...")
talent_dict = {bookworm.name: bookworm, erudite.name: erudite, knowledge_is_reassuring.name: knowledge_is_reassuring}
equipment_list = [("book collection", "map book"), "writing utensils", ("liquor", "slide rule")]
academic = Archetype("Academic", "Logic", "Learning", talent_dict, (4, 6), equipment_list)
AVAILABLE_ARCHETYPES = {academic.name: academic}

def main():
    print()
    print("Character generator for Vaesen: Nordic Horror Roleplaying game")
    print()

    character_name = input("Name your character: ")
    character = Character(character_name)

    while True:
        print()
        print("Archetype options:")
        for archetype in AVAILABLE_ARCHETYPES:
            print("-", archetype)
        name = input("Choose the archetype: ")
        if name in AVAILABLE_ARCHETYPES:
            character.set_archetype(AVAILABLE_ARCHETYPES[name])
            break
    
    while True:
        print()
        age = int(input("Age of the character (>17): "))
        if age > 17:
            character.set_age(age)
            break
    
    while True:
        print()
        print("Talent options:")
        for talent in character.archetype.talents:
            print("-", talent)
        name = input("Choose starting talent: ")
        if name in character.archetype.talents:
            character.give_talent(name)
            break

    command = input("Do you want to see the character sheet (yes/no)? ")
    if command == "yes":
        print()
        print("-------------------------------------")
        for line in character.full_character_sheet():
            print(line)
        print("-------------------------------------")

if __name__ == "__main__":
    main()
