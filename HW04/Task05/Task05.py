# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. Входные и выходные данные хранятся в отдельных текстовых файлах.
# файл первый:
# AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool
# файл второй:
# сжатый текст.

import os
import colorama
from colorama import Fore, Back, Style
colorama.init
os.system("cls")
print(Fore.YELLOW + 'Программа, которая реализует модуль сжатия и восстановления данных. Входные и выходные данные записывает в отдельные текстовые файлы.')
print(Style.RESET_ALL)
message = 'AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooooll!!!'
path_in = 'E:/Learning/Python/PythonHomeWork/HW04/Task05/compression.txt'
path_out = 'E:/Learning/Python/PythonHomeWork/HW04/Task05/decompression.txt'

def write_file(path,message):
    with open(path, 'w+',  encoding= 'utf-8') as data:
        data.write(message)

def rle_compression(data):
    compression = '' 
    pre_char = '' 
    count = 1 
    if not data: return '' 
    for char in data: 
        if char != pre_char:
            if pre_char: 
                if count == 1:
                    compression += pre_char
                else:
                    compression += str(count) + pre_char 
            count = 1 
            pre_char = char 
        else: 
            count += 1 
    else:
        compression += str(count) + pre_char 
        return compression

compression_message = rle_compression(message)
write_file(path_in, compression_message)
print(f'Исходный текст : {message}')
print(f'Сжатый текст : {compression_message}')

def rle_decompression(data): 
    decompression = '' 
    count = '' 
    for char in data: 
        if char.isdigit(): 
            count += char 
        else:  
            if not count:
                count = 1
            decompression += char * int(count) 
            count = '' 
    return decompression

decompression = rle_decompression(compression_message)
write_file(path_out, decompression)

print(f'Текст после распаковки : {decompression}')

