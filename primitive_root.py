import sys

abelian_rank = 0

def is_primitive_root(root, modulo):
    remainders = []
    for i in range(1, modulo + 1):
        if i == 1:
            remainders.append(root % modulo)
        else:
            remainders.append((root * remainders[-1]) % modulo)        
        if __name__ == "__main__":
            print(str(root)+"^"+str(i), "=", root ** i, u"\u2263", str(i)+ " " + u"\u2A09 " + str(root),"=",i * 3, u"\u2263",remainders[-1],"(mod " + str(modulo) + ")", sep="\t")
        
    return modulo - 1 == len(list(dict.fromkeys(remainders))), len(list(dict.fromkeys(remainders)))

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage:")
        print("\tpython primitive_root.py <root> <modulo>")
    else:
        print(is_primitive_root(int(sys.argv[1]), int(sys.argv[2])))
