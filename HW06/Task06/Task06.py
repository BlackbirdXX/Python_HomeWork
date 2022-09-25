# Сформировать список из N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.

import os
import colorama
from colorama import Fore, Back, Style
colorama.init
os.system("cls")

print(Fore.YELLOW + "Программа, которая сформирует список из N членов последовательности." + Style.RESET_ALL)

def number_input(input_string):
    '''
    Функция для проверки ввода числа.
    '''
    while type:
        digit = input(input_string)
        try:
            digit = int(digit)
            return digit
        except ValueError:
            print(Fore.RED + "Введено неверное значение. Только числа!!!")
            print(Style.RESET_ALL)

def generate_list():
    '''
    Функция, которая сформирует список из N членов последовательности.
    '''
    ratio = number_input("Введите число N : ")
    result_list = list((-3) ** i for i in range(ratio))
    print(result_list)

generate_list()