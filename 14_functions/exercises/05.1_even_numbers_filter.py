str_input = input().split()
str_lst = [int(x) for x in str_input]


def even_num(num):
    if num % 2 == 0:
        return True
    else:
        return False


even = list(filter(even_num, str_lst))


print(even)

