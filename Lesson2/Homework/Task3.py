# Реализуйте алгоритм перемешивания списка. 
# НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, 
# максимум использование библиотеки Random для и получения случайного int

list_a = []
for i in range(10):
    list_a.append(i)
print(*list_a)

from random import randint

for i in range(10):
    index_shuffle = randint(0,9)
    temp = list_a[i]
    list_a[i] = list_a[index_shuffle]
    list_a[index_shuffle] = temp
        
print(*list_a)

