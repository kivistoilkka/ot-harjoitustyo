from tkinter import ttk, constants, StringVar, IntVar

from services.character_service import character_service

AVAILABLE_ARCHETYPES = character_service.get_archetype_options()


class BasicInfoView:
    def __init__(self, root, name_updater, archetype_age_updater):
        self._root = root
        self._frame = None
        self._name_updater = name_updater
        self._archetype_age_updater = archetype_age_updater

        self._character_name_var = None

        self._character_name_entry = None
        self._character_archetype_combobox = None
        self._character_age_spinbox = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _handle_name_update(self):
        try:
            self._name_updater(self._character_name_entry.get())
        except ValueError:
            pass

    def _handle_archetype_age_update(self):
        try:
            self._archetype_age_updater(
                self._character_archetype_combobox.get(),
                self._character_age_spinbox.get()
            )
        except ValueError:
            pass

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        header_label = ttk.Label(
            master=self._frame,
            text="Basic information",
            font=("", 15, "bold")
        )
        header_label.pack(fill=constants.X)

        self._character_name_var = StringVar()
        self._character_name_var.set(character_service.get_character_name())
        self._character_archetype_var = StringVar()
        self._character_archetype_var.set(
            character_service.get_character_archetype_name())
        self._character_age_var = IntVar()
        self._character_age_var.set(character_service.get_character_age())

        character_name_label = ttk.Label(
            master=self._frame,
            text=f"Character name: {self._character_name_var.get()}",
        )
        self._character_name_entry = ttk.Entry(
            master=self._frame,
            textvariable=self._character_name_var
        )
        name_update_button = ttk.Button(
            master=self._frame,
            text="Change name",
            command=self._handle_name_update
        )

        sep = ttk.Separator(
            master=self._frame,
            orient="horizontal"
        )

        character_archetype_label = ttk.Label(
            master=self._frame,
            text="Character archetype:",
        )
        self._character_archetype_combobox = ttk.Combobox(
            master=self._frame,
            state="readonly",
            values=AVAILABLE_ARCHETYPES
        )
        self._character_archetype_combobox.set(
            self._character_archetype_var.get())

        character_age_label = ttk.Label(
            master=self._frame,
            text="Character age:"
        )
        self._character_age_spinbox = ttk.Spinbox(
            master=self._frame,
            from_=17,
            to_=999
        )
        self._character_age_spinbox.set(self._character_age_var.get())
        update_button = ttk.Button(
            master=self._frame,
            text="Update",
            command=self._handle_archetype_age_update
        )
        update_note_label = ttk.Label(
            master=self._frame,
            text="Updating age and/or archetype will reset attributes,\nskills, resources, talent and equipment."
        )

        self._root.grid_columnconfigure(1, weight=1)
        header_label.grid(row=0, column=0, columnspan=2,
                          padx=5, pady=5, sticky=constants.W)

        character_name_label.grid(
            row=2, column=0, columnspan=2, padx=5, pady=2, sticky=(constants.E, constants.W))
        self._character_name_entry.grid(
            row=3, column=0, padx=5, pady=5, sticky=(constants.E, constants.W))
        name_update_button.grid(
            row=3, column=1, padx=5, pady=5, sticky=(constants.E, constants.W))
        sep.grid(row=4, columnspan=2, sticky=(constants.E, constants.W))
        character_age_label.grid(
            row=5, column=0, padx=5, pady=2, sticky=(constants.E, constants.W))
        self._character_age_spinbox.grid(
            row=6, column=0, padx=5, pady=5, sticky=(constants.E, constants.W))

        character_archetype_label.grid(
            row=7, column=0, columnspan=2, padx=5, pady=2, sticky=(constants.E, constants.W))
        self._character_archetype_combobox.grid(
            row=8, column=0, columnspan=1, padx=5, pady=5, sticky=(constants.E, constants.W))
        update_button.grid(row=8, column=1)
        update_note_label.grid(row=9, columnspan=2, sticky=(constants.E, constants.W))
