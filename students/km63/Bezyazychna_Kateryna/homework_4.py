﻿#task1------------------------------------------------------------
"""
По данному целому числу N распечатайте все квадраты натуральных чисел, не превосходящие N, в порядке возрастания.
"""

#n-integer number
n=int(input())
i=1
while i**2<=n:
    print(i**2)
    i+=1

#-----------------------------------------------------------------


#task2------------------------------------------------------------
"""
Дано целое число, не меньшее 2. Выведите его наименьший натуральный делитель, отличный от 1.
"""

#N-integer number
N=int(input())
i = N
dil = N
while i > 1:
    if N % i == 0:
        dil = i
    i -= 1
print( dil)

#-----------------------------------------------------------------


#task3------------------------------------------------------------
"""
По данному натуральному числу N найдите наибольшую целую степень двойки, не превосходящую N. Выведите показатель степени и саму степень.
Операцией возведения в степень пользоваться нельзя!
"""

i=1
power=0
N=int(input())
while N>=i*2:
    power+=1
    i=2*i
print(power, i)

#-----------------------------------------------------------------


#task4------------------------------------------------------------
"""
В первый день спортсмен пробежал x километров, а затем он каждый день увеличивал пробег на 10% от предыдущего значения. По данному числу y определите номер дня, на который пробег спортсмена составит не менее y километров.
Программа получает на вход действительные числа x и y и должна вывести одно натуральное число.
"""

x = int(input())
y = int(input())
i = 1
while x < y:
    x += x * 0.1
    i += 1
print(i)

#-----------------------------------------------------------------


#task5------------------------------------------------------------
"""
Вклад в банке составляет x рублей. Ежегодно он увеличивается на p процентов, после чего дробная часть копеек отбрасывается. Определите, через сколько лет вклад составит не менее y рублей.
Выражение «дробная часть копеек отбрасывается» означает, что если у вас оказалось 123.4567 рублей, т. е. 123 рубля и 45.67 копеек, то после округления у вас получится 123 рубля и 45 копеек, т.е. 123.45 рублей.
Программа получает на вход три натуральных числа: x, p, y и должна вывести одно целое число.
"""

x = float(input(""))
p = float(input(""))
y = float(input(""))
i=0
while x < y:
    x = x * (1 + p/100)
    i += 1
print(i)

#-----------------------------------------------------------------


#task6------------------------------------------------------------
"""
Программа получает на вход последовательность целых неотрицательных чисел, каждое число записано в отдельной строке. Последовательность завершается числом 0, при считывании которого программа должна закончить свою работу и вывести количество членов последовательности (не считая завершающего числа 0). Числа, следующие за числом 0, считывать не нужно.
"""

i = 0
while int(input())!=0:
    i += 1
print(i)

#-----------------------------------------------------------------


#task7------------------------------------------------------------
"""
Определите сумму всех элементов последовательности, завершающейся числом 0. В этой и во всех следующих задачах числа, следующие за первым нулем, учитывать не нужно.
"""

sum=0
n=1
while n!=0:
    n = int(input(""))
    sum+=n
print(sum)

#-----------------------------------------------------------------


#task8------------------------------------------------------------
"""
Определите среднее значение всех элементов последовательности, завершающейся числом 0.
"""

len = 0
sum = 0
n = int ( input()) 
while n!= 0:
    len += 1
    sum += n
    n = int(input())
print(sum/len )


#-----------------------------------------------------------------


#task9------------------------------------------------------------
"""
Последовательность состоит из натуральных чисел и завершается числом 0. Определите значение наибольшего элемента последовательности.
"""

n = 1
max = 0 
while n!= 0:
    n= int(input())
    if n > max:
        max = n
    else:
        max = max
print(max)


#-----------------------------------------------------------------


#task10------------------------------------------------------------
"""
Последовательность состоит из натуральных чисел и завершается числом 0. Определите индекс наибольшего элемента последовательности. Если наибольших элементов несколько, выведите индекс первого из них. Нумерация элементов начинается с нуля.
"""

