num = float(input())
if num == 0:
    print('zero')
elif num > 0:
    if 0 < num < 1:
        print('small positive')
    elif num > 1000000:
        print('large positive')
    else:
        print('positive')
else:
    if -1 < num < 0:
        print('small negative')
    elif abs(num) > 1000000:
        print('large negative')
    else:
        print('negative')