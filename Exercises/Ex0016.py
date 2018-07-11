#16.

num = 2**1000
str_num = str(num)
total = 0

for i in range(len(str_num)):
    total = total + int(str_num[i])

print(total)
    

    