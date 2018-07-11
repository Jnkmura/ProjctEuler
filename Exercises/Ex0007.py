
#7.
import time
import math

print(time.ctime())
def is_prime(n):
    count = 0
    for number in range(1,int(math.sqrt(n)+1)):
        if n % number == 0:
            count = count + 1
            if count > 1:
                return False
    if count == 1:
        return True

prime = 3
number_prime = 1
prm = 0

while number_prime != 10001:
    if is_prime(prime):
        prm = prime
        number_prime = number_prime + 1
    prime = prime + 2

print(prm)
print(time.ctime())