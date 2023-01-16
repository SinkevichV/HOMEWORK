# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв". В тексте используется разделитель пробел.
# in
# Number of words: 10

# out
# авб абв бав абв вба бав вба абв абв абв
# авб бав вба бав вба

# in
# Number of words: 6

# out
# ваб вба абв ваб бва абв
# ваб вба ваб бва

from random import sample

def spisok(count, word = 'абв'):
    my_list = []
      
    for i in range(count):
        temp = sample(word, k=3)
        my_list.append(''.join(temp))
        string = str(' '.join(my_list))
    print(string)
    return my_list    
    

def string_filt(my_list):
    new_list = []
    new_list = list(filter(lambda e: not e == 'абв', my_list))
    string_new = str(' '.join(new_list))
    print(string_new)


string_filt(spisok(int(input())))
