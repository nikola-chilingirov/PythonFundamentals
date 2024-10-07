string = input().split()
lst_num = []
for i in string:
    lst_num.append(float(i))
lst_round = []
for x in lst_num:
    lst_round.append(round(x))
print(lst_round)
