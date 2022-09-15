# 5-Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# *Пример:*
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

import os
import math
os.system("cls")

print('Программа, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.')
print('Ведите координаты точек X и Y:')
def number_input(input_string):
    while type:
        digit = input(input_string)
        try:
            digit = int(digit)
            return digit
        except ValueError:
            print("Введено неверное значение. Только числа!!!")

def distance_calculation():
    point_xa = number_input('Введите первую координату точки X :')
    point_xb = number_input('Введите вторую координату точки X :')
    point_ya = number_input('Введите первую координату точки Y :')
    point_yb = number_input('Введите вторую координату точки Y :')
    distance = math.sqrt((point_xb - point_xa)**2 + (point_yb - point_ya)**2)
    print(f'Расстояние между точками : {round(distance, 2)}')

distance_calculation()