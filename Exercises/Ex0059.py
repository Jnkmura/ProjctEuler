
#59.
from time import process_time
from itertools import product
import urllib.request
import numpy as np

start = process_time()
link = 'https://projecteuler.net/project/resources/p059_cipher.txt'
f = urllib.request.urlopen(link)
text = list(f.read().decode('utf-8').split(','))
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'z', 'w', 'y']

def decrypt(text, key):
    new_text = []
    total = 0
    for i, char in enumerate(text):
        sub_key = ord(key[i % len(key)])
        xor = int(char) ^ sub_key
        new_char = chr(xor)

        new_text.append(
            new_char
        )

        total += xor
    
    return "".join(new_text), total

keys = list(product(letters, letters, letters))

for key in keys:
    new_text, total = decrypt(text, key)
    if 'the ' in new_text:
        if new_text.split(' ').count('the') > 1:
            print(key)
            print(new_text)
            print(total)


print("Time taken = %.2f" % (process_time()-start))