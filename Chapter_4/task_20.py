'''
*
Даны два прямоугольника, стороны которых параллельны или перпендикулярны осям координат.
Известны координаты  левого нижнего и правого верхнего углов каждого из них.
Найти координаты левого нижнего и правого верхнего углов минимального прямоугольника,
содержащего указанные прямоугольники.
'''

print("Даны два прямоугольника, стороны которых параллельны или перпендикулярны осям координат.")
print("Известны координаты  левого нижнего и правого верхнего углов каждого из них.")
print("Найти координаты левого нижнего и правого верхнего углов минимального прямоугольника, содержащего указанные прямоугольники.")
print(" ")
print ("Введите координаты левого нижнего и правого углов :")
x1_ld, y1_ld, x1_ru, y1_ru = map(int, input("- первого прямоугольника x1_ld,y1_ld,x1_ru,y1_ru : ").split(","))
x2_ld, y2_ld, x2_ru, y2_ru = map(int, input("- второго прямоугольника x2_ld,y2_ld,x2_ru,y2_ru : ").split(","))

answer1=""
answer2=""
if ( x1_ld > x1_ru ) or ( y1_ld > y1_ru):
    answer1=("Координаты первого прямоугольника некорректны!!!")
elif ( x2_ld > x2_ru ) or ( y2_ld > y2_ru):
    answer2=("Координаты второго прямоугольника некорректны!!!")
else:
    x_ld = x1_ld if ( x1_ld <= x2_ld ) else x2_ld
    y_ld = y1_ld if ( y1_ld <= y2_ld ) else y2_ld
    x_ru = x1_ru if ( x1_ru >= x2_ru ) else x2_ru
    y_ru = y1_ru if ( y1_ru >= y2_ru ) else y2_ru

if not answer1 and not answer2:
    print(" ")
    print("Ответ:")
    print("Оба прямоугольника содержатся в прямоугольнике с координатами:")
    print("Левый нижний угол: x="+str(x_ld)+str(", y=")+str(y_ld))
    print("Правый верхний угол: x="+str(x_ru)+str(", y=")+str(y_ru))
else:
    if not answer1:
        print(" ")
        print("Ответ:")
        print(answer2)
    else:
        print(" ")
        print("Ответ:")
        print(answer1)
