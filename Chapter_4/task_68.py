'''
Год является високосным, если его номер кратен 4, однако из кратных 100 високосными являются лишь кратные 400,
например 1700, 1800 и 1900 – невисокосные года, 2000 – високосный.
Дано натуральное число n. Определить, является ли високосным год с таким номером.
'''

print("Год является високосным, если его номер кратен 4, однако из кратных 100 високосными являются лишь кратные 400,")
print("например 1700, 1800 и 1900 – невисокосные года, 2000 – високосный.")
print("Дано натуральное число n. Определить, является ли високосным год с таким номером.")

n = int(input("Введите год: "))
answer = "Високосный!" if ((n % 4 == 0 and n % 100 != 0) or (n % 400 == 0)) else "Невисокосный!"

print("")
print("Ответ:")
print(answer)
