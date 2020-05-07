import sys
import fast_exponentiation as fast_exp

def primtest(p, a):
    local_a = a
    k = []
    m = []
    i = 1
    m.append((p - 1) // 2)
    k.append(i)
    while m[-1] == (p-1) / (2 ** i):
        i += 1
        m.append((p - 1) // (2 ** i))
        k.append(i)
    print(m)
    print(k)
    d = m[-2]
    S = k[-2]
    print("d =", d)
    print("S =", S)

    result = fast_exp.fast_exponentiation(a, d, p)
    if result in [1, p - 1, -1]:
        return True
    else:
        for i in range(S - 1):
            if fast_exp.fast_exponentiation(result ** 2, (2 ** i) * d, p) in [p - 1, -1]:
                return True
            result = fast_exp.fast_exponentiation(result ** 2, (2 ** i) * d, p)

    return False

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage:")
        print("\tpython primteszt.py <p> <a>")
    else:
        print(primtest(int(sys.argv[1]), int(sys.argv[2]))) 