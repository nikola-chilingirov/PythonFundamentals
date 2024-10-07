def add_and_subtract():
    def sum_num(n1, n2):
        return n1 + n2

    def subtract(res, n3):
        return res - n3

    num_1 = int(input())
    num_2 = int(input())
    num_3 = int(input())

    print(subtract(sum_num(num_1, num_2), num_3))


add_and_subtract()