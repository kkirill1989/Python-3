# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
n = int(input())
out_list = []
while n > 0:
    out_list.append(str(n % 2))
    n //= 2
out_list.reverse()    
print(*out_list, sep='')