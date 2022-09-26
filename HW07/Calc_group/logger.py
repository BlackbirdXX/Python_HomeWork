from datetime import datetime as dt
from time import time
from dictionary import dict_operations as d


def value_num_logger(data, i):
    time = dt.now().strftime('%H:%M')
    if i == 1:
        with open('log.csv', 'a') as file:
            file.write('\n{};value_a;{}\n'.format(time, data))
    if i == 2:
        with open('log.csv', 'a') as file:
            file.write('{};value_b;{}\n'.format(time, data))


def operation_logger(data):
    time = dt.now().strftime('%H:%M')
    data = d[data]
    with open('log.csv', 'a', encoding='utf-8') as file:
        file.write('{};operation_a_b;{}\n'.format(
            time, data))


def result_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:
        file.write('{};result;{}\n'.format(time, data))
