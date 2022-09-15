# 1 - Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр. Учтите, что числа могут быть отрицательными
# Пример:
# 67.82 -> 23
# 0.56 -> 11


import os
import colorama
from colorama import Fore, Back, Style
colorama.init
os.system("cls")

print(Fore.YELLOW + "Программа, которая принимает на вход вещественное число и показывает сумму его цифр.")

def number_input(input_string):
    while type:
        digit = input(input_string)
        try:
            digit = float(digit)
            return digit
        except ValueError:
            print(Fore.RED + "Введено неверное значение. Только числа!!!")

number = number_input(Fore.WHITE + "Введите дробное число : ")

def adding_numbers(digit):
    if digit < 0:
        digit *= -1
    digit_string = str(digit).split('.')
    digit_array = []
    for i in digit_string:
        digit_array += i
    result = 0
    for j in digit_array:
        j = int(j)
        result += j
    print(result)

adding_numbers(number)
print(Style.RESET_ALL)