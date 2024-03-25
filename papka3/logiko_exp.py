'===Логические и условные операторы==='
#boolen-тип данных, который имеет 2 значения
#true(да,истина)и false (нет, ложь)

print(bool(0))#false
print(bool(-10))#true
print(bool(''))#True
print(bool(''))#False
print(bool(None))#False

#Логические операторы- это выражение, которое возвращает True,если выражение  верное,False если не верное
'равенство'
5==5 #True
5==7 # false

'не равенство'
5!=10 # True
5!=5# False
'больше'
5>1#true
0>10#False

'меньше'
10<100 #True
0<-10 #false
5<5#False
'больше или равно'
5>=10 #false
10>=3#True
3>=3 #true
 
'меньше'
10<=5 #False
5<=10 #true
5<=10 #true

'5'==5 #False
'Hello'== 'Hello' # True
'hello'== 'Hello' #False
print('hello'=='hello ') #False

'===And Or Not==='
#and-и
#or-или
#not-нет

'AND- возвращает  True, если все выражения вернули true'  

a= 5
b= 6

#True и  # True
a==5 and b==6 #True

#False и  #True
a==6  and b==6 #False

#True и  #False
a==5 and b==2 #False

#False и #False
a==1 and b==1 #Fasle


'OR -возвращает true, если хотя бы один из выражений вернул true ,  либо когда все выражения вернули true' 

c=5
b=6
  
#True или #True
c==5  or  b==6  #True

#False или  #True
c==1  or   b==6 #True

#True или #False
c==5  or  b<1 #True
 
#False или  #False 
c<=1  or   b>1000 #False

'Not- это частица не, которая меняет значение на противоположное'


a=10 
b=5 
not False  #true
not True #False

#notFalse=true или False и  True 
not a==b       or  b>10 and 10==a #True
 

bool(None) #False
bool ('None') #True
bool ([]) #False








'===Условные операторы==='
#ycловные операторы- это конструкций, которая используется для того , чтобы при разных входных данных код работал по разному (в зависимости от условия)

pagoda='дождь'
if pagoda =='дождь':
    print('взял зонт')
elif pagoda=='снег':
    print('взял шапку и шарф')
elif pagoda=='солнце':
    print('вышел на улицу')
else:   
    print('сижу дома')


# в одной конструкции мы можем использовать только один if
# в одной конструкции мы можем использовать неограниченное кол-во elif или не использовать вообще
# в одной конструкции мы можем использовать только один else или не использовать вообще

# принять от пользователя число, и узнать какое это число , отрицательное, положительное или 0
num=int(input('Введите число:'))

if num > 0:
   print('Число положительное')
else:
   print('Число 0')

'===Тернарный оператор==='
#тернарный оператор- условия в одну строку 


#тело1 if условие1 else тело2

num=10
if num>0:
    message='Положительное число'
else:
    message='Отрицательное число или 0'
print(message)

num=100
message='Положительное число' if num > 0 else 'отрицательное число или 0'
print(message)




   
