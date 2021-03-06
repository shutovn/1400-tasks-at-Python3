'''
Дано двузначное число. Определить, равен ли квадрат
этого числа учетверенной сумме кубов его цифр. Например, для
числа 48 ответ положительный, для числа 52 – отрицательный.
'''
import math
print("Дано двузначное число. Определить, равен ли квадрат этого числа учетверенной сумме кубов его цифр.")
print("Например, для числа 48 ответ положительный, для числа 52 – отрицательный.")

n = int(input("Введите двузначное число: "))

x = math.pow(n, 2)

a = math.floor(n/10)
b = n % 10

y = (math.pow(a, 3) + math.pow(b, 3)) * 4

answer = "Положительный!" if x == y else "Отрицательный!"

print(" ")
print("Ответ:")
print("Результат вычислений - "+str(answer))
