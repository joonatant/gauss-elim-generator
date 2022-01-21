import math
#määritelmät tupplejen laskutoimituksille
def div(a, b):
    return multiply(a, (b[1], b[0]))

def add(a, b):
    n = math.lcm(a[1], b[1])
    am = n/a[1]
    bm = n/b[1]
    return simplify_tuple((round(am*a[0] + bm*b[0]), n))
        
def multiply(a, b):
    return simplify_tuple((a[0]*b[0], a[1]*b[1]))

def tuple_abs(a):
    return abs(a[0]/a[1])

def simplify_tuple(a):
    res = a
    if(res[0] == 0):
        res = (0, 1)
    else:
        k = math.gcd(res[0], res[1])
        if(k > 1):
            res = (round(res[0]/k), round(res[1]/k))
        if (a[0] < 0 and a[1] < 0):
            res =(-res[0], -res[1])
    return res