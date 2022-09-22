# 1- Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# 'абвгдейка - это передача' = >" - это передача"


import os
import colorama
from colorama import Fore, Back, Style
colorama.init
os.system("cls")

print(Fore.YELLOW + 'Программа, удаляющая из текста все слова, содержащие ""абв"".')
print(Style.RESET_ALL)

def text_input(input_string):
    '''
    Функция для проверки ввода числа.
    '''
    while type:
        string = input(input_string)
        try:
            if not string.isdigit():
                return string
        except TypeError:
            print(Fore.RED + "Введено неверное значение. Только текст!!!")
new_string = text_input("Введите фразу : ")
print(new_string)

def search_abc(new_string):
    '''
    Функция, которая удаляет слова, содержащие нужные символы из строки.
    '''
    lower_string = new_string.lower()
    split_string = lower_string.split(' ')

    search_word = 'абв'

    result_string = []
    for word in split_string:
        if search_word not in word:
            result_string.append(word)

    result_string = ' '.join(result_string)
    print(result_string)

search_abc(new_string)