# import sys
# from io import StringIO
#
# test_input1 = """5
# 0K0K0
# K000K
# 00K00
# K000K
# 0K0K0
# """
#
# test_input2 = """2
# KK
# KK
# """
#
# test_input3 = """8
# 0K0KKK00
# 0K00KKKK
# 00K0000K
# KKKKKK0K
# K0K0000K
# KK00000K
# 00K0K000
# 000K00KK
# """
#
# sys.stdin = StringIO(test_input1)
# sys.stdin = StringIO(test_input2)
# sys.stdin = StringIO(test_input3)

n = int(input())

matrix = [[x for x in input().strip()] for r in range(n)]

max_hits = 0
current_el_row_index = 0
current_el_col_index = 0
needed_to_remove_knights = 0


while True:

    current_hits = 0
    hits_flag = True
    max_hits = 0
    current_el_row_index = 0
    current_el_col_index = 0

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):

            el = matrix[row][col]

            current_hits = 0

            knight1, knight2, knight3, knight4, knight5, knight6, knight7, knight8 = 0, 0, 0, 0, 0, 0, 0, 0

            if el == 'K':

                if 0 <= row - 2 <= len(matrix) - 1 and 0 <= col - 1 <= len(matrix[row]) - 1:
                    if matrix[row - 2][col - 1] == 'K':
                        knight1 = 1

                if 0 <= row - 2 <= len(matrix) - 1 and 0 <= col + 1 <= len(matrix[row]) - 1:
                    if matrix[row - 2][col + 1] == 'K':
                        knight2 = 1

                if 0 <= row - 1 <= len(matrix) - 1 and 0 <= col - 2 <= len(matrix[row]) - 1:
                    if matrix[row - 1][col - 2] == 'K':
                        knight3 = 1

                if 0 <= row - 1 <= len(matrix) - 1 and 0 <= col + 2 <= len(matrix[row]) - 1:
                    if matrix[row - 1][col + 2] == 'K':
                        knight4 = 1

                if 0 <= row + 1 <= len(matrix) - 1 and 0 <= col - 2 <= len(matrix[row]) - 1:
                    if matrix[row + 1][col - 2] == 'K':
                        knight5 = 1

                if 0 <= row + 1 <= len(matrix) - 1 and 0 <= col + 2 <= len(matrix[row]) - 1:
                    if matrix[row + 1][col + 2] == 'K':
                        knight6 = 1

                if 0 <= row + 2 <= len(matrix) - 1 and 0 <= col - 1 <= len(matrix[row]) - 1:
                    if matrix[row + 2][col - 1] == 'K':
                        knight7 = 1

                if 0 <= row + 2 <= len(matrix) - 1 and 0 <= col + 1 <= len(matrix[row]) - 1:
                    if matrix[row + 2][col + 1] == 'K':
                        knight8 = 1

                current_hits = knight1 + knight2 + knight3 + knight4 + knight5 + knight6 + knight7 + knight8

            else:
                continue

            if current_hits > max_hits:
                hits_flag = False
                max_hits = current_hits

                current_el_row_index = row
                current_el_col_index = col

    if hits_flag:
        break

    needed_to_remove_knights += 1
    matrix[current_el_row_index][current_el_col_index] = '0'

print(needed_to_remove_knights)
# print(current_el_row_index)
# print(current_el_col_index)
# [print(' '.join([x for x in row])) for row in matrix]
