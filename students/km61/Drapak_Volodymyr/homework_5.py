#task1------------------------------------------------------------
"""
Дані чотири дійсних числа: x1, y1, x2, y2.
 Напишіть функцію distance(x1, y1, x2, y2), яка обчислює відстань між точками (x1,y1) и (x2,y2).
 Зчитайте чотири дійсних числа і виведіть результат роботи цієї функції.
"""



#write your answer here...
"""
# Program outputs the distance between two points
# x1, y1, x2, y2 - respectively x- and y-coordinates of two points (real)
# Result is distance between two points (real)

# import
from math import sqrt

# functions
def distance(x1, y1, x2, y2):
    return(sqrt((x2 - x1)*(x2 - x1) + (y2 - y1)*(y2 - y1)))

# input
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

# body
print(distance(x1, y1, x2, y2))
"""

#-----------------------------------------------------------------


#task2------------------------------------------------------------
"""
Дано дійсне додатнє число a і ціле число n.

Обчисліть a^n. Розвязок оформіть в вигляді функції power(a, n).

Стандартною функцією піднесення до степеня користуватись не можна.
"""



#write your answer here...
"""
# Program outputs power of number
# a - real number, n - integer exponent
# Result is a^n (real)

# functions
def power(a, n):
    if(n == 0):
        return 1
    elif(n < 0):
        return 1/a*power(a, n + 1)
    else:
        return a*power(a, n - 1)

# input
a = float(input())
n = int(input())

# body
print(power(a, n))
"""

#-----------------------------------------------------------------


#task3------------------------------------------------------------
"""
Дано дійсне число a і ціле невід'ємне число n.
 Обчисліть a^n, не використовуючи цикли оператор піднесення до степеня ** та функцію math.pow(),
 а використовуючи рекуррентне співвідношення a^n=a⋅a^(n-1).

Розвязок оформіть в вигляді функції power(a, n).
"""



#write your answer here...
"""
# Program outputs power of number
# a - real number, n - integer exponent
# Result is a^n (real)

# functions
def power(a, n):
    if(n == 0):
        return 1
    return a*power(a, n - 1)

# input
a = float(input())
n = int(input())

# body
print(power(a, n))
"""

#-----------------------------------------------------------------


#task4------------------------------------------------------------
"""
Напишіть функцію fib(n), яка по даному цілому невід'ємному n повертає n-e число Фібоначчі.
В цій задачі не можна використовувати цикли.
"""



#write your answer here...
"""
# Program outputs n-th Fibonacci number
# n - natural number
# Result is n-th Fibonacci number (natural)

# functions
def fib(n):
    if(n < 2):
        return n
    else:
        return fib(n - 1) + fib(n - 2)

# input
n = int(input())

# body
print(fib(n))
"""

#-----------------------------------------------------------------