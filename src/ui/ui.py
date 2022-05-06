from tkinter import Menu, filedialog
from ui.character_sheet_view import CharacterSheetView
from ui.main_view import MainView
from ui.character_creation_view import CharacterCreationView

from services.character_service import character_service


class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None
        self._filemenu = None
        self._set_visual_settings()
        self._set_toplevel_menu()

    def start(self):
        self._show_main_view()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()
        self._current_view = None

    def _show_main_view(self):
        self._hide_current_view()
        self._disable_saving_exporting()
        self._current_view = MainView(
            self._root
        )
        self._current_view.pack()

    def _show_char_creation_view(self):
        self._hide_current_view()
        self._disable_saving_exporting()
        self._current_view = CharacterCreationView(
            self._root,
            self._handle_char_modifying
        )
        self._current_view.pack()

    def _show_char_sheet_view(self):
        self._hide_current_view()
        self._enable_saving_exporting()
        self._current_view = CharacterSheetView(
            self._root
        )
        self._current_view.pack()

    def _enable_saving_exporting(self):
        self._filemenu.entryconfig("Save character as...", state="normal")
        self._filemenu.entryconfig("Export to text file", state="normal")

    def _disable_saving_exporting(self):
        self._filemenu.entryconfig("Save character as...", state="disabled")
        self._filemenu.entryconfig("Export to text file", state="disabled")

    def _handle_char_creation(self):
        self._show_char_creation_view()

    def _handle_char_modifying(self):
        self._show_char_sheet_view()

    def _handle_open(self):
        files = [("JSON", "*.json"), ("All files", "*.*")]
        file = filedialog.askopenfilename(filetypes=files)
        if file:
            character_service.load_character_from_file(file)
            self._handle_char_modifying()

    def _handle_save(self):
        files = [("JSON", "*.json"), ("All files", "*.*")]
        file = filedialog.asksaveasfile(
            filetypes=files, defaultextension=".json")
        if file:
            character_service.save_character_to_file(file.name)

    def _handle_export(self):
        files = [("Text Document", "*.txt"), ("All files", "*.*")]
        file = filedialog.asksaveasfile(
            filetypes=files, defaultextension=".txt")
        if file:
            character_service.export_character_to_file(file.name)

    def _handle_exit(self):
        self._root.destroy()

    def _set_toplevel_menu(self):
        menubar = Menu(self._root)
        self._root.config(menu=menubar)

        self._filemenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=self._filemenu)
        self._filemenu.add_command(label="Create new character",
                                   command=self._show_char_creation_view)
        self._filemenu.add_command(label="Open existing character",
                                   command=self._handle_open)
        self._filemenu.add_command(label="Close current character",
                                   command=self._show_main_view)
        self._filemenu.add_separator()
        self._filemenu.add_command(label="Save character as...",
                                   command=self._handle_save, state="disabled")
        self._filemenu.add_separator()
        self._filemenu.add_command(label="Export to text file",
                                   command=self._handle_export, state="disabled")
        self._filemenu.add_separator()
        self._filemenu.add_command(label="Exit", command=self._handle_exit)

    def _set_visual_settings(self):
        self._root.geometry("1200x900")
        self._root["bg"] = "#f3e7c6"
