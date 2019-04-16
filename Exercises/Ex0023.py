
#23.
import math
import time
import numpy as np
start = time.process_time()

def divisors_new(n):
    divisors_list = set()
    for i in range(1,int(math.sqrt(n))+1):
        if n % i == 0:
            divisors_list.add(i)
            divisors_list.add(int(n/i))
    divisors_list = list(divisors_list)
    divisors_list.remove(n)
    return divisors_list

def is_abundant(n):
    sumdiv = sum(divisors_new(n))
    if sumdiv > n:
        return True
    return False

abundant = []
maxvalue = 28124

for i in range(1,maxvalue):
    if is_abundant(i):
        abundant.append(i)

print(abundant[0:100])

numbers = np.arange(1, maxvalue)
poss = np.add.outer(abundant, abundant)
poss = poss.reshape(len(abundant) ** 2)
poss = np.array(list(set(poss[poss < maxvalue])))

total = 0
for n in numbers:
    if n not in poss:
        total += n

print(total)       
print("Time taken = %.2f" % (time.process_time()-start))
    