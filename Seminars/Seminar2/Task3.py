n = float(input("Введите число: "))
if n%1 == 0:
    print("Нет")
else:
    print(int(abs(n)*10%10))

number = input("Введите число")
number = number.split('.')
print(number[1][0])