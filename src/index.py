from tkinter import Tk
from ui.ui import UI
from ui.command_line_ui import CommandLineUI


def main():
    window = Tk()
    window.title("Vaesen Character App")

    ui = UI(window)
    ui.start()

    window.mainloop()


def text_main():
    ui = CommandLineUI()
    ui.start()


if __name__ == "__main__":
    print("UI options: 1 - graphical, 2 - command line")
    selected_ui = input("Select ui: ")

    if selected_ui == "1":
        main()
    elif selected_ui == "2":
        text_main()
    else:
        print("Invalid command")
