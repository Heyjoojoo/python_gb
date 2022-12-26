# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]


import os
clear = lambda: os.system('cls')
clear()

old_list = [2, 3, 4, 5, 6]
new_list = []
product = 0
count = 0
for i in range(len(old_list)):
    if count <= len(old_list)/2:
        product = old_list[0+count]*(len(old_list)-count+1)
        new_list.append(product)
        count+=1
    
print(new_list)