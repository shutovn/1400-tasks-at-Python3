'''
Замечание
В задачах 3.12–3.15 условный оператор не использовать.

В подъезде No 1 пятиэтажного жилого дома 20 квартир.
Определить:
1) на каком этаже этого подъезда находится квартира с заданным номером;
2) какой по счету является эта квартира, если квартира с минимальным номером является первой на этаже.
'''
import math
a = int(input("Введите номер квартиры от 1 до 20 : "))

x1 = math.ceil( a / 4 )

n = [4, 1, 2, 3]
b = int(a / 4)
x2 = a - b * 4

print ("1) Квартира с заданным номером находится на " +str(x1) +str(" этаже."))
print ("2) Квартира с заданным номером, по счету " +str(n[x2])  +str(" на этаже."))
