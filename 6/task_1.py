# 1. Представлен список чисел. Необходимо вывести элементы исходного списка, 
# значения которых больше предыдущего элемента. Use comprehension.
# in
# 9

# out
# [15, 16, 2, 3, 1, 7, 5, 4, 10]
# [16, 3, 7, 10]

# in
# 10

# out
# [28, 20, 10, 5, 1, 24, 7, 15, 23, 25]
# [24, 15, 23, 25]

from random import *

def list_num(nums):
    n = int(input())
    nums = [randint(1, 9) for i in range(n)]
    print(nums)
    return nums

def sequence(nums):
    
    new_list = [nums[i+1] for i in range(len(nums) - 1) if nums[i] < nums[i+1]]
    print(new_list)


sequence(list_num(print(f'введите длину списка: ')))
    
