# import sys
# from io import StringIO
#
# test_input1 = """3
# 1 2 3
# 4 5 6
# 7 8 9
# Add 0 0 5
# Subtract 1 1 2
# END
# """
#
# test_input2 = """4
# 1 2 3 4
# 5 6 7 8
# 8 7 6 5
# 4 3 2 1
# Add 4 4 100
# Add 3 3 100
# Subtract -1 -1 42
# Subtract 0 0 42
# END
# """
#
# sys.stdin = StringIO(test_input1)
# sys.stdin = StringIO(test_input2)

n = int(input())

matrix = [[int(x) for x in input().split()] for r in range(n)]

cmd = input()

while cmd != 'END':

    cmd = cmd.split()

    if len(cmd) != 4:
        print("Invalid coordinates")
        continue

    command = cmd[0]
    coordinat_row = int(cmd[1])
    coordinat_col = int(cmd[2])
    value = int(cmd[3])

    if 0 <= coordinat_row <= len(matrix) - 1 and 0 <= coordinat_col <= len(matrix[0]):

        if command == 'Add':

            matrix[coordinat_row][coordinat_col] += value

        elif command == 'Subtract':

            matrix[coordinat_row][coordinat_col] -= value

    else:
        print("Invalid coordinates")

    cmd = input()

for row in matrix:
    print(' '.join([str(x) for x in row]))
