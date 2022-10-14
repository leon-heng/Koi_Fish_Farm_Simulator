from perlin_noise import PerlinNoise
from airfoil import *
import math
import pandas as pd
import random
import numpy as np
import cv2
import matplotlib.pyplot as plt

red1 = np.array((227, 68, 39, 255))
orange1 = np.array((241, 99, 35, 255))
yellow1 = np.array((255, 208, 33, 255))
black1 = np.array((75, 75, 75, 255))
white = np.array((255, 255, 255, 255))
transparent = np.array((255, 255, 255, 0))
eyeblack = np.array((0, 0, 0, 255))

WIDTH = 600
HEIGTH = 600
EYE_WIDTH = 60
EYE_THICKNESS = 25

KOI_THICKNESS_MAX = 0.35
KOI_THICKNESS_MIN = 0.18


def main():
    # Pattern 1 - Perlin noise
    seed1 = random.randint(1,999999)
    octave1 = random.randint(1,6)
    noise1 = PerlinNoise(octaves=octave1, seed=seed1)

    # Pattern 2 - Perlin noise
    seed2 = random.randint(1,999999)
    octave2 = random.randint(1,6)
    noise2 = PerlinNoise(octaves=octave2, seed=seed2)

    eye_x = int(random.uniform(0.035, 0.125)*WIDTH)
    EYE_WIDTH = 22
    EYE_THICKNESS = 10
    threshold = random.uniform(-0.2, 0.3)
    thickness = random.uniform(0.185,0.3)

    x1 = np.linspace(0, WIDTH, WIDTH*4)
    x2 = np.append(x1, np.flip(x1, 0))

    y1 = naca4_symmetric(thickness, WIDTH, x1)
    y2 = np.append(y1, np.flip(-y1, 0))
    y2 = y2 + HEIGTH/2

    eyelayer = np.full([WIDTH, HEIGTH, 4], transparent)
    pig1 = np.empty([WIDTH, HEIGTH, 4], dtype = int)
    pig2 = np.empty([WIDTH, HEIGTH, 4], dtype = int)
    
    for x in range(WIDTH):
        limit = (naca4_symmetric(thickness, WIDTH, x))
        upper_limit =  limit + HEIGTH/2
        lower_limit = -limit + HEIGTH/2

        for y in range(HEIGTH):
            if x == eye_x:
                if y == int(upper_limit):
                    for i in range(EYE_WIDTH):
                        for j in range(int(EYE_THICKNESS*math.sin(math.radians(180*i/EYE_WIDTH)))):
                            temp_limit = naca4_symmetric(thickness, WIDTH, x+i) + HEIGTH/2
                            eyelayer[int(temp_limit) - j, x+i] = eyeblack

                elif y == int(lower_limit):
                    for i in range(EYE_WIDTH):
                        for j in range(int(EYE_THICKNESS*math.sin(math.radians(180*i/EYE_WIDTH)))):
                            temp_limit = -naca4_symmetric(thickness, WIDTH, x+i) + HEIGTH/2
                            eyelayer[int(temp_limit) + j, x+i] = eyeblack
            
            if y > lower_limit and y < upper_limit:
                pigment1_intensity = (noise1([x/WIDTH, y/HEIGTH]))
                pigment2_intensity = (noise2([x/WIDTH, y/HEIGTH]))

                if pigment1_intensity > pigment2_intensity > threshold:
                    pig1[y, x] = orange1
                    pig2[y, x] = transparent

                elif pigment2_intensity > pigment1_intensity > threshold:
                    pig1[y, x] = transparent
                    pig2[y, x] = red1

                else:
                    pig1[y, x] = white
                    pig2[y, x] = transparent

            else:
                pig1[y, x] = transparent
                pig2[y, x] = transparent


    pig1.T
    pig2.T
    eyelayer.T

    koi = plt.figure()
    shape = koi.add_subplot(111)
    shape.plot(x2, y2, 'k-', lw=0.5)
    shape.axis([0, WIDTH, 0, HEIGTH])
    shape.axis('off')
    
    shape.imshow(pig1)
    shape.imshow(pig2)
    shape.imshow(eyelayer)
    plt.show() 
    #koi.savefig("koi.png", transparent=True)

def layering():
    return

if __name__== "__main__":
    main()