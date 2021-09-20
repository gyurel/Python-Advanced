opening_parenthesis = ['{', '(', '[']
closing_parenthesis = ['}', ')', ']']

left_parenthesis = []
balanced = True

input_string = input()

for ch in input_string:
    if ch in opening_parenthesis:
        left_parenthesis.append(ch)
    elif ch in closing_parenthesis:
        if not left_parenthesis:
            balanced = False
            print("NO")
            break
        opening_index = opening_parenthesis.index(left_parenthesis[-1])
        closing_index = closing_parenthesis.index(ch)
        if opening_index == closing_index:
            left_parenthesis.pop()
        else:
            balanced = False
            print("NO")
            break

if balanced:
    print("YES")
