# 2-Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат. Предикату можно заменить на понятие "бит".
# Должна получиться таблица истинности.

import os
# pip install colorama
import colorama
from colorama import Fore, Back, Style
colorama.init
os.system("cls")

print(Fore.YELLOW + "Программа для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.")
print(Fore.CYAN + "X Y Z   Truthfulness")
def truth_check():
    for x in range(2):
        for y in range(2):
            for z in range(2):
                result= not (x or y or z) == (not(x) and not(y) and not(z))
                print(Fore.BLACK + Back.WHITE  + f"{x} {y} {z}       {result}    ")

truth_check()
print(Style.RESET_ALL)
