
#42.
import time
import urllib.request
start = time.clock()

import math
alphabet = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}

def word_score(word):
    letter_list = list(word)
    total = 0
    for letter in letter_list:
        total = total + alphabet[letter]
    return total

def triangule_numbers(total):
    triang = (-1 + math.sqrt(1+(8*total)))/2
    if triang == int(triang):
        return True
    else:
        False

link = 'https://projecteuler.net/project/resources/p042_words.txt'
f = urllib.request.urlopen(link)
words = f.read().decode('utf-8')
words = words.split(',')
words_list = []

for word in words:
    word = word.replace('\"','')
    words_list.append(word)

triangule_words = []

for word in words_list:
    if triangule_numbers(word_score(word)):
        triangule_words.append(word)

print(len(triangule_words))
print("Time taken = %.2f" % (time.clock()-start))