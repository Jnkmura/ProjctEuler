
#60.
from time import process_time
import numpy as np
from itertools import product
start = process_time()

def is_prime(n):
    for number in range(2,int(np.sqrt(n)+1)):
        if n % number == 0:
            return False
    return True

def pair_prime(vec):
    p1 = int(str(vec[0]) + str(vec[1]))
    p2 = int(str(vec[1]) + str(vec[0]))
    if is_prime(p1) and is_prime(p2):
        return True
    return False
    
numbers = np.arange(2, 1000, 1)
primes = numbers[list(map(is_prime, numbers))]
prod = np.array(list(product(primes, primes)))

pair_primes = list(map(pair_prime, prod))
pair_primes = prod[pair_primes]

pairs = dict()
for p1, p2 in pair_primes:
    if p1 in pairs:
        pairs[p1].append(p2)
    else:
        pairs[p1] = [p1, p2]

candidates = []
for p1, v1 in pairs.items():
    for p2, v2 in pairs.items():
        intersec = list(set(v1).intersection(set(v2)))
        if len(intersec) == 4:
            candidates.append(intersec)

candidates = np.array(candidates)
print(sorted(np.sum(candidates, axis = 1)))

print("Time taken = %.2f" % (process_time()-start))