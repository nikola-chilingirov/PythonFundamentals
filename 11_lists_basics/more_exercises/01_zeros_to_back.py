data = input()
data = [int(ele) for ele in data.split(', ')]
for i in range(len(data)):
    if data[i] == 0:
        data.remove(0)
        data.append(0)
print(data)