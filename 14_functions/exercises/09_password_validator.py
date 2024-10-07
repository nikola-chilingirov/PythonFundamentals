def password_func(password):
    flag = True
    if len(password) < 6 or len(password) > 10:
        flag = False
        print('Password must be between 6 and 10 characters')
    for i in password:
        if ord(i) < 48 or 57 < ord(i) < 65 or 90 < ord(i) < 97 or ord(i) > 122:
            flag = False
            print('Password must consist only of letters and digits')
            break
    counter_digit = 0
    for i in password:
        if i.isdigit():
            counter_digit += 1
    if counter_digit < 2:
        flag = False
        print('Password must have at least 2 digits')

    if flag:
        print('Password is valid')


password_str = input()


password_func(password_str)
