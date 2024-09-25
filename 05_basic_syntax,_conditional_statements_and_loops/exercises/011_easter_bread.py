budget = float(input())
price_kg_flour = float(input())
price_pack_eggs = price_kg_flour * 0.75
price_1l_milk = price_kg_flour * 1.25
price_1_4l_milk = price_1l_milk / 4
price_for_loaf = price_kg_flour + price_pack_eggs + price_1_4l_milk
counter_loaf = 0
spend_money = 0
colored_eggs = 0
money_left = budget
while money_left >= price_for_loaf:
    counter_loaf += 1
    spend_money = counter_loaf * price_for_loaf
    colored_eggs += 3
    money_left = budget - spend_money
    if counter_loaf % 3 == 0:
        colored_eggs -= (counter_loaf - 2)

print(f"You made {counter_loaf} loaves of Easter bread! Now you have {colored_eggs} eggs and {money_left:.2f}BGN left.")