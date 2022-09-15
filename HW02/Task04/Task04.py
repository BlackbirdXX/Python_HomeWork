# 4 - Реализуйте выдачу случайного числа
# не использовать random.randint и вообще библиотеку random
# Можете использовать xor, биты, библиотеку time или datetime (миллисекунды или наносекунды) - для задания случайности
# Учтите, что есть диапазон: от(минимальное) и до (максимальное)


import math
import time
import os
import colorama
from colorama import Fore, Back, Style
colorama.init
os.system("cls")

print(Fore.YELLOW + 'Программа выдающая случайное число.')

def number_input(input_string):
    while type:
        digit = input(input_string)
        try:
            digit = int(digit)
            return digit
        except ValueError:
            print(Fore.RED + "Введено неверное значение. Только числа!!!")

min_range = number_input('Введите минимальное значение  :  ')
max_range = number_input('Введите максимальное значение  :  ')

def LinearCR_fill_array(seed,min_value,max_value):
    a=1
    b=10
    result = math.ceil(math.fmod(a*math.ceil(seed)+b,max_value))
    if result < min_value:
        result += min_value
    return result
   
print(LinearCR_fill_array(time.time(),min_range, max_range))
print(Style.RESET_ALL)