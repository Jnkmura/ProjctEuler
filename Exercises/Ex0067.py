
#67.
import time
import urllib.request
start = time.clock()

link = 'https://projecteuler.net/project/resources/p067_triangle.txt'
f = urllib.request.urlopen(link)
path_numbers = f.read().decode('utf-8')

row_numbers = []
path_rows = path_numbers.split('\n')
for row in path_rows:
    temp_list = []
    try:
        numbers = row.split(' ')
        for n in numbers:
            temp_list.append(int(n))
        row_numbers.append(temp_list)
    except:
        row_numbers.append(row)

row_numbers.remove('')
lenn = len(row_numbers)-1
new_path = row_numbers
row = 0

while len(row_numbers) != 2:
    temp_list = []
    last_row = row_numbers[lenn-row]
    pre_last_row = row_numbers[lenn-row-1]
    for i in range(len(pre_last_row)):
        i1 = pre_last_row[i] + last_row[i]
        i2 = pre_last_row[i] + last_row[i+1]

        if i1 > i2:
            temp_list.append(i1)
        else:
            temp_list.append(i2)
    new_path.remove(last_row)
    new_path.remove(pre_last_row)
    new_path.append(temp_list)
    print(new_path)
    row = row + 1

print("Time taken = %.2f" % (time.clock()-start))