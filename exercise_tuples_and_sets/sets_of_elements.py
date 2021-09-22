# import sys
# from io import StringIO
#
# test_input1 = """4 3
# 1
# 3
# 5
# 7
# 3
# 4
# 5
# """
#
# test_input2 = """2 2
# 1
# 3
# 1
# 5
# """
#
# # sys.stdin = StringIO(test_input1)
# sys.stdin = StringIO(test_input2)

n, m = [int(x) for x in input().split()]

set_1 = set()
set_2 = set()

[set_1.add(int(input())) for i in range(n)]
[set_2.add(int(input())) for j in range(m)]

set_3 = set_1.intersection(set_2)

[print(el) for el in set_3]
