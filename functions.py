import numpy as np


def multi_brot(z, c, n=2):
    return np.power(z, n) + c


def cos(z, c):
    return np.cos(z) + c


def cosh(z, c):
    return np.cosh(z) + c


def exp(z, c):
    return np.exp(z) + c


def poly2(z, c):
    return z**2 + z + c


def poly3(z, c):
    return z**3 + z**2 + z + c
