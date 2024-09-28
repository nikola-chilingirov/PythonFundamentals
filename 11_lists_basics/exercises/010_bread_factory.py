events = input().split('|')
energy = 100
coins = 100
gained_nrg = 0
flag = True
for event in events:
    event_item = event.split('-')
    event_ing = event_item[0]
    value = int(event_item[1])
    if 'rest' == event_ing:
        if energy + value >= 100:
            gained_nrg = 100 - energy
            energy = 100
        else:
            energy += value
            gained_nrg = value
        print(f"You gained {gained_nrg} energy.")
        print(f"Current energy: {energy}.")
    elif 'order' == event_ing:
        if energy >= 30:
            energy -= 30
            coins += value
            print(f"You earned {value} coins.")
        else:
            energy += 50
            print("You had to rest!")
    else:
        if coins >= value:
            coins -= value
            print(f"You bought {event_ing}.")
        else:
            print(f"Closed! Cannot afford {event_ing}.")
            flag = False
            break
if flag:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")