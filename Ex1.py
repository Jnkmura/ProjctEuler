#1.
total_number = []
for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        total_number.append(i)
answer = sum(total_number)
print(answer)
