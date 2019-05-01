
#27.
from time import process_time
import numpy as np
from itertools import product
start = process_time()

def is_prime(n):
    for number in range(2,int(np.sqrt(n)+1)):
        if n % number == 0:
            return False
    return True

a = np.arange(-1001, 101, 2)
b = np.arange(2, 1000, 1)
b_primes = np.array(list(map(is_prime, b)))
b = b[b_primes]

ns = np.arange(0, 79, 1)
full_space = list(product(a, b))
a_space = np.array(full_space)[:, 0]
b_space = np.array(full_space)[:, 1]
new_space = np.array(full_space)[b_space > np.abs(a_space)]

print(len(new_space))
best_value = 0

for a, b in full_space:
    try:
        result = np.array(list(map(lambda n: (n**2) + (a*n) + b, ns)))
        primes = np.array(list(map(is_prime, result)))
        primes_consq = list(primes).index(False)
        if primes_consq > best_value:
            av, bv = a, b
            best_value = primes_consq
    except:
        continue

print(av, bv, av * bv)
print("Time taken = %.2f" % (process_time()-start))