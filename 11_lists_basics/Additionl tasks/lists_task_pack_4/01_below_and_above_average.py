n = input().split(',')
data = []
bucket = []
counter = 0
below = []
above = []
for i in n:
    counter += 1
    data.append(int(i))
total = sum(data)
avr = total / counter
for x in data:
    if x < avr:
        below.append(str(x))
    elif x > avr:
        above.append(str(x))
print(f"avg: {avr:.2f}")
print(f"below: {','.join(below)}")
print(f"above: {','.join(above)}")
