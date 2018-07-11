
#48.
s = []
final_value = 1000

for i in range(1,final_value+1):
	s.append(i**i)
	print(i)

sumtotal = sum(s)
sumtotal_str = str(sumtotal)
last_ten = sumtotal_str[-10:]

print(last_ten)

