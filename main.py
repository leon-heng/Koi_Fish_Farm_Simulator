from turtle import width
from perlin_noise import PerlinNoise
from airfoil import *
import pandas as pd
import random
import numpy as np
import cv2
import matplotlib.pyplot as plt

red1 = np.array((227, 68, 39, 255))
orange1 = np.array((241, 99, 35, 255))
yellow1 = np.array((255, 208, 33, 255))
black1 = np.array((65, 65, 65, 255))
white = np.array((255, 255, 255, 255))
transparent = np.array((255, 255, 255, 0))
eyeblack = np.array((0, 0, 0, 255))

def main():
    width = 1280
    height = 1280

    # Pattern 1 - Perlin noise
    seed1 = random.randint(1,999999)
    octave1 = random.randint(1,6)
    noise1 = PerlinNoise(octaves=octave1, seed=seed1)

    # Pattern 2 - Perlin noise
    seed2 = random.randint(1,999999)
    octave2 = random.randint(1,6)
    noise2 = PerlinNoise(octaves=octave2, seed=seed2)

    eye_x = int(random.uniform(0.05, 0.15)*width)
    print(eye_x)

    threshold = random.uniform(-0.3, 0.3)
    thickness = random.uniform(0.185,0.355)

    x1 = np.linspace(0, width, width*4)
    x2 = np.append(x1, np.flip(x1, 0))

    y1 = naca4_symmetric(thickness, width, x1)
    y2 = np.append(y1, np.flip(-y1, 0))
    y2 = y2 + height/2

    #eyelayer = np.empty([height, width, 4], dtype = int)
    eyelayer = np.full([height, width, 4], transparent)
    #eyelayer.fill(transparent)
    pig1 = np.empty([height, width, 4], dtype = int)
    pig2 = np.empty([height, width, 4], dtype = int)
    
    for x in range(width):
        limit = (naca4_symmetric(thickness, width, x))
        upper_limit =  limit + height/2
        lower_limit = -limit + height/2

        for y in range(height):
            if x == eye_x:
                if y == int(upper_limit):
                    for i in range(15):
                        for j in range(10):
                            eyelayer[int(naca4_symmetric(thickness, width, x+i))-j, x+i] = eyeblack

                elif y == int(lower_limit):
                    for i in range(15):
                        for j in range(10):
                            eyelayer[int(naca4_symmetric(thickness, width, x+i))+j, x+i] = eyeblack
            
            if y > lower_limit and y < upper_limit:
                pigment1_intensity = (noise1([x/width, y/height]))
                pigment2_intensity = (noise2([x/width, y/height]))

                if pigment1_intensity > pigment2_intensity > threshold:
                    pig1[y, x] = black1
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
    shape.plot(x2, y2, 'k-', linewidth=0.5)
    shape.axis([0, width, 0, height])
    #shape.axis('off')
    
    #shape.imshow(pig1)
    #shape.imshow(pig2)
    shape.imshow(eyelayer)
    plt.show() 
    #koi.savefig("koi.png", transparent=True)

if __name__== "__main__":
    main()