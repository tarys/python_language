#task1------------------------------------------------------------
"""
	По данному целому числу N распечатайте все квадраты натуральных чисел, не превосходящие N, в порядке возрастания.
"""



''' 
    программа распечатывает все квадраты натуральных чисел 
    которые не превосходят число N(которое вводит пользователь)
'''
N=int(input('enter the number')) # number which enter user
i=1 # integer numbers
K=1
while K<=N:
    K=i**2
    if K>N:
        break
    print(K)
    i+=1
	
#-----------------------------------------------------------------


#task2------------------------------------------------------------
"""
	Дано целое число, не меньшее 2. Выведите его наименьший натуральный делитель, отличный от 1.
"""



# program print smaller divisor (i) of number N 
# N>2 and i!=1 
N=int(input())
i=2 #smaller division
while N%i != 0:
    i+=1
print(i)
#-----------------------------------------------------------------


#task3------------------------------------------------------------
"""
	По данному натуральному числу N найдите наибольшую целую степень двойки, не превосходящую N. Выведите показатель степени и саму степень.
	Операцией возведения в степень пользоваться нельзя!
"""


'''
    program which print the biggest power of 2 
    which is no more then N (number which user input)
'''
i=1 #power of 2
number=1
i=0
N=int(input())
while number<N:
    number*=2
    i+=1
if number>N:
    number=number//2
    i+=-1
print(i,number)
#-----------------------------------------------------------------


#task4------------------------------------------------------------
'''
	В первый день спортсмен пробежал x километров, а затем он каждый день увеличивал пробег на 10% от предыдущего значения. 
	По данному числу y определите номер дня, на который пробег спортсмена составит не менее y километров.
	Программа получает на вход действительные числа x и y и должна вывести одно натуральное число.
'''



# program of calculating the number of day which we search
# we searh the day when y==x (x=x+0.1x every day)
# x-frist distance; y-last distance; i-day
x=int(input())
y=int(input())
i=1
while 1==1:
    if x>=y:
        print(i)
        break
    x += x/10
    i+=1
#-----------------------------------------------------------------


#task5------------------------------------------------------------
'''
	Вклад в банке составляет x рублей. Ежегодно он увеличивается на p процентов, после чего дробная часть копеек отбрасывается. 
	Определите, через сколько лет вклад составит не менее y рублей.
	Выражение «дробная часть копеек отбрасывается» означает, что если у вас оказалось 123.4567 рублей, т. е. 123 рубля и 45.67 копеек,
	то после округления у вас получится 123 рубля и 45 копеек, т.е. 123.45 рублей.
	Программа получает на вход три натуральных числа: x, p, y и должна вывести одно целое число.
'''


#program of calculating the deposit in the bank 
#x-bank deposit; p-precent; y-deposit which we need; i-year
x=int(input())
p=int(input())
y=int(input())
i=1
while x<=y:
    x += (x*p)/100
    x = int(x*100)/100 
    
    if x>=y:
        print(i)
        break
    i+=1
#-----------------------------------------------------------------



#task6------------------------------------------------------------
'''
	Программа получает на вход последовательность целых неотрицательных чисел,
	каждое число записано в отдельной строке. Последовательность завершается числом 0,
	при считывании которого программа должна закончить свою работу и вывести 
	количество членов последовательности (не считая завершающего числа 0). 
	Числа, следующие за числом 0, считывать не нужно.
'''


#program which calculating how much numbers user input into the program
#program stop when user input 0
i=1
while 1==1 :
    N=int(input()) #numbers which input user
    if N==0:
        print(i-1)
        break
    i+=1
#-----------------------------------------------------------------



#task7------------------------------------------------------------
'''
	Определите сумму всех элементов последовательности, завершающейся числом 0.
	В этой и во всех следующих задачах числа, следующие за первым нулем, учитывать не нужно.
'''


#program which calculating the sum of numbers user input into the program
#program stop when user input 0
sum=0
while 1==1:
    N=int(input()) #numbers which input user
    sum += N
    if N==0:
        print(sum)
        break
#-----------------------------------------------------------------


#task8------------------------------------------------------------
'''
	Определите среднее значение всех элементов последовательности, завершающейся числом 0.
'''


#program which calculating the average value of numbers which user input into the program
#program stop when user input 0
sum=0
i=1
while 1==1:
    N=int(input())#numbers which user input
    sum += N
    if N==0:
        print(sum/(i-1))
        break
    i+=1
#-----------------------------------------------------------------


#task9------------------------------------------------------------
'''
	Последовательность состоит из натуральных чисел и завершается числом 0.
	Определите значение наибольшего элемента последовательности.
'''


#program which search the biggest number of numbers which user input into the program
#program stop when user input 0
N=int (input())#numbers which input user
maximum=N
while True :
    N=int (input())#numbers which input user
    if N==0:
        break
    if N>maximum:
        maximum=N
print (maximum)
#-----------------------------------------------------------------


#task10------------------------------------------------------------
'''
	Последовательность состоит из натуральных чисел и завершается числом 0.
	Определите индекс наибольшего элемента последовательности.
	Если наибольших элементов несколько, выведите индекс первого из них. Нумерация элементов начинается с нуля.
'''


