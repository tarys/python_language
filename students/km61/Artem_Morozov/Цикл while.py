#task1-----------------------------------------------------------------------------------------------------------------------
 """
 По данному целому числу N распечатайте все квадраты натуральных чисел, не превосходящие N, в порядке возрастания.
 """
 #Program prints squares from 1 to n 
 n=int(input('Enter number'))
 i=1
 print('Squares from 1 to n:')
 while i*i<=n: 
  print(i*i)
  i+=1
 
 #-----------------------------------------------------------------
 
 
 #task2------------------------------------------------------------
 """
 Дано целое число, не меньшее 2. Выведите его наименьший натуральный делитель, отличный от 1.
 
 """
 
 #Program prints minimum devider for n 
 n=int(input('Enter number'))
 devider=2
 while n%devider!=0:
  devider+=1
 print('Minimum divider for n=',devider)
 
 #-----------------------------------------------------------------
 
 
 #task3------------------------------------------------------------
 """
 По данному натуральному числу N найдите наибольшую целую степень двойки, не превосходящую N. Выведите показатель степени и саму степень.
 
 Операцией возведения в степень пользоваться нельзя!
 """
 #Program prints 2 in max involution<=n 
 n=int(input('Enter number'))
 involution=0
 number=1
 while number<n:
  involution+=1
  number*=2    
 if number>n:
  involution+=-1
  number=number//2
 print('Max ivlolution of 2=',involution,'2 in max involution<=n:',number)
 
 #-----------------------------------------------------------------
 #task4------------------------------------------------------------
 """
 В первый день спортсмен пробежал x километров, а затем он каждый день увеличивал пробег на 10% от предыдущего значения. По данному числу y определите номер дня, на который пробег спортсмена составит не менее y километров.
 
 Программа получает на вход действительные числа x и y и должна вывести одно натуральное число.
 """
 #Program prints number of day on which the running athlete is not less than y kilometers.
 x=float(input('Enter how much fif the athlete run in the first day'))
 y=float(input('Enter how much he must run'))
 day=1
 while x<y:
     x+=x*0.1
     day+=1
 print('Number of day on which the running athlete is not less than y kilometers:',day)
 
 #-----------------------------------------------------------------
 
 
 #task5------------------------------------------------------------
 """
 Вклад в банке составляет x рублей. Ежегодно он увеличивается на p процентов, после чего дробная часть копеек отбрасывается. 
 Определите, через сколько лет вклад составит не менее y рублей.
 Программа получает на вход три натуральных числа: x, p, y и должна вывести одно целое число.
 
 """
 #Program prints year on which contribution is not less than y rubles.
 x=int(input('Enter bank deposit'))
 p=int(input('Enter percent'))
 y=int(input('Enter needed sum'))
 year=0
 while x<y:
     x+=x*p/100
     x=int(x*100)
     x=float(x/100)
     year+=1
 print('Year on which contribution is not less than y rubles',year)
 
 #-----------------------------------------------------------------
 
 
 #task6------------------------------------------------------------
 """
 Программа получает на вход последовательность целых неотрицательных чисел, каждое число записано в отдельной строке. 
 Последовательность завершается числом 0, при считывании которого программа должна закончить свою работу и вывести количество членов последовательности (не считая завершающего числа 0).
 Числа, следующие за числом 0, считывать не нужно.
 
 """
 #Program calculates length of sequence
 amount=0
 while True:
    a=int(input())
    if a==0:
         break
    amount+=1
 print('Length of sequence=',amount)
 #-----------------------------------------------------------------
 
 #task7------------------------------------------------------------
 """
 Определите сумму всех элементов последовательности, завершающейся числом 0. В этой и во всех следующих задачах числа, следующие за первым нулем, учитывать не нужно.
 """
 #Program calculates sum of sequence
 a=1
 sum=0
 while a!=0:
     a=int(input('Enter number in sequence'))
     sum+=a
 print('Sum of sequence',sum)
 
 #-----------------------------------------------------------------
 
 
 #task8------------------------------------------------------------
 """
 Определите среднее значение всех элементов последовательности, завершающейся числом 0.
 
 """
 #Program calculates the average value of the sequence
 sum=0
 amount=0
 while True:
     a=int(input('Enter number in sequence'))
     if a==0:
         break
     sum+=a
     amount+=1
 print('The average value of the sequence=',sum/amount)
 
 #-----------------------------------------------------------------
 
 
 #task9------------------------------------------------------------
 """
 Последовательность состоит из натуральных чисел и завершается числом 0. Определите значение наибольшего элемента последовательности.
 """
 #Program prints maximum of sequence
 max=0
 while True:
     a=int(input('Enter number of sequence'))
     if a==0:
        break
     if a>max:
        max=a
 print('maximum of sequence',max)
 
 #-----------------------------------------------------------------
 
 #task10------------------------------------------------------------
 """
 Последовательность состоит из натуральных чисел и завершается числом 0.
 Определите индекс наибольшего элемента последовательности. 
 Если наибольших элементов несколько, выведите индекс первого из них. 
 Нумерация элементов начинается с нуля.
 """
 #Program prints index of maximum of sequence
 max=0
 amount=0
 id=1
 while True:
    a=int(input('Enter number in sequence'))
    if a==0:
        break
    amount+=1
    if max<a:
       max=a
       id=amount-1
