# import sys
# from io import StringIO
#
# test_input1 = """4
# Ce O
# Mo O Ce
# Ee
# Mo
# """
#
# test_input2 = """3
# Ge Ch O Ne
# Nb Mo Tc
# O Ne
# """
#
# sys.stdin = StringIO(test_input1)
# sys.stdin = StringIO(test_input2)

n = int(input())

unique_elements = set()

[unique_elements.add(y) for x in range(n) for y in input().split()]

[print(el) for el in unique_elements]
