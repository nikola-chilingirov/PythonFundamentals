def perfect_num(number):
    counter = 0
    for i in range(1, number):
        if number % i == 0:
            counter += i
    if counter == number:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


num = int(input())


print(perfect_num(num))
