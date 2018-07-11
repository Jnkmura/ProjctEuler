
#53.

import time
start = time.clock()

def fatorial(n):

	if n == 0:
		return 1
	total = 1
	for i in range(n,0,-1):
		total = total * i
	return total

def comb(n,r):
	combinatory = fatorial(n) / (fatorial(r) * fatorial(n-r))
	return combinatory

one_million = []

for n in range(1,101):
	for r in range(1,n+1):
		combs = comb(n,r)
		if combs >= 1000000:
			one_million.append(combs)

print(len(one_million))
print("Time taken = %.2f" % (time.clock()-start))
