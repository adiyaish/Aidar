'====Области видимости====='
#LEGB- local enclosed global build-in

'Build-in(Встроенное пространство)'
#ЭТо простанство, которое находится в python(print,input,int,str,sum)

'Global(Глобальное пространство)'
#Это пространство, которое находится у вас в файле
#globals()- показывает все глобальные переменные 

#a = 5
#b = 'hello'
#print(globals())

'Enclosed(Замкнутое)'
#Это пространство, которое находится во вложенных функциях

#var = 'global'

#def func():
    #локальное пространство для глобального пространства
    #замкнутое пространство (потому что есть более локальное пространство)
   # var = 'enclosed'
   # def func2():
        #Локальное пространство для пространства func
   #     var = 'local'
  #  print(var)
 #   func()

#print(var)
#func()

'local(Локальное пространство)'
#Это пространство, которое находится внутри функции
#locals()- выводит переменные локального пространства

a = 10

#def func (a,b):
   # print(a,b)
   #print('глобальное',globals)
  #   print( 'Локальное',locals())

#func(0, 1)

'Global-это оператор, который позволяет менять переменную с глобального пространства'

#var = 'globals'
#def func():
 #   print(var)
  #  var = 10

#print(var)
#func()
#print(var)


#def func():
 #   var = 'enclosed'
  #  def func2():
   # var = 'local'
   #print(var) #enclosed
   # func2()
   # print(var)#local
#func()

'nonlocal-это оператор, который позволяет менять переменную с не локального пространства'

#Напишите функцию которая увеличивает глобальную переменнную count

count = 0

def incr():
    global count
    count = count + 1

incr() #1    
incr() #2
incr() #3
incr() #4 
incr() #5 
print (count) #5




















    



