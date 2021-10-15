# import sys
from collections import deque
# from io import StringIO
#
# test_input1 = """11, 6, 8, 1
# 3, 1, 9, 10, 5, 9, 1
# """
#
#
# test_input2 = """10, 9, 8, 7, 5
# 5, 10, 9, 8, 7
# """
#
# test_input3 = """12, -3, 14, 3, 2, 0
# 10, 15, 4, 6, 3, 1, 22, 1
# """
#
# sys.stdin = StringIO(test_input1)
# sys.stdin = StringIO(test_input2)
# sys.stdin = StringIO(test_input3)


orders = deque([int(x) for x in input().split(', ') if 0 < int(x) <= 10])
employees = [int(x) for x in input().split(', ')]
total_pizzas = 0


while orders and employees:

    current_order = orders[0]
    current_employee = employees[-1]

    if current_order <= current_employee:
        total_pizzas += current_order
        orders.popleft()
        employees.pop()
    if current_order > current_employee:
        total_pizzas += current_employee
        rest = current_order - current_employee
        employees.pop()
        orders[0] = rest

if not orders:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {total_pizzas}")
    print(f"Employees: {', '.join(map(str, employees))}")
elif not employees:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join(map(str, orders))}")
