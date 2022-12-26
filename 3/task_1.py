# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
# in
# 5

# out
# [10, 2, 3, 8, 9]
# 22

# in
# 4

# out
# [4, 2, 4, 9]
# 8


from random import sample

def num_summ (len_list):
    summ = 0
    i = 0
    new_list = sample (range (10), k=len_list)
    print(new_list)
    while i < len(new_list):
        summ = summ + new_list[i]
        i= i + 2
    else:
        print('сумма нечетных позиций списка = ' , summ)

print (num_summ (int (input('Введите длину списка :'))))