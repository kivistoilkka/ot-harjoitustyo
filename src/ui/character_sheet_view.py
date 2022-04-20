from tkinter import ttk, constants, StringVar, IntVar

from services.character_service import character_service

AVAILABLE_ARCHETYPES = character_service.get_archetype_options()

class BasicInfoView:
    def __init__(self, root, handle_update):
        self._root = root
        self._frame = None
        self._handle_update = handle_update

        self._character_name_entry = None
        self._character_archetype_checkbox = None
        self._character_age_spinbox = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        header_label = ttk.Label(master=self._frame, text="Basic information", font=("", 15, "bold"))
        header_label.pack(fill=constants.X)

        self._character_name_var = StringVar()
        self._character_name_var.set(character_service.get_character_name())
        self._character_archetype_var = StringVar()
        self._character_archetype_var.set(character_service.get_character_archetype_name())
        self._character_age_var = IntVar()
        self._character_age_var.set(character_service.get_character_age())

        character_name_label = ttk.Label(
            master=self._frame,
            text="Character name:",
        )
        self._character_name_entry = ttk.Entry(
            master=self._frame,
            textvariable=self._character_name_var
        )

        character_archetype_label = ttk.Label(
            master=self._frame,
            text="Character archetype:",
        )
        self._character_archetype_checkbox = ttk.Combobox(
            master=self._frame,
            values=AVAILABLE_ARCHETYPES
        )
        self._character_archetype_checkbox.set(self._character_archetype_var.get())

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
        character_agegroup_label = ttk.Label(
            master=self._frame,
            text=character_service.get_character_agegroup(int(self._character_age_var.get()))
        )

        update_button = ttk.Button(
            master=self._frame,
            text="Update",
            command=lambda: self._handle_update(
                self._character_name_entry.get(),
                self._character_archetype_checkbox.get(),
                self._character_age_spinbox.get()
            )
        )

        self._root.grid_columnconfigure(1, weight=1)
        header_label.grid(row=0, column=0, columnspan=2,
                          padx=5, pady=5, sticky=constants.W)

        character_name_label.grid(
            row=2, column=0, columnspan=2, padx=5, pady=2, sticky=(constants.E, constants.W))
        self._character_name_entry.grid(
            row=3, column=0, columnspan=2, padx=5, pady=5, sticky=(constants.E, constants.W))

        character_age_label.grid(
            row=4, column=0, padx=5, pady=2, sticky=(constants.E, constants.W))
        self._character_age_spinbox.grid(
            row=5, column=0, padx=5, pady=5, sticky=(constants.E, constants.W))
        character_agegroup_label.grid(
            row=5, column=1, padx=5, pady=5, sticky=(constants.E, constants.W))

        character_archetype_label.grid(
            row=6, column=0, columnspan=2, padx=5, pady=2, sticky=(constants.E, constants.W))
        self._character_archetype_checkbox.grid(
            row=7, column=0, columnspan=1, padx=5, pady=5, sticky=(constants.E, constants.W))

        update_button.grid(row=7, column=1)

class AttributeListView:
    def __init__(
            self,
            root,
            attributes: dict,
            handle_attribute_change,
            main_attribute,
            attribute_points_left
        ):
        self._root = root
        self._frame = None
        self._attributes = attributes
        self._handle_attribute_change = handle_attribute_change
        self._main_attribute = main_attribute
        self._attribute_points_left = attribute_points_left

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize_attribute_item(self, name, value):
        item_frame = ttk.Frame(master=self._frame)
        name_label = ttk.Label(master=item_frame, text=name)
        if name == self._main_attribute:
            name_label = ttk.Label(master=item_frame, text=name, font=("", 11, "bold"))
        value_label = ttk.Label(master=item_frame, text=value)
        decrease_button = ttk.Button(
            master=item_frame,
            text="-",
            command=lambda: self._handle_attribute_change(name, -1)
        )
        increase_button = ttk.Button(
            master=item_frame,
            text="+",
            command=lambda: self._handle_attribute_change(name, 1)
        )

        name_label.grid(row=0, column=0, padx=5, pady=5, sticky=constants.W)
        decrease_button.grid(row=0, column=1, padx=5, pady=5, sticky=constants.W)
        value_label.grid(row=0, column=2, padx=5, pady=5, sticky=constants.W)
        increase_button.grid(row=0, column=3, padx=5, pady=5, sticky=constants.W)

        item_frame.pack(fill=constants.X)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        header_label = ttk.Label(master=self._frame, text="Attributes", font=("", 15, "bold"))
        points_left_label = ttk.Label(
            master=self._frame,
            text=f"Attribute points left: {self._attribute_points_left}"
        )

        header_label.pack(fill=constants.X)
        for name, value in self._attributes.items():
            self._initialize_attribute_item(name, value)
        points_left_label.pack(fill=constants.X)

