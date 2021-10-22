from collections import deque

males = [int(x) for x in input().split() if int(x) > 0]
females = deque([int(x) for x in input().split() if int(x) > 0])
matches_counter = 0

while males and females:

    current_mail = males[-1]
    current_femail = females[0]

    if current_mail % 25 == 0:
        males.pop()
        males.pop()
        continue

    if current_femail % 25 == 0:
        females.popleft()
        females.popleft()
        continue

    if current_mail == current_femail:
        males.pop()
        females.popleft()
        matches_counter += 1
    else:
        females.popleft()
        males[-1] -= 2
        if males[-1] <= 0:
            males.pop()

print(f"Matches: {matches_counter}")

if males:
    print(f"Males left: {', '.join([str(x) for x in males[::-1]])}")
else:
    print(f"Males left: none")

if females:
    print(f"Females left: {', '.join([str(x) for x in females])}")
else:
    print("Females left: none")
