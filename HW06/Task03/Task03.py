import os
import colorama
from colorama import Fore, Back, Style
colorama.init
os.system("cls")

print(Fore.YELLOW + "Программа, которая найдет расстояние между двумя точками пространства(числа вводятся через пробел)." + Style.RESET_ALL)

def number_input(input_string):
    '''
    Функция для проверки ввода числа.
    '''
    while type:
        try:
            digit = input(input_string)
            input_list = list(map(int, digit.split(' ')))
            return input_list
        except ValueError:
            print(Fore.RED + "Введено неверное значение. Только числа!!!" + Style.RESET_ALL)
def calculation_of_distance():
    '''
    Расчет дистанции между точками.
    '''
    point1 = number_input("Введите координаты первой точки. Две цифры через пробел : ")
    point2 = number_input("Введите координаты второй точки. Две цифры через пробел : ")
    result = round(sum([(j-i) ** 2 for i,j in zip(point1, point2)]) ** 0.5, 2)
    print(f"Расстояние между двумя точками : {result}")