#22.
import csv
import time
start = time.clock()
f = open('names.txt','r')
reader = csv.reader(f)
names = []

for i in reader:
    for name in i:
        names.append(name)

names = sorted(names)
dictalpha = {}
alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L',
            'M','N','O','P','Q','R','S','T','U','V','W','X','Y',
            'Z']
letter_value = 1
for letters in alphabet:
    dictalpha[letters] = letter_value
    letter_value = letter_value + 1

scores = []
def namescore(name):
    name_score = 0
    for letters in range(len(name)):
        name_score = name_score + dictalpha[name[letters]]
    return name_score

for i, name in enumerate(names):
    total_score = 0
    total_score = namescore(name) * (i + 1)
    scores.append(total_score)
print(sum(scores))
print("Time taken = %.2f" % (time.clock()-start))