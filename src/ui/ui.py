from ui.main_view import MainView
from ui.character_creation_view import CharacterCreationView

class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None
    
    def start(self):
        self._show_main_view()
    
    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()
        self._current_view = None
    
    def _show_main_view(self):
        self._current_view = MainView(
            self._root,
            self._handle_char_creation
        )

        self._current_view.pack()

    def _handle_char_creation(self):
        self._show_char_creation_view()
    
    def _show_char_creation_view(self):
        self._hide_current_view()

        self._current_view = CharacterCreationView(
            self._root
        )

        self._current_view.pack()

