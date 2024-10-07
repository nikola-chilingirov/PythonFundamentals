def solve(palidrome):
    reversed_i = i[::-1]
    if palidrome == reversed_i:
        return True
    else:
        return False


num = list(input().split(', '))
for i in num:
    print(solve(i))
