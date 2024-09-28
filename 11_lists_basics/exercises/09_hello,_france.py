item_price = input().split('|')
budget = float(input())
earn_money = 0
old_price = 0
new_price = []
for i in range(len(item_price)):
    temp = item_price[i].split('->')
    if float(temp[1]) > budget:
        continue
    if "Clothes" in item_price[i] and float(temp[1]) <= 50:
        price_cl = float(temp[1])
        old_price += price_cl
        budget -= price_cl
        earn_money += price_cl * 1.4
        new_price.append(f"{price_cl * 1.4:.2f}")
    elif "Shoes" in item_price[i] and float(temp[1]) <= 35:
        price_sh = float(temp[1])
        old_price += price_sh
        budget -= price_sh
        earn_money += price_sh * 1.4
        new_price.append(f"{price_sh * 1.4:.2f}")
    elif "Accessories" in item_price[i] and float(temp[1]) <= 35:
        price_acc = float(temp[1])
        old_price += price_acc
        budget -= price_acc
        earn_money += price_acc * 1.4
        new_price.append(f"{price_acc * 1.4:.2f}")
profit = earn_money - old_price
print(*new_price, sep=' ')
print(f"Profit: {profit:.2f}")
if (earn_money + budget) >= 150:
    print('Hello, France!')
else:
    print('Not enough money.')
