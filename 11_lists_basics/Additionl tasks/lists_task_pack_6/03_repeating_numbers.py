n = int(input())
numbers = []
for i in range(10):
    numbers.append(0)
for i in range(n):
    next_num = int(input())
    numbers[next_num - 1] += 1
max_value = max(numbers)
best_num = 10
for j in range(10):
    if numbers[j] == max_value and best_num > j + 1:
        best_num = j + 1
print(best_num)


