numbers = input()
n = int(input())
res = [int(ele) for ele in numbers.split(' ')]
for i in range(n):
    a = min(res)
    res.remove(a)
print(*res, sep=', ')