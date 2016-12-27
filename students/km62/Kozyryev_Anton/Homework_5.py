# -*- coding: utf-8 -*-

"""
    Домашня робота №5
    Тема: "funсtion"
    Студент: Козирєв Антон Юрійович
    Група: КМ - 62
"""

#Imports module
import math

#Task_1----------------------------------------------------#

"""
    Условие:
    Даны четыре действительных числа: x1, y1, x2, y2.
    Напишите функцию distance(x1, y1, x2, y2), вычисляющая расстояние между точкой (x1,y1) и (x2,y2).
    Считайте четыре действительных числа и выведите результат работы этой функции.
"""

#Function
def distance(x1, y1, x2, y2):
    result = math.sqrt((x2 - x1)**2 + (y2 - y1)**2) # d = \/x^2 + y^2 
    return result
###

abscissa1 = float(input()) #"Enter x1" 
ordinate1 = float(input()) #"Enter y1" 
abscissa2 = float(input()) #"Enter x2" 
ordinate2 = float(input()) #"Enter y2" 

Distance_result = distance(abscissa1, ordinate1, abscissa2, ordinate2)
print(Distance_result)

#----------------------------------------------------------#

#Task_2----------------------------------------------------#

"""
    Условие:
    Дано действительное положительное число a и целоe число n.
    Вычислите an. Решение оформите в виде функции power(a, n).
    !Стандартной функцией возведения в степень пользоваться нельзя.!
"""

#Function
def power(a, n):
    if n == 0:
        result = 1 #a^0 = 1; a = R
    elif n > 0:
        Power = 1 #Initialization
        for i in range(n):
            Power*=a
        result = Power
    elif n < 0:
        Power = 1
        n = -n # -(-n) => n
        for i in range(n):
            Power*=a
        result = 1/Power #a^-n = 1/a^n
    return result
###

Exponent = float(input()) #"Enter exp"
Pow = int(input()) #"Enter pow"

Result = power(Exponent, Pow)
print(Result)

#----------------------------------------------------------#

#Task_3----------------------------------------------------#

"""
    Условие:
    Дано действительное положительное число a и целое неотрицательное число n.
    Вычислите an не используя циклы, возведение в степень через ** и функцию math.pow(), а используя рекуррентное соотношение an=a⋅an-1.
    Решение оформите в виде функции power(a, n).
"""

#Function
def Power(a, n, Pow = 1):
    if n != 0:
        return a * Power(a, n - 1)
    else:
        return 1
###
    
Exponent = float(input()) #"Enter exp"
Pow = int(input()) #"Enter pow (n>=0)"

Result = Power(Exponent, Pow)
print(Result)

#----------------------------------------------------------#

#Task_4----------------------------------------------------#

"""
    Условие:
    Напишите функцию fib(n), которая по данному целому неотрицательному n возвращает n-e число Фибоначчи.
    В этой задаче нельзя использовать циклы — используйте рекурсию.
"""

def fib(n):
    if n >= 2:
        return fib(n - 1) + fib(n - 2)
    elif n == 1:
        return 1
    elif n == 0:
        return 0
    
Number = int(input()) #"Enter parametr (n >= 2, n = Z)"

Result = fib(Number)
print(Result)

#----------------------------------------------------------#
