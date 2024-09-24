number_snowballs = int(input())
snowball_value = 0
temp_snowball_value = 0
temp_weight = 0
temp_time = 0
temp_quality = 0
for i in range(1, number_snowballs + 1):
    weight_of_snowball = int(input())
    time_needed = int(input())
    quality = int(input())
    temp_snowball_value = (weight_of_snowball / time_needed) ** quality
    if temp_snowball_value > snowball_value:
        snowball_value = temp_snowball_value
        temp_weight = weight_of_snowball
        temp_time = time_needed
        temp_quality = quality
        temp_snowball_value = 0
print(f'{temp_weight} : {temp_time} = {int(snowball_value)} ({temp_quality})')