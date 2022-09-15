# 3-Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# *Пример:*
# - [1.1, 1.2, 3.1, 5.17, 10.02] => 0.18 или 18
#  - [4.07, 5.1, 8.2444, 6.98] - 0.91 или 91

import os
os.system("cls")

print('Программа, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.')

input_array1 = [1.1, 1.2, 3.1, 5.17, 10.02]
input_array2 = [4.07, 5.1, 8.2444, 6.98]

def get_abs(a: float) -> float:
    '''
    Функция, которая убирает целочисленную часть числа.
    '''
    if (a<0):
        return int(a) - a
    else:
        return a - int(a)
def search_diff_float(input_array: list):
    '''
    Функция, которая ищет разницу между максимальной и минимальной дробной части чисел.
    '''
    min_value = 1.0
    max_value = 0.0
    temp = 0.0

    for i in range(len(input_array)):
        temp = get_abs(input_array[i])
        if temp < min_value: min_value = temp
        if temp > max_value: max_value = temp
    print(f'Разница между максимальной и минимальной дробной части : {round(max_value-min_value, 2)}')
print(f'Массив №1 : {input_array1}')
search_diff_float(input_array1)
print(f'Массив №2 : {input_array2}')
search_diff_float(input_array2)