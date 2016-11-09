#task1------------------------------------------------


"""
Задача «Длина отрезка»
Условие
Даны четыре действительных числа: x1, y1, x2, y2. 
Напишите функцию distance(x1, y1, x2, y2), вычисляющая расстояние между точкой (x1,y1) и (x2,y2). 
Считайте четыре действительных числа и выведите результат работы этой функции.
"""
#
def distance(x1,y1,x2,y2):

    result=0

    result=(((x2-x1)**2)+((y2-y1)**2))**(0.5)

    return result

x1=float(input())

y1=float(input())

x2=float(input())

y2=float(input())

print (distance(x1,y1,x2,y2))
#-----------------------------------------------------


#task2------------------------------------------------


"""
Задача «Отрицательная степень»
Условие
Дано действительное положительное число a и целоe число n.

Вычислите a^n. Решение оформите в виде функции power(a, n).

Стандартной функцией возведения в степень пользоваться нельзя.
"""
#
def power(a,n):

    res=1

    for i in range(abs(n)):

        res*=a

    if n<0:

        return 1/res

    else:

        return res

a=float(input())

n=int(input())

print (power(a,n))
#-----------------------------------------------------


#task3------------------------------------------------


"""
Задача «Возведение в степень»
Условие
Дано действительное положительное число a и целое неотрицательное число n. 
Вычислите a^n не используя циклы, возведение в степень через ** и функцию math.pow(), 
а используя рекуррентное соотношение a^n=a*a^(n-1).

Решение оформите в виде функции power(a, n).
"""
#
def power(a,n):

    if n==0:

        return 1

    else:

        return a*power(a,n-1)

a=float(input())

n=int(input())

print (power(a,n))
#-----------------------------------------------------


#task4------------------------------------------------


"""
Задача «Числа Фибоначчи»
Условие
Напишите функцию fib(n), которая по данному целому неотрицательному n возвращает n-e число Фибоначчи. 
В этой задаче нельзя использовать циклы — используйте рекурсию.
"""
#
def fib(n):

    if n==1 or n==2:

        return 1

    else:

        return fib(n-1)+fib(n-2)

n=int(input())

print (fib(n))
#-----------------------------------------------------
