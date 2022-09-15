# 1- Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# *Пример:*
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import os
import math
import time
os.system("cls")

print('Программа, которая найдёт сумму элементов списка, стоящих на нечётной позиции.')

def number_input(input_string):
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

print(result)
print(sum(result[1::2]))
