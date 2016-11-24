#task1-------------------------------------------------------------------------
''' Даны четыре действительных числа: x1, y1, x2, y2.
Напишите функцию distance(x1, y1, x2, y2),
вычисляющая расстояние между точкой (x1,y1) и (x2,y2).
Считайте четыре действительных числа и выведите результат работы этой функции.'''

import math

#input
print("Task 1: Нахождение длины отрезка по заданым координатам")
x1 = float(input("Enter real number x1: "))
y1 = float(input("Enter real number y1: "))
x2 = float(input("Enret real number x2: "))
y2 = float(input("Enter real number y2: "))


#main
def distance(x1, y1, x2, y2):
    x = abs (x2 - x1)
    y = abs (y2 - y1)
    res = math.sqrt (x ** 2 + y ** 2)
    return res
length = distance(x1, y1, x2, y2)         #float

#output
print ("The length =", length)
print("")
#-------------------------------------------------------------------------------------


#task2--------------------------------------------------------------------
''' Дано действительное положительное число a и целоe число n.
Вычислите a^n. Решение оформите в виде функции power(a, n).
Стандартной функцией возведения в степень пользоваться нельзя. '''

#input
print("Task 2: Возведение числа а в степень n")
a = float (input("Enter the real positive number a:"))
n = int(input("Enter the integer numder n: "))

#main
def power (a, n):
    res = 1
    for i in range(abs(n)):
        res *= a
    if n >= 0:
        return res
    else:
        return 1/res
power = power(a, n)               #float

#output
print(a,"^", n, "=", power)
print("")
#----------------------------------------------------------------------------

#task3-----------------------------------------------------------------------
'''Дано действительное положительное число a и целое неотрицательное
число n. Вычислите an не используя циклы, возведение в степень через **
и функцию math.pow(), а используя рекуррентное соотношение an=a⋅an-1.
Решение оформите в виде функции power(a, n)'''

#input
print("Task 3: Возвидение числа а в степень n")
a = float(input("Enter the positive real number a: "))
n = int(input("Enter the positive integer number n: "))

#main
def power (a, n):
    if n == 0:
        return 1
    else:
        return a * power(a, n-1)
power = power(a, n)

#output     #real
print(a,"^", n, "=",power)   
print("")
#----------------------------------------------------------------------------

#task4--------------------------------------------------------------------
'''Напишите функцию fib(n), которая по данному целому неотрицательному n
возвращает n-e число Фибоначчи.
В этой задаче нельзя использовать циклы— используйте рекурсию.'''

#input
print("Task 4: Нахождение n-ого числа Фибоначчи по заданому числу ")
n = int(input("Enter the positive real number n: "))

#main
def fib(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fib(n - 2) + fib(n - 1)
fibonacci = fib(n)

#output
print(n,"-ое число Фибоначчи =", fibonacci)
print("")
#----------------------------------------------------------------------------




    
