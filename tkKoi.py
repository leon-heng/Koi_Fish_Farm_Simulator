import math
import tkinter as tk
from PIL import ImageTk, Image

class tkKoi:

    def __init__(self, master : tk.Tk, canvas : tk.Canvas, x : int, y : int, image : str):
        self.master = master
        self.canvas = canvas
        self.temp_image = Image.open(image)
        self.temp_image = self.temp_image.resize((150, 150))

        self.koi_image = ImageTk.PhotoImage(self.temp_image, master = self.master)
        self.image = self.canvas.create_image(x, y, image=self.koi_image)

        self.velocity = -1.0
        self.angle = 0.0


    def move(self, destination : tuple):
        self.angle += 1
        self.angle %= 360
        x, y = self.canvas.coords(self.image)
        x -= 2*math.sin(math.radians(90 + self.angle))
        y -= 2*math.cos(math.radians(90 + self.angle))


        self.koi_image = ImageTk.PhotoImage(self.temp_image.rotate(self.angle), master = self.master)
        self.image = self.canvas.create_image(x, y, image=self.koi_image)
        


        

