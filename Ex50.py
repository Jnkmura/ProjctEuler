
#50.
import math
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
    
max_number = 1000000

maxprimes = []

primes = [2]
for i in range(3,max_number,2):
    if is_prime(i) == True:
        primes.append(i)

n = 0
maxcount = 0
num = math.sqrt(len(primes)) + 1
while n < num:
    totalsum = 0
    tempsum = 0
    count = 0
    tempcount = 0
    for prime in sorted(primes[n:]):
        tempsum = tempsum + prime
        if tempsum > max_number:
            break
        count += 1
        if tempsum in primes:
            tempcount = count
            totalsum = tempsum
    if tempcount > maxcount:
        maxcount = tempcount
        maxprimes.append(totalsum)
    n = n + 1
    
print(max(maxprimes))
print(maxcount)
    

