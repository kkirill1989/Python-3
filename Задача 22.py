# Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
summa = 0
some_list = input(). split()
for ind in range(1, len(some_list), 2):
    summa += int(some_list[ind])
print(summa)    