def odd_or_even(cmd, nrs):
    total = 0

    if cmd == 'Odd':
        for el in nrs:
            if el % 2 == 1:
                total += el
        total *= len(nrs)
    else:
        for el in nrs:
            if el % 2 == 0:
                total += el
        total *= len(nrs)
    return total


command = input()
numbers = [int(x) for x in input().split()]

total = odd_or_even(command, numbers)

print(total)
