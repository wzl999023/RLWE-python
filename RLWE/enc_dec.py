# -*- coding: UTF-8 -*-
# @Time: 2021/1/22 15:52
from RLWE import Poly_cal, Poly_mod
import numpy as np


### pk0=-a*s+e mod x^d+1 ; q
### ct0=pk0*u+e1+q/t*m mod x^d+1 ; q = e1+e*u-a*u*s+q/t*m 在这个表达式中，前两项是“小”的，与噪音成比例，后两项是“大”的。第一个大项有效地掩盖了第二个大项，即消息。
### ct1=pk1*u+e2 mod x^d+1 ; q = a*u+e2 这说明了解密是如何工作的——如果我们知道s，就可以计算出ct1s = [aus + e2s]q，它可以用来消除密文的第一个元素中的非消息大项。
def enc(pk0, pk1, m, d, t, q,sigma):
    e1 = np.array(np.random.normal(0, sigma, d), dtype=int)
    e2 = np.array(np.random.normal(0, sigma, d), dtype=int)
    u = np.array(np.random.normal(0, sigma, d), dtype=int)
    ct0 = Poly_mod.coef(Poly_mod.self(Poly_cal.mul(pk0, u), d) + e1 + (q / t) * m, q)
    ct1 = Poly_mod.coef(Poly_mod.self(Poly_cal.mul(pk1, u), d) + e2, q)
    return ct0, ct1


### ct0 + ct1*s=e1+e*u-a*u*s+q/t*m+a*u*s+e2*s=e1+e*u+e2*s+q/t*m ; m=(ct0 + ct1*s)/(q/t)
def dec(sk, ct0, ct1, d, t, q):
    m = Poly_mod.coef(Poly_mod.self(Poly_cal.mul(ct1, sk), d) + ct0, q)
    m = np.round(m / (q / t), 0)
    m = np.array(m, dtype=int)
    return m



