from collections import deque

def seconds(str_time):
    hh, mm, ss = [int(x) for x in str_time.split(':')]
    result = hh * 3600 + mm * 60 + ss
    return result

def seconds_to_hours(secs):
    secs %= (24 * 60 * 60)
    hours = secs // 3600
    min = (secs % 3600) // 60
    sec = ((secs % 3600) % 60)
    return f"{hours:02d}:{min:02d}:{sec:02d}"

robots = [x.split('-') for x in input().split(';')]

start_time = seconds(input())

for rob in robots:
    rob.append(start_time)

products = deque()

while True:
    product = input()
    if product == 'End':
        break
    products.append(product)

while products:
    start_time += 1
    current_product = products.popleft()
    processed = False

    for i in range(len(robots)):
        rob_name = robots[i][0]
        processing_time = int(robots[i][1])
        busy_until_time = int(robots[i][2])
        if busy_until_time <= start_time:
            busy_until_time = start_time + processing_time
            robots[i].pop(2)
            robots[i].insert(2, busy_until_time)
            print(f"{rob_name} - {current_product} [{seconds_to_hours(start_time)}]")
            processed = True
            break

    if not processed:
        products.append(current_product)
