
#4.
first_number = 100
second_number = 100
last_number = 999

list_of_palindrome = []

for i1 in range(first_number,last_number+1):
    for i2 in range(second_number,last_number+1):
        mult = str(i1 * i2)
        if len(mult) % 2 == 0:
            number_of_digits = len(mult)
            half_of_digits = number_of_digits//2
            count = 0

            for digits in range(half_of_digits):
                if mult[digits] == mult[number_of_digits -1 - digits]:
                    count = count + 1
                else:
                    break

            if count == half_of_digits:
                list_of_palindrome.append(mult)

print(max(list_of_palindrome))

