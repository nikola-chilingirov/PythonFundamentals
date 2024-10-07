num = input().split()
int_lst = [int(x) for x in num]
max_num = max(int_lst)
min_num = min(int_lst)
sum_num = sum(int_lst)
print(f"The minimum number is {min_num}")
print(f"The maximum number is {max_num}")
print(f"The sum number is: {sum_num}")