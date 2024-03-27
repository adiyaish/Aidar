'=====Модули и пакеты====='
#Любой файл с расширением .py - модуль 
#Пакет - набор модулей ( обязательно должен быть файл _init_.py)

'=====Работа с файлами====='
# open - функция, которая открывает файлы в определенном режиме

'Режимы'
# r - read (только для чтения)
# w - write(только для записи, каждый раз очищает файл и потом записывает)
# a - append(только для до записи, добавляет данные в конец)
# x - создает файл, но если он существует выйдет ошибка
# b - binary(в бинарном виде)

'=====Read====='
#file = open('test.txt','r')
#print(file.read())

#print(file.writable()) #false
#print(file.readable()) #true

# print(file.read())
# file.seek(0) #перенос каретки на начало
# print(file.read())

# print(file.readline()) # hello
# print(file.readline()) # world
# print(file.readline()) # makers
# print(file.readline()) # bootcamp

# print(file.readlines()) 
# #['hello\n', 'workd\n' ...]

# print(file.tell()) #на каком индексе находится каретка
# print(file.read())
# print(file.tell()) #27

# file.close() #закрывает файл

# open('fbfbfb.txt','r') нет такого файла

'=====Write====='

file = open('py33.txt','w')
# если файла нет, то он создаст его сам

# print(file.writableO()) #True
# print(file.readable())  #False
# print(file.write('PY333333333'))
# print(file.write('HELLOOOOOOO'))

#file.writelines(['hello\n','world\n','py33\n'])
#file.close()

'=====Append====='
# file = open('new_file.txt','a')

#file.write('HELLO WORLD')

#file.seek(10)
#file.write('HELLO WORLD')
#file,close() 


'=====Контекстный менеджер====='
# Конструкция with

with open('new_file.txt','r') as file:
    print(file.read())

print(file.closed) #True

'Запишите данные из list_1 и через каждый элемент пишите *'

list_1 ={'Hello','world','bootcamp'}

with open('new_file.txt','w') as f:
    for i in list_1:
        f.write(i+'*'+'\n')
                


