from math import sqrt
from math import floor


def closest_point(x, y):
    c = sqrt((x ** 2) + (y ** 2))
    return c


def check_closest_point(point_1, point_2):
    x_1, y_1 = point_1
    x_2, y_2 = point_2
    distance_1 = closest_point(x_1, y_1)
    distance_2 = closest_point(x_2, y_2)
    if distance_1 <= distance_2:
        point_11 = floor(x_1), floor(y_1)
        return point_11
    else:
        point_22 = floor(x_2), floor(y_2)
        return point_22


first_point = (float(input())), (float(input()))
second_point = (float(input())), (float(input()))

print(check_closest_point(first_point, second_point))
