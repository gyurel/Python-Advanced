integers_sequence = list(map(int, input().split()))

reversed_sequence = []

for _ in range(len(integers_sequence)):
    reversed_sequence.append(integers_sequence.pop())

[print(el, end=' ') for el in reversed_sequence]
