'''
Даны вещественные числа a, b, c (a ≠ 0).
Решить уравнение ax 2 + bx + c = 0.
В числе возможных вариантов учесть вариант равенства корней уравнения.
'''

print("Даны вещественные числа a, b, c (a ≠ 0).")
print("Решить уравнение ax 2 + bx + c = 0.")
print("В числе возможных вариантов учесть вариант равенства корней уравнения.")

a, b, c = map(float, input("Введите значения вещественных чисел a, b, c: ").split(","))

discr = b**2 - 4 * a * c

print("Дискриминант D = %.2f" % discr)

if discr > 0:
    import math
    x1 = (-b + math.sqrt(discr)) / (2 * a)
    x2 = (-b - math.sqrt(discr)) / (2 * a)
    answer = ("x1 = %.2f \nx2 = %.2f" % (x1, x2))
elif discr == 0:
    x = -b / (2 * a)
    answer = ("x = %.2f" % x)
else:
    answer = "Корней нет"




print("")
print("Ответ: ")
print(answer)
