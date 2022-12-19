# N = 5: 1, -3, 9, -27, 81 

number = int(input("Введите целое число: "))
for degree in range(number):
    print((-3)**degree, end=', ')
