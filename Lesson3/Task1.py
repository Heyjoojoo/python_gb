# Задайте список. Напишите программу, которая определит,
#  присутствует ли в заданном списке строк некое число.

my_list = ['sdvknskv', 'dcecv']
search = 'sd'

for i in my_list:
    if i.count(search)>0:
        print('yes')
    else:
        print('no')
