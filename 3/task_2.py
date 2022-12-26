# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# in
# 4

# out
# [2, 5, 8, 10]
# [20, 40]

# in
# 5

# out
# [2, 2, 4, 8, 8]
# [16, 16, 4]

from random import sample

def num_multi (len_list):
    multi = 0
    i = 0
    multi_list = []
    new_list = sample (range (10), k=len_list)
    print(new_list)
    if len_list % 2 == 0 :
        while i < len_list / 2 :
            multi = new_list[i] * new_list[len_list - 1 - i]
            i+=1
            multi_list.append(multi)
        print('произведение парных позиций списка = ' , multi_list)  
    else:
        while i < len_list / 2 - 0.5 :
            multi = new_list[i] * new_list[len_list - 1 - i]
            i+=1
            multi_list.append(multi)
        a = int(len_list / 2 + 0.5)
        print('произведение парных позиций списка = ' , multi_list + [new_list[a - 1]])
    return (len_list)
print (num_multi (int (input('Введите длину списка :'))))