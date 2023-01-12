from random import choice

def power(k):
    equation = 'x1'
    coef_list = list(range(1, 101))
   
    for i in range (k, 1, -1):
        coef = str(choice(coef_list))
        equation = equation\
        .__add__((f'**{i}') + choice('+-') + coef + 'x') 
    
    equation = equation\
        .replace('x1', f'{str(choice(coef_list))}x')\
        .replace('1', '')\
        .__add__('+'+ str(choice(coef_list)))
      
    return equation

k = int(input("Введите степень: "))
l = int(input("Введите степень2: "))
with open ('polynomial1.txt', 'a', encoding='utf-8') as poly1:
    poly1.writelines(f'{power(k)}=0')
with open ('polynomial2.txt', 'a', encoding='utf-8') as poly2:
    poly2.writelines(f'{power(l)}=0')
with open ('polynomial_sum.txt', 'a', encoding='utf-8') as polysum:
    polysum.write(f'{power(k)}+{power(l)}=0')
