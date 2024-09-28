steps = input()
left_car_counter = 0
right_car_counter = 0
res = [int(ele) for ele in steps.split()]
left_car = res[:int((len(res) - 1) / 2)]
right_car = reversed(res[int(((len(res) - 1) / 2) + 1):])
for time_l in left_car:
    left_car_counter += time_l
    if time_l == 0:
        left_car_counter = left_car_counter * 0.8
for time_r in right_car:
    right_car_counter += time_r
    if time_r == 0:
        right_car_counter = right_car_counter * 0.8
if left_car_counter < right_car_counter:
    print(f"The winner is left with total time: {left_car_counter:.1f}")
else:
    print(f"The winner is right with total time: {right_car_counter:.1f}")