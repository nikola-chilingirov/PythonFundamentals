lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
spend_aureus = 0
counter_shield = 0
for i in range(1, lost_fights + 1):
    if i % 2 == 0:
        spend_aureus += helmet_price
    if i % 3 == 0:
        spend_aureus += sword_price
        if i % 2 == 0:
            spend_aureus += shield_price
            counter_shield += 1
    if counter_shield % 2 == 0 and counter_shield != 0:
        spend_aureus += armor_price
        counter_shield = 0
print(f'Gladiator expenses: {spend_aureus:.2f} aureus')
