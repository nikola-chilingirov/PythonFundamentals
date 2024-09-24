animals = input().split(', ')
counter = 0
sheep_num = 0
#if animals[-1] == 'wolf':
    #print("Please go away and stop eating my sheep")
for i in animals:
    counter += 1
    if animals[-1] == 'wolf':
        print("Please go away and stop eating my sheep")
        break
    if i == 'wolf':
        sheep_num = (len(animals) - counter)
        print(f'Oi! Sheep number {sheep_num}! You are about to be eaten by a wolf!')
        break
