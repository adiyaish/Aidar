'====SET===='
#множество - изменяемый,неупорядочный,итерируемый тип данных, предназначенный для хранения уникальных значений. Множество могут хранить в себе только неизменяемых тип данных. Если внтури set, используется tuple, то и внутри tupl' а должны быть неизменяемые типы данных ({1,2,0,23,('str',12,True)}). В set работает правило-FIFO (first in first out)

#set_1={True,0,1,'hi'} #1 удаляется
#set_2={1,0,True,'hi'}#True удаляется
#print(set_1)

'====FIFO/LIFO===='
#FIFO-first in first out (очередь в банк, выйдет первым тот кто первым стал в очередь)
#LIFO-last in first out  (стопка бумаг, выйдет та бумага которую вы поставили последним)

'====Методы set===='
'add - добвляет элементы в set'
#set_1 = {1,2,3}
#print(set_1) #{1,2,3,5}
 
'pop-удаляет случайный элемент из set (FIFO)'
#set2 = {1,2,3}
#popped = set2.pop()
#print(set2) 

'remove - удаляет элемент из ser по значению'
#set3 = {1,2,3}
#set3.remove(3)
#print(set3)

#print(dir(set))

'union-объединяет set1 и set2'

#set1 = {1,2,3}
#set2 = {4,5,6}
#set1.union(set2)
#print(set1)

'update-объединяет set1 и set2 и сохраняет изменения в set1'

#set1 = {1,2,3}
#set2 = {4,5,6}
#set1.update(set2)
#print(set1)

'differrence(-) - находит разницу из set1 при помощи set2'
#set1 = {1,2,3}
#set2 = {3,4,5}
#print(set1.difference(set2)) #{1,2}
#print(set2.difference(set1)) #{4,5}
#print (set1-set2) #{1,2}

'symmetric difference-'
#set1 = {1,2,3}
#set2 = {3,4,5}
#print(set1.symmetric_difference(set2))
#{1,2,4,5}

'intesection (&)- находит схожие элементы из двух сетов set1,set2'

#set1 = {1,2,3,4}
#set2 = {3,4,5,6}
#print(set1.intersecion(set2)) #{3,4}
#print(set1 & set2) #{3,4}






























