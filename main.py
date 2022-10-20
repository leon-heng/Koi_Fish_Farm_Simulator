import tkinter as tk
from airfoil import *
import numpy as np
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

WIDTH = 1500
HEIGHT = 1500

def main():
    fish1 = Koi()

    color_layers2 = [orange1, black1]
    fish2 = Koi("Fae", color_layers2)
    
    color_layers3=[red1, orange1]
    fish3 = Koi("Kuri", color_layers3)

    color_layers4=[red1, black1]
    fish4 = Koi("Leo", color_layers4)

    window = tk.Tk()
    canvas =  tk.Canvas(window, width=WIDTH, height=HEIGHT)
    canvas.pack()

    tk_fish1 = tkKoi(window, canvas, 550, 550, fish1.filename)
    x, y = generate_new_location()

    while True:
        if not tk_fish1.reached_destination():
            if not tk_fish1.has_target:
                x, y = generate_new_location()
            tk_fish1.move([x, y])

        window.update()
        time.sleep(0.01)

    window.mainloop()

def generate_new_location():
    target_x = np.random.randint(100, WIDTH - 100)
    target_y = np.random.randint(100, HEIGHT - 100)
    return (target_x, target_y)

if __name__== "__main__":
    main()