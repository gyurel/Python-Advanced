# import sys
# from io import StringIO
#
# text_input1 = """5 6
# SoftUni
# """
#
# text_input2 = """1 4
# Python
# """
#
# sys.stdin = StringIO(text_input1)
# sys.stdin = StringIO(text_input2)

r, c = [int(x) for x in input().split()]

snake = input()
incrementator = 0
current_snake_index = incrementator % (len(snake) - 1)

matrix = [['' for col in range(c)] for row in range(r)]

for n in range(r):

    if n % 2 == 0:
        for m in range(c):
            matrix[n][m] = snake[current_snake_index]
            incrementator += 1
            current_snake_index = incrementator % len(snake)


    else:
        for m in range(c - 1, -1, -1):
            matrix[n][m] = snake[current_snake_index]
            incrementator += 1
            current_snake_index = incrementator % len(snake)

[print(''.join(x for x in row)) for row in matrix]
