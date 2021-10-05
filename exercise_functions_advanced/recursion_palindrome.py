def palindrome(string, index):
    length_iter = len(string) // 2

    start_char = string[index]
    end_char = string[len(string) - 1 - index]

    if index + 1 <= length_iter:
        if start_char == end_char:
            index += 1
            return palindrome(string, index)
        else:
            return f"{string} is not a palindrome"

    else:
        return f"{string} is a palindrome"


print(palindrome("abcba", 0))
print(palindrome("peterep", 0))
print(palindrome("aa", 0))
