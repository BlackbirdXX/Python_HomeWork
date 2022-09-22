# 2- Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета(или сколько вы зададите). Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет(или сколько вы зададите). Все конфеты оппонента достаются сделавшему последний ход.
# Предусмотрите последний ход, ибо там конфет остается меньше.
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

import os
import random
import colorama
from colorama import Fore, Back, Style
colorama.init
import time
import time
import sys
os.system("cls")

# Игру писал сам целиком и полностью, только для прогресс бара подсмотрел решение.
# Логику бота написал по урокам математики и информатики, там же уточнил условие задачи
# Рекомендую попробовать обыграть бота=)

print(Fore.YELLOW + 'Игра с конфетами.')
print("На столе лежит 216 конфет(Изначально в задаче 2021, но это слишком долго). Играют два игрока делая ход друг после друга. \nПервый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Пропускать ход нельзя. \nВсе конфеты оппонента достаются сделавшему последний ход.")
print(Style.RESET_ALL)
pause = input ( "Нажмите Enter для начала игры  " )

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
            print(Style.RESET_ALL)

def mode_selection():
    '''
    Функция выбора режима игры.
    '''
    mode = 0
    while mode <=  0 or mode > 2:
        print(Fore.YELLOW + "Выберите режим игры \n 1 - Игрок против игрока. \n 2 - Игрок против компьютера." + Style.RESET_ALL)
        mode = number_input("Режим : ")
    return mode


def boot():
    '''
    Прогресс бар
    '''
    os.system("cls")
    toolbar_width = 15
    sys.stdout.write("Загрузка игры  %s" % (" " * toolbar_width))
    sys.stdout.flush()
    sys.stdout.write("\b" * (toolbar_width+1)) 

    for i in range(toolbar_width):
        time.sleep(0.1) 
        sys.stdout.write(Back.WHITE + " ")
        sys.stdout.flush()

    sys.stdout.write("\n")
    print(Style.RESET_ALL)
    os.system("cls")



def draw():
    '''
    Функция жеребьевки.
    '''
    os.system("cls")
    p1_dice_roll = 0
    p2_dice_roll = 0
    while p1_dice_roll == p2_dice_roll:
        p1_dice_roll = int(random.randint(1,7))

        p2_dice_roll = int(random.randint(1,7))
    print(Fore.YELLOW + "Бросок костей." + Style.RESET_ALL)
    print(f"Игрок 1 бросил : {p1_dice_roll}")
    time.sleep(1)   
    print(f"Игрок 2 бросил : {p2_dice_roll}")
    time.sleep(1)
    if p1_dice_roll > p2_dice_roll:
        print(Fore.GREEN + "Победил игрок 1, он ходит первым.")
        roll_result = True
    else:
        print(Fore.BLUE + "Победил игрок 2, он ходит первым.")
        roll_result = False
    time.sleep(2)
    print(Style.RESET_ALL)
    return roll_result



def players_move():
    '''
    Функция хода игрока.
    '''
    move = 0
    while move <= 0 or move > 28:
        move = number_input("Возмите от 1 до 28 конфет. Сколько берете ? : ")
    return move

def last_move(candies):
    '''
    Функция хода игрока в конце игры.
    '''
    move = 0
    while move <= 0 or move > candies:
        move = number_input(f"Возмите от 1 до {candies} конфет. Сколько берете ? : ")
    return move


