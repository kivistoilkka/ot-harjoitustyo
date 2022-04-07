from tkinter import ttk, constants

class MainView:
    def __init__(self, root, handle_char_creation):
        self._root = root
        self._handle_char_creation = handle_char_creation
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)
    
    def destroy(self):
        self._frame.destroy()
    
    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, text="Welcome to Vaesen Character App!")

        char_create_button = ttk.Button(
            master=self._frame,
            text="Create new character",
            command=self._handle_char_creation
        )

        label.grid(row=0, column=0)
        char_create_button.grid(row=1, column=0)