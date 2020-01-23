import numpy as np 
from tqdm import tqdm

def is_prime(n):
    if n in [2, 3]:
        return True
    if n % 2 == 0:
        return False
    for number in range(3,int(np.sqrt(n)+1),2):
        if n % number == 0:
            return False
    return True

def get_primes_factors(n):
    primes_less_than_n = np.array(PRIMES) < n
    primes = np.array(PRIMES)[primes_less_than_n]
    prime_factors = []
    residual = n
    for prime in primes:
        if n % prime == 0:
            residual = residual / prime
            prime_factors.append(prime)
            if residual == 1:
                break
    return prime_factors

if __name__ == '__main__':
    sequence = []
    factors_obj = 4
    last_seq = 0
    seq_added = False

    PRIMES = [2]
    for i in range(3, 1000, 2):
        if is_prime(i):
            PRIMES.append(i)

    for i in tqdm(range(2, 200000)):
        seq_added = False
        factors = get_primes_factors(i)
        if len(set(factors)) == factors_obj and (
                (i == last_seq + 1) or (last_seq == 0)):
            sequence.append(i)
            last_seq = i
            seq_added = True

        if seq_added == False:
            if len(sequence) == factors_obj:
                print(sequence)
                break
            sequence = []
            last_seq = 0

