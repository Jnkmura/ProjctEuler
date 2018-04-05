#16.

num = 2**1000
str_num = str(num)
total = 0

for i in range(len(str_num)):
    total = total + int(str_num[i])

print(total)
    

20.

def sum_factor_n(n):
    mult = 1
    for i in range(1,n+1):
        mult = mult * i
    str_mult = str(mult)
    sum_of_digits = sum([int(str_mult[i]) for i in range(len(str_mult))])
    return sum_of_digits
print(sum_factor_n(100))

    