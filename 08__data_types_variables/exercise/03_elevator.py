num_of_people = int(input())
capacity = int(input())
if num_of_people < capacity:
    print("1")
else:
    a = num_of_people % capacity
    if a == 0:
        b = num_of_people / capacity
        print(f"{int(b)}")
    else:
        b = num_of_people / capacity
        print(f"{int(b + 1)} ")
