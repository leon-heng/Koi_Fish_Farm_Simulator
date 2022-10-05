from tkinter import ANCHOR, NW, Tk, Canvas, PhotoImage, mainloop
import matplotlib.pyplot as plt
from math import sin
from perlin_noise import PerlinNoise
from collections import namedtuple, OrderedDict
from airfoil import *
import random

width, height = 640, 640
img_width, img_height = 540, 540

Color = namedtuple('RGB','red, green, blue')
colors = {} #dict of colors


def hex_format(r, g, b):
    #'''Returns color in hex format'''
    return '#{:02X}{:02X}{:02X}'.format(r, g, b)

def main():
    window = Tk()
    canvas = Canvas(window, bg="white", height=height, width=width)
    canvas.pack()

    #Empty image
    img = PhotoImage(width=img_width, height=img_height)
    # Pattern 1 - Perlin noise
    seed1 = random.randint(1,999999)
    octave1 = random.randint(1,6)
    noise1 = PerlinNoise(octaves=octave1, seed=seed1)

    # Pattern 2 - Perlin noise
    seed2 = random.randint(1,999999)
    octave2 = random.randint(1,6)
    noise2 = PerlinNoise(octaves=octave2, seed=seed2)

    threshold = random.randint(10,35)
    thickness = random.uniform(0.185,0.355)

    for x in range(img_width+1):
        limit = (naca4_symmetric(thickness, img_width, x))
        upper_limit =  limit + img_height/2
        lower_limit = -limit + img_height/2

        if x == img_width :
            upper_limit = img_height/2
            lower_limit = upper_limit

        for y in range(img_height+1):

            if y < upper_limit and y > lower_limit:
                pigment1_intensity = int(200 * (noise1([x/img_width, y/img_height])))
                pigment2_intensity = int(200 * (noise2([x/img_width, y/img_height])))

                if pigment1_intensity >= pigment2_intensity and pigment1_intensity >= threshold:
                    img.put("#%02x%02x%02x" % (200, 10, 10), (x, y))
                elif pigment2_intensity >= pigment1_intensity and pigment2_intensity >= threshold:
                    img.put("#%02x%02x%02x" % (55, 55, 55), (x, y))
                else:
                    img.put("#%02x%02x%02x" % (255, 255, 255), (x, y))

            if y == int(upper_limit) or y == int(lower_limit):
                img.put("#%02x%02x%02x" % (0, 0, 0), (x, y))


    canvas.create_image((width-img_width)/2, (height-img_height)/2, image=img, anchor=NW)
    mainloop()


if __name__== "__main__":
    main()