from tkinter import ttk, constants, StringVar

class TalentsEquipmentView:
    def __init__(
            self,
            root,
            talent_options,
            talent,
            handle_talent_change
        ):
        self._root = root
        self._frame = None
        self._talent_options = talent_options
        self._talent_options_names = list(talent_options.keys())
        self._talent = talent
        self._handle_talent_change = handle_talent_change

        self._talent_name_var = None
        self._talent_desc_var = None
        self._talent_combobox = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _set_current_talent(self, event):
        talent_name = self._talent_combobox.get()
        if talent_name:
            talent_description = self._talent_options[talent_name].description
            self._handle_talent_change(talent_name)
            self._talent_desc_var.set(f"{talent_name}: {talent_description}")

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._talent_name_var = StringVar()
        self._talent_name_var.set(self._talent)
        self._talent_desc_var = StringVar()
        self._talent_desc_var.set(
            "" if self._talent is None else f"{self._talent[0].name}: {self._talent[0].description}"
        )

        talent_header_label = ttk.Label(master=self._frame, text="Talent", font=("", 15, "bold"))
        self._talent_combobox = ttk.Combobox(
            master=self._frame,
            values=self._talent_options_names,
            state="readonly"
        )
        self._talent_combobox.bind("<<ComboboxSelected>>", self._set_current_talent)
        talent_description_label = ttk.Label(master=self._frame, textvariable=self._talent_desc_var)

        equipment_header_label = ttk.Label(
            master=self._frame,
            text="Equipment",
            font=("", 15, "bold")
        )

        talent_header_label.pack(fill=constants.X)
        self._talent_combobox.pack(fill=constants.X)
        talent_description_label.pack(fill=constants.X)
        equipment_header_label.pack(fill=constants.X)
