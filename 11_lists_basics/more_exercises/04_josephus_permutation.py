numbers = input().split()
k = int(input())
lst = []
counter = 0
idx = 0
while len(numbers) > 0:
    counter += 1
    if counter % k == 0:
        lst.append(numbers[idx])
        numbers.pop(idx)
    else:
        idx += 1
    if idx >= len(numbers):
        idx = 0
print(str(lst).replace(' ', '').replace('\'', ''))