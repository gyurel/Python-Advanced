def concatenate(*args):
    string = ''
    for el in args:
        string += el

    return string


# print(concatenate("Soft", "Uni", "Is", "Great", "!"))
print(concatenate("I", " ", "Love", " ", "Python"))
