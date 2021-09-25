# import sys
from collections import deque
# from io import StringIO
#
# test_input1 = """20, 24, -5, 17, 22, 60, 26
# 26, 60, 22, 17, 24, 10, 55
# """
#
# test_input2 = """-10, -2, -30, 10
# -5
# """
#
# test_input3 = """2, 3, 3, 7, 2
# 2, 7, 3, 3, 2, 14, 6
# """
#
# sys.stdin = StringIO(test_input1)
# sys.stdin = StringIO(test_input2)
# sys.stdin = StringIO(test_input3)

chocolates = []
cups_of_milk = deque()

[chocolates.append(int(x)) for x in input().split(', ')]
[cups_of_milk.append(int(x)) for x in input().split(', ')]

milkshake_counter = 0

while chocolates and cups_of_milk and milkshake_counter < 5:
    if chocolates[-1] <= 0 or chocolates[-1] > 100:
        chocolates.pop()
        continue

    if cups_of_milk[0] <= 0 or cups_of_milk[0] > 100:
        cups_of_milk.popleft()
        continue

    if chocolates[-1] == cups_of_milk[0]:
        milkshake_counter += 1
        chocolates.pop()
        cups_of_milk.popleft()
    else:
        cups_of_milk.append(cups_of_milk.popleft())
        chocolates[-1] -= 5

if milkshake_counter == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolates:
    print(f"Chocolate: {', '.join([str(x) for x in chocolates])}")

else:
    print("Chocolate: empty")

if cups_of_milk:
    print(f"Milk: {', '.join([str(x)for x in cups_of_milk])}")

else:
    print("Milk: empty")
