from tkinter import ttk, constants, StringVar, IntVar, Frame
from tkinter.messagebox import showerror

from services.character_service import character_service

AVAILABLE_ARCHETYPES = character_service.get_archetype_options()


class CharacterCreationView:
    def __init__(self, root, _handle_char_modifying):
        self._root = root
        self._frame = None
        self._handle_char_modifying = _handle_char_modifying
        self._character_name_entry = None
        self._character_archetype_combobox = None
        self._character_age_spinbox = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _handle_create(self):
        name_value = self._character_name_entry.get()
        archetype_value = self._character_archetype_combobox.get()
        age_value = self._character_age_spinbox.get()

        if name_value and archetype_value and age_value:
            try:
                character_service.create_character(
                    name_value, archetype_value, int(age_value))
                self._handle_char_modifying()
            except ValueError:
                showerror(
                    "Error",
                    "Character could not be created, make sure that character age is 17 or more."
                )

    def _initialize(self):
        self._frame = Frame(master=self._root, bg=self._root["bg"])
        self._character_archetype_var = StringVar()
        self._character_archetype_var.set(AVAILABLE_ARCHETYPES[0])
        self._character_age_var = IntVar()
        self._character_age_var.set(17)

        header_label = ttk.Label(
            master=self._frame,
            text="Create a new character",
            font=("", 20),
            background=self._root["bg"]
        )

        character_name_label = ttk.Label(
            master=self._frame,
            text="Character name:",
            background=self._root["bg"]
        )
        self._character_name_entry = ttk.Entry(
            master=self._frame
        )

        character_archetype_label = ttk.Label(
            master=self._frame,
            text="Character archetype:",
            background=self._root["bg"]
        )
        self._character_archetype_combobox = ttk.Combobox(
            master=self._frame,
            state="readonly",
            values=AVAILABLE_ARCHETYPES
        )
        self._character_archetype_combobox.set(AVAILABLE_ARCHETYPES[0])

        character_age_label = ttk.Label(
            master=self._frame,
            text="Character age:",
            background=self._root["bg"]
        )
        self._character_age_spinbox = ttk.Spinbox(
            master=self._frame,
            from_=17,
            to_=999
        )
        self._character_age_spinbox.set(17)

        create_button = ttk.Button(
            master=self._frame,
            text="Create",
            command=self._handle_create
        )

        self._root.grid_columnconfigure(1, weight=1)
        header_label.grid(row=0, column=0, columnspan=2,
                          padx=5, pady=5, sticky=constants.W)

        character_name_label.grid(
            row=1, column=0, padx=5, pady=5, sticky=(constants.E, constants.W))
        self._character_name_entry.grid(
            row=1, column=1, padx=5, pady=5, sticky=(constants.E, constants.W))

        character_archetype_label.grid(
            row=2, column=0, padx=5, pady=5, sticky=(constants.E, constants.W))
        self._character_archetype_combobox.grid(
            row=2, column=1, padx=5, pady=5, sticky=(constants.E, constants.W))

        character_age_label.grid(
            row=3, column=0, padx=5, pady=5, sticky=(constants.E, constants.W))
        self._character_age_spinbox.grid(
            row=3, column=1, padx=5, pady=5, sticky=(constants.E, constants.W))

        create_button.grid(row=4, column=1, padx=5, pady=5, sticky=constants.E)
