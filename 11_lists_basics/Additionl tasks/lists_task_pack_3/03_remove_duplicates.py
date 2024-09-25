n = input().split(',')
bucket = [n[0]]
for i in n:
    if i in bucket:
        continue
    else:
        bucket.append(i)
print(*bucket, sep=',')