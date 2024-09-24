n = int(input())
total = 255
temp = 0
for i in range(0, n):
    ltr = int(input())
    temp += ltr
    if temp <= total:
        total -= temp
        temp = 0
    else:
        print("Insufficient capacity!")
        temp = 0
        continue
print(f"{255 - total}")