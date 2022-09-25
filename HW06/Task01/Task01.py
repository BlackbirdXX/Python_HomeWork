# Определить, присутствует ли в заданном списке строк, некоторое число

import os
import colorama
from colorama import Fore, Back, Style
colorama.init
os.system("cls")

print(Fore.YELLOW + "Программа, которая определяет присутствует ли в заданном списке строк, некоторое число." + Style.RESET_ALL)
new_list = 'Первый', 'Второй', '3', 'Четвертый', 'Пятый'
def search_num(input_list):
    '''
    Поиск числа.
    '''
    input_num = input("Введите число : ")

    search_number = list(filter(lambda x: str(input_num) in x, input_list))
    if search_number == []:
         print(f"Числа {input_num} в списке нет.")
    else:
        print(f"Число {input_num} в списке есть.")

search_num(new_list)