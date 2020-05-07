import random
import primitive_root
def elgamal_encrypt(m, p, g, a):
    k = 10#random.randint(2, primitive_root.is_primitive_root(g, p)[1])
    K = a ** k
    c_1 = g ** k
    c_2 = K * m
    return k, c_1, c_2

print(elgamal_encrypt(3,53,2,13))

