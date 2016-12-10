#task1------------------------------------------------------------
"""
Даны четыре действительных числа: x1, y1, x2, y2. Напишите функцию distance(x1, y1, x2, y2), вычисляющая расстояние между точкой (x1,y1) и (x2,y2). Считайте четыре действительных числа и выведите результат работы этой функции.

"""
#
from math import sqrt

def distance(x1, y1, x2, y2):

	dis=sqrt((x2-x1)**2+(y2-y1)**2)

	print("distance",round(dis,3))
x1=float(input("Enter number:"))

y1=float(input("Enter number:"))

x2=float(input("Enter number:"))

y2=float(input("Enter number:"))

distance(x1,y1,x2,y2)
#-----------------------------------------------------------------

#task2------------------------------------------------------------
"""
Дано действительное положительное число a и целоe число n.

Вычислите an. Решение оформите в виде функции power(a, n).

"""
#
a=float(input("Enter number:"))

n=int(input("Enter number:"))

def power(a, n):

	p=1

	for i in range(n):

		p=p*a

	print("a**n:",round(p,3))

power(a,n)
#-----------------------------------------------------------------

#task2------------------------------------------------------------
"""
Дано действительное положительное число a и целоe число n.

Вычислите an. Решение оформите в виде функции power(a, n).

"""
#
a=float(input("Enter number:"))

n=int(input("Enter number:"))

def power(a, n):

	p=1

	for i in range(n):

		p=p*a

	print("a**n:",round(p,3))

power(a,n)
#-----------------------------------------------------------------

#task3------------------------------------------------------------
"""
Дано действительное положительное число a и целое неотрицательное число n. Вычислите an не используя циклы, возведение в степень через ** и функцию math.pow(), а используя рекуррентное соотношение an=a?an-1.
"""
#
a=float(input("Enter number:"))

while a<0:

	if a<0:

		print("incorrect input,try again...")

	a=float(input("Enter number:"))

n=int(input("Enter number:"))

while n<0:

	if n<0:

		print("incorrect input,try again...")

	n=int(input("Enter number:"))

def power(a, n):

	if n==0:

		return 1

	else:

		return a*power(a,n-1)

p=power(a,n)

print(round(p,3))
#-----------------------------------------------------------------

#task4------------------------------------------------------------
"""
Напишите функцию fib(n), которая по данному целому неотрицательному n возвращает n-e число Фибоначчи. В этой задаче нельзя использовать циклы — используйте рекурсию.

"""
#
n=int(input("Enter number:"))

def fib(n):

	if n==1 or n==0:

		return 1

	return fib(n-1)+fib(n-2)

print(fib(n))
#-----------------------------------------------------------------