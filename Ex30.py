#30.

def power(n,p):
    str_n = str(n)
    sumt = 0
    for i in range(len(str_n)):
        sumt = sumt + (int(str_n[i]) ** p)
    return sumt
    
fifth_n = 2
last_n = 9999999
powerl = []

while fifth_n != last_n:
    if power(fifth_n,5) == fifth_n:
        powerl.append(fifth_n)
    fifth_n += 1
    
print(sum(powerl))