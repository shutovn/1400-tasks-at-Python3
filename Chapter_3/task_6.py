# В купейном вагоне имеется 9 купе с четырьмя местами для пассажиров в каждом.
# Определить номер купе, в котором находится место с заданным номером
# (нумерация мест сквозная, начинается с 1).
import math

x = int(input("Введите номер искомого места: "))

if (x <= 36):
    n = math.ceil(x / 4)
    print ("Место " +str(x) +str(", находиться в  ") +str(n)+str(" купе."))
else:
    print ("Введенного вами номера места " +str(x) +str(" в данном вагоне не существует!"))
