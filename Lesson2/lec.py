# функции:
# def function_name(x):
#     body line 1
#     body line n
#     optional return


def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return

def new_string(symbol, count=3):
    return symbol * count

print(new_string('!', 5)) #!!!!!
print(new_string('!')) #!!!
print(new_string(4)) #12

def concatenatio(*params):
    res: str = ""
    for item in params:
        res += item
    return res

print(concatenatio('a', 's', 'd', 'w'))


#рекурсия

def fib(n):
    if n in (1, 2):
        return 1
    else: 
        return fib(n-1) + fib(n-2)

list = []
for e in range(1, 10):
    list.append(fib(e))
print(list) #1 1 2 3 5 8 13 21 34

#кортежи, неизменяемый список
a, b = 3, 4 #множественное присваивание
a = (3,4) #кортеж
print(a[0]) #3


#словари неупорядоченные коллекции произвольных объектов с доступом по ключу
dictionary = {}
dictionary = \
    {
        'up': 'вверх',
        'left': 'влево',
        'down': 'вниз',
        'right': 'вправо'
    }

    #обратный слэш нужен чтобы перенести на новую строку

print(dictionary)
print(dictionary['left'])

#типы ключей могут отличаться
for k in dictionary.keys(): # получить все ключи
    print(k)

for k in dictionary.values(): # получить все значения
    print(k)

#множества
colors = {'red', 'green', 'blue'}
print(colors)

colors.add('red')
print(colors) #red green blue
colors.add('gray')
print(colors) #red green blue gray
colors.remove('red')
print(colors) #green blue gray
colors.discard('red') #ok
print(colors) #green blue gray
colors.clear() # { }
print(colors) #set()

s = frozenset(a) #замороженное множество, нельзя изменять


#списки

list1 = [1,2,3,4,5]
list2 = list1 #при копировании списков дальнейшие изменения и в исходнике и в копии будут влиять друг на друга

list1.pop #извлекает и удаляет значение из списка. По умолчанрию последний элемент, если не указать явно, какой
list1.insert #добавляет значение туда, куда укажешь через запятую, сдвигая все остальные значения
