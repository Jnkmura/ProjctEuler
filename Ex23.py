
#23.
import math
import time
start = time.clock()

def divisors_new(n):
    import math
    divisors_list = []
    for i in range(1,int(math.sqrt(n))+1):
        if n % i == 0:
            divisors_list.append(i)
            divisors_list.append(int(n/i))
    divisors_list.remove(max(divisors_list))
    return divisors_list

def is_abundant(n):
    sumdiv = sum(divisors_new(n))
    if sumdiv > n:
        return True
    else:
        return False

abundant = []
nabundant = []
maxavalue = 10000

for i in range(1,maxavalue):
    if is_abundant(i) == True:
        abundant.append(i)
    else:
        nabundant.append(i)

i = len(abundant)
for i1 in abundant:
    for i2 in range(len(abundant[0:i])):
        total = i1 + abundant[-(1+i2)]
        if total in nabundant:
            nabundant.remove(total)
        i = i - 1
    i = len(abundant)

       
print(sum(nabundant))
print("Time taken = %.2f" % (time.clock()-start))
    