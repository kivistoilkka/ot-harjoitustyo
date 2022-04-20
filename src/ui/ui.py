from tkinter import Menu
from ui.character_sheet_view import CharacterSheetView
from ui.main_view import MainView
from ui.character_creation_view import CharacterCreationView


class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None
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
        self._current_view = MainView(
            self._root
        )
        self._current_view.pack()

    def _handle_char_creation(self):
        self._show_char_creation_view()

    def _show_char_creation_view(self):
        self._hide_current_view()
        self._current_view = CharacterCreationView(
            self._root,
            self._handle_char_modifying
        )
        self._current_view.pack()

    def _handle_char_modifying(self):
        self._show_char_sheet_view()

    def _show_char_sheet_view(self):
        self._hide_current_view()
        self._current_view = CharacterSheetView(
            self._root
        )
        self._current_view.pack()

    def _handle_exit(self):
        self._root.destroy()

    def _set_toplevel_menu(self):
        menubar = Menu(self._root)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Create new character",
                             command=self._show_char_creation_view)
        filemenu.add_command(label="Close current character",
                             command=self._show_main_view)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self._handle_exit)
        menubar.add_cascade(label="File", menu=filemenu)

        self._root.config(menu=menubar)

    def _set_visual_settings(self):
        self._root.geometry("800x900")
        self._root["bg"] = "#f3e7c6"
