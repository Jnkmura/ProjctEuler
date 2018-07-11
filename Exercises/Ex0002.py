#2.
max_number = 4000000
fib_numbers = [1,2]

while fib_numbers[-1] < max_number:
    sum_of_last_two = fib_numbers[-1] + fib_numbers[-2]
    fib_numbers.append(sum_of_last_two)

total_even = 0
for i in fib_numbers[:-1]:
    if i % 2 == 0:
        total_even = total_even + i

print(fib_numbers[:-1])
print(total_even)
