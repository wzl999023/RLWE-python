# -*- coding: UTF-8 -*-
# @Time: 2021/1/20 16:34
import numpy as np


# class Poly_cal(object):

def add(a, b):
    a = a.tolist()
    b = b.tolist()
    diff = [0] * abs(len(a) - len(b))
    if len(a) >= len(b):
        b = diff + b
    else:
        a = diff + a
    a = np.array(a)
    b = np.array(b)
    return a + b


def minus(a, b):
    b = b * (-1)
    return add(a, b)


def mul(a, b):
    c = [0] * ((len(a) - 1) + (len(b) - 1) + 1)
    c = np.array(c)
    for i in range(len(a)):
        for j in range(len(b)):
            c[i + j] = c[i + j] + a[i] * b[j]
    return c
