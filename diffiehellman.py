import sys
import random
import fast_exponentiation as fast_exp

if len(sys.argv) != 3:
    print("Usage:")
    print("\tpython diffiehellman.py <p> <g>")
    sys.exit(0)

p = int(sys.argv[1])
g = int(sys.argv[2])

A = random.randint(2, p - 1)
B = random.randint(2, p - 1)
print("A random száma:",A, sep="\t")
print("B random száma:",B, sep="\t")

a = fast_exp.fast_exponentiation(g, A, p)
b = fast_exp.fast_exponentiation(g, B, p)
print("A generált kulcsa:",a, sep="\t")
print("B generált kulcsa:",b, sep="\t")

# Tegyük fel, hogy itt átküldik egymásnak a kulcsot

A_key = fast_exp.fast_exponentiation(b, A, p)
B_key = fast_exp.fast_exponentiation(a, B, p)

print("A kulcsa: ", A_key, sep="\t")
print("B kulcsa: ", B_key, sep="\t")