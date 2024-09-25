import sys
n = int(input())
temp_sum = 0
max_sum = -sys.maxsize
for i in range(n):
    num = int(input())
    temp_sum = max(num, num + temp_sum)
    if temp_sum > max_sum:
        max_sum = temp_sum
print(max_sum)