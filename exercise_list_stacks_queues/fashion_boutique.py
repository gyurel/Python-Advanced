clothes_box = [int(x) for x in input().split()]

rack_capacity = int(input())

current_rack_capacity = rack_capacity
rack_counter = 1

while clothes_box:
    if clothes_box[-1] <= current_rack_capacity:
        current_rack_capacity -= clothes_box[-1]
        clothes_box.pop()
    else:
        rack_counter += 1
        current_rack_capacity = rack_capacity

print(rack_counter)
