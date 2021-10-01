# import sys
# from io import StringIO
#
# test_input1 = """5
# 1 3 7 9 11
# X 5 4 X 63
# 7 3 21 95 1
# B 1 73 4 9
# 9 2 33 2 0
# """
#
# test_input2 = """3
# 1 5 5
# 5 X 5
# 5 X B
# """
#
# test_input3 = """8
# 4 18 9 7 24 41 52 11
# 54 21 19 X 6 34 75 57
# 76 67 7 44 76 27 56 37
# 92 35 25 37 52 34 56 72
# 35 X 1 45 4 X 37 63
# 105 X B 2 12 43 5 19
# 48 19 35 20 32 27 42 4
# 73 88 78 32 37 52 X 22
# """
#
# sys.stdin = StringIO(test_input1)
# sys.stdin = StringIO(test_input2)
# sys.stdin = StringIO(test_input3)

def go_left(destination, dir_dict, sum_dict, matrix, row_b, col_b):
    if col_b == 0:
        dir_dict[destination] = []
        return dir_dict, sum_dict

    current_sum = 0
    current_indexes = []

    for col in range(col_b - 1, -1, -1):
        current_value = matrix[row_b][col]
        if current_value == 'X':
            break

        current_sum += int(current_value)
        current_indexes.append([row_b, col])

    dir_dict[destination] = current_indexes
    if current_sum > sum_dict[1]:
        sum_dict[0] = destination
        sum_dict[1] = current_sum

    return dir_dict, sum_dict


def go_right(destination, dir_dict, sum_dict, matrix, row_b, col_b):
    if col_b == len(matrix[row_b]) - 1:
        dir_dict[destination] = []
        return dir_dict, sum_dict

    current_sum = 0
    current_indexes = []

    for col in range(col_b + 1, len(matrix[row_b])):
        current_value = matrix[row_b][col]
        if current_value == 'X':
            break

        current_sum += int(current_value)
        current_indexes.append([row_b, col])

    dir_dict[destination] = current_indexes
    if current_sum > sum_dict[1]:
        sum_dict[0] = destination
        sum_dict[1] = current_sum

    return dir_dict, sum_dict

def go_up(destination, dir_dict, sum_dict, matrix, row_b, col_b):
    if row_b == 0:
        dir_dict[destination] = []
        return dir_dict, sum_dict

    current_sum = 0
    current_indexes = []

    for row in range(row_b - 1, - 1, -1):
        current_value = matrix[row][col_b]
        if current_value == 'X':
           break

        current_sum += int(current_value)
        current_indexes.append([row, col_b])

    dir_dict[destination] = current_indexes
    if current_sum > sum_dict[1]:
        sum_dict[0] = destination
        sum_dict[1] = current_sum

    return dir_dict, sum_dict

def go_down(destination, dir_dict, sum_dict, matrix, row_b, col_b):
    if row_b == len(matrix) - 1:
        dir_dict[destination] = []
        return dir_dict, sum_dict

    current_sum = 0
    current_indexes = []

    for row in range(row_b + 1, len(matrix)):
        current_value = matrix[row][col_b]
        if current_value == 'X':
           break

        current_sum += int(current_value)
        current_indexes.append([row, col_b])

    dir_dict[destination] = current_indexes
    if current_sum > sum_dict[1]:
        sum_dict[0] = destination
        sum_dict[1] = current_sum

    return dir_dict, sum_dict



n = int(input())

matrix = [[x for x in input().strip().split()] for r in range(n)]

directions_dict = {'right': [], 'left': [], 'up': [], 'down': []}
# sums_dict = {'left': 0, 'right': 0, 'up': 0, 'down': 0}
sums_dict = ['', float('-inf')]

row_b = None
col_b = None

for row in range(n):
    for col in range(n):
        if matrix[row][col] == 'B':
            row_b = row
            col_b = col


for destination in directions_dict:
    if destination == 'left':
        directions_dict, sums_dict = go_left(destination, directions_dict, sums_dict, matrix, row_b, col_b)

    elif destination == 'right':
        directions_dict, sums_dict = go_right(destination, directions_dict, sums_dict, matrix, row_b, col_b)

    elif destination == 'up':
        directions_dict, sums_dict = go_up(destination, directions_dict, sums_dict, matrix, row_b, col_b)

    elif destination == 'down':
        directions_dict, sums_dict = go_down(destination, directions_dict, sums_dict, matrix, row_b, col_b)

# print(directions_dict)
# print(sums_dict)
best_direction = sums_dict[0]
total_number_eggs = sums_dict[1]
print(best_direction)
[print(val) for val in directions_dict[best_direction]]
print(total_number_eggs)
