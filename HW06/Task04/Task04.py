# Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
# Примеры
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1

import os
import colorama
from colorama import Fore, Back, Style
colorama.init
os.system("cls")

print(Fore.YELLOW + "Программа, которая определить позицию второго вхождения строки в списке либо сообщить, что её нет." + Style.RESET_ALL)

def search_element():
    '''
    Поиск элемента в списке.
    '''
    new_list = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
    print(f"Список строк : {new_list}")
    search_elem = "qwe"
    print(f"Искомый элемент : {search_elem}")
    position = [i for j, i in zip(new_list, list(range(len(new_list)))) if j == search_elem]
    if len(position) > 1:
        print(f"Позиция второго вхождения : {position[1]}")
    else:
        print("Второго вхождения нет.")

search_element()