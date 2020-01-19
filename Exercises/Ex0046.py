import numpy as np 

PRIMES = []

def is_prime(n):
    if n in [2, 3]:
        return True
    for number in range(3,int(np.sqrt(n)+1),2):
        if n % number == 0:
            return False
    return True

def odd_numbers_generator(n):
    for i in range(3, n, 2):
        if is_prime(i):
            PRIMES.append(i)
            continue
        yield i
        
def goldbach_conjecture(n):
    primes_less_than_n = np.array(PRIMES) < n
    primes = np.array(PRIMES)[primes_less_than_n]

    for prime in primes:
        sq = np.sqrt((n - prime)/2)
        if sq == int(sq):
            return True
    return False

if __name__ == '__main__':
    odd_numbers = odd_numbers_generator(10000)

    for o in odd_numbers:
        is_goldbach = goldbach_conjecture(o)
        if not is_goldbach:
            print(o)
            break