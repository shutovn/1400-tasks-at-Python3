'''
Определить, является ли заданное шестизначное число счастливым.
(Счастливым называют такое шестизначное число,
в котором сумма его первых трех цифр равна сумме его последних трех цифр.)
'''
import math

print("Определить, является ли заданное шестизначное число счастливым.")
print("(Счастливым называют такое шестизначное число, в котором сумма его первых трех цифр равна сумме его последних трех цифр.)")
print("")

n = int(input("Введите шестизначное число: "))

if n in range(100000,1000000):

    a = math.floor(n / 100000)
    b = math.floor((n % 100000) / 10000)
    c = math.floor((n % 10000) / 1000)
    d = math.floor((n % 1000) / 100)
    e = math.floor((n % 100) / 10)
    f = n % 10

    answer = "Число является счастливым!" if (a + b + c) == (d + e + f) else "Число не является счастливым!"

else:
    answer = "Число n не является шестизначным!"

print("")
print("Ответ:")
print(answer)
