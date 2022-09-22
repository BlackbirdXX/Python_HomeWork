# Создайте два списка — один с названиями языков программирования, другой — с числами от 1 до длины первого.
# ['python', 'c#']
# [1,2]
# Вам нужно сделать две функции: первая из которых создаст список кортежей, состоящих из номера и языка, написанного большими буквами.
# [(1,'PYTHON'), (2,'C#')]
# Вторая — которая отфильтрует этот список следующим образом: если сумма очков слова имеет в делителях номер, с которым она в паре в кортеже, то кортеж остается, 
# его номер заменяется на сумму очков.
# [сумма очков c# = 102, в делителях есть 2 с которым в паре. Значит список будет]
# [(1,'PYTHON'), (102,'C#')]
# Если нет — удаляется. Суммой очков называется сложение порядковых номеров букв в слове. Порядковые номера смотрите в этой таблице, в третьем столбце: https://www.charset.org/utf-8
# Это — 16-ричная система, поищите, как правильнее и быстрее получать эти символы.
# Cложите получившиеся числа и верните из функции в качестве ответа вместе с преобразованным списком
# https://dzen.ru/media/simplichka/kak-tekst-hranitsia-v-kompiutere-chast-3-62d3d91515d67a522f78e1e6?&

from functools import reduce
import os
import colorama
from colorama import Fore, Back, Style
colorama.init
os.system("cls")

programming_language = "Python c# Java C++ JavaScript SQL Go html Assembler Pascal"
# language_list = programming_language.split()
# print(language_list)
# language_list = list(map(lambda language: language.upper(), language_list))
# print(language_list)

# sequence_number = []
# print(sequence_number)
# ziped_language = list(zip(sequence_number, language_list))
# print(ziped_language) 



def upper_zip(programming_language):
    language_list = programming_language.split()
    print(f'Исходный список : {language_list}')
    language_list = list(map(lambda language: language.upper(), language_list))
    print(f'Список переведенный в верхний регистр {language_list}')
    sequence_number = [i for i in range(1, len(language_list) + 1)]
    ziped_language = list(zip(sequence_number, language_list))
    print(f'Список кортежей {ziped_language}') 

upper_zip(programming_language)

def utf_dropout(programming_language):
    result_list = []
    language_list = programming_language.split()
    language_list = list(map(lambda language: language.upper(), language_list))
    sequence_number = [i for i in range(1, len(language_list) + 1)]
    recoded_list = []
    for i in range(len(language_list)):
        sum_utf = reduce(lambda a,b: a+b, [ord(char) for char in language_list[i]])
        recoded_list.append(sum_utf)
    
    for i in range(len(sequence_number)):
        if recoded_list[i] % sequence_number[i] == 0:
            result_list.append((recoded_list[i],language_list[i]))
    print(f'Отфильтрованные кортежи {result_list}')


utf_dropout(programming_language)