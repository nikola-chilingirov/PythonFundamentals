temp = input()
temp_int = temp.split(' ')
new_list = []
for i in temp_int:
    y = float(i)
    new_list.append(y)
temp_f = ''
for x in temp_int:
    temp_f = (float(x) * 1.8) + 32
    print(round(temp_f))