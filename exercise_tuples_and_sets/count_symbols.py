# import sys
# from io import StringIO
#
# test_input1 = """SoftUni rocks"""
#
# test_input2 = """Why do you like Python?"""
#
# sys.stdin = StringIO(test_input1)
# sys.stdin = StringIO(test_input2)

characters_dict = {}

for ch in input():
    if ch in characters_dict:
        characters_dict[ch] += 1
    else:
        characters_dict[ch] = 1

for key, val in sorted(characters_dict.items()):
    print(f"{key}: {val} time/s")
