import tkinter as tk


class LeftPanel(tk.Frame):
    def __init__(self, master, on_open):
        super().__init__(master, bg="lightblue", width=200)
        self.on_open = on_open

        self._build()

    def _build(self):
        open_file_btn = tk.Button(self, text="Open Image", command=self.on_open)
        open_file_btn.pack(side=tk.TOP, pady=12)

        # left_frame = tk.Frame(self, bg="lightblue", width=200)
        # left_frame.pack(side=tk.LEFT, fill=tk.Y)

        # # create btn of open-image
