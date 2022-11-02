import string
from perlin_noise import PerlinNoise
from airfoil import *
import math
import pandas as pd
import random
import numpy as np
import matplotlib.pyplot as plt

red1 = np.array((227, 68, 39, 255))
orange1 = np.array((221, 99, 35, 255))
yellow1 = np.array((255, 208, 33, 255))
black1 = np.array((75, 75, 75, 255))
white = np.array((255, 255, 255, 255))
transparent = np.array((255, 255, 255, 0))
eyeblack = np.array((0, 0, 0, 255))

WIDTH = 600
HEIGTH = 600
EYE_WIDTH = 30
EYE_THICKNESS = 12

KOI_THICKNESS_MAX = 0.30
KOI_THICKNESS_MIN = 0.18


class Koi:
    def __init__(self, name : string="Koi", color_layers : list=[red1]):
        self.name = name
        self.thickness = random.uniform(KOI_THICKNESS_MIN, KOI_THICKNESS_MAX)
        x1 = np.linspace(0, WIDTH, WIDTH * 4)
        x2 = np.append(x1, np.flip(x1, 0))
        y1 = naca4_symmetric(self.thickness, WIDTH, x1)
        y2 = np.append(y1, np.flip(-y1, 0))
        y2 = y2 + HEIGTH/2

        self.shape = [x2, y2]
        self.pig_layers = []
        self.seed = []
        self.octave = []
        self.thres = []
        self.filename = ""
        
        for i in range(len(color_layers)):
            self.seed.append(random.randint(1,999999))
            self.octave.append(random.randint(2,8))
            self.thres.append(random.uniform(-0.18, 0.2))
            is_first_layer = False
            if i == 0:
                is_first_layer = True
            self.draw_layer(y1, self.seed[i], self.octave[i], self.thres[i], color_layers[i], is_first_layer)
        
        self.eye = np.empty([WIDTH, HEIGTH, 4], dtype = int)
        self.eye_pos = int(random.uniform(0.075, 0.10) * WIDTH)
        self.draw_eye(y1, self.eye_pos)


    def draw_layer(self, shape : float, seed : int, octave : int, threshold : float,\
             color, first_layer : bool = False):
        noise = PerlinNoise(octaves=octave, seed=seed)
        layer = np.empty([WIDTH, HEIGTH, 4], dtype = int)

        for x in range(WIDTH):
            limit = shape[4*x]
            upper_limit =  limit + HEIGTH/2
            lower_limit = -limit + HEIGTH/2

            for y in range(HEIGTH):
                if y > lower_limit and y < upper_limit:
                    pigment1_intensity = (noise([x/WIDTH, y/HEIGTH]))

                    if pigment1_intensity > threshold:
                        layer[y, x] = color

                    else:
                        if first_layer:
                            layer[y, x] = white
                        else:
                            layer[y, x] = transparent

                else:
                    layer[y, x] = transparent

        self.pig_layers.append(layer)


    def draw_eye(self, shape : float, eye_pos : int):
        layer = np.full([WIDTH, HEIGTH, 4], transparent)

        for i in range(EYE_WIDTH):
            for j in range(int(EYE_THICKNESS * math.sin(math.radians(-75 + 255 * i/EYE_WIDTH)))):
                layer[int(shape[4 * eye_pos + 4 * i] + HEIGTH/2) - j, eye_pos + i] = eyeblack
                layer[-int(shape[4 * eye_pos + 4 * i] + HEIGTH/2) + j, eye_pos + i] = eyeblack

        self.eye = layer


def main():
    color_layer = [red1, orange1]
    fish = Koi("Fea", color_layer.count, color_layer)
    print(fish.eye_pos, fish.thickness)

