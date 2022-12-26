#  4. Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# in
# 5
# out
# [5.16, 8.62, 6.57, 7.92, 9.22]
# Min: 0.16, Max: 0.92. Difference: 0.76

from random import uniform
def diff(n) :
    

    rnd_list = []
    for i in list(range(n)):
        num = round(uniform(0, 9), 2)
        i+= 1
        rnd_list.append(num)

    print(rnd_list)

    new_list = [round(i % 1, 2) for i in rnd_list if i % 1 != 0]
    print(max(new_list) - min(new_list))
    return ''
print(diff(n = int(input('введите размер списка: '))))