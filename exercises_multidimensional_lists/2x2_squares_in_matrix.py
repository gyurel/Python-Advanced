# import sys
# from io import StringIO
#
# test_input1 = """3 4
# A B B D
# E B B B
# I J B B
# """
#
# test_input2 = """2 2
# a b
# c d
# """
#
# test_input3 = """5 4
# A A B D
# A A B B
# I J B B
# C C C G
# C C K P
# """
#
# sys.stdin = StringIO(test_input1)
# sys.stdin = StringIO(test_input2)
# sys.stdin = StringIO(test_input3)

n, m = map(int, input().split())

matrix = [[x for x in input().split()] for row in range(n)]

square_counter = 0

for row in range(n -1):
    for col in range(m - 1):
        current_square1 = matrix[row][col]
        current_square2 = matrix[row][col + 1]
        current_square3 = matrix[row + 1][col]
        current_square4 = matrix[row + 1][col + 1]

        if current_square1 == current_square2 and current_square1 == current_square3 and current_square1 == current_square4:
            square_counter += 1

print(square_counter)
