def even_odd(*args):
    command = args[-1]
    numbers = args[:-1]
    if command == 'even':
        res_list = [_ for _ in numbers if _ % 2 == 0]
    else:
        res_list = [_ for _ in numbers if _ % 2 == 1]

    return res_list


# print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
