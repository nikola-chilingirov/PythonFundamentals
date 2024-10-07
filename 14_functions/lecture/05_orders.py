product = input()
quantity = float(input())
price_coffee = 1.50
price_water = 1.00
price_coke = 1.40
price_snacks = 2.00


def price(quan, type_pro):
    result = 0
    if type_pro == 'coffee':
        result = f'{(quan * price_coffee):.2f}'
    elif type_pro == 'water':
        result = f'{(quan * price_water):.2f}'
    elif type_pro == 'coke':
        result = f'{(quan * price_coke):.2f}'
    elif type_pro == 'snacks':
        result = f'{(quan * price_snacks):.2f}'
    return result


print(price(quantity, product))
