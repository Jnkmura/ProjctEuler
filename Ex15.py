

#15.

import numpy as np
import random

rows = 1
columns = 1
ar = (rows+1,columns+1)

ar_matrix = np.zeros(ar,int)

combinations = []
count = 0

while count < 5000:
    temp_row = 0
    temp_column = 0
    ar_matrix[0,0] = 1
    while ar_matrix[rows,columns] != 1:
        randomint = random.randint(0,1)
        if randomint == 0:
            try:
                ar_matrix[temp_row+1,temp_column] = 1
                temp_row = temp_row + 1
                temp_column = temp_column
            except:
                continue
        if randomint == 1:
            try:
                ar_matrix[temp_row,temp_column+1] = 1
                temp_row = temp_row
                temp_column = temp_column+1
            except:
                continue
    ar_list = ar_matrix.tolist()
    if ar_list not in combinations:
        combinations.append(ar_list)
    ar_matrix = np.zeros(ar,int)
    count = count + 1


combinations = np.array(combinations)
print(len(combinations))




rows = 20
columns = 20
ar = (rows+1,columns+1)
ar_matrix = np.zeros(ar,dtype='int64')

for row in range(1,rows+1):
    i = 0
    ar_matrix[row,i] = row + 1
    i = i + 1
    while i != row:
        if ar_matrix[row-1,i] == 0:
            ar_matrix[row,i] = abs(ar_matrix[row,i-1]*2)
            break
        else:
            ar_matrix[row,i] = ar_matrix[row,i-1] + ar_matrix[row-1,i]
        i = i + 1

print(ar_matrix.max())