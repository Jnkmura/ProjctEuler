
#5.
import time
print(time.ctime())

def number_evenly_divisible(n):
    if n <= 0:
        return False
    for number in range(11,20+1):
        if n % number != 0:
            return False
    return True

smallest_number = 0

while number_evenly_divisible(smallest_number) != True:
    smallest_number = smallest_number + 20

print(time.ctime())
print(smallest_number)
    