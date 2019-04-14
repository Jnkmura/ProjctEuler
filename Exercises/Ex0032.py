#32.
from itertools import product, permutations
from time import process_time, sleep
import numpy as np

start = process_time()
pandigital = set()

def is_pandigital(a, b):
    p = a * b
    number_str = str(p) + str(a) + str(b)
    if '0' in number_str:
        return False

    if len(set(list(number_str))) == 9 and len(number_str) == 9:
        return True
    return False

perms = []
for i in range(1, 5):
    perm = np.array(list(permutations('123456789', i)))
    for number in perm:
        perms.append(int(''.join(number)))

result = set()
for i, v1 in enumerate(perms):
    for j in range(i + 1, len(perms)):
        pandigital = is_pandigital(v1, perms[j])
        if pandigital:
            result.add(v1 * perms[j])

print(sum(result))
print("Time taken = %.2f" % (process_time()-start))
