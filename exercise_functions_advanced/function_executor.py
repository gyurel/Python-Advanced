def func_executor(*args):
    list_results = []
    for key, val in args:
        list_results.append(key(*val))
    return list_results


def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4))))
