group_size = int(input())
days = int(input())
earn_coins = 0
spend_coins = 0
for i in range(1, days + 1):
    if i % 10 == 0:
        group_size -= 2
    if i % 15 == 0:
        group_size += 5
    if i % 3 == 0:
        spend_coins += (3 * group_size)
    if i % 5 == 0:
        earn_coins += (20 * group_size)
        if i % 3 == 0:
            spend_coins += (2 * group_size)
    earn_coins += 50
    spend_coins += (2 * group_size)
total_coins = earn_coins - spend_coins
coins_per_companion = total_coins / group_size
print(f"{group_size} companions received {int(coins_per_companion)} coins each.")
