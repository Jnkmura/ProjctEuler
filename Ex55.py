#55.

import time
start = time.clock()


def reverse_and_add(n):
	n_str = str(n)
	num_order = list(n_str)
	num_reverse = list(reversed(num_order))
	num_1 = int(''.join(num_order))
	num_2 = int(''.join(num_reverse))
	total = num_1 + num_2 
	return total

def islychrel(n):
	aux = 0
	strn = str(n)
	if len(strn) % 2 != 0:
		aux = 1
	halfn = int(len(strn) / 2)
	first_str = strn[0:halfn + aux]
	last_str = strn[halfn:]
	first_str_list = list(first_str)
	last_str_list = list(last_str)
	last_str_list = list(reversed(last_str_list))
	if last_str_list == first_str_list:
		return False
	else:
		return  True


def try_until_lychrel(n,tries):
	i = 0
	result = 0
	number = n
	while i != tries:
		number = reverse_and_add(number)
		is_ly = islychrel(number)
		if is_ly == False:
			return 0
		else:
			i = i + 1
	if i == tries:
		result = n
		return result
		

total_numbers = 10000
lychrel = []

for i in range(total_numbers):
	if try_until_lychrel(i,50) != 0:
		lychrel.append(i)


print(len(lychrel))

print("Time taken = %.2f" % (time.clock()-start))