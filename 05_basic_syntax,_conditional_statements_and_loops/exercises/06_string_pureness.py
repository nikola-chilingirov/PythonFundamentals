n = int(input())
for i in range(n):
    data = input()
    for x in data:
        if x == "," or x == '.' or x == '_':
            print(f"{data} is not pure!")
            break
    else:
        print(f"{data} is pure.")