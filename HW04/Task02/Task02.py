# 2 - Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности. Не использовать множества.
# [1,1,1,1,2,2,2,3,3,3,4] -> [1,2,3,4]

import os
import colorama
from colorama import Fore, Back, Style
colorama.init
os.system("cls")

print(Fore.YELLOW + 'Программа, которая выведет список неповторяющихся элементов исходной последовательности.')

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

size = 8

def fill_array(sise: int) ->list:
    '''
    Функция, которая заполняет список числами
    '''
    numbers_list = []
    for i in range(size + 1):
        numbers_list.append (number_input(Fore.WHITE + 'Введите натуральное число : '))
    return numbers_list

numbers_list = fill_array(size)
print(f'Введенный список : {numbers_list}')
result = []
[result.append(i) for i in numbers_list if i not in result]
print(f"Уникальные элементы списка : {result}")


print(Style.RESET_ALL)