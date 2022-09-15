# 1 - Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# N = 20 -> [2,5]
# N = 30 -> [2, 3, 5]

import os
import colorama
from colorama import Fore, Back, Style
colorama.init
os.system("cls")

print(Fore.YELLOW + 'Программа, которая составит список простых множителей числа N.')

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

input_number = number_input(Fore.WHITE + 'Введите натуральное число : ')

def prime_factorization(n: int) -> list:
    '''
    Функция, для разложения простых чисел на множители.
    '''
    i = 2
    prime = []
    while i * i <= n:
       while n % i == 0:
           prime.append(i)
           n = int(n / i)
       i = i + 1
    if n > 1:
       prime.append(n)
    return prime

result = prime_factorization(input_number)
print(f'Результат разложения на множители : {result}')

numbers_list = []
[numbers_list.append(i) for i in result if i not in numbers_list]
print(f"Простыми множителями числа являются : {numbers_list}")

print(Style.RESET_ALL)