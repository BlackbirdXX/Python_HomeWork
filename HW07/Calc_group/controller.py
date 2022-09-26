import user_interface as ui
import operations as op
import check as ch
import os
os.system("cls")


def button_click():
    value_a = ui.get_number(1)
    value_b = ui.get_number(2)
    operation_a_b = ui.get_operation()
    if operation_a_b == 1:
        result = op.sum_numbers(value_a, value_b)
    elif operation_a_b == 2:
        result = op.diff_numbers(value_a, value_b)
    elif operation_a_b == 3:
        result = op.mult_numbers(value_a, value_b)
    elif operation_a_b == 4:
        ch.check_exceptions_div(value_a, value_b)
        result = op.div_numbers(value_a, value_b)
    elif operation_a_b == 5:
        ch.check_exceptions_exp(value_a, value_b)
        result = op.exp_numbers(value_a, value_b)
    ui.view_result(result)
