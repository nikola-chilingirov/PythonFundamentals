n = int(input())
word = input()
lst = []
new_lst = []
for i in range(n):
    data = input()
    lst.append(data)
for i in range(len(lst)):
    if word in lst[i]:
        new_lst.append(lst[i])
    else:
        continue
print(lst)
print(new_lst)
