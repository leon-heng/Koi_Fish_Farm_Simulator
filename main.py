from tkinter import ANCHOR, NW, Tk, Canvas, PhotoImage, mainloop
import matplotlib.pyplot as plt
from math import sin
from perlin_noise import PerlinNoise
from collections import namedtuple, OrderedDict

width, height = 640, 640
img_width, img_height = 480, 480

Color = namedtuple('RGB','red, green, blue')
colors = {} #dict of colors


def hex_format(r, g, b):
    #'''Returns color in hex format'''
    return '#{:02X}{:02X}{:02X}'.format(r, g, b)

def main():
    window = Tk()
    canvas = Canvas(window, bg="white", height=500, width=500)
    canvas.pack()

    #Empty image
    img = PhotoImage(width=img_width, height=img_height)
    # Perlin noise
    noise = PerlinNoise(octaves=2, seed=12)

    for x in range(img_width):
        for y in range(img_height):
            if int(200 * (noise([x/img_width, y/img_height]))) >= 15:
                img.put("#%02x%02x%02x" % (200, 10, 10), (x, y))
            else:
                img.put("#%02x%02x%02x" % (255, 255, 255), (x, y))


    canvas.create_image((640-480)/2, (640-480)/2, image=img, anchor=NW)
    mainloop()




if __name__== "__main__":
    main()