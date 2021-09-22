# import sys
# from io import StringIO
#
# test_input1 = """6
# George
# George
# George
# Peter
# George
# NiceGuy1234
# """
#
# test_input2 = """10
# Peter
# Maria
# Peter
# George
# Steve
# Maria
# Alex
# Peter
# Steve
# George
# """
#
# # sys.stdin = StringIO(test_input1)
# sys.stdin = StringIO(test_input2)

n = int(input())

unique_names = set()

[unique_names.add(input()) for i in range(n)]

[print(el) for el in unique_names]
