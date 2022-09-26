import check as ch
# import controller as c
from typing import Optional, Union
import logger as log


def get_number(i):
    number_type = ch.check_number_type(
        f'Укажите, какого типа будет число {i}? \n 1 Рациональное \n 2 Комплексное \n')
    if number_type == 1:
        num = ch.check_ratio_number(f'Введите число {i}:\n')
        log.value_num_logger(num, i)
        return num
    elif number_type == 2:
        num = ch.check_complex_number(
            f'Число {i}. Введите через запятую 2 числа. Для комплексного числа вида z = a + bj, первое из них - действительная часть a, второе - мнимая часть b:\n')
        log.value_num_logger(num, i)
        return num


def get_operation():
    operation_a_b = ch.check_number_operation(
        'Какую операцию вы хотите выполнить? \n 1 Сложение \n 2 Вычитание \n 3 Умножение \n 4 Деление \n 5 Возведение в степень\n')
    log.operation_logger(operation_a_b)
    return operation_a_b


def view_result(res: Union[int, float, complex]) -> Optional[str]:
    '''
    Вывод результатов выполнения действия с числами на экран.
    '''
    log.result_logger(res)
    print(f'\nРезультат:\n{res}')
