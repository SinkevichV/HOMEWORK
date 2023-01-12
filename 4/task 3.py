# 3. Задайте последовательность чисел. Напишите программу, которая выведет список 
# неповторяющихся элементов исходной последовательности в том же порядке.
# in
# 7

# out
# [4, 5, 3, 3, 4, 1, 2]
# [5, 1, 2]

# in
# -1

# out
# Negative value of the number of numbers!
# []

# in
# 10

# out
# [4, 4, 5, 5, 6, 2, 3, 0, 9, 4]
# [6, 2, 3, 0, 9]
def listnonrecurring ():
    lst = list(map(int, input("Введите числа через пробел:\n").split()))
    print(f"Исходный список: {lst}")
    new_lst = []       
    [new_lst.append(i) for i in lst if i not in new_lst]
            
    print(f"Список из неповторяющихся элементов: {new_lst}")
listnonrecurring ()