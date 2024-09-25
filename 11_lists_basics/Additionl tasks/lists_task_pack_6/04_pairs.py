target = int(input())
line = [int(el) for el in input().split(" ")]
t = False
for i in range(len(line)):
    for x in range(i + 1, len(line)):
        if line[i] + line[x] == target:
            print(",".join(str(el) for el in [line[i], line[x]]))
            t = True
if t is False:
    print("no pairs")