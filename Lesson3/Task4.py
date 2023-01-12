from random import sample

def generate_words(count, word='abc'):
    new_list = []
    for i in range(count):
        temp = sample(word, k=3)
        new_list.append(''.join(temp))
    return new_list

def index_find(word, some_list):
    if word in some_list and some_list.count(word) > 1:
        index_1 = some_list.index(word)
        print(some_list.index(word,index_1+1))
    else:
        print(-1)

list_1 = generate_words(int(input("Введите количество: ")))
print(list_1)
index_find(input(), list_1)
