'''
Известны год и номер месяца рождения человека, а так-
же год и номер месяца сегодняшнего дня (январь – 1 и т. д.). Опре-
делить возраст человека (число полных лет). В случае совпадения
указанных номеров месяцев считать, что прошел полный год.
'''
import datetime

year = int(input("Введите год рождения человека: "))
month = int(input("Введите месяц рождения человека: "))

now = datetime.datetime.today()

delta_year = now.year - year

delta_month = now.month - month
if delta_month < 0:
    delta_year = delta_year - 1


print ("Ответ:")
print ("Возраст человека - "+str(delta_year)+str(" полных лет.")) 
