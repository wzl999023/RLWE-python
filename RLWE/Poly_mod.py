# -*- coding: UTF-8 -*-
# @Time: 2021/1/21 10:03
import numpy as np


def coef(a, t):  ##### mod t
    a = a % t
    for i in range(len(a)):
        # if np.floor(-t/2)<a[i]<=np.floor(t/2):
        #     a[i]=a[i]
        if a[i] > np.floor(t / 2):
            a[i] = a[i] - t
    return a


def self(a, d):  #### mod x^d+1
    c = [0] * d
    c = np.array(c)
    for i in range(len(a)):
        c[-1 * (i % d + 1)] = c[-1 * (i % d + 1)] + a[-1] * ((-1) ** (i // d))
        a = np.delete(a, -1)
    return c
