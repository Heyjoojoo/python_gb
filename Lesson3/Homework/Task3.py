# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов, отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import os
clear = lambda: os.system('cls')
clear()
import random
my_list = []

for i in range(10):
    index = random.randint(0,3)
    my_list.append(round(random.uniform(0,10), index))
print(my_list)   

n_max = 0
n_min = 1000

for i in range(len(my_list)):
    my_list[i]*=1000
    my_list[i]%=1000
    if n_max < my_list[i]:
        n_max=my_list[i]
        
    if n_min > my_list[i] and my_list[i]>0:
        n_min=my_list[i]


print(my_list)
print(n_min)
print(n_max)
print(float(n_max-n_min)/1000)
