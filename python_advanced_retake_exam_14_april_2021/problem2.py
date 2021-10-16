import sys
from io import StringIO

test_input1 = """Ivan, Peter
12 21 18 4 20 7 11
9 D D D D D 10
15 D T T T D 3
2 D T B T D 19
17 D T T T D 6
22 D D D D D 14
5 8 23 13 16 1 24
(3, 3)
"""

test_input2 = """George, Hristo
17 8 21 6 13 3 24
16 D D D D D 14
7 D T T T D 15
23 D T B T D 2
9 D T T T D 22
19 D D D D D 10
12 18 4 20 5 11 1
(1, 0)
(2, 3)
(0, 0)
(4, 2)
(5, 1)
(3, 1)
(0, 0)
(2, 3)
"""

sys.stdin = StringIO(test_input1)
# sys.stdin = StringIO(test_input2)


def is_inside(rw, cl, dimension_darts):
    return 0 <= rw <= dimension_darts - 1 and 0 <= cl <= dimension_darts - 1


def d_hit(board, rw, cl):
    score = int(board[rw][0]) + int(board[rw][n - 1]) + int(board[0][cl]) + int(board[n - 1][cl])
    return score * 2


def t_hit(board, rw, cl):
    score = int(board[rw][0]) + int(board[rw][n - 1]) + int(board[0][cl]) + int(board[n - 1][cl])
    return score * 3


def wins(crnt_player_score):
    if crnt_player_score <= 0:
        return True


players = input().split(', ')

n = 7

players_scores = {key: 501 for key in players}

players_turns = {key: 0 for key in players}

darts_board = [input().split() for row in range(n)]

current_player, second_player = players[0], players[1]

# current_wins = False

shot = input()

while True:

    shot = shot[1:-1].split(', ')

    row = int(shot[0])
    col = int(shot[1])

    if not is_inside(row, col, n):
        players_turns[current_player] += 1
        try:
            shot = input()
        except EOFError:
            break
        continue

    current_hit = darts_board[row][col]
    if current_hit.isdigit():
        players_scores[current_player] -= int(current_hit)
        players_turns[current_player] += 1
        if wins(players_scores[current_player]):
            # current_wins = True
            break

    if current_hit == "D":
        current_score = d_hit(darts_board, row, col)
        players_scores[current_player] -= current_score
        players_turns[current_player] += 1
        if wins(players_scores[current_player]):
            # current_wins = True
            break

    if current_hit == "T":
        current_score = t_hit(darts_board, row, col)
        players_scores[current_player] -= current_score
        players_turns[current_player] += 1
        if wins(players_scores[current_player]):
            # current_wins = True
            break

    if current_hit == "B":
        players_turns[current_player] += 1
        break

    current_player, second_player = second_player, current_player
    try:
        shot = input()
    except EOFError:
        break


print(f"{current_player} won the game with {players_turns[current_player]} throws!")
