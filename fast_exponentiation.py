

def fast_exponentiation(a, b, m):
    b_local = b
    remainders = []
    while b_local != 0:
        if b_local % 2 == 0:
            remainders.append(False)
        else:
            remainders.append(True)
        b_local = b_local // 2
    
    arr = []
    rem = a
    for i in range(len(remainders)):
        if i == 0:
            if remainders[0]:
                arr.append(rem)
            continue

        if remainders[i]:
            arr.append((rem ** 2) % m)
        
        rem = (rem ** 2) % m
    
    prod = 1
    for elem in arr:
        prod *= elem
    return prod % m

if __name__ == "__main__":
    print(fast_exponentiation(182, 1175, 3397))
