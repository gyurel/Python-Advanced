def math_operations(*args, **kwargs):

    kwargs = [(key, int(val)) for key, val in kwargs.items()]

    for i in range(len(args)):
        digit2 = args[i]
        operand = kwargs[i % len(kwargs)][0]
        digit1 = kwargs[i % len(kwargs)][1]

        if operand == 'a':
            result = digit1 + digit2
            kwargs[i % len(kwargs)] = (kwargs[i % len(kwargs)][0], result)
        elif operand == 's':
            result = digit1 - digit2
            kwargs[i % len(kwargs)] = (kwargs[i % len(kwargs)][0], result)
        elif operand == 'd':
            if digit2 == 0:
                continue
            result = digit1 / digit2
            kwargs[i % len(kwargs)] = (kwargs[i % len(kwargs)][0], result)
        elif operand == 'm':
            result = digit1 * digit2
            kwargs[i % len(kwargs)] = (kwargs[i % len(kwargs)][0], result)

    kwargs = {x[0]: x[1] for x in kwargs}

    return kwargs


print(math_operations(2, 12, 0, -3, 6, -20, -11, a=1, s=7, d=33, m=15))
print(math_operations(-1, 0, 1, 0, 6, -2, 80, a=0, s=0, d=0, m=0))
print(math_operations(6, a=0, s=0, d=0, m=0))
