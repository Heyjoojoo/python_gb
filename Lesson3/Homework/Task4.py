# Напишите программу, которая будет преобразовывать 
# десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10


import os
clear = lambda: os.system('cls')
clear()
num = int(input("Введите число: "))
num_list = []
while num > 0:
    if num%2 == 0:
        num_list.append(0)
    else:
        num_list.append(1)
        
    num=num//2
num_list.reverse()

print(int(''.join(map(str, num_list))))