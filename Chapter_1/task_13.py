# Напишите программу, в которую вводится целое число,
# после чего на экран выводится следующее и предыдущее целое число.

x = int(input("Введите число: "))

print ('Следующее за числом', x,'число –',str(x+1)+'.')
print ('Для числа',x,'предыдущее число –',str(x-1)+'.')
