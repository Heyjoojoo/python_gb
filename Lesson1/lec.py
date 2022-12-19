print('hello world')

a = 123
b = 1.23
s = 'hello \nworld'

print(s)
print(a, ' - ', b, ' - ', s )
print('{} - {} - {}'.format(a, b, s) )
print(f'{a} - {b} - {s}')

f = True
print(f)

list = ['1','2','3', 'hello', 1,2,3] #массив с разным типом данных
print(list)

#Ввод и вывод данных
# print('Введите а');
# a = int (input())
# print('Введите b');
# b = int (input())
# print(a+b)

#арифметические операции
#+ - * / % // деление в целых числах ** - возведение в степень

a = 12
b = 8
c = a//b 
print(c)

#управляющие конструкции
#if, else

a = int(input('a = '))
b = int(input('b = '))
if a > b:
    print(a)
else:
    print(b)

for i in 1,2,3,4:
    print(i**2)


for i in range(1, 10, 2):
    print(i)


#задать список можно просто задав  его. Рейндж это не список Тип рейндж надо привести к типу список

numbers = [1,2,3,4,5]
print(numbers)
ran = range[1,6]
print(type(ran))
numbers = list(ran)
print(type(numbers))

