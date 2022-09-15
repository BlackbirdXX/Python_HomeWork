# 4- Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

import os
os.system("cls")

print("Программа, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).")

def number_input(input_string):
    while type:
        digit = input(input_string)
        try:
            digit = int(digit)
            return digit
        except ValueError:
            print("Введено неверное значение. Только числа!!!")

point = number_input("Введите номер четверти (числа от 1 до 4):   ")

def quarter_1():
    print(f'Координаты точки по оси X ∈ (0: ∞), по оси Y ∈ (0: ∞) ')
    print("     |     ")
    print("     |  1  ")
    print("     |     ")
    print("-----------")
    print("     |     ")
    print("     |     ")
    print("     |     ")

def quarter_2():
    print(f'Координаты точки по оси X ∈ (0: -∞), по оси Y ∈ (0: ∞) ')
    print("     |     ")
    print("  2  |     ")
    print("     |     ")
    print("-----------")
    print("     |     ")
    print("     |     ")
    print("     |     ")

def quarter_3():
    print(f'Координаты точки по оси X ∈ (0: -∞), по оси Y ∈ (0: -∞)')
    print("     |     ")
    print("     |     ")
    print("     |     ")
    print("-----------")
    print("     |     ")
    print("  3  |     ")
    print("     |     ")

def quarter_4():
    print(f'Координаты точки по оси X ∈ (0: ∞), по оси Y ∈ (0: -∞) ')
    print("     |     ")
    print("     |     ")
    print("     |     ")
    print("-----------")
    print("     |     ")
    print("     |  4  ")
    print("     |     ")


def search_range(point):
    if 0 < point <5:
        if point == 1:
             quarter_1()
        elif point == 2:
            quarter_2()
        elif point == 3:
            quarter_3()
        else: quarter_4()
    else: print('Вы ввели неверные координаты, диапазон чисел от 1 до 4.')

search_range(point)