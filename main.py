import tkinter as tk
from PIL import ImageTk
from PIL import Image
from perlin_noise import PerlinNoise
from airfoil import *
import math
import pandas as pd
import random
import numpy as np
import matplotlib.pyplot as plt
import time
from Koi import Koi
from tkKoi import tkKoi

red1 = np.array((227, 68, 39, 255))
orange1 = np.array((241, 99, 35, 255))
yellow1 = np.array((255, 208, 33, 255))
black1 = np.array((75, 75, 75, 255))
white = np.array((255, 255, 255, 255))
transparent = np.array((255, 255, 255, 0))
eyeblack = np.array((0, 0, 0, 255))

def main():
    fish1 = Koi()
    # color_layers = [orange1, black1]
    # fish2 = Koi("Fae", color_layers)

    window = tk.Tk()
    WIDTH = 500
    HEIGHT = 500
    canvas =  tk.Canvas(window, width=WIDTH, height=HEIGHT)
    canvas.pack()

    tk_fish1 = tkKoi(window, canvas, 250, 250, fish1.filename)
    
    window.mainloop()



class SimpleApp(object):
    def __init__(self, master, filename, **kwargs):
        self.master = master
        self.filename = filename
        self.canvas = tk.Canvas(master, width=1000, height=1000)
        self.canvas.pack()

        self.update = self.movement().__next__
        master.after(100, self.update)

    def movement(self):
        image = Image.open(self.filename)
        image = image.resize((256, 256))

        angle = 0
        x = 250
        y = 100

        while True:
            
            koi_image = ImageTk.PhotoImage(image.rotate(angle))
            canvas_obj = self.canvas.create_image(x, y, image=koi_image)
            self.canvas.move(canvas_obj, x, y)
            self.master.after_idle(self.update)

            yield
            self.canvas.delete(canvas_obj)
            angle += 0.5
            angle %= 360
            x -= 1.5*math.sin(math.radians(90 + angle))
            y -= 1.5*math.cos(math.radians(90 + angle))
            time.sleep(0.005)




if __name__== "__main__":
    main()