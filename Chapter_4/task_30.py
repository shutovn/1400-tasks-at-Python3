'''
Дано трехзначное число. Выяснить, является ли оно палиндромом («перевертышем»),
т. е. таким числом, десятичная запись­ которого читается одинаково слева направо и справа налево.
'''
import math

print("Дано трехзначное число. Выяснить, является ли оно палиндромом («перевертышем»),")
print("т. е. таким числом, десятичная запись­ которого читается одинаково слева направо и справа налево.")

n = int(input("Введите трехзначное число: "))

a = math.floor(n/100)
c = n % 10

if a == c:
    answer = "данное число является палиндромом!"
else:
    answer = "данное число НЕ является палиндромом!"

print(" ")
print("Ответ:")
print("Результат - "+str(answer))
