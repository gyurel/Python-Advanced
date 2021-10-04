def age_assignment(*args, **kwargs):
    names_ages = {}
    for el in args:
        for key, val in kwargs.items():
            if key == el[0]:
                names_ages[el] = val

    return names_ages


print(age_assignment("Peter", "George", G=26, P=19))
# print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
