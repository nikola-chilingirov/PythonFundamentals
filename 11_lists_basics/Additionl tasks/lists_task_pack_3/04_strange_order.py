n = input().split(',')
data = []
bucket = []
for i in n:
    data.append(int(i))
for i in data:
    if i < 0:
        bucket.append(i)
for i in data:
    if i == 0:
        bucket.append(i)
for i in data:
    if i > 0:
        bucket.append(i)
print(*bucket, sep=',')