num = input().split(',')
n = int(input())
counter = 0
new_list = []
result = ''
for x in num:
    counter += 1
if counter == n:
    new_list = num
    print(*new_list, sep=',')
elif counter > n:
    new_list = num[n:] + num[:n]
    print(*new_list, sep=',')
elif counter < n:
    if 2 * counter < n:
        q = n % counter
        new_list = num[q:] + num[:q]
        print(*new_list, sep=',')
    else:
        m = n - counter
        new_list = num[m:] + num[:m]
        print(*new_list, sep=',')

# This line prompts the user to input a string of values separated by commas (,). It then splits this string into a list of values using the split(",") method. The resulting list is stored in the variable lst.
#lst = input().split(",")
# This line prompts the user to input an integer rota, which represents the number of positions to rotate the list to the right.
#rota = int(input())

#for _ in range(rota):
    # Inside the loop, lst[1:] slices the list lst from the second element to the end, effectively removing the first element. [lst[0]] creates a new list containing only the first element of lst. lst[1:] + [lst[0]] combines these two lists by adding the first element to the end of the sliced list, effectively rotating the list to the right by one position. This rotated list is assigned back to the variable lst, replacing the original list.
    #lst = lst[1:] + [lst[0]]

# After completing the rotations, this line joins the elements of the lst list using commas and prints the result as a comma-separated string.
#print(",".join(lst))