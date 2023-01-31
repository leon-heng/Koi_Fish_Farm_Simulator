from asyncio.windows_events import NULL
from concurrent.futures import thread
import tkinter as tk
from airfoil import *
import numpy as np
import time
from Koi import Koi
from tkKoi import tkKoi
from queue import Empty, Queue
from threading import Thread
from multiprocessing import Process, JoinableQueue 
import matplotlib.pyplot as plt
import sys


red1 = np.array((227, 68, 39, 255))
orange1 = np.array((241, 99, 35, 255))
yellow1 = np.array((255, 208, 33, 255))
black1 = np.array((75, 75, 75, 255))
white = np.array((255, 255, 255, 255))
transparent = np.array((255, 255, 255, 0))
eyeblack = np.array((0, 0, 0, 255))

color_list = [
    red1,    
    orange1,
    yellow1,
    black1
    ]

WIDTH = 900
HEIGHT = 900
MARGIN = 50

thrd = []
queue = []
t = []
fish = []
tk_fish = []
new_loc = []

number_of_koi = 40
number_of_process = 20
dev_mode = 0

def main():

    if len(sys.argv) == 3:
        try:
            dev_mode = int(sys.argv[2])
            if dev_mode < 0 or dev_mode > 2:
                dev_mode = 0
                print("Please enter a valid interger number")
        except:
            print("Please enter a valid interger number")

        try:
            nkois = int(sys.argv[1])
        except:
            print("Please enter a valid interger number")

    elif len(sys.argv) == 2:
        dev_mode = 0
        try:
            nkois = int(sys.argv[1])
        except:
            print("Please enter a valid interger number")

    else:
        dev_mode = 0
        nkois = number_of_koi

    start = time.time()
    q_input = JoinableQueue()
    q_output = JoinableQueue()

    koi_number = np.random.randint(1,11)
    for i in range(number_of_process):
        thrd.append(Process(target=consumer_kois, args=(q_input, q_output, i)))
        thrd[i].daemon = True
        thrd[i].start()
    
    generate_kois(nkois, q_input, q_output)
    q_input.join()

    while q_output.qsize() != nkois:
        if dev_mode: print(str(q_output.qsize()))
        continue
    if dev_mode: print(f"Patterns generation completed in {round(time.time() - start,2)}s")

    if dev_mode: print("Start image generation")
    for i in range(q_output.qsize()):
        koi = q_output.get()
        fish.append(koi)
        generate_koi_img(koi)
    if dev_mode: print(f"Total {len(fish)} fishes generated in {round(time.time() - start,2)}s")
    if dev_mode: print(round(time.time() - start,2))

    window = tk.Tk()
    window.title("Koi Farm")
    canvas = tk.Canvas(window, width=WIDTH, height=HEIGHT, bg='skyblue')
    canvas.pack()

    for i in range(len(fish)):
        x, y = random_location()
        tk_fish.append(tkKoi(window, canvas, x, y, fish[i].filename))
        t.append(Thread(target=new_location, args=(np.random.randint(2,4),)))
        queue.append(Queue(maxsize=1))
        new_location(i, 0)
        new_loc.append(None)

    while True:
        for i in range(len(fish)):
            if queue[i].empty():
                if not t[i].is_alive():
                    t[i] = None
                    t[i] = Thread(target=new_location, args=(i,np.random.randint(2,12),))
                    t[i].daemon = True
                    t[i].start()

            else:
                new_loc[i] = queue[i].get()

            tk_fish[i].move(new_loc[i])

        window.update()
        time.sleep(0.01)

    window.mainloop()


def generate_kois(n : int, q_input : JoinableQueue, q_output : JoinableQueue):
    for i in range(n):
        color_num = np.random.randint(1,4)
        layer = None
        layer = []
        for j in range(3):
            layer.append(color_list[np.random.randint(0,4)])

        q_input.put([i, layer])


def consumer_kois(q_input : JoinableQueue, q_output : JoinableQueue, n : int):
    if dev_mode: print("Process " + str(n+1) + " Starts")
    while True:
        i, layer = q_input.get()
        if dev_mode: print(str(n+1) + " Working on koi "+ str(i+1))
        koi = Koi(("Koi_"+ str(i + 1)), layer)
        if dev_mode: print("Done " + koi.name)
        q_output.put(koi)
        q_input.task_done()


def generate_koi_img(koi : Koi):
    # path = os.path.abspath(__file__)
    full_path = "koi_folder/" + koi.name + ".png"
    image = plt.figure()
    layers = image.add_subplot(111)
    layers.plot(koi.shape[0], koi.shape[1], 'k-', lw=0.5)
    layers.axis([0, 600, 0, 600])
    layers.axis('off')

    for pigment in koi.pig_layers:
        layers.imshow(pigment)
    layers.imshow(koi.eye)
    image.savefig(full_path, transparent=True, format = 'png')
    koi.filename = full_path
    image.clf()
    plt.close()


def new_location(q_index : int, delay : int):
    time.sleep(delay)
    queue[q_index].put(random_location())


def random_location():
    x = np.random.randint(MARGIN, WIDTH - MARGIN)
    y = np.random.randint(MARGIN, HEIGHT - MARGIN)
    if dev_mode == 2: print(x, y)
    return [x, y]


if __name__== "__main__":
    main()