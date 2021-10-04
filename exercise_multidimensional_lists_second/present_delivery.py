# import sys
# from io import StringIO
#
# test_input1 = """5
# 4
# - X V -
# - S - V
# - - - -
# X - - -
# up
# right
# down
# right
# Christmas morning
# """
#
# test_input2 = """3
# 4
# - - - -
# V - X -
# - V C V
# - - - S
# left
# up
# """
#
# sys.stdin = StringIO(test_input1)
# sys.stdin = StringIO(test_input2)


def cookies_to_everybody(r, c, matx, pres):
    cells_dict = {

        'up': (r - 1, c),
        'down': (r + 1, c),
        'left': (r, c - 1),
        'right': (r, c + 1),

        }

    for key, val in cells_dict.items():
        current_cell = matx[val[0]][val[1]]
        if current_cell != '-':
            pres -= 1
            matx[val[0]][val[1]] = '-'

    return matx, pres


def is_inside(rw, cl, n):
    if 0 <= rw < n and 0 <= cl < n:
        return True
    return False


presents = int(input())

n = int(input())

matrix = []
nice_kids = 0
santa_row = None
santa_col = None


for row in range(n):
    current_row = input().split()
    matrix.append(current_row)
    for col in range(len(current_row)):
        current_el = current_row[col]
        if current_el == 'S':
            santa_row = row
            santa_col = col
        if current_el == 'V':
            nice_kids += 1


while True:

    if presents <= 0:
        break

    cmd = input()

    if cmd == 'Christmas morning':
        break

    current_row = santa_row
    current_col = santa_col

    if cmd == "up":
        current_row -= 1
    elif cmd == "down":
        current_row += 1
    elif cmd == "left":
        current_col -= 1
    elif cmd == "right":
        current_col += 1

    if is_inside(current_row, current_col, n):
        matrix[santa_row][santa_col] = '-'
        current_house = matrix[current_row][current_col]

        if current_house == 'V':
            presents -= 1
        elif current_house == 'X':
            pass
        elif current_house == 'C':
            matrix, presents = cookies_to_everybody(current_row, current_col, matrix, presents)

        matrix[current_row][current_col] = 'S'
        santa_row, santa_col = current_row, current_col

    else:
        continue

nice_kids_left = 0
for rw in matrix:
    for el in rw:
        if el == 'V':
            nice_kids_left += 1

if presents <= 0 and nice_kids_left > 0:
    print("Santa ran out of presents!")

for r in matrix:
    print(*r)

if nice_kids_left == 0:
    print(f"Good job, Santa! {nice_kids} happy nice kid/s.")
elif nice_kids_left > 0:
    print(f"No presents for {nice_kids_left} nice kid/s.")
