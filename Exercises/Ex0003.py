#3.
import time
print(time.ctime())

factor = 600851475143

def is_prime(n):
    count = 0
    for number in range(1,n):
        if n % number == 0:
            count = count + 1
            if count > 1:
                return False
    if count == 1:
        return True

highest_n = 1
factorized = factor

while is_prime(highest_n) != True:
    for i in range(1,factorized,1):
        if factorized % i == 0:
            if is_prime(i):
                highest_n = int(factorized/i)
                factorized = highest_n
                break

print(highest_n)
print(time.ctime())