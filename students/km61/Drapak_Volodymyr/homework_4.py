#task1------------------------------------------------------------
"""
По данному целому числу N распечатайте все квадраты натуральных чисел, не превосходящие N, в порядке возрастания.
"""



#write your answer here...
"""
# Program outputs squares of natural numbers where squares are no more than N
# N - integer
# Result is string of said squares

# default
i = 1

# input
N = int(input())

# body
while i*i <= N:
    print(i*i, end = ' ')
    i += 1
"""

#-----------------------------------------------------------------


#task2------------------------------------------------------------
"""
Дано целое число, не меньшее 2. Выведите его наименьший натуральный делитель, отличный от 1.
"""



#write your answer here...
"""
# Program outputs the least divisor of number
# N - integer, more than 1
# Result is the least divisor of N

# default
i = 2

# input
N = int(input())

# body
while N%i != 0:
    i += 1
print(i)
"""

#-----------------------------------------------------------------


#task3------------------------------------------------------------
"""
По данному натуральному числу N найдите наибольшую целую степень двойки, не превосходящую N.
Выведите показатель степени и саму степень.

Операцией возведения в степень пользоваться нельзя!
"""



#write your answer here...
"""
# Program outputs integer power of 2 that is no more than earlier inputted number
# N - natural
# Result is exponent and power, written recorded through the gap

# default
Res = 1
pow = 0

# input
N = int(input())

# body
while Res <= N:
    Res *= 2
    pow += 1
else:
    Res /= 2
    pow -= 1
print(str(pow) + " " + str(int(Res)))
"""

#-----------------------------------------------------------------


#task4------------------------------------------------------------
"""
В первый день спортсмен пробежал x километров, а затем он каждый день увеличивал пробег на 10% от предыдущего значения.
По данному числу y определите номер дня, на который пробег спортсмена составит не менее y километров.

Программа получает на вход действительные числа x и y и должна вывести одно натуральное число.
"""



#write your answer here...
"""
# Program outputs natural number of days for which the sportsman can run his distance
# x, y - real numbers
# Result is number of days (natural)

# default
ratio = 0.1
N = 1

# input
x = float(input())
y = float(input())

# body
while x < y:
    x = (1 + ratio)*x
    N += 1
print(N)
"""

#-----------------------------------------------------------------


#task5------------------------------------------------------------
"""
Вклад в банке составляет x рублей. Ежегодно он увеличивается на p процентов, после чего дробная часть копеек отбрасывается.
Определите, через сколько лет вклад составит не менее y рублей.

Выражение «дробная часть копеек отбрасывается» означает, что если у вас оказалось 123.4567 рублей,
т. е. 123 рубля и 45.67 копеек, то после округления у вас получится 123 рубля и 45 копеек, т.е. 123.45 рублей.

Программа получает на вход три натуральных числа: x, p, y и должна вывести одно целое число.
"""



#write your answer here...
"""
# Program outputs the number of years for which money in bank will increase from number x to number y
# x, y - real positive numbers
# p - percents (real)
# Result is number of years (natural)

# import
from math import floor

# default
N = 0

# input
x = float(input())
p = float(input())/100
y = float(input())

# body
while x < y:
    x = floor((x + x*p)*100)/100
    N += 1
print(N)
"""

#-----------------------------------------------------------------


#task6------------------------------------------------------------
"""
Программа получает на вход последовательность целых неотрицательных чисел, каждое число записано в отдельной строке.
Последовательность завершается числом 0, при считывании которого программа должна
 закончить свою работу и вывести количество членов последовательности (не считая завершающего числа 0).
 Числа, следующие за числом 0, считывать не нужно.
"""



#write your answer here...
"""
# Program outputs number of elements of some sequence that ends with 0
# N - number of elements (natural)
# Result is number of elements

# default
N = 0

# body
while int(input()) != 0:
    N += 1
print(N)
"""

#-----------------------------------------------------------------


#task7------------------------------------------------------------
"""
Определите сумму всех элементов последовательности, завершающейся числом 0.
 В этой и во всех следующих задачах числа, следующие за первым нулем, учитывать не нужно.
"""



