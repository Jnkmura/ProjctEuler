
#102.
from time import process_time
import datetime

start = process_time()
year = 1901
total = 0

while year != 2000:

    for month in range(1, 13):
        date = datetime.date(year, month, 1)
        if date.weekday() == 0:
            total += 1

    year += 1

print(total)
print("Time taken = %.2f" % (process_time()-start))