import sys
from io import StringIO

test_input1 = """. . . . .
x . . . .
. A . . .
. . . x .
. x . . x
3
shoot down
move right 4
move left 1
"""

test_input2 = """. . . . .
. . . . . 
. A x . .
. . . . .
. x . . .
2
shoot down
shoot right
"""

test_input3 = """. . . . .
. . . . .
. . x . .
. . . . .
. x . . A
3
shoot down
move right 2
shoot left
"""

sys.stdin = StringIO(test_input1)
# sys.stdin = StringIO(test_input2)
# sys.stdin = StringIO(test_input3)


def next_step(r, c, direction):
    r, c = directions_dict[direction](r, c)
    return r, c


def is_inside(rw, cl, n):
    if 0 <= rw < n and 0 <= cl < n:
        return True
    return False


n = 5

matrix = [[x for x in input().split()] for r in range(n)]

directions_dict = {

    'up': lambda a, b: (a - 1, b),
    'down': lambda a, b: (a + 1, b),
    'left': lambda a, b: (a, b - 1),
    'right': lambda a, b: (a, b + 1),

}

my_row = None
my_col = None
targets_count = 0
hit_list = []
hit_target = 0


for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        current = matrix[row][col]
        if current == 'A':
            my_row = row
            my_col = col
        elif current == 'x':
            targets_count += 1

cmd_count = int(input())

for _ in range(cmd_count):

    cmd = input().split()
    command = cmd[0]

    if command == 'move':
        direction = cmd[1]
        steps = int(cmd[2])

        for step in range(steps):
            current_row, current_col = next_step(my_row, my_col, direction)
            if is_inside(current_row, current_col, n):
                if matrix[current_row][current_col] == 'x':
                    break
                matrix[my_row][my_col] = '.'
                matrix[current_row][current_col] = 'A'
                my_row = current_row
                my_col = current_col

    elif command == 'shoot':
        direction = cmd[1]

        shoot_row = my_row
        shoot_col = my_col

        while True:
            shoot_row, shoot_col = next_step(shoot_row, shoot_col, direction)
            if is_inside(shoot_row, shoot_col, n):
                if matrix[shoot_row][shoot_col] == 'x':
                    hit_target += 1
                    matrix[shoot_row][shoot_col] = '.'
                    hit_list.append([shoot_row, shoot_col])
                    break
                else:
                    continue
            else:
                break

if targets_count == hit_target:
    print(f"Training completed! All {targets_count} targets hit.")
else:
    print(f"Training not completed! {targets_count - hit_target} targets left.")

for _ in hit_list:
    print(_)
