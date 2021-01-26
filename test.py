# -*- coding: UTF-8 -*-
# @Time: 2021/1/22 15:47
from RLWE import Poly_cal, Poly_mod, SK_PK_gen, enc_dec
import numpy as np

d = 16  ###明文密文的长度-多项式长度
t = 5  ###明文系数范围
q = 10240  ###密文系数范围
sigma = 2  ###噪声范围系数
np.random.seed()

#### 生成 私钥sk 公钥pk
sk = SK_PK_gen.sk_gen(d)
pk0, pk1 = SK_PK_gen.pk_gen(sk, d, q, sigma)

#### 明文 随机生成m1 m2
m1 = Poly_mod.coef(np.random.randint(0, t, d), t)
m2 = Poly_mod.coef(np.random.randint(0, t, d), t)
# m1 = np.array([-2, 0, 1, 0, 1, -1, 2, -2, 2, -2, 0, 2, 1, 2, -1, 1])
# m2 = np.array([2, 1, 0, -3, 0, -3, -2, -2, 3, -3, 1, 3, 3, -1, -2, 1])
#### enc
c1_0, c1_1 = enc_dec.enc(pk0, pk1, m1, d, t, q, sigma)
c2_0, c2_1 = enc_dec.enc(pk0, pk1, m2, d, t, q, sigma)

#### dec
dec_m1 = enc_dec.dec(sk, c1_0, c1_1, d, t, q)
dec_m2 = enc_dec.dec(sk, c2_0, c2_1, d, t, q)

# print('--m1--=', m1)
# print('dec_m1=', dec_m1)
# print('--m2--=', m2)
# print('dec_m2=', dec_m2)

if m1.tolist() == dec_m1.tolist():
    print('m1解密正确')
else:
    print('m1解密错误')
if m2.tolist() == dec_m2.tolist():
    print('m2解密正确')
else:
    print('m2解密错误')

#### FHE_add  c1_0 + c2_0, c1_1 + c2_1
m_before = Poly_mod.coef(m1 + m2, t)
m_after = Poly_mod.coef(enc_dec.dec(sk, c1_0 + c2_0, c1_1 + c2_1, d, t, q), t)
# print('明文相加=', m_before)
# print('密文相加=', m_after)
if m_before.tolist() == m_after.tolist():
    print('FHE_add 正确')
else:
    print('FHE_add 错误')

#### FHE_mult (c1_0+c1_1*s)*(c2_0+c2_1*s)
m_before = Poly_mod.coef(Poly_mod.self(Poly_cal.mul(m1, m2), d), t)
a1 = Poly_mod.self(Poly_cal.mul(c1_1, sk), d) + c1_0  ### (c1_0+c1_1*s)
b1 = Poly_mod.self(Poly_cal.mul(c2_1, sk), d) + c2_0  ### (c2_0+c2_1*s)
m_after = Poly_mod.self(Poly_cal.mul(a1, b1), d)
m_after = np.round(m_after * (t / q) * (t / q), 0)
m_after = Poly_mod.coef(m_after, t)
m_after = np.array(m_after, dtype=int)
# print('明文相乘=', m_before)
# print('密文相乘=', m_after)
if m_before.tolist() == m_after.tolist():
    print('FHE_mult 正确')
else:
    print('FHE_mult 错误')
