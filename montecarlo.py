import random

#generates random coordinates, estimates pi
def montecarlo(numsims):
    points_inside = 0
    total_points = 0
    i = 0
    for i in range(numsims):
        x, y = random.random(), random.random()
        if (x*x + y*y) <= 0.25:
            points_inside += 1
        total_points += 1
        i += 1
    pi = 16 * (points_inside / total_points)
    return pi
