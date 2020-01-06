import numpy as np

def is_square(n):
    sqrt = np.sqrt(n)
    if sqrt == int(sqrt):
        return True
    return False

def fraction_representation(s):
    cf = []
    m = 0
    d = 1
    a = int(np.sqrt(s))    
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

def is_odd(n):
    if n % 2 == 0:
        return False
    return True

if __name__ == '__main__':
    odd_count = 0
    for i in range(2, 10001):
        if is_square(i):
            continue
        fraction_rep = fraction_representation(i)
        periods = fraction_rep[1:]
        if is_odd(len(periods)):
            odd_count += 1

    print(odd_count)