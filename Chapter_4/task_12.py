'''
Даны радиус круга и сторона квадрата. У какой фигуры
площадь больше?
'''

import math

print("Даны радиус круга и сторона квадрата.")
print("У какой фигуры площадь больше?")

r = float(input("Введите радиус круга: "))
a = float(input("Введите сторону квадрата: "))

pi = math.pi

Sc = pi * r ** 2
Ss = a * a

if Sc > Ss:
    x = "Круг - circle"
else:
    x = "Квадрат - square"


print(" ")
print("Ответ: ")
print("Большей по площади является фигура - "+str(x))
