# import sys
# from io import StringIO
#
# test_input1 = """4
# Pesho
# Stefan
# Stamat
# Gosho
# """
#
# test_input2 = """6
# Preslav
# Gosho
# Ivan
# Stamat
# Pesho
# Stefan
# """
#
# sys.stdin = StringIO(test_input1)
# sys.stdin = StringIO(test_input2)

n = int(input())

even_numbers = set()
odd_numbers = set()

for i in range(1, n + 1):
    current_name = input()

    current_sum = 0
    for ch in current_name:
        current_sum += ord(ch)

    current_sum //= i

    if current_sum % 2 == 0:
        even_numbers.add(current_sum)
    else:
        odd_numbers.add(current_sum)

if sum(even_numbers) == sum(odd_numbers):
    print(', '.join(map(str, even_numbers.union(odd_numbers))))

elif sum(odd_numbers) > sum(even_numbers):
    print(', '.join(map(str, odd_numbers.difference(even_numbers))))

elif sum(even_numbers) > sum(odd_numbers):
    print(', '.join(map(str, even_numbers.symmetric_difference(odd_numbers))))
