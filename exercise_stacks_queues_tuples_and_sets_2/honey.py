# import sys
from collections import deque
# from io import StringIO
#
# test_input1 = """20 62 99 35 0 150
# 120 60 10 1 70 10
# + - + + / * - - /
# """
#
# test_input2 = """30
# 15 9 5 150 8
# * + + * -
# """
#
# sys.stdin = StringIO(test_input1)
# sys.stdin = StringIO(test_input2)

bees = deque([int(x) for x in input().split()])
honey_stack = [int(x) for x in input().split()]
operators = input().split()

operators_dict = {

    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b,

}

total_honey = 0

while bees and honey_stack:
    current_bee = bees[0]
    current_honey = honey_stack[-1]
    current_operator = operators[0]
    current_operation = operators_dict[current_operator]

    if current_honey < current_bee:
        honey_stack.pop()
        continue
    else:
        if current_operator == '/' and current_honey == 0:
            continue
        produced_honey = abs(current_operation(current_bee, current_honey))
        total_honey += produced_honey
        operators.pop(0)
        bees.popleft()
        honey_stack.pop()

print(f"Total honey made: {total_honey}")

if bees:
    print(f"Bees left: {', '.join([str(x) for x in bees])}")

if honey_stack:
    print(f"Nectar left: {', '.join([str(x) for x in honey_stack])}")
