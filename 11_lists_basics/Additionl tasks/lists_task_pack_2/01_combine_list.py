first_list = input().split(",")
second_list = input().split(",")

output = []
for i in range(len(first_list)):
    output.append(first_list[i])
    output.append(second_list[i])
print(",".join(output))




