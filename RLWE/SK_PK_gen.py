# -*- coding: UTF-8 -*-
# @Time: 2021/1/21 17:04
from RLWE import Poly_cal, Poly_mod
import numpy as np


# d = 16
# t = 7
# q = 896

def sk_gen(d):  ###  d-长度
    sk = np.random.randint(-1, 2, d)  ### 私钥
    return sk


def pk_gen(sk, d, q,sigma):  ###  d-长度  q-系数mod
    # s = np.random.randint(-1, 2, (1, d))  ### 私钥
    pk1 = np.random.randint(0, q, d)   ###用于生成公钥
    pk1 = Poly_mod.coef(pk1, q)             ###用于生成公钥
    e = np.array(np.random.normal(0, sigma, d),dtype=int)     ###噪声多项式
    ##### pk-gen   pk0=-a*s+e mod x^d+1 ; q   (a=pk1  s=sk)
    pk0 = Poly_mod.coef(Poly_mod.self(Poly_cal.mul(-1 * pk1, sk), d) + e, q)

    return pk0,pk1
