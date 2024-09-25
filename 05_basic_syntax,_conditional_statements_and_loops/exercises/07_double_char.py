string = input()
word = ''
while string != 'End':
    if string != 'SoftUni':
        for i in string:
            word += (2 * i)
        print(word)
        word = ''
    string = input()