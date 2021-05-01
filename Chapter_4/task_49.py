'''
Дано двузначное число. Определить:
а) входит ли в него цифра 3;
б) входит ли в него цифра а.
'''
import math

print("Дано двузначное число. Определить: ")
print("а) входит ли в него цифра 3; ")
print("б) входит ли в него цифра а. ")

n = int(input("Введите двузначное число: "))
a = int(input("Введите число a: "))

if n in range(10,100):

    x = math.floor(n/10)
    y = n % 10

    answer_a = "Цифра 3 входит в число n = "+str(n)+str(".") if x == 3 or y == 3 else "Цифра 3 не входит в число n = "+str(n)+str(".")
    answer_b = "Цифра "+str(a)+str(" входит в число n = ")+str(n)+str(".") if x == a or y == a else "Цифра "+str(a)+str(" не входит в число n = ")+str(n)+str(".")

else:
    answer_a = "Число n не является двузначным!"
    answer_b = "Число n не является двузначным!"

print(" ")
print("Ответ:")
print("a) "+str(answer_a))
print("б) "+str(answer_b))
