# import sys
# from io import StringIO
from collections import deque
#
# test_input1 = """10 -5 20 15 -30 10
# 40 60 10 4 10 0
# """
#
# test_input2 = """30 5 15 60 0 30
# -15 10 5 -15 25
# """
#
# sys.stdin = StringIO(test_input1)
# sys.stdin = StringIO(test_input2)

toys_nomenclature = {

    150: 'Doll',
    250: 'Wooden train',
    300: 'Teddy bear',
    400: 'Bicycle',

}

crafted_toys = {}

materials = [int(x) for x in input().split()]
magic = deque([int(x) for x in input().split()])

the_presents_are_crafted = False

while materials and magic:
    current_mat = materials[-1]
    if current_mat == 0:
        materials.pop()
        continue
    current_magic = magic[0]
    if current_magic == 0:
        magic.popleft()
        continue
    result_magic = current_mat * current_magic

    if result_magic < 0:
        callc_sum = materials.pop() + magic.popleft()
        materials.append(callc_sum)
        continue

    if result_magic in toys_nomenclature:
        current_toy = toys_nomenclature[result_magic]
        if current_toy in crafted_toys:
            crafted_toys[current_toy] += 1
        else:
            crafted_toys[current_toy] = 1
        materials.pop()
        magic.popleft()
    elif result_magic not in toys_nomenclature and result_magic > 0:
        magic.popleft()
        materials[-1] += 15
        continue

    if 'Doll' in crafted_toys and 'Wooden train' in crafted_toys or 'Teddy bear' in crafted_toys and 'Bicycle' in crafted_toys:
        the_presents_are_crafted = True

if the_presents_are_crafted:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join(reversed([str(x) for x in materials]))}")

if magic:
    print(f"Magic left: {', '.join([str(x) for x in magic])}")

[print(f"{toy}: {value}")for toy, value in sorted(crafted_toys.items())]
