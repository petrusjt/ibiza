import fast_exponentiation as fast_exp

def rsa_decrypt(c, d, n):
    return fast_exp.fast_exponentiation(c, d, n)

"""
    Használat(a gyakorló feladatok alapján):
    python -i rsa_decrypt.py

    A python shellbe:
        n = p*q
        rsa_decrypt(c, d, n)
        ahol p, q, c, d és e a feladatban megadott értékek
"""