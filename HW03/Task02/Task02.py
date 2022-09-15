# 2-Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# *Пример:*
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import os
import math
import time
os.system("cls")

print('Программа, которая найдёт сумму элементов списка, стоящих на нечётной позиции.')

def number_input(input_string) -> int:
    '''
    Функция для проверки ввода числа
    '''
    while type:
        digit = input(input_string)
        try:
            digit = int(digit)
            return digit
        except ValueError:
            print("Введено неверное значение. Только числа!!!")

array_size = number_input('Введите размер массива  :  ')
max_range = 10

def LinearCR_fill_array(seed,size,max):
    '''
    Функция для заполнения массива случайными числами.
    '''
    a=1
    b=123
    if size==1:
        return math.ceil(math.fmod(a*math.ceil(seed)+b,max))
    rand_filled_array=[0 for i in range(size)]
    rand_filled_array[0]=math.ceil(seed)
    for i in range(1,size):
        rand_filled_array[i]=math.ceil(math.fmod((a*rand_filled_array[i-1]+b),max))
    return rand_filled_array[1:size]
result = LinearCR_fill_array(time.time(),array_size + 1, max_range)


print(f'Сгенерированный массив чисел:   {result}')

def conposition_array(result):
    '''
    Функция для умножения пар чисел массива.
    '''
    composition = []
    for i in range((len(result)+1)//2):
        composition.append(result[i]*result[len(result)-1 -i])
    print(f'Произведение пар чисел массива:   {composition}')

conposition_array(result)