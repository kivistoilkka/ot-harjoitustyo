from tkinter import ttk, constants, StringVar, IntVar

from entities.character import Character

from repositories.archetype_repository import archetype_repository

AVAILABLE_ARCHETYPES = archetype_repository.find_all()
ARCHETYPE_NAMES = list(AVAILABLE_ARCHETYPES.keys())


class CharacterCreationView:
    def __init__(self, root):
        self._root = root
        self._frame = None
        self._character_name_entry = None
        self._character_archetype_checkbox = None
        self._character_age_spinbox = None

        self._character = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _handle_create(self):
        name_value = self._character_name_entry.get()
        archetype_value = self._character_archetype_checkbox.get()
        age_value = self._character_age_spinbox.get()

        if name_value and archetype_value and age_value:
            self._character = Character(name_value)
            self._character.set_archetype(
                AVAILABLE_ARCHETYPES[archetype_value])
            self._character.age = int(age_value)
            print(self._character)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._character_archetype_var = StringVar()
        self._character_archetype_var.set(ARCHETYPE_NAMES[0])
        self._character_age_var = IntVar()
        self._character_age_var.set(17)

        header_label = ttk.Label(
            master=self._frame,
            text="Create a new character",
            font=("", 20)
        )

        character_name_label = ttk.Label(
            master=self._frame,
            text="Character name:",
        )
        self._character_name_entry = ttk.Entry(
            master=self._frame
        )

        character_archetype_label = ttk.Label(
            master=self._frame,
            text="Character archetype:",
        )
        self._character_archetype_checkbox = ttk.Combobox(
            master=self._frame,
            values=ARCHETYPE_NAMES
        )
        self._character_archetype_checkbox.set(ARCHETYPE_NAMES[0])

        character_age_label = ttk.Label(
            master=self._frame,
            text="Character age:"
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
        self._character_archetype_checkbox.grid(
            row=2, column=1, padx=5, pady=5, sticky=(constants.E, constants.W))

        character_age_label.grid(
            row=3, column=0, padx=5, pady=5, sticky=(constants.E, constants.W))
        self._character_age_spinbox.grid(
            row=3, column=1, padx=5, pady=5, sticky=(constants.E, constants.W))

        create_button.grid()
