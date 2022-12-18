# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет

import os
clear = lambda: os.system('cls')
clear()

number = (int(input("Введите номер дня недели: ")))
while number > 7 or number < 1:
    number = (int(input("Ошибка! Введите номер дня недели: ")))

if number == 6 or number == 7:
    print("да! супра!")
else:
    print("нет, иди работай")