'====Excetions===='
#Исключение-объекты, которые прерывают работу кода, если не были обработаны

SyntaxError
#исключение, которое выходит, когда в коде допущена синтаксическая ошибка

'''
a =
SyntaxError
'''

NameError
#исключение которое выходит когда мы обращаемся к несуществующей переменной

'''
num=15
print(num15)
NameError
'''

IndexError
# исключение, которое выходит когда мы обращаемся по несуществующему индексу

'''
list_=[12,20,0,2]
print(list_[1000])
IndexError
'''
'''
[12,0,24,'hi'].pop(1000)
IndexError
'''

'''
[].pop()
IndexError:pop from empty out of range
'''
KeyError
#исключение, которое выходит, когда мы обращаемся по несуществующему ключу
'''
dict_={'a':1}
dict_['c']кк
KeyError
'''
'''
dict_={'a':1}
dict_.get('c') #None
ошибки не будет!! Так как get не вызывает ошибку, а вернет None, если такого ключа нет
'''
ValueError
#когда мы передаем функцию не корректный для нее тип данных
#когда мы распаковываем итерируемый объект на несколько переменных и кол-во переменных не совпадает с кол-во элементов
'''
int('10cf')
ValueError
'''

'''
a,b,c=2,3
ValueError
'''

TypeError
#исключение выходит,когда мы пытаемся использовать методы не свойственные какому то типу данных
#когда мы пытаемся передать функции больше или  меньше аргументов чем принимает функция
'''
for i  in 1234:
'''
TypeError


'''
"5"+5
TypeError
'''

'''
{[1,2,3]:'hi'}
TypeError
'''

'''
input('Введите число',123)
TypeError:
'''

'''
[].append()
TypeErro

'''

ZeroDivisionError
'''
45/0
ZeroDivisionError
'''

'''
45//0
ZeroDivisionError

'''
'''
45%0
ZeroDivisionError
'''
AttributeError
#выходит, когда мы обращаемся к несуществующему аттрибуту или методу объекта (типа данных)

'''
[1,23,1,56].replace('a','')
AttributeError
'''

'''
'makers'.pop(0)
AttributeError
'''

IndentationError
#выходит, когда мы не правильно используем отступы
'''
a=5
IndentationError
'''

'''
for i in range(11):
print(i)
IndentationError
'''

Exception
#исключение, которое создали, чтобы его вызывать

'====Вызов исключений===='
#raise NameError('Просто вызываю NameError')
#raise IndexError
#raise KeyError

'====Обработка исключений===='
#Чтобы код не прекращал свою работу, мы можем использовать конструкцию try-except, и обрабатывать вызванное исключение
#try: #код, который может вызвать ошибку\исключение
   # num=(input('Введите число:'))
#Except ValueError: #Ожидаемую исключение
  #  #Обработку на исключение которое поймали
   # print('Вы вели не число')
#else: #код, который отработает, если исключения не вышло
 #   print('Вы ввели число {num}')
#finally
   #работает всегда
   # print('До свидания')
    
#try:
#num = int(input('Введите число'))
 #  res = 10/num

#except (ValueError,ZeroDivisionError):
 #   print('Что-то пошло не так')

#except:обрабатывает все исключения, которые могут выйти
#except Exception:обрабатывает все исключения, которые могут выйти

#можем указать except несколько исключений при помощи скобок и запятой except (ValueError,TypeError,ZeroDivisionError)

#try:
 #   raise NameError
#except NameError:
 #   print(1)


'Напишите программу при помощи try-except, пользователь вводит число, вам нужно сделать проверку на положительность, отрицательность и 0'
'Положительное число, должно выходить исключение ValueError'
'Отрицательное число, должно выходить исключение TypeError'
'0, должно выходить исключение ZeroDivisionError'

# try:
#     num = int(input('Введите число: '))
#     if num == 0:
#         raise ZeroDivisionError
#     elif num > 0:
#         raise ValueError
#     elif num < 0:
#         raise TypeError
# except ValueError:
#     print('Положительное')
# except TypeError:
#     print('Отрицательно')
# except ZeroDivisionError:
#     print('0')































