# import sys
from collections import deque
# from io import StringIO
#
# test_input1 = """5, 6, 4, 16, 11, 5, 30, 2, 3, 27
# 1, 13, 5, 3, -7, 32, 19, 3, 5, 7, 22
# """
#
# test_input2 = """-15, -8, 0, -16, 0, -22
# 10, 5
# """
#
# sys.stdin = StringIO(test_input1)
# sys.stdin = StringIO(test_input2)


def fireworks_done(frwks):
    return frwks['Crossette Fireworks'] >= 3 and frwks['Willow Fireworks'] >= 3\
           and frwks['Palm Fireworks'] >= 3


effects = deque([int(x) for x in input().split(', ') if int(x) > 0])
power = [int(x) for x in input().split(', ') if int(x) > 0]

fireworks = {'Palm Fireworks': 0, 'Willow Fireworks': 0, 'Crossette Fireworks': 0}
done = False

while effects and power and not done:

    current_effect = effects[0]
    current_power = power[-1]
    current_sum = current_effect + current_power

    if current_sum % 3 == 0 and current_sum % 5 == 0:
        fireworks['Crossette Fireworks'] += 1
        effects.popleft()
        power.pop()
        if fireworks_done(fireworks):
            done = True
    elif current_sum % 3 == 0:
        fireworks['Palm Fireworks'] += 1
        effects.popleft()
        power.pop()
        if fireworks_done(fireworks):
            done = True
    elif current_sum % 5 == 0:
        fireworks['Willow Fireworks'] += 1
        effects.popleft()
        power.pop()
        if fireworks_done(fireworks):
            done = True
    else:
        current_effect = current_effect - 1
        effects.popleft()
        effects.append(current_effect)


if done:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")

if effects:
    print(f"Firework Effects left: {', '.join([str(x) for x in effects])}")

if power:
    print(f"Explosive Power left: {', '.join([str(x) for x in power])}")

for key, val in fireworks.items():
    print(f"{key}: {val}")
