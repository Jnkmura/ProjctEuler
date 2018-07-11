
#40
n = '12345678910'
i = 11
last_n = 1000000

while i < last_n:
    n = n+str(i)
    i = i + 1

digits = []
dx = [1,10,100,1000,10000,100000,1000000]
mult = 1
for digit in range(len(n)):
    if digit + 1 in dx:
        mult = mult * int(n[digit])
        print(n[digit])

print(mult)