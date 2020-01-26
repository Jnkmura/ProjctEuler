import numpy as np 

basic_nums = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
}

tenths = {
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety'
}
   
def get_tenths(n):
    str_n = str(n)
    unit = int(str_n[-1])
    residual = n - unit
    return unit, residual

def get_hundreds(n):
    str_n = str(n)
    first_number = int(str_n[0])
    residual =  n - (first_number * 100)
    return first_number, residual

def form_words(n, text):
    str_n = str(n)
    n_size = len(str_n)

    if n in basic_nums:
        text += ' ' + basic_nums[n]
        return text.strip()

    if n in tenths:
        text += ' ' + tenths[n]
        return text.strip()

    if n_size == 2:       
        unit, residual = get_tenths(n)
        text += ' ' + tenths[residual]
        return form_words(unit, text)
    
    if n_size == 3:
        first_n, residual = get_hundreds(n)
        text += basic_nums[first_n] + ' hundred'
        if residual == 0:
            return text.strip()
        text += ' and'
        return form_words(residual, text)

    if n_size == 4:
        return 'one thousand'

def get_word_len(word):
    return len(''.join(word.split(' ')))

letters = 0
for i in range(1, 1001):
    number_word = form_words(i, '')
    words_len = get_word_len(number_word)
    letters += words_len

print(letters)
    

    