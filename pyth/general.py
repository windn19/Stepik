from random import random, randint
import time


def time_complite(func):
    def proc(n):
        start_time = time.time()
        result = func(n)
        finish_time = time.time()
        delta = round(finish_time - start_time, 4)
        print(delta)
        return result
    return proc


@time_complite
def point_line(number):
    points = [random() * randint(1, 10) for _ in range(number)]
    points.sort()
    print(points)
    result = {}
    while len(points) != 0:
        i = min(points)
        while len(points) != 0 and i + 1 > points[0]:
            points.pop(0)
            result[(i, i + 1)] = result.get((i, i + 1), 0) + 1
    return result


if __name__ == '__main__':
    print(point_line(n=10))
