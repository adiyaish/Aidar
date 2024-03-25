'==String=='
#  строки - неизменяемый тип данных, который предназначен для 
#хранения текста заключенного в одинарные либо двойные кавычки
string1='строка с одинарными кавычками'
string2='строка с двойными кавычками'
string3='Dont'# внутри двойных кавычек все одинарные кавычки-просто часть текста
string4='Название магазина азбука'
string5=''''''
"""_Многострочный текст 
в одинарных кавычках """   


string6='''
Многострочный текст
в двойных авычкых
тут можно использовать и одинарные и двоные кавычки
'''
string7='hello'+'world'# hello world
print(string7)

string8='A'* 3
print(string8)

'==Экранизация строк=='
'\n' #  перенос на новую строку
print('hello world') #hello world
print('he\nllo world') #hello 

                       #world
'-------------------'

print('he\nloo world') #he
                       #llo world
'--------------------'
'\t' # табуляция(несколько пробелов)
print('hello\tworld') #hello world
print('he\tllo world') #he  loo world

'\v' #перенос на новую строку со смещением вправо на длинну предыдущей строки
print('hello\vworld\vmakers') #hello
                               #world
                                   #makers

'\r' #перенос каретки в самое начало строки
print('hello world\rMa') #Mallo world


'\'' #отображение
"\""#отображение

print('Don\'t')
print("Home\\'Makers")
'\\' #отображение
print('команда\\n-переносит строку')

'===Формативная строк==='
title='Iphone15'
price=1000
print('я купил title за price')
shop='Makers'
'1.f строка'
print(f'я купил(title)з (price), в магазине( shop)')


'2.%s'
print('Я купил %s за %s $' %(title,price)) 

'3. str.format'
print(' я купил () за ()$, в магазине ()' .format)
(title,price,shop)

"===Методы строк(str)==="
#Методы- функции, которые относятся к определенному типу данных
#(классу), к ним мы обращаемся через точкy
print(dir(str))

string = 'hello world'

# print(string.upper()) #HELLO WORLD
# print(string.lower()) #hello world
# print(string.swapcase()) #hello WORLD

# print(string.title()) #Hello World
# print(string.capitalize()) #HELLO WORLD

# print(string.islower()) #True  да
# print(string.isupper()) #False нет

# print(string.center(12,'*')) #'*****Hi*****'

# string='hello world'
# print(string.count('l')) #3
# print(string.count('el')) #1
# print(string.count('o w')) #1
# print(string.count('hello')) #1

# print(string.startswith('h')) #True
# print(string.startswith('H')) #False
# print(string.startswith('hello')) #True
# print(string.endswith('ld')) #True

# string='makers'
# print(string.isalpha()) # True, проверяет на буквы
# print(string.isdigit()) #False, проверяет на числа
# print(string.isalnum()) #True, проверяет является ли строка
# #числом или буквой или и числом и буквой, если есть 
# # символ то вернет False
# string='hello. world.makers.bootcamp'
# print(string.split('.')) #('hello', 'world,'makers','bootcamp')

# #('hell','.w','rld.makers.b,'','tcamp')
# print(string.replace('','$'))
# string=' $12 hi$$$$$$$$$$$$'
# print(string.strip('$')) #убрал доллар

#''.join(string)#string-это переменная которая хранит тип  даннных list()


'===Индексы==='
# индекс- порядковый номер элемента в последовательности(индекс начиная с 0)

#-11-10-9-8-7-6-5-4-3-2-1 
#  'h e l l o  w o r l d'
#   0 1 2 3 4 5 6 7 8 9 10

# string= 'hello world'
# print(string(0)) #'h'
# print(string(-1)) #'d'
# print(string(5)) #' '

# #срез (start:end(не включительно):step)
# string(6:10) #worl
# string(:5) #hello
# print (string(::2)) #hlowrd
# print(string(::-1)) #dlrow olleh
# print(string(::-2)) #drwolh



