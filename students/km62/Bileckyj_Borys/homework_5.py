#task1------------------------------------------------------------
"""
Даны четыре действительных числа: x1, y1, x2, y2. Напишите функцию distance(x1, y1, x2, y2), вычисляющая расстояние между точкой (x1,y1) и (x2,y2). Считайте четыре действительных числа и выведите результат работы этой функции.
"""

#import_module------------------------
from math import sqrt
#function-----------------------------
def distance(arg_x1,arg_y1,arg_x2,arg_y2):
    return sqrt((arg_x1-arg_x2)**2+(arg_y1-arg_y2)**2)
#input--------------------------------
x1=float(input())
y1=float(input())
x2=float(input())
y2=float(input())
#output-------------------------------
print(float(distance(x1,y1,x2,y2)))

#-----------------------------------------------------------------


#task2------------------------------------------------------------
"""
Дано действительное положительное число a и целоe число n.

Вычислите an. Решение оформите в виде функции power(a, n).

Стандартной функцией возведения в степень пользоваться нельзя.
"""

#function-----------------------------
def power(number, power):
    number_save=number
    if power>0:
        for i in range(power-1):
            number*=number_save
    elif power<0:
        for i in range(abs(power)-1):
            number*=number_save
        number=1/number
    else:
        number=1
    return number
#input--------------------------------
input_number=float(input())
input_power=int(input())
#output-------------------------------
print(power(input_number, input_power))
        
#-----------------------------------------------------------------


#task3------------------------------------------------------------
"""
Дано действительное положительное число a и целое неотрицательное число n. Вычислите an не используя циклы, возведение в степень через ** и функцию math.pow(), а используя рекуррентное соотношение an=a⋅an-1.

Решение оформите в виде функции power(a, n).
"""

#function-----------------------------
def power(number, pow):
    if pow>0:
        return number*power(number, pow-1)
    elif pow<0:
        number=number*power(number, abs(pow)-1)
        number=1/number
        return number
    else:
        number=1
        return number
#input--------------------------------
input_number=float(input())
input_power=int(input())
#output-------------------------------
print(power(input_number, input_power))

#-----------------------------------------------------------------


#task4------------------------------------------------------------
"""
Напишите функцию fib(n), которая по данному целому неотрицательному n возвращает n-e число Фибоначчи. В этой задаче нельзя использовать циклы — используйте рекурсию.
"""

#function-----------------------------
def fib(position_func):
    if position_func==0:
        return 0
    elif position_func==1 or position_func==2:
        return 1
    else:
        return fib(position_func-2) + fib(position_func-1)
#input--------------------------------
position=int(input())
#output-------------------------------
print(fib(position))

#-----------------------------------------------------------------
