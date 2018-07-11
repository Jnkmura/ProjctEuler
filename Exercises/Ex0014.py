#14.

import time

print(time.ctime())

def odd_even(n):
    if n % 2 == 0:
        ni = n/2
    else:
        ni = 3*n + 1
    return ni

final_point = 1000000
max_len = 0
i = 2
dicti = {1:1}

while i < final_point:
    collatz_list = []
    collatz_list.append(i)

    while collatz_list[-1] != 1:
        new_value = collatz_list[-1]
        is_odd_even = odd_even(new_value)
        if is_odd_even in dicti:
            leni = len(collatz_list) + dicti[is_odd_even]
            break
        else:
            collatz_list.append(int(is_odd_even))
            leni = len(collatz_list)

    dicti[i] = leni

    if leni > max_len:
        max_len = leni
        value_to_remember = i

    i = i + 1

print(max_len)
print(value_to_remember)
print(time.ctime())

        