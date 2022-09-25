# Найти сумму чисел списка стоящих на нечетной позиции

import os
import random
import colorama
from colorama import Fore, Back, Style
colorama.init
os.system("cls")

print(Fore.YELLOW + "Программа, которая находит сумму чисел списка стоящих на нечетной позиции." + Style.RESET_ALL)

def odd_sum():
    '''
    Сложение нечетных чисел в списке.
    '''
    new_list = list(map(lambda _: random.randint(0, 11), range(6)))
    print(f"Рандомный список чисел : {new_list}")
    result = sum([i for j, i in enumerate(new_list) if j%2 == 0])
    print(f"Сумма чисел стоящих на нечетных позициях : {result}")

odd_sum()