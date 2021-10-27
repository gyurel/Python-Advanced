def shopping_list(budget, **kwargs):

    bought_products = []

    if budget < 100:
        return "You do not have enough budget."

    for key, val in kwargs.items():
        current_sum = kwargs[key][0] * kwargs[key][1]
        if current_sum <= budget:
            bought_products.append(f"You bought {key} for {current_sum:.2f} leva.")
            budget -= current_sum
            if len(bought_products) == 5:
                break

    return '\n'.join([x for x in bought_products])


# print(shopping_list(100,
#                     microwave=(70, 2),
#                     skirts=(15, 4),
#                     coffee=(1.50, 10),
#                     ))

# print(shopping_list(20,
#                     jeans=(19.99, 1),
#                     ))

print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))
