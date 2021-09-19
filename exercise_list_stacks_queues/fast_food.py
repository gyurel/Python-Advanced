from collections import deque

food_quantity = int(input())

food_queue = deque([int(x) for x in input().split()])

print(max(food_queue))

not_complete = False

while food_queue:
    if food_queue[0] <= food_quantity:
        food_quantity -= food_queue[0]
        food_queue.popleft()
    else:
        print(f"Orders left:", end=' ')
        for _ in range(len(food_queue)):
            concurrent_el = food_queue[_]
            if _ == len(food_queue) - 1:
                print(concurrent_el)
            else:
                print(concurrent_el, end=' ')
        not_complete = True
        break

if not not_complete:
    print("Orders complete")
