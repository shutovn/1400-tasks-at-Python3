'''
Дано натуральное число n (n > 99). Найти:
а) число десятков в нем;
б) число сотен в нем.
'''

n = str(input("Введите число > 99: "))

numbers = []
for i in n[::-1]:
    numbers.append(i)

print("а) число десятков: "+str(numbers[1]))
print("б) число сотен: "+str(numbers[2]))
