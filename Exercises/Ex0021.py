#21.

import math
import time
print(time.ctime())

def is_prime(n):
    import math
    count = 0
    if n == 2:
        return True
    for number in range(1,int(math.sqrt(n)+1),2):
        if n % number == 0:
            count = count + 1
            if count > 1:
                return False
    if count == 1:
        return True

def divisor(n):
    factors = [1]
    factorized = n
    while factorized != 1:
        for numbers in range(2,int(factorized + 1)):
            if factorized % numbers == 0:
                if is_prime(numbers) == True:
                    factors.append(numbers)
                    factorized = factorized/numbers
                    break
    return factors

def combinations(l):
    import numpy as np
    new_arr = np.array(l)
    total_n = np.prod(new_arr)
    new_list = []
    while total_n != 1:
        for factors in l:
            if total_n % factors == 0:
                factor = total_n/factors
                if int(factor) not in new_list and factor >= 1:
                    new_list.append(int(factor))
        for number in reversed(sorted(new_list)):
            if number < total_n:
                total_n = number
                break
    return new_list[1:]

def amicables(x1,x2):
    div1 = divisor(x1)
    div2 = divisor(x2)
    if sum(combinations(div1)) == x2 and sum(combinations(div2)) == x1:
        return True
    else:
        return False

amicable = []
amidict = {}
maxi = 10000

for i in range(1,maxi+1):
    divisors = divisor(i)
    sumcombi = sum(combinations(divisors))
    amidict[i] = sumcombi

for i in range(1,maxi+1):
    find1 = amidict[i]
    try:
        find2 = amidict[find1]
        if i == find2 and i != find1:
            amicable.append(i)
    except:
        continue

print(sum(amicable))
