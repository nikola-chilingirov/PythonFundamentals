n = int(input())
new_lst = []
lst = []
sort_list = []
for i in range(n):
    num = input().split(',')
    for x in num:
        new_lst.append(int(x))
        lst.append(int(x))
    new_lst.sort()
    if new_lst == lst:
        print('true')
        new_lst = []
        lst = []
    else:
        print('false')
        new_lst = []
        lst = []
