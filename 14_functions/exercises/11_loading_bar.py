def loading(num):
    a = int(num / 10)
    lst = []
    for i in range(0, a):
        lst.append('%')
    for x in range(a, 10):
        lst.append('.')
    if num < 100:
        return f"{num}% [{''.join(lst)}]\nStill loading..."
    else:
        return f"100% Complete!\n[{''.join(lst)}]"


number = int(input())
print(loading(number))