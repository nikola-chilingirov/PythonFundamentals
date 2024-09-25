budget = int(input())
price = input()
amount = 0
while price != 'End':
    price_1 = int(price)
    amount += price_1
    if amount > budget:
        print('You went in overdraft!')
        break
    price = input()
if price == 'End':
    print("You bought everything needed.")