# 2. Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N в виде списка.
# 1 - 1 * 1, 2 - 1 * 2, 3 - 1 * 2 * 3, 4 - 1 * 2 * 3 * 4 и т.д.
# - 4 -> [1, 2, 6, 24]
# - 6 -> [1, 2, 6, 24, 120, 720]


n = int(input("Введите число N: "))
multi_list = []
multi = 1
for i in range(n) :
        multi = (i + 1) * multi
        multi_list.append (multi)
        i += 1
print(multi_list)
