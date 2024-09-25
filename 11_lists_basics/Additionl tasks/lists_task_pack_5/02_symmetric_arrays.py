n = int(input())
bucket = []
lst = []
for i in range(n):
    array = input().split(' ')
    for x in array:
        bucket.append(int(x))
        lst.append(int(x))
    bucket.reverse()
    if bucket == lst:
        print('Yes')
        bucket = []
        lst = []
    else:
        print('No')
        bucket = []
        lst = []
