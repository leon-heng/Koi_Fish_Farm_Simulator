from Koi import Koi
from tkKoi import tkKoi
import numpy as np
import tkinter as tk
from main import generate_koi_img, random_location
import pytest

def test_koi():
    given_name = "Jeff"
    layers = (np.array((227, 68, 39, 255)), np.array((75, 75, 75, 255)))
    koi = Koi(given_name, layers)

    assert (koi.name == given_name)
    assert (len(koi.pig_layers) == len(layers))
    assert (len(koi.shape) == 2)
    

def test_angle():
    given_name = "Jeff"
    layers = (np.array((227, 68, 39, 255)), np.array((75, 75, 75, 255)))
    koi = Koi(given_name, layers)
    generate_koi_img(koi)
    window = tk.Tk()
    canvas = tk.Canvas(window, width=1, height=1)
    canvas.pack()
    tk_koi = tkKoi(window, canvas, 1, 1, koi.filename)
    assert (tk_koi.calculate_target_angle(5, 5) == 135.0)
    assert (tk_koi.calculate_target_angle(-5, 5) == 45.0)
    assert (tk_koi.calculate_target_angle(5, -5) == -135.0)
    assert (tk_koi.calculate_target_angle(-5, -5) == -45.0)


def test_random_location():
    assert (len(random_location()) == 2)


if __name__ == "__main__":
    test_koi()
    test_angle()
    test_random_location()
