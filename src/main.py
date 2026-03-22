import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class Application(tk.Frame):
  def __init__(self, master: tk.Tk=None):

    # design image
    self.design_image = None
    self.canvas = None
    
    tk.Frame.__init__(self, master)
    
    self.pack(fill=tk.BOTH, expand=True)
    self.create_left()
    self.create_right()

    

  def create_left(self):
    left_frame = tk.Frame(self, bg="lightblue", width=200)
    left_frame.pack(side=tk.LEFT, fill=tk.Y)

    # create btn of open-image
    
    open_file_btn = tk.Button(left_frame, text="Open Image",command=self.open_image)
    open_file_btn.pack(side=tk.TOP, pady=12)
    
  def open_image(self):
    path = filedialog.askopenfilename(
      filetypes=[("Image files", "*.png")]
    )
    
    if not path:
      return 

    image = tk.PhotoImage(file=path)
    self.design_image = image
    self.canvas.create_image(0, 0, image=self.design_image)

    # self.design_image = ImageTk.PhotoImage

  def create_right(self):
    canvas = tk.Canvas(self, bg="white", width=400, height=400)
    canvas.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
    self.canvas = canvas
    
    # right_frame = tk.Frame(self, bg="white",)
    # right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

app = Application()

app.master.title('Simple application')
app.master.geometry("800x600")
app.mainloop()