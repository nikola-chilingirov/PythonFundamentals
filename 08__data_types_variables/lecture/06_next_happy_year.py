import sys
num = int(input())
digit_str = ''
for i in range(num, sys.maxsize):
    digit = str(i)
    if len(digit) == 1:
        print(num + 1)
        break
    for x in range(len(digit)):
        current_digit = digit.replace(digit[x], '', 1)
        if digit[x] in current_digit:
            break
        else:
            digit_str += digit[x]
    if len(digit_str) == len(digit) and digit_str != str(num):
        print(digit_str)
        break
    else:
        digit_str = ''