import primitive_root

def elgamal_decrypt(c_1, c_2, p, g, x):

    K = c_1 ** x
    return c_2 * pow(K, -1)


print(elgamal_decrypt(48, 12, 53, 2, 16))