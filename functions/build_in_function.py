'=====Встроенные функции====='
#map, filter, reduce, zip, enumerate

'ZIP'
# соединяет несколько последовательностей (получаем генератор, в котором элементы-tuple)

#list1 = [1,2,3,4]
#list2 = ['a','b','c','d']
#list3 = [10.5, 20.6, 35.8, 0.5]

#zipped = zip(list1,list2,)
#print(list(zipped)) list[tuple,tuple,tuple]
#print(dict(zipped)) dict{k:v,k:v,k:v}


'ENUMERATE'
#нумерует последовательность (по дефолту с 0) (тоже возвращает генератор)
#enumerated = enumerate ('hello') #<enumarate object  at 0x7d70df94df40>
#print(list(enumerated))
#[(0, 'h'), (1, 'e'), (2, 'l'), (3, 'l'), (4, 'o')]

# for i in enumerated:
#     print(i)
#[(0, 'h')
#(1, 'e')
#(2, 'l')
#(3, 'l')
#(4, 'o')

# enum = enumerate ([12,8,'hi',True,'HELLO',None],15)
# #print(list(enum))

# for n, v in enum:
#     print(f'Номер: {n},Значение:{v}')

'Map'
#принимает другую функцию и последовательность. Мэп применяет функцию, которую передали на каждый элемент из последовательности. Возвращает map объект

# list_=[1,2,3,4]
# def func (a):
#     return str(a)

# mapped = map(func,list_)
# print(mapped) #<map object at 0x77624033ff70>
# print(list(mapped)) #['1','2','3','4']
 
# list_1 = [1,2,3,4] #->[1,4,9,16]
# def func (a):
#     return a ** 2

# mapped = map(func,list_1)
# print(mapped)


'lambda- это однаразовая, анонимная функция'
# def func(num1):
#     return num1 ** 3

# func(2) #8
 
# result = lambda num1: num1**3
# print(result(2))

# print((lambda num1: num1 ** 3))(2)
# #Возведите каждый элемент листа во 2 степень

# mapped = map(lambda a: a** 2, list_1)
# print(list(mapped))

'Filter'
# принимает другую функцию и последовательность, применяет функцию, которую мы передали на каждыйй элемент  последовательности и оставляет только те элементы, которые прошли проверку

# list_1=[-10,0,39,-12,-3,23,1,0]# -> [0,39,23,1,0]
# def func(a):
#     return a >= 0list_1 = [1,2,3,4] #->[1,4,9,16]
# def func (a):
#     return a ** 2


# mapped = map(func,list_1)
# print(mapped)

# filtered = filter(func, list_1) 
# print(list(filtered)) #[0,39,23,1,0]

# filtered=filter(lambda a: a>=0,list_1)
# print(list(filtered)) 

# list_1 = [1,2,3,4,5,6,7,8] #-> [2,4,6,8]
# def func(a):
#     return a % 2 ==0
# filtered = filter (func,list_1)
# print(list(filtered))

'REDUCE'
#принимает функцию и последовательность, возвращает 1 результат (передаваемая функция, должна принимать 2 аргумента)

from functools import reduce

list_1 = [12,3,0,5]
print(reduce(lambda a,b: a + b, list_1))





 