#write your answer here...
"""
# Program outputs the sum of all elements of sequence that ends with 0
# All elements are integers
# Result is integer sum

# default
Sum = 0

# input
a = int(input())

# body
while a != 0:
    Sum += a
    a = int(input())
print(Sum)
"""

#-----------------------------------------------------------------


#task8------------------------------------------------------------
"""
Определите среднее значение всех элементов последовательности, завершающейся числом 0.
"""



#write your answer here...
"""
# Program outputs mean of elements of sequence that ends with 0
# N - number of elements
# Result is mean of elements (real number)

# default
Sum = 0
N = 0

# input
a = int(input())

# body
while a != 0:
    Sum += a
    a = int(input())
    N += 1
print(Sum/N)
"""

#-----------------------------------------------------------------


#task9------------------------------------------------------------
"""
Последовательность состоит из натуральных чисел и завершается числом 0. Определите значение наибольшего элемента последовательности.
"""



#write your answer here...
"""
# Program outputs maximal element of sequence that consists of natural ends with 0
# my_max - maximum (integer)
# Result is maximum of sequence (integer)

# default
my_max = -1

# input
a = int(input())

# body
while a != 0:
    my_max = max(a, my_max)
    a = int(input())
print(my_max)
"""

#-----------------------------------------------------------------


#task10------------------------------------------------------------
"""
Последовательность состоит из натуральных чисел и завершается числом 0. Определите индекс наибольшего элемента последовательности.
Если наибольших элементов несколько, выведите индекс первого из них. Нумерация элементов начинается с нуля.
"""



#write your answer here...
"""
# Program outputs index of maximum of sequence that ends with 0
# a - element (natural)
# i - index of current maximum
# N - number of elements of sequence
# Result is index of maximum (natural)

# default
i = 0
N = 0

# input
a = int(input())

# body
my_max = a
while a != 0:
    N += 1
    a = int(input())
    if(my_max < a):
        my_max = a
        i = N
print(i)
"""

#-----------------------------------------------------------------


#task11------------------------------------------------------------
"""
Определите количество четных элементов в последовательности, завершающейся числом 0.
"""



#write your answer here...
"""
# Program outputs number of even elements of sequence that ends with 0
# N - number of even numbers
# a - element (natural)
# Result is number of even numbers (integer)

# default
N = 0

# input
a = int(input())

# body
while a != 0:
    if(a % 2 == 0):
        N += 1
    a = int(input())
print(N)
"""

#-----------------------------------------------------------------


#task12------------------------------------------------------------
"""
Последовательность состоит из натуральных чисел и завершается числом 0.
Определите, сколько элементов этой последовательности больше предыдущего элемента.
"""



#write your answer here...
"""
# Program outputs number of elements that are more than previous element in sequence that ends with 0
# N - number of said elements (integer)
# a, b - respective previous and next elements
# Result is N

# default
N = 0

# input
a = int(input())
b = int(input())

# body
while b != 0:
    if(b > a):
        N += 1
    a = b
    b = int(input())
print(N)
"""

#-----------------------------------------------------------------


#task13------------------------------------------------------------
"""
Последовательность состоит из различных натуральных чисел и завершается числом 0.
Определите значение второго по величине элемента в этой последовательности.
Гарантируется, что в последовательности есть хотя бы два элемента.
"""



#write your answer here...
"""
# Program outputs the second maximal element in sequence that ends with 0
# max1, max2 - respective first and second maximums of sequence that ends with 0
# a - element (natural)
# Result is max2 (natural)

# default
max1, max2 = -1, -1

# input
a = int(input())

# body
while a != 0:
    if(max1 < a):
        max2 = max1
        max1 = a
    elif(max2 < a):
        max2 = a
    a = int(input())
print(max2)
"""

#-----------------------------------------------------------------


#task14------------------------------------------------------------
"""
Последовательность состоит из натуральных чисел и завершается числом 0.
Определите, сколько элементов этой последовательности равны ее наибольшему элементу.
"""



