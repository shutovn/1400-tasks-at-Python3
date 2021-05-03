'''
Дано трехзначное число. Определить:
а) входит ли в него цифра 6;
б) входит ли в него цифра n.
'''
import math

print("Дано трехзначное число. Определить: ")
print("а) входит ли в него цифра 6 ")
print("б) входит ли в него цифра n. ")

numeric = int(input("Введите трехзначное число: "))
n = int(input("Введите цифру n: "))

if numeric in range(100,1000):

    a = math.floor(numeric / 100)
    b = math.floor((numeric % 100) / 10)
    c = numeric % 10


    answer_a = "Цифра 6 входит в число "+str(numeric)+str(".") if a == 6 or b == 6 or c == 6  else "Цифра 6 НЕ входит в число "+str(numeric)+str(".")
    answer_b = "Цифра "+str(n)+str(" входит в число ")+str(numeric)+str(".") if a == n or b == n or c == n else "Цифра "+str(n)+str(" НЕ входит в число ")+str(numeric)+str(".")

else:
    answer_a = "Введенное число не является трехзначным!"
    answer_b = "Введенное число не является трехзначным!"


print(" ")
print("Ответ:")
print("a) "+str(answer_a))
print("б) "+str(answer_b))
