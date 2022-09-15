# 3 - Палиндромом называется слово, которое в обе стороны читается одинаково: "шалаш", "кабак".
# А еще есть палиндром числа - смысл также в том, чтобы число в обе стороны читалось одинаково, но есть одно "но".
# Если перевернутое число не равно исходному, то они складываются и проверяются на палиндром еще раз.
# Это происходит до тех пор, пока не будет найден палиндром.
# Напишите такую программу, которая найдет палиндром введенного пользователем числа.


import os
import colorama
from colorama import Fore, Back, Style
colorama.init
os.system("cls")

print(Fore.YELLOW + "Программа, которая найдет палиндром введенного пользователем числа.")

def number_input(input_string):
    while type:
        digit = input(input_string)
        try:
            digit = int(digit)
            return digit
        except ValueError:
            print(Fore.RED + "Введено неверное значение. Только числа!!!")
n = number_input(Fore.WHITE + "Введите число : ")
input_number = n
reverse_number = 0

while n > 0:
    temp = n % 10
    reverse_number = reverse_number * 10 + temp
    n = int(n / 10)

if input_number == reverse_number:
    print(Fore.GREEN + f"Число {input_number} является палиндромом.")
else: print(Fore.MAGENTA + f"Число {input_number} не палинтром.")
print(Style.RESET_ALL)