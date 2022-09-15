# 4- Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# *Пример:*
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

import os
os.system("cls")

print('Программа, которая будет преобразовывать десятичное число в двоичное.')

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
            print("Введено неверное значение. Только числа!!!")

def dec_to_bin(dec):
    '''
    Функция перевода десятичного числа в двоичного.
    '''
    bin_number = [0] * dec
    i = 0
    while (dec > 0):
        bin_number[i] = dec % 2
        dec = int(dec / 2)
        i += 1

    for j in range(i - 1, -1, -1):
        print(bin_number[j], end = "")
 
dec_number = number_input('Введите число : ')
dec_to_bin(dec_number)