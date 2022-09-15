# 3- Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).
# *Пример:*
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

import os
os.system("cls")

print("Программа, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,  в которой находится эта точка (или на какой оси она находится).")
print('Введите координаты точки, по осям X и Y. Эти  координаты не должны быть равны 0.')
def number_input(input_string):
    while type:
        digit = input(input_string)
        try:
            digit = int(digit)
            return digit
        except ValueError:
            print("Введено неверное значение. Только числа!!!")

axis_x = number_input("Введите координату точки по оси X:   ")
axis_y = number_input("Введите координату точки по оси Y:   ")

def quarter_1():
    print(f'Координаты точки по оси X = {axis_x}, по оси Y = {axis_y}')
    print("     |     ")
    print("     |  1  ")
    print("     |     ")
    print("-----------")
    print("     |     ")
    print("     |     ")
    print("     |     ")

def quarter_2():
    print(f'Координаты точки по оси X = {axis_x}, по оси Y = {axis_y}')
    print("     |     ")
    print("  2  |     ")
    print("     |     ")
    print("-----------")
    print("     |     ")
    print("     |     ")
    print("     |     ")

def quarter_3():
    print(f'Координаты точки по оси X = {axis_x}, по оси Y = {axis_y}')
    print("     |     ")
    print("     |     ")
    print("     |     ")
    print("-----------")
    print("     |     ")
    print("  3  |     ")
    print("     |     ")

def quarter_4():
    print(f'Координаты точки по оси X = {axis_x}, по оси Y = {axis_y}')
    print("     |     ")
    print("     |     ")
    print("     |     ")
    print("-----------")
    print("     |     ")
    print("     |  4  ")
    print("     |     ")

def search_position(axis_x, axis_y):
    if axis_x != 0 and axis_y !=0:
        if axis_x > 0 and axis_y > 0:
             quarter_1()
        elif axis_x < 0 and axis_y > 0:
            quarter_2()
        elif axis_x < 0 and axis_y < 0:
            quarter_3()
        else: quarter_4()
    else: print('Вы ввели неверные координаты, по условиям задачи 0 не подходит.')

search_position(axis_x, axis_y)