print('index of maximum of sequence',id)
#-----------------------------------------------------------------


#task11------------------------------------------------------------
"""
Определите количество четных элементов в последовательности, завершающейся числом 0.

"""
#Program prints amount of even elements in sequence
amount=0
while True:
   a=int(input('Enter number in sequence'))
   if a==0:
      break
   if a%2==0:
       amount+=1
 +print('amount of even elements in sequence',amount)
#-----------------------------------------------------------------


#task12------------------------------------------------------------
"""
Последовательность состоит из натуральных чисел и завершается числом 0. Определите, сколько элементов этой последовательности больше предыдущего элемента.
"""
#Program prints amount of elements bigger then previous
amount=0
a=int(input('Enter number in sequence'))
while True:
   b=a
   a=int(input('Enter number in sequence'))
   if a==0:
       break
   if a>b:
       amount+=1
print('amount of elements bigger then previous',amount)
#-----------------------------------------------------------------

#task13-----------------------------------------------------------
"""
Последовательность состоит из различных натуральных чисел и завершается числом 0. 
Определите значение второго по величине элемента в этой последовательности.
Гарантируется, что в последовательности есть хотя бы два элемента.
"""
#Program prints second maximum in sequence
a=int(input('Enter number in sequence'))
max=a
second_max=0
while a!=0:
    a=int(input('Enter number in sequence'))
    if a>max:
        second_max=max
        max=a
    if a>second_max and a<max:   
	    second_max=a
print('second maximum in sequence',second_max)

#-----------------------------------------------------------------


#task14------------------------------------------------------------
"""
Последовательность состоит из натуральных чисел и завершается числом 0. Определите, сколько элементов этой последовательности равны ее наибольшему элементу.

"""
#Program prints amount of elements equal to maximum 
a=int(input('Enter number in sequence'))
amount=1
max=a
while a!=0:
    a=int(input('Enter number in sequence'))
    if a==max:
        amount+=1
    if a>max:
        max=a
        amount=1
print('amount of elements equal to maximum',amount)


#-----------------------------------------------------------------


#task15------------------------------------------------------------
"""
По данному числу n определите n-е число Фибоначчи φn.

Эту задачу можно решать и циклом for.
"""
#Program prints number of fibonachi sequence
a,b=0,1
n=int(input('Enter number of fibonachi sequence'))
for i in range(1,n+1):
    a,b=b,a+b
print('number of fibonachi sequence',a)

#-----------------------------------------------------------------

#task16------------------------------------------------------------
"""
Дано натуральное число A. 
Определите, каким по счету числом Фибоначчи оно является, то есть выведите такое число n, что φn = A.
Если А не является числом Фибоначчи, выведите число -1.
"""
#Program prints index of number of fibonachi sequence
a=0
b=1
c=0
n=0
A=int(input('Enter number of fibonachi sequence'))
while a<A:
    c=b
    b=a+b
    a=c
    n+=1
if a==A:
    print('index of number of fibonachi sequence',n)
 +else:
    print('Entered number is not a number of fibonachi sequence')

#-----------------------------------------------------------------


#task17------------------------------------------------------------
"""
Дана последовательность натуральных чисел, завершающаяся числом 0. Определите, какое наибольшее число подряд идущих элементов этой последовательности равны друг другу.

"""
#Program prints the maximum number of consecutive equal elements
amount=1
max=1
a=int(input('Enter number in sequence'))
while a!=0:
    b=a
    a=int(input('Enter number in sequence'))
    if b==a:
        amount+=1
    elif amount>max:
        max=amount
        amount=1
    else:
        amount=1
print('the maximum number of consecutive equal elements',max)


#-----------------------------------------------------------------


#task18------------------------------------------------------------
"""
Определите стандартное отклонение для данной последовательности натуральных чисел, завершающейся числом 0.
"""
#Program calculates standard deviation of sequence
import math
a=int(input('Enter number in sequence'))
amount=1
sum=a
res=0
square_sum=a*a
while a!=0:
    a=int(input('Enter number in sequence'))
    amount+=1
    sum+=a
    square_sum+=a*a
amount+=-1
s=sum/amount
res=math.sqrt((square_sum-2*s*sum+amount*s*s)/(amount-1))
print('standard deviation of sequence',res)


#-----------------------------------------------------------------
 