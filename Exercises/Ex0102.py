
#102.
from time import process_time
import urllib.request
import numpy as np

start = process_time()
link = 'https://projecteuler.net/project/resources/p102_triangles.txt'
f = urllib.request.urlopen(link)
triangules = np.array(f.read().decode('utf-8').split('\n'))

def inside_vector(a, b, c, p):
    if np.dot(np.cross(b-a, p-a), np.cross(b-a, c-a)) >= 0:
        return True 
    return False

def point_in_triangule(a, b, c, p):
    if inside_vector(a, b, c, p) and inside_vector(b, c, a, p) and inside_vector(c, a, b, p):
        return True
    return False

total_triangules = 0
for t in triangules:
    t = np.fromstring(t, dtype = np.int, sep =',')
    if len(t) < 6:
        continue
    a, b, c = t[0:2], t[2:4], t[4:6]
    result = point_in_triangule(a, b, c, [0,0])
    if result:
        total_triangules += 1

print(total_triangules)
print("Time taken = %.2f" % (process_time()-start))