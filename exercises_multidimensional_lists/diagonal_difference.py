import sys
from io import StringIO

test_input1 = """3
11 2 4
4 5 6
10 8 -12
"""

test_input2 = """4
-7 14 9 -20
3 4 9 21
-14 6 8 44
30 9 7 -14
"""

# sys.stdin = StringIO(test_input1)
sys.stdin = StringIO(test_input2)

n = int(input())

matrix = [[int(number) for number in input().split()] for row in range(n)]

primary_diagonal = [matrix[row][row] for row in range(len(matrix))]
secondary_diagonal = [matrix[row][len(matrix) - row - 1] for row in range(len(matrix))]

result = abs(sum(primary_diagonal) - sum(secondary_diagonal))

print(result)
