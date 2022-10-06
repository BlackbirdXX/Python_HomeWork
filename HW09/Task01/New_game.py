from cv2 import CALIB_HAND_EYE_ANDREFF
from config import TOKEN
import logging
import random

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
)

# Включим ведение журнала
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

candies = 100
digit=0
roll_result = False
move = 1
global_array = [candies, roll_result, move]


logger = logging.getLogger(__name__)

# Определяем константы этапов разговора
DRAW, GAME = range(2)

def start(update, _):

    # Начинаем разговор с вопроса
    update.message.reply_text(
        'Игра с конфетами.'
        'На столе лежит 216 конфет'
        'Играют два игрока делая ход друг после друга.'
        'Первый ход определяется жеребьёвкой. '
        'За один ход можно забрать не более чем 28 конфет. '
        'Пропускать ход нельзя. Все конфеты '
        'оппонента достаются сделавшему последний ход.'
        'Введите любой текст.')
        
    return DRAW

# def number_input(update, context):
#     '''
#     Функция для проверки ввода числа.
#     '''
#     global digit
#     word = update.message.text
#     while type:
#         digit = word
#         try:
#             digit = int(digit)
#             return digit
#         except ValueError:
#             context.bot.send_message(update.effective_chat.id, "Введено неверное значение. Только числа!!!")

def draw(update, context):
    '''
    Функция жеребьевки.
    '''
    global roll_result
    p1_dice_roll = 0
    p2_dice_roll = 0
    while p1_dice_roll == p2_dice_roll:
        p1_dice_roll = int(random.randint(1,7))

        p2_dice_roll = int(random.randint(1,7))
    context.bot.send_message(update.effective_chat.id, 
                                        "Бросок костей.\n" 
                                        f"Игрок 1 бросил : {p1_dice_roll}\n"
                                        f"Игрок 2 бросил : {p2_dice_roll}\n")
    if p1_dice_roll > p2_dice_roll:
        context.bot.send_message(update.effective_chat.id, "Победил игрок 1, он ходит первым.\n"
                                                        "Возмите от 1 до 28 конфет. Сколько берете ? : ")
        roll_result = True
        
    else:
        context.bot.send_message(update.effective_chat.id, "Победил бот, он ходит первым.")
        roll_result = False
        
    return GAME

def players_move(update):
    '''
    Функция хода игрока.
    '''
    global candies
    global move
    global roll_result
    global digit
    move = update.message.text
    move = int(move)
    # while right == False:
    #     # digit = update.message.text
    #     if digit.isdigit():
    #         move = int(digit)
    #         right = True
    #     else:
    #         update.message.reply_text("Неверное число! Введите заново.")
    while move <= 0 or move > 28:
        candies -= move
    roll_result = False
    update.message.reply_text(f'Игрок взял {move} конфет.\n'
                                f'Осталось {candies}.\n'
                                'Теперь ходит бот.'
                                )
    return GAME

def last_move(update):
    '''
    Функция хода игрока в конце игры.
    '''
    global candies
    global move
    global game_actions
    move = 0
    while move <= 0 or move > candies:
        
        move = update.message.text
    return GAME



def computer_move(update):
    '''
    Логика ходов бота.
    '''
    global move
    global candies
    global roll_result
    global game_actions
    if candies > 28:
        move = candies%29
        candies -= move
    elif candies <= 28:
        move = candies
        candies -= move
    roll_result = True
    update.message.reply_text(f"Бот взял  {move} конфет.\n"
                                f'Осталось {candies}.\n'
                                f"Возмите от 1 до 28 конфет. Сколько берете ? : ")
    
    return GAME

def pve_mode(update,context):
    '''
    Логика режима игры игрок - бот.
    '''
    global digit
    global move
    global candies
    global roll_result
    global game_actions
    while candies > 28:
        if roll_result == True:
            players_move(update)
            print(candies)
            # context.bot.send_message(update.effective_chat.id, f"Конфет осталось {candies} штук.")
            # context.bot.send_message(update.effective_chat.id, "Ход первого игрока.")
            # move = players_move()
            # context.bot.send_message(update.effective_chat.id, f"Игрок 1 взял {move} конфет.")
            # candies -= move
            # roll_result = False
            
        elif roll_result == False:
            computer_move(update)
            print(candies, move, roll_result, digit)
            # return ConversationHandler.END
            # context.bot.send_message(update.effective_chat.id, f"Конфет осталось {candies} штук.")
            # context.bot.send_message(update.effective_chat.id, "Ход компьютера.")
            # move = computer_move(candies)
            # context.bot.send_message(update.effective_chat.id, f"Компьютер взял {move} конфет.")
            # candies -= move
            # roll_result = True
    while candies <= 28 and candies > 0:
        if roll_result == True:
            last_move(update)
            # context.bot.send_message(update.effective_chat.id, f"Конфет осталось {candies} штук.")
            # context.bot.send_message(update.effective_chat.id, "Ход первого игрока.")
            # move = last_move(candies)
            # context.bot.send_message(update.effective_chat.id, f"Игрок 1 взял {move} конфет.")
            # candies -= move
            # roll_result = False
        else:
            computer_move(update)
            # context.bot.send_message(update.effective_chat.id, f"Конфет осталось {candies} штук.")
            # context.bot.send_message(update.effective_chat.id, "Ход компьютера.")
            # move = computer_move(candies)
            # context.bot.send_message(update.effective_chat.id, f"Компьютер взял {move} конфет.")
            # candies -= move
            # roll_result = True

    if roll_result == False:
        update.message.reply_text ("Поздарляем игрока №1. Он забирает все конфеты!!!!! \nБерегите зубы =)")
    else:
        update.message.reply_text ("Поздарляем ваш компьютер. Он выигрывает все конфеты и отдает нуждающимся!!!!! \nСледите за сахаром в крови =)")


# def game(update, context):
#     '''
#     Сборка игры по модулям.
#     '''
#     draw(update, context)
#     pve_mode(update, context)

def skip(update, _):
    # определяем пользователя
    user = update.message.from_user
    # Пишем в журнал о том, что пользователь не разговорчивый
    logger.info("Пользователь %s отменил игру.", user.first_name)
    # Отвечаем на отказ поговорить
    update.message.reply_text(
        'Стоп игра.', 
        reply_markup=ReplyKeyboardRemove()
    )
    # Заканчиваем разговор.
    return ConversationHandler.END

if __name__ == '__main__':
    # Создаем Updater и передаем ему токен вашего бота.
    updater = Updater(TOKEN)
    # получаем диспетчера для регистрации обработчиков
    dispatcher = updater.dispatcher
   
    conv_handler = ConversationHandler( # здесь строится логика разговора
        # точка входа в разговор
        
        entry_points=[CommandHandler('start', start)],
        
        # этапы разговора, каждый со своим списком обработчиков сообщений
        states={
            DRAW: [MessageHandler(Filters.text, draw)],
            GAME: [MessageHandler(Filters.text, pve_mode)],
        },
        # точка выхода из разговора
        fallbacks=[CommandHandler('skip', skip)],
    )

    # Добавляем обработчик разговоров `conv_handler`
    dispatcher.add_handler(conv_handler)

    # Запуск бота
    updater.start_polling()
    updater.idle()