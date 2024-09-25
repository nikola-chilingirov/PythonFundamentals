n = int(input())
counter_1 = 0
counter_2 = 0
for i in range(n):
    data = input()
    if data == "(":
        counter_1 += 1
    if data == ")" and counter_1 == 1:
        counter_2 += 1
        counter_1 = 0
    if data == ")" and counter_1 != 1:
        break
if counter_2 != 0:
    print("BALANCED")
else:
    print("UNBALANCED")
