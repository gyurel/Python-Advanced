def inside(row, col, n):
    return 0 <= row <= n - 1 and 0 <= col <= n - 1


string = input()

n = int(input())

field = [list(input()) for row in range(n)]

row_p = None
col_p = None

for row in range(n):
    for col in range(n):
        current_el = field[row][col]
        if current_el == 'P':
            row_p = row
            col_p = col


m = int(input())

for _ in range(m):

    command = input()
    current_row_p = row_p
    current_col_p = col_p

    if command == 'up':
        current_row_p -= 1
        if not inside(current_row_p, current_col_p, n):
            if len(string) > 0:
                string = string[:-1]
                continue
        current_position = field[current_row_p][current_col_p]
        if current_position == '-':
            field[row_p][col_p] = '-'
            row_p = current_row_p
            col_p = current_col_p
            field[row_p][col_p] = 'P'
        else:
            field[row_p][col_p] = '-'
            string += field[current_row_p][current_col_p]
            row_p = current_row_p
            col_p = current_col_p
            field[row_p][col_p] = 'P'

    if command == 'down':
        current_row_p += 1
        if not inside(current_row_p, current_col_p, n):
            if len(string) > 0:
                string = string[:-1]
                continue
        current_position = field[current_row_p][current_col_p]
        if current_position == '-':
            field[row_p][col_p] = '-'
            row_p = current_row_p
            col_p = current_col_p
            field[row_p][col_p] = 'P'
        else:
            field[row_p][col_p] = '-'
            string += field[current_row_p][current_col_p]
            row_p = current_row_p
            col_p = current_col_p
            field[row_p][col_p] = 'P'

    if command == 'left':
        current_col_p -= 1
        if not inside(current_row_p, current_col_p, n):
            if len(string) > 0:
                string = string[:-1]
                continue
        current_position = field[current_row_p][current_col_p]
        if current_position == '-':
            field[row_p][col_p] = '-'
            row_p = current_row_p
            col_p = current_col_p
            field[row_p][col_p] = 'P'
        else:
            field[row_p][col_p] = '-'
            string += field[current_row_p][current_col_p]
            row_p = current_row_p
            col_p = current_col_p
            field[row_p][col_p] = 'P'

    if command == 'right':
        current_col_p += 1
        if not inside(current_row_p, current_col_p, n):
            if len(string) > 0:
                string = string[:-1]
                continue
        current_position = field[current_row_p][current_col_p]
        if current_position == '-':
            field[row_p][col_p] = '-'
            row_p = current_row_p
            col_p = current_col_p
            field[row_p][col_p] = 'P'
        else:
            field[row_p][col_p] = '-'
            string += field[current_row_p][current_col_p]
            row_p = current_row_p
            col_p = current_col_p
            field[row_p][col_p] = 'P'


print(string)
for row in field:
    print(''.join([str(x) for x in row]))
