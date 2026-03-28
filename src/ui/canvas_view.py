import tkinter as tk
from PIL import ImageTk, Image

class CanvasView(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.canvas = None
        self.origin_image = None
        self.view_image = None
        self.view_image_id = None
        self.zoom_num = 1

        # record drag position
        self.pan_start_x = 0
        self.pan_start_y = 0

        self._build()


    def _build(self):
        canvas = tk.Canvas(self, bg="white")
        self.canvas = canvas

        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        canvas.bind("<MouseWheel>",self.on_mousewhell)
        canvas.bind("<Configure>", self.on_resize)
        canvas.bind('<ButtonPress-3>', self.on_pan_start) # right button pressed
        canvas.bind('<B3-Motion>', self.on_pan_move) # right button held + mouse moved

    def on_pan_start(self, event):
        self.pan_start_x = event.x
        self.pan_start_y = event.y
    
    def on_pan_move(self, event):
        cur_x = event.x
        cur_y = event.y
        move_x = cur_x - self.pan_start_x
        move_y = cur_y - self.pan_start_y
        self.canvas.move(self.view_image_id, move_x, move_y)

        self.pan_start_x = cur_x 
        self.pan_start_y = cur_y
    
    def on_resize(self, event):
        self.canvas.coords(self.view_image_id, event.width / 2, event.height / 2)
        
    
    def on_mousewhell(self, event):
        print("MouseWheel")
        if event.delta > 0:
            self.zoom_num += 0.1
        else:
            self.zoom_num -= 0.1
        iw, ih = self.origin_image.size
        new_w = int(iw * self.zoom_num)
        new_h = int(ih * self.zoom_num)
        resized = self.origin_image.resize((new_w, new_h), Image.Resampling.LANCZOS)
        
        self.view_image = ImageTk.PhotoImage(resized)
        self.canvas.itemconfig(self.view_image_id, image=self.view_image)
        
    def load_image(self, image):
        self.origin_image = image
        self.view_image = ImageTk.PhotoImage(self.origin_image)
        
        
        # canvas w h
        # img w h
        cw = self.canvas.winfo_width()
        ch = self.canvas.winfo_height()
        iw,ih = self.origin_image.size

        scale_w = cw * 0.9
        scale_h = ch * 0.9
        self.zoom_num = min(scale_w / iw, scale_h / ih)
        rw, rh = (iw * self.zoom_num, ih * self.zoom_num)
        
        resized = self.origin_image.resize((int(rw), int(rh)), Image.Resampling.LANCZOS)
        self.view_image = ImageTk.PhotoImage(resized)

        # posx = cw + (iw / 2)
        # posy = ch + (ih / 2)

        # print(cw, ch)
        
        self.view_image_id = self.canvas.create_image(cw / 2, ch / 2, image=self.view_image)
