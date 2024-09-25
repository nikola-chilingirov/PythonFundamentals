num = input().split(' ')
new_list = []
for i in num:
    y = int(i)
    new_list.append(y)
output_pos = []
output_neg = []
output_null = []
for a in new_list:
    if a < 0:
        output_neg.append(a)
    elif a > 0:
        output_pos.append(a)
    else:
        output_null.append(a)
output = output_neg + output_null + output_pos
print(*output, sep=' ')

