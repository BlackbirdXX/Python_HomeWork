# 4- Шифр Цезаря - это способ шифрования, где каждая буква смещается на определенное количество символов влево или вправо. При расшифровке происходит обратная операция. 
# К примеру, слово "абба" можно зашифровать "бввб" - сдвиг на 1 вправо. "вггв" - сдвиг на 2 вправо, "юяяю" - сдвиг на 2 влево.
# Сдвиг часто называют ключом шифрования.
# Ваша задача - написать функцию, которая записывает в файл шифрованный текст, а также функцию, которая спрашивает ключ, считывает текст и дешифровывает его.

import os
import colorama
from colorama import Fore, Back, Style
colorama.init
os.system("cls")

alphabet =  'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя,.! '
path_in = 'E:/Learning/Python/PythonHomeWork/HW04/Task04/text.txt'

print(Fore.YELLOW + 'Программа, которая записывает в файл шифрованный текст, а также функцию, которая спрашивает ключ, считывает текст и дешифровывает его.')

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

step = number_input(Fore.WHITE + 'Задайте шаг смещения : ')
if step > 70:
    step = step%70

message = ('Пришел, увидел, победил!')
print(message)

def encryption(message, step):
    '''
    Функция, которая шифрует сообщение Шифром Цезаря.
    '''
    result = ''
    for i in message:
        position = alphabet.find(i)
        code_position = position + step
        if code_position > 69:
            code_position -= 70
            result += alphabet[code_position]  
        else:
            result += alphabet[code_position]
    return result
encrypted_message = encryption(message, step)
print(encrypted_message)

with open(path_in, 'w+',  encoding= 'utf-8') as data:
    data.write(encrypted_message)

with open(path_in, 'r',  encoding= 'utf-8') as data:
    encrypted_message_read = data.read()

def de_encryption(encrypted_message_read, step2):
    '''
    Функция, которая дешифрует сообщение из Шифра Цезаря.
    '''
    result = ''
    for i in encrypted_message_read:
        position = alphabet.find(i)
        code_position = position - step2
        if code_position > 69:
            code_position -= 70
            result += alphabet[code_position]  
        else:
            result += alphabet[code_position]
    return result

step2 = number_input('Введите ключ дешифровки : ')
if step2 > 70:
    step2 = step%70

de_encrypted_message = de_encryption(encrypted_message_read, step2)

print(de_encrypted_message)
print(Style.RESET_ALL)