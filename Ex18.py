

#18.
import time
start = time.clock()

path_numbers = '''
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''


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
