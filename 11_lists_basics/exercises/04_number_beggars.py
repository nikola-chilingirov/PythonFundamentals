money = input()
res = [int(ele) for ele in money.split(", ")]
beggars = int(input())
lst = []
result = []
for x in range(beggars):
    lst.append([])
    for i in range(0 + x, len(res), beggars):
        lst[x].append(res[i])
for z in range(len(lst)):
    total = sum(lst[z])
    result.append(total)
print(result)