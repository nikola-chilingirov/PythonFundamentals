key = int(input())
n = int(input())
result = ''
for i in range(n):
    data = input()
    result += chr(ord(data) + key)
print(result)
