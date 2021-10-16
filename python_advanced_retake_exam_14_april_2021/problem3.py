def flights(*args):

    flights_dict = {}
    current_key = ''

    for _ in range(len(args)):
        current_el = args[_]

        if current_el == 'Finish':
            break

        if _ % 2 == 0:
            if current_el in flights_dict:
                current_key = current_el
                pass
            else:
                current_key = current_el
                flights_dict[current_key] = 0
        else:
            if current_key in flights_dict:
                flights_dict[current_key] += current_el

    return flights_dict


print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))
