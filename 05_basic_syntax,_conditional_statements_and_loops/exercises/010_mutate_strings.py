first_string = input()
second_string = input()
current_string = first_string
new_string = ''
for chr_idx in range(len(first_string)):
    left_part = second_string[:chr_idx + 1]
    right_part = first_string[chr_idx + 1:]
    new_string = left_part + right_part
    if new_string != current_string:
        print(new_string)
        current_string = new_string