#program which search index of the biggest number of 
#numbers which user input into the program
#program stop when user input 0
element=int (input())
max_element=element
index=0
index_max=index
while True:
    element=int (input ()) 
    index+=1
    if element==0:
        break
    if element>max_element:
        max_element=element
        index_max=index
print (index_max)
#-----------------------------------------------------------------


#task11------------------------------------------------------------
'''
	Определите количество четных элементов в последовательности, завершающейся числом 0.
'''


#program which calculating how many even number of 
#numbers which user input into the program
#program stop when user input 0
i=0
while 1==1 :
    N=int(input())#numbers which user input
    if N==0:
        break
    if N%2==0:
        i+=1
print(i)
#-----------------------------------------------------------------


#task12------------------------------------------------------------
'''
	Последовательность состоит из натуральных чисел и завершается числом 0.
	Определите, сколько элементов этой последовательности больше предыдущего элемента.
'''


#program which calculating how many number more then previous 
#numbers user input into the program
#program stop when user input 0
element=int(input())
previous_element=element
i=0
while element!=0:
    element=int(input())
    if element>previous_element:
        i+=1
    previous_element=element
print(i)
#-----------------------------------------------------------------

#task13------------------------------------------------------------
"""
	Последовательность состоит из различных натуральных чисел и завершается числом 0.
	Определите значение второго по величине элемента в этой последовательности.
	Гарантируется, что в последовательности есть хотя бы два элемента.
"""



#program which search the second maximum of numbers 
#numbers user input into the program
#program stop when user input 0
element=int(input())
maximum=element
second_maximum=0
while 1==1:
    element=int(input())
    
    if element==0:
        break
    
    if element>maximum:
        second_maximum=maximum
        maximum=element
    if element<maximum and element>=second_maximum:
        second_maximum=element
print(second_maximum)

#-----------------------------------------------------------------


#task14------------------------------------------------------------
"""
	Последовательность состоит из натуральных чисел и завершается числом 0. 
	Определите, сколько элементов этой последовательности равны ее наибольшему элементу.
"""



#program which calculating how many numbers == the biggest number 
#numbers user input into the program
#program stop when user input 0
element=int(input())
maximum=element
i=1
while element!=0:
    element=int(input())
    if maximum==element:
        i+=1
    if element>maximum:
        maximum=element
        i=1
print(i)
#-----------------------------------------------------------------


#task15------------------------------------------------------------
"""
	Последовательность Фибоначчи определяется так:
	φ0 = 0,  φ1 = 1,  φn = φn−1 + φn−2.
	По данному числу n определите n-е число Фибоначчи φn.
	Эту задачу можно решать и циклом for.
"""



#program which calculating the number of Fibonaccci
n=int(input())
previous_element=0
element=1
next_element=0
i=1
while n>=i:
    next_element=element+previous_element
    i+=1
    previous_element=element
    element=next_element
    if i==n:
        break
print(next_element)

#-----------------------------------------------------------------

#task16------------------------------------------------------------
"""
	Дано натуральное число A. Определите, каким по счету числом Фибоначчи оно является,
	то есть выведите такое число n, что φn = A. Если А не является числом Фибоначчи, выведите число -1.
"""



#program which search the index of number of Fibonacci
#A-integer number; i-index of number A (if A==number_of_Fibonacci)
#if A!=number_of_Fibonacci print -1
A=int(input())
previous_element=0
element=1
next_element=0
i=1
while 1==1:
    next_element=element+previous_element
    i+=1
    previous_element=element
    element=next_element
    if A==next_element:
        break
    if A<next_element:
        break
if A<next_element:
    print(-1)
else:
    print(i)

#-----------------------------------------------------------------


#task17------------------------------------------------------------
"""
	Дана последовательность натуральных чисел, завершающаяся числом 0.
	Определите, какое наибольшее число подряд идущих элементов этой последовательности равны друг другу.
"""



#program which calculating how many number == previous number
#numbers user input into the program
#program stop when user input 0
amount=1
maximum=1
n=int(input())
while n!=0:
    b=n
    n=int(input())
    if b==n:
        amount+=1
    elif amount>maximum:
        maximum=amount
        amount=1
    else:
        amount=1
print(maximum)

#-----------------------------------------------------------------


#task18------------------------------------------------------------
"""
	Дана последовательность натуральных чисел x1x1, x2x2, ..., xnxn.
	Определите стандартное отклонение для данной последовательности натуральных чисел, завершающейся числом 0.
"""



#program which calculating the standard deviation 
#numbers user input into the program
#program stop when user input 0
x=int(input()) #nubers which user input
numerator=x 3 #numerator of average 
numerator_CO=0 # numerator of stanard deviation 
s=0 #average
i=1
CO=0 #stanard deviation
list_1=[x]
while 1==1:
    x=int(input())
    if x==0:
        for j in list_1:
            numerator_CO+=(j-s)**2
        CO=(numerator_CO/(i-1))**(1/2)
        break
    list_1.append(x)
    numerator+=x
    i+=1
    s=numerator/i
print(CO)

#-----------------------------------------------------------------


