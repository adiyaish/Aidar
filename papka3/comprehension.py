'====comprehension===='
# генератор, с помощью которого можно создать последовательность используя цикл for в одну строку

# range()
# [][/]
# {}
# {:}

# результат for элемент in последовательность 
#list1 = [x + 2 for x in range (11)]
#print(list1) #[2,3,..]

'Создайте список состоящий из четных чисел от 1 до 10 используя comprehension'
#list_= []
#for i in range(1,11):
#    if i % 2 ==0:
#        list_.append(i)
#print(list_)        

#list_ = ['четный' if  i % 2 == 0 i % 2!else 'нечетный' for i in range i in range (1,11)]
#print(list_)

'В comprehension можно добавлять условия, там их бывает 2 вида'
'1- тернарный оператор, пишется перед циклом, так как используем и if, и else'
'2- фильтр, пишется после цикла, так как используется только if'

# Создать список из существующего списка, оставив только строки
#list_1 = [12,True,None,'hi', 0, False, 'makers','world']

#list_2=[i for i in list_1 if type(i)==str ]
#print(list_2) #['hi','makers','world']

#a =12
#print (type(a)==int) #True

'====Виды comprehension===='
'1-list comrehension'
'2-dict comprehension'
'3-set comprehension'

'Dict comprehension'
#dict_1 = {i:i for i in range(1,11)}
#print(dict_1)
#{1:1,2:4,3:9,...}

'дан словарь dict_1, поменяйте ключи и значение с помощью comprehension'
dict_1 = {'a':1,'b':2,'c':3}
dict_2 = {value: key for key, value in dict_1.items()} 
#{1:'a',2:'b',3:'c'}
print(dict_2)

'Дань словарь, где значение- списки из чисел, создайте словарь, где значение суммы этих списков'

#dict_1={
 # 'a':{1,2,3}
#  'b':[12,0,1],
#    'c':[32,0,0,10]
#}

#dict_2={k:sum(v) for k, in dict_1.items()}
#{'a':6, 'b':13,'c':42}
#sum ([10,20,0]) -> 30

'set comprehension'

#set_1={i for i in range (1,11)}
#print(set_1) #{1,2,3,4,5,6,7,8,10}


#set_1={i for i in 'makers'}
#print(set_1) #{'m','a','k','e','r','s'}

#set_1 = {2, 3, 4, 15, 1}
#set_2 = {i**2 for i in set_1 } #{4,9,16, , 1}
#print(set_2)

#set_1 = {12, 4, 34, 5, 6}
#set_2 = {str(i)for i in set_1} #{'12','4','34','5','6'}
#print=set_2

'Сохраните только строки'
#set_1={1,12,'hi',34,True,'makers'}
#set_2={i for i in set_1 if type(i) == str } #{'hi','makers'}
#print(set_2)

'Сохраните только строки, те строки в которых хранятся числа переведите c int "12" -> 12?, а простые строки с символами и буквами сохраните'

#set_1 = {12, True ,'Hi',23,'10','makers',False,'1'}
#set_2= {int(i) if i.isdigit() else i  for i in set_1 if type (i)==str}
#{'Hi',10,'makers','1'}
#print(set_2)

'создайте словарь где ключи будут числа от 1 дл 5, а значениями - списки с числами от 1 до этого числа'
{
   1:[1],
   2:[1,2],
   3:[1,2,3],
   4:[1,2,3,4],
   5:[1,2,3,4,5]
}

dict_1 = {i: [i for i in range(1,i+1)] for i in range (1,6)}
print(dict_1)
















