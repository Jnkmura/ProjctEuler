import numpy as np
import math

def is_square(n):
    sqrt = np.sqrt(n)
    if sqrt == int(sqrt):
        return True
    return False

def fraction_representation(s):
    cf = []
    m = 0
    d = 1
    a = int(math.sqrt(s))    
    a0 = a
    if a0 * a0 == s:
        return [a0]
    
    while a != 2 * a0:
        cf.append(a)
        m = (d * a) - m
        d = (s - (m * m)) // d
        a = (a0 + m) // d
    cf.append(a)
    return cf

def check_pells_equation(D, hn, kn):
    equation = (hn ** 2) - (D * (kn ** 2))
    if equation == 1:
        return True
    return False

def get_fundamental_solution(D):
    fraction_rep = fraction_representation(D)

    hn_m2, hn_m1 = 0, 1
    kn_m2, kn_m1 = 1, 0
    idx = 0

    while True:
        a = fraction_rep[idx]
        hn = (a * hn_m1) + hn_m2
        kn = (a * kn_m1) + kn_m2

        if check_pells_equation(D, hn, kn):
            return hn, kn

        hn_m2, hn_m1 = hn_m1, hn
        kn_m2, kn_m1 = kn_m1, kn

        idx += 1
        if idx == len(fraction_rep):
            idx = 1

    return None, None

if __name__ == '__main__':
    highest = 0
    answer_D = None

    for D in range(2, 1001):
        if is_square(D):
            continue
        x, y = get_fundamental_solution(D)
        if x > highest:
            highest = x
            answer_D = D
    
    print(answer_D)