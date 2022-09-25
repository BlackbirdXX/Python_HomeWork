# Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

import os
import random
import colorama
from colorama import Fore, Back, Style
colorama.init
os.system("cls")

print(Fore.YELLOW + "Программа, которая определить позицию второго вхождения строки в списке либо сообщить, что её нет." + Style.RESET_ALL)


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
def multiplication_pairs():
    size = number_input("Введите размер списка : ")
    new_list = list(map(lambda _: random.randint(0, 11), range(size)))
    print(f"Список рандомных чисел : {new_list}")
    result_list = [new_list[i] * new_list[-1-i] for i in range(len(new_list)//2 + len(new_list)%2)]
    print(f"Произведение пар чисел : {result_list}")

multiplication_pairs()