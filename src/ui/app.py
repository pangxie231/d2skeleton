import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

from ui.left_panel import LeftPanel
from ui.canvas_view import CanvasView


class Application(tk.Frame):
    def __init__(self, master: tk.Tk = None):

        tk.Frame.__init__(self, master)

        self.pack(fill=tk.BOTH, expand=True)

        # left
        left = LeftPanel(self, self.open_image)
        left.pack(side=tk.LEFT, fill=tk.Y)

        # right
        self.canvas_view = CanvasView(self)
        self.canvas_view.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    def open_image(self):
        path = filedialog.askopenfilename(filetypes=[("Image files", "*.png")])
        if not path:
            return

        image = Image.open(path)
        self.canvas_view.load_image(image)

