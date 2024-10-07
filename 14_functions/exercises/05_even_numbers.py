def even_num(num):
    lst_even = [y for y in num if y % 2 == 0]
    return lst_even


str_input = input().split()
str_lst = [int(x) for x in str_input]
print(even_num(str_lst))


