from collections import deque

number_of_pumps = int(input())

pumps = deque()

for _ in range(number_of_pumps):
    current_pump = [int(x) for x in input().split()]
    pumps.append(current_pump)

not_complete = True
fuel_in_tank = 0
pumps_counter = 0
current_start_index = 0

while not_complete:
    for i in range(len(pumps)):
        fuel = pumps[i][0]
        distance = pumps[i][1]
        fuel_in_tank += fuel
        if fuel_in_tank >= distance:
            pumps_counter += 1
            fuel_in_tank -= distance
            if pumps_counter == number_of_pumps:
                print(current_start_index)
                not_complete = False
                break
        else:
            pumps.append(pumps.popleft())
            fuel_in_tank = 0
            pumps_counter = 0
            current_start_index += 1
            break
