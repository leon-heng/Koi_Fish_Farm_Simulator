import Koi
import tkKoi
from main import add_koi, random_location
import numpy as np
import pytest

def test_koi():
    koi = Koi("Jeff", np.array(227,33,233,255))
    