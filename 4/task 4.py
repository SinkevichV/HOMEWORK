# * 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (от 0 до 10) многочлена, 
# записать в файл полученный многочлен не менее 3-х раз.
# in
# 9
# 5
# 3

# out in the file
# 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 = 0
# 4*x^5 + 1*x^4 - 3*x^3 - 3 = 0
# 4*x^2 - 4 = 0

# in
# 0
# -1
# 4

# out in the file
# 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 = 0
# 4*x^5 + 1*x^4 - 3*x^3 - 3 = 0
# 4*x^2 - 4 = 0
# 2*x^4 - 3*x^3 + 3*x^2 + 1*x^1 - 2 = 0

import random


def rnd():
    return random.randint(0, 11)

def create_polynomial():
    global k
    lst = [rnd() for i in range(k+1)]
    poly = f"{lst[k]}*x^{k}"
    nomial = ""
    if lst[k] !=0:
        while k > 1:
            k = k-1
            nomial += f'+{lst[k]}*x^{k}'
    elif k == 0:
            nomial = f'+{lst[k]}'    
        
    poly += f'{nomial}+{lst[k]}=0'    
    with open("poly.txt", "a", encoding="utf-8") as file:
        file.write(f'{poly} \n')
    return ''

    

k = int(input("Введите натуральную степень k = "))
create_polynomial()
