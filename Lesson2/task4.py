#создать список длины n, где значения формируются по 
# формуле 3k+1 где k принимает значения от 1 до n включительно


n = int(input("Введите число: "))
new_list = []

for k in range(1, n+1):
    new_list.append(3*k+1)
print(new_list)

