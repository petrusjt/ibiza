import sys

def gcd(a, b):
    if a == b:
        return a
    if b < a:
        a, b = b, a
    while (0 < a):
        a, b = b % a, a
    return b


def extended_euclid(a, b):
    s = [1,0]
    t = [0,1]
    q = []
    r = [a,b]

    while r[-1] != 0:
        q.append(r[-2] // r[-1])
        r.append(r[-2] - q[-1] * r[-1])
        s.append(s[-2] - q[-1] * s[-1])
        t.append(t[-2] - q[-1] * t[-1])
        if __name__ == "__main__":
            print(q,r,s,t)
        result = s[-2]
        if result < 0:
            result += b
    return r[-2], s[-2], t[-2], result

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage:\n\tpython exteuclid.py <method> <a> <b>\n\n\tmethod can be: gcd or ext\n\ta and b are two (positive) integers")
    elif sys.argv[1] == "gcd":
        print(gcd(int(sys.argv[2]), int(sys.argv[3])))
    elif sys.argv[1] == "ext":
        print(extended_euclid(int(sys.argv[2]), int(sys.argv[3])))