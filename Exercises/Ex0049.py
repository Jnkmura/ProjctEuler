
#49.
from time import process_time
import numpy as np
from itertools import permutations
start = process_time()

def is_prime(n):
    for number in range(2,int(np.sqrt(n)+1)):
        if n % number == 0:
            return False
    return True

def get_permutations(n):
    permutation = permutations(str(n))
    return list(set(map(lambda x: int(''.join(x)), permutation)))

def get_diff(arr, n):
    diff = []
    for value in arr:
        diff.append(abs(value - n))
    return diff
    
init_n = 1001
max_n = 9999

for i in range(init_n, max_n):
    if is_prime(i):
        permutation = np.array(get_permutations(i))
        primes = np.array(list(map(is_prime, permutation)))
        primes = permutation[primes]
        diff = get_diff(primes, i)
        if len(set(diff)) < len(primes):
            print(i, primes, diff)
    
print("Time taken = %.2f" % (process_time()-start))