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
    #character_name = "Astrid Gregorius"
    character = Character(character_name)

    while True:
        print()
        print("Archetype options:")
        for archetype in AVAILABLE_ARCHETYPES:
            print("-", archetype)
        name = input("Choose the archetype: ")
        #name = "Academic"
        if name in AVAILABLE_ARCHETYPES:
            character.set_archetype(AVAILABLE_ARCHETYPES[name])
            break
    
    while True:
        print()
        age = int(input("Age of the character (>17): "))
        #age = 55
        if age > 17:
            character.set_age(age)
            break
    
    while True:
        print()
        print("Talent options:")
        for talent in character.archetype.talents:
            print("-", talent)
        name = input("Choose starting talent: ")
        #name = "Erudite"
        if name in character.archetype.talents:
            character.give_talent(name)
            break
    
    print()
    print("Add points to attributes")
    while True:
        print()
        print("1 - show attributes, 2 - add point, 3 - remove point, 4 - reset, 0 - ready")
        print("Attribute points left:", character.attribute_points_left())
        command = input("Command: ")
        
        if command == "0":
            break

        elif command == "1":
            print()
            for attribute in character.get_attributes_as_list():
                print(attribute)

        elif command == "2":
            name = input("Name of the attribute: ")
            if name in character.attributes:
                try:
                    character.change_attribute(name, 1)
                except:
                    print("More points cannot be added to this attribute")
            else:
                "Attribute not found"

        elif command == "3":
            name = input("Name of the attribute: ")
            if name in character.attributes:
                try:
                    character.change_attribute(name, -1)
                except:
                    print("More points cannot be removed from this attribute")
            else:
                "Attribute not found"
        
        elif command == "4":
            confirm = input("Type 'yes' if you want to reset all of the attributes: ")
            if confirm == "yes":
                character.reset_attributes()
    print()


    command = input("Type 'yes' if you want to see the character sheet: ")
    if command == "yes":
        print()
        print("-------------------------------------")
        for line in character.full_character_sheet():
            print(line)
        print("-------------------------------------")

if __name__ == "__main__":
    main()
