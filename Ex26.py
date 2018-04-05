
#26.
import time
import collections
from decimal import Decimal
import math
start = time.clock()

def cycles_number(n):
    combinations = []
    result = 1 % n
    combinations.append(result)
    remainder = 0
    while True:
        remainder = (10*result) % n
        if remainder in combinations:
            break
        else:
            combinations.append(remainder)
        result = remainder
    return len(combinations), combinations

#print(cycles_number(975))

total = 0
for i in range(1,1001):
    try:
        len_value = cycles_number(i)[0]
        i_value = i
    except:
        len_value = 0
    if len_value > total:
        total = len_value
        cycle = i_value
    
print(cycle)

print("Time taken = %.2f" % (time.clock()-start))