from tkinter import ttk, constants, IntVar, Frame


class SkillListResourcesView:
    skill_to_attribute = {
        "Agility": "Physique",
        "Close combat": "Physique",
        "Force": "Physique",
        "Medicine": "Precision",
        "Ranged combat": "Precision",
        "Stealth": "Precision",
        "Investigation": "Logic",
        "Learning": "Logic",
        "Vigilance": "Logic",
        "Inspiration": "Empathy",
        "Manipulation": "Empathy",
        "Observation": "Empathy"
    }

    def __init__(
        self,
        root,
        skills: dict,
        skill_updater,
        main_skill,
        resources,
        resource_updater,
        skill_points_left
    ):
        self._root = root
        self._frame = None
        self._skills = skills
        self._skill_updater = skill_updater
        self._main_skill = main_skill
        self._resources = resources
        self._resource_updater = resource_updater
        self._skill_points_left = skill_points_left

        self._resources_var = None
        self._skill_points_var = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _handle_skill_change(self, skill, amount, value_label_var, skill_points_var):
        response = self._skill_updater(skill, amount)
        value_label_var.set(response[0])
        skill_points_var.set(response[1])

    def _handle_resource_change(self, amount):
        response = self._resource_updater(amount)
        self._resources_var.set(response[0])
        self._skill_points_var.set(response[1])

    def _initialize_resources(self):
        item_frame = Frame(master=self._frame, bg=self._root["bg"])
        value_label = ttk.Label(
            master=item_frame,
            textvariable=self._resources_var,
            background=self._root["bg"]
        )
        decrease_button = ttk.Button(
            master=item_frame,
            text="-",
            command=lambda: self._handle_resource_change(-1)
        )
        increase_button = ttk.Button(
            master=item_frame,
            text="+",
            command=lambda: self._handle_resource_change(1)
        )

        item_frame.grid_columnconfigure(0, minsize=240)
        decrease_button.grid(row=0, column=1, padx=5,
                             pady=5, sticky=constants.W)
        value_label.grid(row=0, column=2, padx=5, pady=5, sticky=constants.W)
        increase_button.grid(row=0, column=3, padx=5,
                             pady=5, sticky=constants.W)
        item_frame.pack(fill=constants.X)

    def _initialize_skill_item(self, name, value):
        item_frame = Frame(master=self._frame, bg=self._root["bg"])

        name_label = ttk.Label(
            master=item_frame,
            text=f"{name} ({SkillListResourcesView.skill_to_attribute[name]})",
            background=self._root["bg"]
        )
        if name == self._main_skill:
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
            command=lambda: self._handle_skill_change(
                name, -1, value_label_var, self._skill_points_var)
        )
        increase_button = ttk.Button(
            master=item_frame,
            text="+",
            command=lambda: self._handle_skill_change(
                name, 1, value_label_var, self._skill_points_var)
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
        self._skill_points_var = IntVar()
        self._skill_points_var.set(self._skill_points_left)
        self._resources_var = IntVar()
        self._resources_var.set(self._resources)

        resources_label = ttk.Label(
            master=self._frame, text="Resources",
            font=("", 15, "bold"),
            background=self._root["bg"]
        )
        skills_label = ttk.Label(
            master=self._frame,
            text="Skills",
            font=("", 15, "bold"),
            background=self._root["bg"]
        )
        points_left_label = ttk.Label(
            master=self._frame,
            text="Skill/resource points left:",
            background=self._root["bg"]
        )
        points_left_value_label = ttk.Label(
            master=self._frame,
            textvariable=self._skill_points_var,
            background=self._root["bg"]
        )

        resources_label.pack(fill=constants.X, padx=5)
        self._initialize_resources()
        skills_label.pack(fill=constants.X, padx=5)
        for name, value in self._skills.items():
            self._initialize_skill_item(name, value)
        points_left_label.pack(fill=constants.X, padx=5)
        points_left_value_label.pack(fill=constants.X, padx=5)