# candies = 2021
candies = 100
def pvp_mode(roll_result, candies):
    '''
    Логика режима игры игрок - игрок.
    '''
    
    while candies > 28:
        if roll_result == True:
            os.system("cls")
            print(Fore.YELLOW + f"Конфет осталось {candies} штук.")
            print(Fore.GREEN + "Ход первого игрока.")
            move = players_move()
            print(f"Игрок 1 взял {move} конфет.")
            candies -= move
            print(Style.RESET_ALL)
            roll_result = False
            time.sleep(1)
            
        elif roll_result == False:
            os.system("cls")
            print(Fore.YELLOW + f"Конфет осталось {candies} штук.")
            print(Fore.BLUE + "Ход второго игрока.")
            move = players_move()
            print(f"Игрок 2 взял {move} конфет.")
            candies -= move
            print(Style.RESET_ALL)
            roll_result = True
            time.sleep(1)
            
        else:
            print(Fore.RED + "Произошла какая то ошибка. Игру придется завершить =(")
            print(Style.RESET_ALL)
            break
    while candies <= 28 and candies > 0:
        if roll_result == True:
            os.system("cls")
            print(Fore.YELLOW + f"Конфет осталось {candies} штук.")
            print(Fore.GREEN + "Ход первого игрока.")
            move = last_move(candies)
            print(f"Игрок 1 взял {move} конфет.")
            candies -= move
            print(Style.RESET_ALL)
            roll_result = False
            time.sleep(1)
        else:
            os.system("cls")
            print(Fore.YELLOW + f"Конфет осталось {candies} штук.")
            print(Fore.BLUE + "Ход второго игрока.")
            move = last_move(candies)
            print(f"Игрок 2 взял {move} конфет.")
            candies -= move
            print(Style.RESET_ALL)
            roll_result = True
            time.sleep(1)

    os.system("cls")
    if roll_result == False:
        print(Fore.GREEN + Style.BRIGHT + "Поздарляем игрока №1. Он забирает все конфеты!!!!! \nБерегите зубы =)")
    else:
        print(Fore.BLUE + Style.BRIGHT + "Поздарляем игрока №2. Он забирает все конфеты!!!!! \nСледите за сахаром в крови =)")

    print(Style.RESET_ALL)

def computer_move(candies):
    '''
    Логика ходов бота.
    '''
    if candies > 28:
        move = candies%29
    elif candies <= 28:
        move = candies
    return move

def pve_mode(roll_result, candies):
    '''
    Логика режима игры игрок - бот.
    '''
    while candies > 28:
        if roll_result == True:
            os.system("cls")
            print(Fore.YELLOW + f"Конфет осталось {candies} штук.")
            print(Fore.GREEN + "Ход первого игрока.")
            move = players_move()
            print(f"Игрок 1 взял {move} конфет.")
            candies -= move
            print(Style.RESET_ALL)
            roll_result = False
            time.sleep(1)
            
        elif roll_result == False:
            os.system("cls")
            print(Fore.YELLOW + f"Конфет осталось {candies} штук.")
            print(Fore.CYAN + "Ход компьютера.")
            move = computer_move(candies)
            print(f"Компьютер взял {move} конфет.")
            candies -= move
            print(Style.RESET_ALL)
            roll_result = True
            time.sleep(1)
    while candies <= 28 and candies > 0:
        if roll_result == True:
            os.system("cls")
            print(Fore.YELLOW + f"Конфет осталось {candies} штук.")
            print(Fore.GREEN + "Ход первого игрока.")
            move = last_move(candies)
            print(f"Игрок 1 взял {move} конфет.")
            candies -= move
            print(Style.RESET_ALL)
            roll_result = False
            time.sleep(1)
        else:
            os.system("cls")
            print(Fore.YELLOW + f"Конфет осталось {candies} штук.")
            print(Fore.BLUE + "Ход компьютера.")
            move = computer_move(candies)
            print(f"Компьютер взял {move} конфет.")
            candies -= move
            print(Style.RESET_ALL)
            roll_result = True
            time.sleep(1)

    os.system("cls")
    if roll_result == False:
        print(Fore.GREEN + Style.BRIGHT + "Поздарляем игрока №1. Он забирает все конфеты!!!!! \nБерегите зубы =)")
    else:
        print(Fore.BLUE + Style.BRIGHT + "Поздарляем ваш компьютер. Он выигрывает все конфеты и отдает нуждающимся!!!!! \nСледите за сахаром в крови =)")

    print(Style.RESET_ALL)

def game():
    '''
    Сборка игры по модулям.
    '''
    boot()
    candies = 216
    mode = mode_selection()
    roll_result = draw()
    
    if mode == 1:
        pvp_mode(roll_result,candies)
    else:
        pve_mode(roll_result, candies)

game()
