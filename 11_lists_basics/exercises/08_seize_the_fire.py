fires = input().split("#")
water = int(input())
counter_water = 0
counter_effort = 0
total_fire = 0
print('Cells:')
for i in range(len(fires)):
    temp = fires[i].split(' ')
    if 'High' in fires[i]:
        #temp = fires[i].split(' ')
        if 81 <= int(temp[2]) <= 125 and int(temp[2]) <= water:
            print(f"- {temp[2]}")
            water -= int(temp[2])
            counter_effort += 0.25*int(temp[2])
            total_fire += int(temp[2])
            continue
    elif 'Medium' in fires[i]:
        #temp = fires[i].split(' ')
        if 51 <= int(temp[2]) <= 80 and int(temp[2]) <= water:
            print(f"- {temp[2]}")
            water -= int(temp[2])
            counter_effort += 0.25*int(temp[2])
            total_fire += int(temp[2])
            continue
    elif 'Low' in fires[i]:
        #temp = fires[i].split(' ')
        if 1 <= int(temp[2]) <= 50 and int(temp[2]) <= water:
            print(f"- {temp[2]}")
            water -= int(temp[2])
            counter_effort += 0.25*int(temp[2])
            total_fire += int(temp[2])
            continue
print(f"Effort: {counter_effort:.2f}")
print(f"Total Fire: {total_fire}")