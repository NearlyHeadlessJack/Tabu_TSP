from dataloader import *
from numpy import sqrt
import numpy as np

d = Dataloder()


def distance_calculation(route_now):
    r = route_now
    distance = 0.0
    for i in range(1, 5):
        print(r[1][i])
        distance += sqrt(((r[1][i][0] - r[1][i - 1][0]) ** 2) + ((r[1][i][1] - r[1][i - 1][1]) ** 2))
    distance += sqrt(((r[1][4][0] - r[1][0][0]) ** 2) + ((r[1][4][1] - r[1][0][1]) ** 2))

    return distance


print(distance_calculation(d.cities))
