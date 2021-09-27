# import sys
# from io import StringIO
#
# text_input1 = """2 3
# 1 2 3
# 4 5 6
# swap 0 0 1 1
# swap 10 9 8 7
# swap 0 1 1 0
# END
# """
#
# text_input2 = """1 2
# Hello World
# 0 0 0 1
# swap 0 0 0 1
# swap 0 1 0 0
# END
# """
#
# sys.stdin = StringIO(text_input1)
# sys.stdin = StringIO(text_input2)

r, c = [int(x) for x in input().split()]

matrix = [[x for x in input().split()] for row in range(r)]

cmd = input()

while cmd != 'END':

    command = cmd.split()

    if command[0] == 'swap' and len(command) == 5:

        row1 = int(command[1])
        col1 = int(command[2])
        row2 = int(command[3])
        col2 = int(command[4])

        if 0 <= row1 <= r and 0 <= row2 <= r and 0 <= col1 <= c and 0 <= col2 <= c:

            matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]

            [print(' '.join(seq for seq in row)) for row in matrix]

        else:
            print("Invalid input!")
            cmd = input()
            continue

    else:
        print("Invalid input!")

    cmd = input()
