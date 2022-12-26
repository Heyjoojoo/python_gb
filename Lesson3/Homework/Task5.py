# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи

import os
clear = lambda: os.system('cls')
clear()

k = int(input("Введите число: "))

list_nums_1 = [0]
num = -1
for i in range (k):
    num = list_nums_1[i-1] - num 
    list_nums_1.append(num)
list_nums_1.reverse()


list_nums_2 = [1]
num = 0
for i in range(k-1):
    num = list_nums_2[i-1] + num
    list_nums_2.append(num)

list_nums_1.extend(list_nums_2)

print(list_nums_1)
