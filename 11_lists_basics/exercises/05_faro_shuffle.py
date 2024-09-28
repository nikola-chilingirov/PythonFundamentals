cards = input().split(" ")
shuffles = int(input())
result = []
for f in range(shuffles):
    if f > 0:
        cards = []
        for x in result:
            cards.append(x)
        result = []
    for i in range(int(len(cards)/2)):
        result.append(cards[i])
        result.append(cards[i + int(len(cards)/2)])
print(result)