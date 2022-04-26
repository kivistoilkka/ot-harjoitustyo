from tkinter import ttk, constants, filedialog

from services.character_service import character_service
from ui.sheet_components.basic_info_view import BasicInfoView
from ui.sheet_components.talents_equipment_view import TalentsEquipmentView
from ui.sheet_components.attribute_list_view import AttributeListView
from ui.sheet_components.skill_list_resources_view import SkillListResourcesView


class CharacterSheetView:
    def __init__(self, root):
        self._root = root
        self._frame = None
        self._basic_info_frame = None
        self._basic_info_view = None
        self._talents_equipment_frame = None
        self._talents_equipment_view = None
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
        self._initialize_basic_info()

    def _handle_attribute_change(self, attribute, amount, value_label_var, attribute_points_var):
        new_value = character_service.change_character_attribute(
            attribute, amount)
        value_label_var.set(new_value)
        attribute_points_var.set(
            character_service.get_character_attribute_points_left())

    def _handle_resource_change(self, amount, resources_label_var, skill_points_var):
        new_value = character_service.change_character_resources(amount)
        resources_label_var.set(new_value)
        skill_points_var.set(
            character_service.get_character_skill_points_left())

    def _handle_skill_change(self, skill, amount, value_label_var, skill_points_var):
        new_value = character_service.change_character_skill(skill, amount)
        value_label_var.set(new_value)
        skill_points_var.set(
            character_service.get_character_skill_points_left())

    def _handle_talent_change(self, talent_name):
        character_service.give_talent_to_character(talent_name)

    def _handle_equipment_change(self, equipment):
        return character_service.set_character_equipment(equipment)

    def _initialize_basic_info(self):
        if self._basic_info_view:
            self._basic_info_view.destroy()
            self._initialize_attribute_list()
            self._initialize_skill_list()
            self._initialize_talents_equipment()

        self._basic_info_view = BasicInfoView(
            self._basic_info_frame,
            self._handle_basic_info_update
        )

        self._basic_info_view.pack()

    def _initialize_talents_equipment(self):
        if self._talents_equipment_view:
            self._talents_equipment_view.destroy()

        talent_options = character_service.get_talent_options()
        character_talent = character_service.get_character_talents()
        equipment_options = character_service.get_equipment_options()
        character_equipment = character_service.get_character_equipment()

        self._talents_equipment_view = TalentsEquipmentView(
            self._talents_equipment_frame,
            talent_options,
            character_talent,
            self._handle_talent_change,
            equipment_options,
            character_equipment,
            self._handle_equipment_change
        )

        self._talents_equipment_view.pack()

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

        self._skill_list_view = SkillListResourcesView(
            self._attribute_list_frame,
            skills,
            self._handle_skill_change,
            character_service.get_character_main_skill(),
            character_service.get_character_resources(),
            self._handle_resource_change,
            character_service.get_character_skill_points_left(),
        )

        self._skill_list_view.pack()

    def _handle_export(self):
        files = [("Text Document", "*.txt"), ("All files", "*.*")]
        file = filedialog.asksaveasfile(
            filetypes=files, defaultextension=".txt")
        if file:
            character_service.save_character_to_file(file.name)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._basic_info_frame = ttk.Frame(master=self._frame)
        self._talents_equipment_frame = ttk.Frame(master=self._frame)
        self._attribute_list_frame = ttk.Frame(master=self._frame)
        self._skill_list_frame = ttk.Frame(master=self._frame)

        self._initialize_basic_info()
        self._initialize_talents_equipment()
        self._initialize_attribute_list()
        self._initialize_skill_list()

        header_label = ttk.Label(
            master=self._frame,
            text="Character sheet",
            font=("", 20, "bold")
        )

        export_button = ttk.Button(
            master=self._frame,
            text="Export to text file",
            command=self._handle_export
        )

        self._root.grid_columnconfigure(1, weight=1)
        header_label.grid(row=0, column=0, columnspan=2,
                          padx=5, pady=5, sticky=constants.W)
        self._basic_info_frame.grid(
            row=1, column=0, padx=5, pady=5, sticky=constants.NW)
        self._attribute_list_frame.grid(
            row=1, column=1, padx=5, pady=5, sticky=constants.NW)
        self._skill_list_frame.grid(
            row=1, column=3, rowspan=2, padx=5, pady=5, sticky=constants.NW)
        self._talents_equipment_frame.grid(
            row=1, column=2, padx=5, pady=5, sticky=constants.NW)
        export_button.grid(row=1, column=4, padx=5,
                           pady=5, sticky=constants.NW)
