#Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
k = int(input())
some_list = [0] * (k * 2 + 1)
some_list[k + 1] = 1
some_list[k - 1] = 1
for ind in range(k + 2, k * 2 + 1):
    some_list[ind] = some_list[ind - 1] + some_list[ind - 2]
for ind in range(k - 2, -1, -1):
     some_list[ind] = some_list[ind + 2] + some_list[ind + 1]
print(some_list) 