max = 0
max_ind = -1
n = -1
len = 0
while n!= 0:
    n= int(input())
    if n > max:
        max = n
        max_ind = len
    len += 1
print(max_ind)

#-----------------------------------------------------------------


#task11------------------------------------------------------------
"""
Определите количество четных элементов в последовательности, завершающейся числом 0.
"""

num = -1
n = -1
while n!= 0:
    n = int(input())
    if n % 2 == 0:
        num += 1
print(num)

#-----------------------------------------------------------------


#task12------------------------------------------------------------
"""
Последовательность состоит из натуральных чисел и завершается числом 0. Определите, сколько элементов этой последовательности больше предыдущего элемента.
"""

prev = int(input())
n = 0
while prev != 0:
    next = int(input())
    if next != 0 and prev < next:
        n += 1
    prev = next
print(n)


#-----------------------------------------------------------------


#task13------------------------------------------------------------
"""
Последовательность состоит из различных натуральных чисел и завершается числом 0. Определите значение второго по величине элемента в этой последовательности. Гарантируется, что в последовательности есть хотя бы два элемента.
"""

n=int(input())
max=n
second_max=0
while n!=0:
    n=int(input())
    if n>max:
        second_max=max
        max=n
    elif n>second_max and n<max:
        second_max=n
print(second_max)

#-----------------------------------------------------------------


#task14------------------------------------------------------------
"""
Последовательность состоит из натуральных чисел и завершается числом 0. Определите, сколько элементов этой последовательности равны ее наибольшему элементу.
"""

n=int(input())
num=1
max=n
while n!=0:
    n=int(input())
    if n==max:
        num+=1
    if n>max:
        max=n
        num=1
print(num)

#-----------------------------------------------------------------


#task15------------------------------------------------------------
"""
Последовательность Фибоначчи определяется так:
φ0 = 0,  φ1 = 1,  φn = φn−1 + φn−2.
По данному числу n определите n-е число Фибоначчи φn.

Эту задачу можно решать и циклом for.
"""

n = int(input())
if n == 0:
    print(0)
else:
    x=0
    y=1
    for i in range(2, n + 1):
        x,y=y,x + y
    print(y)

#-----------------------------------------------------------------


#task16------------------------------------------------------------
"""
Дано натуральное число A. Определите, каким по счету числом Фибоначчи оно является, то есть выведите такое число n, что φn = A. Если А не является числом Фибоначчи, выведите число -1.
"""

a = int(input())
if a == 0:
    print(0)
else:
    n1, n2 = 0, 1 
    i=1
    while n2<=a:
        if n2==a:
            print(i)
            break
        n1, n2 = n2, n1 + n2
        i += 1
    else:
        print(-1)

#-----------------------------------------------------------------


#task17------------------------------------------------------------
"""
Дана последовательность натуральных чисел, завершающаяся числом 0. Определите, какое наибольшее число подряд идущих элементов этой последовательности равны друг другу.
"""

amount=1
max=1
a=int(input())
while a!=0:
    b=a
    a=int(input())
    if b==a:
        amount+=1
    elif amount>max:
        max=amount
        amount=1
    else:
        amount=1
print(max)

#-----------------------------------------------------------------


#task18------------------------------------------------------------
"""
Дана последовательность натуральных чисел x1x1, x2x2, ..., xnxn. Стандартным отклонением называется величина
σ=(x1−s)2+(x2−s)2+…+(xn−s)2n−1−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−√
σ=(x1−s)2+(x2−s)2+…+(xn−s)2n−1
где s=x1+x2+…+xnns=x1+x2+…+xnn — среднее арифметическое последовательности.

Определите стандартное отклонение для данной последовательности натуральных чисел, завершающейся числом 0.
"""

import math
a=int(input())
amount=1
sum=a
res=0
square_sum=a*a
while a!=0:
    a=int(input())
    amount+=1
    sum+=a
    square_sum+=a*a
amount+=-1
s=sum/amount
res=math.sqrt((square_sum-2*s*sum+amount*s*s)/(amount-1))
print(res)

#-----------------------------------------------------------------
