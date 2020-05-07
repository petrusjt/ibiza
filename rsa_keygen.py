import sys
from exteuclid import gcd, extended_euclid

if len(sys.argv) != 3:
    print("Usage:")
    print("\tpython rsa_keygen.py <p> <q>")
    sys.exit(0)

p = int(sys.argv[1])
q = int(sys.argv[2])

n = p * q
print("n =", n)

phi_n = (p - 1)*(q - 1)
print("phi(n) =", phi_n)

e = 3
while gcd(phi_n, e) != 1:
    e += 2

d = extended_euclid(e, phi_n)[1]

while d < 0:
    d += phi_n

print("Nyilvános kulcs: (",n,",",e,")")
print("Titkos kulcs: (",p,",",q,",",phi_n,",",d,")")
