# task1------------------------------------------------------------
"""
Даны четыре действительных числа: x1, y1, x2, y2.
Напишите функцию distance(x1, y1, x2, y2), вычисляющая расстояние между точкой (x1,y1) и (x2,y2).
Считайте четыре действительных числа и выведите результат работы этой функции.
"""
# Program calculates length of line
import math


def distance(x1, y1, x2, y2):
    result = round(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2), 5)
    return result


x1 = float(input('Enter first dot first coordinate'))
y1 = float(input('Enter first dot second coordinate'))
x2 = float(input('Enter second dot first coordinate'))
y2 = float(input('Enter second dot second coordinate'))
print('Distance between two dots= ', distance(x1, y1, x2, y2))

# -----------------------------------------------------------------

# task2------------------------------------------------------------
"""
Дано действительное положительное число a и целоe число n.
Вычислите a^n. Решение оформите в виде функции power(a, n).
"""


# Program calculates power of number
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


a = float(input('Enter number you want to involve '))
n = int(input('Enter power you want to get'))
print('a^n=', power(a, n))

# -----------------------------------------------------------------

# task3------------------------------------------------------------
"""
Дано действительное положительное число a и целое неотрицательное число n.
Вычислите a^n  используя рекуррентное соотношение an=a⋅an-1.
Решение оформите в виде функции power(a, n).
"""


# Program calculates power of number with recursion
def power(a, n):
    if n == 0:
        return 1
    else:
        return a * power(a, n - 1)


a = float(input('Enter number you want to involve'))
n = int(input('Enter power you want to get'))
print('a^n=', power(a, n))
# -----------------------------------------------------------------

# task4------------------------------------------------------------
"""
Напишите функцию fib(n), которая по данному целому неотрицательному n возвращает n-e число Фибоначчи.
В этой задаче нельзя использовать циклы — используйте рекурсию.
"""


# Program calculates Fibonacci number with recursion
def fib(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return fib(n - 1) + fib(n - 2)


n = int(input('Enter index of Fibonacci number'))
print('Fibonacci number=', fib(n))

# -----------------------------------------------------------------
