# 5-Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# *Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи](https://clck.ru/yWbkX.)

import os
os.system("cls")

print('Программа, которая составляет список чисел Фибоначчи, в том числе для отрицательных индексов.')

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
            print("Введено неверное значение. Только числа!!!")

k = number_input('Введите число-диапазон для формулы Фибоначчи : ')

positive_fibonacci = [0,1]
negative_fibonacci = [1,1]

def fibonacci(k: int)->list:
    '''
    Функция заполняющая список числами фибоначи.
    '''
    for i in range(2, k+1):
        positive_fibonacci.append(positive_fibonacci[i-2]+positive_fibonacci[i-1])
    return positive_fibonacci


def negafibonacci(k: int)->list:
    '''
    Функция заполняющая список отрицательными числами фибоначи.
    '''
    for i in range(2, k):
        negative_fibonacci.append(negative_fibonacci[i-2]+negative_fibonacci[i-1])
    for i in range(len(negative_fibonacci)):
            if i%2!=0:
                negative_fibonacci[i] *= -1

    negative_fibonacci.reverse()    
    return negative_fibonacci

result = negafibonacci(k) + fibonacci(k)

print(result)