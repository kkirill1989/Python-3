# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
some_list = input().split()
maxx = 0
minn = 1
for el in some_list:
    if '.' in el:
        number = el.split('.')[1]
        if int(number) != 0:
            if float('0.' + number) < minn:
                minn = float('0'+ number)
            elif float('0.' + number) > maxx:
                maxx = float('0.' + number)
print(maxx - minn)                    