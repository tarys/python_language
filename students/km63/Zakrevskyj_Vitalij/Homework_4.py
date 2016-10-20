#task1------------------------------------------------


"""
Задача «Список квадратов»
По данному целому числу N распечатайте все квадраты натуральных чисел, не превосходящие N, в порядке возрастания.
"""
#
n=int(input())

i=1

while (i**2)<=n:

    print(i**2)

    i+=1
#-----------------------------------------------------


#task2------------------------------------------------


"""
Задача «Минимальный делитель»
Дано целое число, не меньшее 2. Выведите его наименьший натуральный делитель, отличный от 1.
"""
#
n=int(input())

i=2

while n%i!=0:

    i+=1

print(i)
#-----------------------------------------------------


#task3------------------------------------------------


"""
Задача «Степень двойки»
По данному натуральному числу N найдите наибольшую целую степень двойки, не превосходящую N. Выведите показатель степени и саму степень.

Операцией возведения в степень пользоваться нельзя!
"""
#
n = int (input ())

k=2

m=1

while k<=n:
 
    k*=2

    m+=1

print(m-1,k//2)
#-----------------------------------------------------


#task4------------------------------------------------


"""
Задача «Утренняя пробежка»
В первый день спортсмен пробежал x километров, а затем он каждый день увеличивал пробег на 10% от предыдущего значения. По данному числу y определите номер дня, на который пробег спортсмена составит не менее y километров.

Программа получает на вход действительные числа x и y и должна вывести одно натуральное число.
"""
#
x=int(input())

y=int(input())

day=1

while x<y:

    x+=x*0.1

    day+=1

print(day)
#-----------------------------------------------------


#task5------------------------------------------------


"""
Задача «Банковские проценты»
Вклад в банке составляет x рублей. Ежегодно он увеличивается на p процентов, после чего дробная часть копеек отбрасывается. Определите, через сколько лет вклад составит не менее y рублей.

Выражение «дробная часть копеек отбрасывается» означает, что если у вас оказалось 123.4567 рублей, т. е. 123 рубля и 45.67 копеек, то после округления у вас получится 123 рубля и 45 копеек, т.е. 123.45 рублей.

Программа получает на вход три натуральных числа: x, p, y и должна вывести одно целое число.
"""
#
x = float(input())
p = float(input())
y = float(input())
i = 0
while x < y:
    x += x * p*0.01
    x = int(x*100)/100
    i += 1
print(i)
#-----------------------------------------------------


#task6------------------------------------------------


"""
Задача «Длина последовательности»
Программа получает на вход последовательность целых неотрицательных чисел, каждое число записано в отдельной строке. Последовательность завершается числом 0, при считывании которого программа должна закончить свою работу и вывести количество членов последовательности (не считая завершающего числа 0). Числа, следующие за числом 0, считывать не нужно.
"""
#
i=0

while True:

    n=int(input())

    if n==0:

        break

    i+=1

print(i)
#-----------------------------------------------------


#task7------------------------------------------------


"""
Задача «Сумма последовательности»
Определите сумму всех элементов последовательности, завершающейся числом 0. В этой и во всех следующих задачах числа, следующие за первым нулем, учитывать не нужно.
"""
#
sum=0
while True:
    n=int(input())
    if n==0:
        n+=n
        break
    sum+=n
print(sum)
#-----------------------------------------------------


#task8------------------------------------------------


"""
Задача «Среднее значение последовательности»
Определите среднее значение всех элементов последовательности, завершающейся числом 0.
"""
#
i=0
sum=0
while True:
    n = int(input())
    if n==0:
        n+=n
        break
    sum+=n
    i+=1
    s=sum/i
print(s)
#-----------------------------------------------------


#task9------------------------------------------------


"""
Задача «Максимум последовательности»
Последовательность состоит из натуральных чисел и завершается числом 0. Определите значение наибольшего элемента последовательности.
"""
#
i = 0
max = 0
while True:
    n = int(input())
    if n == 0:
        break
    if max<n:
        max=n
print(max)
#-----------------------------------------------------


#task10------------------------------------------------


"""
number = 1
max = 0
i = 0
index = 0
 
while number != 0:
    number = int(input())
    if number > max:
        max = number
        index = i
    i += 1
print(index)
"""
#
#-----------------------------------------------------


#task11------------------------------------------------


"""
Задача «Количество четных элементов последовательности»
Определите количество четных элементов в последовательности, завершающейся числом 0.
"""
#
number = 1
max = 0
count = 0
while number != 0:
    number = int(input())
    if number % 2 == 0 and number != 0:
        count += 1
print(count)
#-----------------------------------------------------


#task12------------------------------------------------


"""
Задача «Количество элементов, которые больше предыдущего»
Последовательность состоит из натуральных чисел и завершается числом 0. Определите, сколько элементов этой последовательности больше предыдущего элемента.
"""
#
n=0

n1=1

count=0

while n1!=0:

    n1=int(input())

    if n1>n:

        if n!=0:

            count+=1

    n=n1

print(count)
#-----------------------------------------------------


#task13------------------------------------------------


"""
Задача «Второй максимум»
Последовательность состоит из различных натуральных чисел и завершается числом 0. Определите значение второго по величине элемента в этой последовательности. Гарантируется, что в последовательности есть хотя бы два элемента.
"""
#
n=1

n1=0

n2=0

while n!=0:

    n=int(input())

    if n>n1:

        n2=n1

        n1=n

    elif n>n2:

        n2=n

print(n2)
    
#-----------------------------------------------------


#task14------------------------------------------------


"""
Задача «Количество элементов, равных максимуму»
Последовательность состоит из натуральных чисел и завершается числом 0. Определите, сколько элементов этой последовательности равны ее наибольшему элементу.
"""
#
n=1

max=0

count=1

while n!=0:

    n=int(input())

    if n>max:

        count=1

        max=n

    elif n==max:

        count+=1

print(count)
#-----------------------------------------------------


#task15------------------------------------------------


"""
Последовательность Фибоначчи определяется так:
?0 = 0,  ?1 = 1,  ?n = ?n?1 + ?n?2.

По данному числу n определите n-е число Фибоначчи ?n.

Эту задачу можно решать и циклом for
"""
#
i=0

n=0

n1=1

n2=0

count=int(input())-1

for i in range(0,count):

    n=n1+n2

    n2=n1

    n1=n

    if count==0:

        n=1

print(n)
#-----------------------------------------------------


#task16------------------------------------------------


"""
Задача «Номер числа Фибоначчи»
Дано натуральное число A. Определите, каким по счету числом Фибоначчи оно является, то есть выведите такое число n, что ?n = A. Если А не является числом Фибоначчи, выведите число -1.
"""
#
a=int(input())

i=0

n2,n1=0,1

while True:

    if n1>a:

        i=-1

        break

    elif n1==a:

        i+=1

        break

    n2,n1=n1,n2+n1

    i+=1

print(i)
#-----------------------------------------------------


#task17------------------------------------------------


"""
Задача «Максимальное число идущих подряд равных элементов»
Дана последовательность натуральных чисел, завершающаяся числом 0. Определите, какое наибольшее число подряд идущих элементов этой последовательности равны друг другу.
"""
#
n=1

i=1

previous_i=0

previous=0

while True:

    n=int(input())

    if n==0:

        break

    if n==previous:

        i+=1

    else:

        i=1

    if i>previous_i:

        previous_i=i

    previous=n

print(previous_i)
#-----------------------------------------------------


#task18------------------------------------------------


"""
Дана последовательность натуральных чисел x1x1, x2x2, ..., xnxn. Стандартным отклонением называется величина
?=(x1?s)2+(x2?s)2+…+(xn?s)2n?1???????????????????????????????v
?=(x1?s)2+(x2?s)2+…+(xn?s)2n?1
где s=x1+x2+…+xnns=x1+x2+…+xnn — среднее арифметическое последовательности.

Определите стандартное отклонение для данной последовательности натуральных чисел, завершающейся числом 0.
"""
#

#-----------------------------------------------------

