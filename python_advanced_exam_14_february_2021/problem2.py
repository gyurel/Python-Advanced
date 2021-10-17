# import sys
# from io import StringIO
#
# test_input1 = """5
# 1 X 7 9 11
# X 14 46 62 0
# 15 33 21 95 X
# P 14 3 4 18
# 9 20 33 X 0
# right
# right
# up
# up
# left
# down
# """
#
# test_input2 = """8
# 13 18 9 7 24 41 52 11
# 54 21 19 X 6 4 75 6
# 76 5 7 1 76 27 2 37
# 92 3 25 37 52 X 56 72
# 15 X 1 45 45 X 7 63
# 1 63 P 2 X 43 5 1
# 48 19 35 20 100 27 42 80
# 73 88 78 33 37 52 X 22
# up
# left
# """
#
# sys.stdin = StringIO(test_input1)
# sys.stdin = StringIO(test_input2)


def is_inside(rw, cl):
    return 0 <= rw <= n - 1 and 0 <= cl <= n - 1


n = int(input())

field = [input().split() for row in range(n)]
row_index_p = None
col_index_p = None

for row in range(n):
    for col in range(n):
        current_el = field[row][col]
        if current_el == 'P':
            row_index_p = row
            col_index_p = col

coins = 0
path = []
won = True


while True:
    try:
        command = input()
    except EOFError:
        break

    if command == 'up':
        row_index_p -= 1
        if is_inside(row_index_p, col_index_p) and field[row_index_p][col_index_p] != 'X':
            coins += int(field[row_index_p][col_index_p])
            path.append((row_index_p, col_index_p))
        else:
            coins = int(coins * 0.5)
            won = False
            break

    elif command == 'down':
        row_index_p += 1
        if is_inside(row_index_p, col_index_p) and field[row_index_p][col_index_p] != 'X':
            coins += int(field[row_index_p][col_index_p])
            path.append((row_index_p, col_index_p))
        else:
            coins = int(coins * 0.5)
            won = False
            break

    elif command == 'left':
        col_index_p -= 1
        if is_inside(row_index_p, col_index_p) and field[row_index_p][col_index_p] != 'X':
            coins += int(field[row_index_p][col_index_p])
            path.append((row_index_p, col_index_p))
        else:
            coins = int(coins * 0.5)
            won = False
            break

    elif command == 'right':
        col_index_p += 1
        if is_inside(row_index_p, col_index_p) and field[row_index_p][col_index_p] != 'X':
            coins += int(field[row_index_p][col_index_p])
            path.append((row_index_p, col_index_p))
        else:
            coins = int(coins * 0.5)
            won = False
            break

    else:
        continue

if won and coins >= 100:
    print(f"You won! You've collected {coins} coins.")
else:
    print(f"Game over! You've collected {coins} coins.")

print("Your path:")

for el in path:
    print(f"[{el[0]}, {el[1]}]")
