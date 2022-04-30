from tkinter import Tk
from ui.ui import UI
from ui.command_line_ui import CommandLineUI


def main():
    window = Tk()
    window.title("Vaesen Character App")

    user_interface = UI(window)
    user_interface.start()

    window.mainloop()


def text_main():
    user_interface = CommandLineUI()
    user_interface.start()


if __name__ == "__main__":
    main()
    # print("UI options: 1 - graphical, 2 - command line")
    # SELECTED_UI = input("Select ui: ")

    # if SELECTED_UI == "1":
    #     main()
    # elif SELECTED_UI == "2":
    #     text_main()
    # else:
    #     print("Invalid command")
