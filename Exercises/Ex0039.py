
#39.
import time
start = time.clock()

a = 0
b = 0
c = 0

perimeter = 1000
i = 1
max_n = 0
max_x = 0

while i < perimeter:
    perimeter_b = 1
    solutions = []
    for a1 in range(1,i):
        for b1 in range(perimeter_b,i):
            c1 = i - a1 - b1
            if c1 ** 2 == a1 ** 2+ b1 ** 2:
                solutions_items = []
                solutions_items.append(a1)
                solutions_items.append(b1)
                solutions_items.append(c1)
                solutions_items = sorted(solutions_items)
                if solutions_items not in solutions:
                    solutions.append(solutions_items)
        perimeter_b = perimeter_b + 1
    if len(solutions) > max_n:
        max_n = len(solutions)
        max_x = i
        def_solutions = solutions
    i = i + 1

                    
print(max_x)
print(def_solutions)
print("Time taken = %.2f" % (time.clock()-start))

