def calc_factorial(num_1, num_2):
    counter_1 = 1
    counter_2 = 1
    for i in range(1, num_1 + 1):
        counter_1 *= i
    for x in range(1, num_2 + 1):
        counter_2 *= x
    result = counter_1 / counter_2
    return result


first_number = int(input())
second_number = int(input())
print(f'{calc_factorial(first_number, second_number):.2f}')
