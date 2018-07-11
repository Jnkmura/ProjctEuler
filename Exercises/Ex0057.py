
#57.

import time
start = time.clock()

interactions_results = []
total = 0

def fraction_sum_by_1(numerator, denominator):
    new_numerator = numerator + denominator
    new_denominator = denominator
    return new_numerator, new_denominator

def squatetwo_interactions(n, list):
    if n == 1:
        interactions_results.append((3,2))
    if n == 2:
        interactions_results.append((7,5))

    last_numerator = interactions_results[-1][0]
    last_denominator = interactions_results[-1][1]
    result = fraction_sum_by_1(last_numerator,last_denominator)
    result = fraction_sum_by_1(result[1],result[0])
    interactions_results.append(result)
    return interactions_results

for i in range(1,1001):
    squatetwo_interactions(i,interactions_results)

for fractions in interactions_results:
    if len(str(fractions[0])) > len(str(fractions[1])):
        total = total + 1

print(total)
print("Time taken = %.2f" % (time.clock()-start))
