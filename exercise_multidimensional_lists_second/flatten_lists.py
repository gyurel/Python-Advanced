# import sys
# from io import StringIO
#
# test_input1 = """1 2 3 |4 5 6 |  7  88"""
#
# test_input2 = """7 | 4  5|1 0| 2 5 |3"""
#
# test_input3 = """1| 4 5 6 7  |  8 9"""
#
# sys.stdin = StringIO(test_input1)
# sys.stdin = StringIO(test_input2)
# sys.stdin = StringIO(test_input3)

input_string = input().split('|')

matrix = []

for r in range(len(input_string) - 1, -1, -1):

    row = input_string[r].split()
    if len(row) == 0:
        continue

    current_row_list = []
    for el in row:
        current_el = int(el)
        current_row_list.append(current_el)
    matrix.append(current_row_list)

[print(el, end=' ') for row in matrix for el in row]
