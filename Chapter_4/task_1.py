'''
Даны два различных вещественных числа. Определить:
а) какое из них больше;
б) какое из них меньше.
'''

a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))

if a > b:
    x = a
    y = b
else:
    y = a
    x = b

print("а) большее число =",x)
print("б) меньшее число =",y)
