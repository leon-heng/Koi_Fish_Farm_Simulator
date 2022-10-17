import tkinter as tk
from PIL import ImageTk, Image

class tkKoi:

    def __init__(self, master : tk.Tk, canvas : tk.Canvas, x : int, y : int, image : str):
        self.master = master
        self.canvas = canvas
        temp_image = Image.open(image)
        #temp_image = temp_image.resize((100, 100))
        koi_image = ImageTk.PhotoImage(file=image, master = canvas)
        self.image = self.canvas.create_image(10, 10, image=koi_image)
        self.image2 = canvas.create_oval(10,10,50,50,fill="white")
