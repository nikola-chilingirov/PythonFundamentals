digit_in = input()


def solve(digit):
    counter_odd = 0
    counter_even = 0
    for i in digit:
        i_int = int(i)
        if i_int % 2 == 0:
            counter_even += i_int
            continue
        else:
            counter_odd += i_int
            continue
    return f'Odd sum = {counter_odd}, Even sum = {counter_even}'


print(solve(digit_in))



