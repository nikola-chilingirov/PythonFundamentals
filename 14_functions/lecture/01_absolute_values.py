string = input().split()
num_lst = []
for i in string:
    num_lst.append(float(i))
abs_lst = []
for x in num_lst:
    abs_lst.append(abs(x))
print(abs_lst)