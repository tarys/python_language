#task1------------------------------------------------------------
"""
Даны четыре действительных числа: x1, y1, x2, y2. Напишите функцию distance(x1, y1, x2, y2), вычисляющая расстояние между точкой (x1,y1) и (x2,y2). 
Считайте четыре действительных числа и выведите результат работы этой функции.
"""

from math import sqrt 

x1 = int(input('Please enter x1 coordinate '))
y1 = int(input('Please enter y1 coordinate '))
x2 = int(input('Please enter x2 coordinate '))
y2 = int(input('Please enter y2 coordinate '))


def distance(x1, y1, x2, y2):
	result = 0 #distanse between x and y , result of function distance
	result = sqrt((x1 - x2)**2 + (y1 - y2) ** 2)
	return result

result = distance(x1, y1, x2, y2)
print('Distance between x and y = ', result)	


#-----------------------------------------------------------------

#task2------------------------------------------------------------
"""
Дано действительное положительное число a и целоe число n.
Вычислите an. Решение оформите в виде функции power(a, n).
Стандартной функцией возведения в степень пользоваться нельзя.
"""

a = int(input('Enter a '))
n = int(input('Enter n '))


def power(a, n):
	result = 1
	for i in range(abs(n)):
			result *= a	
	if n < 0:
		result = 1/result
	return result

result = power(a, n)
print('Number ', a, 'in power', n, ' = ', result)

#-----------------------------------------------------------------

#task3------------------------------------------------------------
"""
Дано действительное положительное число a и целое неотрицательное число n. 
Вычислите an не используя циклы, возведение в степень через ** и функцию math.pow(), а используя рекуррентное соотношение an=a⋅an-1.
Решение оформите в виде функции power(a, n).
"""

a = int(input('Enter a '))
n = int(input('Enter n '))
if n < 0:
	print('invalid')
	exit(0)


def power(a, n):
	if n != 1:
		return a * power(a, n - 1)
	else: 
		return a	

result = power(a, n)
print('Number ', a, 'in power', n, ' = ', result)

#-----------------------------------------------------------------

#task4------------------------------------------------------------
"""
Напишите функцию fib(n), которая по данному целому неотрицательному n возвращает n-e число Фибоначчи. 
В этой задаче нельзя использовать циклы — используйте рекурсию.
"""

n = int(input('Enter n '))
if n < 0:
	print('invalid')
	exit(0)

def fib(n):
	if n == 1:
		return 1
	if n == 2:
		return 1
	else:
		return fib(n - 1) + fib(n - 2)

result = fib(n)
print(n, '`st Fibonacci number = ', result)					

#-----------------------------------------------------------------

