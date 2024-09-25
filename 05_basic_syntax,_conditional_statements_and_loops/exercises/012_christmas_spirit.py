quantity = int(input())
days_left = int(input())
ornament_set = 2
tree_skirt = 5
tree_garland = 3
tree_lights = 15
total_spirit = 0
budget = 0
for i in range(1, days_left + 1):
    if i % 11 == 0:
        quantity += 2
    if i % 2 == 0:
        budget += (quantity * ornament_set)
        total_spirit += 5
    if i % 3 == 0:
        budget += quantity * (tree_skirt + tree_garland)
        total_spirit += 13
    if i % 5 == 0:
        budget += (quantity * tree_lights)
        total_spirit += 17
        if i % 3 == 0:
            total_spirit += 30
    if i % 10 == 0:
        total_spirit -= 20
        budget += tree_skirt + tree_garland + tree_lights
if days_left % 10 == 0:
    total_spirit -= 30
print(f"Total cost: {budget}")
print(f"Total spirit: {total_spirit}")