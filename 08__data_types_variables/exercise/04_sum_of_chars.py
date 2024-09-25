n = int(input())
result = 0
for i in range(n):
    data = input()
    result += ord(data)
print(f"The sum equals: {result}")