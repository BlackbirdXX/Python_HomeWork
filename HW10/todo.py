import csv
import logging

from numpy import empty
from config import TOKEN
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
)


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

MENU, HELP, SHOW, DELETE, ADD = range(5)


def start(update, context):
    '''
    Функция начала диалога.
    '''
    reply_keyboard = [['/help', '/add', '/delete'],
                      ['/show', '/stop']]
    markup_key = ReplyKeyboardMarkup(
        reply_keyboard, one_time_keyboard=False)
    update.message.reply_text(
        'Привет! Я Умный_Бот. Я помогу вам создать список дел.\n\n'
        'Выберите кнопку.',
        reply_markup=markup_key)
    
    context.bot.send_sticker(update.effective_chat.id,
                             'CAACAgIAAxkBAAIJVmM-33MfFLHeukW_tKbam4IKY5p2AAI9AANSiZEj56KM1HtGgRAqBA')
    update.message.reply_text(
            'Доступны следующие команды:\n'
            '/help - информация,\n'
            '/add - добавить задачу,\n'
            '/delete - удалить (пометить выполненным) задачу,\n'
            '/show - показать весь список задач,\n'
            '/stop - прекратить общение с ботом.')
    return MENU


def menu(update, _):
    '''
    Функция обработки выбора кнопки на первом этапе.
    '''
    user = update.message.from_user
    logger.info("Пользователь %s нажал кнопку %s.",
                user.first_name, update.message.text)
    step = update.message.text
    if step == '/help':
        update.message.reply_text(
            'Открыть список команд? Выберите /Yes или /No.')
        return HELP
    if step == '/add':
        update.message.reply_text(
            'Введите задачу, которую хотите добавить. Иначе нажмите /No.')
        return ADD
    if step == '/delete':
        update.message.reply_text(
            'Если хотите удалить какую-то задачу, введите ее название, иначе нажмите /No.')
        return DELETE
    if step == '/show':
        update.message.reply_text(
            'Открыть список дел? Выберите /Yes или /No.')
        return SHOW
    if step == '/stop':
        return stop(update, _)


def help(update, context):
    '''
    Функция вызова помощи со списком команд.
    '''
    user = update.message.from_user
    logger.info("Пользователь %s подтвердил операцию вызова списка команд, нажал %s.",
                user.first_name, update.message.text)
    
    if update.message.text == '/Yes':
        context.bot.send_sticker(update.effective_chat.id,
                                 'CAACAgIAAxkBAAIJUGM-3ow5HcUX2tDYj5BKKELG0Q61AAJGAANSiZEj-P7l5ArVCh0qBA')
        update.message.reply_text(
            'Доступны следующие команды:\n'
            '/help - информация,\n'
            '/add - добавить задачу,\n'
            '/delete - удалить (пометить выполненным) задачу,\n'
            '/show - показать весь список задач,\n'
            '/stop - прекратить общение с ботом.')
    else:
        context.bot.send_sticker(update.effective_chat.id,
                                 'CAACAgIAAxkBAAIJU2M-3vVOlaF2MPr01lenVM_HplAoAAK7AAP3AsgPZJdBk2UwHMAqBA')
        update.message.reply_text("Пользователь отклонил операцию вызова списка команд.")
        logger.info("Пользователь %s отклонил операцию вызова списка команд, нажал %s.",
                    user.first_name, update.message.text)
        return MENU
    return MENU


def add(update, context):
    '''
    Функция добавления задачи в список.
    '''
    user = update.message.from_user
    text = update.message.text
    if text == '/No':
        logger.info("Пользователь %s отклонил операцию добавления новой задачи, нажал %s.",
                    user.first_name, update.message.text)
        update.message.reply_text("Пользователь отклонил операцию добавления новой задачи")
        context.bot.send_sticker(update.effective_chat.id,
                                 'CAACAgIAAxkBAAIJU2M-3vVOlaF2MPr01lenVM_HplAoAAK7AAP3AsgPZJdBk2UwHMAqBA')
        return MENU
    else:
        context.bot.send_sticker(update.effective_chat.id,
                                 'CAACAgIAAxkBAAIJUGM-3ow5HcUX2tDYj5BKKELG0Q61AAJGAANSiZEj-P7l5ArVCh0qBA')
        logger.info("Пользователь %s добавил задачу: %s.",
                    user.first_name, update.message.text)
        with open('list.csv', 'a', encoding='utf-8', newline='\n') as file:
            new_text = text + ',\n'
            file.write(new_text)
            update.message.reply_text(
                f'Задача "{text}" добавлена в список задач.')
    return MENU


