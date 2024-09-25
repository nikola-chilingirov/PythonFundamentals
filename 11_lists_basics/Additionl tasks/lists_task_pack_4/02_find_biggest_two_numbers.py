n = input().split(' ')
n_int = []
bigger = -10000
biggest = -10000
current = 0
for i in n:
    n_int.append(int(i))
n_int.sort()
n_int.reverse()
last_two = n_int[:2]
print(*last_two, end=' ')
