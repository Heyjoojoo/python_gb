# программа принимает N и выводит 
# последовательность от -N до N

n = int(input("Введите N: "))
for i in range(-n, n+abs(n)//n, n+abs(n)//n):
    print(i, end=', ')

