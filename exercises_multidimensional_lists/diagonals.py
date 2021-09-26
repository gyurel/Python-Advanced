# import sys
# from io import StringIO
#
# test_input1 = """3
# 1, 2, 3
# 4, 5, 6
# 7, 8, 9
# """
#
# sys.stdin = StringIO(test_input1)

n = int(input())

matrix = [[int(number) for number in input().split(', ')] for row in range(n)]

primary_diagonal = [matrix[row][row] for row in range(len(matrix))]
secondary_diagonal = [matrix[row][n - row - 1] for row in range(len(matrix))]


print(f"Primary diagonal: {', '.join(str(x) for x in primary_diagonal)}. Sum: {sum(primary_diagonal)}")
print(F"Secondary diagonal: {', '.join(str(x) for x in secondary_diagonal)}. Sum: {sum(secondary_diagonal)}")
