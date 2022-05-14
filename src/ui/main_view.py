from tkinter import ttk, constants, Frame
import webbrowser


class MainView:
    def __init__(self, root):
        self._root = root
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = Frame(master=self._root, bg=self._root["bg"])
        header_label = ttk.Label(
            master=self._frame,
            text="Vaesen Character App",
            background=self._root["bg"],
            font=("", 30, "bold")
        )

        introduction_label = ttk.Label(
            master=self._frame,
            text="""Character generator for Vaesen: Nordic Horror Roleplaying game \
(Free League Publishing).""",
            background=self._root["bg"]
        )

        url = "https://freeleaguepublishing.com/en/games/vaesen/"
        publisher_website_button = ttk.Button(
            master=self._frame,
            text="Open publisher website",
            command=lambda: webbrowser.open_new_tab(url)
        )

        program_information_label = ttk.Label(
            master=self._frame,
            text="""This program is made as a coursework for University of Helsinki course \
TKT20002: Ohjelmistotekniikka (Software Development Methods) in 2022 by Ilkka Kivistö.""",
            background=self._root["bg"],
            font=("", 9, "italic")
        )

        self._frame.grid_columnconfigure(0, minsize=1100)
        self._frame.grid_rowconfigure(0, minsize=100)
        header_label.grid(row=0, column=0, padx=5, pady=5)
        introduction_label.grid(row=1, column=0, padx=15, pady=5, sticky=constants.NW)
        publisher_website_button.grid(row=2, column=0, padx=15, pady=5, sticky=constants.NW)
        self._frame.grid_rowconfigure(3, minsize=690)
        program_information_label.grid(row=3, column=0, padx=15, pady=5, sticky=constants.SW)
