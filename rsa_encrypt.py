import fast_exponentiation as fast_exp

def rsa_encrypt(m, e, n):
    return fast_exp.fast_exponentiation(m, e, n)

"""
    Használat(a gyakorló feladatok alapján):
    python -i rsa_encrypt.py

    A python shellbe:
        rsa_encrypt(m, e, n)
        ahol m, n és e a feladatban megadott értékek
"""