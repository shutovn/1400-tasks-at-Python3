'''
Дано трехзначное число.
Найти число, полученное при перестановке второй и третьей цифр заданного числа.
'''

n = str(input("Введите трехзначное число: "))

numbers = []
for i in n[::]:
    numbers.append(i)

print (numbers[0]+numbers[2]+numbers[1])
