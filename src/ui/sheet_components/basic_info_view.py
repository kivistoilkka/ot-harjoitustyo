from tkinter import ttk, constants, StringVar, IntVar, Text

from services.character_service import character_service

AVAILABLE_ARCHETYPES = character_service.get_archetype_options()


class BasicInfoView:
    def __init__(
        self,
        root,
        name_updater,
        archetype_age_updater,
        character_description_updater
    ):
        self._root = root
        self._frame = None
        self._name_updater = name_updater
        self._archetype_age_updater = archetype_age_updater
        self._character_description_updater = character_description_updater

        self._character_name_var = None

        self._character_name_entry = None
        self._character_archetype_combobox = None
        self._character_age_spinbox = None
        self._character_description_text = None

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

    def _handle_description_update(self):
        try:
            response = self._character_description_updater(
                self._character_description_text.get("1.0", "end")[0:-1]
            )
            self._character_description_text.delete("1.0", "end")
            self._character_description_text.insert("1.0", response)
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

        sep1 = ttk.Separator(
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
        archetype_age_update_button = ttk.Button(
            master=self._frame,
            text="Update",
            command=self._handle_archetype_age_update
        )
        archetype_age_update_note_label = ttk.Label(
            master=self._frame,
            text="""Updating age and/or archetype will reset attributes,
resources, skills, talent and equipment."""
        )

        sep2 = ttk.Separator(
            master=self._frame,
            orient="horizontal"
        )

        description_label = ttk.Label(
            master=self._frame,
            text="Short description of the character:"
        )
        self._character_description_text = Text(
            master=self._frame,
            height=8,
            width=30
        )
        self._character_description_text.insert(
            "1.0",
            character_service.get_character_description()
        )
        description_update_button = ttk.Button(
            master=self._frame,
            text="Update",
            command=self._handle_description_update
        )

        self._root.grid_columnconfigure(1, weight=1)
        header_label.grid(row=0, column=0, columnspan=2,
                          padx=5, pady=5, sticky=constants.W)

        character_name_label.grid(
            row=2, column=0, columnspan=2, padx=5, pady=2, sticky=(constants.E, constants.W))
        self._character_name_entry.grid(
            row=3, column=0, padx=5, pady=5, sticky=(constants.E, constants.W))
        name_update_button.grid(
            row=3, column=1, padx=5, pady=5, sticky=(constants.E))

        sep1.grid(row=4, columnspan=2, pady=2,
                  sticky=(constants.E, constants.W))

        character_age_label.grid(
            row=5, column=0, padx=5, pady=2, sticky=(constants.E, constants.W))
        self._character_age_spinbox.grid(
            row=6, column=0, padx=5, pady=5, sticky=(constants.E, constants.W))

        character_archetype_label.grid(
            row=7, column=0, columnspan=2, padx=5, pady=2, sticky=(constants.E, constants.W))
        self._character_archetype_combobox.grid(
            row=8, column=0, columnspan=1, padx=5, pady=5, sticky=(constants.E, constants.W))
        archetype_age_update_button.grid(row=8, column=1, sticky=(constants.E))
        archetype_age_update_note_label.grid(row=9, columnspan=2,
                                             sticky=(constants.E, constants.W))

        sep2.grid(row=10, columnspan=2, pady=2,
                  sticky=(constants.E, constants.W))

        description_label.grid(
            row=11, column=0, columnspan=2, padx=5, pady=2, sticky=(constants.E, constants.W))
        self._character_description_text.grid(
            row=12, column=0, columnspan=2, padx=5, pady=2, sticky=(constants.E, constants.W))
        description_update_button.grid(
            row=13, column=1, padx=5, pady=5, sticky=(constants.E)
        )
