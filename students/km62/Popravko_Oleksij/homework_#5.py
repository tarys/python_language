#task1------------------------------------------------------------
"""
Даны четыре действительных числа: x1, y1, x2, y2. Напишите функцию distance(x1, y1, x2, y2), вычисляющая расстояние между точкой (x1,y1) и (x2,y2). Считайте четыре действительных числа и выведите результат работы этой функции.
  
"""



#
x1=float(input())
y1=float(input())
x2=float(input())
y2=float(input())
def distance():
    import math
    res=math.hypot(x2-x1,y2-y1)
    print(res)
distance()
#-----------------------------------------------------------------


#task2------------------------------------------------------------
"""
Дано действительное положительное число a и целоe число n.

Вычислите an. Решение оформите в виде функции power(a, n).

Стандартной функцией возведения в степень пользоваться нельзя. 
"""



#
def power(a,n):
    if n>0:
        c=a
        for i in range(n-1):
            c*=a
        return c
    elif n<0:
        c=1
        for i in range(abs(n)):
            c*=a
        c=1/c
        return c
    else:
        c=1
        return c

a=float(input())
n=int(input())
print(power(a,n))
#-----------------------------------------------------------------


#task3------------------------------------------------------------
"""
Дано действительное положительное число a и целое неотрицательное число n. Вычислите an не используя циклы, возведение в степень через ** и функцию math.pow(), а используя рекуррентное соотношение an=a⋅an-1.

Решение оформите в виде функции power(a, n). 
"""



#
def power(a,n):
    if n==0:
        return 1
    else:
        return a*power(a,n-1)
print(power(float(input()),int(input())))

#-----------------------------------------------------------------

#task4------------------------------------------------------------
"""
Напишите функцию fib(n), которая по данному целому неотрицательному n возвращает n-e число Фибоначчи. В этой задаче нельзя использовать циклы — используйте рекурсию.  
"""



#
def fib(n):
    if n==1 or n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
print(fib(int(input())))
#-----------------------------------------------------------------

