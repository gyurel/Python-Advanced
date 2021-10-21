def stock_availability(*args):
    inventory_list = args[0]
    cmd = args[1]

    if cmd == 'delivery':
        delivery_list = args[2:]
        [inventory_list.append(x) for x in delivery_list]
    elif cmd == 'sell':
        sell_list = args[2:]
        if len(sell_list) != 0 and isinstance(sell_list[0], int):
            for i in range(int(sell_list[0])):
                inventory_list.pop(0)
        elif len(sell_list) != 0 and isinstance(sell_list[0], str):
            for el in sell_list:
                while el in inventory_list:
                    inventory_list.remove(el)
        else:
            inventory_list.pop(0)

    return inventory_list


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie", "banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
