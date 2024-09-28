factor = int(input())
count = int(input())
lst = [i for i in range(factor, count*factor + 1, factor)]
print(lst)