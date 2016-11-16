# -*- coding: utf-8 -*-

"""
    Домашня робота №4
    Тема: "Цикл while"
    Студент: Козирєв Антон Юрійович
    Група: КМ - 62
"""

#Task_1----------------------------------------------------#

"""
    Условие:
    По данному целому числу N распечатайте все квадраты натуральных чисел, не превосходящие N, в порядке возрастания.
"""

Default_Number = 1;
Step = 1 #Step counter
Limit = int(input()) #"Enter pow limit: "
if Limit <= Default_Number:
    Limit = Default_Number
while Step ** 2 <= Limit:
    print(Step ** 2)
    Step += 1

#Variant 2

#i = 1 #Step counter
#num = "" #Row of Numbers
#N = int(input())
#while i ** 2 <= N:
#    num = num + str(i ** 2) + " "
#    i += 1
#print(num)

#----------------------------------------------------------#

#Task_2----------------------------------------------------#

"""
    Условие:
    Дано целое число, не меньшее 2. Выведите его наименьший натуральный делитель, отличный от 1.
"""

Default_Number = 2 #Default value
Number = int(input()) #"Enter devide number: "
if Number <= Default_Number:
    Number = Default_Number
Devider = 2 #Default devider
while Number % Devider != 0:
    Devider += 1
print(Devider)

#----------------------------------------------------------#

#Task_3----------------------------------------------------#

"""
    Условие:
    По данному натуральному числу N найдите наибольшую целую степень двойки, не превосходящую N. Выведите показатель степени и саму степень.
    Операцией возведения в степень пользоваться нельзя!
"""

MaxPow = int(input()) #"Enter maximum pow number:"
CurrentPow = 0 #Current pow number
Number = 1 #Current number
while (Number * 2) <= MaxPow: 
    CurrentPow += 1 #Count of repeat
    Number = Number * 2; 
print(CurrentPow, Number)

#----------------------------------------------------------#

#Task_4----------------------------------------------------#

"""
    Условие:
    В первый день спортсмен пробежал x километров, а затем он каждый день увеличивал пробег на 10% от предыдущего значения.
    По данному числу y определите номер дня, на который пробег спортсмена составит не менее y километров.
"""

Days = 1 # Default days number
First_attempt = int(input()) #"Enter first attempt:"
Final_try = int(input()) #"Enter final try:"
while First_attempt < Final_try:
    First_attempt = First_attempt + 0.1*First_attempt
    Days += 1
print(Days)

#----------------------------------------------------------#

#Task_5----------------------------------------------------#

"""
    Условие:
    Вклад в банке составляет x рублей. Ежегодно он увеличивается на p процентов, после чего дробная часть копеек отбрасывается.
    Определите, через сколько лет вклад составит не менее y рублей.
    Выражение «дробная часть копеек отбрасывается» означает, что если у вас оказалось 123.4567 рублей, т. е. 123 рубля и 45.67 копеек, то после округления у вас получится 123 рубля и 45 копеек, т.е. 123.45 рублей.
    Программа получает на вход три натуральных числа: x, p, y и должна вывести одно целое число.
"""

Years = 0;

Deposit = int(input()); #"Start deposit: "
Interest = int(input()); #"Interest: "
Get = int(input()); #"Get: "

while Deposit < Get:
    Deposit = round(Deposit, 2);
    Deposit = Deposit + 0.01*Interest*Deposit;
    Years += 1;
print(Years);

#----------------------------------------------------------#

#Task_6----------------------------------------------------#

"""
    Условие:
    Программа получает на вход последовательность целых неотрицательных чисел, каждое число записано в отдельной строке.
    Последовательность завершается числом 0, при считывании которого программа должна закончить свою работу и вывести количество членов последовательности (не считая завершающего числа 0).
    Числа, следующие за числом 0, считывать не нужно.
"""


Count = 0 #Numbers count

while True:
    Number = int(input()) #"Enter number (enter 0 to stop): "
    if Number == 0:
        break #not count +1
    Count+=1
print(Count)

#----------------------------------------------------------#

#Task_7----------------------------------------------------#

"""
    Условие:
    Определите сумму всех элементов последовательности, завершающейся числом 0.
    В этой и во всех следующих задачах числа, следующие за первым нулем, учитывать не нужно.
"""

Count = 0 #Numbers count
Sum = 0

while True:
    Number = int(input())
    Sum = Sum + Number;
    if Number == 0:
        break #not count +1
    Count+=1
print(Sum)

#----------------------------------------------------------#

#Task_8----------------------------------------------------#

"""
    Условие:
    Определите среднее значение всех элементов последовательности, завершающейся числом 0.
"""

Count = 0 #Numbers count
Sum = 0

while True:
    Number = int(input())
    Sum = Sum + Number;
    if Number == 0:
        break #not count +1
    Count+=1
print(Sum / Count) # (X1 + X2 + X3 + ... + Xn) / n 

#----------------------------------------------------------#

#Task_9----------------------------------------------------#

"""
    Условие:
    Последовательность состоит из натуральных чисел и завершается числом 0.
    Определите значение наибольшего элемента последовательности.
"""

Count = 0 #Numbers count
Default_value = 0

while True:
    Number = int(input())
    if Number > Default_value:
        Default_value = Number # Set temp var to bigger value
    if Number == 0:
        break #not count +1
    Count+=1
print(Default_value)

#----------------------------------------------------------#

#Task_10---------------------------------------------------#

"""
    Условие:
    Последовательность состоит из натуральных чисел и завершается числом 0.
    Определите индекс наибольшего элемента последовательности.
    Если наибольших элементов несколько, выведите индекс первого из них.
    Нумерация элементов начинается с нуля.
"""

