#task1
"""
Условие
Даны четыре действительных числа: x1, y1, x2, y2. Напишите функцию distance(x1, y1, x2, y2), 
вычисляющая расстояние между точкой (x1,y1) и (x2,y2). Считайте четыре действительных числа и выведите результат работы этой функции.
Если вы не знаете, как решить эту задачу, то вы, возможно, не изучали в школе теорему Пифагора. Попробуйте прочитать о ней на Википедии.
"""
#Длина отрезка#
import math 
def distance(x1, y1, x2, y2): 
    result = round(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2), 5) 
    return result 
x1 = float(input())
y1 = float(input()) 
x2 = float(input()) 
y2 = float(input()) 
print(distance(x1, y1, x2, y2))

#task2
"""
Условие
Дано действительное положительное число a и целоe число n.

Вычислите an. Решение оформите в виде функции power(a, n).

Стандартной функцией возведения в степень пользоваться нельзя.
"""
#Отрицательная степень#
def power(a, n): 
    original_number = a 
    if n < 0: 
        for i in range(1, n, -1): 
            a /= original_number 
    elif n > 0: 
        for i in range(1, n): 
            a *= original_number 
    else: 
        a = 1 
    return a 
a = float(input()) 
n = int(input()) 
print(power(a, n))

#task3
"""
Условие
Дано действительное положительное число a и целое неотрицательное число n. 
Вычислите an не используя циклы, возведение в степень через ** и функцию math.pow(), 
а используя рекуррентное соотношение an=a⋅an-1.

Решение оформите в виде функции power(a, n).
"""
#Возведение в степень#
def power(a, n): 
    if n == 0: 
        return 1 
    else: 
        return a * power(a, n - 1) 
a = float(input()) 
n = float(input()) 
print(power(a, n))

#task4
"""
Условие
Напишите функцию fib(n), которая по данному целому неотрицательному n возвращает n-e число Фибоначчи. 
В этой задаче нельзя использовать циклы — используйте рекурсию.
"""
#Числа Фибоначчи#
def fib(n): 
    if n == 1: 
        return 1 
    elif n == 0: 
        return 0 
    else: 
        return fib(n - 1) + fib(n - 2) 
n = int(input()) 
print(fib(n))