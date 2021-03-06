'''
Дано трехзначное число. Определить:
а) входят ли в него цифры 4 или 7;
б) входят ли в него цифры 3, 6 или 9.
'''
import math

print("Дано трехзначное число. Определить: ")
print("а) входят ли в него цифры 4 или 7; ")
print("б) входят ли в него цифры 3, 6 или 9. ")

n = int(input("Введите трехзначное число: "))

if n in range(100,1000):

    a = math.floor(n / 100)
    b = math.floor((n % 100) / 10)
    c = n % 10

    answer_a = "Цифра 4 или 7 входит в число "+str(n)+str(".") if 4 in [a,b,c] or 7 in [a,b,c] else "Цифра 4 или 7 НЕ входит в число "+str(n)+str(".")
    answer_b = "Цифра 3, 6 или 9 входит в число "+str(n)+str(".") if 3 in [a,b,c] or 6 in [a,b,c] or 9 in [a,b,c] else "Цифра 3, 6 или 9 НЕ входит в число "+str(n)+str(".")

else:
    answer_a = "Число n не является трехзначным!"
    answer_b = "Число n не является трехзначным!"


print(" ")
print("Ответ:")
print("a) "+str(answer_a))
print("б) "+str(answer_b))