class SkillListView:
    def __init__(
            self,
            root,
            skills: dict,
            handle_skill_change,
            main_skill,
            resources,
            handle_resource_change,
            skill_points_left
        ):
        self._root = root
        self._frame = None
        self._skills = skills
        self._handle_skill_change = handle_skill_change
        self._main_skill = main_skill
        self._resources = resources
        self._handle_resource_change = handle_resource_change
        self._skill_points_left = skill_points_left

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize_resources(self):
        item_frame = ttk.Frame(master=self._frame)
        value_label = ttk.Label(master=item_frame, text=self._resources)
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

        decrease_button.grid(row=0, column=0, padx=5, pady=5, sticky=constants.W)
        value_label.grid(row=0, column=1, padx=5, pady=5, sticky=constants.W)
        increase_button.grid(row=0, column=2, padx=5, pady=5, sticky=constants.W)

        item_frame.pack(fill=constants.X)

    def _initialize_skill_item(self, name, value):
        item_frame = ttk.Frame(master=self._frame)
        name_label = ttk.Label(master=item_frame, text=name)
        if name == self._main_skill:
            name_label = ttk.Label(master=item_frame, text=name, font=("", 11, "bold"))
        value_label = ttk.Label(master=item_frame, text=value)
        decrease_button = ttk.Button(
            master=item_frame,
            text="-",
            command=lambda: self._handle_skill_change(name, -1)
        )
        increase_button = ttk.Button(
            master=item_frame,
            text="+",
            command=lambda: self._handle_skill_change(name, 1)
        )

        name_label.grid(row=0, column=0, padx=5, pady=5, sticky=constants.W)
        decrease_button.grid(row=0, column=1, padx=5, pady=5, sticky=constants.W)
        value_label.grid(row=0, column=2, padx=5, pady=5, sticky=constants.W)
        increase_button.grid(row=0, column=3, padx=5, pady=5, sticky=constants.W)

        item_frame.pack(fill=constants.X)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        resources_label = ttk.Label(master=self._frame, text="Resources", font=("", 15, "bold"))
        skills_label = ttk.Label(master=self._frame, text="Skills", font=("", 15, "bold"))
        points_left_label = ttk.Label(
            master=self._frame,
            text=f"Skill/resource points left: {self._skill_points_left}"
        )

        resources_label.pack(fill=constants.X)
        self._initialize_resources()
        skills_label.pack(fill=constants.X)
        for name, value in self._skills.items():
            self._initialize_skill_item(name, value)
        points_left_label.pack(fill=constants.X)


class CharacterSheetView:
    def __init__(self, root):
        self._root = root
        self._frame = None
        self._basic_info_frame = None
        self._basic_info_view = None
        self._attribute_list_frame = None
        self._attribute_list_view = None
        self._resource_frame = None
        self._resource_view = None
        self._skill_list_frame = None
        self._skill_list_view = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _handle_basic_info_update(self, name_value, archetype_value, age_value):
        character_service.set_character_name(name_value)
        character_service.set_character_archetype(archetype_value)
        character_service.set_character_age(int(age_value))
        print(character_service.get_character_summary())
        self._initialize_basic_info()

    def _handle_attribute_change(self, attribute, amount):
        character_service.change_character_attribute(attribute, amount)
        self._initialize_attribute_list()

    def _handle_resource_change(self, amount):
        character_service.change_character_resources(amount)
        self._initialize_skill_list()

    def _handle_skill_change(self, skill, amount):
        character_service.change_character_skill(skill, amount)
        self._initialize_skill_list()

    def _initialize_basic_info(self):
        if self._basic_info_view:
            self._basic_info_view.destroy()
            character_service.reset_character_attributes()
            character_service.reset_character_resources()
            character_service.reset_character_skills()
            self._initialize_attribute_list()
            self._initialize_skill_list()

        self._basic_info_view = BasicInfoView(
            self._basic_info_frame,
            self._handle_basic_info_update
        )

        self._basic_info_view.pack()

    def _initialize_attribute_list(self):
        if self._attribute_list_view:
            self._attribute_list_view.destroy()

        self._attribute_list_view = AttributeListView(
            self._attribute_list_frame,
            character_service.get_character_attributes(),
            self._handle_attribute_change,
            character_service.get_character_main_attribute(),
            character_service.get_character_attribute_points_left()
        )

        self._attribute_list_view.pack()

    def _initialize_skill_list(self):
        if self._skill_list_view:
            self._skill_list_view.destroy()

        skills = character_service.get_character_skills()

        self._skill_list_view = SkillListView(
            self._attribute_list_frame,
            skills,
            self._handle_skill_change,
            character_service.get_character_main_skill(),
            character_service.get_character_resources(),
            self._handle_resource_change,
            character_service.get_character_skill_points_left(),
        )

        self._skill_list_view.pack()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._basic_info_frame = ttk.Frame(master=self._frame)
        self._attribute_list_frame = ttk.Frame(master=self._frame)
        self._skill_list_frame = ttk.Frame(master=self._frame)

        self._initialize_basic_info()
        self._initialize_attribute_list()
        self._initialize_skill_list()

        header_label = ttk.Label(
            master=self._frame,
            text="Character sheet",
            font=("", 20)
        )

        #self._root.grid_columnconfigure(1, weight=1)
        header_label.grid(row=0, column=0, columnspan=2,
                          padx=5, pady=5, sticky=constants.W)
        self._basic_info_frame.grid(row=1, column=0)
        self._attribute_list_frame.grid(row=1, column=1)
        self._skill_list_frame.grid(row=2, column=2)
