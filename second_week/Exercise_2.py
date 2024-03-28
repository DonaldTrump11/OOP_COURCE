import math
import random
import pygame

SCREEN_DIM = (800, 600)

class Vec2d:

    def __add__(x, y):
        """возвращает сумму двух векторов"""
        return x[0] + y[0], x[1] + y[1]

    def __sub__(x, y):
        """возвращает разность двух векторов"""
        return x[0] - y[0], x[1] - y[1]

    def __mul__(v, k):
        """возвращает произведение вектора на число"""
        return v[0] * k, v[1] * k

    def __len__(x):
        """возвращает длину вектора"""
        return math.sqrt(x[0] * x[0] + x[1] * x[1])

    def int_pair(x):
        """возвращает кортеж из двух целых чисел (текущие координаты вектора)"""
        return (x[0], x[1])



class Polyline:

    def set_points(points, speeds):
        """пересчёт координат точек"""
        for p in range(len(points)):
        points[p] = add(points[p], speeds[p])
        if points[p][0] > SCREEN_DIM[0] or points[p][0] < 0:
            speeds[p] = (- speeds[p][0], speeds[p][1])
        if points[p][1] > SCREEN_DIM[1] or points[p][1] < 0:
            speeds[p] = (speeds[p][0], -speeds[p][1])

    def draw_points():
        """отрисовка ломаной линии"""
        pass

    #TODO: Арифметические действия с векторами должны быть реализованы с помощью операторов, а не через вызовы соответствующих методов.


class Knot(Polyline):
    
    def get_knot():
        pass

