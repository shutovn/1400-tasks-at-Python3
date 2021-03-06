'''
Вася пытается высунуть голову в форточку размерами a и b см.
Приняв условно, что его голова – круглая диаметром d см, определить, сможет ли Вася сделать это.
Для прохождения головы в форточку необходим зазор в 1 см с каждой стороны.
'''

print("Вася пытается высунуть голову в форточку размерами a и b см.")
print("Приняв условно, что его голова – круглая диаметром d см, определить, сможет ли Вася сделать это.")
print("Для прохождения головы в форточку необходим зазор в 1 см с каждой стороны.")

a, b = map(int, input("Введите размеры форточки a, b см: ").split(","))
d = int(input("Введите диаметр головы Васи в см: "))

answer = "Вася сможет просунуть голову в форточку!" if ( d + 1 <= a ) and ( d + 1 <= b )   else "Вася не сможет просунуть голову в форточку!"

print(" ")
print("Ответ:")
print(answer)
