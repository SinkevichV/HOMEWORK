from fractions import Fraction
from logg import logging
import mod_calc as m
import excep as e




def menu():
    logging.info('Start calc')
    while True:
        num_type = input("Enter\n"
                         "1 - compl\n"
                         "2 - ra\n"
                         "3 - ex\n")
        match num_type:
            case "1":
                
                menu_compl()
            case "2":
                
                menu_ra()
            case "3":
                logging.info('exit calc')
                quit()
            case _:
                logging.error('incorrect values')
                print("Err")

def menu_compl():
    while True:
        logging.info('selected operations with complex numbers')
        operations_compl()
def menu_ra():
    while True:
        logging.info('selected operations with rational numbers')
        operations_ra()


def operations_compl():
    while True:
        operations_type = input("Enter\n"
                                "1 - sum\n"
                                "2 - sub\n"
                                "3 - mul\n"
                                "4 - div\n"
                                "5 - pow\n"
                                "6 - sqrt\n"
                                "0 - previous menu\n")
        match operations_type:
            case "1":
                m.sum_num(e.comp_num(), e.comp_num())
            case "2":
                m.sub_num(e.comp_num(), e.comp_num())
            case "3":
                m.mul_num(e.comp_num(), e.comp_num())
            case "4":
                m.div_num(e.comp_num(), e.comp_num())
            case "5":
                m.pow_num(e.comp_num(), e.comp_num())
            case "6":
                m.sqrt_num(e.comp_num())
            case "0":
                menu()
            case _:
                logging.error('incorrect values')
                print("Err")

def operations_ra():
    while True:
        operations_type = input("Enter\n"
                                "1 - sum\n"
                                "2 - sub\n"
                                "3 - mul\n"
                                "4 - div\n"
                                "5 - pow\n"
                                "6 - sqrt\n"
                                "0 - previous menu\n")
        match operations_type:
            case "1":
                m.sum_num(e.rat_num(), e.rat_num())
            case "2":
                m.sub_num(e.rat_num(), e.rat_num())
            case "3":
                m.mul_num(e.rat_num(), e.rat_num())
            case "4":
                m.div_num(e.rat_num(), e.rat_num())
            case "5":
                m.pow_num(e.rat_num(), e.rat_num())
            case "6":
                m.sqrt_num(e.rat_num())
            case "0":
                menu()
            case _:
                print("Err")
       
