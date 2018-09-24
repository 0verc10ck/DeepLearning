def AND(x1, x2):
    w1, w2, b = 0.5, 0.5, -0.7
    tmp = w1 * x1 + w2 * x2 + b
    if tmp <= 0:
        return 0
    else:
        return 1

def NAND(x1, x2):
    w1, w2, b = -0.5, -0.5, 0.7
    tmp = w1 * x1 + w2 * x2 + b
    if tmp <= 0:
        return 0
    else:
        return 1

def OR(x1, x2):
    w1, w2, b = 0.5, 0.5, -0.2
    tmp = w1 * x1 + w2 * x2 + b
    if tmp <= 0:
        return 0
    else:
        return 1

def XOR(x1, x2):
    s1 = NAND(x1,x2)
    s2 = OR(x1,x2)
    y = AND(s1, s2)
    return y

print(XOR(0,0))
print(XOR(1,0))
print(XOR(0,1))
print(XOR(1,1))