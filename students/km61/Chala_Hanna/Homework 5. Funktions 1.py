'''
Задача 1 «Длина отрезка»
Условие
Даны четыре действительных числа: x1, y1, x2, y2. Напишите функцию distance(x1, y1, x2, y2), 
вычисляющая расстояние между точкой (x1,y1) и (x2,y2). 
Считайте четыре действительных числа и выведите результат работы этой функции.
Если вы не знаете, как решить эту задачу, то вы, возможно, не изучали в школе теорему Пифагора. 
Попробуйте прочитать о ней на Википедии.
'''
# identifying function (name)
def distance (x1,y1,x2,y2):
# performing function (formula of counting the distance between 2 points)
    dist=((x2-x1)**2+(y2-y1)**2)**0.5
#printing the distance
    print (dist)
# identifying the variables
x1=float(input())
y1=float(input())
x2=float(input())
y2=float(input())
# function call
distance (x1,y1,x2,y2)

'''
Задача 2 «Отрицательная степень»
Условие
Дано действительное положительное число a и целоe число n.

Вычислите an. Решение оформите в виде функции power(a, n).

Стандартной функцией возведения в степень пользоваться нельзя.
'''
# identifying function (name)
def power (a,n):
# performing function (erasing a into the power n)
    p=a**n
#printing the result
    print (p)
# identifying the variables
a=float(input())
n=int(input())
# function call
power (a,n)

'''
Задача 3 «Возведение в степень»
Условие
Дано действительное положительное число a и целое неотрицательное число n. Вычислите an не используя циклы, возведение в степень через ** и функцию math.pow(), а используя рекуррентное соотношение an=a⋅an-1.

Решение оформите в виде функции power(a, n).
'''
# identifying the variables
a= float(input())
n=int(input())
# identifying function (name)
def power(a,n):
# the initial value (the result, when the power is zero)
    if n == 0:
        return 1
# When the power is more than zero, a is multiplyed by the value of the function
    elif n>0: return a*power(a,n-1)
# When the power is less than zero, a is multiplyed by another value of the function
    else: return 1/a*power(a,n+1)
# function call
#printing the result
print (power(a,n))

'''
Задача 4 «Числа Фибоначчи»
Условие
Напишите функцию fib(n), которая по данному целому неотрицательному n возвращает n-e число Фибоначчи. 
В этой задаче нельзя использовать циклы — используйте рекурсию.
'''
# identifying the variables
n=int(input())
# identifying function (name)
def fib(n):
# The result if n=0
    if (n==0):
        return 0
# The result if n=1
    elif (n==1):
        return 1
# Formula to count a Fibonacci number (n>1)
    elif (n>1):
        return fib(n-2) + fib(n-1)
# function call
#printing the result
print (fib(n))
