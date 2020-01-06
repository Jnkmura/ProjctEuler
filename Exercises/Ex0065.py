import numpy as np

def get_fundamental_solution(cf):
    hn_m2, hn_m1 = 0, 1
    kn_m2, kn_m1 = 1, 0

    for a in cf:
        hn = (a * hn_m1) + hn_m2
        kn = (a * kn_m1) + kn_m2

        hn_m2, hn_m1 = hn_m1, hn
        kn_m2, kn_m1 = kn_m1, kn

    return hn, kn

if __name__ == '__main__':
    cf_e = [2, 1, 2, 1]
    for _ in range(100):
        cf_e += list(np.add(cf_e[-3:], [0, 2, 0]))

    cf_e = cf_e[0:100]
    cf_e = map(int, cf_e)

    numerator, denominator = get_fundamental_solution(cf_e)
    print(numerator)
    print(sum(list(map(int, list(str(numerator))))))