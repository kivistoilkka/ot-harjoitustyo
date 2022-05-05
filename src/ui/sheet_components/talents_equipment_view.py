from tkinter import ttk, constants, StringVar


class TalentsEquipmentView:
    def __init__(
        self,
        root,
        talent_options: dict,
        talents: list,
        handle_talent_change,
        equipment_options: list,
        character_equipment: list,
        handle_equipment_change
    ):
        self._root = root
        self._frame = None
        self._talent_options = talent_options
        self._talent_options_names = list(talent_options.keys())
        self._talents = talents
        self._handle_talent_change = handle_talent_change
        self._equipment_options = equipment_options
        self._character_equipment = character_equipment
        self._handle_equipment_change = handle_equipment_change

        self._talent_header_label = None
        self._talent_name_var = None
        self._talent_desc_var = None
        self._talent_combobox = None
        self._talent_description_label = None
        self._equipment_header_label = None
        self._equipment_selected_label = None
        self._equipment_names_var = None
        self._equipment_selection_fields = None
        self._equipment_save_button = None
        self._equipment_saved_var = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _set_current_talent(self, event):
        talent_name = event.widget.get()
        if talent_name:
            talent_description = self._talent_options[talent_name].description
            self._handle_talent_change(talent_name)
            self._talent_desc_var.set(f"{talent_name}:\n{talent_description}")

    def _change_current_equipment(self, equipment_name):
        another_option = ""
        for item in self._equipment_options:
            if isinstance(item, tuple) and equipment_name in item:
                another_option = item[0] if item[1] == equipment_name else item[1]
        for item in self._equipment_names_var:
            if item.get() == another_option:
                item.set(equipment_name)
                return

    def _set_character_equipment(self):
        selected_equipment = [item.get() for item in self._equipment_names_var]
        self._character_equipment = self._handle_equipment_change(
            selected_equipment)
        i = 0
        while i < 3:
            self._equipment_saved_var[i].set(selected_equipment[i])
            i += 1

    def _initialize_talent_section(self):
        self._talent_name_var = StringVar()
        self._talent_name_var.set(self._talents)
        self._talent_desc_var = StringVar()
        self._talent_desc_var.set(
            "" if self._talents is None else f"{self._talents[0].name}:\n{self._talents[0].description}"
        )

        self._talent_header_label = ttk.Label(
            master=self._frame,
            text="Talent",
            font=("", 15, "bold")
        )
        self._talent_combobox = ttk.Combobox(
            master=self._frame,
            values=self._talent_options_names,
            state="readonly"
        )
        self._talent_combobox.bind(
            "<<ComboboxSelected>>", self._set_current_talent)
        if self._talents is not None:
            self._talent_combobox.set(self._talents[0].name)
        self._talent_description_label = ttk.Label(
            master=self._frame,
            textvariable=self._talent_desc_var
        )

    def _initialize_equipment_section(self):
        self._equipment_names_var = [StringVar(), StringVar(), StringVar()]
        self._equipment_saved_var = [StringVar(), StringVar(), StringVar()]
        if len(self._character_equipment) == 0:
            equipment_list_to_use = self._equipment_options
        else:
            equipment_list_to_use = self._character_equipment
        i = 0
        while i < 3:
            if isinstance(equipment_list_to_use[i], tuple):
                self._equipment_names_var[i].set(equipment_list_to_use[i][0])
                self._equipment_saved_var[i].set(equipment_list_to_use[i][0])
            else:
                self._equipment_names_var[i].set(equipment_list_to_use[i])
                self._equipment_saved_var[i].set(equipment_list_to_use[i])
            i += 1
        if len(self._character_equipment) == 0:
            self._set_character_equipment()

        self._equipment_header_label = ttk.Label(
            master=self._frame,
            text="Equipment",
            font=("", 15, "bold")
        )
        self._equipment_selected_label = ttk.Label(
            master=self._frame,
            text="Currently selected:",
            font=("", 11, "italic")
        )
        self._equipment_selection_fields = []
        for item in self._equipment_options:
            if isinstance(item, tuple):
                combobox = ttk.Combobox(
                    master=self._frame,
                    values=[item[0], item[1]],
                    state="readonly"
                )
                if item[1] in self._character_equipment:
                    combobox.set(item[1])
                else:
                    combobox.set(item[0])
                combobox.bind(
                    "<<ComboboxSelected>>",
                    lambda event: self._change_current_equipment(event.widget.get()))
                self._equipment_selection_fields.append(combobox)
            else:
                label = ttk.Label(
                    master=self._frame,
                    text=item,
                )
                self._equipment_selection_fields.append(label)
        self._equipment_save_button = ttk.Button(
            master=self._frame,
            text="Change equipment",
            command=self._set_character_equipment
        )

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        self._initialize_talent_section()
        self._initialize_equipment_section()

        self._talent_header_label.pack(fill=constants.X)
        self._talent_combobox.pack(fill=constants.X)
        self._talent_description_label.pack(fill=constants.X)
        self._equipment_header_label.pack(fill=constants.X)
        for item in self._equipment_selection_fields:
            item.pack(fill=constants.X)
        self._equipment_save_button.pack()
        self._equipment_selected_label.pack(fill=constants.X, pady=5)
        for item in self._equipment_saved_var:
            ttk.Label(master=self._frame, textvariable=item).pack(
                fill=constants.X)
