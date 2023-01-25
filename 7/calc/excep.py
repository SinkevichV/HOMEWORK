from logg import logging
from fractions import Fraction
def value_num():
    n = input("")
    return n

def check_natural_num(n):
    while True:
        if n.isdigit():
            n = int(n)
            if n > 0:
                return n
        logging.error('incorrect values')
        print("Введено некорректное значение")
        return check_natural_num(value_num())     
    
def check_integer_num(n):
    
    try:
        int(n)
        return n
    except ValueError:
        logging.error('incorrect values')
        return print("Введено некорректное значение"), check_integer_num(value_num())
    
def check_real_num(n):
    try:
        float(n)
        return n
    except ValueError:
        logging.error('incorrect values')
        return print("Введено некорректное значение"), check_real_num(value_num())

def rat_num():
    print('Задайте рациональное число:')
    print('Введите числитель рационального числа: ')
    a = int(check_integer_num(value_num()))
    print('Введите знаменатель рационального числа: ')
    b = int(check_natural_num(value_num()))
    r = Fraction(a, b)
    logging.info('given rational number')
    return r     

def comp_num():
    print('Задайте комплексное число:')
    print('Введите вещественную часть числа: ')
    a = float(check_real_num(value_num()))
    print('Введите мнимую часть числа: ')
    b = float(check_real_num(value_num()))
    c = complex(a, b)
    logging.info('given complex number')
    return c
       
            
    


# check_natural_num(value_num())  натуральное
# check_integer_num(value_num()) целое
# check_real_num(value_num())
# rat_num()   
# comp_num()