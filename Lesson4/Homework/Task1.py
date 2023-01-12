# A. Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и 
# записать в файл многочлен степени k.
# Пример:
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import choice

def power(k):
    equation = 'x1'
    coef_list = list(range(1, 101))
   
    for i in range (k, 1, -1):
        coef = str(choice(coef_list))
        equation = equation\
        .__add__((f'**{i}') + choice('+-') + coef + 'x') #вместо range -100, 100 решила сделать рандомный знак
    
    equation = equation\
        .replace('x1', f'{str(choice(coef_list))}x')\
        .replace('1', '')\
        .__add__('+'+ str(choice(coef_list)) + '=0')
      
    return equation

k = int(input("Введите степень: "))
with open ('polynomial.txt', 'a', encoding='utf-8') as poly:
    poly.writelines(power(k))
print(power(k))
