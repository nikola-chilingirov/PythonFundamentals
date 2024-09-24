string = input()
new_str = string.lower()
counter = 0
current_str = ''
if 'water' in new_str:
    current_str = new_str.replace('water', '')
    counter += (len(new_str) - len(current_str))/5
    new_str = current_str
if 'sand' in new_str:
    current_str = new_str.replace('sand', '')
    counter += (len(new_str) - len(current_str))/4
if 'fish' in new_str:
    current_str = new_str.replace('fish', '')
    counter += (len(new_str) - len(current_str))/4
if 'sun' in new_str:
    current_str = new_str.replace('sun', '')
    counter += (len(new_str) - len(current_str))/3
print(int(counter))






