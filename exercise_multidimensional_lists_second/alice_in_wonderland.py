# import sys
# from io import StringIO
#
# test_input1 = """5
# . A . . 1
# R . 2 . .
# 4 7 . 1 .
# . . . 2 .
# . 3 . . .
# down
# right
# left
# down
# up
# left
# """
#
# test_input2 = """7
# . A . 1 1 . .
# 9 . . . 6 . 5
# . 6 . R . . .
# . 3 . . 1 . .
# . . . 2 . . 2
# . 3 . . 1 . .
# . 8 3 . . . 2
# left
# down
# down
# right
# """
#
# sys.stdin = StringIO(test_input1)
# sys.stdin = StringIO(test_input2)


def next_step(r, c, direction):
    r, c = directions_dict[direction](r, c)
    return r, c


def is_inside(rw, cl, n):
    if 0 <= rw < n and 0 <= cl < n:
        return True
    return False


n = int(input())

matrix = [[x for x in input().split()] for r in range(n)]

directions_dict = {

    'up': lambda a, b: (a - 1, b),
    'down': lambda a, b: (a + 1, b),
    'left': lambda a, b: (a, b - 1),
    'right': lambda a, b: (a, b + 1),

}

alice_row = None
alice_col = None

alice_found = False

for row in range(len(matrix)):
    if alice_found:
        break
    for col in range(len(matrix[row])):
        current = matrix[row][col]
        if current == 'A':
            alice_row = row
            alice_col = col
            matrix[alice_row][alice_col] = '*'
            alice_found = True
            break

tea_bags = 0

while True:

    command = input()

    alice_row, alice_col = next_step(alice_row, alice_col, command)

    if is_inside(alice_row, alice_col, n):
        if matrix[alice_row][alice_col].isdigit():
            tea_bags += int(matrix[alice_row][alice_col])
            matrix[alice_row][alice_col] = '*'
            if tea_bags >= 10:
                break
        elif matrix[alice_row][alice_col] == '*' or matrix[alice_row][alice_col] == '.':
            matrix[alice_row][alice_col] = '*'
            continue
        elif matrix[alice_row][alice_col] == 'R':
            matrix[alice_row][alice_col] = '*'
            break
    else:
        went_to_party = False
        break

if tea_bags >= 10:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")

[print(' '.join(val for val in row)) for row in matrix]
