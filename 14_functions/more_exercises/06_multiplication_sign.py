def multiplication_sign(n_1, n_2, n_3):
    if n_1 == 0 or n_2 == 0 or n_3 == 0:
        return 'zero'
    if n_1 > 0 and n_2 > 0 and n_3 > 0:
        return 'positive'
    if (n_1 < 0 and n_2 < 0 and n_3 < 0) or (n_1 < 0 and n_2 > 0 and n_3 > 0) or (n_1 > 0 and n_2 < 0 and n_3 > 0) or (n_1 > 0 and n_2 > 0 and n_3 < 0):
        return 'negative'
    else:
        return 'positive'


first_num = int(input())
second_num = int(input())
third_num = int(input())
print(multiplication_sign(first_num, second_num, third_num))
