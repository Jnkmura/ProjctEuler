
#29.
from time import process_time
import numpy as np

start = process_time()

numbers = set()
for a in range(2, 101):
    for b in range(2, 101):
        numbers.add(a ** b)

print(len(numbers))
print("Time taken = %.2f" % (process_time()-start))