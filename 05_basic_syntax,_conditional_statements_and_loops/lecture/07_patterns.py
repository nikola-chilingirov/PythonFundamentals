n = int(input())
for row in range(n):
    for col in range(row + 1):
        print("*", end='')
    print()
for row in range(n - 1, 0, -1):
    for col in range(row):
        print("*", end='')
    print()