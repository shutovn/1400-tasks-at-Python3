'''
Задачи повышенной сложности

С начала суток часовая стрелка повернулась на y градусов
(0 ≤ y < 360, y – вещественное число). Определить число полных
часов и число полных минут, прошедших с начала суток.
'''

y = float(input("Введите значение смещения часовой стрелки в градусах°: "))
# Градусы на циферблате
# 1 час = 360 / 12 = 30°
# 1 минута = 30° / 60 = 0.5°

h = int(y / 30)
m = int((y % 30) / 0.5)

print("Определить число полных часов и число полных минут, прошедших с начала суток.")
print("Число полных часов =", h)
print("Число полных минут =", m)
