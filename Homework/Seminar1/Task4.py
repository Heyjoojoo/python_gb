# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

import os
clear = lambda: os.system('cls')
clear()

number = int(input("Введите номер четверти: "))
while number < 0 or number > 4:
    number = int(input("Ну, серьезно, введите нормальный номер четверти (от 1 до 4): "))
if number == 1:
    print("x > 0 and y > 0")
if number == 2:
    print("x < 0 and y > 0")
if number == 3:
    print("x < 0 and y < 0")
if number == 4:
    print("x > 0 and y < 0")
