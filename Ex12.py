

#12.
import math
import time

print(time.ctime())

def n_of_divisors(n):
    count = 2
    for number in range(2,int((n/2)+1)):
        if n % number == 0:
            count += 1

    return count

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
    return len(new_list)


        
triang_numbers = [1]
seq_number = 50000
seq_in_code = seq_number + 1
target = 500

for i in range(2,seq_in_code):
    maxn = max(triang_numbers)
    triang_numbers.append(maxn+i)
    
    div_counts = combinations(divisor(maxn+i))
    
    if div_counts >= target:
        print(maxn+i)
        break

print(time.ctime())