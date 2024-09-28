gifts = input().split(' ')
while True:
    command = input().split(' ')
    if 'No' in command:
        break
    elif 'OutOfStock' in command:
        temp = command[1]
        for i in range(len(gifts)):
            if temp in gifts:
                a = gifts.index(temp)
                gifts.pop(a)
                gifts.insert(a, 'None')
            else:
                break
    elif 'Required' in command:
        temp = int(command[2])
        if 0 < temp < len(gifts):
            gifts[temp] = command[1]
    elif 'JustInCase' in command:
        gifts[-1] = command[1]
while "None" in gifts:
    gifts.remove('None')
print(*gifts, sep=' ')
