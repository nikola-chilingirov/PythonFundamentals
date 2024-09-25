num = input().split(' ')
num_int = []
flag = True
for x in num:
    num_int.append(int(x))
if num_int[0] == num_int[1]:
    flag = False
if num_int[0] > num_int[1]:
    for j in range(len(num_int) - 1):
        if j % 2 == 0:
            if num_int[j] > num_int[j + 1]:
                flag = True
            else:
                flag = False
                break
        elif j % 2 != 0:
            if num_int[j] < num_int[j + 1]:
                flag = True
            else:
                flag = False
                break
elif num_int[0] < num_int[1]:
    for j in range(len(num_int) - 1):
        if j % 2 == 0:
            if num_int[j] < num_int[j + 1]:
                flag = True
            else:
                flag = False
                break
        elif j % 2 != 0:
            if num_int[j] > num_int[j + 1]:
                flag = True
            else:
                flag = False
                break
if flag:
    print('yes')
else:
    print('no')