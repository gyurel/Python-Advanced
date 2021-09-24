# import sys
from collections import deque
# from io import StringIO
#
# test_input1 = """6 3 - 2 1 * 5 /"""
#
# test_input2 = """2 2 - 1 *"""
#
# test_input3 = """10 23 * 4 2 / 30 10 + 100 50 - 2 -1 *"""
#
# sys.stdin = StringIO(test_input1)
# sys.stdin = StringIO(test_input2)
# sys.stdin = StringIO(test_input3)

expression = input()

numbers = deque()

for ch in expression.split():
    if ch.replace('-', '').isnumeric():
        numbers.append(int(ch))
    else:
        result = numbers.popleft()

        while numbers:
            if ch == "+":
                result += numbers.popleft()
            elif ch == "-":
                result -= numbers.popleft()
            elif ch == "*":
                result *= numbers.popleft()
            elif ch == "/":
                result //= numbers.popleft()

        numbers.append(result)

print(*numbers)
