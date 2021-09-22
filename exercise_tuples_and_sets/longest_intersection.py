# import sys
# from io import StringIO
#
# test_input1 = """3
# 0,3-1,2
# 2,10-3,5
# 6,15-3,10
# """
#
# test_input2 = """5
# 0,10-2,5
# 3,8-1,7
# 1,8-2,4
# 4,7-2,5
# 1,10-2,11
# """
#
# sys.stdin = StringIO(test_input1)
# sys.stdin = StringIO(test_input2)

n = int(input())

longest_intersection = set()
current_sets = []

for i in range(n):
    sets_info = input().split('-')

    for j in range(len(sets_info)):
        current_set = set()
        el = sets_info[j]
        s, e = map(int, el.split(','))

        for k in range(s, e + 1):
            current_set.add(k)
        current_sets.append(current_set)

    current_longest = current_sets[0].intersection(current_sets[1])
    if len(current_longest) > len(longest_intersection):
        longest_intersection = current_longest

    current_sets = []

print(f"Longest intersection is [{', '.join(map(str, longest_intersection))}] with length {len(longest_intersection)}")
