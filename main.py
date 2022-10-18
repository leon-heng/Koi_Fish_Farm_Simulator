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

def main():
    fish1 = Koi()

    color_layers2 = [orange1, black1]
    fish2 = Koi("Fae", color_layers2)
    
    color_layers3=[red1, orange1]
    fish3 = Koi("Kuri", color_layers3)

    color_layers4=[red1, black1]
    fish4 = Koi("Leo", color_layers4)

    

    window = tk.Tk()
    WIDTH = 500
    HEIGHT = 500
    canvas =  tk.Canvas(window, width=WIDTH, height=HEIGHT)
    canvas.pack()

    tk_fish1 = tkKoi(window, canvas, 250, 250, fish1.filename)
    tk_fish2 = tkKoi(window, canvas, 199, 70, fish2.filename)
    tk_fish3 = tkKoi(window, canvas, 125, 189, fish3.filename)
    tk_fish4 = tkKoi(window, canvas, 100, 120, fish4.filename)

    
    while True:
        tk_fish1.move([1,1])
        tk_fish2.move([1,1])
        tk_fish3.move([1,1])
        tk_fish4.move([1,1])

        window.update()
        time.sleep(0.01)

    window.mainloop()


if __name__== "__main__":
    main()