from services.character_service import character_service


class CommandLineUI:
    def start(self):
        print()
        print("Character generator for Vaesen: Nordic Horror Roleplaying game")
        print()

        while True:
            character_name = input("Name your character: ")
            #character_name = "Astrid Gregorius"
            if character_name != "":
                break

        while True:
            print()
            print("Archetype options:")
            archetype_options = character_service.get_archetype_options()
            for archetype in archetype_options:
                print("-", archetype)
            archetype_name = input("Choose the archetype: ")
            #archetype_name = "Academic"
            if archetype_name in archetype_options:
                break

        while True:
            print()
            age = input("Age of the character (>17): ")
            #age = "55"
            try:
                age = int(age)
                if age > 17:
                    break
            except ValueError:
                print("Give the value in integer")
        character_service.create_character(character_name, archetype_name, age)

        while True:
            print()
            print("Talent options:")
            for talent in character_service.get_talent_options():
                print("-", talent)
            name = input("Choose starting talent: ")
            #name = "Erudite"
            if name in character_service.get_talent_options():
                character_service.give_talent_to_character(name)
                break
        print()

        print("Add points to attributes (range 2-4, for main attribute 2-5)")
        while True:
            print()
            print(
                "1 - show attributes, 2 - add point, 3 - remove point, 4 - reset, 0 - ready")
            print("Attribute points left:",
                  character_service.get_character_attribute_points_left())
            command = input("Command: ")
            #command = "0"

            if command == "0":
                break

            elif command == "1":
                print()
                for attribute in character_service.get_character_attributes_as_list():
                    print(attribute)

            elif command == "2":
                name = input("Name of the attribute: ")
                if character_service.change_character_attribute(name, 1):
                    print(f"1 point added to {name}")
                else:
                    print("Unable to add points")

            elif command == "3":
                name = input("Name of the attribute: ")
                if character_service.change_character_attribute(name, -1):
                    print(f"1 point removed from {name}")
                else:
                    print("Unable to remove points")

            elif command == "4":
                confirm = input(
                    "Type 'yes' if you want to reset all of the attributes: ")
                if confirm == "yes":
                    character_service.reset_character_attributes()
        print()

        print("Add points to skills and resources (range 0-2, for main skill 0-3)")
        while True:
            print()
            print("1 - show skills and resources", end="")
            print(
                ", 2 - add point to skills, 3 - remove point from skills, 4 - reset skills", end="")
            print(
                ", 5 - add point to resources, 6 - remove point from resources, 7 - reset resources, 0 - ready")
            print("Skill points left:",
                  character_service.get_character_skill_points_left())
            command = input("Command: ")
            #command = "0"

            if command == "0":
                break

            elif command == "1":
                print()
                for skill in character_service.get_character_skills_as_list():
                    print(skill)
                print("Resources:", character_service.get_character_resources())

            elif command == "2":
                name = input("Name of the skill: ")
                amount = input("Points to be added: ")
                try:
                    amount = int(amount)
                    if amount < 0:
                        print("Value must be positive")
                    elif character_service.change_character_skill(name, amount):
                        print(f"{amount} points added to {name}")
                    else:
                        print("Unable to add points")
                except:
                    print("Unable to add points")

            elif command == "3":
                name = input("Name of the skill: ")
                amount = input("Points to be removed: ")
                try:
                    amount = int(amount)
                    if amount < 0:
                        print("Value must be positive")
                    elif character_service.change_character_skill(name, -amount):
                        print(f"{amount} points removed from {name}")
                    else:
                        print("Unable to remove points")
                except:
                    print("Unable to remove points")

            elif command == "4":
                confirm = input(
                    "Type 'yes' if you want to reset all of the skills: ")
                if confirm == "yes":
                    character_service.reset_character_skills()
                    print("Skill points are reset")

            elif command == "5":
                if character_service.change_character_resources(1):
                    print("One point has been added to the resources")
                else:
                    print("More points cannot be added to resources")

            elif command == "6":
                if character_service.change_character_resources(-1):
                    print("One point has been removed from the resources")
                else:
                    print("More points cannot be removed from resources")

            elif command == "7":
                confirm = input("Type 'yes' if you want to reset resources: ")
                if confirm == "yes":
                    character_service.reset_character_resources()
        print()

        print("Equipment:")
        options = character_service.get_equipment_options()
        items = []
        for option in options:
            if type(option) == tuple:
                while True:
                    command = input(
                        f"Choose one: 1 - {option[0]} or 2 - {option[1]}: ")
                    try:
                        selected = int(command)-1
                        if selected == 0 or selected == 1:
                            option = option[selected]
                            break
                    except ValueError:
                        print("Give the value in integer")
            items.append(option)
            print(option, "added to the equipment list")
        character_service.set_character_equipment(items)
        print()

        command = input("Type 'yes' if you want to see the character sheet: ")
        if command == "yes":
            print()
            print("-------------------------------------")
            for line in character_service.full_character_sheet():
                print(line)
            print("-------------------------------------")
        print()

        command = input(
            "Type 'yes' if you want to save the character to a text file: ")
        if command == "yes":
            filename = input("Name of the file: ")
            character_service.save_character_to_file(filename)


if __name__ == "__main__":
    ui = CommandLineUI()
    ui.start()
