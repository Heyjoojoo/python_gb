#напишите программу, которая определит позицию вхождения строки в списке либо сообщит, что ее нет
# *Пример:*

# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# - список: [], ищем: "123", ответ: -1

my_list = ['йцу', 'вмлт',  'ывлдм']
search = 'йцу'
count = 0
for i in range(len(my_list)):
    if my_list[i] == search:
        count+=1
        if count == 2:
            print(i)
            break       
    elif (i == len(my_list) - 1):
        print(-1)    


