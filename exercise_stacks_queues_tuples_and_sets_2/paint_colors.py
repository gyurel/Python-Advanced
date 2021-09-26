# import sys
from collections import deque
# from io import StringIO
#
# test_input1 = """d yel blu e low redd"""
#
# test_input2 = """r ue nge ora bl ed"""
#
# test_input3 = """re ple blu pop e pur d"""
#
# sys.stdin = StringIO(test_input1)
# sys.stdin = StringIO(test_input2)
# sys.stdin = StringIO(test_input3)

main_colors = ["red", "yellow", "blue"]
secondary_colors = {


    "orange": {'red', 'yellow'},
    "purple": {'red', 'blue'},
    "green": {'yellow', 'blue'},

}

found_color = []

substrings = deque(input().split())

while substrings:

    if len(substrings) == 1:
        current_color = substrings.popleft()
        if current_color in main_colors or current_color in secondary_colors:
            found_color.append(current_color)
            continue
        else:
            continue

    first_substring = substrings.popleft()
    second_substring = substrings.pop()

    combination_1 = first_substring + second_substring
    combination_2 = second_substring + first_substring

    if combination_1 in main_colors or combination_1 in secondary_colors:
        found_color.append(combination_1)
    elif combination_2 in main_colors or combination_2 in secondary_colors:
        found_color.append(combination_2)
    else:
        first_substring = first_substring[:-1]
        second_substring = second_substring[:-1]

        index = len(substrings) // 2

        substrings.insert(index, first_substring)
        substrings.insert(index, second_substring)

found_colors = found_color

for color in found_color:
    if color in main_colors:
        continue
    needed_colors = secondary_colors[color]

    for col in needed_colors:
        if col in found_color:
            continue
        else:
            found_colors.remove(color)
            break

print(found_colors)
