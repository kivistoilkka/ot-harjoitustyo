from cmath import exp
from pydoc import doc
from entities.archetype import Archetype
from entities.character import Character
from entities.talent import Talent

bookworm = Talent("Bookworm", "Gain +2 to...")
erudite = Talent("Erudite", "You can pass a...")
knowledge_is_reassuring = Talent("Knowledge is Reassuring", "Ignore Conditions when...")
academic_talent_dict = {bookworm.name: bookworm, erudite.name: erudite, knowledge_is_reassuring.name: knowledge_is_reassuring}
academic_equipment_list = [("book collection", "map book"), "writing utensils", ("liquor", "slide rule")]
academic = Archetype("Academic", "Logic", "Learning", academic_talent_dict, (4, 6), academic_equipment_list)

army_medic = Talent("Army medic", "Gain +2 to...")
chief_physician = Talent("Chief physician", "When you use...")
emergency_medicine = Talent("Emergency medicine", "Ignore...")
doctor_talent_dict = {army_medic.name: army_medic, chief_physician.name: chief_physician, emergency_medicine.name: emergency_medicine}
doctor_equipment_list = ["doctor's bag /w medicinal equipment", ("liquor", "wine"), ("weak horse", "strong poison")]
doctor = Archetype("Doctor", "Logic", "Medicine", doctor_talent_dict, (4, 6), doctor_equipment_list)


AVAILABLE_ARCHETYPES = {academic.name: academic, doctor.name: doctor}

def main():
    print()
    print("Character generator for Vaesen: Nordic Horror Roleplaying game")
    print()

    while True:
        #character_name = input("Name your character: ")
        character_name = "Astrid Gregorius"
        if character_name != "":
            character = Character(character_name)
            break

    while True:
        print()
        print("Archetype options:")
        for archetype in AVAILABLE_ARCHETYPES:
            print("-", archetype)
        #name = input("Choose the archetype: ")
        name = "Academic"
        if name in AVAILABLE_ARCHETYPES:
            character.set_archetype(AVAILABLE_ARCHETYPES[name])
            break
    
    while True:
        print()
        #age = input("Age of the character (>17): ")
        age = "55"
        try:
            age = int(age)
            if age > 17:
                character.age = age
                break
        except ValueError:
            print("Give the value in integer")
    
    while True:
        print()
        print("Talent options:")
        for talent in character.archetype.talents:
            print("-", talent)
        #name = input("Choose starting talent: ")
        name = "Erudite"
        if name in character.archetype.talents:
            character.give_talent(name)
            break
    print()

    print("Add points to attributes (range 2-4, for main attribute 2-5)")
    while True:
        print()
        print("1 - show attributes, 2 - add point, 3 - remove point, 4 - reset, 0 - ready")
        print("Attribute points left:", character.attribute_points_left())
        #command = input("Command: ")
        command = "0"

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
                print("Attribute not found")

        elif command == "3":
            name = input("Name of the attribute: ")
            if name in character.attributes:
                try:
                    character.change_attribute(name, -1)
                except:
                    print("More points cannot be removed from this attribute")
            else:
                print("Attribute not found")
        
        elif command == "4":
            confirm = input("Type 'yes' if you want to reset all of the attributes: ")
            if confirm == "yes":
                character.reset_attributes()
    print()

    print("Add points to skills and resources (range 0-2, for main skill 0-3)")
    while True:
        print()
        print("1 - show skills and resources", end="")
        print(", 2 - add point to skills, 3 - remove point from skills, 4 - reset skills", end="")
        print(", 5 - add point to resources, 6 - remove point from resources, 7 - reset resources, 0 - ready")
        print("Skill points left:", character.skill_points_left())
        #command = input("Command: ")
        command = "0"
        
        if command == "0":
            break

        elif command == "1":
            print()
            for skill in character.get_skills_as_list():
                print(skill)
            print("Resources:", character.resources)
        
        elif command == "2":
            name = input("Name of the skill: ")
            amount = input("Points to be added: ")
            try:
                amount = int(amount)
                if amount < 0:
                    print("Value must be positive")
                elif name in character.skills:
                    try:
                        character.change_skill(name, amount)
                    except:
                        print("More points cannot be added to this skill")
                else:
                    print("Skill not found")
            except ValueError:
                print("Give the value in integer")
        
        elif command == "3":
            name = input("Name of the skill: ")
            amount = input("Points to be removed: ")
            try:
                amount = int(amount)
                if amount < 0:
                    print("Value must be positive")
                elif name in character.skills:
                    try:
                        character.change_skill(name, -amount)
                    except:
                        print("More points cannot be removed from this skill")
                else:
                    print("Skill not found")
            except ValueError:
                print("Give the value in integer")
        
        elif command == "4":
            confirm = input("Type 'yes' if you want to reset all of the skills: ")
            if confirm == "yes":
                character.reset_skills()
        
        elif command == "5":
            try:
                character.change_resources(1)
            except:
                print("More points cannot be added to resources")
        
        elif command == "6":
            try:
                character.change_resources(-1)
            except:
                print("More points cannot be removed from resources")
        
        elif command == "7":
            confirm = input("Type 'yes' if you want to reset resources: ")
            if confirm == "yes":
                character.reset_resources()
    print()

    print("Equipment:")
    options = character.archetype.equipment
    for option in options:
        if type(option) == tuple:
            while True:
                command = input(f"Choose one: 1 - {option[0]} or 2 - {option[1]}: ")
                try:
                    selected = int(command)-1
                    if selected == 0 or selected == 1:
                        option = option[selected]
                        break
                except ValueError:
                    print("Give the value in integer")
        character.equipment.append(option)
        print(option, "added to the equipment list")

    command = input("Type 'yes' if you want to see the character sheet: ")
    if command == "yes":
        print()
        print("-------------------------------------")
        for line in character.full_character_sheet():
            print(line)
        print("-------------------------------------")
    
    command = input("Type 'yes' if you want to save the character to a text file: ")
    if command == "yes":
        filename = input("Name of the file: ")
        character.save_to_file(filename)

if __name__ == "__main__":
    main()
