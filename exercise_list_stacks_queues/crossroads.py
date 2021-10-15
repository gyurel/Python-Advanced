# import sys
# from io import StringIO
from collections import deque
#
# test_input1 = """10
# 5
# Mercedes
# green
# Mercedes
# BMW
# Skoda
# green
# END
# """
#
# test_input2 = """9
# 3
# Mercedes
# Hummer
# green
# Hummer
# Mercedes
# green
# END
# """
#
# sys.stdin = StringIO(test_input1)
# sys.stdin = StringIO(test_input2)

green_light_duration = int(input())
free_window_duration = int(input())

cars = deque()
a_crash_happend = False

cmd = input()

total_passed_cars = 0

while not cmd == "END":

    Done = False

    if cmd == 'green':

        current_index = 0
        current_car = cars.popleft()

        for time in range(green_light_duration):
            if current_index == len(current_car) - 1 and time != green_light_duration - 1:
                total_passed_cars += 1
                if len(cars) > 0:
                    current_car = cars.popleft()
                    current_index = 0
                    continue
                else:
                    Done = True
                    break

            elif current_index == len(current_car) - 1 and time == green_light_duration - 1:
                current_car = ''
                total_passed_cars += 1
                Done = True

            current_index += 1

        if not Done and current_car != '':

            for tm in range(free_window_duration):
                if current_car != '' and current_index == len(current_car) - 1:
                    current_car = ''
                    total_passed_cars += 1
                    Done = True
                    break

                if current_car != '' and tm == free_window_duration - 1:
                    current_index += 1
                    break

                current_index += 1

        if not Done and current_car != '':
            print("A crash happened!")
            print(f"{current_car} was hit at {current_car[current_index]}.")
            a_crash_happend = True
            break

    else:
        cars.append(cmd)

    cmd = input()
if not a_crash_happend:
    print("Everyone is safe.")
    print(f"{total_passed_cars} total cars passed the crossroads.")
