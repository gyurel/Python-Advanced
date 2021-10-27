def collect_score(cl):

    currnent_sum = 0
    for r in range(6):
        current_position = matrix[r][cl]
        if current_position.isdigit():
            currnent_sum += int(current_position)

    return currnent_sum


matrix = [input().split() for x in range(6)]

bucket_coordinates = []

scores_sum = 0

for r in range(6):
    for c in range(6):
        if matrix[r][c] == 'B':
            crnt_coordinate = list((r, c))
            bucket_coordinates.append(crnt_coordinate)

for i in range(3):
    coord = [int(x) for x in input()[1:-1].split(', ')]
    row, col = [x for x in coord]

    if coord in bucket_coordinates:
        score = collect_score(col)
        scores_sum += score
        for el in bucket_coordinates:
            if el == coord:
                bucket_coordinates.remove(el)
    else:
        continue

win_present = ''

if 100 <= scores_sum <= 199:
    win_present = 'Football'
elif 200 <= scores_sum <= 299:
    win_present = 'Teddy Bear'
elif 300 <= scores_sum:
    win_present = 'Lego Construction Set'


if win_present != '':
    print(f"Good job! You scored {scores_sum} points, and you've won {win_present}.")
else:
    print(f"Sorry! You need {100 - scores_sum} points more to win a prize.")
