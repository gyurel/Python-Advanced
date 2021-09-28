import sys
from io import StringIO

text_input1 = """4 6"""

text_input2 = """3 2"""

sys.stdin = StringIO(text_input1)
# sys.stdin = StringIO(text_input2)

r, c = [int(x) for x in input().split()]

matrix = []

for n in range(r):
    current_row = []
    for m in range(c):
        current_sequence = chr(97 + n) + chr(97 + n + m) + chr(97 + n)
        current_row.append(current_sequence)
    matrix.append(current_row)

[print(' '.join(seq for seq in row)) for row in matrix]
