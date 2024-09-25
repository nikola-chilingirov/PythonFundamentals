num = int(input())
flag = 0
if num > 1:
    for i in range(2, int(num**(1/2)) + 1):
        if num % i == 0:
            flag = 1
            break
    if flag == 0:
        print("True")
    else:
        print("False")
else:
    print("False")
