'===Lists==='
#списки изменяемый,индексируемый, упорядочный итерируемый тип данных предназначенный для хранения любых данных в определенном порядке

list_1=[1,2,14,'hello', True,[0,0,0], None]
       #0 1  2   3        4      5       6

list_1[3]#'hello'
list_1[-1]#none
list_1[-2][-1] #0
list_1[3][-2]#l
list_1[5]#[0,0,0]

#list('hello') -> {'h','e','l','l','o'}
list_2=list (range(0, 101)) #[0,1,2,...,99,100]
print(list_2) 
print(list(range (50,71))) #[50,51,...,69,70]
'range-(start, end (не включительно),step)-это функция генератор,которая генерирует\создает диапозон от start до end (не включительно)'

print(list(range(11, 4, -1))) #0-можно не указывать
#[0,2,4,6,8,10] шаг2
#[10,9,8,7,6,5,4,3,2,1,0] шаг -1

'===Методы списков==='
'append-добавление элемента в конец списка'
#list_=[1]
#list_.append(1)
#list_.append('hello world')
#list_.append(True)
#print(list_) #[1,'hello world', True]
'pop-удаление элемента из списка по индексу, возвращает удаленный элемент. Если не указать индекс, то удалит с конца'

list_=[90, True,None,'Hi']
popped=list_.pop(1)
print(list_)  #[90,None,'Hi']
print(popped) #True

'remove-это удаление элемента из списка по значению' 
#list_=[1,2,3,1,'hi',5,99,0,-11]
#list_.remove(1)
#print(list_)

'count-считает кол-во принятого элемента в списке'
 
#list_=[1,23,1,'hi','hi',5,6,1,7,1,7,8,1,'Hi']
#print(list_.count(1)) #5
#print(list_.count(7)) #2
#print(list_.count('hi')) #2

'index-возвращает индекс первого вхождения принятого элемента'

list_=['hi',1,341,2,0,'makers',2,1,99,10]
print(list_.index('hi')) #0

'extend-расширяет список при помощи другого списка'

#list_1=[1,2,3]
#list_2=[0,0,0]
#list_1.append(list_2) #[1,2,3,[0,0,0]]
#print(list_1)
#list_1.extend(list_2) #[1,2,3,[0,0,0],0,0,0]
#print(list_1)

'revers-изменяет список, расставляя его элементы в обратном порядке'

list_=['hi',1,2,3,True]
list_.reverse()
print(list_) # [[1,2,3], True,3,2,1,'hi']

'sort-сортирует список, состоящих из элементов одно тип данных'

list_=[12,4,1,0,25,7]
list_.sort(reverse=True)
print(list_)

list_=['c','b','a','A','B']
list_.sort()
print(list_) #['A','B','a','b','c']

'clear-очищает список'
list_=[12,42,1,'hi',0,False,None]
list_.clear()
print(list_) #[]

len([12,4,5[1,2,3]]) #4

list_=[23,'hi',4,0,'makers']

for i in list_:
    print(i)

meshok=['картошка','лук', 'лук', 'картошка', 'лук']

paket1=[]
paket2=[]

for ruka in meshok:
       if ruka == 'картошка':
          paket1.append(ruka)
       elif ruka == 'лук':
          paket2.append(ruka)    
print(paket1)
print(paket2)