Count = 0 #Numbers count
Index = 0 #Default index
Default_value = 0 #Default value

while True:
    Number = int(input())
    if Number == 0:
        break #not count +1
    if Number > Default_value:
        Default_value = Number # Set temp var to bigger value
        Index = count
    Count+=1
print(Index)

#----------------------------------------------------------#

#Task_11---------------------------------------------------#

"""
    Условие:
    Определите количество четных элементов в последовательности, завершающейся числом 0.
"""

Count = 0 #Numbers count
Mod = 0

while True:
    Number = int(input())
    if Number == 0:
        break #not count +1
    if Number % 2 == 0:
        Mod += 1
    Count+=1
print(Mod)

#----------------------------------------------------------#

#Task_12---------------------------------------------------#

"""
    Условие:
    Последовательность состоит из натуральных чисел и завершается числом 0.
    Определите, сколько элементов этой последовательности больше предыдущего элемента.
"""

Count = 0
Number_previous = 0

Number = int(input())
while True:
    if Number == 0:
        break
    if Number > Number_previous:
        Count += 1
    Number_previous = Number
    Number = int(input())
print(Count)

#----------------------------------------------------------#

#Task_13---------------------------------------------------#

"""
    Условие:
    Последовательность состоит из различных натуральных чисел и завершается числом 0.
    Определите значение второго по величине элемента в этой последовательности
    Гарантируется, что в последовательности есть хотя бы два элемента.
"""

Count = 0 #Numbers count
Default_value = 0 
Second_Maximum = 0; # Second maximum

while True:
    Number = int(input())
    if Second_Maximum <= Number and Second_Maximum <= Default_value:
        Second_Maximum = Default_value
    if Number > Default_value:
        Default_value = Number # Set temp var to bigger value
    if Number == 0:
        break #not count +1
    Count+=1
print(Second_Maximum)

#----------------------------------------------------------#

#Task_14---------------------------------------------------#

"""
    Условие:
    Последовательность состоит из натуральных чисел и завершается числом 0.
    Определите, сколько элементов этой последовательности равны ее наибольшему элементу.
"""

num_M = 0
array = []
count = 0
while True:
    N = int(input())
    if n == 0:
        break
    array.append(n)
    if num_M < n:
        num_M = n
for i in array:
    if i == num_M:
        count += 1
print(count)

#----------------------------------------------------------#

#Task_15---------------------------------------------------#

"""
    Условие:
    Последовательность Фибоначчи определяется так:
    φ0 = 0,  φ1 = 1,  φn = φn−1 + φn−2.

    По данному числу n определите n-е число Фибоначчи φn.

    Эту задачу можно решать и циклом for.
"""

n = int(input())
fib1 = 0 #F0 = 0
fib2 = 1 #F1 = 1
fibS = 0 # Fibonachi sum
Count = 0 #Cycle parametr

if n == 0:
    print(fib1)
elif n == 1:
    print(fib2)
else:
    while Count < n - 1:
        fibS = fib2 + fib1 # Fn+2 = Fn+1 + Fn
        fib1 = fib2 # Fn => Fn+1
        fib2 = fibS # Fn+1 => Fn+2
        # Fn+3 = Fn+2 + Fn+1
        Count += 1
    print(fibS)

#----------------------------------------------------------#

#Task_16---------------------------------------------------#

"""
    Условие:
    Дано натуральное число A. Определите, каким по счету числом Фибоначчи оно является, то есть выведите такое число n, что φn = A.
    Если А не является числом Фибоначчи, выведите число -1.   
"""

n = int(input())
fib1 = 0 #F0 = 0
fib2 = 1 #F1 = 1
fibN = -1
fibS = 0 # Fibonachi sum
Count = 0 #Cycle parametr

while fibS <= n - 1:
        fibS = fib2 + fib1 # Fn+2 = Fn+1 + Fn
        fib1 = fib2 # Fn => Fn+1
        fib2 = fibS # Fn+1 => Fn+2
        # Fn+3 = Fn+2 + Fn+1
        Count += 1
if n == fibS:
    fibN = Count + 1
print(fibN)

#----------------------------------------------------------#

#Task_17---------------------------------------------------#

"""
    Условие:
    Дана последовательность натуральных чисел, завершающаяся числом 0.
    Определите, какое наибольшее число подряд идущих элементов этой последовательности равны друг другу. 
"""

count = 1 #Numbers count
tempNum = 0 #Comparing number
Pnum = 0 #Previous number

while True:
    num = int(input()) #"Enter number (enter 0 to stop): "
    if num == 0:
        break #not count +1
    if Pnum == num:
        count+=1
    else:
        if count>tempNum:
            tempNum = count
            count = 1
    Pnum = num
if tempNum > count:
    print(tempNum)
elif tempNum <= count:
    print(count)

#----------------------------------------------------------#

#Task_18---------------------------------------------------#

"""
    Дана последовательность натуральных чисел x1x1, x2x2, ..., xnxn. Стандартным отклонением называется величина
    σ=(x1−s)2+(x2−s)2+…+(xn−s)2n−1−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−√
    σ=(x1−s)2+(x2−s)2+…+(xn−s)2n−1
    где s=x1+x2+…+xnns=x1+x2+…+xnn — среднее арифметическое последовательности.

    Определите стандартное отклонение для данной последовательности натуральных чисел, завершающейся числом 0.


"""

n = 0
s = 0
Arr = []
Sum = 0
while True:
    x = int(input())
    if x == 0: break
    Arr = x
    s += x
    n += 1
s = s/n

for i in range(Arr):
    Sum += (Arr - s) ** 2 

delta = (Sum/(n-1)) ** (1/2)
print(delta)

#----------------------------------------------------------#
