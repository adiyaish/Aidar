'====Словари===='
# dict- изменяемый, итерируемый,неупорядочный (псевдопорядок), неиндексируемый тип данных,для хранения даннных в парах {ключ:значение}

#user = {'name':'Anonym', 'age':30, 'last name': 'Makers' }
#print(user['name']) #Anonym
#print(user['age']) #30
#print(user['last name']) #Makers

#ключами с словаре могут быть только неизменяемые типы данных
#ключи в словарях должны быть уникальными

'====Создание словарей===='
#dict_ = {'a':1, 'b':1 }
#dict_ = dict([('a',:1), ('b',2)])
#print(dict_) 
#dict_= dict(['a1', 'b2','c3'])
#print(dict_) #{'a':'1', 'b':'2', 'c':'3'}

#dict_={}
#dict_['name'] ='makers'
#dict_['age'] = 50
#dict_['last name'] = 'bootcamp'
#print(dict_) 

'====Методы словаря===='
 
'get-метод, который получает значение по ключу, если указанного ключа нет, то выходит None- по умолчанию, мы можем его поменять'
user = {'name':'Anonym', 'age': 15, 'last_name': 'Makers'}
 
# print(user['id']) #error-KeyError
#print(user.get('id')) #None
#print(user.get('id'), 'Такого ключа нет') #'Такого ключа нет'

'pop-удаляет пару по ключу и возвращает значение'
#dict_={'a':1, 'b':2, 'C':3}
#popped = dict_.pop('b')
#print(dict_) #{'a':1, 'c':3}
#print(popped) # 2

'popitem-удаляет последнюю пару и возвращает ее'
#dict_={'a':1, 'b':2, 'c':3}
#popped= dict_.popiten()
#print(dict_) #{'a':1, 'b':2}
#print(popped)#('c',3)

'update- расширяет словарь парами из второго словаря'

#dict_1={1:'a', 2:'a'}
#dict_2={2:'b', 3:'b'}
#dict_1. update(dict_2)
#print(dict_1) #{1:'a', 2:'b',3:'b'}
'clear-очищает словарь'
#dict_={'a':1, 'b':2,'c':3}
#dict_.clear()
#print(dict_) #{}

'fromkeys- метод для создания нового словаря, используя список ключей'

#dict_=dict.fromkeys('hi')
#print(dict_) #{'h':None, 'i':None}
#dict_2 = dict.fromkeys(['hi', 123, True])
#print(dict_2) #{'hi':None, 123:0, True:0}

'keys, value,items'
#keys-метод, который возвращает все ключи
#value-метод, который возвращает все значения
#items-метод, который возвращает пары ключь и значение в виде tuple
user = {
    'name':'Anonym',
    'age':15,
    'last_name':'V=Makers'
}
print(user.keys()) #dict_keys(['name', 'age', 'last_name'])
print(user.values())#dict_values(['Anonym', 15, 'V=Makers'])
print(user.items())#dict_items([('name', 'Anonym'), ('age', 15), ('last_name', 'V=Makers')])

'=====Итерирование словарей====='
user
user = {
    'name':'Anonym',
    'age':15,
    'last_name':'V=Makers'
}
for key in user.keys():
    print(key) 
#при итерации словаря будут проходить ключи
    
for value in user.values():
    print(value)
#при итерации словаря с методом values(), приходять значения

for item in user.items():
    print(item)
#при итерации словаря с методом items(),приходят tuple с ключем и значением
 
'-----------------------------------------------'
# у нас есть dict_1={1:'a', 2:'b'}
# вам нужно создать новый словарь dict_2 при помощи кода
#dict_2={'a':1, 'b':2}

#for, .items(), dict_2[]

# dict_1 = {1:'a', 2:'b'}
# dict_2={}

# for k, v in dict_1.items():
#     dict_2[v]=k

# print(dict_2)
