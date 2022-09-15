# 1-Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# *Пример:*
# - 6 -> да
# - 7 -> да
# - 1 -> нет

import os
# pip install colorama
import colorama
from colorama import Fore, Back, Style
colorama.init
os.system("cls")

print(Fore.YELLOW + "Программа, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.")

def input_weekday():
    while True:
        try:
            digit = int(input(Fore.GREEN + "Введите порядковый номер дня недели. Чистла от 1 до 7.    :"))
            return digit
        except ValueError:
            print(Fore.RED + "Введено неверное значение. Только числа, от 1 до 7!!!")


def definition_day(day_of_week):
    if (0 < day_of_week < 8):
        if (0 < day_of_week < 6):
            print(Fore.CYAN + "Это будний день.")
        else:
            print(Fore.MAGENTA +"Это выходные")
    else:
        print(Fore.RED + "В неделе всего 7 дней.")

day_of_week = input_weekday()
definition_day(day_of_week)
print(Style.RESET_ALL)