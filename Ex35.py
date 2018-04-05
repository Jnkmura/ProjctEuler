
#35.
import time
start = time.clock()
def is_prime(n):
    import math
    count = 0
    if n == 2:
        return True
    for number in range(1,int(math.sqrt(n)+1)):
        if n % number == 0:
            count = count + 1
            if count > 1:
                return False
    if count == 1:
        return True


def permutations_primes(n,primes):
    if len(str(n)) == 1:
        return True
    str_n = str(n)
    k = []
    for i in range(len(str_n)):
        rotation = str_n[0:i]
        new_n = str_n[i:]+rotation
        if int(new_n) not in primes:
            return False
    return True


max_n = 1000000
primes = [2]
for i in range(3,max_n,2):
    str_i = str(i)
    if '2' not in str_i:
        if '4' not in str_i:
            if '6' not in str_i:
                if '8' not in str_i:
                    if '5' not in str_i:
                        if is_prime(i) == True:
                            primes.append(i)

circular_primes_count = 0
for prime in primes:
    if permutations_primes(prime,primes) == True:
        circular_primes_count = circular_primes_count + 1
        
print(circular_primes_count)
print("Time taken = %.2f" % (time.clock()-start))
    