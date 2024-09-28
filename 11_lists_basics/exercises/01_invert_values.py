string = input().split(' ')
lst = []
new_lst = []
end = 0
for i in range(len(string)):
    i_int = int(string[i])
    lst.append(i_int)
a = abs(min(lst))
b = abs(max(lst))
for i in range(len(string)):
    for x in range(-b, a + 1):
        if (x + lst[i]) == 0:
            new_lst.append(x)
            break
        else:
            continue
print(new_lst)
