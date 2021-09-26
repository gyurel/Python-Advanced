# import sys
# from io import StringIO
#
# test_input1 = """4 5
# 1 5 5 2 4
# 2 1 4 14 3
# 3 7 11 2 8
# 4 8 12 16 4
# """
#
# test_input2 = """5 6
# 1 0 4 3 1 1
# 1 3 1 3 0 4
# 6 4 1 2 5 6
# 2 2 1 5 4 1
# 3 3 3 6 0 5
# """
#
#
# sys.stdin = StringIO(test_input1)
# sys.stdin = StringIO(test_input2)

n, m = map(int, input().split())

matrix = [[int(x) for x in input().split()] for row in range(n)]

max_sum = float('-inf')
max_square = []

for row in range(n - 2):
    for col in range(m - 2):

        current_square1 = matrix[row][col]
        current_square2 = matrix[row][col + 1]
        current_square3 = matrix[row][col + 2]
        current_square4 = matrix[row + 1][col]
        current_square5 = matrix[row + 1][col + 1]
        current_square6 = matrix[row + 1][col + 2]
        current_square7 = matrix[row + 2][col]
        current_square8 = matrix[row + 2][col + 1]
        current_square9 = matrix[row + 2][col + 2]

        current_sum = current_square1 + current_square2 + current_square3 \
            + current_square4 + current_square5 + current_square6 + current_square7 \
            + current_square8 + current_square9

        if current_sum > max_sum:
            max_sum = current_sum

            max_square = [

                [current_square1, current_square2, current_square3],
                [current_square4, current_square5, current_square6],
                [current_square7, current_square8, current_square9]
            ]

print(f"Sum = {max_sum}")

for row in max_square:
    print(' '.join(str(num) for num in row))