def delete(update, context):
    ''''
    Функция удаления задачи из списка.
    '''
    user = update.message.from_user
    str = ''
    text = update.message.text
    if text == '/No':
        context.bot.send_sticker(update.effective_chat.id,
                                 'CAACAgIAAxkBAAIJU2M-3vVOlaF2MPr01lenVM_HplAoAAK7AAP3AsgPZJdBk2UwHMAqBA')
        update.message.reply_text("Пользователь отклонил операцию удаления задачи")
        logger.info("Пользователь %s отклонил операцию удаления задачи, нажал %s.",
                    user.first_name, update.message.text)
        return MENU
    elif text and text != '/No':
        context.bot.send_sticker(update.effective_chat.id,
                                 'CAACAgIAAxkBAAIJUGM-3ow5HcUX2tDYj5BKKELG0Q61AAJGAANSiZEj-P7l5ArVCh0qBA')
        logger.info("Пользователь %s удаляет задачу, содержащую текст: %s.",
                    user.first_name, update.message.text)
        try:
            open('list.csv')
            with open('list.csv', 'r', encoding='utf-8', newline='\n') as file:
                file_reader = csv.reader(file)
                for row in file_reader:
                    if text.lower()  in ''.join(row).lower():
                        continue
                    else:
                        update.message.reply_text("Такой записи нет.")
                        return MENU

                for row in file_reader:
                    if text.lower() in ''.join(row).lower():
                        continue
                    else:
                        row = ''.join(row)
                        str += row
                        str += ',\n'
            with open('list.csv', 'w', encoding='utf-8', newline='\n') as file:
                file.write(str)
            update.message.reply_text(f'Задачи, содержащие "{text}", удалены.')
        except FileNotFoundError:
            update.message.reply_text('Нет готового списка дел.')
    return MENU


def show(update, context):
    '''
    Функция отображения списка дел.
    '''
    user = update.message.from_user
    if update.message.text == '/Yes':
        context.bot.send_sticker(update.effective_chat.id,
                                 'CAACAgIAAxkBAAIJUGM-3ow5HcUX2tDYj5BKKELG0Q61AAJGAANSiZEj-P7l5ArVCh0qBA')
        logger.info("Пользователь %s подтвердил операцию отображения списка дел, нажал %s.",
                    user.first_name, update.message.text)
        str = ''
        filename = 'list.csv'
        try:
            open(filename)
            with open(filename, encoding='utf-8') as notes:
                file_reader = csv.reader(notes)
                for row in file_reader:
                    if len(row) > 0:
                        row = ''.join(row)
                        str += row
                        str += '\n'
                update.message.reply_text(str)
        except FileNotFoundError:
            update.message.reply_text('Нет готового списка дел.')
    else:
        logger.info("Пользователь %s отклонил операцию, нажал %s.",
                    user.first_name, update.message.text)
        update.message.reply_text("Пользователь отклонил вывод списка задач.")
        return MENU
    return MENU


def stop(update, context):
    '''
    Функция остановки диалога.
    '''
    user = update.message.from_user
    logger.info("Пользователь %s отменил разговор.", user.first_name)
    update.message.reply_text(
        'Выход из редактора списка дел.\n'
        'Начать заново : (команда: /start)!',
        reply_markup=ReplyKeyboardRemove()
    )
    context.bot.send_sticker(update.effective_chat.id,
                             'CAACAgIAAxkBAAIJWWM-4Ctx-UXlARGDnLMQ7uj83hn4AAJMDgACsisRSfQVv4tbKj6YKgQ')
    return ConversationHandler.END


if __name__ == '__main__':
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher
    conv_handler = ConversationHandler( 
        entry_points=[CommandHandler('start', start)],
        states={
            MENU: [MessageHandler(Filters.regex('^(/help|/add|/edit|/find|/delete|/show|/save|/load)$'), menu)],
            HELP: [MessageHandler(Filters.text, help)],
            SHOW: [MessageHandler(Filters.text, show)],
            DELETE: [MessageHandler(Filters.text, delete)],
            ADD: [MessageHandler(Filters.text, add)],
        },
        fallbacks=[CommandHandler('stop', stop)],
    )

    dispatcher.add_handler(conv_handler)

    updater.start_polling()
    print('server started')
    updater.idle()
    print('server stoped')
