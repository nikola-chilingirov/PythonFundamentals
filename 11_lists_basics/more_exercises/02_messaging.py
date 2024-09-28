numbers = input().split()
string = input()
result = []
for i in range(len(numbers)):
    digit = [int(x) for x in numbers[i]]
    sum_digit = sum(digit)
    if sum_digit >= len(string):
        idx = sum_digit % len(string)
        result.append(string[idx])
        string = string.replace((string[idx]), '', 1)
    else:
        idx = sum_digit
        result.append(string[idx])
        string = string.replace((string[idx]), '', 1)
print(*result, sep='')