# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.

import math

x1 = float(input('Введите координаты X1. \n x1 = '))
x2 = float(input('Введите координаты X2. \n x1 = '))
y1 = float(input('Введите координаты Y1. \n y1 = '))
y2 = float(input('Введите координаты Y2. \n y2 = '))
print(math.sqrt((x1-x2)**2 + (y1-y2)**2))
