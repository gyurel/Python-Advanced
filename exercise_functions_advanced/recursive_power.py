def recursive_power(digit, exponent):
    if exponent == 1:
        return digit
    result = digit * recursive_power(digit, exponent - 1)
    return result


print(recursive_power(2, 10))
print(recursive_power(10, 100))
