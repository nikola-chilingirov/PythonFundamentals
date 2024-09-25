n = int(input())
data = []
for _ in range(n):
    num = int(input())
    data.append(num)
counter = 1
max_counter = -100
for i in range(len(data) - 1):
    a = data[i]
    b = data[i + 1]
    if a == b:
        counter += 1
        if counter > max_counter:
            max_counter = counter
    else:
        counter = 1
print(max_counter)