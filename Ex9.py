#9.

for ib in range(1,1000):
    for ia in range(1,1000):
        ic = 1000 - ia - ib
        if pow(ia,2) + pow(ib,2) == pow(ic,2) and ib > ia:
            print(ia)
            print(ib)
            print(ic)
