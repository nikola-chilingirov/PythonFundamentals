a = int(input())
b = int(input())
temp_a = a
temp_b = b
a = b
b = temp_a
print(f"Before:\na = {temp_a}\nb = {temp_b}\nAfter:\na = {a}\nb = {b}")