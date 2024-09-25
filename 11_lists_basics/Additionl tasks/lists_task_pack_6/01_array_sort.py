line = [int(i) for i in input().split(',')]
new_line_0 = []
new_line_num = []
for x in line:
    if x == 0:
        new_line_0.append(x)
    else:
        new_line_num.append(x)
print(*(new_line_num + new_line_0), sep=',')
