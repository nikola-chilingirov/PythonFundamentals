n = int(input())
first_list = []
second_list = []
for x in range(n):
    num = int(input())
    first_list.append(num)
for y in range(n):
    num = int(input())
    second_list.append(num)
if first_list == second_list:
    print('equal')
else:
    print('not equal')