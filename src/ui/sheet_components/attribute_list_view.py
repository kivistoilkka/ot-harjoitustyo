from tkinter import ttk, constants, IntVar, Frame


class AttributeListView:
    def __init__(
        self,
        root,
        attributes: dict,
        attribute_updater,
        main_attribute,
        attribute_points_left
    ):
        self._root = root
        self._frame = None
        self._attributes = attributes
        self._attribute_updater = attribute_updater
        self._main_attribute = main_attribute
        self._attribute_points_left = attribute_points_left
        self._attribute_points_var = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _handle_attribute_change(
        self,
        attribute,
        amount,
        value_label_var,
        attribute_points_var
    ):
        response = self._attribute_updater(attribute, amount)
        value_label_var.set(response[0])
        attribute_points_var.set(response[1])

    def _initialize_attribute_item(self, name, value):
        item_frame = Frame(master=self._frame, bg=self._root["bg"])

        name_label = ttk.Label(
            master=item_frame,
            text=name,
            background=self._root["bg"]
        )
        if name == self._main_attribute:
            name_label.config(font=("", 11, "bold"))

        value_label_var = IntVar()
        value_label_var.set(value)
        value_label = ttk.Label(
            master=item_frame,
            textvariable=value_label_var,
            background=self._root["bg"]
        )
        decrease_button = ttk.Button(
            master=item_frame,
            text="-",
            command=lambda: self._handle_attribute_change(
                name, -1, value_label_var, self._attribute_points_var)
        )
        increase_button = ttk.Button(
            master=item_frame,
            text="+",
            command=lambda: self._handle_attribute_change(
                name, 1, value_label_var, self._attribute_points_var)
        )

        item_frame.grid_columnconfigure(0, minsize=240)
        name_label.grid(row=0, column=0, padx=5, pady=5, sticky=constants.W)
        decrease_button.grid(row=0, column=1, padx=5,
                             pady=5, sticky=constants.W)
        value_label.grid(row=0, column=2, padx=5, pady=5, sticky=constants.W)
        increase_button.grid(row=0, column=3, padx=5,
                             pady=5, sticky=constants.W)

        item_frame.pack(fill=constants.X)

    def _initialize(self):
        self._frame = Frame(master=self._root, bg=self._root["bg"])
        self._attribute_points_var = IntVar()
        self._attribute_points_var.set(self._attribute_points_left)

        header_label = ttk.Label(
            master=self._frame,
            text="Attributes",
            font=("", 15, "bold"),
            background=self._root["bg"]
        )
        points_left_label = ttk.Label(
            master=self._frame,
            text="Attribute points left:",
            background=self._root["bg"]
        )
        points_left_value_label = ttk.Label(
            master=self._frame,
            textvariable=self._attribute_points_var,
            background=self._root["bg"]
        )
        sep = ttk.Separator(
            master=self._frame,
            orient="horizontal"
        )

        header_label.pack(fill=constants.X, padx=5)
        for name, value in self._attributes.items():
            self._initialize_attribute_item(name, value)
        points_left_label.pack(fill=constants.X, padx=5)
        points_left_value_label.pack(fill=constants.X, padx=5)
        sep.pack(fill=constants.X, padx=5, pady=5)
