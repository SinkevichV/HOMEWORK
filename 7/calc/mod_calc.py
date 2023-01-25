from fractions import Fraction
import excep as e
from logg import logging


def sum_num(a, b):
    summ = a + b
    logging.info('operation sum of numbers')
    print(f'сумма чисел {a} и {b} равна: {summ}')

def sub_num(a, b):
    sub = a - b
    logging.info('operation difference of numbers')
    print(f'разность чисел {a} и {b} равна: {sub}')

def mul_num(a, b):
    mul = a * b
    logging.info('multiplication operation')
    print(f'произведение чисел {a} и {b} равна: {mul}')

def div_num(a, b):
    if b != 0: 
        div = a / b
        logging.info('number division operation')
        print(f'деление чисел {a} и {b} равна: {div}')
    else:
        print('Деление на 0 не возможно')

def pow_num(a, b):
    pow = a ** b
    logging.info('exponentiation operation')
    print(f'возведение числа {a} в степень {b} равно: {pow}')

def sqrt_num(a):
    sqrt = a ** 0.5
    logging.info('square root operation')
    print(f'квадратный корень числа {a} равен: {sqrt}')


