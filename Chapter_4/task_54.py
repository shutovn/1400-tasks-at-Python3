'''
Дано четырехзначное число. Определить:
а) входит ли в него цифра 4;
б) входит ли в него цифра b.
'''
import math

print("Дано четырехзначное число. Определить: ")
print("а) входит ли в него цифра 4; ")
print("б) входит ли в него цифра b. ")

n = int(input("Введите четырехзначное число: "))
b = int(input("Введите цифру b: "))

if n in range(1000,10000):

    c = math.floor(n / 1000)
    d = math.floor((n % 1000) / 100)
    e = math.floor((n % 100) / 10)
    f = n % 10

    answer_a = "Цифра 4 входит в число "+str(n)+str(".") if 4 in [c,d,e,f] else "Цифра 4 НЕ входит в число "+str(n)+str(".")
    answer_b = "Цифра "+str(b)+str(" входит в число ")+str(n)+str(".") if b in [c,d,e,f] else "Цифра "+str(b)+str(" НЕ входит в число ")+str(n)+str(".")

else:
    answer_a = "Число n не является четырехзначным!"
    answer_b = "Число n не является четырехзначным!"

print(" ")
print("Ответ:")
print("a) "+str(answer_a))
print("б) "+str(answer_b))
