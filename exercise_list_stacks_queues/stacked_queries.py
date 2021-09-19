queries_stack = []

n = int(input())

for _ in range(n):
    current_querie = input()

    if current_querie.startswith("1"):
        command, num = current_querie.split(" ")
        queries_stack.append(int(num))

    elif current_querie == "2":
        if queries_stack:
            queries_stack.pop()
        else:
            continue

    elif current_querie == "3":
        if not queries_stack:
            continue
        print(max(queries_stack))

    elif current_querie == "4":
        if not queries_stack:
            continue
        print(min(queries_stack))

for _ in range(- 1, -len(queries_stack) -1, -1):
    if _ == -len(queries_stack):
        print(queries_stack[_])
    else:
        print(queries_stack[_], end=", ")
