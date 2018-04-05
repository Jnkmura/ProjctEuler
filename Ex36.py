
#36.
import time
start = time.clock()


def change_to_base10(number,base):
    total = 0
    str_number = str(number)
    digits = len(str_number)
    for digit in range(digits):
        total = total + (int(str_number[digit]) * base**(digits-digit-1))

    return total


def change_base(n1,from_base,to_base):
    base10_number = change_to_base10(n1,from_base)
    if to_base == 10:
        return base10_number, to_base
    value = base10_number
    values = []

    while value != 0:
        remainder = value % to_base
        value = value // to_base
        values.append(remainder)

    new_number = int(''.join(map(str,reversed(values))))
    return new_number, to_base



def palindronic_numbers(n):
    str_number = str(n)
    digits = len(str_number)
    list_number = list(str_number)

    if digits % 2 == 0:
        half = digits // 2
        first_number = int(''.join(map(str,list_number[:half])))
        last_number = int(''.join(map(str,reversed(list_number[half:]))))
    else:
        half = (digits // 2) + 1
        first_number = int(''.join(map(str,list_number[:half])))
        last_number = int(''.join(map(str,reversed(list_number[half-1:]))))

    if first_number == last_number:
        return True
    else:
        return False


limit = 1000000
pn = []
for i in range(1,limit):
    if palindronic_numbers(i):
        if palindronic_numbers(change_base(i,10,2)[0]):
            pn.append(i)



print(sum(pn))
print("Time taken = %.2f" % (time.clock()-start))
