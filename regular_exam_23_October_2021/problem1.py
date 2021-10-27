from collections import deque


def compare(cur_sum):

    if 100 <= cur_sum <= 199:
        return 'Gemstone'
    elif 200 <= cur_sum <= 299:
        return 'Porcelain Sculpture'
    elif 300 <= cur_sum <= 399:
        return 'Gold'
    elif 400 <= cur_sum <= 499:
        return 'Diamond Jewellery'


def done(presents):
    if presents['Gemstone'] >= 1 and presents['Porcelain Sculpture'] >= 1:
        return True
    if presents['Gold'] >= 1 and presents['Diamond Jewellery'] >= 1:
        return True

    return False


materials = [int(x) for x in input().split()]

magic_level = deque([int(x) for x in input().split()])

presents_dict = {'Gemstone': 0, 'Porcelain Sculpture': 0, 'Gold': 0, 'Diamond Jewellery': 0}

while materials and magic_level:

    current_material = materials[-1]
    current_magic_level = magic_level[0]
    current_sum = current_material + current_magic_level

    result = compare(current_sum)

    if result:
        presents_dict[result] += 1
        materials.pop()
        magic_level.popleft()
        if done(presents_dict):
            break
    else:
        if current_sum < 100 and current_sum % 2 == 0:
            current_material *= 2
            current_magic_level *= 3
            current_sum = current_material + current_magic_level
            result = compare(current_sum)
            if result:
                presents_dict[result] += 1
                materials.pop()
                magic_level.popleft()
                # if done(presents_dict):
                #     break
            else:
                materials.pop()
                magic_level.popleft()
        elif current_sum < 100 and current_sum % 2 == 1:
            current_material *= 2
            current_magic_level *= 2
            current_sum = current_material + current_magic_level
            result = compare(current_sum)
            if result:
                presents_dict[result] += 1
                materials.pop()
                magic_level.popleft()
                # if done(presents_dict):
                #     break
            else:
                materials.pop()
                magic_level.popleft()
        elif current_sum > 499:
            current_material /= 2
            current_magic_level /= 2
            current_sum = current_material + current_magic_level
            result = compare(current_sum)
            if result:
                presents_dict[result] += 1
                materials.pop()
                magic_level.popleft()
                # if done(presents_dict):
                #     break
            else:
                materials.pop()
                magic_level.popleft()

if done(presents_dict):
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f"Materials left: {', '.join([str(x) for x in materials])}")
if magic_level:
    print(f"Magic left: {', '.join([str(x) for x in magic_level])}")

for key, val in sorted(presents_dict.items()):
    if val > 0:
        print(f"{key}: {val}")
