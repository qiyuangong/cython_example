# File: StdDev.py

import math
import numpy as np

def pyStdDev(a):
    mean = sum(a) / len(a)
    return math.sqrt((sum(((x - mean)**2 for x in a)) / len(a)))

def npStdDev(a):
    return np.std(a)