#write your answer here...
"""
# Program outputs number of elements those are equals to maximum in sequence that ends with 0
# N - number of said elements (integer)
# a - element (natural)
# Result is N

# default
N = 1
max = -1

# input
a = int(input())

# body
while a != 0:
    if(a == max):
        N += 1
    elif(a > max):
        max = a
        N = 1
    a = int(input())
print(N)
"""

#-----------------------------------------------------------------


#task15------------------------------------------------------------
"""
Последовательность Фибоначчи определяется так:
φ0 = 0,  φ1 = 1,  φn = φn−1 + φn−2.

По данному числу n определите n-е число Фибоначчи φn.

Эту задачу можно решать и циклом for.
"""



#write your answer here...
"""
# Program outputs n-th fibonacci number with help of operator FOR
# n - index of fibonacci number
# Result is fibonacci number (integer)

# default
fib_previous, fib_current, fib_next = 0, 1, 0

# input
n = int(input())

# body
for i in range(2, n + 1):
    fib_next = fib_previous + fib_current
    fib_previous = fib_current
    fib_current = fib_next
if(n < 2):
    print(n)
else:
    print(fib_current)
"""

#-----------------------------------------------------------------


#task16------------------------------------------------------------
"""
Дано натуральное число A. Определите, каким по счету числом Фибоначчи оно является, то есть выведите такое число n, что φn = A.
Если А не является числом Фибоначчи, выведите число -1.
"""



#write your answer here...
"""
# Program outputs index of fibonacci number A (if A isn't fibonacci number then program outputs "-1")
# N - index of fibonacci number(or -1) (integer)
# Result is N

# default
fib_previous, fib_current, fib_next = 0, 1, 0
N = 1

# input
A = int(input())

# body
while fib_next < A:
    fib_next = fib_previous + fib_current
    fib_previous = fib_current
    fib_current = fib_next
    N += 1
print(N*(A == fib_next) + -(A != fib_next))
"""

#-----------------------------------------------------------------


#task17------------------------------------------------------------
"""
Дана последовательность натуральных чисел, завершающаяся числом 0.
Определите, какое наибольшее число подряд идущих элементов этой последовательности равны друг другу.
"""



#write your answer here...
"""
# Program outputs maximal number of elements that are equals and consecutive. Elements are sequence that ends with 0
# N - counter of said elements (natural)
# my_max - final number of said elements
# a, b - respective previous and next elements of sequence (natural)

# default
N = 0
my_max = 0

# input
a = int(input())

# body
b = a
while a != 0:
    if(a == b):
        N += 1
        my_max = max(N, my_max)
    else:
        N = 1
    b = a
    a = int(input())
print(my_max)
"""

#-----------------------------------------------------------------


#task18------------------------------------------------------------
"""
Дана последовательность натуральных чисел x1x1, x2x2, ..., xnxn. Стандартным отклонением называется величина
σ=sqrt(((x1−s)^2+(x2−s)^2+…+(xn−s)^2)/(n−1))
где s=(x1+x2+…+xn)/n= — среднее арифметическое последовательности.

Определите стандартное отклонение для данной последовательности натуральных чисел, завершающейся числом 0.
"""



#write your answer here...
"""
# Program outputs standard deviation of sequence that ends with 0
# N - number of elements
# x_sum - sum of elements
# x_square_sum - sum of squares of elements
# mid_arithm - arithmetical mean of sequence
# standard_mist - standard deviation
# a - element

# import
from math import sqrt

# default
N, x_sum, x_square_sum = 0, 0, 0
mid_arithm, standard_mist = 0.0, 0.0

# input
a = int(input())

# body
while a != 0:
    x_sum += a
    x_square_sum += a*a
    N += 1
    a = int(input())
mid_arithm = x_sum/N
standard_mist = sqrt((x_square_sum - 2*x_sum*mid_arithm + N*mid_arithm*mid_arithm)/(N - 1))
print(standard_mist)
"""

#-----------------------------------------------------------------