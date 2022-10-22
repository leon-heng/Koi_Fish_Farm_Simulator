from concurrent.futures import thread
import tkinter as tk
from airfoil import *
import numpy as np
import time
from Koi import Koi
from tkKoi import tkKoi
from queue import Empty, Queue
from threading import Thread

red1 = np.array((227, 68, 39, 255))
orange1 = np.array((241, 99, 35, 255))
yellow1 = np.array((255, 208, 33, 255))
black1 = np.array((75, 75, 75, 255))
white = np.array((255, 255, 255, 255))
transparent = np.array((255, 255, 255, 0))
eyeblack = np.array((0, 0, 0, 255))

WIDTH = 800
HEIGHT = 800
MARGIN = 50

queue = Queue(maxsize=1)

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
    t = Thread(target=new_location, args=(np.random.randint(2,4),))
    new_location(0)

    while True:

        if queue.empty():
            if not t.is_alive():
                t = None
                t = Thread(target=new_location, args=(np.random.randint(2,12),))
                t.start()
        else:
            new_loc = queue.get()
            print(new_loc)

        tk_fish1.move(new_loc)
        window.update()
        time.sleep(0.01)

    window.mainloop()


def new_location(delay : int):
    x = np.random.randint(MARGIN, WIDTH - MARGIN)
    y = np.random.randint(MARGIN, HEIGHT - MARGIN)
    time.sleep(delay)
    queue.put([x, y])


if __name__== "__main__":
    main()