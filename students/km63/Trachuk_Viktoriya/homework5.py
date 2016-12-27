# task1--------------------------------------------
"""
Given four real numbers: x1, y1, x2, y2. Write a function distance (x1, y1, x2, y2), calculates the distance between the point (x1, y1) and (x2, y2).
"""
import math


def distance(x1, x2, y1, y2):
    result = 0
    result = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2))
    return result


x1 = float(input())
x2 = float(input())
y1 = float(input())
y2 = float(input())
res = distance(x1, x2, y1, y2)
print(res)
# -------------------------------------------------
# task2--------------------------------------------
"""
Given a positive real number and a whole number n. Calculate an. The solution presented in the form function power (a, n).
"""


def power(a, n):
    if n == 1:
        result = a
    else:
        k = 2
        while k <= n:
            result *= a
            k += 1
    return result


a = float(input())
n = int(input())
res = power(a, n)
print(res)
# -------------------------------------------------

# task3--------------------------------------------
"""
Given a positive real number and a non-negative number n.
Calculate an without using loops, powers and function through ** math.pow (), and using the recurrence relation an = a?an-1.
"""


def power(a, n):
    if n == 0:

        return 1

    else:

        return a * power(a, n - 1)


a = float(input())

n = int(input())

res = power(a, n)
print(res)
# ---------------------------------------------------

# task4----------------------------------------------
"""
Write a function fib (n), which is on the non-negative integer n returns n-e Fibonacci number.
In this task, you can not use loops - use recursion.
"""


def fib(n):
    if n == 1 or n == 2:

        return 1
    else:

        return fib(n - 1) + fib(n - 2)


n = int(input())
res = fib(n)

print(res)
# -----------------------------------------------------
