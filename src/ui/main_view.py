from tkinter import ttk, constants


class MainView:
    def __init__(self, root):
        self._root = root
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        header_label = ttk.Label(
            master=self._frame,
            text="Vaesen Character App",
            background=self._root["bg"],
            font=("", 20)
        )
        introduction_label = ttk.Label(
            master=self._frame,
            text="Character generator for Vaesen: Nordic Horror Roleplaying game",
            background=self._root["bg"]
        )

        header_label.grid(row=0, column=0, padx=5, pady=5)
        introduction_label.grid(row=1, column=0, padx=5, pady=5)
