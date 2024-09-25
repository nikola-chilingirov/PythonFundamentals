n = int(input())
lst = []
lst_even = []
lst_odd = []
lst_neg = []
lst_pos = []
for i in range(n):
    data = int(input())
    if data % 2 == 0:
        lst_even.append(data)
    if data % 2 != 0:
        lst_odd.append(data)
    if data < 0:
        lst_neg.append(data)
    if data >= 0:
        lst_pos.append(data)
command = input()
if command == "even":
    print(lst_even)
elif command == "odd":
    print(lst_odd)
elif command == "negative":
    print(lst_neg)
elif command == "positive":
    print(lst_pos)
