
#10.
import math
import time

print(time.ctime())
def is_prime(n):
    count = 0
    if n == 2:
        return True
    for number in range(1,int(math.sqrt(n)+1),2):
        if n % number == 0:
            count = count + 1
            if count > 1:
                return False
    if count == 1:
        return True
            
count = 3
sump = 2

while count < 2000000:
    if is_prime(count):
        sump = sump + count
    count = count + 2

print(sump)
print(time.ctime())
