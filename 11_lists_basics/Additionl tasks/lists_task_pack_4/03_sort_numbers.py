n = input().split(', ')
n_int = []
for i in n:
    n_int.append(int(i))
n_int.sort()
n_int.reverse()
print(*n_int, sep=', ')