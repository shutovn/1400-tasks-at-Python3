# Известны количество жителей в государстве и площадь его территории. Определить плотность населения в этом государстве.

print ("Необходимо определить плотность населения в государстве.")

Pop = int(input("Введите кол-во жителей государства, например в Росии - 146 748 590: "))
S = float(input("Введите площать территории государства, например площадь России - 17 098 246 км²: "))

p = Pop / S

print ("Плотность населения равна " + str(p) + " чел/км²")
