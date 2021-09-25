# import sys
# from io import StringIO
#
# test_input1 = """1 2 3 4 5
# 1 2 3
# 3
# Add First 5 6
# Remove Second 8 9 11
# Check Subset
# """
#
# test_input2 = """5 4 2 9 9 5 4
# 1 1 1 5 6 5
# 4
# Add First 5 6 9 3
# Add Second 1 2 3 3 3
# Check Subset
# Remove Second 1 2 3 4 5
# """
#
# sys.stdin = StringIO(test_input1)
# sys.stdin = StringIO(test_input2)

set1 = set([int(el) for el in input().split()])
set2 = set([int(el) for el in input().split()])

n = int(input())

for i in range(n):
    command = input()

    if "Add First" in command:
        numbers = command[10:].split()
        for n in numbers:
            set1.add(int(n))

    elif "Add Second" in command:
        numbers1 = command[11:].split()
        for n in numbers1:
            set2.add(int(n))

    elif "Remove First" in command:
        numbers2 = set([int(x) for x in command[13:].split()])
        set1 = set1.difference(numbers2)

    elif "Remove Second" in command:
        numbers3 = set([int(x) for x in command[14:].split()])
        set2 = set2.difference(numbers3)

    elif "Check Subset" in command:
        if set1.issubset(set2) or set2.issubset(set1):
            print("True")
        else:
            print("False")

print(', '.join(sorted([str(x) for x in set1])))
print(', '.join(sorted([str(x) for x in set2])))
