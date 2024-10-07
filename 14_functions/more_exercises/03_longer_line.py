from math import sqrt
from math import floor


def closest_point(x, y):
    c = sqrt((x ** 2) + (y ** 2))
    return c


def new_coord(x_1, y_1, x_2, y_2):
    x = 0
    y = 0
    if (x_1 <= 0 <= x_2) or (x_1 >= 0 >= x_2):
        x = abs(x_1) + abs(x_2)
    if (y_1 <= 0 <= y_2) or (y_1 >= 0 >= y_2):
        y = abs(y_1) + abs(y_2)
    if (x_1 < 0 and x_2 < 0) or (x_1 > 0 and x_2 > 0):
        x = abs(x_1) - abs(x_2)
    if (y_1 < 0 and y_2 < 0) or (y_1 > 0 and y_2 > 0):
        y = abs(y_1) - abs(y_2)
    return x, y


def check_closest_point(point_1, point_2, point_3, point_4):
    x_1, y_1 = point_1
    x_2, y_2 = point_2
    x_3, y_3 = point_3
    x_4, y_4 = point_4
    x_12, y_12 = new_coord(x_1, y_1, x_2, y_2)
    x_34, y_34 = new_coord(x_3, y_3, x_4, y_4)
    distance_1 = closest_point(x_12, y_12)
    distance_2 = closest_point(x_34, y_34)
    if distance_1 >= distance_2:
        closest_point_final_1 = closest_point(x_1, y_1)
        closest_point_final_2 = closest_point(x_2, y_2)
        if closest_point_final_1 <= closest_point_final_2:
            point_11 = f'({floor(x_1)}, {floor(y_1)})({floor(x_2)}, {floor(y_2)})'
            return point_11
        else:
            point_12 = f'({floor(x_2)}, {floor(y_2)})({floor(x_1)}, {floor(y_1)})'
            return point_12
    else:
        closest_point_final_3 = closest_point(x_3, y_3)
        closest_point_final_4 = closest_point(x_4, y_4)
        if closest_point_final_3 <= closest_point_final_4:
            point_21 = f'({floor(x_3)}, {floor(y_3)})({floor(x_4)}, {floor(y_4)})'
            return point_21
        else:
            point_22 = f'({floor(x_4)}, {floor(y_4)})({floor(x_3)}, {floor(y_3)})'
            return point_22


first_point = (float(input())), (float(input()))
second_point = (float(input())), (float(input()))
third_point = (float(input())), (float(input()))
forth_point = (float(input())), (float(input()))

print(check_closest_point(first_point, second_point, third_point, forth_point))
