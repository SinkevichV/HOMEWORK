# ** 5. Реализуйте алгоритм перемешивания списка.
# Без функции shuffle из модуля random.
# 10
# -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# -> [0, 7, 6, 3, 4, 2, 9, 5, 1, 8]


from random import sample
num_list = list(range(int(input("Введите число N: "))))
a = int(len(num_list))
print(num_list)
nums = range(a)
num_listsecond = sample(nums, len(nums))
print(num_listsecond)

    