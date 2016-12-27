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

Maximum_Number = 0
array = []
Count = 0
while True:
    Number = int(input())
    if Number == 0:
        break
    array.append(Number)
    if Maximum_Number < Number:
        Maximum_Number = Number
for i in array:
    if i == Maximum_Number:
        Count += 1
print(Count)

#----------------------------------------------------------#

#Task_15---------------------------------------------------#

"""
    Условие:
    Последовательность Фибоначчи определяется так:
    φ0 = 0,  φ1 = 1,  φn = φn−1 + φn−2.

    По данному числу n определите n-е число Фибоначчи φn.

    Эту задачу можно решать и циклом for.
"""

Number = int(input())
Zero_Fibonachi = 0 #F0 = 0
First_Fibonachi = 1 #F1 = 1
Sum_Fibonachi = 0 # Fibonachi sum
Count = 0 #Cycle parametr

if Number == 0:
    print(Zero_Fibonachi)
elif Number == 1:
    print(First_Fibonachi)
else:
    while Count < Number - 1:
        Sum_Fibonachi = First_Fibonachi + Zero_Fibonachi # Fn+2 = Fn+1 + Fn
        Zero_Fibonachi = First_Fibonachi # Fn => Fn+1
        First_Fibonachi = Sum_Fibonachi # Fn+1 => Fn+2
        # Fn+3 = Fn+2 + Fn+1
        Count += 1
    print(Sum_Fibonachi)

#----------------------------------------------------------#

#Task_16---------------------------------------------------#

"""
    Условие:
    Дано натуральное число A. Определите, каким по счету числом Фибоначчи оно является, то есть выведите такое число n, что φn = A.
    Если А не является числом Фибоначчи, выведите число -1.   
"""

Number = int(input())
Zero_Fibonachi = 0 #F0 = 0
First_Fibonachi = 1 #F1 = 1
Result_Fibonachi = -1
Sum_Fibonachi = 0 # Fibonachi sum
Count = 0 #Cycle parametr

while Sum_Fibonachi <= Number - 1:
        Sum_Fibonachi = First_Fibonachi + Zero_Fibonachi # Fn+2 = Fn+1 + Fn
        Zero_Fibonachi = First_Fibonachi # Fn => Fn+1
        First_Fibonachi = Sum_Fibonachi # Fn+1 => Fn+2
        # Fn+3 = Fn+2 + Fn+1
        Count += 1
if Number == Sum_Fibonachi:
    Result_Fibonachi = Count + 1
print(Result_Fibonachi)

#----------------------------------------------------------#

#Task_17---------------------------------------------------#

"""
    Условие:
    Дана последовательность натуральных чисел, завершающаяся числом 0.
    Определите, какое наибольшее число подряд идущих элементов этой последовательности равны друг другу. 
"""

Count = 1 #Numbers count
TemplateNumber = 0 #Comparing number
PreviousNumber = 0 #Previous number

while True:
    Number = int(input()) #"Enter number (enter 0 to stop): "
    if Number == 0:
        break #not count +1
    if PreviousNumber == Number:
        Count+=1
    else:
        if Count>TemplateNumber:
            TemplateNumber = Count
            Count = 1
    PreviousNumber = Number
if TemplateNumber > Count:
    print(TemplateNumber)
elif TemplateNumber <= Count:
    print(Count)

#----------------------------------------------------------#

#Task_18---------------------------------------------------#

"""
    Дана последовательность натуральных чисел x1x1, x2x2, ..., xnxn. Стандартным отклонением называется величина
    σ=(x1−s)2+(x2−s)2+…+(xn−s)2n−1−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−√
    σ=(x1−s)2+(x2−s)2+…+(xn−s)2n−1
    где s=x1+x2+…+xnns=x1+x2+…+xnn — среднее арифметическое последовательности.

    Определите стандартное отклонение для данной последовательности натуральных чисел, завершающейся числом 0.


"""

Number_N = 0
Number_S = 0
Array = []
Sum = 0
while True:
    Number = int(input())
    if Number == 0: break
    Array = Number
    Number_S += Number
    Number_N += 1
Number_S = Number_S/Number_N

for i in range(Array):
    Sum += (Array - Number_S) ** 2 

Delta = (Sum/(Number_N-1)) ** (1/2)
print(Delta)

#----------------------------------------------------------#
